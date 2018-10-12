#!/usr/bin/python3

import pgi
pgi.install_as_gi()

import argparse
import os
import sched
import sys
import time

from datetime import datetime, timedelta
from gi.repository import Notify, Gtk, GdkPixbuf
from random import randint

DELAY = 1200  # in seconds
MAX_IMAGES = 2
PRIORITY = 1


parser = argparse.ArgumentParser(description='Hydrate')
parser.add_argument('beverage',
    type=str, choices=['water', 'coffee'], help='Select a beverage to notification')
parser.add_argument('-d', '--delay',
    type=int, help='Set an integer, a delay for notification')
# parser.add_argument('-t', '--time',
#     type=str, help='Set a time for notification in the format HH:MM:SS')

path = os.getcwd()
water_image_path = "{path}/images/water_{image}.jpg"
coffee_image_path = "{path}/images/coffee_{image}.jpg"

Notify.init("Drink")


def showAlert(beverage, delay):
    image_path = water_image_path if beverage == "water" else coffee_image_path

    notice = Notify.Notification.new(
        "Time to Hydrate",
        f"Take a break and have some {beverage}",
        image_path.format(
            path=path,
            image=randint(1, MAX_IMAGES)
        )
    )
    notice.show()

    icon = image_path.format(
        path=path,
        image=randint(1, MAX_IMAGES)
    )
    pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size(icon, 400, 400)

    notice.set_icon_from_pixbuf(icon=pixbuf)

    now = datetime.now()
    next_notice = now + timedelta(seconds=DELAY)

    print('next notice:', next_notice.strftime('%H:%M:%S - %d/%m/%Y'))
    s.enter(delay, PRIORITY, showAlert, argument=(beverage, delay))


if __name__ == "__main__":
    parse = parser.parse_args()
    beverage = parse.beverage
    delay = parse.delay

    s = sched.scheduler(time.time, time.sleep)
    s.enter(1, PRIORITY, showAlert, argument=(beverage, delay))
    s.run()
