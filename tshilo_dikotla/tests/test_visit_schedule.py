from django.test import TestCase

from edc_visit_schedule import site_visit_schedules


class TestSubjectConsent(TestCase):

    def setUp(self):
        pass

    def test_visit_schedule(self):
        print('********************** Printing Visit Schedules **********************')
        print(site_visit_schedules.visit_schedules())
