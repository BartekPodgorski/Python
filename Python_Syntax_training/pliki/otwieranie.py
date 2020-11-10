#Obsluga wyjatkow bloki try i finally, po error nic juz sie nie
#wykona , jedynie w finally musi sie wykonac

try:
    file = open("test", "w") #uchwyt HANDLE
    file.write("sample")
    print(0/0)
    file.write("sample")
finally:
    file.close()
