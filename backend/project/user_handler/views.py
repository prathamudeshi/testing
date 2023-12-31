
from io import TextIOWrapper
from django.http import HttpResponse
from rest_framework import viewsets, status
from rest_framework.response import Response
import csv
from . import serializers
from . import models
from rest_framework.views import APIView
from django.shortcuts import render



from .models import AcademicYear
from .serializers import AcademicYearSerializer

class AcademicYearViewSet(viewsets.ModelViewSet):
    def create(request):
        if request.method=="POST":
            data=request.POST
            AY_name=data.get['AY_name']
            odd_sem_checkbox = request.POST.get('odd_sem_checkbox')
            if odd_sem_checkbox == 'on':
                AY_is_odd_semester = True
            else:
                AY_is_odd_semester = False

            AcademicYear.objects.create(
                AY_name=AY_name,
                AY_is_odd_semester=AY_is_odd_semester,
            )



        return render(request, )



    queryset = AcademicYear.objects.all()
    serializer_class = AcademicYearSerializer


class FacultyViewSet(viewsets.ViewSet):
    def list(self, request):
        faculties = models.Faculty.objects.all()
        serializer = serializers.FacultySerializer(faculties, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            faculty_instance = models.Faculty.objects.get(pk=pk)
            serializer = serializers.FacultySerializer(faculty_instance)
            return Response(serializer.data)
        except models.Faculty.DoesNotExist:
            return Response({"message": "Faculty not found."}, status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        file = request.FILES.get('file')
        if file:
           
            csv_data = csv.reader(TextIOWrapper(file, encoding='utf-8'))
            next(csv_data, None)

            for row in csv_data:
                
                branch = row[0]
                dept = row[1]
                employee_code = int(row[2])
                faculty_name = row[3]
                employee_abbreviation = row[4]
                faculty_email = row[5]
                experience = int(row[6])
                post = row[7]
                
                try:
                    faculty_instance = models.Faculty.objects.get(employee_abbreviation=employee_abbreviation)
                except models.Faculty.DoesNotExist:
                    faculty_instance = None

                if faculty_instance:
                    
                    serializer = serializers.FacultySerializer(faculty_instance, data={
                        'branch': branch,
                        'dept': dept,
                        'employee_code': employee_code,
                        'faculty_name': faculty_name,
                        'faculty_email': faculty_email,
                        'experience': experience,
                        'post': post,
                        
                    }, partial=True)
                else:
                    
                    serializer = serializers.FacultySerializer(data={
                        'branch': branch,
                        'dept': dept,
                        'employee_code': employee_code,
                        'faculty_name': faculty_name,
                        'employee_abbreviation': employee_abbreviation,
                        'faculty_email': faculty_email,
                        'experience': experience,
                        'post': post,
                        
                    })

                if serializer.is_valid():
                    serializer.save()

            return Response({"message": "CSV data added to faculty models successfully."}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": "No file uploaded."}, status=status.HTTP_400_BAD_REQUEST)


    def destroy(self, request, pk=None):
        try:
            faculty_instance = models.Faculty.objects.get(pk=pk)
            faculty_instance.delete()
            return Response({"message": "Faculty deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
        except models.Faculty.DoesNotExist:
            return Response({"message": "Faculty not found."}, status=status.HTTP_404_NOT_FOUND)

class StaffViewSet(viewsets.ViewSet):
    def list(self, request):
        staffs = models.Staff.objects.all()
        serializer = serializers.StaffSerializer(staffs, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            staff_instance = models.Staff.objects.get(pk=pk)
            serializer = serializers.StaffSerializer(staff_instance)
            return Response(serializer.data)
        except models.Staff.DoesNotExist:
            return Response({"message": "Staff not found."}, status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        file = request.FILES.get('file')
        if file:
            
            csv_data = csv.reader(TextIOWrapper(file, encoding='utf-8'))
            
            next(csv_data, None)

            for row in csv_data:

                branch = row[0]
                dept = row[1]
                employee_code = int(row[2])
                staff_name = row[3]
                employee_abbreviation = row[4]
                staff_email = row[5]
                experience = int(row[6])
                post = row[7]
                
                try:
                    staff_instance = models.Staff.objects.get(employee_abbreviation=employee_abbreviation)
                except models.Staff.DoesNotExist:
                    staff_instance = None

                if staff_instance:
                    
                    serializer = serializers.StaffSerializer(staff_instance, data={
                        'branch': branch,
                        'dept': dept,
                        'employee_code': employee_code,
                        'staff_name': staff_name,
                        'staff_email': staff_email,
                        'experience': experience,
                        'post': post,
                        
                    }, partial=True)
                else:
                    
                    serializer = serializers.StaffSerializer(data={
                        'branch': branch,
                        'dept': dept,
                        'employee_code': employee_code,
                        'staff_name': staff_name,
                        'employee_abbreviation': employee_abbreviation,
                        'staff_email': staff_email,
                        'experience': experience,
                        'post': post,
                        
                    })

                if serializer.is_valid():
                    serializer.save()

            return Response({"message": "CSV data added to staff models successfully."}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": "No file uploaded."}, status=status.HTTP_400_BAD_REQUEST)


    def destroy(self, request, pk=None):
        try:
            staff_instance = models.Staff.objects.get(pk=pk)
            staff_instance.delete()
            return Response({"message": "Staff deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
        except models.Staff.DoesNotExist:
            return Response({"message": "Staff not found."}, status=status.HTTP_404_NOT_FOUND)

class StudentViewSet(viewsets.ViewSet):
    def list(self, request):
        students = models.Student.objects.all()
        serializer = serializers.StudentSerializer(students, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            student_instance = models.Student.objects.get(pk=pk)
            serializer = serializers.StudentSerializer(student_instance)
            return Response(serializer.data)
        except models.Student.DoesNotExist:
            return Response({"message": "Student not found."}, status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        file = request.FILES.get('file')
        if file:
            
            csv_data = csv.reader(TextIOWrapper(file, encoding='utf-8'))
            
            next(csv_data, None)

            for row in csv_data:

                student_branch = row[0]
                student_name = row[1]
                roll_number = int(row[2])
                email = row[3]
                proctor_abbreviation = row[4]
                student_contact_no = row[5]
                parents_contact_no = row[6]
                parent_email_id = row[7]
                
                try:
                    student_instance = models.Student.objects.get(roll_number=roll_number)
                except models.Student.DoesNotExist:
                    student_instance = None

                if student_instance:
                    
                    serializer = serializers.StudentPostSerializer(student_instance, data={
                        'student_branch' : student_branch,
                        'student_name' : student_name,
                        'roll_number' : roll_number,
                        'email' : email,
                        'proctor_abbreviation' : proctor_abbreviation,
                        'student_contact_no' : student_contact_no,
                        'parents_contact_no' : parents_contact_no,
                        'parent_email_id' : parent_email_id,
                        
                    }, partial=True)
                else:
                    
                    serializer = serializers.StudentPostSerializer(data={
                        'student_branch' : student_branch,
                        'student_name' : student_name,
                        'roll_number' : roll_number,
                        'email' : email,
                        'proctor_abbreviation' : proctor_abbreviation,
                        'student_contact_no' : student_contact_no,
                        'parents_contact_no' : parents_contact_no,
                        'parent_email_id' : parent_email_id,
                        
                    })

                if serializer.is_valid():
                    serializer.save()

            return Response({"message": "CSV data added to Student models successfully."}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": "No file uploaded."}, status=status.HTTP_400_BAD_REQUEST)


    def destroy(self, request, pk=None):
        try:
            student_instance = models.Student.objects.get(pk=pk)
            student_instance.delete()
            return Response({"message": "Student deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
        except models.Student.DoesNotExist:
            return Response({"message": "Student not found."}, status=status.HTTP_404_NOT_FOUND)

class CourseViewSet(viewsets.ViewSet):
    def list(self, request):
        courses = models.Course.objects.all()
        serializer = serializers.CourseSerializer(courses, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            course_instance = models.Course.objects.get(pk=pk)
            serializer = serializers.CourseSerializer(course_instance)
            return Response(serializer.data)
        except models.Course.DoesNotExist:
            return Response({"message": "Course not found."}, status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        file = request.FILES.get('file')
        if file:
            
            csv_data = csv.reader(TextIOWrapper(file, encoding='utf-8'))
            
            next(csv_data, None)

            for row in csv_data:
                
                branch = row[0]
                course_code = row[1]
                course_name = row[2]
                dept = row[3]
                sem = row[4]
                scheme_name = row[5]
                credit = row[6]
                hours = row[7]
                
                try:
                    course_instance = models.Course.objects.get(course_code=course_code)
                except models.Course.DoesNotExist:
                    course_instance = None

                if course_instance:
                    
                    serializer = serializers.CourseSerializer(course_instance, data={
                        
                        'branch' : branch,
                        'course_code' : course_code,
                        'course_name' : course_name,
                        'dept' : dept,
                        'sem' : sem,
                        'scheme_name' : scheme_name,
                        'credit' : credit,
                        'hours' : hours,

                    }, partial=True)
                else:
                    
                    serializer = serializers.CourseSerializer(data={
                        'branch' : branch,
                        'course_code' : course_code,
                        'course_name' : course_name,
                        'dept' : dept,
                        'sem' : sem,
                        'scheme_name' : scheme_name,
                        'credit' : credit,
                        'hours' : hours,
                        
                    })

                if serializer.is_valid():
                    serializer.save()

            return Response({"message": "CSV data added to Course models successfully."}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": "No file uploaded."}, status=status.HTTP_400_BAD_REQUEST)


    def destroy(self, request, pk=None):
        try:
            course_instance = models.Course.objects.get(pk=pk)
            course_instance.delete()
            return Response({"message": "Course deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
        except models.Course.DoesNotExist:
            return Response({"message": "Course not found."}, status=status.HTTP_404_NOT_FOUND)


class DownloadCSV(APIView):

    allowed_methods = ['GET', 'POST']

    def get(self, request, model):
        if model == 'Faculty':
            queryset = models.Faculty.objects.none()  
            serializer_class = serializers.FacultySerializer
        elif model == 'Staff':
            queryset = models.Staff.objects.none()  
            serializer_class = serializers.StaffSerializer
        elif model == 'Student':
            queryset = models.Student.objects.none()  
            serializer_class = serializers.StudentSerializer
        elif model == 'Course':
            queryset = models.Course.objects.none()  
            serializer_class = serializers.CourseSerializer
        else:
            return Response({'message': 'Invalid model name.'}, status=400)

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="{}.csv"'.format(model)

        serializer = serializer_class(queryset, many=True)

        field_names = ['branch', 'dept', 'employee_code', 'faculty_name', 'employee_abbreviation',
                       'faculty_email', 'experience', 'post'] if model == 'Faculty' else ['branch', 'dept', 'employee_code', 'staff_name', 'employee_abbreviation',
                       'staff_email', 'experience', 'post'] if model == 'Staff' else ['student_branch', 'student_name', 'roll_number', 'email', 'proctor_abbreviation',
                       'student_contact_no', 'parents_contact_no', 'parent_email_id'] if model == 'Student' else ['branch', 'course_code', 'course_name', 'dept', 'sem',
                       'scheme_name', 'credit', 'hours'] if model == 'Course' else []

        writer = csv.DictWriter(response, fieldnames=field_names)
        writer.writeheader()

        return response

