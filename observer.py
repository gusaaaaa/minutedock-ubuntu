class Subject(object):
  def __init__(self):
    self._observers = []

  def attach(self, observer):
    if not observer in self._observers:
      self._observers.append(observer)
                                                
  def detach(self, observer):
    try:
      self._observers.remove(observer)
    except ValueError:
      pass

  def notify(self, obj):
    for observer in self._observers:
      observer.update(obj)

