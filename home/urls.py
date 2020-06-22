
from django.urls import include, path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('synthesis/', include(('synthesis.urls', 'synthesis'), namespace='synthesis')),
    path('design/', include(('design.urls', 'design'), namespace='design')), 
    path('admin/', admin.site.urls)]