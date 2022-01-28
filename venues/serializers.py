from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Like, Venue, Comment
User = get_user_model()

class NestedUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        field = ('id', 'username', 'profile_image')

class CommentSerializer(serializers.ModelSerializer):
    '''Serializer for Comments'''

    class Meta:
        model = Comment
        fields = '__all__'

class NestedCommentSerializer(serializers.ModelSerializer):
    '''Serializer for Nested Comments'''
    owner = NestedUserSerializer()

    class Meta:
        model = Comment
        fields = '__all__'

class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Like
        fields = '__all__'

class NestedLikeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Like
        fields = '__all__'


class VenueSerializer(serializers.ModelSerializer):
    '''Serialaizer for outgoing pokemon response'''
    comments = NestedCommentSerializer(many=True, read_only=True)
    liked_by = NestedLikeSerializer(many=True, read_only=True)

    class Meta:
        model = Venue
        fields = '__all__'
