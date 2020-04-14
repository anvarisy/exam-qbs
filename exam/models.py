from django.db import models


# Create your models here.

class Account(models.Model):
    class Meta:
        permissions = [('teacher_access', 'Access page for teacher'),
                       ('student_access', 'Access page for student'),
                       ('admin_access', 'Access page for admin')]
