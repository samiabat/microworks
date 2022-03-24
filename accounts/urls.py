from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)




urlpatterns = [
    path('profile/', views.profileApi, name = 'profile'),
    path('proposals/', views.proposalApi, name = "proposals"),
    path('proposals/<str:pk>/', views.proposalApi, name = "proposals"),
    path('jobs/', views.jobApi, name = "jobs"),
    path('jobs/<str:pk>/', views.jobApi, name = "jobs"),
    path('customers/', views.customerApi, name = "customer"),
    path('customers/<str:pk>/', views.customerApi, name = "customer"),
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]


urlpatterns = format_suffix_patterns(urlpatterns)