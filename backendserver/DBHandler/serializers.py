from rest_framework import serializers
from DBHandler.models import GameUserData

class GameUserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameUserData
        fields = ('Id', 'UserName','GameName','DateTime','Values',)