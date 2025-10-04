from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include

from accounts.views import RegisterView, ProfileDetails, ProfileUpdateView

urlpatterns =[
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('register/', RegisterView.as_view(), name='register'),
    path('<int:pk>/', include([
        path('details/', ProfileDetails.as_view(), name='profile-details'),
        path('edit/', ProfileUpdateView.as_view(), name='profile-edit'),
    ]))
]