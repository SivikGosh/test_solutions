from django.db import models
from django.http import HttpResponse

from school_library.models import Book


def some_queryset(request):
    queryset1 = Book.objects.filter(
        models.Q(author_id__in=(2, 3, 5)) | models.Q(is_active=True)
    )
    queryset2 = Book.objects.filter(
        models.Q(author_id__in=(7, 8, 9)) | models.Q(is_active=True)
    )
    union_queryset = queryset1.union(queryset2)

    print(union_queryset.query)  # распечатать в терминале

    return HttpResponse(union_queryset.query)
