import os
import logging
from logging.config import dictConfig
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Var to hold discord API token
DISCORD_API_SECRET = os.getenv("DISCORD_API_TOKEN")

# Logs directory path
LOGS_DIR = "logs"
LOGS_FILE = "Logs.log"

# Check if this is a first-time install and create logs directory if it doesn't exist
if not os.path.exists(LOGS_DIR):
    os.makedirs(LOGS_DIR)

LOGGING_CONFIG = {
    "version": 1,
    "disabled_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "%(levelname)-10s %(asctime)s %(module)-15s %(message)s)"
        },
        "standard": {
            "format": "%(levelname)-10s %(name)-15s %(message)s"
        }
    },
    "handlers": {
        "console": {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
        "console2": {
            'level': 'WARNING',
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
        "file": {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': os.path.join(LOGS_DIR, LOGS_FILE),
            'mode': 'w',
            'formatter': "verbose"
        }
    },
    "loggers": {
        "bot": {
            'handlers': ['console'],
            "level": "INFO",
            "propagate": False
        },
        "discord": {
            'handlers': ['console2', "file"],
            "level": "INFO",
            "propagate": False
        }
    }
}

dictConfig(LOGGING_CONFIG)