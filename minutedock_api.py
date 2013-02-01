import urllib
import urllib2
import json
import os

class MinutedockApi:
  URL_BASE = 'https://minutedock.com/api/v1'

  def __init__(self, api_key = None):
    if api_key is None:
      self.api_key = os.environ['MINUTEDOCK_KEY']
    else:
      self.api_key = api_key

  def get_current_entry(self):
    response = urllib.urlopen(self.URL_BASE + '/entries/current.json?api_key=' + self.api_key).read()
    return json.loads(response)

  def start_current_entry_timer(self):
    response = urllib2.urlopen(self.URL_BASE + '/entries/current/start.json?api_key=' + self.api_key, "").read()

  def pause_current_entry_timer(self, entry_id):
    response = urllib2.urlopen(self.URL_BASE + "/entries/%s/pause.json?api_key=%s" % (entry_id, self.api_key), "").read()

  def log_current_entry(self):
    response = urllib.urlopen(self.URL_BASE + '/entries/current/log.json?api_key=' + self.api_key)

