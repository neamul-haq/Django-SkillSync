from django.urls import path, include
from . import views
urlpatterns = [
    path('add/', views.AddProjectCreateView.as_view(), name='add_project'),
    path('add_rating/<int:project_id>/', views.AddRating, name='add_rating'),
    path('details/<int:id>/', views.DetailProjectView.as_view(), name='detail_project'),
]