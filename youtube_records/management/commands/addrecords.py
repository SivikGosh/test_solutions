from django.core.management.base import BaseCommand
from progress.bar import Bar

from youtube_records.models import Record


class Command(BaseCommand):
    help = 'Заполнение тестовыми записями'

    def add_arguments(self, parser):
        parser.add_argument(
            'amount', type=int, help='Кол-во добавляемых записей'
        )

    def handle(self, *args, **kwargs):
        records = []
        amount = kwargs['amount']
        bar = Bar(max=amount)
        for i in range(1, amount):
            records.append(Record(name=f'Запись № {i}'))
            bar.next()
        bar.finish()
        Record.objects.bulk_create(records)
