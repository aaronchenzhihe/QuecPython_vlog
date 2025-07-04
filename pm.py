#EC200UEUAA

import pm
import utime

# 创建wakelock锁
lpm_fd = pm.create_wakelock("test_lock", len("test_lock"))
# 设置自动休眠模式
SW=pm.autosleep(1)
print("自动休眠模式开启")
# 模拟测试，实际开发请根据业务场景选择使用
while 1:
    utime.sleep(5)  # 休眠
    res = pm.wakelock_lock(lpm_fd)# 锁
    print("%d 上锁,进入工作模式 " %lpm_fd)
    utime.sleep(5)
    res = pm.wakelock_unlock(lpm_fd)# 解锁
    print("%d 解锁,进入休眠模式  " % lpm_fd)    
    num = pm.get_wakelock_num()  # 获取已创建锁的数量
    print(num)
    pm.delete_wakelock(lpm_fd)
    

