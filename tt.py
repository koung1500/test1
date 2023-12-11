# import streamlit as st
# import time







# import sys
# sys.exit()

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

col1, col2, col3 = st.columns(3)

with col1:
    c1 = st.sidebar.radio('선의 색을 선택하시오',['red', 'green', 'blue', 'orange'])
with col2:
    s1 = st.sidebar.radio('선의 형태을 선택하시오', ['-', ':', '--'])
with col3:
    m1 = st.sidebar.radio('마커의 형태를 선택하시오',['o', '^', 's', 'p'])
    
fig, ax = plt.subplots()

x = []
y = []
for i in range(-20, 21, 5):
    x.append(i)
    y.append(-2*i*i + 3*i+ 5)

plt.plot(x, y, color = c1, linestyle = s1, marker = m1)




st.pyplot(fig)






# x = []
# y = []
# for i in range(-20, 21, 1):
#     x.append(i)
#     y.append(3*i*i - 5*i + 2)

# plt.plot(x,y, '-ro', linewidth = 2)
# st.pyplot(fig)


# import sys
# sys.exit()
# fig, ax = plt.subplots()


# col = st. columns(3)
# with col[0]:
#     a = st.number_input('Insert a' , step = 10)
# with col[1]:
#     b = st.number_input('Insert b' , step = 10)
# with col[2]:
#     c = st.number_input('Insert c' , step = 10)

# y = []
# for i in x:
#     y.append(a*i**2 + b*i + c)

# plt.plot(x, y)

# st.pyplot(fig)

# import streamlit as st


# s = [3, 7, 1, 9, -3, 3, 10]
# s
# print(s.sort())



# a = sum(s)
# 'sum', a
# mx = max(s)
# 'max', mx
# mn = min(s)
# 'min', mn






# mx = -1e10
# mx
# for i in s:
#     if i > mx:
#         mx = i
# mx



# t = 0
# for i in s:
#     # t = t + i
#     t += i
# t




# s = ['a', 'b', 'c', 'd', 'e']

# s. append('사과')
# s. remove('c')
# s
# i = s.index('b')



# s[-1]

# if 'f' not in s:
#     '1'
# else:
#     '2'








# import turtle
# import random



# t = turtle.Turtle()


# def tree(length):
#     if length > 5:
#         t.forward(length)
#         t.right(20)
#         tree(length-15)
#         t.right(40)
#         tree(length-15)
#         t.right(20)
#         t.backward(length)

# t = turtle.Turtle()
# t.left(90)

# t.color("green")
# t.speed(0)
# tree(90)



# t.speed(0)
# t.pensize(5)
# t.goto(0,0)


# while True:
#     for i in range(30):
#         # t.circle(1+5*i)
#         t.forward(1 + 5*1)
#         t.left(90)
#         t.forward(1 + 5*1)
#         t.left(90)
#         t.forward(1 + 5*1)
#         t.left(90)
#         t.forward(1 + 5*1)
#         t.left(90)
#         t.color((random.random(),random.random(),random.random()))
#         t.goto(i*20, 0)
#     t.clear() 



# t.forward(100)











# screen = turtle.Screen()
# im1 = 'rabbit.gif'
# im2 = 'rabbit.gif'
# im3 = 'rabbit.gif'


# t1 = turtle. Turtle()
# t2 = turtle. Turtle()
# t3 = turtle. Turtle()

# screen.addshape(im1)
# screen.addshape(im2)
# screen.addshape(im3)




# t1. shape(im1)
# t2. shape(im2)
# t3. shape(im3)
 
# t1. penup()
# t1. shapesize(3)
# t1. pensize(5)
# t1. goto(-300, 150)

# t2. penup()
# t2. shapesize(3)
# t2. pensize(5)
# t2. goto(-300,-100)

# t3. penup()
# t3. shapesize(3)
# t3. pensize(5)
# t3. goto(-300,100)


# t1. pendown()
# t2. pendown()
# t3. pendown()
# t1. speed(1)
# t2. speed(1)
# t3. speed(1)

# for i in range(50):
#     d1 = r.randint(1, 30)
#     t1. forward(d1)
#     d2 =  r.randint(1, 30)
#     t2. forward(d2)
#     d3 =  r.randint(1, 30)
#     t3. forward(d3)



# turtle.done()

# for _ in range(6): 
#     a1 = r.randint(1, 45)
#     a2 = r.randint()
#     a1, a2

# c = 0 
# for i in range():  
#     c = r.choice('abcedf')
#     if c == 'a':
#         a = a + 1



# import turtle
# t = turtle.Turtle()
# t.shape('turtle')
# t.speed(0)








# def rec(x, y, lx, ly):
#     t.up()
#     t.goto(x, y)
#     t.down()
#     for l in range(2):
#         t.forward(lx)
#         t.left(90)
#         t.forward(ly)
#         t.left(90)
    

# rec(-200, 0, 100, 0)
# rec(0, 0, 100, 150)
# rec(200, 0, 100, 100)
# rec(0, 0, 100, 150)







# turtle.done()













# def user_sum(n):
#     s = 0
#     for i in range(1, n+1):
#         s = s + i
#     s  

# user_sum(100)
# user_sum(200)





# for i in range(1, 100):
    # if i%5 == 2:
        # i



# age = 20
# if age < 20:
#     print('aa')
# else:
#     print('bb')



#'apple' +'grape'
# 'apple' * 3

#'나는' +"12" + '개의 사과를 먹었다'









# colrs = ['red', 'purple', 'blue', 'yellow', 'orange', 'green']
# t.width(2)
# turtle.bgcolor('black')


#length = 5
#for i in range(100):
 #   t.forward(length)
    # t.pencolor(colors[length%7])
  #  t.right(49)
   # length += 5



# turtle.done()

# n = 20
# ang = 360/n


# for i in range(n):
#     t.circle(80) #80 : 픽셀 : (원의 반지름)
#     t.left(ang)   #60 : 각도 

# for i in range(20):
#     t.circle(80) #80 : 픽셀 : (원의 반지름)
#     t.left(18)   #60 : 각도 



#turtle.done()













#for i in range(1, 10):
 #    if i%3 == 1:
  #       i








# s = 50

# if s >= 90:
#     st.write('귀하의 점수는'+ str(s)+'점으로 :blue[A등급]입니다')

# elif s >= 80:
#     '귀하의 점수는'+ str(s) +'점으로 :green[B등급]입니다'
# elif s >= 70:
#     '귀하의 점수는'+ str(s) +'점으로 :orange[C등급]입니다'
# elif s >= 60:
#     '귀하의 점수는'+ str(s) +'점으로 :blue[D등급]입니다'
# else:
#     '귀하의 점수는'+ str(s) +'점으로 :red[F등급]입니다'










# s = 0 #초기값
# for i in range(1, 101, 2):
#     # 's = ', s , 'i = ', i
#     # s = s + i
#     s += i
#     # 's + i', s





# 1 + 2 + 3 + 4 + 5











# '7과 4의 산술 연산'

# '덧셈', 7 + 4
# '뺄셈', 7 - 4
# '곱셈', 7 * 4
# '나눗셈', 7 / 4
# '몫', 7 // 4
# '나머지', 7 % 4





# t = turtle.Turtle()
# t.shape('turtle')


# t. shape('turtle')


# r = 20
# area = 3.14*r*r
# area


# distance=150
# angle=120
# for i in range(3):
#     t.forward(distance)
#     t.left(angle)

# import turtle
# t = turtle.turtle()
# t.shape('turtle')
# t.speel(1)


# turtle.done()
# a = 3.141592*10*10.0
# b = (1/100)*1234

# print(a)
# a,b 

# print('Hello')
# st.write('Hello')

# st.write('강아지'+'고양이') 



#st.write('스트림릿')
#st.title('streamlit Image')
#st.imagr('im.jpg')

