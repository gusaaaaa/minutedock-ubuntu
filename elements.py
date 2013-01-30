from minutedock_api import MinutedockApi
from observer import Subject

import time
import signal

class CurrentEntry(Subject):

  def __init__(self, polling_interval=15):
    Subject.__init__(self)
    self.__api = MinutedockApi()

    # store current entry in data instance variable
    self.data = self.__api.get_current_entry()
    signal.signal(signal.SIGALRM, self.__poll_server)
    signal.setitimer(signal.ITIMER_REAL, polling_interval, polling_interval)
    
  def start_timer(self):
    self.__api.start_current_entry_timer()

  def pause_timer(self):
    self.__api.pause_current_entry_timer(self.data['id'])
  
  # def log:

  def __poll_server(self, signum, frame):
    # store current entry in data instance variable
    self.data = self.__api.get_current_entry()
    self.notify(self.data)

if __name__ == "__main__":
  class TestPolling(object):
    def update(self, data):
      print data['duration']

  ce = CurrentEntry(5)
  ce.attach(TestPolling())
  while True:
    time.sleep(5)
