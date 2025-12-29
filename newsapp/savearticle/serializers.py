from rest_framework import serializers
from .models import SaveArticle
class SavearticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaveArticle
        fields = ['id','article','user']
