from django.urls import path
from . import views

urlpatterns = [
    path('createlist', views.createlist, name = 'createlist'),
    path('deletelist/<int:list>', views.deletelist, name = 'deletelist'),
    path('deletelistconfirm/<int:list>', views.deletelistconfirm, name = 'deletelistconfirm'),
    path('', views.lists, name = 'lists'),
    path('tasks/<int:list>', views.index, name = 'index'),
    path('details/<int:list>/<int:id>', views.details, name = 'details'),
    path('edit/<int:list>/<int:id>', views.edit, name = 'edit'),
    path('create/<int:list>', views.create, name = 'create'),
    path('delete/<int:list>/<int:id>', views.delete, name = 'delete'),
    path('check/<int:list>/<int:id>', views.check, name = 'check'),
]