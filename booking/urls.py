from django.urls import path
from . import views

urlpatterns = [
    path('', views.book, name='bookings'),
    path('index/', views.index, name='index'),
    path('start/<int:shiftId>/<int:branchId>', views.startShift, name='start'),
    path('delete_item/<int:pk>', views.deleteItem, name='deleteItem'),
    path('update_item/<int:pk>', views.updateItem, name='updateItem'),
    path('viewQueue/<int:branchId>', views.viewBranchQueue, name='viewBranchQueue'),
    path('setup/', views.setup),
    path('destroy/', views.destroy)
]
