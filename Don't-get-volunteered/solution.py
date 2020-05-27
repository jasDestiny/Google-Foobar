class box: 
      
    def __init__(self, x = 0, y = 0, dist = 0): 
        self.x = x 
        self.y = y 
        self.dist = dist 
          
def isWithin(x, y, N): 
    if (x >= 1 and x <= N and y >= 1 and y <= N):  
        return True
    return False
      
def minNumReq(mylocation,golocation, N): 
      
    posX = [2, 2, -2, -2, 1, 1, -1, -1] 
    posY = [1, -1, 1, -1, 2, -2, 2, -2] 
      
    q = [] 
      
    q.append(box(mylocation[0], mylocation[1], 0)) 
      
    goneboxs = [[False for i in range(N + 1)]  
                      for j in range(N + 1)] 
      
    goneboxs[mylocation[0]][mylocation[1]] = True
      
    while(len(q) > 0): 
          
        t = q[0] 
        q.pop(0) 
          
        if(t.x == golocation[0] and t.y == golocation[1]): 
            return t.dist 
 
        for i in range(8): 
              
            x = t.x + posX[i] 
            y = t.y + posY[i] 
              
            if(isWithin(x, y, N) and not goneboxs[x][y]): 
                goneboxs[x][y] = True
                q.append(box(x, y, t.dist + 1)) 
  
def solution(src,dest):
    dicx={}
    dicy={}
    x=1
    y=1
    for i in range(0,64,1):
        dicx[i]=x
        dicy[i]=y
        x+=1
        if x%9==0:
            x=1
            y+=1
    N = 30
    mylocation = [dicx[src], dicy[src]] 
    golocation = [dicx[dest], dicy[dest]] 
    print(mylocation)
    print(golocation)
    return minNumReq(mylocation, golocation, N)

print(solution(0,17))



