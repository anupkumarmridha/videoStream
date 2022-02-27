"""exhabition URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from home import views
from home.views import homeView, AddPostView, VideoDetailsView, UpdatePostView, DeletePostView, AddCategoryView

urlpatterns = [
    path('', homeView.as_view(), name='homeView'),
    
    #Product Url
    path('Add_Video/', AddPostView.as_view(), name='Add_Video'),
    path('add_comment/<int:pk>', views.AddComment, name='add_comment'),
    path('Video/<int:pk>', VideoDetailsView.as_view(), name='Video_Details'),
    path('Video/Edit/<int:pk>', UpdatePostView.as_view(), name='Update_Video'),
    path('Video/Delete/<int:pk>', DeletePostView.as_view(), name='Delete_Video'),
    path('Add_Category/', AddCategoryView.as_view(), name='add_category'),
    path('category/<str:cats>', views.CategoryView, name='category'),
    path('categoroy_list',views.CategoryListView , name='category_list'),
    
    #Regestration    
    path('signup/', views.handelSingup, name='handelSingup'),
    path('login', views.handleLogin, name='handleLogin'),
    path('logout', views.handleLogout, name='handleLogout'),
    
]
