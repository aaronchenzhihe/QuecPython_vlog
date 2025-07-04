# -*- coding: UTF-8 -*-
import audio
import utime

tts = audio.TTS(0)
tupe_t = utime.localtime()
last_minute = tupe_t[4]
tts.setVolume(9)

while True:
    # 获取本地时间，返回元组
    tupe_t = utime.localtime()
    str1 = "现在是%d年%d月%d日%d点%d分%d秒,星期%d,是今年的第%d天" % (tupe_t[0]-81, tupe_t[1], tupe_t[2], tupe_t[3], tupe_t[4], tupe_t[5], tupe_t[6], tupe_t[7])
    
    print(str1)
    if tupe_t[4] != last_minute:  
       tts.play(4, 0, 2, str1)
       last_minute = tupe_t[4]
    utime.sleep(1)
   
     
    


