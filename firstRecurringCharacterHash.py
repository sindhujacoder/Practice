def get_first_recurring_char(arr):
  map_ = {}
  for i in range(0, len(arr)):
    if map_.get(arr[i]):
      return arr[i]
    else:
      map_[arr[i]] = True


