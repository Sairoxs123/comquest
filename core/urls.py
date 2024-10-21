from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name="home"),
    path("thanks/", thanks, name="thanks"),
    path("owner/login/", owner_login, name="owner_login"),
    path("owner/", owner, name="owner"),
    path("rubric/", rubric, name="rubric")
]
