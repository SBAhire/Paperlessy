from django.urls import path
from tasks import views
urlpatterns=[
    path('',views.index,name="index"),
    path('<int:category_id>',views.categorical_list,name="categorical_list"),
    path('<int:category_id>/<int:task_id>',views.task,name="task"),
    path('delete/<int:category_id>',views.delete_category,name='delete_category'),
    path('<int:category_id>/delete/<int:task_id>',views.delete_task,name='delete_task'),
    path('<int:category_id>/mark_as_complete/<int:task_id>',views.mark_task_as_complete,name='mark_task_as_complete'),
    path('api/',views.api_overview,name='API'),
    path('api/categories',views.api_category_list,name="Category_list_api"),
    path('api/<int:category_id>/',views.api_tasks,name='Tasks_list_api'),
    path('api/<int:category_id>/<int:task_id>/',views.api_task,name='Tasks_list_api'),
    path('api/create-category/',views.api_create_category,name='Create_category_api'),
    path('api/delete-category/<int:category_id>',views.api_delete_category,name='Delete_category_api'),
    path('api/<int:category_id>/create-task/',views.api_create_task,name='Create_task_api'),
    path('api/<int:category_id>/delete-task/<int:task_id>/',views.api_delete_task,name='Delete_task_api'),


]