from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CategorySerializer
from .services.categoryservice import CategoryService

# Create your views here.
class CategoryView(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.service = CategoryService()

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        elif self.request.method == 'POST':
            return [IsAdminUser()]
        return super().get_permissions()

    def post(self,request):
        serializer= CategorySerializer(data=request.data)
        if serializer.is_valid():
            try:
                name = serializer.validated_data.get("name")
                category = self.service.create_category(name)
                return Response({"message": "Đăng ký thành công!", "category_id": category.id}, status=status.HTTP_201_CREATED)
            except ValueError as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self,request):
        categories = self.service.list_category()
        serializer = CategorySerializer(categories,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
class CategoryDetailView(APIView):
    permission_classes = [IsAdminUser]
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.service = CategoryService()
    def put(self,request, id):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            try:
                updated_category = self.service.update_category(id, **serializer.validated_data)
                return Response({
                    "message": "Cập nhật thành công",
                    "data": CategorySerializer(updated_category).data
                }, status=status.HTTP_200_OK)
            except ValueError as e:
                return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request, id):
        try:
            self.service.delete_category(id)
            return Response({
                "message": "Xoa thành công",
            }, status=status.HTTP_200_OK)
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)







