from rest_framework import serializers
from mods.models import Mod
from django.contrib.auth.models import User

class ModSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mod
        fields = ('title', 'mod', 'owner')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'username', 'snippets')
