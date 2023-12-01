from task import Task

class Tasklist:
  def __init__(self):
    self._tasklist = []
    file = open('task.txt', 'r')
    for line in file:
      info = line.strip().split(',')
      task = Task(info[0], info[1], info[2])
      self._tasklist.append(task)
      self._tasklist.sort()

  def add_task(self, desc, date, time):
    task = Task(desc, date, time)
    self._tasklist.append(task)
    self._tasklist.sort()

  def mark_complete(self):
    if self._tasklist:
      self._tasklist.pop(0)

  def save_file(self):
    file = open('task.txt', 'w')
    for task in self._tasklist:
      file.write(repr(task) + '\n')

  def __getitem__(self, index):
    return self._tasklist[index]

  def __len__(self):
    return len(self._tasklist)

#changes
  def get_current_task(self):
    return self._tasklist[0]

  def __iter__(self):
    self._n = 0
    return self

  def __next__(self):
    self._n += 1
    if self._n > len(self._tasklist)-1:
      raise StopIteration
    else:
      return self._tasklist[self._n]