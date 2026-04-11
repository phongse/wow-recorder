import os

CWD = os.path.dirname(__file__)

NAME = "raid_reset"
LOG = f"{CWD}/../../logs/retail/{NAME}.txt"
OVERRUN = 15  # ENCOUNTER_END non-kills use raid overrun.
SLEEPS = {
    "ENCOUNTER_END": 2,
}
