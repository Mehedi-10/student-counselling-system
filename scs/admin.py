from django.contrib import admin
from .models import (University, College, Campus, Department, FacultyMember, Funding,
                     Student, Contact, Ethnicity, EducationalBackground, Dissertation,
                     TestScore, Award, TrainingWorkshop, Skill, WorkExperience, AcknowledgementForm,
                     Reference, VolunteerActivity)

# Register your models here.
admin.site.register(University)
admin.site.register(College)
admin.site.register(Campus)
admin.site.register(Department)
admin.site.register(FacultyMember)
admin.site.register(Funding)
admin.site.register(Student)
admin.site.register(Contact)
admin.site.register(Ethnicity)
admin.site.register(EducationalBackground)
admin.site.register(Dissertation)
admin.site.register(TestScore)
admin.site.register(Award)
admin.site.register(TrainingWorkshop)
admin.site.register(Skill)
admin.site.register(WorkExperience)
admin.site.register(AcknowledgementForm)
admin.site.register(Reference)
admin.site.register(VolunteerActivity)
