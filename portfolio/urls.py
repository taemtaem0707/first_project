from django.urls import path

from . import views


# urls -> views와 연결
urlpatterns = [
    path('', views.loading, name='loading'),
    path('main/', views.main, name='main'),
    path('info/', views.info, name='info'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('team_project/', views.team_project, name='team_project'),
    path('certificates/', views.certificates, name='certificates'),
    path('blog/', views.blog, name='blog'),
]