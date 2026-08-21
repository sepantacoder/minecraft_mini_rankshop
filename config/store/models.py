from django.db import models


class Rank(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.PositiveIntegerField()
    image = models.ImageField(upload_to="ranks/", blank=True)
    published = models.BooleanField(default=True)

    def __str__(self):
        return self.name
class Order(models.Model):
    rank = models.ForeignKey(Rank, on_delete=models.CASCADE)
    username = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=15)
    amount = models.PositiveIntegerField()
    commission = models.PositiveIntegerField(default=0)
    paid = models.BooleanField(default=False)
    authority = models.CharField(max_length=100, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.username} - {self.rank.name}"