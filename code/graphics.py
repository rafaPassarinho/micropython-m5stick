import os, sys, io
import M5
from M5 import *
from hardware import *
import time



circle_red = None
circle_green = None
circle_blue = None
line_r_g = None
line_g_b = None
line_r_b = None


import random

x_r = None
direction = None
new_direction = None
x_r_direction = None
i = None
x_g = None
y_r_direction = None
speed = None
x_b = None
x_g_direction = None
speeds = None
y_r = None
y_g_direction = None
y_g = None
x_b_direction = None
y_b = None
y_b_direction = None

# Describe this function...
def set_position():
  global x_r, direction, new_direction, x_r_direction, i, x_g, y_r_direction, speed, x_b, x_g_direction, speeds, y_r, y_g_direction, y_g, x_b_direction, y_b, y_b_direction, circle_red, circle_green, circle_blue, line_r_g, line_g_b, line_r_b
  x_r = random.randint(5, 140)
  x_g = random.randint(5, 140)
  x_b = random.randint(5, 140)
  y_r = random.randint(5, 245)
  y_g = random.randint(5, 245)
  y_b = random.randint(5, 245)

# Describe this function...
def random_direction():
  global x_r, direction, new_direction, x_r_direction, i, x_g, y_r_direction, speed, x_b, x_g_direction, speeds, y_r, y_g_direction, y_g, x_b_direction, y_b, y_b_direction, circle_red, circle_green, circle_blue, line_r_g, line_g_b, line_r_b
  direction = random.random()
  if direction >= 0:
    new_direction = 1
  else:
    new_direction = -1
  return new_direction

# Describe this function...
def set_direction():
  global x_r, direction, new_direction, x_r_direction, i, x_g, y_r_direction, speed, x_b, x_g_direction, speeds, y_r, y_g_direction, y_g, x_b_direction, y_b, y_b_direction, circle_red, circle_green, circle_blue, line_r_g, line_g_b, line_r_b
  x_r_direction = random_direction()
  y_r_direction = random_direction()
  x_g_direction = random_direction()
  y_g_direction = random_direction()
  x_b_direction = random_direction()
  y_b_direction = random_direction()


def btnA_wasPressed_event(state):
  global circle_red, circle_green, circle_blue, line_r_g, line_g_b, line_r_b, x_r, direction, new_direction, x_r_direction, i, x_g, random, y_r_direction, speed, x_b, x_g_direction, speeds, y_r, y_g_direction, y_g, x_b_direction, y_b, y_b_direction
  set_position()
  set_direction()


def btnB_wasClicked_event(state):
  global circle_red, circle_green, circle_blue, line_r_g, line_g_b, line_r_b, x_r, direction, new_direction, x_r_direction, i, x_g, random, y_r_direction, speed, x_b, x_g_direction, speeds, y_r, y_g_direction, y_g, x_b_direction, y_b, y_b_direction
  i = (i if isinstance(i, (int, float)) else 0) + 1
  if i > 3:
    i = 1


def setup():
  global circle_red, circle_green, circle_blue, line_r_g, line_g_b, line_r_b, x_r, direction, new_direction, x_r_direction, i, x_g, random, y_r_direction, speed, x_b, x_g_direction, speeds, y_r, y_g_direction, y_g, x_b_direction, y_b, y_b_direction

  M5.begin()
  circle_red = Widgets.Circle(70, 84, 10, 0xff0000, 0xff0000)
  circle_green = Widgets.Circle(98, 136, 10, 0x00ff00, 0x00ff00)
  circle_blue = Widgets.Circle(26, 135, 10, 0x0000ff, 0x0000ff)
  line_r_g = Widgets.Line(44, 178, 94, 178, 0xffff00)
  line_g_b = Widgets.Line(64, 197, 114, 197, 0x00ffff)
  line_r_b = Widgets.Line(52, 213, 102, 213, 0xff00ff)

  BtnA.setCallback(type=BtnA.CB_TYPE.WAS_PRESSED, cb=btnA_wasPressed_event)
  BtnB.setCallback(type=BtnB.CB_TYPE.WAS_CLICKED, cb=btnB_wasClicked_event)

  i = 1
  speeds = [10, 20, 30]
  Widgets.setBrightness(5)
  Speaker.setVolumePercentage(0.25)
  x_r = 0
  x_g = 0
  x_b = 0
  y_r = 0
  y_g = 0
  y_b = 0
  direction = -1
  x_b_direction = 0
  x_g_direction = 0
  x_r_direction = 0
  y_b_direction = 0
  y_g_direction = 0
  y_r_direction = 0
  set_position()
  set_direction()


def loop():
  global circle_red, circle_green, circle_blue, line_r_g, line_g_b, line_r_b, x_r, direction, new_direction, x_r_direction, i, x_g, random, y_r_direction, speed, x_b, x_g_direction, speeds, y_r, y_g_direction, y_g, x_b_direction, y_b, y_b_direction
  M5.update()
  speed = speeds[int(i - 1)]
  circle_red.setCursor(x=x_r, y=y_r)
  circle_green.setCursor(x=x_g, y=y_g)
  circle_blue.setCursor(x=x_b, y=y_b)
  line_r_g.setPoints(x0=x_r, y0=y_r, x1=x_g, y1=y_g)
  line_g_b.setPoints(x0=x_g, y0=y_g, x1=x_b, y1=y_b)
  line_r_b.setPoints(x0=x_r, y0=y_r, x1=x_b, y1=y_b)
  x_r = (x_r if isinstance(x_r, (int, float)) else 0) + x_r_direction * 5
  y_r = (y_r if isinstance(y_r, (int, float)) else 0) + y_r_direction * 5
  x_g = (x_g if isinstance(x_g, (int, float)) else 0) + x_g_direction * 5
  y_g = (y_g if isinstance(y_g, (int, float)) else 0) + y_g_direction * 5
  x_b = (x_b if isinstance(x_b, (int, float)) else 0) + x_b_direction * 5
  y_b = (y_b if isinstance(y_b, (int, float)) else 0) + y_b_direction * 5
  if x_r >= 140 or x_r <= 0:
    Speaker.tone(2930, 50)
    x_r_direction = x_r_direction * -1
  if x_g >= 140 or x_g <= 0:
    Speaker.tone(3290, 50)
    x_g_direction = x_g_direction * -1
  if x_b >= 140 or x_b <= 0:
    Speaker.tone(2610, 50)
    x_b_direction = x_b_direction * -1
  if y_r >= 245 or y_r <= 0:
    Speaker.tone(2930, 50)
    y_r_direction = y_r_direction * -1
  if y_g >= 245 or y_g <= 0:
    Speaker.tone(3290, 50)
    y_g_direction = y_g_direction * -1
  if y_b >= 245 or y_b <= 0:
    Speaker.tone(2610, 50)
    y_b_direction = y_b_direction * -1
  time.sleep_ms(speed)


if __name__ == '__main__':
  try:
    setup()
    while True:
      loop()
  except (Exception, KeyboardInterrupt) as e:
    try:
      from utility import print_error_msg
      print_error_msg(e)
    except ImportError:
      print("please update to latest firmware")
