from django.urls import path
from .views import Createtodo, createCategory, delete_task, index, detailed_task, login_view, logout_view, todo_by_status, category_tasks, update_task

urlpatterns = [
    path('/m', index, name="home"),
    path('detailed/<int:id>/', detailed_task, name="detail"),
    path('todos/status/<str:st>/', todo_by_status, name="status"),
    path('category/<int:category_id>/', category_tasks, name='category_tasks'),
    path('categopry/create' , createCategory , name='createcategory' ),
    path('todo/create' , Createtodo , name="createtodo"),
    path('todo/update/<int:id>' , update_task , name ="update-task"),
    path('todo/delete/<int:id>' , delete_task , name ="delete-task"),
    path('', login_view, name='login'),
    path('logout/', logout_view, name='logout'),  
]
