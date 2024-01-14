# schoolapp/models.py

from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=255)
    wikipedia_link = models.URLField()

    def __str__(self):
        return self.name

class Course(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Material(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Order(models.Model):
    name = models.CharField(max_length=255)
    dob = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=15)
    mail_id = models.EmailField()
    address = models.TextField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    purpose = models.CharField(max_length=20)
    materials_provide = models.ManyToManyField(Material)

    PURPOSE_CHOICES = [
        ('ForEnquiry', 'For Enquiry'),
        ('PlaceOrder', 'Place Order'),
        ('Return', 'Return'),
        # Add more choices as needed
    ]

    purpose = models.CharField(max_length=20, choices=PURPOSE_CHOICES)

    # ... other fields ...

    def __str__(self):
        return self.name
