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

toggleable = True
state = False

def main(event):
  global toggleable
  global state

  # Macro hotkey pressed
  if event.name == 'z':
    # Toggle
    if event.event_type == 'down':

      # Disable macro
      if toggleable and state:
        print("Toggle disabled")
        state = False
        pyautogui.mouseUp(0,0)
        #keyboard.release('w')
      # Enable macro
      elif toggleable and not state:
        print("Toggle enabled")
        state = True
        pyautogui.mouseDown(0,0)
        #keyboard.press('w')

      toggleable = False

    # Toggleable again
    elif event.event_type == 'up':
      toggleable = True

keyboard.hook(main)
keyboard.wait()
