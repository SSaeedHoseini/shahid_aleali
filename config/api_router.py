from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from schools.views import (
    AcademicYearModelViewSet,
    AttendanceModelViewSet,
    ClassModelViewSet,
    ClassScheduleModelViewSet,
    ExamModelViewSet,
    ExamScoreModelViewSet,
    GradeLevelModelViewSet,
    LessonModelViewSet,
    ParentModelViewSet,
    SchoolModelViewSet,
    StudentModelViewSet,
    SubjectModelViewSet,
    TeacherModelViewSet,
    TeacherSubjectModelViewSet,
)
from shahid_aleali.users.api.views import GroupViewSet, UserViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("groups", GroupViewSet)
router.register("academic-year", AcademicYearModelViewSet)
router.register("attendances", AttendanceModelViewSet)
router.register("classes", ClassModelViewSet)
router.register("class-schedule", ClassScheduleModelViewSet)
router.register("exams", ExamModelViewSet)
router.register("exam-scores", ExamScoreModelViewSet)
router.register("grade-levels", GradeLevelModelViewSet)
router.register("lessons", LessonModelViewSet)
router.register("parents", ParentModelViewSet)
router.register("schools", SchoolModelViewSet)
router.register("students", StudentModelViewSet)
router.register("subjects", SubjectModelViewSet)
router.register("teachers", TeacherModelViewSet)
router.register("teacher-subjects", TeacherSubjectModelViewSet)


app_name = "api"
urlpatterns = router.urls
