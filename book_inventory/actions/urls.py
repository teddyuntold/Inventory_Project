<<<<<<< HEAD
from django.urls import path
from .views import CreateActionView, UpdateDeleteActionView

urlpatterns = [
    path('actions/', CreateActionView.as_view(), name='task-list-create'),
    path('actions/<int:pk>/', UpdateDeleteActionView.as_view(), name='action-retrieve-update-delete'),
]
=======
from django.urls import path
from .views import CreateActionView, UpdateDeleteActionView

urlpatterns = [
    path('actions/', CreateActionView.as_view(), name='task-list-create'),
    path('actions/<int:pk>/', UpdateDeleteActionView.as_view(), name='action-retrieve-update-delete'),
]
>>>>>>> 59d377753d1f1b0d186c349bc7c3a802a07a04c2
