from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Venue, Comment
User = get_user_model()

class NestedUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        field = ('id', 'username')

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

class VenueSerializer(serializers.ModelSerializer):
    '''Serialaizer for outgoing pokemon response'''
    comments = NestedCommentSerializer(many=True, read_only=True)

    class Meta:
        model = Venue
        fields = '__all__'
