from django.db import models

class Register(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(primary_key=True)
    password = models.CharField(max_length=100)
    phonenumber = models.CharField(max_length=20)

    class Meta:
        db_table = "register"  # Use lowercase table names for consistency

    def __str__(self):
        return self.name  # Provide a string representation for better readability

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    feedback = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Donation(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()
    message = models.TextField()
    donation_amount = models.DecimalField(max_digits=10, decimal_places=2)
    donation_frequency = models.CharField(max_length=20, choices=[
        ('once', 'Once'),
        ('monthly', 'Monthly'),
        ('yearly', 'Yearly')
    ])

    class Meta:
        verbose_name = "Donation"  # Provide a human-readable name for the model
        verbose_name_plural = "Donations"  # Provide a plural name for consistency

    def __str__(self):
        return self.name  # Provide a string representation for better readability


class DonationCard(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "DonationCard"

    def __str__(self):
        return self.title

from django.db import models

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.name
