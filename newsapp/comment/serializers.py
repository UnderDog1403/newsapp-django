from rest_framework import serializers
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Comment
        fields = ['id','comment','user','article']
class CommentCreateUpdateSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(write_only=True)
    article_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = Comment
        fields = ['comment', 'user_id', 'article_id']
