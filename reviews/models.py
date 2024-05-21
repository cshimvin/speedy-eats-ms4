from django.db import models
from django.contrib.auth.models import User


class Review(models.Model):
    review_title = models.CharField(max_length=254, null=False, blank=False)
    review_body = models.TextField(null=False, blank=False)
    rating = models.DecimalField(null=False, blank=False)
    review_date = models.DateTimeField(auto_now_add=True)
    reviewer = models.ForeignKey(
        User, related_name='reviews', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
