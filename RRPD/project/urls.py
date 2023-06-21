from django.urls import path

from . import views

urlpatterns = [
    path("createProject/", views.projectCreate, name="create_project"),
    path("save_data/", views.save_data, name="Save_Data"),
]