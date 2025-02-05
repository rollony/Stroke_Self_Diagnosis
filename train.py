import numpy as np
import os
import sys
from result import left_right_gap, predict

W = np.random.rand(1,1)
b = np.random.rand(1)

def sigmoid(x):
    return 1/(1+np.exp(-x))

def loss_func(x, t):
    
    delta = 1e-7 # log 무한대 발산 방지
    z = np.dot(x, W) + b
    y = sigmoid(z)
    
    #coss-entropy : 손실함수
    return -np.sum(t*np.log(y + delta) + (1-t)*np.log((1-y)+delta))

def numerical_derivative(f, x):
    delta_x = 1e-4
    grad = np.zeros_like(x)
    
    it = np.nditer(x, flags=['multi_index'], op_flags=['readwrite'])
    
    while not it.finished:
        idx = it.multi_index
        tmp_val = x[idx]
        x[idx] = float(tmp_val) + delta_x
        fx1 = f(x)
        
        x[idx] = tmp_val - delta_x
        fx2 = f(x)
        grad[idx] = (fx1-fx2) / (2*delta_x)
        
        x[idx] = tmp_val
        it.iternext()
        
    return grad

def error_val(x, t):
    delta = 1e-7
    
    z = np.dot(x, W) + b
    y = sigmoid(z)
    
    #coss-entropy : 손실함수
    return -np.sum(t*np.log(y + delta) + (1-t)*np.log((1-y)+delta))



learning_rate = 1e-2 #발산 방지

#안면장애를 가진 사람들 사진 학습
odd_path_dir = os.getcwd() + '/odd_pictures' 
odd_file_list = os.listdir(odd_path_dir)
files = []
t_data = []

#print('odd_________')
for i in range(len(odd_file_list)):
    img = odd_path_dir + '/' + odd_file_list[i]
    gap = left_right_gap(img)
    if gap == 999:
        continue
    #print(gap)
    files.append(gap)
    t_data.append(1)

#정상 사람들 사진 학습
normal_path_dir = os.getcwd() + '/normal_pictures'
normal_file_list = os.listdir(normal_path_dir)

#print('normal_________')
for i in range(len(normal_file_list)):
    img = normal_path_dir + '/' + normal_file_list[i]
    gap = left_right_gap(img)
    if gap == 999:
        continue
    #print(gap)
    files.append(gap)
    t_data.append(0)

x_data = np.array(files).reshape(len(files), 1)
t_data = np.array(t_data).reshape(len(t_data), 1)

     
print("W = ", W, ", W.shape = ", W.shape, ", b = ", b, " , b.shape = ", b.shape)

             
f= lambda x : loss_func(x_data, t_data)

print("initial error value = ", error_val(x_data, t_data), "initial W = ", W, " \n", ", b = ", b)

                  
for step in range(30001):
    W -= learning_rate * numerical_derivative(f, W)
    b -= learning_rate * numerical_derivative(f, b)
    
    if (step % 10000 == 0):
        print("step = ", step, "error value = ", error_val(x_data, t_data), "W = ", W, " , b = ", b) 
        
f = open("./data.txt", 'w')
f.write(str(W[0,0]) + '\n')
f.write(str(b[0]))
f.close()