from django.http import JsonResponse, HttpResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import Student, University, College, Department, FacultyMember, Reference, VolunteerActivity, \
    AcknowledgementForm, WorkExperience, Skill, TrainingWorkshop, Award, TestScore, Dissertation, EducationalBackground, \
    Ethnicity, Contact

import json


def parse_json(request):
    try:
        return json.loads(request.body)
    except json.JSONDecodeError:
        return None

@method_decorator(csrf_exempt, name='dispatch')
class LoginView(View):
    def post(self, request):
        data = json.loads(request.body)
        email = data.get('email')
        password = data.get('password')
        if email=="teacher@gmail.com" or email=="student@gmail.com":
            request.session['user_type']=email.split('@')[0]
            return JsonResponse({
                'message': 'Login successful',
            }, status=200)
        else:
            return JsonResponse({'error': 'Invalid credentials'}, status=400)

@method_decorator(csrf_exempt, name='dispatch')
class UniversityView(View):
    def get(self, request):
        universities = list(University.objects.values())
        return JsonResponse(universities, safe=False)

    def post(self, request):
        data = parse_json(request)
        if not data:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        university = University.objects.create(**data)
        return HttpResponse(status=201)


@method_decorator(csrf_exempt, name='dispatch')
class CollegeView(View):
    def get(self, request):
        colleges = list(College.objects.values())
        return JsonResponse(colleges, safe=False)

    def post(self, request):
        data = parse_json(request)
        if not data:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        college = College.objects.create(**data)
        return HttpResponse(status=201)


@method_decorator(csrf_exempt, name='dispatch')
class DepartmentView(View):
    def get(self, request):
        departments = list(Department.objects.values())
        return JsonResponse(departments, safe=False)

    def post(self, request):
        data = parse_json(request)
        if not data:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        department = Department.objects.create(**data)
        return HttpResponse(status=201)


@method_decorator(csrf_exempt, name='dispatch')
class FacultyMemberView(View):
    def get(self, request):
        faculty_members = list(FacultyMember.objects.values())
        return JsonResponse(faculty_members, safe=False)

    def post(self, request):
        data = parse_json(request)
        if not data:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        faculty_member = FacultyMember.objects.create(**data)
        return HttpResponse(status=201)


@method_decorator(csrf_exempt, name='dispatch')
class StudentView(View):
    def get(self, request):
        students = list(Student.objects.values())
        return JsonResponse(students, safe=False)

    def post(self, request):
        data = parse_json(request)
        if not data:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        student = Student.objects.create(**data)
        return HttpResponse(status=201)


@method_decorator(csrf_exempt, name='dispatch')
class ContactView(View):
    def get(self, request):
        contacts = list(Contact.objects.values('student_id', 'phone_number', 'email'))
        return JsonResponse(contacts, safe=False)

    def post(self, request):
        data = parse_json(request)
        if not data:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        contact = Contact.objects.create(**data)
        return HttpResponse(status=201)


@method_decorator(csrf_exempt, name='dispatch')
class EthnicityView(View):
    def get(self, request):
        ethnicities = list(Ethnicity.objects.values('student_id', 'ethnicity'))
        return JsonResponse(ethnicities, safe=False)

    def post(self, request):
        data = parse_json(request)
        if not data:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        ethnicity = Ethnicity.objects.create(**data)
        return HttpResponse(status=201)


@method_decorator(csrf_exempt, name='dispatch')
class EducationalBackgroundView(View):
    def get(self, request):
        backgrounds = list(EducationalBackground.objects.values())
        return JsonResponse(backgrounds, safe=False)

    def post(self, request):
        data = parse_json(request)
        if not data:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        background = EducationalBackground.objects.create(**data)
        return HttpResponse(status=201)


@method_decorator(csrf_exempt, name='dispatch')
class DissertationView(View):
    def get(self, request):
        dissertations = list(Dissertation.objects.values())
        return JsonResponse(dissertations, safe=False)

    def post(self, request):
        data = parse_json(request)
        if not data:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        dissertation = Dissertation.objects.create(**data)
        return HttpResponse(status=201)


@method_decorator(csrf_exempt, name='dispatch')
class TestScoreView(View):
    def get(self, request):
        test_scores = list(TestScore.objects.values())
        return JsonResponse(test_scores, safe=False)

    def post(self, request):
        data = parse_json(request)
        if not data:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        test_score = TestScore.objects.create(**data)
        return HttpResponse(status=201)


@method_decorator(csrf_exempt, name='dispatch')
class AwardView(View):
    def get(self, request):
        awards = list(Award.objects.values())
        return JsonResponse(awards, safe=False)

    def post(self, request):
        data = parse_json(request)
        if not data:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        award = Award.objects.create(**data)
        return HttpResponse(status=201)


@method_decorator(csrf_exempt, name='dispatch')
class TrainingWorkshopView(View):
    def get(self, request):
        workshops = list(TrainingWorkshop.objects.values())
        return JsonResponse(workshops, safe=False)

    def post(self, request):
        data = parse_json(request)
        if not data:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        workshop = TrainingWorkshop.objects.create(**data)
        return HttpResponse(status=201)


@method_decorator(csrf_exempt, name='dispatch')
class SkillView(View):
    def get(self, request):
        skills = list(Skill.objects.values())
        return JsonResponse(skills, safe=False)

    def post(self, request):
        data = parse_json(request)
        if not data:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        skill = Skill.objects.create(**data)
        return HttpResponse(status=201)


@method_decorator(csrf_exempt, name='dispatch')
class WorkExperienceView(View):
    def get(self, request):
        experiences = list(WorkExperience.objects.values())
        return JsonResponse(experiences, safe=False)

    def post(self, request):
        data = parse_json(request)
        if not data:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        experience = WorkExperience.objects.create(**data)
        return HttpResponse(status=201)


@method_decorator(csrf_exempt, name='dispatch')
class AcknowledgementFormView(View):
    def get(self, request):
        forms = list(AcknowledgementForm.objects.values())
        return JsonResponse(forms, safe=False)

    def post(self, request):
        data = parse_json(request)
        if not data:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        form = AcknowledgementForm.objects.create(**data)
        return HttpResponse(status=201)


@method_decorator(csrf_exempt, name='dispatch')
class ReferenceView(View):
    def get(self, request):
        references = list(Reference.objects.values())
        return JsonResponse(references, safe=False)

    def post(self, request):
        data = parse_json(request)
        if not data:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        reference = Reference.objects.create(**data)
        return HttpResponse(status=201)


@method_decorator(csrf_exempt, name='dispatch')
class VolunteerActivityView(View):
    def get(self, request):
        activities = list(VolunteerActivity.objects.values())
        return JsonResponse(activities, safe=False)

    def post(self, request):
        data = parse_json(request)
        if not data:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        activity = VolunteerActivity.objects.create(**data)
        return HttpResponse(status=201)
