from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Project, Skill, About, Experience, Certification, JourneyChapter
from .serializers import ProjectSerializer, SkillSerializer, AboutSerializer, ExperienceSerializer, CertificationSerializer, JourneyChapterSerializer

class ProjectViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows projects to be viewed.
    """
    queryset = Project.objects.all().order_by('-created_at')
    serializer_class = ProjectSerializer
    lookup_field = 'id'

class SkillViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows skills to be viewed.
    """
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

class AboutAPIView(APIView):
    """
    API endpoint that allows about information to be viewed.
    """
    def get(self, request, format=None):
        about = About.objects.first()
        if about:
            serializer = AboutSerializer(about)
            return Response(serializer.data)
        return Response({})

class ExperienceViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows experience to be viewed.
    """
    queryset = Experience.objects.all().order_by('order', '-created_at')
    serializer_class = ExperienceSerializer

class CertificationViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows certifications to be viewed.
    """
    queryset = Certification.objects.all().order_by('order', '-created_at')
    serializer_class = CertificationSerializer

class JourneyChapterViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows journey chapters to be viewed.
    """
    queryset = JourneyChapter.objects.all().order_by('order', '-created_at')
    serializer_class = JourneyChapterSerializer
