from django.conf.urls import url
from datamaticsConsole import views

urlpatterns = [
    url(r'^$', views.Home),
    url(r'^search/', views.Search, name='search'),
    url(r'^analyze/', views.Analyze, name='analyze'),
    url(r'^filterEntries/', views.filterEntries, name='filterEntries'),
]