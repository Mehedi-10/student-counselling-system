from django.core.validators import FileExtensionValidator
from django.db import models

from scs.models import User


class DocumentInformation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    resume = models.FileField(
        upload_to='resumes/',
        validators=[FileExtensionValidator(['pdf', 'docx'])],
        blank=True,
        null=True
    )
    sop = models.FileField(
        upload_to='sops/',
        validators=[FileExtensionValidator(['pdf', 'docx'])],
        blank=True,
        null=True
    )

    def __str__(self):
        return f"Resume: {self.resume.name if self.resume else 'No File'} - SOP: {self.sop.name if self.sop else 'No File'}"


class BiographicInformation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    middle_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    city_of_birth = models.CharField(max_length=100, null=True, blank=True)
    country_of_birth = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        full_name = f"{self.first_name or ''} {self.middle_name or ''} {self.last_name or ''}".strip()
        return full_name


class ContactInformation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address_line_1 = models.CharField(max_length=255, null=True, blank=True)
    address_line_2 = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state_province = models.CharField(max_length=100, null=True, blank=True)
    postal_code = models.CharField(max_length=20, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    is_permanent_address = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return f"{self.address_line_1}, {self.city}, {self.state_province} - Permanent: {self.is_permanent_address}"


class CitizenInformation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    us_citizenship_status = models.CharField(max_length=100, null=True, blank=True)
    country_of_citizenship = models.CharField(max_length=100, null=True, blank=True)
    dual_citizenship = models.BooleanField(default=False, blank=True)
    legal_state_of_residence = models.CharField(max_length=100, null=True, blank=True)
    has_us_visa = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return f"{self.us_citizenship_status} - {self.country_of_citizenship}"


class Ethnicity(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


class EthnicityInformation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    hispanic_latino_origin = models.BooleanField(default=False, blank=True)
    ethnicities = models.ManyToManyField(Ethnicity, blank=True)

    def __str__(self):
        ethnicities = ', '.join([ethnicity.name for ethnicity in self.ethnicities.all()])
        return f"Hispanic/Latino: {'Yes' if self.hispanic_latino_origin else 'No'} - Ethnicities: {ethnicities if ethnicities else 'None'}"


class Language(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


class OtherInformation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    languages = models.ManyToManyField(Language, blank=True)
    us_military_status = models.CharField(max_length=255, null=True, blank=True)
    is_currently_serving = models.BooleanField(default=False, blank=True)
    parent_college_graduate = models.BooleanField(default=False, blank=True)

    def __str__(self):
        languages = ', '.join([language.name for language in self.languages.all()])
        serving_status = 'Currently Serving' if self.is_currently_serving else 'Not Serving'
        parent_status = 'Parent is a College Graduate' if self.parent_college_graduate else 'Parent is not a College Graduate'
        return f"Languages: {languages if languages else 'None'} - Military Status: {self.us_military_status} - {serving_status}, {parent_status}"


class ResearchInterest(models.Model):
    topic = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.topic


class ResearchInterestInformation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    interests = models.ManyToManyField(ResearchInterest, blank=True)

    def __str__(self):
        interests = ', '.join([interest.topic for interest in self.interests.all()])
        return f"Research Interests: {interests if interests else 'None'}"


class Institution(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name


class AcademicRecord(models.Model):
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    degree_earned_or_expected = models.CharField(max_length=255, null=True, blank=True)
    major = models.CharField(max_length=255, null=True, blank=True)
    degree_date_or_expected = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.institution.name} - {self.major} ({self.degree_earned_or_expected})"


class AcademicHistory(models.Model):
    is_currently_enrolled = models.BooleanField(default=False)
    has_applied_before = models.BooleanField(default=False)
    academic_records = models.ManyToManyField(AcademicRecord, blank=True)

    def __str__(self):
        return f"Currently Enrolled: {'Yes' if self.is_currently_enrolled else 'No'} - Applied Before: {'Yes' if self.has_applied_before else 'No'}"


class TestScore(models.Model):
    test_name = models.CharField(max_length=255, null=True, blank=True)
    score = models.CharField(max_length=100, null=True,
                             blank=True)  # Depending on score format, you might want CharField or DecimalField
    date_taken = models.DateField(null=True, blank=True)
    percentile = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)  # Store as a percentage

    def __str__(self):
        return f"{self.test_name}: Score {self.score}, Percentile {self.percentile}%" if self.test_name else "Test Score Information"


class TestScoreInformation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    test_scores = models.ManyToManyField(TestScore, blank=True)

    def __str__(self):
        return ', '.join(
            [str(score) for score in self.test_scores.all()]) if self.test_scores.all() else "No Test Scores"


class AwardGrantScholarship(models.Model):
    name_of_award_grant_scholarship = models.CharField(max_length=255, null=True, blank=True)
    awarding_organization = models.CharField(max_length=255, null=True, blank=True)
    date_received = models.DateField(null=True, blank=True)
    monetary_value = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    description_reason_for_award = models.TextField(null=True, blank=True)

    def __str__(self):
        return (f"{self.name_of_award_grant_scholarship} - {self.awarding_organization}"
                if self.name_of_award_grant_scholarship and self.awarding_organization
                else "Award/Grant/Scholarship Information")


class AwardGrantScholarshipInformation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    awards_scholarships = models.ManyToManyField(AwardGrantScholarship, blank=True)

    def __str__(self):
        return (', '.join([str(award) for award in self.awards_scholarships.all()])
                if self.awards_scholarships.all()
                else "No Awards/Grants/Scholarships")


class TrainingAndWorkshop(models.Model):
    name_of_training_workshop = models.CharField(max_length=255, null=True, blank=True)
    organizer = models.CharField(max_length=255, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    duration = models.CharField(max_length=100, null=True, blank=True)
    completion_date = models.DateField(null=True, blank=True)
    certificate = models.FileField(
        upload_to='certificates/',
        validators=[FileExtensionValidator(['pdf', 'jpg', 'jpeg', 'png'])],
        null=True,
        blank=True
    )

    def __str__(self):
        return (f"{self.name_of_training_workshop} - Organized by {self.organizer}"
                if self.name_of_training_workshop and self.organizer
                else "Training and Workshop Information")


class TrainingAndWorkshopInformation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    trainings_workshops = models.ManyToManyField(TrainingAndWorkshop, blank=True)

    def __str__(self):
        return (', '.join([str(training) for training in self.trainings_workshops.all()])
                if self.trainings_workshops.all()
                else "No Trainings/Workshops")


class Skill(models.Model):
    skill_name = models.CharField(max_length=255, null=True, blank=True)
    proficiency_level = models.CharField(max_length=100, null=True, blank=True)
    years_of_experience = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return (f"{self.skill_name} - {self.proficiency_level} ({self.years_of_experience} years)"
                if self.skill_name
                else "Skill Information")


class SkillInformation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    skills = models.ManyToManyField(Skill, blank=True)

    def __str__(self):
        return (', '.join([str(skill) for skill in self.skills.all()])
                if self.skills.all()
                else "No Skills")


class WorkExperience(models.Model):
    position_title = models.CharField(max_length=255, null=True, blank=True)
    company_organization_name = models.CharField(max_length=255, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    description_of_duties = models.TextField(null=True, blank=True)

    def __str__(self):
        return (f"{self.position_title} at {self.company_organization_name}"
                if self.position_title and self.company_organization_name
                else "Work Experience Information")


class WorkExperienceInformation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    work_experiences = models.ManyToManyField(WorkExperience, blank=True)

    def __str__(self):
        return (', '.join([str(experience) for experience in self.work_experiences.all()])
                if self.work_experiences.all()
                else "No Work Experiences")


class Publication(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    authors = models.CharField(max_length=255, null=True, blank=True)
    publication_date = models.DateField(null=True, blank=True)
    journal_or_conference_name = models.CharField(max_length=255, null=True, blank=True)
    doi_or_url = models.URLField(null=True, blank=True)
    abstract = models.TextField(null=True, blank=True)

    def __str__(self):
        return (f"{self.title} by {self.authors}"
                if self.title and self.authors
                else "Publication Information")


class PublicationInformation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    publications = models.ManyToManyField(Publication, blank=True)

    def __str__(self):
        return (', '.join([str(publication) for publication in self.publications.all()])
                if self.publications.all()
                else "No Publications")


class Dissertation(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    academic_level = models.CharField(max_length=100, null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    abstract = models.TextField(null=True, blank=True)
    publications = models.TextField(null=True, blank=True)
    link_to_full_dissertation = models.URLField(null=True, blank=True)

    def __str__(self):
        return (f"{self.title} ({self.academic_level})"
                if self.title
                else "Dissertation Information")


class DissertationInformation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dissertations = models.ManyToManyField(Dissertation, blank=True)

    def __str__(self):
        return (', '.join([str(dissertation) for dissertation in self.dissertations.all()])
                if self.dissertations.all()
                else "No Dissertations")


class SocialMedia(models.Model):
    platform_name = models.CharField(max_length=100, null=True, blank=True)
    url = models.URLField(null=True, blank=True)

    def __str__(self):
        return f"{self.platform_name}: {self.url}" if self.platform_name else "Social Media Entry"


class SocialMediaInformation(models.Model):
    social_media_accounts = models.ManyToManyField(SocialMedia, blank=True)

    def __str__(self):
        return ', '.join([str(account) for account in
                          self.social_media_accounts.all()]) if self.social_media_accounts.all() else "No Social Media Information"


class VolunteerActivity(models.Model):
    name_of_organization = models.CharField(max_length=255, null=True, blank=True)
    designation = models.CharField(max_length=255, null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    role_description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.name_of_organization} - {self.designation}" if self.name_of_organization and self.designation else "Volunteer Activity"


class VolunteerInformation(models.Model):
    activities = models.ManyToManyField(VolunteerActivity, blank=True)

    def __str__(self):
        return ', '.join([str(activity) for activity in
                          self.activities.all()]) if self.activities.all() else "No Volunteer Activities"


class Reference(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    middle_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    name_of_organization = models.CharField(max_length=255, null=True, blank=True)
    designation = models.CharField(max_length=255, null=True, blank=True)
    contact_number = models.CharField(max_length=20, null=True, blank=True)
    email_address = models.EmailField(null=True, blank=True)
    relationship = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.title} {self.first_name} {self.last_name} - {self.relationship}"


class ReferenceInformation(models.Model):
    references = models.ManyToManyField(Reference, blank=True)

    def __str__(self):
        return ', '.join(
            [str(reference) for reference in self.references.all()]) if self.references.all() else "No References"
