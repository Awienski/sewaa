from django.urls import path
from . import views

app_name = 'product'


urlpatterns = [
    path('', views.index, name='index'),
    path('product_category/<category>/', views.product_category, name='product_category'),
    path('<int:id>/', views.detail, name='detail'),
    path('loanedprodcuctbyuser/', views.loanedprodcuctbyuser, name='loanedprodcuctbyuser'),
    path('sewaa/<int:id>', views.sewaa, name='sewaa'),
    path('profile/', views.profile, name='profile'),
    path('about/', views.about, name='about'),
    path('add/', views.add, name='add'),
    path('update/<int:id>', views.update, name='update'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('productchatdetail/<int:id>/', views.productchatdetail, name='productchatdetail'),
    path('chat/<int:id>/', views.chat, name='chat'),
]