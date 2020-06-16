#!/usr/bin/env python3
#
#    MacroMC is macro software for Minecraft written in Python 3.
#    Copyright (C) 2020  Kris Lamoureux
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3 of the License.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

import keyboard
import pyautogui

enabled = False

while True:
  toggled = keyboard.is_pressed('z')

  if toggled:
    if enabled:
      print("Macro disabled.")
      enabled = False
    else:
      print("Macro enabled.")
      enabled = True

  if toggled and not enabled:
    pyautogui.mouseUp(0,0)
    #pyautogui.keyUp('w')
  elif enabled:
    pyautogui.mouseDown(0,0)
    #pyautogui.keyDown('w')
