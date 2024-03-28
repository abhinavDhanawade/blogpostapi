import os
import sys

ENABLE_PRODUCTION = os.environ.get('ENABLE_PRODUCTION', 'FALSE')


if ENABLE_PRODUCTION == 'TRUE':
    from .prod import *

elif ENABLE_PRODUCTION == 'FALSE':
    from .dev import *