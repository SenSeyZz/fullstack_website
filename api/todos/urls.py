from django.urls import path

from . import views


urlpatterns = [
    path('', views.ListTodo.as_view()),
    path('<int:pk>/', views.DetailTodo.as_view()),
    path('back/<int:pk>', views.DataBack.as_view()),
    path('back/', views.DataBack.as_view()),
    path('back/delete/<int:pk>/', views.DeleteDataById.as_view()),

]