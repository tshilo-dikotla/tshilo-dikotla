from django.conf import settings
from edc_lab_dashboard.dashboard_urls import dashboard_urls as lab_dashboard_urls
from edc_navbar import NavbarItem, site_navbars, Navbar


tshilo_dikotla = Navbar(name='tshilo_dikotla')

tshilo_dikotla.append_item(
    NavbarItem(
        name='eligible_subject',
        label='Subject Screening',
        fa_icon='fa-user-plus',
        url_name=settings.DASHBOARD_URL_NAMES.get('screening_listboard_url')))

tshilo_dikotla.append_item(
    NavbarItem(
        name='maternal_subject',
        label='Maternal Subjects',
        fa_icon='far fa-user-circle',
        url_name=settings.DASHBOARD_URL_NAMES.get('subject_listboard_url')))


tshilo_dikotla.append_item(
    NavbarItem(
        name='infant_subject',
        title='Infant Subjects',
        label='Infant Subjects',
        fa_icon='far fa-user-circle',
        url_name=settings.DASHBOARD_URL_NAMES.get('infant_listboard_url')))

tshilo_dikotla.append_item(
    NavbarItem(
        name='odk_forms_subject',
        label='ODK Forms',
        fa_icon='fa fa-file-image',
        url_name=settings.DASHBOARD_URL_NAMES.get('odk_listboard_url')))

tshilo_dikotla.append_item(
    NavbarItem(
        name='export_data',
        label='Export Data',
        fa_icon='fa fa-file-export',
        url_name=settings.DASHBOARD_URL_NAMES.get('export_listboard_url')))


site_navbars.register(tshilo_dikotla)
