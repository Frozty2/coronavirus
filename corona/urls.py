from django.urls import path
from . import views

app_name = "corona"
urlpatterns = [
    path('', views.corona, name="corona"),
    path('details/', views.details, name="details")
]