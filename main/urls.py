from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('todo_list/', views.list_todo_items),
    path('insert_todo/', views.insert_todo_item, name='insert_todo_item'),
    path('delete_todo/<int:todo_id>/', views.delete_todo_item, name='delete_todo_item'),
    path('completed_todo/<int:todo_id>/', views.complete_todo_item, name='complete_todo_item'),
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
]
