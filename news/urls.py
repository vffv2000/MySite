from . import views
from django.urls import path

urlpatterns = [
    path('', views.news_home,name='news_home'),
    path('<int:pk>', views.NewsDetailView.as_view(),name='news-detail')
]
