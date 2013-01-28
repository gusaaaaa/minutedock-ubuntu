import urllib
import json
import os

class MinutedockApi:
  # export MINUTEDOCK_KEY=cd43ee8819e1bcd47cf2edf321a29320
  URL_BASE = 'https://minutedock.com/api/v1'
  
  def __init__(self, api_key = None):
    if api_key is None:
      self.api_key = os.environ['MINUTEDOCK_KEY']
    else:
		  self.api_key = api_key

		# self.raw = urllib.request.urlopen('https://minutedock.com/api/v1/accounts/current.json?api_key=cd43ee8819e1bcd47cf2edf321a29320').read()

  def get_current_entry(self):
    response = urllib.urlopen(self.URL_BASE + '/entries/current.json?api_key=' + self.api_key).read()
    return json.loads(response)

  def start_current_entry_timer(self):
    response = urllib.urlopen(self.URL_BASE + '/entries/current/start.json?api_key=' + self.api_key)

  def pause_current_entry_timer(self):
    response = urllib.urlopen(self.URL_BASE + '/entries/current/pause.json?api_key=' + self.api_key)

  def log_current_entry(self):
    response = urllib.urlopen(self.URL_BASE + '/entries/current/log.json?api_key=' + self.api_key)

