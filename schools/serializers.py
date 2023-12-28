from rest_framework import serializers

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


class AcademicYearSerializers(serializers.ModelSerializer):
    class Meta:
        model = AcademicYear
        fields = "__all__"


class AttendanceSerializers(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = "__all__"


class ClassSerializers(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = "__all__"


class ClassScheduleSerializers(serializers.ModelSerializer):
    class Meta:
        model = ClassSchedule
        fields = "__all__"


class ExamSerializers(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = "__all__"


class ExamScoreSerializers(serializers.ModelSerializer):
    class Meta:
        model = ExamScore
        fields = "__all__"


class GradeLevelSerializers(serializers.ModelSerializer):
    class Meta:
        model = GradeLevel
        fields = "__all__"


class LessonSerializers(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"


class ParentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Parent
        fields = "__all__"


class SchoolSerializers(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = "__all__"


class SubjectSerializers(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = "__all__"


class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"


class TeacherSerializers(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = "__all__"


class TeacherSubjectSerializers(serializers.ModelSerializer):
    class Meta:
        model = TeacherSubject
        fields = "__all__"
