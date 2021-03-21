from django.urls import path, include
from . import views


urlpatterns = [
    path('add-student/', views.add_student, name='add-student'),
    path('edit-student/<int:id>', views.edit_student, name='edit-student'),
    path('', views.HomePageView.as_view(), name='home'),
    path('student-list/', views.StudentListView.as_view(), name='student-list'),
    path('student-detail/<int:pk>', views.StudentDetailView.as_view(), name='student-detail'),
]