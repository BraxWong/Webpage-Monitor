import win32api
import time

def jiggle_mouse():
    start_time = time.time()
    while time.time() - start_time < 8:
        x, y = win32api.GetCursorPos()
        x += 10
        y -= 10
        win32api.SetCursorPos((x, y))
        time.sleep(0.01)
        win32api.SetCursorPos((x, y)) 