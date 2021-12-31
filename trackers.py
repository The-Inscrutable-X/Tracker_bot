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
  def __init__(self, file_name:str, unit:str):
    super().__init__(file_name)
    self.unit = unit
    #make labels
    with open(self.file_name, 'r') as f:
      lines = list(csv.reader(f))
      if lines == []:
        print('new tracker!')
        entry = ('Time', 'Value'+'('+self.unit+')')
        with open(self.file_name, 'a+') as g:
          appender = csv.writer(g)
          appender.writerow(entry)

  def entry(self, data:str):
    dtime = datetime.datetime.now()
    entry = (dtime, data)
    with open(self.file_name, 'a+') as f:
      appender = csv.writer(f)
      appender.writerow(entry)

class CumulativeTracker(Tracker):
  def __init__(self, file_name:str, unit:str):
    super().__init__(file_name)
    self.unit = unit
    #make labels
    with open(self.file_name, 'r') as f:
      lines = list(csv.reader(f))
      if lines == []:
        print('new tracker!')
        entry = ('Time', 'Value'+'('+self.unit+')')
        with open(self.file_name, 'a+') as g:
          appender = csv.writer(g)
          appender.writerow(entry)

  def entry(self, cum):
    with open(self.file_name, 'r') as f:
      lines = list(csv.reader(f))
      lines = lines[1:]
      try:
        lastline = lines[-1]
        last_value = lastline[-1]
      except IndexError:
        print('new tracker!')
        last_value = 0
      #print(lines)
    with open(self.file_name, 'a+') as g:
      dtime = datetime.datetime.now()
      entry = (dtime, str(float(last_value)+cum))
      appender = csv.writer(g)
      appender.writerow(entry)
  
  def override(self, data):
    with open(self.file_name, 'a+') as f:
      dtime = datetime.datetime.now()
      appender = csv.writer(f)
      entry = (dtime, data)
      appender.writerow(entry)

  def test(self):
    pass