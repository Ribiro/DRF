from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include('drfapp.urls')),
    path('', views.FirstView.as_view(), name='first-view'),
    path('api/token/', obtain_auth_token, name='obtain')
]
