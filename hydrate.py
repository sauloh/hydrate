#!/usr/bin/python

from gi.repository import Notify
from gi.repository import Gtk
import sched, time

s = sched.scheduler(time.time, time.sleep)

Notify.init("Drink")
notice = Notify.Notification.new(
    'Time to Hydrate',
    'Take a break and have some water',
    None
)

def showAlert(sc):
    notice.show()
    s.enter(900, 1, showAlert, (s,))
    

s.enter(900, 1, showAlert, (s,))
s.run()
