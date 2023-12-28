from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class School(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()

    class Meta:
        verbose_name = _("school")
        verbose_name_plural = _("schools")


class Teacher(models.Model):
    person = models.OneToOneField(User, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("teacher")
        verbose_name_plural = _("teachers")


class Student(models.Model):
    person = models.OneToOneField(User, on_delete=models.CASCADE)
    parent = models.ForeignKey("Parent", on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    grade_level = models.ForeignKey("GradeLevel", on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("student")
        verbose_name_plural = _("students")


class Parent(models.Model):
    person = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("parent")
        verbose_name_plural = _("parents")


class Lesson(models.Model):
    name = models.CharField(max_length=255)
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("lesson")
        verbose_name_plural = _("lessons")


class Class(models.Model):
    name = models.CharField(max_length=255)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student)

    class Meta:
        verbose_name = _("class")
        verbose_name_plural = _("Classes")


class AcademicYear(models.Model):
    year = models.CharField(max_length=9)  # e.g., "2022-2023"

    class Meta:
        verbose_name = _("academic year")
        verbose_name_plural = _("academic years")


class GradeLevel(models.Model):
    level = models.CharField(max_length=255)

    class Meta:
        verbose_name = _("grade level")
        verbose_name_plural = _("grade levels")


class Exam(models.Model):
    name = models.CharField(max_length=255)
    academic_year = models.ForeignKey(AcademicYear, on_delete=models.CASCADE)
    lessons = models.ManyToManyField(Lesson)

    class Meta:
        verbose_name = _("exam")
        verbose_name_plural = _("exams")


class ExamScore(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    score = models.FloatField()

    class Meta:
        verbose_name = _("exam score")
        verbose_name_plural = _("exam scores")


class Subject(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = _("subject")
        verbose_name_plural = _("subjects")


class TeacherSubject(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("teacher subject")
        verbose_name_plural = _("teacher subjects")


class Attendance(models.Model):
    date = models.DateField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    present = models.BooleanField(default=True)

    class Meta:
        verbose_name = _("attendance")
        verbose_name_plural = _("attendances")


class ClassSchedule(models.Model):
    class_name = models.ForeignKey(Class, on_delete=models.CASCADE)
    day_of_week = models.CharField(max_length=10)  # e.g., "Monday"
    start_time = models.TimeField()
    end_time = models.TimeField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("class schedule")
        verbose_name_plural = _("classe schedules")
