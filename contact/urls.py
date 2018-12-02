from django.urls import path, include
from contact import views

urlpatterns = [
    path('ensure_csrf/', views.ensure_csrf),
    path('contact_me/', views.ContactList.as_view()),
    path('contact_me/<int:pk>', views.ContactDetail.as_view())
]
