from django.urls import path
from .views import BookApiView, TodoList, TodoListDetail

urlpatterns = [
    path('', BookApiView.as_view()),
    path('todo/', TodoList.as_view()),
    path('todo/<uuid:pk>/', TodoListDetail.as_view())
]