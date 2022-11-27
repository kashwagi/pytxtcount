import collections
dp = open('sample.txt','r',encoding='UTF-8')
mozi = dp.read()
txtcount = collections.Counter(mozi)

i=0
code = 0x41
while i < 10:
    print(chr(code))
    print(txtcount[chr(code)])
    code +=1
    i +=1




num = 0
while num < 10:
    print("num = " + str(num))
    num += 1

print("End")

dp.close()