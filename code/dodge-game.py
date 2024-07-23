import os, sys, io
import M5
from M5 import *
from hardware import *
import time



game = None
over = None
label0 = None
restart = None
rect = None
circle = None


import random

circle_x = None
flag = None
score = None
red = None
green = None
blue = None
rect_x_position = None
i = None
x_acc = None


def setup():
  global game, over, label0, restart, rect, circle, circle_x, flag, score, red, green, blue, rect_x_position, i, x_acc

  M5.begin()
  game = Widgets.Label("GAME", 8, 45, 1.0, 0xff0000, 0x000000, Widgets.FONTS.DejaVu40)
  over = Widgets.Label("OVER", 11, 87, 1.0, 0xff0000, 0x000000, Widgets.FONTS.DejaVu40)
  label0 = Widgets.Label("Score:", 0, 131, 1.0, 0xffffff, 0x000000, Widgets.FONTS.DejaVu18)
  restart = Widgets.Label("M5 RESTART", 9, 185, 1.0, 0xffffff, 0x000000, Widgets.FONTS.DejaVu18)
  rect = Widgets.Rectangle(0, 0, 25, 25, 0xffffff, 0xffffff)
  circle = Widgets.Circle(67, 223, 15, 0xff0000, 0xfe0000)

  Widgets.setBrightness(1)
  flag = True


def loop():
  global game, over, label0, restart, rect, circle, circle_x, flag, score, red, green, blue, rect_x_position, i, x_acc
  M5.update()
  circle_x = 67
  flag = True
  score = 0
  rect.setVisible(True)
  circle.setVisible(True)
  game.setVisible(False)
  over.setVisible(False)
  label0.setVisible(False)
  restart.setVisible(False)
  while flag:
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    rect.setColor(color=(red << 16) | (green << 8) | blue, fill_c=(red << 16) | (green << 8) | blue)
    rect.setVisible(True)
    rect_x_position = random.randint(0, 108)
    for i in range(-25, 251):
      rect.setCursor(x=rect_x_position, y=i)
      (x_acc, _, _) = Imu.getAccel()
      if x_acc > 0.1 and circle_x >= 15:
        circle_x = (circle_x if isinstance(circle_x, (int, float)) else 0) + (int((-1 * x_acc) * 7))
        circle.setCursor(x=circle_x, y=223)
      if x_acc < -0.1 and circle_x <= 115:
        circle_x = (circle_x if isinstance(circle_x, (int, float)) else 0) + (int((-1 * x_acc) * 7))
        circle.setCursor(x=circle_x, y=223)
      if i > 220 and circle_x - rect_x_position < 40 and circle_x + 15 > rect_x_position:
        flag = False
      if i == 249:
        Speaker.tone(2610, 70)
      time.sleep_ms(1)
    score = (score if isinstance(score, (int, float)) else 0) + 1
  score = (score if isinstance(score, (int, float)) else 0) + -1
  rect.setVisible(False)
  circle.setVisible(False)
  game.setVisible(True)
  over.setVisible(True)
  label0.setVisible(True)
  restart.setVisible(True)
  label0.setText(str((str('Score: ') + str(score))))
  while not (BtnA.wasHold()):
    M5.update()
    score = 0


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
