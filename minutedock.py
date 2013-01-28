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
    self.current_entry = CurrentEntry(5)
    self.current_entry.attach(self)
    self.data = self.current_entry.data

    timer = timedelta(seconds=int(self.data['duration']))
    clock = datetime(1, 1, 1) + timer

    self.ind = appindicator.Indicator("minutedock-ubuntu", 
      "indicator-messages", 
      appindicator.CATEGORY_APPLICATION_STATUS)
    
    self.ind.set_status(appindicator.STATUS_ACTIVE)
    self.ind.set_attention_icon("indicator-messages-new")
    self.ind.set_icon_theme_path(os.path.realpath('.'))
    self.ind.set_icon("minutedock")
    self.ind.set_label("%02d:%02d" % (clock.hour, clock.minute))

    # create a menu
    self.menu = gtk.Menu()

    self.update_menu()

    self.ind.set_menu(self.menu)

  def update(self, data):
    self.data = data
    timer = timedelta(seconds=int(data['duration']))
    clock = datetime(1, 1, 1) + timer
    self.ind.set_label("%02d:%02d" % (clock.hour, clock.minute))
    self.update_menu()

  def update_menu(self):
    self.menu.hide()

    for i in self.menu.get_children():
      self.menu.remove(i)
    
    # create items for the menu - labels, checkboxes, radio buttons and images are supported:

    if self.data['timer_active']:
      item = gtk.MenuItem("Pause")
      item.show()
      self.menu.append(item)
    else:
      item = gtk.MenuItem("Start")
      item.show()
      self.menu.append(item)

    item.connect("activate", self.toggle_timer, self.data['timer_active'])

    image = gtk.ImageMenuItem(gtk.STOCK_QUIT)
    image.connect("activate", self.quit)
    image.show()
    self.menu.append(image)

    self.menu.show()

  def quit(self, widget, data=None):
    gtk.main_quit()

  def toggle_timer(self, widget, timer_active):
    if timer_active:
      self.current_entry.pause_timer()
    else:
      self.current_entry.start_timer()

def main():
  gtk.main()
  return 0

if __name__ == "__main__":
  indicator = MinutedockUbuntu()
  main()
