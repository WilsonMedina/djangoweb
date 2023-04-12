from django.urls import path
from django.contrib.auth.decorators import login_required
#-----------------------------------Own files-----------------------------------------------#
from .views import HomeBlogView, ReadPostView, ListPostsView, DashboardView, UpdatePostView, CreatePostView, DeletePostView, UpdatePhotoView, UpdateProfileView

urlpatterns = [
    path('', HomeBlogView.as_view(), name='home_blog'),
    path('read-post/<int:pk>/', ReadPostView.as_view(), name='read_post'),
    path('list-posts/<int:pk>/', ListPostsView.as_view(), name='list_posts'),
    path('dashboard/', login_required(DashboardView.as_view()), name='dashboard'),
    path('update-post/<int:pk>/', login_required(UpdatePostView.as_view()), name='update_post'),
    path('create-post/', login_required(CreatePostView.as_view()), name='create_post'),
    path('delete-post/<int:pk>/', login_required(DeletePostView.as_view()), name='delete_post'),
    path('update-photo/<int:pk>/', login_required(UpdatePhotoView.as_view()), name='update_photo'),
    path('update-profile/<int:pk>/', login_required(UpdateProfileView.as_view()), name='update_profile'),
]
