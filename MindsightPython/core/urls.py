from django.contrib import admin
from django.urls import include, path
from rest_framework.urlpatterns import format_suffix_patterns

from MindsightPython import core
from MindsightPython.core import views 

app_name = 'core'
urlpatterns = [
    path('', core.views.home , name='home'),
    path('api/', include('MindsightPython.api.urls', namespace='api'))
]
urlpatterns = format_suffix_patterns(urlpatterns)