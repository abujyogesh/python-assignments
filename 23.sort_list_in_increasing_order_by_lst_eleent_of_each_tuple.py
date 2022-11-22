def last(n):
    return n[-1]

def incr(list):
    return sorted(list,key=last)

list=[(10,20),(30,40),(40,10),(24,34)]
print("after sorting=",incr(list))
