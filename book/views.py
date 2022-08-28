from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.response import Response

from book.models import Books
from book.serializers import BookSerializer


class BookAPIView(APIView):
    serializer_class = BookSerializer

    def post(self, request):
        book_data = JSONParser().parse(request)
        books_serializer = self.serializer_class(data=book_data)

        if books_serializer.is_valid():
            books_serializer.save()
            return Response({"message": "Added Successfully"}, status=status.HTTP_200_OK)
        return Response({"message": "Failed to Add"}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        book_id = request.query_params.get('book', None)

        if book_id:
            books = Books.objects.filter(id=book_id)
        else:
            books = Books.objects.all()

        if books:
            books_serializer = self.serializer_class(books, many=True)
            return Response(books_serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"message": "No books found"}, status=status.HTTP_200_OK)

    def put(self, request):
        book_id = request.query_params.get('book', None)

        book = Books.objects.get(id=book_id)

        if not book:
            return Response({"message": "No book found"}, status=status.HTTP_404_NOT_FOUND)

        name = request.data.get('name', None)
        author = request.data.get('author', None)
        quantity_pages = request.data.get('quantityPages', None)
        year_launch = request.data.get('yearLaunch', None)

        if name:
            book.name = name
        if author:
            book.author = author
        if quantity_pages:
            book.quantityPages = quantity_pages
        if year_launch:
            book.yearLaunch = year_launch

        book.save()

        return Response({"message": "Updated Successfully"}, status=status.HTTP_200_OK)

    def delete(self, request):
        book_id = request.query_params.get('book', None)
        book = Books.objects.get(id=book_id)

        if not book:
            return Response({"message": "No book found"}, status=status.HTTP_404_NOT_FOUND)

        book.delete()
        return Response({"message": "Book removed"}, status=status.HTTP_200_OK)
