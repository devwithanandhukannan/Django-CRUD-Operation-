from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Category
from .serializers import CategorySerializer

from rest_framework.viewsets import ModelViewSet
from .models import Course
from .serializers import CourseSerializer




class CategoryListCreate(APIView):

    # GET → list all categories
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    # POST → create new category
    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryDetail(APIView):

    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return None

    # GET single category
    def get(self, request, pk):
        category = self.get_object(pk)
        if not category:
            return Response({"error": "Not found"}, status=404)

        serializer = CategorySerializer(category)
        return Response(serializer.data)

    # PUT → update category
    def put(self, request, pk):
        category = self.get_object(pk)
        if not category:
            return Response({"error": "Not found"}, status=404)

        serializer = CategorySerializer(category, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=400)

    # DELETE → delete category
    def delete(self, request, pk):
        category = self.get_object(pk)
        if not category:
            return Response({"error": "Not found"}, status=404)

        category.delete()
        return Response(status=204)



class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer