from django.urls import path
from .import views

urlpatterns = [
    path("reference/", views.reference, name="reference"),
    path("reference/my_model/", views.my_model, name="save_data"),
    # path("reference/my_model/responce/", views.responce, name="responce"),
]