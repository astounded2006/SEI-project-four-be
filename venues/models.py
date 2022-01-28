from django.db import models

# Create your models here.
class Venue(models.Model):
    name = models.CharField(max_length=40)
    types = models.CharField(max_length=30)
    image = models.CharField(max_length=400, blank=True)
    description = models.TextField(max_length=1000)
    number = models.CharField(max_length=20, blank=True)
    expensive = models.CharField(max_length=10, blank=True)
    location = models.TextField(max_length=30)
    parking = models.CharField(max_length=50, blank=True)
    childfriendly = models.CharField(max_length=50, blank=True)
    outdoor = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f'{self.name} - {self.types}'

class Comment(models.Model):
    '''Comment Model'''
    content = models.TextField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    venue = models.ForeignKey(
        Venue,
        related_name='comments',
        on_delete=models.CASCADE
    )
    owner = models.ForeignKey(
        'jwt_auth.User',
        related_name='comments_posted',
        on_delete=models.CASCADE

    )

    def __str__(self):
        return f'Comment {self.id} on Venue {self.venue}'

class Like(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    venue = models.ForeignKey(
      Venue,
      related_name='liked_by',
      on_delete=models.CASCADE
    )
    owner = models.ForeignKey(
          'jwt_auth.User',
          related_name='liked_venue',
          on_delete=models.CASCADE
    )

    def __str__(self):
        return f'Like {self.id} on Venue {self.venue}'
        