from rest_framework import serializers
from django.contrib.auth import get_user_model
import django.contrib.auth.password_validation as validation
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from django.conf import settings

from venues.models import Venue, Like, Comment


User = get_user_model()

class UserRegistrationSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)
    password_confirmation = serializers.CharField(write_only=True)

    def validate(self, attrs):
        password = attrs.pop('password')
        password_confirmation = attrs.pop('password_confirmation')

        if password != password_confirmation:
            raise ValidationError({'detail':'Password and Confirmation do not match'})

        if settings.ENV != 'DEV':
            try:
                validation.validate_password(password=password)
            except ValidationError as err:
                raise ValidationError({'password':err})

        attrs['password'] = make_password(password)

        return attrs

    class Meta:
        model = User
        fields = '__all__'

class NestedVenueSerializer(serializers.ModelSerializer):

    class Meta:
        model = Venue
        fields = ('id', 'name', 'types', 'image', 'description', 'number', 'expensive', 'location')

class NestedLikeSerializer(serializers.ModelSerializer):
    venue = NestedVenueSerializer()

    class Meta:
        model = Like
        fields = '__all__'

class NestedCommentSerializer(serializers.ModelSerializer):
    venue = NestedVenueSerializer()

    class Meta:
        model = Comment
        fields = '__all__'

class UserProfileSerializer(serializers.ModelSerializer):

    liked_venue = NestedLikeSerializer(many=True)
    comments_posted = NestedCommentSerializer(many=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'profile_image', 'liked_venue', 'comments_posted')
