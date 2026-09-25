# import numpy as np
# # 1-d array
# n1=np.array([1,2,3,4,5])
# print(n1)
# print(n1.size)
# print(type(n1))
# print(n1.ndim)
# # # all execution are part of EDA
# # jitna jayad EDA hoga ustna Accha machine train hoga

# # Model always accept 2-D array

# n2=np.array([1,2,3,4,5],[4,5,6,6])
# print(n2)
# print(n2.size)
# print(type(n2))
# print(n2.ndim) 

# n3=np.array([1,2,3,4,5],[4,5,6,6],,[3,6,8,8,6])
# print(n3)
# print(n3.size)
# print(type(n3))
# print(n3.ndim) 

# # in case you 3-d array then must be convert into 2-d 
# # then model trained

# # why 4-d doesmot support ml ?
# # our eyes doesn't support 4-d 

# n4=np.array([1,2,3,4,5],[4,5,6,6],,[3,6,8,8,6],[3,4,5,6])
# print(n4)
# print(n4.size)
# print(type(n4))
# print(n4.ndim)

# n4 = np.array(list(map(int,input("enter the elementts").split()))
# print(n4)

# ===========================================================

# import numpy as np
# n=int(input("enter the elements"))
# n5= np.array([int(input()) for i in range(n)])
# print(n5)

# ========================================================

# import numpy as np

# rows = int(input("Enter number of rows: "))
# cols = int(input("Enter number of cols: "))

# t = []

# for i in range(rows):
#     v = list(map(int, input().split()))
#     t.append(v)

# n6 = np.array(t)

# print(n6)

# =======================================
# zeros is used to recieve sensor sata(cameraa)
# z = np.zeros(4)
# print(z)
# z2 = np.zeroes((4,4))
# print(z2)

# ==================
# 1 is used to availability like product,loan and email
# 0 and 1 is mostly used in binary classification

# t1 = np.ones(4)
# print(t1)
# t2 = np.ones((3,4))
# print(t2)

# # identity matrix is used for co-relation
# # in ML eye replace with t3.corr() method

# t3 

# ===============================================
# why slicing or indexing in numpy 
# import numpy as np

# a1 = np.array([1,2,3,4,5,6,7,8,9])
# a2 = np.array([1,2,3,4],[5,6,7,8])
# a3 = np.array([1,2,3],[4,5,6],[7,8,9])

# # requirements 3,5,7 and[4,5,6] in 3-d

# print(a3[0,0,2])
# print(a3[0,1,1])
# print(a3[0,2,0])

# # 7th what is the first work in ml 
# # shape and reshape

# a1= np.array([1,2,3,4,5])
# print(a1.shape)
# a2=np.array([1,2,3,4,5,6,7,8,9])
# print(a2.shape)
# s=a2.reshape(3,3)
# print(s)

# ==============
import numpy as np

# x=np.arange(1,9)
# y=x.reshape(2,2,2)
# print(y)
# print(y.admin)

# =============
# next is age and salary,,bonuus,gross,net salary (inc or dec)
# in product ,if purchase 1000 then free delivery
# in oroduct ,if purchase 5000 then 5% discount
# is usedfor (inc or dec)
# a=np.array([1,2,3,4,5,6])
# x=a+2
# y=a*2
# print(x)
# print(y)

a1=np.array([1,2,3,4],[5,6,7,8])
a2=np.array([11,22,33,44])

z1 = a1+a2
z2=a1*a2
print(z1)
print(z2)

z3 = a1/a2
print(z3)
