
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema
from .services import fetch_posts_from_external_api, paginate_posts
from .serializers import PostSerializer

class PostListView(APIView):
    @extend_schema(request={}, responses=PostSerializer)
    def get(self, request, page):
        items_per_page = 10
        
        posts_data = fetch_posts_from_external_api()
        posts = paginate_posts(posts_data, page, items_per_page)
        
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


