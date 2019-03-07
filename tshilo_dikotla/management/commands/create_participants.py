from django.core.management.base import BaseCommand, CommandError
from edc_facility.import_holidays import import_holidays

from td_maternal.tests.base_test_case import hiv_neg_mother_options
from td_maternal.tests.base_test_case import hiv_pos_mother_options, create_mother


class Command(BaseCommand):

    help = 'Create participants'

    def handle(self, *args, **options):
        import_holidays()
        try:
            count = 0
            while count < 16:
                omang = '111121110'
                omang = omang[:-len(str(count))] + str(count)
                if count % 2:
                    create_mother(hiv_pos_mother_options, omang=omang)
                else:
                    create_mother(hiv_neg_mother_options, omang=omang)
                count += 1
        except AttributeError as e:
            raise CommandError(e)
