from rest_framework.generics import (
  ListCreateAPIView,
  RetrieveUpdateDestroyAPIView,
  CreateAPIView,
  DestroyAPIView
)
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsOwnerOrReadOnly

from .models import Venue, Comment
from .serializers import VenueSerializer, CommentSerializer

class VenueListView(ListCreateAPIView):
    queryset = Venue.objects.all().order_by('number')
    serializer_class = VenueSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

class VenueDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Venue.objects.all()
    serializer_class = VenueSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

class CommentListView(CreateAPIView):
    '''View for /venues/id/comments POST'''
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

class CommentDetailView(DestroyAPIView):
    '''View for /venues/id/comments/commentId DELETE'''

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsOwnerOrReadOnly, )
