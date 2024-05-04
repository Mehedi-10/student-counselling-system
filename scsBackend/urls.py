"""
URL configuration for scsBackend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from scs.views import (UniversityView, CollegeView, DepartmentView, FacultyMemberView,
                       StudentView, ContactView, EthnicityView, EducationalBackgroundView,
                       DissertationView, TestScoreView, AwardView, TrainingWorkshopView,
                       SkillView, WorkExperienceView, AcknowledgementFormView, ReferenceView,
                       VolunteerActivityView, LoginView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(), name='login'),
    path('universities/', UniversityView.as_view(), name='universities'),
    path('colleges/', CollegeView.as_view(), name='colleges'),
    path('departments/', DepartmentView.as_view(), name='departments'),
    path('faculty_members/', FacultyMemberView.as_view(), name='faculty_members'),
    path('students/', StudentView.as_view(), name='students'),
    path('contacts/', ContactView.as_view(), name='contacts'),
    path('ethnicities/', EthnicityView.as_view(), name='ethnicities'),
    path('educational_backgrounds/', EducationalBackgroundView.as_view(), name='educational_backgrounds'),
    path('dissertations/', DissertationView.as_view(), name='dissertations'),
    path('test_scores/', TestScoreView.as_view(), name='test_scores'),
    path('awards/', AwardView.as_view(), name='awards'),
    path('training_workshops/', TrainingWorkshopView.as_view(), name='training_workshops'),
    path('skills/', SkillView.as_view(), name='skills'),
    path('work_experiences/', WorkExperienceView.as_view(), name='work_experiences'),
    path('acknowledgement_forms/', AcknowledgementFormView.as_view(), name='acknowledgement_forms'),
    path('references/', ReferenceView.as_view(), name='references'),
    path('volunteer_activities/', VolunteerActivityView.as_view(), name='volunteer_activities'),
]
