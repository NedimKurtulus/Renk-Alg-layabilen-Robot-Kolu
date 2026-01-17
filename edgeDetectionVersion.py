

# -*- coding: utf-8 -*-


import cv2
import numpy as np
import serial
import time

# Arduino bağlantısı
arduino = serial.Serial('COM7', 9600)
time.sleep(2)

# Kamera ayarları
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

# Renk durumu (edge detection için)
current_state = None

while True:
    ret, frame = cap.read()
    if not ret:
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # --- KIRMIZI (iki aralık) ---
    lower_red1 = np.array([0, 120, 70])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([170, 120, 70])
    upper_red2 = np.array([180, 255, 255])

    mask_red = cv2.inRange(hsv, lower_red1, upper_red1) + \
               cv2.inRange(hsv, lower_red2, upper_red2)

    # --- YEŞİL ---
    lower_green = np.array([40, 70, 70])
    upper_green = np.array([80, 255, 255])
    mask_green = cv2.inRange(hsv, lower_green, upper_green)

    # Piksel sayıları
    red_pixels = cv2.countNonZero(mask_red)
    green_pixels = cv2.countNonZero(mask_green)

    # --- KARAR MEKANİZMASI ---
    if red_pixels > 1500:
        if current_state != 'R':
            print("Kırmızı algılandı")
            arduino.write(b'R')
            current_state = 'R'

    elif green_pixels > 1500:
        if current_state != 'G':
            print("Yeşil algılandı")
            arduino.write(b'G')
            current_state = 'G'

    else:
        # Kadrajda hedef renk yok → reset
        current_state = None

    # Görüntü göster
    cv2.imshow("Frame", frame)

    # ESC ile çıkış
    if cv2.waitKey(1) == 27:
        break

# Temiz kapatma
cap.release()
cv2.destroyAllWindows()
arduino.close()
