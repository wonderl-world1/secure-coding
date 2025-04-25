from django.urls import path
from .views import (
    UserSignupView, UserLoginView, UserInfoView,
    ProductListCreateView, ProductDetailView,
    ChatMessageView, BlockUserView, PaymentView,
    ProductSearchView, AdminUserBlockToggleView
)

urlpatterns = [
    path('signup/', UserSignupView.as_view(), name='signup'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('me/', UserInfoView.as_view(), name='user-info'),

    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),

    path('chat/', ChatMessageView.as_view(), name='chat'),
    path('block/', BlockUserView.as_view(), name='block'),
    path('pay/', PaymentView.as_view(), name='payment'),
    path('search/', ProductSearchView.as_view(), name='search'),

    path('admin/block-toggle/<int:user_id>/', AdminUserBlockToggleView.as_view(), name='admin-block-toggle'),
]
