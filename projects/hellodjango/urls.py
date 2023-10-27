
from django.contrib import admin
from django.urls import path
from app.views import hello_views
urlpatterns = [
    path('hello/', hello_views),
    path('admin/', admin.site.urls),
]
