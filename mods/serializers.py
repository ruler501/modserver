from rest_framework import serializers
from mods.models import Mod
from django.contrib.auth.models import User

class ModSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mod
        fields = ('title', 'mod', 'version', 'owner')
        read_only_fields = ('owner',)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    mods = serializers.HyperlinkedRelatedField(many=True, view_name='mod-detail', read_only=True)
    password = serializers.CharField(
        style={'input_type': 'password'}
    )
    
    def create(self, validated_data):

        user = User.objects.create(
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()

        return user
    
    class Meta:
        model = User
        fields = ('url', 'username', 'password', 'mods')
        extra_kwargs = {'password': {'write_only': True}}
