from django.urls import path
from .views import *
from . import views

app_name="summer"
urlpatterns = [
    path('', views.movie_list_create),
    path('<int:movie_pk>/', views.movie_detail_update_delete),
    path('comment/', views.comment_list),
    path('comment/<int:comment_pk>', views.comment_detail),
    path('<int:comment_pk>/comments/', views.comment_create),
]
