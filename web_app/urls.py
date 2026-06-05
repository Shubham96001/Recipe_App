from django.urls import path
from web_app import views

urlpatterns = [
    path('', views.recipe_list, name='recipe_list'),
    path('add/', views.recipe_create, name='recipe_create'),
    path('recipe/<int:pk>/', views.recipe_detail, name='recipe_detail'),
    path('api/recipe/<int:pk>/update/', views.recipe_update_ajax, name='recipe_update_ajax'),
    path('api/recipe/<int:pk>/delete/', views.recipe_delete_ajax, name='recipe_delete_ajax'),
]
