from rest_framework.views import APIView
from rest_framework.response import Response
from Web_repo.services.homepage_sections import get_homepage_section

class HomepageView(APIView):
    def get(self, request):
        user = self.request.user
        section_index = int(request.GET.get("section_index", 0))
        section_data, has_next_section = get_homepage_section(user, section_index)

        return Response({
            "section": section_data,
            "has_next_section": has_next_section
        }, status=200)



