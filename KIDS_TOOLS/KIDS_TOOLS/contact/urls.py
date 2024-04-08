from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views

app_name = 'contact'

# user Router
contact_router = DefaultRouter()


urlpatterns = [
    path('', include(contact_router.urls)),
    path('data', views.DataView.as_view(), name='data_upload'),

    path('list', views.ContactListView.as_view(), name='contact_list'),
    path('sort', views.ContactSortView.as_view(), name='contact_sort'),

    path('search/<int:pk>/', views.ContactDetailSearchView.as_view(), name='contact-search'),

    path('create', views.ContactCreateView.as_view(), name='contact-create'),


]