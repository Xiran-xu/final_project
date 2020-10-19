from django.urls import path

from . import views

app_name='squirrel'

urlpatterns = [
        path('',views.index),
        path('<int:squirrel_id>/',views.detail,name='detail'),
        path('<int:squirrel_id>/update/',views.update,name='update'),
]
