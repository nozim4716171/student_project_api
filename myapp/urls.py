from django.urls import path
from .views import StudentListView,StudentCreateView,StudentDetailView,StudentUpdateView,StudentDeleteView
from .views import GroupListView,GroupCreateView,GroupStudentView,GroupUpdateView,GroupDeleteView
from rest_framework.routers import SimpleRouter
from .views import StudentViewSet



router = SimpleRouter()
router.register('student', StudentViewSet, basename='student')

urlpatterns = [
    path('student/list/', StudentListView, name='student_list'),
    path('student/create/', StudentCreateView, name='student_create'),
    path('student/<int:id>/', StudentDetailView, name='student_detail'),
    path('student/<int:id>/update',StudentUpdateView, name='student_update'),
    path('student/<int:id>/delete',StudentDeleteView, name='student_delete'),
    path('group/list/', GroupListView, name='group_list'),
    path('group/create/', GroupCreateView, name='group_create'),
    path('group/<int:id>/',GroupStudentView, name='group_students'),    
    path('group/<int:id>/update',GroupUpdateView, name='group_update'),    
    path('group/<int:id>/delete',GroupDeleteView, name='group_delete'),    
      
]


urlpatterns = urlpatterns + router.urls
