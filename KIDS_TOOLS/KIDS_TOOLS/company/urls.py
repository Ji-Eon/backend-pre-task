from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views
from rest_framework_jwt.views import obtain_jwt_token

app_name = 'company'

# user Router
company_router = DefaultRouter()


urlpatterns = [
    path('', include(company_router.urls)),

]