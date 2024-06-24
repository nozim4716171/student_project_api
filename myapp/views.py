from django.shortcuts import render
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from .models import Talaba,Guruh
from .serializers import TalabaSerializer,GuruhSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet

# Create your views here.

# Talabalar ro'yxatini chiqarish viewsi 
@api_view(['GET'])
def StudentListView(request):
    try:
        students = Talaba.objects.all()
        serializer = TalabaSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except:
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
    
    
# Talabalarni qo'shish uchun viewi
@api_view(['POST'])
def StudentCreateView(request):
    try:
        data = request.data
        serializer = TalabaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    except:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
 
# Talabalarning to'liq ma'lumotini olish uchun viewsi
@api_view(['GET'])
def StudentDetailView(request, id):
    try:
        student = get_object_or_404(Talaba, id=id)
        serializer = TalabaSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except:
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
    
    
# Talabalarning ma'lumotini yangilash uchun viewsi
@api_view(['PUT'])
def StudentUpdateView(request, id):
    try:
        student = get_object_or_404(Talaba, id=id)
        data = request.data
        serializer = TalabaSerializer(student, data=data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    except:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
# Talabalarning ma'lumotini yangilash uchun viewsi
@api_view(['PATCH'])
def StudentUpdateallView(request, id):
    try:
        student = get_object_or_404(Talaba, id=id)
        data = request.data
        serializer = TalabaSerializer(student, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    except:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# Talabalarning ma'lumotini o'chirish uchun viewsi
@api_view(['DELETE'])
def StudentDeleteView(request, id):
    try:
        student = get_object_or_404(Talaba, id=id)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    

# Guruhlar ro'yxatini chiqarish viewsi 
@api_view(['GET'])
def GroupListView(request):
    try:
        students = Guruh.objects.all()
        serializer = GuruhSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except:
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
    
    
# Guruhni qo'shish uchun viewi
@api_view(['POST'])
def GroupCreateView(request):
    try:
        data = request.data
        serializer = GuruhSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    except:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# Guruh nomini yozganda talabalar ro'yxatini chiqarib beradigan view
@api_view(['GET'])
def GroupStudentView(request, id):
    try:
        group = get_object_or_404(Guruh, id=id)
        students = Talaba.objects.filter(guruh=group)
        serializer = TalabaSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except:
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
    
    
# Guruhlarning ma'lumotini yangilash uchun viewsi
@api_view(['PUT'])
def GroupUpdateView(request, id):
    try:
        student = get_object_or_404(Guruh, id=id)
        data = request.data
        serializer = GuruhSerializer(student, data=data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    except:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
# Guruhning ma'lumotini yangilash uchun viewsi
@api_view(['PATCH'])
def GroupUpdateallView(request, id):
    try:
        student = get_object_or_404(Guruh, id=id)
        data = request.data
        serializer = GuruhSerializer(student, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    except:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# Guruhlarning ma'lumotini o'chirish uchun viewsi
@api_view(['DELETE'])
def GroupDeleteView(request, id):
    try:
        student = get_object_or_404(Guruh, id=id)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
#     
class StudentViewSet(ModelViewSet):
    queryset = Talaba.objects.all()
    serializer_class = TalabaSerializer