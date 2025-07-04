#EC200UEUAB

from machine import I2C # type: ignore
from utime import sleep_ms # type: ignore
class ATH20:
    def __init__(self):
        self.iic=I2C(I2C.I2C0,I2C.STANDARD_MODE,0)
        self.iic_init()
        #初始化命令
    def iic_init(self):
        self.iic.write(0x38,bytearray([0x00,]),len(bytearray([0x00,])),bytearray([0xE1,]),len(bytearray([0xE1,])))

    def reset(self):
        self.iic.write(0x38,bytearray([0x00,]),len(bytearray([0x00,])),bytearray([0xBA,]),len(bytearray([0xBA,])))

    def read(self):
        self.iic.write(0x38,bytearray([0x00,]),len(bytearray([0x00,])),bytearray([0xAC,0x33,0x00]),len(bytearray([0xAC,0x33,0x00])))
        sleep_ms(80)
        data=bytearray([0x00]*6)
        self.iic.read(0x38,bytearray([0x00,]),0,data,6,80)
        busy=0
        if not busy:            
            data_RH=data[1]<<12|data[2]<<4|data[3]>>4
            data_temp=data[3]&0x0f<<20|data[4]<<12|data[5]

            RH=data_RH/1048576*100
            temp=data_temp/1048576*200-50
            return RH,temp
        else:
            return("busy,wite again")

if __name__=="__main__":
    aht20=ATH20()
   
    sleep_ms(1000)
    while True:
        data1=aht20.read()
        if data1:
            print("RH:%.2f"% data1[0])
            print("temp:%.2f"% data1[1])
            print(len(data1))
            print("------------------")
        else:
            print("read error")
            
        sleep_ms(1000)
