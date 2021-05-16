LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,

    'formatters': {
        'console_debug': {
            'format': '%(asctime)s %(levelname)s %(message)s'
        },
        'console_warning': {
            'format': '%(asctime)s %(levelname)s %(message)s %(pathname)s'
        },
        'console_error': {
            'format': '%(asctime)s %(levelname)s %(message)s %(pathname)s %(exc_info)s'
        },
        'general': {
            'format': '%(asctime)s %(levelname)s %(module)s %(message)s'
        },
        'errors': {
            'format': '%(asctime)s %(levelname)s %(message)s %(pathname)s %(exc_info)s'
        }
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        }
    },

    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'console',
            'filters': ['require_debug_true']
        },
        'console_warning': {
            'level': 'WARNING',
            'class': 'logging.StreamHandler',
            'formatter': 'console_warning',
            'filters': ['require_debug_true']
        },
        'console_error': {
            'level': 'ERROR',
            'class': 'logging.StreamHandler',
            'formatter': 'console_error',
            'filters': ['require_debug_true']
        },
        'fileGeneral': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'formatter': 'general',
            'filename': 'general.log',
            'filters': ['require_debug_true']
        },
        'fileErrors': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'formatter': 'errors',
            'filename': 'errors.log',
        },
        'fileSecurity': {
            'class': 'logging.FileHandler',
            'formatter': 'general',
            'filename': 'security.log'
         },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'filters': ['require_debug_false'],
            'formatter': 'console_warning'
        }
    },
    'loggers': {
        'django': {
            'handlers':['console', 'console_warning', 'console_error', 'fileGeneral'],
            'propagate': True,
        },
        'django.request': {
            'handlers': ['fileErrors', 'mail_admins'],
            'level': 'ERROR',
            'propagate': False
        },
        'django.server': {
            'handlers': ['fileErrors', 'mail_admins'],
            'level': 'ERROR',
            'propagate': False
        },
        'django.template': {
            'handlers': ['fileErrors'],
            'level': 'ERROR',
            'propagate': False
        },
        'django.db_backenends': {
            'handlers': ['fileErrors'],
            'level': 'ERROR',
            'propagate': False
        },
        'django.security': {
            'handlers': ['fileSecurity'],
            'propagate': False
        }
    }
}