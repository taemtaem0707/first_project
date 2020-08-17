from django.urls import path
from . import views

# urls -> views와 연결
urlpatterns = [
    path('main/', views.main, name='main'),
    path('crawling/', views.crawling, name='crawling'),
    path('processing/', views.processing, name='processing'),
    path('visual/', views.visual, name='visual'),
    path('introduce/', views.introduce, name='introduce'),
    path('result/', views.result, name='result'),
    path('function/', views.function, name='function'),
    path('extension/', views.extension, name='extension')

]