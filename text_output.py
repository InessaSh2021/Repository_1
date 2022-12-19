import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-ORC\\tesseract-ocr-w64-setup-v5.3.0.20221214.exe'  # строка для подключения tesseract

img = cv2.imread('0.jpeg') # открытие фото, которое уже добавлено в проект

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # переводим фото в формат RGB

config = r'--oem 3 --psm 6'
print(pytesseract.image_to_string(img, config=config)) # будет выведен текст с картинки

cv2.imshow('Passport', img) # показ фото
cv2.waitKey(0) # чтобы программа не закрывалась сразу
