import os, sys, io
import M5
from M5 import *
from hardware import *
import time



time_label = None
battery_label = None
circle = None
game_label = None
target = None
over_label = None
restart_label = None
points_label = None


import math
import random

battery_percent = None
distance = None
flag = None
normal_x_acc = None
normal_y_acc = None
circle_x = None
game_over = None
points = None
circle_r = None
circle_y = None
target_x = None
target_y = None
score = None
end_time = None
initial_time = None
x_acc = None
y_acc = None

# Describe this function...
def show_battery():
  global battery_percent, distance, flag, normal_x_acc, normal_y_acc, circle_x, game_over, points, circle_r, circle_y, target_x, target_y, score, end_time, initial_time, x_acc, y_acc, time_label, battery_label, circle, game_label, target, over_label, restart_label, points_label
  battery_percent = Power.getBatteryLevel()
  battery_label.setText(str((str(battery_percent) + str('%'))))

# Describe this function...
def is_target_in_circle():
  global battery_percent, distance, flag, normal_x_acc, normal_y_acc, circle_x, game_over, points, circle_r, circle_y, target_x, target_y, score, end_time, initial_time, x_acc, y_acc, time_label, battery_label, circle, game_label, target, over_label, restart_label, points_label
  distance = math.sqrt((target_x - circle_x) ** 2 + (target_y - circle_y) ** 2)
  if distance < circle_r:
    flag = True
  else:
    flag = False
  return flag


def btnB_wasClicked_event(state):
  global time_label, battery_label, circle, game_label, target, over_label, restart_label, points_label, battery_percent, distance, flag, normal_x_acc, normal_y_acc, circle_x, game_over, points, circle_r, circle_y, target_x, target_y, score, end_time, initial_time, x_acc, y_acc
  Speaker.tone(2610, 70)
  (normal_x_acc, normal_y_acc, _) = Imu.getAccel()
  circle_x = 67
  circle_y = 120
  circle.setCursor(x=circle_x, y=circle_y)


def setup():
  global time_label, battery_label, circle, game_label, target, over_label, restart_label, points_label, battery_percent, distance, flag, normal_x_acc, normal_y_acc, circle_x, game_over, points, circle_r, circle_y, target_x, target_y, score, end_time, initial_time, x_acc, y_acc

  M5.begin()
  time_label = Widgets.Label("label0", 4, 0, 1.0, 0xffffff, 0x000000, Widgets.FONTS.DejaVu12)
  battery_label = Widgets.Label("100%", 99, 0, 1.0, 0xffffff, 0x000000, Widgets.FONTS.DejaVu12)
  circle = Widgets.Circle(67, 120, 10, 0xf70000, 0xff0000)
  game_label = Widgets.Label("GAME", 8, 80, 1.0, 0xff0000, 0x000000, Widgets.FONTS.DejaVu40)
  target = Widgets.Circle(131, 236, 2, 0xffffff, 0xffffff)
  over_label = Widgets.Label("OVER", 11, 125, 1.0, 0xff0000, 0x000000, Widgets.FONTS.DejaVu40)
  restart_label = Widgets.Label("press M5 restart", 13, 225, 1.0, 0xffffff, 0x000000, Widgets.FONTS.DejaVu12)
  points_label = Widgets.Label("Points", 0, 186, 1.0, 0xffffff, 0x000000, Widgets.FONTS.DejaVu12)

  BtnB.setCallback(type=BtnB.CB_TYPE.WAS_CLICKED, cb=btnB_wasClicked_event)

  Widgets.setBrightness(5)
  circle_x = 67
  circle_y = 120
  circle_r = 10
  score = 0
  target_x = 0
  target_y = 0
  battery_percent = 0
  points = 0
  game_over = False
  (normal_x_acc, normal_y_acc, _) = Imu.getAccel()
  circle.setCursor(x=circle_x, y=circle_y)
  circle.setRadius(r=circle_r)
  initial_time = time.time()
  end_time = initial_time + 10
  game_label.setVisible(False)
  over_label.setVisible(False)
  restart_label.setVisible(False)
  points_label.setVisible(False)


def loop():
  global time_label, battery_label, circle, game_label, target, over_label, restart_label, points_label, battery_percent, distance, flag, normal_x_acc, normal_y_acc, circle_x, game_over, points, circle_r, circle_y, target_x, target_y, score, end_time, initial_time, x_acc, y_acc
  M5.update()
  while not game_over:
    M5.update()
    show_battery()
    target_x = random.randint(2, 130)
    target_y = random.randint(14, 230)
    target.setCursor(x=target_x, y=target_y)
    distance = math.sqrt((target_x - circle_x) ** 2 + (target_y - circle_y) ** 2)
    time_label.setText(str((str('Time: ') + str((end_time - (time.time()))))))
    if end_time <= (time.time()):
      game_over = True
    while not is_target_in_circle():
      M5.update()
      if end_time <= (time.time()):
        game_over = True
        break
      show_battery()
      (x_acc, y_acc, _) = Imu.getAccel()
      if math.fabs(x_acc - normal_x_acc) >= 0.05:
        if x_acc - normal_x_acc > 0 and circle_x >= circle_r:
          circle_x = (circle_x if isinstance(circle_x, (int, float)) else 0) + -1
        if x_acc - normal_x_acc < 0 and circle_x + circle_r <= 135:
          circle_x = (circle_x if isinstance(circle_x, (int, float)) else 0) + 1
      if math.fabs(y_acc - normal_y_acc) >= 0.05:
        if y_acc - normal_y_acc < 0 and circle_y >= circle_r:
          circle_y = (circle_y if isinstance(circle_y, (int, float)) else 0) + -1
        if y_acc - normal_y_acc > 0 and circle_y + circle_r <= 235:
          circle_y = (circle_y if isinstance(circle_y, (int, float)) else 0) + 1
      circle.setCursor(x=circle_x, y=circle_y)
      time.sleep_ms(2)
      time_label.setText(str((str('Time: ') + str((end_time - (time.time()))))))
    points = (points if isinstance(points, (int, float)) else 0) + 1
    end_time = (end_time if isinstance(end_time, (int, float)) else 0) + 2
    Speaker.tone(2610, 70)
    time.sleep_ms(2)
  points = (points if isinstance(points, (int, float)) else 0) + -1
  points_label.setText(str((str('Score:') + str(points))))
  time_label.setVisible(False)
  circle.setVisible(False)
  target.setVisible(False)
  game_label.setVisible(True)
  over_label.setVisible(True)
  points_label.setVisible(True)
  restart_label.setVisible(True)
  while not (BtnA.isPressed()):
    M5.update()
    game_over = False
    show_battery()
  time_label.setVisible(True)
  circle.setVisible(True)
  target.setVisible(True)
  game_label.setVisible(False)
  over_label.setVisible(False)
  points_label.setVisible(False)
  restart_label.setVisible(False)
  initial_time = time.time()
  end_time = initial_time + 10
  circle_x = 67
  circle_y = 120
  points = 0


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
