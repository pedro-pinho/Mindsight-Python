from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('MindsightPython.core.urls', namespace='core')),
    path('admin/', admin.site.urls),
    path('employees/', include('MindsightPython.api.urls', namespace='api')),
]