import csv as csv
import datetime
import typing

class Tracker(object):
  def __init__(self, file_name:str):
    self.file_name = file_name

  def read(self):
    with open(self.file_name, 'r') as f:
      entries = csv.reader(f)
      #print(list(entries))
      return entries

class ValueTracker(Tracker):
  def __init__(self, file_name:str):
    super().__init__(file_name)

  def entry(self, data:str):
    dtime = datetime.datetime.now()
    entry = (dtime, data)
    with open(self.file_name, 'a+') as f:
      appender = csv.writer(f)
      appender.writerow(entry)

class CounterTracker(Tracker):
  def __init__(self, file_name:str):
    super().__init__(file_name)

  def entry(self):
    with open(self.file_name, 'r') as f:
      lines = list(csv.reader(f))
      try:
        lastline = lines[-1]
        last_value = lastline[-1]
      except IndexError:
        print('new tracker!')
        last_value = 0
      print(lines)
    with open(self.file_name, 'a+') as g:
      dtime = datetime.datetime.now()
      entry = (dtime, str(int(last_value)+1))
      appender = csv.writer(g)
      appender.writerow(entry)
  
  def override(self, data):
    with open(self.file_name, 'a+') as f:
      dtime = datetime.datetime.now()
      appender = csv.writer(f)
      entry = (dtime, data)
      appender.writerow(entry)

#weight_tracker = ValueTracker("weight_tracker.csv")
#weight_tracker.entry(input("entry:"))

test = CounterTracker("exercise_tracker.csv")
#test.override(50)
test.entry()

