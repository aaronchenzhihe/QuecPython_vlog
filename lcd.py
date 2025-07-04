#EG810M

from machine import LCD 
from machine import Pin
from machine import ExtInt
import utime
import math
# 根据LCD商家给出的相应的初始化示例来填写
# 第一行：2, 0, 120,		2表示sleep命令,中间恒为0,120表示sleep的毫秒数。收到此行数据,LCD将sleep 120ms
# 第二行：0, 0, 0x11,		0表示写入寄存器地址命令,中间数字表示后续需要写入的DATA长度，0表示没有要写入的数据,0x11是寄存器地址
# 第三行：0, 1, 0x36,		0表示写入寄存器地址命令,中间数字表示后续需要写入的DATA长度，1表示要写入一字节数据,0x36是寄存器地址
# 第四行：1, 1, 0x00,		1表示写入数据命令,中间数字表示写入的数据长度,0x00是数据
# 后面按照前四行的格式将初始化示例填入即可
init_data = (
            0, 0, 0x11,
            2, 0, 120,
            0, 1, 0x36,
            1, 1, 0x00,
            0, 1, 0x3A,
            1, 1, 0x05,
            0, 5, 0xB2,
            1, 1, 0x05,
            1, 1, 0x05,
            1, 1, 0x00,
            1, 1, 0x33,
            1, 1, 0x33,
            0, 1, 0xB7,
            1, 1, 0x75,
            0, 1, 0xBB,
            1, 1, 0x22,
            0, 1, 0xC0,
            1, 1, 0x2C,
            0, 1, 0xC2,
            1, 1, 0x01,
            0, 1, 0xC3,
            1, 1, 0x13,
            0, 1, 0xC4,
            1, 1, 0x20,
            0, 1, 0xC6,
            1, 1, 0x11,
            0, 2, 0xD0,
            1, 1, 0xA4,
            1, 1, 0xA1,
            0, 1, 0xD6,
            1, 1, 0xA1,
            0, 14, 0xE0,
            1, 1, 0xD0,
            1, 1, 0x05,
            1, 1, 0x0A,
            1, 1, 0x09,
            1, 1, 0x08,
            1, 1, 0x05,
            1, 1, 0x2E,
            1, 1, 0x44,
            1, 1, 0x45,
            1, 1, 0x0F,
            1, 1, 0x17,
            1, 1, 0x16,
            1, 1, 0x2B,
            1, 1, 0x33,
            0, 14, 0xE1,
            1, 1, 0xD0,
            1, 1, 0x05,
            1, 1, 0x0A,
            1, 1, 0x09,
            1, 1, 0x08,
            1, 1, 0x05,
            1, 1, 0x2E,
            1, 1, 0x43,
            1, 1, 0x45,
            1, 1, 0x0F,
            1, 1, 0x16,
            1, 1, 0x16,
            1, 1, 0x2B,
            1, 1, 0x33,
            0, 0, 0x29,
            0, 0, 0x21)

display_on_data = (
            0, 0, 0x28,
            2, 0, 120,
            0, 0, 0x10,
)
display_off_data =(
            0, 0, 0x11,
            2, 0, 20,
            0, 0, 0x29,
)
# 设置区域参数
XSTART_H = 0xf0
XSTART_L = 0xf1
YSTART_H = 0xf2
YSTART_L = 0xf3
XEND_H = 0xE0
XEND_L = 0xE1
YEND_H = 0xE2
YEND_L = 0xE3
invalid_data = (
    0, 4, 0x2a,
    1, 1, XSTART_H,
    1, 1, XSTART_L,
    1, 1, XEND_H,
    1, 1, XEND_L,
    0, 4, 0x2b,
    1, 1, YSTART_H,
    1, 1, YSTART_L,
    1, 1, YEND_H,
    1, 1, YEND_L,
    0, 0, 0x2c,
)

lcd = LCD()
init_list = bytearray(init_data)
display_on_list = bytearray(display_on_data)
display_off_list = bytearray(display_off_data)
invalid_list = bytearray(invalid_data)


lcd.lcd_init(init_list, 240,320,13000,1,4,0,invalid_list,display_on_list,display_off_list,None)
key = Pin(28,Pin.IN,Pin.PULL_PU,1)



def fun(args):
    while key.read()==0:
        if key.read()==1:
            break
        pass

def generate_data(i):
        r = int((math.sin(0.02 * i + 0) * 0.5 + 0.5) * 31)  # 红色分量 (5 bits)
        g = int((math.sin(0.02 * i + 2) * 0.5 + 0.5) * 63)  # 绿色分量 (6 bits)
        b = int((math.sin(0.02 * i + 4) * 0.5 + 0.5) * 31)  # 蓝色分量 (5 bits)
        return ((r << 11) | (g << 5) | b)  # RGB565 格式

i = 0

while True:   
    color = generate_data(i)
    lcd.lcd_clear(color) 
    print(color)
    utime.sleep_ms(10)    
    extint = ExtInt(ExtInt.GPIO28, ExtInt.IRQ_FALLING, ExtInt.PULL_PU, fun)
    extint.enable()
    i += 1
    

