from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('services/', views.service_list),
    path('services/<int:pk>/', views.service_detail),
    # path('users/', views.UserListView.as_view()),
    path('users/', views.user_list),
    path('users/<int:pk>/', views.user_detail),
    path('proyects/', views.proyect_list),
    path('proyects/<int:pk>', views.proyect_detail),
]
