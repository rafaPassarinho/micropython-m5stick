import os, sys, io
import M5
from M5 import *
import time
from hardware import *



begin_label = None
hora = None
minuto = None
segundo = None
label_h = None
label_m = None
label_s = None
bat = None
hold_label = None
circle0 = None


total_seconds = None
hour_ = None
minute_ = None
second_ = None
hours_left = None
state = None
minutes_left = None
i = None

# Describe this function...
def show_time():
  global total_seconds, hour_, minute_, second_, hours_left, state, minutes_left, i, begin_label, hora, minuto, segundo, label_h, label_m, label_s, bat, hold_label, circle0
  if hour_ < 10:
    hora.setText(str((str('0') + str(hour_))))
  else:
    hora.setText(str(hour_))
  if minute_ < 10:
    minuto.setText(str((str('0') + str(minute_))))
  else:
    minuto.setText(str(minute_))
  if second_ < 10:
    segundo.setText(str((str('0') + str(second_))))
  else:
    segundo.setText(str(second_))

# Describe this function...
def countdown():
  global total_seconds, hour_, minute_, second_, hours_left, state, minutes_left, i, begin_label, hora, minuto, segundo, label_h, label_m, label_s, bat, hold_label, circle0
  total_seconds = hour_ * 3600 + minute_ * 60 + second_
  while total_seconds > 0:
    total_seconds = (total_seconds if isinstance(total_seconds, (int, float)) else 0) + -1
    hours_left = int(total_seconds / 3600)
    if hours_left < 10:
      hora.setText(str((str('0') + str(hours_left))))
    else:
      hora.setText(str(hours_left))
    minutes_left = total_seconds % 3600
    if (int(minutes_left / 60)) < 10:
      minuto.setText(str((str('0') + str((int(minutes_left / 60))))))
    else:
      minuto.setText(str(int(minutes_left / 60)))
    if minutes_left % 60 < 10:
      segundo.setText(str((str('0') + str((minutes_left % 60)))))
    else:
      segundo.setText(str(minutes_left % 60))
    time.sleep(1)


def setup():
  global begin_label, hora, minuto, segundo, label_h, label_m, label_s, bat, hold_label, circle0, total_seconds, hour_, minute_, second_, hours_left, state, minutes_left, i

  Widgets.setBrightness(5)
  M5.begin()
  begin_label = Widgets.Label("to begin", 42, 219, 1.0, 0xffffff, 0x000000, Widgets.FONTS.DejaVu12)
  hora = Widgets.Label("0", 23, 34, 1.0, 0xffffff, 0x000000, Widgets.FONTS.DejaVu40)
  minuto = Widgets.Label("0", 23, 94, 1.0, 0xffffff, 0x000000, Widgets.FONTS.DejaVu40)
  segundo = Widgets.Label("0", 23, 154, 1.0, 0xffffff, 0x000000, Widgets.FONTS.DejaVu40)
  label_h = Widgets.Label("h", 80, 34, 1.0, 0xffffff, 0x000000, Widgets.FONTS.DejaVu40)
  label_m = Widgets.Label("m", 80, 94, 1.0, 0xffffff, 0x000000, Widgets.FONTS.DejaVu40)
  label_s = Widgets.Label("s", 80, 154, 1.0, 0xffffff, 0x000000, Widgets.FONTS.DejaVu40)
  bat = Widgets.Label("i", 80, 4, 1.0, 0xffffff, 0x000000, Widgets.FONTS.DejaVu18)
  hold_label = Widgets.Label("hold M5", 44, 203, 1.0, 0xffffff, 0x000000, Widgets.FONTS.DejaVu12)
  circle0 = Widgets.Circle(10, 50, 5, 0xffffff, 0xffffff)

  Speaker.setVolumePercentage(0.5)
  state = 0
  hour_ = 0
  minute_ = 0
  second_ = 0
  i = 0
  hora.setColor(0xff0000, 0xff0000)
  minuto.setColor(0xff0000, 0xff0000)
  segundo.setColor(0xff0000, 0xff0000)
  label_h.setColor(0xff0000, 0xff0000)
  label_m.setColor(0xff0000, 0xff0000)
  label_s.setColor(0xff0000, 0xff0000)


def loop():
  global begin_label, hora, minuto, segundo, label_h, label_m, label_s, bat, hold_label, circle0, total_seconds, hour_, minute_, second_, hours_left, state, minutes_left, i
  M5.update()
  bat.setText(str((str((Power.getBatteryLevel())) + str('%'))))
  circle0.setVisible(True)
  hold_label.setVisible(True)
  begin_label.setVisible(True)
  label_h.setVisible(True)
  label_m.setVisible(True)
  label_s.setVisible(True)
  show_time()
  if BtnA.wasClicked():
    if state == 0:
      hour_ = (hour_ if isinstance(hour_, (int, float)) else 0) + 1
    elif state == 1:
      minute_ = (minute_ if isinstance(minute_, (int, float)) else 0) + 1
    else:
      second_ = (second_ if isinstance(second_, (int, float)) else 0) + 1
  if BtnPWR.wasClicked():
    if state == 0:
      hour_ = (hour_ if isinstance(hour_, (int, float)) else 0) + -1
    elif state == 1:
      minute_ = (minute_ if isinstance(minute_, (int, float)) else 0) + -1
    else:
      second_ = (second_ if isinstance(second_, (int, float)) else 0) + -1
  if BtnB.wasClicked():
    state = (state if isinstance(state, (int, float)) else 0) + 1
    circle0.setCursor(x=10, y=(50 + state * 60))
  if state > 2:
    state = 0
    circle0.setCursor(x=10, y=50)
  if hour_ > 23:
    hour_ = 0
  if hour_ < 0:
    hour_ = 23
  if minute_ > 59:
    minute_ = 0
  if minute_ < 0:
    minute_ = 59
  if second_ > 59:
    second_ = 0
  if second_ < 0:
    second_ = 59
  if BtnA.wasHold():
    hold_label.setVisible(False)
    begin_label.setVisible(False)
    circle0.setVisible(False)
    countdown()
    while not i == 4:
      M5.update()
      # E
      Speaker.tone(2637, 120)
      time.sleep_ms(200)
      time.sleep_ms(320)
      # G
      Speaker.tone(3135, 120)
      time.sleep_ms(200)
      time.sleep_ms(320)
      # A
      Speaker.tone(3520, 120)
      time.sleep_ms(200)
      time.sleep_ms(320)
      # G
      Speaker.tone(3135, 120)
      time.sleep_ms(200)
      for count in range(3):
        # A
        Speaker.tone(3520, 120)
        time.sleep_ms(200)
      # D
      Speaker.tone(2349, 120)
      time.sleep_ms(200)
      # C
      Speaker.tone(2093, 120)
      time.sleep_ms(200)
      # B
      Speaker.tone(3951, 120)
      time.sleep_ms(200)
      # A
      Speaker.tone(3520, 120)
      time.sleep_ms(200)
      # B
      Speaker.tone(3951, 240)
      time.sleep_ms(200)
      i = (i if isinstance(i, (int, float)) else 0) + 1
    hour_ = 0
    minute_ = 0
    second_ = 0
  i = 0


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
