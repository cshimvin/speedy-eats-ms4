from django.db import models


class Driver(models.Model):
    """
    Delivery Driver model containing personal details
    """
    staff_number = models.CharField(max_length=10, null=False, blank=False)
    first_name = models.CharField(max_length=254, null=False, blank=False)
    last_name = models.CharField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=15, null=False, blank=False)
    vehicle_type = models.CharField(max_length=254, null=False, blank=False)
    vehicle_reg_number = models.CharField(max_length=20, null=False,
                                          blank=False)

    def __str__(self):
        return self.staff_number
