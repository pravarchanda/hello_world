from dogpile.cache import make_region

region = make_region().configure('dogpile.cache.memory')

def save(key, value):
  """
  general purpose method to save data (value) in the cache

  :param key (string) key of the value to be saved in cache
  :param value (any type) the value to be saved
  """
  region.set(key, value)


def get(key):
  """
  general purpose method to get data from the cache

  :param key (string) key of the data to be fetched
  :return value (any type) data to be returned from the cache
  """
  return region.get(key)

save("hello","world")
val = get("hello")
print val