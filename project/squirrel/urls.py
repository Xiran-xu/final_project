from django.urls import path

from . import views

app_name='squirrel'

urlpatterns = [
        path('',views.index),
        path('<int:squirrel_id>/',views.update,name='update'),
        path('add/',views.add,name='add'),
]
