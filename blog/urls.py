from django.urls import path
from . import views
from .views import PostListView, CreatePostView, DeletePostView,UpdatePostView


app_name = 'blog'
urlpatterns = [
    path('blog/', PostListView.as_view(), name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
         views.post_detail,
         name='post_detail'),
    path('blog/add/', CreatePostView.as_view(), name='post_add'),
    path('blog/<int:pk>/update', UpdatePostView.as_view(), name='update_post'),
    path('blog/<int:pk>/delete', DeletePostView.as_view(), name='post_delete')
]
