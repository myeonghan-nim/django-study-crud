from django.urls import path
from . import views

urlpatterns = [
    # read
    path('', views.index),
    path('<int:id>/detail/', views.detail),
    
    # create
    path('new/', views.new),
    path('create/', views.create),

    # delete
    path('<int:id>/delete/', views.delete),

    # update
    path('<int:id>/edit/', views.edit),
    path('<int:id>/update/', views.update),
]