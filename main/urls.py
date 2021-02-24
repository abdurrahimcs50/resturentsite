
from django.urls import path
from . import views

urlpatterns = [

	path('', views.index, name='home'),
	path('about/', views.about, name = 'aboutus'),
	path('contact/', views.contact, name = 'contacts'),
	path('shop/', views.shop, name = 'shop'),
	path('blog/', views.blogs, name = 'blogs'),
	#path('blogs/<int:blog_id>/', views.detail, name = 'detail'),

]