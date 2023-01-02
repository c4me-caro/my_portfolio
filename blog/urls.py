from django.urls import path
from .views import *

urlpatterns = [
    path("", index),
    path("post/<int:id>", render_post)
]