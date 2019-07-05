import csv
import datetime

from django.core.management.base import BaseCommand, CommandError
from django.utils.timezone import get_current_timezone
from edc_facility.import_holidays import import_holidays

from td_maternal.tests.load_maternal_data import hiv_neg_mother_options
from td_maternal.tests.load_maternal_data import hiv_pos_mother_options, create_mother


tz = get_current_timezone()


class Command(BaseCommand):
    help = 'Create participants'

    def add_arguments(self, parser):
        parser.add_argument(
            '--path',
            dest='path',
            default=None,
            help=('full path to CSV file. Default: app_config.'
                  'randomization_list_path'),
        )

    tz = get_current_timezone()
    format_dt = '%d-%b-%y %I:%M:%S.%f'
    format_d = '%d-%b-%y'

    def handle(self, *args, **options):
        import_holidays()
        path = options['path'] or '/home/django/td_temp_data.csv'
        options_ = {}
        try:
            with open(path, newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                count = 20
                omang = '1111211'

                for row in reader:
                    omang = '1111211'
                    omang = omang + str(count)
                    if row['current_hiv_status'] == 'Neg':
                        options_ = {
                            'current_hiv_status': row['current_hiv_status'],
                            'week32_test_date': self.convert_and_localize_date(row['week32_test_date']),
                            'consent_datetime': self.convert_and_localize_datetime(row['consent_datetime']),
                            'last_period_date': self.convert_and_localize_date(row['last_period_date']),
                            'edd_by_lmp': self.convert_and_localize_date(row['edd_by_lmp']),
                            'est_edd_ultrasound': self.convert_and_localize_date(row['est_edd_ultrasound']),
                            'infant_dob': self.convert_and_localize_datetime(row['infant_birth']),
                            'visit_code': row['visit_code'],
                            'bpd': row['bpd'],
                            'hc': row['hc'],
                            'ac': row['ac'],
                            'fl': row['fl']
                        }
                        create_mother(self, options=hiv_neg_mother_options,
                                      options_2=options_, omang=omang)
                    else:
                        options_ = {
                            'current_hiv_status': row['current_hiv_status'],
                            'week32_test_date': '',
                            'consent_datetime': self.convert_and_localize_datetime(row['consent_datetime']),
                            'last_period_date': self.convert_and_localize_date(row['last_period_date']),
                            'edd_by_lmp': self.convert_and_localize_date(row['edd_by_lmp']),
                            'est_edd_ultrasound': self.convert_and_localize_date(row['est_edd_ultrasound']),
                            'infant_dob': self.convert_and_localize_datetime(row['infant_birth']),
                            'visit_code': row['visit_code'],
                            'bpd': row['bpd'],
                            'hc': row['hc'],
                            'ac': row['ac'],
                            'fl': row['fl']
                        }
                        create_mother(self, options=hiv_pos_mother_options,
                                      options_2=options_, omang=omang)
                    count += 1
        except AttributeError as e:
            raise CommandError(e)

    def convert_and_localize_datetime(self, datetime_string=None):
        date_object = datetime.datetime.strptime(
            datetime_string, self.format_dt)
        date_obj = self.tz.localize(date_object)
        return date_obj

    def convert_and_localize_date(self, date_string=None):
        date_object = datetime.datetime.strptime(
            date_string, self.format_d)
        date_obj = self.tz.localize(date_object)
        return date_obj.date()
