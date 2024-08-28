
from django.db import models

class Order(models.Model):

    OrderID = models.AutoField(primary_key=True)
    CustomerName = models.CharField(max_length=50)
    OrderDate = models.DateField()
    TotalAmount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.CustomerName

class Line_items(models.Model):
    LineItemID = models.AutoField(primary_key=True)
    Order = models.ForeignKey(Order, on_delete=models.CASCADE,null=True)
    ProductID = models.IntegerField()
    ProductName = models.CharField(max_length=50)
    Quantity = models.IntegerField()
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.ProductName