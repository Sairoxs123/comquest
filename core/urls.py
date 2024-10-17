from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name="home"),
    path("thanks/", thanks, name="thanks"),
    path("owner/", admin, name="owner")
]
