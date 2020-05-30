from django.urls import path
from tasks import views


urlpatterns = [

    path('',views.index,name="index"),
    path('TaskList',views.TaskList,name="list"),
    path('update_task/<str:pk>/',views.updatetask,name="update_task"),
    path('delete/<str:pk>/',views.deleteTask,name="delete"),
    path('UserProfile',views.UserProfile,name='Register'),
    path('user_login/',views.user_login,name='user_login'),

]
