import random
from flask import Flask,render_template,jsonify,request
# from flask_cors import CORS
import json
from time import sleep
import numpy as np
from prune import minimax_tree
app=Flask(__name__,template_folder='./templates',static_folder='./templates')
# CORS(app)

@app.route('/submit',methods=['GET','POST'])
def submit():
    command=request.form.get('command',type=str)
    if command=='reset':
        new_game=game()
        data=new_game.return_data()
        # return render_template('index.html',data=json.dumps(data['data']),score=json.dumps(data['score']))
        return jsonify(data)
        # return render_template('index.html',data=data['data'],score=data['score'])

    else:
        return jsonify({ 'error': 'Invalid command' })

@app.route('/ai-mode',methods=['POST'])
def auto_ai():
    data_full=request.get_json()
    print('data_full',data_full)
    origin_data=data_full.get('data')
    for i in range(4):
        for j in range(4):
            if origin_data[i][j]=='':
                origin_data[i][j]=0
            else:
                origin_data[i][j]=int(origin_data[i][j])
    origin_score=data_full.get('score')
    game_ai=game(mat=origin_data,score=int(origin_score),mode='ai')
    game_ai.load_ai_data()
    data=game_ai.return_data()
    return jsonify(data)

@app.route('/move',methods=['POST'])
def upload():
    data_full=request.get_json()
    command=data_full.get('command')
    print(command)
    if command in ['w','a','s','d']:
        origin_data=data_full.get('data')
        for i in range(4):
            for j in range(4):
                if origin_data[i][j]=='':
                    origin_data[i][j]=0
                else:
                    origin_data[i][j]=int(origin_data[i][j])
        # origin_data=json.loads(origin_data)
        origin_score=int(data_full.get('score'))
        renew_game=game(mat=origin_data,score=int(origin_score))
        print(origin_score)
        renew_game.get_key(command)
        data=renew_game.return_data()
        #renew_game.mat,
        return jsonify(data)
    else:
        return jsonify({ 'error': 'Invalid command' })
class game():
    def __init__(self,mat='',score=0,mode='human'):
        if mat!='':
            self.mat=mat
            self.score=score
            self.move_flag=0
            self.wh_move=1
        else:
            while(1):
                random_1,random_2=random.randint(0,15),random.randint(0,15)
                if random_1!=random_2 :
                    break
            self.mat=self.game_init(random_1,random_2)
            self.score=0
            self.wh_move=1
            self.move_flag=0
        self.mode=mode
        if mode=='ai':
            self.tree=minimax_tree() 
            self.load_ai_data()

    def load_ai_data(self):
        mat=self.tree.mat_init(input=self.mat)
        print('mat',mat)
        evaluation_origin=self.tree.set_full(mat)
        score=self.score
        evaluation=self.get_suggestion()
        self.score=score
        self.mat,flag=self.movement(evaluation,self.mat)
        # mat=self.tree.mat_init(input=mat)
        # print(mat)
        # self.mat=mat
        # self.return_data()
        

    def get_suggestion(self):
        process_list=['a','s','w','d']
        worse_score=[]
        for i in process_list:
            mat,_=self.movement(i,self.mat)
            mat=self.tree.mat_init(input=mat)
            worse_score.append(self.tree.worse_choice(mat))
        print(worse_score)
        return process_list[worse_score.index(max(worse_score))]
        
        
    def return_data(self):
        mat=self.mat
        for i in range(4):
            for j in range(4):
                if mat[i][j]==0:
                    mat[i][j]=''
        if self.has_zero(mat)==False and self.check_wh_process(mat):
            return {'data':mat,'score':self.score,'wh_move':self.wh_move}
        else:
            return {'data':mat,'score':self.score,'wh_move':self.wh_move}

    def check_wh_process(self,mat):
        mat_zero=[['' for i in range(6)]for j in range(6)]
        for i in range(4):
            for j in range(4):
                mat_zero[i+1][j+1]=mat[i][j]
        mat=mat_zero
        for i in range(1,5):
            for j in range(1,5):
                if mat[i][j]==mat[i][j+1] or mat[i][j]==mat[i][j-1] or mat[i][j]==mat[i-1][j] or mat[i][j]==mat[i+1][j]:
                    return False
        return True
    def has_zero(self,matrix):
        for row in matrix:
            for element in row:
                if element == '':
                    return True
        return False

    def get_key(self,key):
        self.mat,flag=self.movement(key,self.mat)
        print(self.mat)
        flag=self.check_wh_process(self.mat)
        if self.has_zero(self.mat)==False and flag:
            #有0就还能动、flag代表四种操作能否进行
            # print('无法操作你输了')
            self.wh_move=0
        else:
            self.wh_move=1
            # break

    def merge_num(self,mat):
        mat_new=[i for i in mat if i!=0 and i!='']
        for i in range(len(mat_new)-1):
            if mat_new[i]==mat_new[i+1]:
                mat_new[i]=2*mat_new[i]
                mat_new[i+1]=''
                print(mat_new[i])
                self.score+=mat_new[i]
                # process+=1
                
        mat_new=[num for num in mat_new if num!=0]
        # print(mat_new)
        mat_str=mat_new
        mat_str+=['' for i in range(4-len(mat_new))]
        mat_new+=[0 for i in range(4-len(mat_new))]
        if mat_str!=mat:
            self.move_flag+=1
        return mat_new

    def transpose(self,mat):
        mat_new=[[0 for i in range(4)]for j in range(4)]
        for i in range(4):
            for j in range(4):
                mat_new[i][j]=mat[j][i]
        return mat_new

    def movement(self,key,matrix):
        if key=='a':
            mat,flag=self.gener_nm([self.merge_num(matrix[j]) for j in range(4)])
            # self.generate_platform(mat)
        elif key=='d':
            mat,flag=self.gener_nm([self.merge_num(matrix[j][: :-1])[: :-1] for j in range(4)])
            # self.generate_platform(mat)
        elif key=='w':
            matrix=self.transpose(matrix)
            mat,flag=self.gener_nm([self.merge_num(matrix[j]) for j in range(4)])
            mat=self.transpose(mat)
            # self.generate_platform(mat)
        elif key=='s':
            matrix=self.transpose(matrix)
            mat,flag=self.gener_nm([self.merge_num(matrix[j][: :-1])[::-1] for j in range(4)])
            mat=self.transpose(mat)
            # self.generate_platform(mat)
        return mat,flag

    def print_platform(self):
        print("#",end='')
        for j in range(4):
            if j!=3:
                print(' '*8,'|',end='',sep='')
            else:
                print(" "*8,end='',sep='')
        print("#",end='\n')

    def print_number(self,x):
        for i in range(4):
            if x[i]==0:
                x[i]=''
        print("#","{0: ^8}".format(x[0]),'|',"{0: ^8}".format(x[1]),'|',"{0: ^8}".format(x[2]),"|","{0: ^8}".format(x[3]),"#",sep='')

    def gener_nm(self,mat):
        flag=self.move_flag
        if self.move_flag>0:
            while(1):
                random_location=random.randint(0,15)
                i,j=random_location//4,random_location%4
                if mat[i][j]=='':
                    mat[i][j]=2
                    break
        self.move_flag=0
        return mat,flag

    def game_init(self,location_1,location_2):
        location=[[0 for i in range(4)] for j in range(4)]
        location[location_1//4][location_1%4],location[location_2//4][location_2%4]=2,2
        return location

    def generate_platform(self,location):
        print('Mode:human')
        print(f'Score:{self.score}')
        print("#"*37)
        for i in range(4):
            self.print_platform()
            self.print_number(location[i])
            self.print_platform()
            if i!=3:
                print("#","-"*35,'#',sep='')
        print("#" * 37)


@app.route('/',methods=['GET','POST'])
def set_web():
    game_2048=game()
    data=game_2048.return_data()
    return render_template('index.html',data=data['data'],score=data['score'])

if __name__ == '__main__':
    app.run(host='127.0.0.1',
      port=7890,debug=True,)
