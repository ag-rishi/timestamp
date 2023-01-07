import datetime
import os
import pyautogui
import time

timestamp_value = datetime.datetime.now().astimezone().replace(microsecond=0).isoformat()

lines = ["", "", "", timestamp_value, "", "", ""]
with open('NEW JOURNAL ENTRY.txt', 'w') as f:
    for line in lines:
        f.write(line)
        f.write('\n')


os.startfile(r'C:\Users\rishi\American_Journal.txt')
time.sleep(0.20)
pyautogui.hotkey('ctrl', 'end') 
os.startfile('NEW.txt')
time.sleep(0.10)
pyautogui.hotkey('ctrl', 'end')
time.sleep(0.10)
os.system("netsh wlan disconnect")