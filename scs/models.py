from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


# Enums
class Status(models.TextChoices):
    ACTIVE = 'Active', _('Active')
    INACTIVE = 'Inactive', _('Inactive')


class MilitaryStatus(models.TextChoices):
    ACTIVE = 'active', _('Active')
    VETERAN = 'veteran', _('Veteran')
    NONE = 'none', _('None')


class CitizenshipStatus(models.TextChoices):
    CITIZEN = 'citizen', _('Citizen')
    NON_CITIZEN = 'non-citizen', _('Non-Citizen')
    PERMANENT_RESIDENT = 'permanent resident', _('Permanent Resident')


# Models
class University(models.Model):
    name = models.CharField(max_length=255)
    web_address = models.URLField()
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    statement = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.ACTIVE)


class College(models.Model):
    name = models.CharField(max_length=255)
    university = models.ForeignKey(University, on_delete=models.SET_NULL, null=True)
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
    college = models.ForeignKey(College, on_delete=models.SET_NULL, null=True)
    campus = models.ForeignKey(Campus, on_delete=models.SET_NULL, null=True)
    web_address = models.URLField()
    address = models.TextField(blank=True, null=True)
    statement = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.ACTIVE)


class FacultyMember(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    campus = models.ForeignKey(Campus, on_delete=models.SET_NULL, null=True)
    college = models.ForeignKey(College, on_delete=models.SET_NULL, null=True)
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


# User model customized for Students
class Student(models.Model):
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    date_of_birth = models.DateField()
    city_of_birth = models.CharField(max_length=100)
    country_of_birth = models.CharField(max_length=100)
    first_language = models.CharField(max_length=50)
    military_status = models.CharField(max_length=20, choices=MilitaryStatus.choices)
    military_serving_status = models.BooleanField(default=False)
    parental_college_graduation_status = models.BooleanField(default=False)
    hispanic_latino_origin = models.BooleanField(default=False)
    us_citizenship_status = models.CharField(max_length=50, choices=CitizenshipStatus.choices)
    country_of_citizenship = models.CharField(max_length=100)
    dual_citizenship = models.BooleanField(default=False)
    legal_state_of_residence = models.CharField(max_length=100)
    us_visa_status = models.BooleanField(default=False)
    current_address_line1 = models.CharField(max_length=255)
    current_address_line2 = models.CharField(max_length=255, blank=True, null=True)
    current_city = models.CharField(max_length=100)
    current_state_province = models.CharField(max_length=100)
    current_postal_code = models.CharField(max_length=20)
    current_country = models.CharField(max_length=100)
    permanent_address_status = models.BooleanField(default=False)


# Contact Model
class Contact(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)


# Ethnicity Model
class Ethnicity(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    ethnicity = models.CharField(max_length=50)


# Educational Background Model
class EducationalBackground(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    currently_enrolled = models.BooleanField(default=False)
    previously_applied = models.BooleanField(default=False)
    institution_name = models.CharField(max_length=255)
    institution_address = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    degree_expected = models.CharField(max_length=100)
    degree_date = models.DateField(null=True, blank=True)
    major = models.CharField(max_length=100)


# Dissertation Model
class Dissertation(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    academic_level = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    abstract = models.TextField()
    publications = models.TextField(blank=True, null=True)
    full_dissertation_link = models.URLField()


# Test Scores Model
class TestScore(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    test_name = models.CharField(max_length=100)
    score = models.CharField(max_length=50)
    date_taken = models.DateField()
    percentile = models.CharField(max_length=50)


# Awards, Grants, Scholarships Model
class Award(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    awarding_organization = models.CharField(max_length=255)
    date_received = models.DateField()
    monetary_value = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()


# Training Workshops Model
class TrainingWorkshop(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    organizer = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    duration = models.CharField(max_length=100)
    completion_date = models.DateField()
    certificate = models.TextField()


# Skills Model
class Skill(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=100)
    proficiency_level = models.CharField(max_length=50)
    years_experience = models.IntegerField()


# Work Experience Model
class WorkExperience(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    position_title = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description_of_duties = models.TextField()


# Acknowledgement Form Model
class AcknowledgementForm(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    content = models.TextField()
    is_acknowledged = models.BooleanField(default=False)


# References Model
class Reference(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100)
    organization_name = models.CharField(max_length=255)
    designation = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=20)
    email_address = models.EmailField()
    relationship = models.CharField(max_length=100)


# Volunteer Activities Model
class VolunteerActivity(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    organization_name = models.CharField(max_length=255)
    designation = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    role_description = models.TextField()
