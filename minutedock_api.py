import urllib2
import json
import os

class MinutedockApi:
  URL_BASE = 'https://minutedock.com/api/v1'

  def __init__(self, api_key = None):
    if api_key is None:
      self.api_key = os.environ.get('MINUTEDOCK_KEY')
      if self.api_key is None:
          raise KeyError, "Environment variable MINUTEDOCK_KEY must be set prior to execution. See your profile page for more info."
    else:
      self.api_key = api_key

  def get_current_entry(self):
    response = urllib2.urlopen(self.URL_BASE + '/entries/current.json?api_key=' + self.api_key).read()
    return json.loads(response)

  def start_current_entry_timer(self):
    # The second, empty, parameter forces a POST request.
    response = urllib2.urlopen(self.URL_BASE + '/entries/current/start.json?api_key=' + self.api_key, "").read()
    return json.loads(response)

  def pause_current_entry_timer(self):
    response = urllib2.urlopen(self.URL_BASE + '/entries/current/pause.json?api_key=' + self.api_key, "").read()
    return json.loads(response)

  def log_current_entry(self):
    response = urllib2.urlopen(self.URL_BASE + '/entries/current/log.json?api_key=' + self.api_key, "").read()
    return json.loads(response)

