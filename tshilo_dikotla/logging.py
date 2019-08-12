# see http://www.simonkrueger.com/2015/05/27/logging-django-apps-to-syslog.html
import os

APP_NAME = 'tshilo_dikotla'

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'formatters': {
        'verbose': {
            'format': '%(process)-5d %(thread)d %(name)-50s %(levelname)-8s %(message)s'
        },
        'simple': {
            'format': '[%(asctime)s] %(name)s %(levelname)s %(message)s',
            'datefmt': '%d/%b/%Y %H:%M:%S'
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'log', f'{APP_NAME}-django-debug.log'),
        },
        #         'console': {
        #             'level': 'DEBUG',
        #             'filters': ['require_debug_true'],
        #             'class': 'logging.StreamHandler',
        #             'formatter': 'simple'
        #         },
        'syslog': {
            'level': 'DEBUG',
            'class': 'logging.handlers.SysLogHandler',
            'facility': 'local7',
            'address': '/dev/log',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
        # root logger
        '': {
            'handlers': ['syslog'],
            'level': 'INFO',
            'disabled': False
        },
        'cancer': {
            'handlers': ['syslog'],
            'level': 'DEBUG',
            'propagate': False,
        },
    },
}
