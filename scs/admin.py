from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from scs.scs_models.admin_controlled_models import *
from scs.scs_models.student_profile_models import *
from scs.models import *

admin.site.register(User, UserAdmin)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(DocumentInformation)
admin.site.register(BiographicInformation)
admin.site.register(ContactInformation)
admin.site.register(CitizenInformation)
admin.site.register(Ethnicity)
admin.site.register(EthnicityInformation)
admin.site.register(Language)
admin.site.register(OtherInformation)
admin.site.register(ResearchInterest)
admin.site.register(ResearchInterestInformation)
admin.site.register(Institution)
admin.site.register(AcademicRecord)
admin.site.register(AcademicHistory)
admin.site.register(TestScore)
admin.site.register(TestScoreInformation)
admin.site.register(AwardGrantScholarship)
admin.site.register(AwardGrantScholarshipInformation)
admin.site.register(TrainingAndWorkshop)
admin.site.register(TrainingAndWorkshopInformation)
admin.site.register(Skill)
admin.site.register(SkillInformation)
admin.site.register(WorkExperience)
admin.site.register(WorkExperienceInformation)
admin.site.register(Publication)
admin.site.register(PublicationInformation)
admin.site.register(Dissertation)
admin.site.register(DissertationInformation)


admin.site.register(University)
admin.site.register(College)
admin.site.register(Campus)
admin.site.register(Department)
admin.site.register(FacultyMember)
admin.site.register(Funding)
