#!/usr/bin/python3

import pgi
pgi.install_as_gi()

import os
import sys
import sched, time

from gi.repository import Notify, Gtk, GdkPixbuf
from random import randint
from datetime import datetime, timedelta

MAX_IMAGES = 2
DELAY = 900  # in seconds
PRIORITY = 1


if len(sys.argv) > 1:
    DELAY = int(sys.argv[1])

print('DELAY:', DELAY, 'seconds')

path = os.getcwd()
image_path = "{path}/images/agua_{image}.jpg"

s = sched.scheduler(time.time, time.sleep)

Notify.init("Drink")
notice = Notify.Notification.new(
    "Time to Hydrate",
    "Take a break and have some water",
    image_path.format(
        path=path,
        image=randint(1, MAX_IMAGES)
    )
)

def showAlert():
    notice.show()

    icon = image_path.format(
        path=path,
        image=randint(1, MAX_IMAGES)
    )
    pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size(icon, 25, 25)

    notice.set_icon_from_pixbuf(icon=pixbuf)

    now = datetime.now()
    next_notice = now + timedelta(seconds=DELAY)

    print('next notice:', next_notice.strftime('%H:%M:%S - %d/%m/%Y'))
    s.enter(DELAY, PRIORITY, showAlert)

s.enter(1, PRIORITY, showAlert)
s.run()
