import pyautogui,  time,keyboard
num1 = input("введите команду")
if num1 == "поиск":
    num2 = input("введите запрос")
    pyautogui.moveTo(1250, 5)
    pyautogui.click()
    time.sleep(1)
    pyautogui.moveTo(1250, 40)
    pyautogui.click()
    pyautogui.click()
    time.sleep(2)
    keyboard.write(num2)
    time.sleep(2)
    pyautogui.press('enter')
elif num1 == "текст":
    pyautogui.moveTo(1250, 5)
    pyautogui.click()
    time.sleep(1)
    pyautogui.click(button = 'right')
    pyautogui.moveTo(1250, 250)
    time.sleep(1)
    pyautogui.moveTo(1000, 250)
    time.sleep(1)
    pyautogui.moveTo(1000, 400)
    time.sleep(1)
    pyautogui.click()
    pyautogui.moveTo(1250, 40)
    time.sleep(1)
    pyautogui.doubleClick()
elif num1 == "выход":
    exit
else: print('неизвестная команда')
print(" вы вышли из программы")

    
