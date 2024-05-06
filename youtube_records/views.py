from django.http import HttpResponse
import time
from youtube_records.models import Record


def delete_records(request):
    start = time.time()

    Record.objects.all().adelete()  # как delete(), только асинхронное :)

    end = time.time()

    return HttpResponse(end - start)
