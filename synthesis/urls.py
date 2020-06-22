from django.urls import path

from . import views

appname='synthesis'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:structure_id>/', views.detail, name='detail'),
    # path('<int:structure_id>/results/', views.results, name='results'),
    # path('<int:structure_id>/vote/', views.vote, name='vote'),
]