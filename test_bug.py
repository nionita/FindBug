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

def test_bug_landscape2():
  bug = Bug('bug.txt')
  landscape = Landscape('landscape2.txt')

  occ = bug.count_occurences(landscape)
  # The bigger bug contains the smaller bug, so it counts too
  assert occ == 5

def test_bug2_landscape2():
  bug = Bug('bug2.txt')
  landscape = Landscape('landscape2.txt')

  occ = bug.count_occurences(landscape)
  assert occ == 1