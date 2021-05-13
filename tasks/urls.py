from django.urls import path
from tasks import views
urlpatterns=[
    path('',views.index,name="index"),
    path('<int:category_id>',views.categorical_list,name="categorical_list"),
    path('<int:category_id>/<int:task_id>',views.task,name="task"),
    path('delete/<int:category_id>',views.delete_category,name='delete_category'),
    path('<int:category_id>/delete/<int:task_id>',views.delete_task,name='delete_task'),
    path('<int:category_id>/mark_as_complete/<int:task_id>',views.mark_task_as_complete,name='mark_task_as_complete'),
    
]