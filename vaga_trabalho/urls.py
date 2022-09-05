"""vaga_trabalho URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from other.logged import Logged
from other.search import Search
from user.api import viewsets as userviewsets
from vacancy.api import viewsets as vacancyviewsets
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

route = routers.DefaultRouter()
route.register(r'api/user', userviewsets.UserViewSet, basename='Users')
route.register(r'api/vacancy', vacancyviewsets.VacancyViewSet, basename='Vacancy')

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/authentication/login/", TokenObtainPairView.as_view(), name= 'token_obtain_pair'),
    path("api/authentication/refresh/", TokenRefreshView.as_view(), name='token_refresh'),
    path("api/vacancy/keyword/", Search.as_view(),),
    path("api/user/me/", Logged.as_view(),),
    path("", include(route.urls)),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "docs/",
        SpectacularSwaggerView.as_view(
            template_name="swagger-ui.html", url_name="schema"
        ),
        name="swagger-ui",
    ),
]
