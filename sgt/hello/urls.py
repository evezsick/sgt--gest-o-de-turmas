from django.urls import path
from . import views

urlpatterns = [
#    path('<str:name>', views.greet, name='greet'),
    path('<str:name>', views.gm, name='greet')
]

