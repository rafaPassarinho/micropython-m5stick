# M5Stick CPlus MicroPython Project
MicroPython code examples for the M5Stick CPlus 2 based on ESP32. This repository contains scripts and resources to help you explore and utilize the capabilities of the M5Stick CPlus using MicroPython, including examples for input/output operations, display usage and sensor interactions.

## Table of Contents

- [Introduction](#introduction)
- [Code Examples](#code-examples)

## Introduction

The M5Stick CPlus 2 is a compact development board based on the ESP32 microcontroller. It is equipped with various sensors, a display, and other features that make it ideal for IoT projects. This project provides example codes and resources to help you explore the capabilities of the M5Stick CPlus using MicroPython.

## Code Examples


- [Catch the Dot](code/catch_dot.py): The game tests the player's ability to move a circle to capture randomly appearing targets on the screen, using the device's accelerometer for control, every time you reach the target, earn extra time.
- [Clock](code/clock.py): A digital timer with countdown and alarm. It provides a user-friendly interface to set a timer and counts down to zero, complete with an Evangelion opening alarm when the countdown finishes.
- [Dodge Game](code/dodge-game.py): The game leverages the built-in accelerometer to move a player-controlled circle to avoid falling rectangles, testing the player's reflexes and hand-eye coordination.
- [Graphics](code/graphics.py): a visual and interactive display of three circles (red, green, and blue) that move randomly on the screen. The movement is accompanied by sound alerts whenever a circle reaches the edge of the screen.
