def solution(s):
    maximum=0
    length=len(s)
    for i in range(0,length-1,1):
        for j in range(i+1,length+1,1):
           number = len(s.split(s[i:j]))-1
           if number>maximum and len(s)/len(s[i:j])==number:
               maximum=number
    return maximum     
