import time
from enum import Enum
from random import randint
import curses as c

from blessed import Terminal


# Example of json structure of file
DATA = {
    "items": [
      { "name": "Make an example struct", "description": "1. Write a python object that looks like a json file.\n2. Decide what data each item needs.\n3. Write some example items in it.", "index": "0"},
      { "name": "Foo", "description": "bar", "index": "1"},
      {"name":"n", "description":"ok", "index":"2"},
      {"name":"p", "description":"ok", "index":"2"},
      {"name":"xdfsfa", "description":"ok", "index":"2"}
      ]
    }


class ListEntry:
  def __init__(self, name, description, index):
    self.name = name
    self.description = description
    self.index = index

  def __str__(self):
    return f"{self.name}:\n\t{self.description}"

  def __repr__(self):
    return f"ListEntry({self.name}, {self.description}, {self.index})"


def main():
  t = Terminal()
  with t.fullscreen():
    e = [ListEntry(*item.values()) for item in DATA["items"]]

    for entry in e:
      print( t.color_rgb(randint(0, 256), randint(0, 256), randint(0, 256))(t.center(str(entry))))
      t.inkey()



if __name__ == "__main__":
  main()
