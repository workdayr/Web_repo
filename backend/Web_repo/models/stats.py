from django.db import models

class NotificationLog(models.Model):
    STATUS_CHOICES = [
        ('on_time', 'On Time'),
        ('late', 'Late'),
        ('missed', 'Missed'),
    ]
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

class RedirectAnalytics(models.Model):
    platform_name = models.CharField(max_length=100)
    redirect_count = models.IntegerField()
    date = models.DateField()

    def __str__(self):
        return self.platform_name
    

class UserRecord(models.Model):
    LOGIN_CHOICES=[
        ('Google', 'Google'),
        ('Facebook', 'Facebook'),
        ('Email', 'Email'),
        ('Apple', 'Apple'),
    ]

    STATUS_CHOICES = [
        ('Online', 'Online'),
        ('Offline', 'Offline'),
    ]

    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    country = models.CharField(max_length=50)
    login_type = models.CharField(max_length=20, choices=LOGIN_CHOICES)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name