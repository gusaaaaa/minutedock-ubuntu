#!/usr/bin/env python
#
# [SNIPPET_NAME: MinutedockUbuntu]
# [SNIPPET_CATEGORIES: Application Indicator]
# [SNIPPET_DESCRIPTION: Application Indicator for Minutedock]
# [SNIPPET_AUTHOR: Gustavo Armagno <gusa@neo.com>]
# [SNIPPET_DOCS: https://github.com/gusaaaaa/minutedock-ubuntu/blob/master/README.md]
# [SNIPPET_LICENSE: GPL]

import pygtk
pygtk.require('2.0')
import gtk
import appindicator
import urllib
import os.path

from elements import CurrentEntry
from datetime import datetime, timedelta

class MinutedockUbuntu:
  
  def __init__(self):
    current_entry = CurrentEntry(5)
    self.timer = timedelta(seconds=int(current_entry.data['duration']))
    self.datetime = datetime(1, 1, 1) + self.timer

    current_entry.attach(self)

    self.ind = appindicator.Indicator ("minutedock-ubuntu", 
      "indicator-messages", 
      appindicator.CATEGORY_APPLICATION_STATUS)
    self.ind.set_status (appindicator.STATUS_ACTIVE)
    self.ind.set_attention_icon ("indicator-messages-new")
    self.ind.set_icon("distributor-logo")
    self.ind.set_label("MinuteDock - {0}:{1}".format(self.datetime.hour, self.datetime.minute))

    # create a menu
    self.menu = gtk.Menu()

    image = gtk.ImageMenuItem(gtk.STOCK_QUIT)
    image.connect("activate", self.quit)
    image.show()
    self.menu.append(image)

    self.menu.show()

    self.ind.set_menu(self.menu)

  def update(self, data):
    self.timer = timedelta(seconds=int(data['duration']))
    self.datetime = datetime(1, 1, 1) + self.timer
    self.ind.set_label("MinuteDock - {0}:{1}".format(self.datetime.hour, self.datetime.minute))

  def quit(self, widget, data=None):
    gtk.main_quit()


def main():
  gtk.main()
  return 0

if __name__ == "__main__":
  indicator = MinutedockUbuntu()
  main()
