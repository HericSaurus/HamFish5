from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # blog section urls
    path('', include('blog.urls')),
]
