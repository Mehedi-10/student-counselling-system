from rest_framework import serializers
from .scs_models.admin_controlled_models import *
from .models import User
from .scs_models.student_profile_models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'is_student', 'is_teacher']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
            is_student=validated_data.get('is_student', False),
            is_teacher=validated_data.get('is_teacher', False)
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = ['id', 'name', 'web_address', 'country', 'state', 'statement', 'status']


class CollegeSerializer(serializers.ModelSerializer):
    class Meta:
        model = College
        fields = ['id', 'name', 'university', 'web_address', 'address', 'statement', 'status']


class CampusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campus
        fields = ['id', 'name', 'web_address', 'country', 'state', 'city', 'statement', 'status']


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'name', 'college', 'campus', 'web_address', 'address', 'statement', 'status']


class FacultyMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = FacultyMember
        fields = ['id', 'name', 'email', 'department', 'campus', 'college', 'web_address', 'address', 'statement',
                  'faculty_type', 'status']


class FundingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funding
        fields = ['id', 'name', 'start_date', 'end_date', 'funding_type', 'number_of_positions', 'department', 'campus',
                  'college', 'statement', 'status']

class DocumentInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentInformation
        fields = '__all__'

class BiographicInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = BiographicInformation
        fields = '__all__'

class ContactInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInformation
        fields = '__all__'

class CitizenInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CitizenInformation
        fields = '__all__'

class EthnicitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Ethnicity
        fields = '__all__'

class EthnicityInformationSerializer(serializers.ModelSerializer):
    ethnicities = EthnicitySerializer(many=True, read_only=True)
    class Meta:
        model = EthnicityInformation
        fields = '__all__'

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'

class OtherInformationSerializer(serializers.ModelSerializer):
    languages = LanguageSerializer(many=True, read_only=True)
    class Meta:
        model = OtherInformation
        fields = '__all__'

class ResearchInterestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResearchInterest
        fields = '__all__'

class ResearchInterestInformationSerializer(serializers.ModelSerializer):
    interests = ResearchInterestSerializer(many=True, read_only=True)
    class Meta:
        model = ResearchInterestInformation
        fields = '__all__'

class InstitutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institution
        fields = '__all__'

class AcademicRecordSerializer(serializers.ModelSerializer):
    institution = InstitutionSerializer(read_only=True)
    class Meta:
        model = AcademicRecord
        fields = '__all__'

class AcademicHistorySerializer(serializers.ModelSerializer):
    academic_records = AcademicRecordSerializer(many=True, read_only=True)
    class Meta:
        model = AcademicHistory
        fields = '__all__'

class TestScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestScore
        fields = '__all__'

class TestScoreInformationSerializer(serializers.ModelSerializer):
    test_scores = TestScoreSerializer(many=True, read_only=True)
    class Meta:
        model = TestScoreInformation
        fields = '__all__'

class AwardGrantScholarshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = AwardGrantScholarship
        fields = '__all__'

class AwardGrantScholarshipInformationSerializer(serializers.ModelSerializer):
    awards_scholarships = AwardGrantScholarshipSerializer(many=True, read_only=True)
    class Meta:
        model = AwardGrantScholarshipInformation
        fields = '__all__'

class TrainingAndWorkshopSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainingAndWorkshop
        fields = '__all__'

class TrainingAndWorkshopInformationSerializer(serializers.ModelSerializer):
    trainings_workshops = TrainingAndWorkshopSerializer(many=True, read_only=True)
    class Meta:
        model = TrainingAndWorkshopInformation
        fields = '__all__'

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'

class SkillInformationSerializer(serializers.ModelSerializer):
    skills = SkillSerializer(many=True, read_only=True)
    class Meta:
        model = SkillInformation
        fields = '__all__'

class WorkExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkExperience
        fields = '__all__'

class WorkExperienceInformationSerializer(serializers.ModelSerializer):
    work_experiences = WorkExperienceSerializer(many=True, read_only=True)
    class Meta:
        model = WorkExperienceInformation
        fields = '__all__'

class PublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = '__all__'

class PublicationInformationSerializer(serializers.ModelSerializer):
    publications = PublicationSerializer(many=True, read_only=True)
    class Meta:
        model = PublicationInformation
        fields = '__all__'

class DissertationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dissertation
        fields = '__all__'

class DissertationInformationSerializer(serializers.ModelSerializer):
    dissertations = DissertationSerializer(many=True, read_only=True)
    class Meta:
        model = DissertationInformation
        fields = '__all__'

class SocialMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMedia
        fields = '__all__'

class SocialMediaInformationSerializer(serializers.ModelSerializer):
    social_media_accounts = SocialMediaSerializer(many=True, read_only=True)
    class Meta:
        model = SocialMediaInformation
        fields = '__all__'

class VolunteerActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = VolunteerActivity
        fields = '__all__'

class VolunteerInformationSerializer(serializers.ModelSerializer):
    activities = VolunteerActivitySerializer(many=True, read_only=True)
    class Meta:
        model = VolunteerInformation
        fields = '__all__'

class ReferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reference
        fields = '__all__'

class ReferenceInformationSerializer(serializers.ModelSerializer):
    references = ReferenceSerializer(many=True, read_only=True)
    class Meta:
        model = ReferenceInformation
        fields = '__all__'
