# *-* coding: utf-8 *-*

import sys

"""
A class for a drawing
"""
class Drawing:
  """
  Initialised from a text file with the ASCII style drawing.
  We store the busy squares (coordinates and values)
  and the first occurence of a relevant character in the read
  direction (left/right, up/down)
  """
  def __init__(self, file):
    try:
      ofile = open(file, 'r')
    except IOError:
      print('File', file, 'not found')
      exit(0)

    self.origin = None
    self.anchor = None
    self.busy = {}

    y = 0
    for line in ofile:
      x = 0
      for char in line.strip():
        if char != ' ':
          if self.origin is None:
            self.origin = (x, y)
            self.anchor = char
          self.busy[(x, y)] = char
        x += 1
      y += 1
    ofile.close()

  """
  Check the existence of a given char at the given coordinates
  """
  def check_char_at(self, coord, char):
    return coord in self.busy and self.busy[coord] == char

  """
  Generate the coordinates that match a given char
  """
  def first_matches(self, anchor):
    for coord, char in self.busy.items():
      if char == anchor:
        yield coord

  """
  Match all relevant chars with the given landscape at the given anchor
  """
  def match_all(self, landscape, anchor):
    # All relevant squares must be correct aligned and matched
    for bug_coord, char in self.busy.items():
      # Bug (0, 0) coordinate corresponds to (anchor_x, anchor_y) in landscape coordinates
      landscape_x = anchor[0] + bug_coord[0]
      landscape_y = anchor[1] + bug_coord[1]
      if not landscape.check_char_at((landscape_x, landscape_y), char):
        return False
    return True

  """
  Count the occurences in the given landscape
  """
  def find_occurences(self, landscape):
    occurences = 0
    # First we match the anchor:
    for anchor in landscape.first_matches(self.anchor):
      # Small optimization: skip misaligned anchors (too far left):
      if anchor[0] >= self.origin[0] and self.match_all(landscape, anchor):
        occurences += 1
    return occurences

if __name__ == '__main__':
  # # We need 2 arguments, the bug file and the landscape file
  # parser = argparse.ArgumentParser(description='Find the bug')
  # parser.add_argument('-b', '--bug', required=True, type=argparse.FileType('r'), help='Bug file name')
  # parser.add_argument('-l', '--landscape', required=True, type=argparse.FileType('r'), help='Landscape file name')
  # args = parser.parse_args()

  if len(sys.argv) != 3:
    print('Arguments error: exactly 2 arguments (file names) are needed.')
    print('Usage: find-the-bug.py bug-file landscape-file')
    exit(1)

  bug = Drawing(sys.argv[1])
  print('Bug:', bug.busy)

  landscape = Drawing(sys.argv[2])
  print('Landscape:', landscape.busy)

  occ = bug.find_occurences(landscape)
  print('Occurences:', occ)