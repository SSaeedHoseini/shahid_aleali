from django.contrib.auth import get_user_model
from rest_framework.viewsets import ModelViewSet

from .models import (
    AcademicYear,
    Attendance,
    Class,
    ClassSchedule,
    Exam,
    ExamScore,
    GradeLevel,
    Lesson,
    Parent,
    School,
    Student,
    Subject,
    Teacher,
    TeacherSubject,
)
from .serializers import (
    AcademicYearSerializers,
    AttendanceSerializers,
    ClassScheduleSerializers,
    ClassSerializers,
    ExamScoreSerializers,
    ExamSerializers,
    GradeLevelSerializers,
    LessonSerializers,
    ParentSerializers,
    SchoolSerializers,
    StudentSerializers,
    SubjectSerializers,
    TeacherSerializers,
    TeacherSubjectSerializers,
)

User = get_user_model()


class AcademicYearModelViewSet(ModelViewSet):
    serializer_class = AcademicYearSerializers
    queryset = AcademicYear.objects.all()


class AttendanceModelViewSet(ModelViewSet):
    serializer_class = AttendanceSerializers
    queryset = Attendance.objects.all()


class ClassModelViewSet(ModelViewSet):
    serializer_class = ClassSerializers
    queryset = Class.objects.all()


class ClassScheduleModelViewSet(ModelViewSet):
    serializer_class = ClassScheduleSerializers
    queryset = ClassSchedule.objects.all()


class ExamModelViewSet(ModelViewSet):
    serializer_class = ExamSerializers
    queryset = Exam.objects.all()


class ExamScoreModelViewSet(ModelViewSet):
    serializer_class = ExamScoreSerializers
    queryset = ExamScore.objects.all()


class GradeLevelModelViewSet(ModelViewSet):
    serializer_class = GradeLevelSerializers
    queryset = GradeLevel.objects.all()


class LessonModelViewSet(ModelViewSet):
    serializer_class = LessonSerializers
    queryset = Lesson.objects.all()


class ParentModelViewSet(ModelViewSet):
    serializer_class = ParentSerializers
    queryset = Parent.objects.all()


class SchoolModelViewSet(ModelViewSet):
    serializer_class = SchoolSerializers
    queryset = School.objects.all()


class StudentModelViewSet(ModelViewSet):
    serializer_class = StudentSerializers
    queryset = Student.objects.all()


class SubjectModelViewSet(ModelViewSet):
    serializer_class = SubjectSerializers
    queryset = Subject.objects.all()


class TeacherModelViewSet(ModelViewSet):
    serializer_class = TeacherSerializers
    queryset = Teacher.objects.all()


class TeacherSubjectModelViewSet(ModelViewSet):
    serializer_class = TeacherSubjectSerializers
    queryset = TeacherSubject.objects.all()
