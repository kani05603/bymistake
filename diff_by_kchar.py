d1,d2,d3 = map(str,input().split())
k = int(d3)
if(len(d1) != len(d2)):
    print("no")
else:
    c =0
    for i in range(len(d1)):
        if(d1[i] != d2[i]):
            c+=1
    if(c == k):
        print('yes')
    else:
        print('no')
