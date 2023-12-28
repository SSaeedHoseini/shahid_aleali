from django.contrib import admin

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

admin.site.register(School)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Parent)
admin.site.register(Lesson)
admin.site.register(Class)
admin.site.register(AcademicYear)
admin.site.register(Attendance)
admin.site.register(GradeLevel)
admin.site.register(Exam)
admin.site.register(ExamScore)
admin.site.register(Subject)
admin.site.register(TeacherSubject)
admin.site.register(ClassSchedule)
