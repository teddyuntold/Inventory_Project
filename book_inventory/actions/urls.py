from django.urls import path
from .views import CreateActionView, UpdateDeleteActionView

urlpatterns = [
    path('actions/', CreateActionView.as_view(), name='task-list-create'),
    path('actions/<int:pk>/', UpdateDeleteActionView.as_view(), name='action-retrieve-update-delete'),
]
