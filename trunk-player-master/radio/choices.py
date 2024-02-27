

RADIO_TYPE_MOBILE = 'M'
RADIO_TYPE_PORTABLE = 'P'
RADIO_TYPE_BASE = 'B'
RADIO_TYPE_DISPATCH = 'D'
RADIO_TYPE_CHOICES = (
    (RADIO_TYPE_MOBILE, 'Mobile'),
    (RADIO_TYPE_PORTABLE, 'Portable'),
    (RADIO_TYPE_BASE, 'Base'),
    (RADIO_TYPE_DISPATCH, 'Dispatch'),
)

TG_MODE_ANALOG = 'A'
TG_MODE_DIGITAL = 'D'
TG_MODE_ENCRYPTED = 'E'
TG_MODE_CHOICES = (
    (TG_MODE_ANALOG, "Analog"),
    (TG_MODE_DIGITAL, "Digital"),
    (TG_MODE_ENCRYPTED, "Encrypted"),
)

MESG_ALL_PAGES = 'A'
MESG_HOME_PAGE = 'H'

MESG_CHOICES = (
    (MESG_ALL_PAGES, 'All Pages'),
    (MESG_HOME_PAGE, 'Home Page'),
)
