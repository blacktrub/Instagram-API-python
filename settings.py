LOGGING_SETTINGS = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '[%(asctime)s: %(levelname)s/%(name)s] %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'error_file': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': '/var/log/instagram_api.log',
            'maxBytes': 1024 * 1024 * 100,  # 5 MB
            'backupCount': 7,
            'formatter': 'verbose',
        },
        'access_file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': '/var/log/instagram_api.log',
            'maxBytes': 1024 * 1024 * 100,  # 5 MB
            'backupCount': 7,
            'formatter': 'verbose',
        },
    },
    'loggers': {
        '': {
            'handlers': ['error_file', 'access_file'],
            'level': "INFO",
        },
    }
}
