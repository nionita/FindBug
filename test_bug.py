# -*- coding: utf-8 -*-
import pytest
from find_the_bug import Bug, Landscape

def test_bug_landscape():
  bug = Bug('bug.txt')
  landscape = Landscape('landscape.txt')

  occ = bug.count_occurences(landscape)
  assert occ == 3

def test_bug_bug():
  bug = Bug('bug.txt')
  landscape = Landscape('bug.txt')

  occ = bug.count_occurences(landscape)
  assert occ == 1

def test_landscape_landscape():
  bug = Bug('landscape.txt')
  landscape = Landscape('landscape.txt')

  occ = bug.count_occurences(landscape)
  assert occ == 1