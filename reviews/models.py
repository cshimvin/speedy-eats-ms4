from django.db import models


class Review(models.Model):
    review_title = models.CharField(max_length=254, null=False, blank=False)
    review_body = models.TextField(null=False, blank=False)
    rating = models.DecimalField(null=False, decimal_places=0,
                                 max_digits=1, blank=False)
    review_date = models.DateTimeField(auto_now_add=True),
    reviewer_name = models.CharField(max_length=254, null=False, blank=False)

    def __str__(self):
        return self.name
