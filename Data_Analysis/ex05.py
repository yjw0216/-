# 05ex.py
a = range(1000000000000000000)
print(a)  ## range(0,1000000000000000000)   >>> 선언만 된 것 ! (실제 값이 아님 )
# lazy loading
sum = 0
for i in a:
    sum = sum + i
    if i >10 :
        break

print(sum)