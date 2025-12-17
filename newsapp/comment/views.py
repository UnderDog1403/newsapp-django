from django.core.serializers import serialize
from django.db.migrations import serializer
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import CommentSerializer, CommentCreateUpdateSerializer
from .services.commentservice import CommentService


# Create your views here.
class CommentView(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.service = CommentService()

    def post(self, request):
        serializer = CommentCreateUpdateSerializer(data=request.data)
        if serializer.is_valid():
            try:
                comment = serializer.validated_data.get("comment")
                user_id = serializer.validated_data.get("user_id")
                article_id = serializer.validated_data.get("article_id")
                result = self.service.create_comment(comment,user_id,article_id)
                return Response(
                    {"message": "Thêm thành công", "comment_id": result.id},
                    status=status.HTTP_201_CREATED
                )
            except ValueError as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class CommentDetailView(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.service = CommentService()
    def patch(self,request,id):
        serializer = CommentCreateUpdateSerializer(data=request.data,partial=True)
        if serializer.is_valid():
            try:
                comment = serializer.validated_data.get("comment")
                updated_comment = self.service.change_comment(comment,id)
                print(updated_comment)
                return Response({
                    "message": "Cập nhật thành công",
                }, status=status.HTTP_200_OK)
            except ValueError as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,id):
        try:
            self.service.delete_comment(id)
            return Response({
                "message": "Xoa thành công",
            }, status=status.HTTP_200_OK)
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
class CommentByArticleView(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.service = CommentService()
    def get(self,request,article_slug):
        try:
            comments =self.service.get_by_article(article_slug)
            serialized = CommentSerializer(comments,many=True)
            return Response({
                "message": "Lay thanh cong",
                "data": serialized.data
            }, status=status.HTTP_200_OK)
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

#



