from django.urls import path
from .views import todoView
urlpatterns = [
    path('', todoView.as_view(),name= "todo_home")
]