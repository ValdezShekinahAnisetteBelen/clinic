from django.urls import path 
from . import views
from django.conf import settings  # Add this import

urlpatterns = [
    path('', views.index, name='index'),
    path('booking', views.booking, name='booking'),
    path('booking-submit', views.bookingSubmit, name='bookingSubmit'),
    path('user-panel', views.userPanel, name='userPanel'),
    path('user-update/<int:id>', views.userUpdate, name='userUpdate'),
    path('user-update-submit/<int:id>', views.userUpdateSubmit, name='userUpdateSubmit'),
    path('staff-panel', views.staffPanel, name='staffPanel'),
    path('userAccounts', views.userAccounts, name='userAccounts'),
    path('edit-status/<int:id>', views.editStatus, name='editStatus'),
    path('delete-account/<int:id>', views.deleteAccount, name='deleteAccount'),
]

from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
