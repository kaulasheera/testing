import time
import pyautogui
time.sleep(5)
for x in range(1,31):
	pyautogui.typewrite(str(x))
	pyautogui.typewrite("spam")
	pyautogui.press("enter")
	time.sleep(0.1)