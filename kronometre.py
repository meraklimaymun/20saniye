from sense_hat import SenseHat
import time
import serial

ser = serial.Serial('/dev/ttyACM0', 9600)

sense = SenseHat()

OFFSET_LEFT = 1
OFFSET_TOP = 2

NUMS =[1,1,1,1,0,1,1,0,1,1,0,1,1,1,1,  # 0
       0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,  # 1
       1,1,1,0,0,1,0,1,0,1,0,0,1,1,1,  # 2
       1,1,1,0,0,1,1,1,1,0,0,1,1,1,1,  # 3
       1,0,0,1,0,1,1,1,1,0,0,1,0,0,1,  # 4
       1,1,1,1,0,0,1,1,1,0,0,1,1,1,1,  # 5
       1,1,1,1,0,0,1,1,1,1,0,1,1,1,1,  # 6
       1,1,1,0,0,1,0,1,0,1,0,0,1,0,0,  # 7
       1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,  # 8
       1,1,1,1,0,1,1,1,1,0,0,1,0,0,1]  # 9

# tek basamakli sayilari gostermek icin (0-9)
def show_digit(val, xd, yd, r, g, b):
  offset = val * 15
  for p in range(offset, offset + 15):
    xt = p % 3
    yt = (p-offset) // 3
    sense.set_pixel(xt+xd, yt+yd, r*NUMS[p], g*NUMS[p], b*NUMS[p])

# iki basamakli sayilari gostermek icin (0-99)
def show_number(val, r, g, b):
  abs_val = abs(val)
  tens = abs_val // 10
  units = abs_val % 10
  if (abs_val > 9): show_digit(tens, OFFSET_LEFT, OFFSET_TOP, r, g, b)
  show_digit(units, OFFSET_LEFT+4, OFFSET_TOP, r, g, b)

while True:
    input = ser.read()
    veri = input.decode("utf-8")
    print(veri)
    if int(veri) == 1:
        sense.clear()
        show_number(20, 255, 0, 0)
        time.sleep(3) #Muslugu acip sabun surme icin ek zaman
        show_number(19, 255, 0, 0)
        time.sleep(1)
        show_number(18, 255, 0, 0)
        time.sleep(1)
        show_number(17, 255, 0, 0)
        time.sleep(1)
        show_number(16, 255, 0, 0)
        time.sleep(1)
        show_number(15, 255, 70, 0)
        time.sleep(1)
        show_number(14, 255, 70, 0)
        time.sleep(1)
        show_number(13, 255, 70, 0)
        time.sleep(1)
        show_number(12, 255, 70, 0)
        time.sleep(1)
        show_number(11, 255, 70, 0)
        time.sleep(1)
        show_number(10, 255, 70, 0)
        time.sleep(1)
        sense.clear()
        show_digit(9, 3, 2, 255, 140, 0)
        time.sleep(1)
        show_digit(8, 3, 2, 255, 140, 0)
        time.sleep(1)
        show_digit(7, 3, 2, 255, 140, 0)
        time.sleep(1)
        show_digit(6, 3, 2, 255, 255, 0)
        time.sleep(1)
        show_digit(5, 3, 2, 255, 255, 0)
        time.sleep(1)
        show_digit(4, 3, 2, 255, 255, 0)
        time.sleep(1)
        show_digit(3, 3, 2, 0, 255, 0)
        time.sleep(1)
        show_digit(2, 3, 2, 0, 255, 0)
        time.sleep(1)
        show_digit(1, 3, 2, 0, 255, 0)
        time.sleep(1)
        show_digit(0, 3, 2, 0, 255, 0)
        time.sleep(1)
        sense.clear()
        time.sleep(1)
        show_digit(0, 3, 2, 0, 255, 0)
        time.sleep(1)
        sense.clear()
        time.sleep(1)
        show_digit(0, 3, 2, 0, 255, 0)
        time.sleep(1)
        sense.clear()
        sense.show_message("EVDE KAL")
        sense.clear()
        input=0
    else:
        sense.clear()
        

        
