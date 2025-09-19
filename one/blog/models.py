from django.db import models





class Product(models.Model):
    title = models.CharField(max_length=20)
    Description = models.TextField()
    numberOfProduct = models.IntegerField()
    price = models.DecimalField(decimal_places=2, max_digits=5)
    AddToCart = models.BooleanField(default=False)

    def __str__(self):
        return self.title