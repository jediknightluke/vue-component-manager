from django.urls import path
from .views import RegisterView, LoginView, NoteCardCreateView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('note-cards/', NoteCardCreateView.as_view(), name='note-cards'),
]
