
from django.contrib import admin
from django.urls import path
from movies.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('list/', List, name= "list"),
]
