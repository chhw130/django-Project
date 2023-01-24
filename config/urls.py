from django.contrib import admin
from django.urls import path, include

# from rooms.views import say_hello

urlpatterns = [
    path("admin/", admin.site.urls),
    path("rooms/", include("rooms.urls")),
    path("categories/", include("categories.urls")),
]
