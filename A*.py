from queue import PriorityQueue as pq
from copy import deepcopy
class Node():
    def __init__(self, mat, move,height,parent=None):
        self.mat = mat
        self.move = move
        self.parent = parent
        self.height=height
    
    def __lt__(self,other): #makes nodes comparable
        return 0
   
    def zero(self):
        for i in range(3):
            for j in range(3):
                if self.mat[i][j] == 0:
                    return i,j

    def dist(self,goal): #manhattan distance
        total = 0
        for i in range(3):
            for j in range(3):
                if self.mat[i][j]!=goal.mat[i][j] and self.mat[i][j]!=0:
                    for k in range(3):
                        for l in range(3):
                            if(self.mat[i][j]==goal.mat[k][l]):
                                total += abs(i-k)+abs(j-l)
        return total


  
    def change(self,mat,zero,y,x,height,move):
        newboard=deepcopy(mat)
        newboard[zero[0]][zero[1]]=newboard[zero[0]+y][zero[1]+x]
        newboard[zero[0]+y][zero[1]+x]=0
        newboardnode=Node(newboard,move,height,self)
        return newboardnode
    
    def FindChildren(self,height):
        zero = self.zero() 
        mat = self.mat 
        children = [] 
        if zero[0]-1>=0: 
            children.append(self.change(mat,zero,-1,0,height,'down'))
        if zero[0]+1<3: 
            children.append(self.change(mat,zero,1,0,height,'up'))
        if zero[1]-1>=0: 
            children.append(self.change(mat,zero,0,-1,height,'right'))
        if zero[1]+1<3: 
            children.append(self.change(mat,zero,0,1,height,'left'))
        return children
    
    def path(self):
        path = []
        path.append((self.move,self.mat))
        n = self.parent
        while n.parent is not None:
            path.append((n.move,n.mat))
            n = n.parent
        path.append((n.move,n.mat))
        path.reverse()
        return path
   

def solve(start_node,goal):
    PQueue = pq() 
    visited = []
    explored = 0
    PQueue.put((start_node.dist(goal),start_node)) 
    while not PQueue.empty(): 
       h,n = PQueue.get() 
       #h=h+n.height # A star
       if n.mat in visited:   
           continue
       if h==0: 
           print_path(n.path())
           print('explored nodes:%d'%explored)
           return
       
       visited.append(n.mat)
       
       explored+=1 
       
       for nnode in n.FindChildren(n.height+1):
           PQueue.put((nnode.dist(goal),nnode))
           

         
def print_board(mat):
    
    for i in mat:
        print('%d%d%d'%(i[0],i[1],i[2]))
    print("\n")  

 
def print_path(path):
    for b in path:
        print(b[0])
        print_board(b[1])
    print('end') 

start_node = Node([
                    [7,2,4],
                    [5,0,6],
                    [8,3,1]
                    ],'start',0)
Goal_node = Node([
                [0,1,2],
                [3,4,5],
                [6,7,8]
                ],'done',0)
solve(start_node,Goal_node)
