from django.db import models

# Create your models here.

class Farmer(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    
    CONTRACT_CHOICES = [
        ('casual', 'Casual'),
        ('contract', 'Contract'),
    ]
    
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    farm = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')
    contract_type = models.CharField(max_length=10, choices=CONTRACT_CHOICES, default='casual')
    password = models.CharField(max_length=100, default="farmer12345")

    class Meta:
        db_table = 'farmer'
        ordering = ['name']


    def __str__(self):
        return self.name

class Attendance(models.Model):
    date = models.DateField()
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    is_present = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.farmer.name} - {self.date} - {'Present' if self.is_present else 'Absent'}"

    class Meta:
        db_table = 'attendance_attendance'
        ordering = ['-date']
