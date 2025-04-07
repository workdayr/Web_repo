from rest_framework.views import APIView
from rest_framework.response import Response
from Web_repo.services.homepage_sections import get_homepage_sections

class HomepageView(APIView):
    def get(self, request):
        user = self.request.user
        page = int(request.GET.get("page", 0))
        sections = get_homepage_sections(user, page=page)
        response = Response(sections, status=200)

        return response


