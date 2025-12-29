from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import SavearticleSerializer
from .services.savearticleservice import SavearticleService


# Create your views here.
class SaveArticleView(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.service = SavearticleService()
    def get(self,request):
        page = int(request.GET.get('page', 1))
        per_page = int(request.GET.get('per_page', 5))
        user_id = request.GET.get('id')
        try:
            articles =self.service.get_paginated_savearticle(user_id,page,per_page)
            serialized = SavearticleSerializer(articles,many=True)
            return Response({
                'data': serialized.data,
                'count': articles.paginator.count,
                'num_pages': articles.paginator.num_pages,
                'current_page': articles.number
            })
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)
    def post(self,request):
        serialized = SavearticleSerializer(data=request.data)
        if serialized.is_valid():
            try:
                user_id=serialized.validated_data.get("user")
                article_id=serialized.validated_data.get("article")
                result =self.service.post_savearticle(user_id,article_id)
                return Response(
                    {"message": "Thêm thành công", "savearticle_id": result.id},
                    status=status.HTTP_201_CREATED
                )
            except ValueError as e:
                return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)



