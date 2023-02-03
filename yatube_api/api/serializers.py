
from rest_framework import serializers
from posts.models import Post, Group, Comment, User

class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    class Meta:
        fields = ('id', 'author', 'text', 'image', 'pub_date', 'group',)
        read_only_fields = ('author', 'group',)
        model = Post

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title', 'slug', 'description',)
        model = Group

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    class Meta:
        fields = ('id', 'author', 'post', 'text', 'created',)
        model = Comment
        read_only_fields = ('author', 'post',)

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('id', 'username',)
        ref_name = 'ReadOnlyUsers'