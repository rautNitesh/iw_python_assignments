from django.urls import path

from .views import home, blog, blog_detail


urlpatterns = [
    path('', home, name='home'),
    path('blog/', blog, name='blog'),
    path('blog/<int:post_id>', blog_detail, name='blog_detail'),
]
