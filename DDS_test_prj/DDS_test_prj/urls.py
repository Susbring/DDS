from django.contrib import admin
from django.urls import path, include

from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.dds_list, name='dds_list'),
    path('new/', views.dds_form, name='dds_new'),
    path('edit/<int:pk>/', views.dds_form, name='dds_edit'),
    path('delete/<int:pk>/', views.delete_dds, name='dds_delete'),
    path('reference/', views.reference_dds, name='reference_dds'),
    path('status/', views.StatusListView.as_view(), name='status_list'),
    path('status/new/', views.StatusCreateView.as_view(), name='status_new'),
    path('status/edit/<int:pk>/', views.StatusUpdateView.as_view(), name='status_edit'),
    path('status/delete/<int:pk>/', views.StatusDeleteView.as_view(), name='status_delete'),

    # --- URL-адреса для Type ---
    path('type/', views.TypeListView.as_view(), name='type_list'),
    path('type/new/', views.TypeCreateView.as_view(), name='type_new'),
    path('type/edit/<int:pk>/', views.TypeUpdateView.as_view(), name='type_edit'),
    path('type/delete/<int:pk>/', views.TypeDeleteView.as_view(), name='type_delete'),

    # --- URL-адреса для Category ---
    path('category/', views.CategoryListView.as_view(), name='category_list'),
    path('category/new/', views.CategoryCreateView.as_view(), name='category_new'),
    path('category/edit/<int:pk>/', views.CategoryUpdateView.as_view(), name='category_edit'),
    path('category/delete/<int:pk>/', views.CategoryDeleteView.as_view(), name='category_delete'),

    # --- URL-адреса для Subcategory ---
    path('subcategory/', views.SubcategoryListView.as_view(), name='subcategory_list'),
    path('subcategory/new/', views.SubcategoryCreateView.as_view(), name='subcategory_new'),
    path('subcategory/edit/<int:pk>/', views.SubcategoryUpdateView.as_view(), name='subcategory_edit'),
    path('subcategory/delete/<int:pk>/', views.SubcategoryDeleteView.as_view(), name='subcategory_delete'),
]
