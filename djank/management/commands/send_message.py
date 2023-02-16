from django.utils import timezone
from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    def handle(self, *args, **options):
        print('Привет')
        # for all in DistributionList.objects.all():
        #     c = all.status
        #     if str(all.time) == '12:00:00':
        #         PeriodicTask.objects.create(
        #             name = 'periodic_task9',
        #             task = 'repeat_order_make',
        #             interval = IntervalSchedule.objects.get(every=10, period='seconds'),
        #             start_time=timezone.now(),
        #             args = c
        #         )
        #     else:
        #         print('АлваоылаоывгРПШГРЦУИШГФИТШФ')