from mods.models import Mod
from django.contrib.auth.models import User
from mods.serializers import ModSerializer
from mods.serializers import UserSerializer
from rest_framework import generics
from rest_framework import permissions
from mods.permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework import permissions
from rest_framework.generics import CreateAPIView


class CreateUserView(CreateAPIView):

    model = User
    permissin_classes = [
        permissions.AllowAny # Or anon users can't register
    ]
    serializer_class = UserSerializer
    
class ModViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Mod.objects.all()
    serializer_class = ModSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)
                          
    def pre_save(self,obj):
        if(self.request.FILES.get('file').content_type == 'application/zip'):
            obj.mod = self.request.FILES.get('file')

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

@api_view(['POST'])
def create_auth(request):
    serialized = UserSerializer(data=request.DATA)
    if serialized.is_valid():
        User.objects.create_user(
            serialized.init_data['email'],
            serialized.init_data['username'],
            serialized.init_data['password']
        )
        return Response(serialized.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)
