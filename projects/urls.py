#-*- coding:utf-8 -*-

from django.urls import path, re_path
from . import views

# namespace
app_name = 'projects'

urlpatterns = [
    # Create a project
    path('create/', views.ProjectCreateView.as_view(), name='project_create'),
    # Retrieve project list
    path('', views.ProjectListView.as_view(), name='project_list'),
    # Retrieve single project object
    re_path(r'^(?P<pk>\d+)/$', views.ProjectDetailView.as_view(), name='project_detail'),
    # Update a project
    re_path(r'^(?P<pk>\d+)/update/$', views.ProjectUpdateView.as_view(), name='project_update'),
    # Delete a project
    re_path(r'^(?P<pk>\d+)/delete/$', views.ProjectDeleteView.as_view(), name='project_delete')

    # # Create a project
    # path('create/', views.project_create, name='project_create'),
    # # Retrieve project list
    # path('', views.project_list, name='project_list'),
    # # Retrieve single project object
    # re_path(r'^(?P<pk>\d+)/$', views.project_detail, name='project_detail'),
    # # Update a project
    # re_path(r'^(?P<pk>\d+)/update/$', views.project_update, name='project_update'),
    # # Delete a project
    # re_path(r'^(?P<pk>\d+)/delete/$', views.project_delete, name='project_delete'),

]