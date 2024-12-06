from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', include('register.urls', namespace='register')),
    path('projects/', include('projects.urls', namespace='projects')),
    path('', include('core.urls', namespace='core')),
]
