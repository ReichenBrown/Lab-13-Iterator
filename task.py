class Task:
  def __init__(self, desc, date, time):
    self._desc = desc
    self._date = date
    self._time = time

  @property
  def date(self):
    return self._date
    
  def __str__(self):
    return self._desc + "\n- Due: " + self._date + " at " + self._time

  def __repr__(self):
    return self._desc + "," + self._date + "," + self._time

  def __lt__(self, other):
    selfdate = self._date.split("/")
    otherdate = other._date.split("/")
    selftime = self._time.split(":")
    othertime = other._time.split(":")
    descs = [self._desc, other._desc]
    descs.sort()

    if (selfdate[2], selfdate[0], selfdate[1], selftime[1], selftime[0], self._desc) <= (otherdate[2], otherdate[0], otherdate[1], othertime[1], othertime[0], descs[0]):
      return True
    return False