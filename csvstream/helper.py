import csv
from datetime import datetime

from .models import Order, Line_items


def helper():
    with open(r"C:\Users\DELL\Desktop\djangoprojects\task1\csvstream\csvdata\orders.csv", 'r') as file:
        reader = csv.DictReader(file)
        headers = reader.fieldnames
        for row in reader:
            print(row)
            Order.objects.create(
                OrderID=row['OrderID'],
                CustomerName=row['CustomerName'],
                OrderDate=row['OrderDate'],
                TotalAmount=row['TotalAmount'],
            )
            print(f"created successfully: {row['OrderID']}")


def line_item():
    with open(r"C:\Users\DELL\Desktop\git folder\begineer_projects\tasks\csvstream\data\line_items (1).csv",
              'r') as file:
        reader = csv.DictReader(file)
        headers = reader.fieldnames
        for row in reader:
            print(row)
            order_instance=Order.objects.get(OrderID=row['OrderID'])
            Line_items.objects.create(
                LineItemID=row['LineItemID'],
                Order=order_instance,
                ProductID=row['ProductID'],
                ProductName=row['ProductName'],
                Quantity=row['Quantity'],
                Price=row['Price'],
            )
            print(f"created successfully: {row['LineItemID']}")
