import re
import os
pak_re = re.compile(r'[a-zA-Z0-9]+[-]*[a-zA-Z0-9]*')
print("正在获取需要升级的包列表，需要网络，可能需要一点时间")
pak_list = os.popen("pip list -o").readlines()
print("已获取全部需要升级的包，总共", str(len(pak_list)), "个，请耐心等待")
 
for i in range(len(pak_list)):
    pak_list[i] = pak_re.search(pak_list[i])[0] + os.linesep
 
count = 1
for i in pak_list:
    os.system("pip install --upgrade " + i)
    print("第" + str(count) + "个包升级完成")
    count += 1
 
print("恭喜！全部升级完成了！")

