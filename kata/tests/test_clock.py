import pytest

from kata.clock import Clock 

def test_it_ticks_every_min():
  #given
  time = "18:03:00"
  #when
  clock = Clock()
  sound = clock.sayTime(time)

  #then
  assert sound == "tick"

def test_it_beeps_every_hour():
  #given
  time = "19:00:00"
  #when
  clock = Clock()
  sound = clock.sayTime(time)
  #then
  assert sound == "beep"

def test_it_wakes_up_at_7_am():
  #given
  time = "07:00:00"
  #when
  clock = Clock()
  sound = clock.sayTime(time)
  #then
  assert sound == "wake up!"






