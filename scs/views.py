from django.contrib.auth.hashers import check_password
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .permissions import IsTeacherOrReadOnly
from .serializers import *
from .swagger_auto_schemas import *


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


@swagger_post_serializer(UserSerializer)
@api_view(['POST'])
def register_view(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = get_tokens_for_user(user)
            return Response({
                'token': token,
                'user_type': 'student' if user.is_student else 'teacher'
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_login_user()
@api_view(['POST'])
def login_view(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')
        user = User.objects.filter(username=username).first()
        if user and check_password(password, user.password):
            token = get_tokens_for_user(user)
            return Response({'token': token, 'user_type': 'student' if user.is_student else 'teacher'},
                            status=status.HTTP_200_OK)
        return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def home_view(request):
    user = request.user
    user_type = 'student' if user.is_student else 'teacher'
    return Response({'message': f'Logged in as a {user_type}.'})


@swagger_get_serializer(UniversitySerializer)
@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def university_list(request):
    """
    List all universities, only GET method is allowed.
    """
    if request.method == 'GET':
        universities = University.objects.all()
        serializer = UniversitySerializer(universities, many=True)
        return Response(serializer.data)


@swagger_get_serializer(UniversitySerializer)
@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def university_detail_get(request, pk):
    try:
        university = University.objects.get(pk=pk)
    except University.DoesNotExist:
        return Response({'message': 'The university does not exist'}, status=status.HTTP_404_NOT_FOUND)
    serializer = UniversitySerializer(university)
    return Response(serializer.data)
@swagger_post_serializer(UniversitySerializer)
@api_view(['POST'])
@permission_classes([IsTeacherOrReadOnly])
def university_create(request):
    if request.method == 'POST':
        serializer = UniversitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_detail_put_delete_serializer(UniversitySerializer)
@api_view(['PUT', 'DELETE'])
@permission_classes([IsTeacherOrReadOnly])
def university_detail_modify(request, pk):
    try:
        university = University.objects.get(pk=pk)
    except University.DoesNotExist:
        return Response({'message': 'The university does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = UniversitySerializer(university, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        university.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@swagger_get_serializer(CollegeSerializer)
@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def college_list(request):
    """
    List all colleges, only GET method is allowed.
    """
    if request.method == 'GET':
        colleges = College.objects.all()
        serializer = CollegeSerializer(colleges, many=True)
        return Response(serializer.data)

@swagger_get_serializer(CollegeSerializer)
@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def college_detail_get(request, pk):
    try:
        college = College.objects.get(pk=pk)
    except College.DoesNotExist:
        return Response({'message': 'College not found'}, status=status.HTTP_404_NOT_FOUND)
    serializer = CollegeSerializer(college)
    return Response(serializer.data)

@swagger_post_serializer(CollegeSerializer)
@api_view(['POST'])
@permission_classes([IsTeacherOrReadOnly])
def college_create(request):
    if request.method == 'POST':
        serializer = CollegeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_detail_put_delete_serializer(CollegeSerializer)
@api_view(['PUT', 'DELETE'])
@permission_classes([IsTeacherOrReadOnly])
def college_detail_modify(request, pk):
    try:
        college = College.objects.get(pk=pk)
    except College.DoesNotExist:
        return Response({'message': 'College not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = CollegeSerializer(college, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        college.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@swagger_get_serializer(CampusSerializer)
@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def campus_list(request):
    """
    List all campuses, only GET method is allowed.
    """
    if request.method == 'GET':
        campuses = Campus.objects.all()
        serializer = CampusSerializer(campuses, many=True)
        return Response(serializer.data)
@swagger_get_serializer(CampusSerializer)
@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def campus_detail_get(request, pk):
    try:
        campus = Campus.objects.get(pk=pk)
    except Campus.DoesNotExist:
        return Response({'message': 'Campus not found'}, status=status.HTTP_404_NOT_FOUND)
    serializer = CampusSerializer(campus)
    return Response(serializer.data)

@swagger_post_serializer(CampusSerializer)
@api_view(['POST'])
@permission_classes([IsTeacherOrReadOnly])
def campus_create(request):
    if request.method == 'POST':
        serializer = CampusSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_detail_put_delete_serializer(CampusSerializer)
@api_view(['PUT', 'DELETE'])
@permission_classes([IsTeacherOrReadOnly])
def campus_detail_modify(request, pk):
    try:
        campus = Campus.objects.get(pk=pk)
    except Campus.DoesNotExist:
        return Response({'message': 'Campus not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = CampusSerializer(campus, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        campus.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@swagger_get_serializer(DepartmentSerializer)
@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def department_list(request):
    """
    List all departments, only GET method is allowed.
    """
    if request.method == 'GET':
        departments = Department.objects.all()
        serializer = DepartmentSerializer(departments, many=True)
        return Response(serializer.data)
@swagger_get_serializer(DepartmentSerializer)
@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def department_detail_get(request, pk):
    try:
        department = Department.objects.get(pk=pk)
    except Department.DoesNotExist:
        return Response({'message': 'Department not found'}, status=status.HTTP_404_NOT_FOUND)
    serializer = DepartmentSerializer(department)
    return Response(serializer.data)

@swagger_post_serializer(DepartmentSerializer)
@api_view(['POST'])
@permission_classes([IsTeacherOrReadOnly])
def department_create(request):
    if request.method == 'POST':
        serializer = DepartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@swagger_detail_put_delete_serializer(DepartmentSerializer)
@api_view(['PUT', 'DELETE'])
@permission_classes([IsTeacherOrReadOnly])
def department_detail_modify(request, pk):
    try:
        department = Department.objects.get(pk=pk)
    except Department.DoesNotExist:
        return Response({'message': 'Department not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = DepartmentSerializer(department, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        department.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@swagger_get_serializer(FacultyMemberSerializer)
@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def faculty_member_list(request):
    """
    List all faculty members, only GET method is allowed.
    """
    if request.method == 'GET':
        faculty_members = FacultyMember.objects.all()
        serializer = FacultyMemberSerializer(faculty_members, many=True)
        return Response(serializer.data)
@swagger_get_serializer(FacultyMemberSerializer)
@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def faculty_member_detail_get(request, pk):
    try:
        faculty_member = FacultyMember.objects.get(pk=pk)
    except FacultyMember.DoesNotExist:
        return Response({'message': 'Faculty member not found'}, status=status.HTTP_404_NOT_FOUND)
    serializer = FacultyMemberSerializer(faculty_member)
    return Response(serializer.data)

@swagger_post_serializer(FacultyMemberSerializer)
@api_view(['POST'])
@permission_classes([IsTeacherOrReadOnly])
def faculty_create(request):
    if request.method == 'POST':
        serializer = FacultyMemberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@swagger_detail_put_delete_serializer(FacultyMemberSerializer)
@api_view(['PUT', 'DELETE'])
@permission_classes([IsTeacherOrReadOnly])
def faculty_member_detail_modify(request, pk):
    try:
        faculty_member = FacultyMember.objects.get(pk=pk)
    except FacultyMember.DoesNotExist:
        return Response({'message': 'Faculty member not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = FacultyMemberSerializer(faculty_member, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        faculty_member.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@swagger_get_serializer(FundingSerializer)
@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def funding_list(request):
    """
    List all fundings, only GET method is allowed.
    """
    if request.method == 'GET':
        fundings = Funding.objects.all()
        serializer = FundingSerializer(fundings, many=True)
        return Response(serializer.data)
@swagger_get_serializer(FundingSerializer)
@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def funding_detail_get(request, pk):
    try:
        funding = Funding.objects.get(pk=pk)
    except Funding.DoesNotExist:
        return Response({'message': 'Funding not found'}, status=status.HTTP_404_NOT_FOUND)
    serializer = FundingSerializer(funding)
    return Response(serializer.data)

@swagger_post_serializer(FundingSerializer)
@api_view(['POST'])
@permission_classes([IsTeacherOrReadOnly])
def funding_create(request):
    if request.method == 'POST':
        serializer = FundingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@swagger_detail_put_delete_serializer(FundingSerializer)
@api_view(['PUT', 'DELETE'])
@permission_classes([IsTeacherOrReadOnly])
def funding_detail_modify(request, pk):
    try:
        funding = Funding.objects.get(pk=pk)
    except Funding.DoesNotExist:
        return Response({'message': 'Funding not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = FundingSerializer(funding, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        funding.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@swagger_auto_schema(method='get', responses={200: BiographicInformationSerializer(many=True)})
@swagger_auto_schema(method='post', request_body=BiographicInformationSerializer())
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def biographic_information(request):
    if request.method == 'GET':
        if request.user.is_teacher:
            biographic_info = BiographicInformation.objects.all()
        else:
            biographic_info = BiographicInformation.objects.filter(user=request.user)
        serializer = BiographicInformationSerializer(biographic_info, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = BiographicInformationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)  # Ensure user is set correctly
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
