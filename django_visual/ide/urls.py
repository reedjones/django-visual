from django.urls import re_path, path

from . import views

urlpatterns = [
    path('create_project/', views.create_project, name='create_project'),

    re_path(r'open_project/(?P<project_id>\w+)/run_project/', views.run_project, name='run_project'),
    re_path(r'open_project/(?P<project_id>\w+)/stop_project/', views.stop_project, name='stop_project'),
    re_path(r'open_project/(?P<project_id>\w+)/create_application/', views.create_application,
            name='create_application'),
    re_path(r'open_project/(?P<project_id>\w+)/remove_application/', views.remove_application,
            name='remove_application'),
    re_path(r'open_project/(?P<project_id>\w+)/add_application/', views.add_application, name='add_application'),
    re_path(r'open_project/(?P<project_id>\w+)/add_model/', views.add_model, name='add_model'),
    re_path(r'open_project/(?P<project_id>\w+)/', views.open_project, name='open_project'),

    path('open_file/', views.open_file, name='open_file'),
    path('save_file/', views.save_file, name='save_file'),

    path('welcome/', views.index, name='index'),
]
