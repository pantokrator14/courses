from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    start_date = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

class Lesson(models.Model):
    product = models.ForeignKey(Product, related_name='lessons', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    video_link = models.URLField()

class UserBalance(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=1000.00)

    def save(self, *args, **kwargs):
        if self.balance < 0:
            raise ValueError("Balance cannot be less than zero.")
        super().save(*args, **kwargs)