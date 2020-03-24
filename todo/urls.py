from django.urls import path
from . import views
app_name = "todo"
urlpatterns = [
    path('', views.index, name="index"),
    path('add', views.add_todo, name="add"),
    path('complete/<int:todo_id>', views.complete_todo, name="complete"),
    path('deletecomplete', views.delete_completed, name="delete_complete")
]
