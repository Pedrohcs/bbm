from django.urls import path
from book.views import BookAPIView


urlpatterns = [
    path('books', BookAPIView.as_view())
]