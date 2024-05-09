from django.db import models
from django.utils.translation import gettext_lazy as _

class Status(models.TextChoices):
    ACTIVE = 'Active', _('Active')
    INACTIVE = 'Inactive', _('Inactive')


class University(models.Model):
    name = models.CharField(max_length=255)
    web_address = models.URLField()
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    statement = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.ACTIVE)


class College(models.Model):
    name = models.CharField(max_length=255)
    university = models.ForeignKey(University, on_delete=models.SET_NULL, null=True, related_name='colleges')
    web_address = models.URLField()
    address = models.TextField(blank=True, null=True)
    statement = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.ACTIVE)


class Campus(models.Model):
    name = models.CharField(max_length=255)
    web_address = models.URLField()
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    statement = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.ACTIVE)


class Department(models.Model):
    name = models.CharField(max_length=255)
    college = models.ForeignKey(College, on_delete=models.SET_NULL, null=True, related_name='departments')
    campus = models.ForeignKey(Campus, on_delete=models.SET_NULL, null=True, related_name='departments')
    web_address = models.URLField()
    address = models.TextField(blank=True, null=True)
    statement = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.ACTIVE)


class FacultyMember(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, related_name='faculty_members')
    campus = models.ForeignKey(Campus, on_delete=models.SET_NULL, null=True, related_name='faculty_members')
    college = models.ForeignKey(College, on_delete=models.SET_NULL, null=True, related_name='faculty_members')
    web_address = models.URLField()
    address = models.TextField(blank=True, null=True)
    statement = models.TextField(blank=True, null=True)
    faculty_type = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.ACTIVE)


class Funding(models.Model):
    name = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    funding_type = models.CharField(max_length=100)
    number_of_positions = models.IntegerField()
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    campus = models.ForeignKey(Campus, on_delete=models.SET_NULL, null=True)
    college = models.ForeignKey(College, on_delete=models.SET_NULL, null=True)
    statement = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.ACTIVE)