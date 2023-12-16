from django.contrib import admin
from django.urls import path

from django.urls import include
urlpatterns = [
    path('admin/', admin.site.urls),
    # Enter the app name in following
    # syntax for this to work
    path('',include('crud_blog_web.urls'))
    ]
