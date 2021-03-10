"""mkstowe.com development configuration."""

import pathlib

# Root of this application, useful if it doesn't occupy an entire domain
APPLICATION_ROOT = '/'

# File Upload to var/uploads/
MKSTOWE_ROOT = pathlib.Path(__file__).resolve().parent
STATIC_ROOT = MKSTOWE_ROOT/'static'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
MAX_CONTENT_LENGTH = 16 * 1024 * 1024

VARIEGATA_ROOT = MKSTOWE_ROOT/'variegata'
