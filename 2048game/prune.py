"""
a Alpha-beta prune al for 2048 demo
our baseline is minimax which is promoted to solve the best solution for game 2048.
"""
import numpy as np
class minimax_tree():
    def __init__(self,depth=4,alpha=1e10,beta=1e10,weight=[0.6,0.05,0.01,0.5]):
        self.alpha=alpha
        self.beta=beta
        self.weight=np.array(weight)
        self.depth=depth
        

    def mat_init(self,input):
        mat=[]
        for i in range(4):
            output=[]
            for j in range(4):
                if input[i][j]=='':
                    output.append(0)
                else:
                    output.append(int(input[i][j]))
            mat.append(output)
        return np.array(mat)
    
    def set_full(self,x):
        monotonicity,smoothy=self.cal_smoothy_monotonicity(x)
        zeroes=self.cal_zeroes(x)
        max_num=self.cal_maximum(x)
        return np.dot(self.weight,np.array([smoothy,zeroes,max_num,monotonicity]))
    
    

    def cal_smoothy_monotonicity(self,x):
        sum_smoothy=0
        sum_monotonicity=0
        for i in range(4):
            cum_line=[]
            cum_column=[]
            for j in range(4):
                if x[i][j]!=0:
                    cum_line.append(x[i][j])
                if x[j][i]!=0:
                    cum_column.append(x[j][i])
            sum_smoothy+=len(np.array(cum_line))+len(np.array(cum_column))-len(np.unique(np.array(cum_line)))\
            -len(np.unique(np.array(cum_column)))
            sum1,sum2=0,0
            unique_line=np.unique(np.array(cum_line))
            unique_column=np.unique(np.array(cum_column))
            for i in range(len(unique_column)-1):
                if unique_column[i]<unique_column[i+1]:
                    sum1+=1
                else:
                    sum1-=1
            if sum1==abs(len(unique_column)):
                sum_monotonicity+=1
            for i in range(len(unique_line)-1):
                if unique_line[i]<unique_line[i+1]:
                    sum2+=1
                else:
                    sum2-=1
            if sum2==abs(len(unique_line)):
                sum_monotonicity+=1
        return sum_monotonicity,sum_smoothy
    

    def cal_zeroes(self,x):
        index = np.array(np.where(x==0))
        return len(index.flatten())

    def worse_choice(self,x):
        index = np.array(np.where(x==0))
        beta=self.beta
        for i in range(len(index)):
            x[i]=2
            if beta>self.set_full(x):
                beta=self.set_full(x)
            x[i]=0
        return beta
    
    def cal_maximum(self,x):
        return np.max(x.flatten())
    
    def wh_win(self,mat):
        if np.max(mat.flatten())>=2048:
            return True
        else:
            return False
    

# prune.mat_init(array)
# print(prune.cal_zeroes(array))
# print(prune.cal_maximum(array))