from tkinter import *
import random
w=Tk()
w.title("SUDOKU")
B=[]
n=[]
for i in range(3):
    for j in range(3):
        frame=Frame(w,bg='powder blue',width=150,height=170)
        frame.grid(row=i,column=j,padx=5,pady=5)
        #m=[1,2,3,4,5,6,7,8,9]
        
        for k in range(3):
            for l in range(3):
                B.append(Button(frame,width=5,state='disable',height=2,command=lambda x=((3*i+j),k,l):g(x)))
                B[-1].grid(row=k,column=l,padx=3,pady=3)
                a=((3*i+j),k,l)
                n.append(a)
print(n)
'''
for t in n:
    print(t[0],end='\t')
'''
#print(n[0])
p=[0,1,2,3,4]

#print(B)
#B[n[3]]
                
def g(t):
    
    for i in range(10):
        y=random.choice(B)
        print(y)
        y['state']='active'
        
        B.remove(y)
        r=random.randrange(0,10)
        y['text']=r
        print(r)
    '''
    for i in B:
        f=random.choice(p)
        #p.remove(f)
        p.pop()
        i['text']=f
    #print(t)
    #n.append(t)
    #print(n)
    
'''        

        #entry['text']=
'''        
for i in range(1):
    for j in range(3):
        frame=Frame(w,bg='green',width=150,height=50)
        frame.grid(row=4,column=j)
        for k in range(3):
            button=Button(frame,text=k)
            button.grid(row=4,column=k,padx=3,pady=3)
'''      

w.mainloop()
