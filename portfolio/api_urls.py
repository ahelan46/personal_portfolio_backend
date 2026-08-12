from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import ProjectViewSet, SkillViewSet, AboutAPIView, ExperienceViewSet, CertificationViewSet, JourneyChapterViewSet

router = DefaultRouter()
router.register(r'projects', ProjectViewSet)
router.register(r'skills', SkillViewSet)
router.register(r'experience', ExperienceViewSet, basename='experience')
router.register(r'certifications', CertificationViewSet, basename='certifications')
router.register(r'journey', JourneyChapterViewSet, basename='journey')

urlpatterns = [
    path('', include(router.urls)),
    path('about/', AboutAPIView.as_view(), name='api-about'),
]
