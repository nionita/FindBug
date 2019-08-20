# *-* coding: utf-8 *-*

import sys

"""
A class for a drawing
"""
class Drawing:
  """
  Initialised from a text file with the ASCII style drawing.
  We store the busy squares (coordinates and values)
  """
  def __init__(self, file):
    try:
      ofile = open(file, 'r')
    except IOError:
      print('File', file, 'not found')
      exit(0)

    self.busy = {}

    y = 0
    for line in ofile:
      x = 0
      for char in line.rstrip():
        if char != ' ':
          self.busy[(x, y)] = char
        x += 1
      y += 1
    ofile.close()

"""
Landscape has specific methods to search for anchor positions
and check the existence of a given char at a given position
"""
class Landscape(Drawing):
  """
  Generate the coordinates that match a given char
  """
  def first_matches(self, char):
    for coord, c in self.busy.items():
      if c == char:
        yield coord

  """
  Check the existence of a given char at the given coordinate
  """
  def check_char_at(self, coord, char):
    return coord in self.busy and self.busy[coord] == char

"""
The bug has specific methods and fields.
New fields: the first occurence of a relevant character in the read
direction (up/down, left/right) is the anchor: we store its local position
"""
class Bug(Drawing):
  def __init__(self, file):
    super().__init__(file)

    # The first occurence of a char in the read direction (up/down, left/right) is the anchor
    self.anchor = None

    for coord, char in self.busy.items():
      if self.anchor is None or coord[1] < self.anchor[1] or (coord[1] == self.anchor[1] and coord[0] < self.anchor[0]):
        self.anchor = coord

  """
  Match all relevant chars with the given landscape at the given position
  """
  def match_all(self, landscape, start):
    # All relevant squares must be correct aligned and matched
    for bug_coord, char in self.busy.items():
      # Transform bug coordinates to landscape coordinates:
      landscape_x = start[0] + bug_coord[0]
      landscape_y = start[1] + bug_coord[1]
      if not landscape.check_char_at((landscape_x, landscape_y), char):
        return False
    return True

  """
  Count the occurences in the given landscape
  """
  def count_occurences(self, landscape):
    occurences = 0
    # First we match the anchor:
    for start in landscape.first_matches(self.busy[self.anchor]):
      # Small optimization: skip misaligned start positions (too far left):
      if start[0] >= self.anchor[0] and self.match_all(landscape, start):
        occurences += 1
    return occurences

if __name__ == '__main__':
  # We need 2 arguments, the bug file and the landscape file
  if len(sys.argv) != 3:
    print('Arguments error: exactly 2 arguments (file names) are needed.')
    print('Usage: find-the-bug.py bug-file landscape-file')
    exit(1)

  bug = Bug(sys.argv[1])
  # print('Bug:', bug.busy)

  landscape = Landscape(sys.argv[2])
  # print('Landscape:', landscape.busy)

  occ = bug.count_occurences(landscape)
  print('Occurences:', occ)