from django.urls import path
from .views import (
  VenueListView,
  VenueDetailView,
  CommentListView,
  CommentDetailView,
  LikeListView,
  LikeDetailView,
)

urlpatterns = [
    path('', VenueListView.as_view()),
    path('<int:pk>/', VenueDetailView.as_view()),
    path('<int:pk>/comments/', CommentListView.as_view()),
    path('<int:venue_pk>/comments/<int:pk>/', CommentDetailView.as_view()),
    path('<int:pk>/likes/', LikeListView.as_view()),
    path('<int:venue_pk>/likes/<int:pk>/', LikeDetailView.as_view())
]
