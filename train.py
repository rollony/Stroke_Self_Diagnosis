import numpy as np
from result import left_right_gap
import os
import sys

W = np.random.rand(2,1)
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

def predict(x):
    
    z = np.dot(x, W) + b
    y = sigmoid(z)
    
    if y > 0.5:
        result = 1
    else:
        result = 0
        
        
    return y, result



learning_rate = 1e-2

odd_path_dir = os.getcwd() + '/odd_pictures'
odd_file_list = os.listdir(odd_path_dir)
files = []

for i in range(len(odd_file_list)):
    img = odd_path_dir + '/' + odd_file_list[i]
    gap = left_right_gap(img)       
    files.append([gap,1])
    
normal_path_dir = os.getcwd() + '/normal_pictures'
normal_file_list = os.listdir(normal_path_dir)

for i in range(len(normal_file_list)):
    img = normal_path_dir + '/' + normal_file_list[i]
    gap = left_right_gap(img)
    files.append([gap,0])

x_data = np.array(files).reshape(len(odd_file_list) + len(normal_file_list), 2)
tmp_data = np.random.rand(len(odd_file_list) + len(normal_file_list),1)
t_data = np.ones_like(tmp_data)

     
print("W = ", W, ", W.shape = ", W.shape, ", b = ", b, " , b.shape = ", b.shape)

             
f= lambda x : loss_func(x_data, t_data)

print("initial error value = ", error_val(x_data, t_data), "initial W = ", W, " \n", ", b = ", b)

                  
for step in range(len(odd_file_list) + len(normal_file_list)):        
    W -= learning_rate * numerical_derivative(f, W)
    b -= learning_rate * numerical_derivative(f, b)
    
    
    print("step = ", step, "error value = ", error_val(x_data, t_data), "W = ", W, " , b = ", b)    

print(predict([left_right_gap(sys.argv[1]), 0]))