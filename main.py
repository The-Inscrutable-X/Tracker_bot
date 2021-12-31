from trackers import ValueTracker, CumulativeTracker

#init trackers
weight_tracker = ValueTracker("weight_tracker.csv", 'lbs')
exercise_tracker = CumulativeTracker("exercise_tracker.csv", 'minutes')

#init selector
selection_array = {'w-e':weight_tracker.entry, 'e-e':exercise_tracker.entry, 'e-o':exercise_tracker.override, 'test':exercise_tracker.test}

#work selector
try:
  select = input('select:')
  argument = eval(input('value:'))
except EOFError:
  selection_array[select]()
except SyntaxError:
  selection_array[select]()
else:
  #print(type(argument))
  selection_array[select](argument)

