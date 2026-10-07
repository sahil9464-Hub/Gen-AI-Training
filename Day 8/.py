import numpy as np 

# n=np.array([1,2,3,4,5,6,7,8,9])
# print(np.sum(n))
# print(np.size(n))
# print(np.max(n))
# print(np.min(n))
# print(np.mean(n))
# print(np.median(n))
# print(np.cumsum(n))
# print(np.cumprod(n))

# for 2-d
# t=np.array([[1,2],[3,4]])
# print(np.cumsum(t))
# print(np.cumprod(t))

# for 3-d
# t=np.array([[1,2],[3,4],[5,6]])
# print(np.cumsum(t))
# print(np.cumprod(t))

# =============================================================
# axis=0 mean up and down
# axis=1 mean left to right

# n=np.array([
#     [10,20,30],
#     [40,50,60]
# ])
# print(n)
# print(np.sum(n,axis=0))
# print(np.sum(n,axis=1))

# for 3-d
# n=np.array([
#     [10,20,30],
#     [40,50,60],
#     [10,20,30]
# ])
# print(n)
# print(np.sum(n,axis=0))
# print(np.sum(n,axis=1))

# ======================================================
# *Pandas is used for perform operation on dataset
# there are two types
# 1. series(1-D) and 2.DataFrame(2-D)

import pandas as pd

# s1=pd.Series()
# print(s1)
# s2=np.array([1,2,3,4,5])
# s3=pd.Series(s2)
# print(s3)
# s4=pd.Series([11,22,33,44])
# print(s4)
# # customize indexing are important  in ml
# s5=pd.Series(["aman","chaman","daman"],index=["a","b","c"])
# print(s5)
# s6=pd.Series([10,20,30,40,50])
# print(s6.index)
# print(s6.shape) #for dimension
# print(s6.size)
# print(s6.values)
# print(s6.dtype) #type of data ml

# data=[
#     [1,"david","developer",2300,"noida"],
#     [2,"aman","opertaor",45300,"delhi"],
#     [3,"raman","hr",4800,"mohali"],
#     [4,"chaman","asssistant",6200,"punjab"]
# ]
# df = pd.DataFrame(data,columns=["Id","Name","POST","Salary","city"])
# print(df)

# ==========================================================
# 2nd way 2D Dataset

# emp={
#     "id":[1,2,3,4,5],
#     "name":["ram","sham","tom","dog","boyy"],
#     "post":["hr","pr","op","am","gm"],
#     "salary":[535,4534,5454,455,545],
#     "city":["jk","pb","up","kl","dl"]

# }
# df = pd.DataFrame(emp)
# print(df)

# # get only name
# print(df["name"])
# # get top 2
# print(df.head(2))
# # get last 2 element
# print(df.tail(2))
# # whose salarry greater than 545
# print(df[df["salary"]>545])
# # get salary b/w 32  to 54985
# print(df[df["salary"].between(32,54556)])
# # get min,max salary
# print(df["salary"].max())
# print(df["salary"].min())
# # get name,post and  salaary
# print(df[["name","post","salary"]])
# how to  add new coluumn interviewer will ask

#client mostly ask each and every months
# give me panda dataset like id , name ,post,salary,city and age
data = {
    "id": [101, 102, 103, 104, 105, 106, 107, 108],
    "name": ["Rahul", "Aman", "Priya", "Neha", "Rohit", "Simran", "Karan", "Anjali"],
    "post": ["Manager", "Developer", "HR", "Accountant", "Developer", "Manager", "Tester", "HR"],
    "salary": [60000, 45000, 40000, 38000, 50000, 65000, 42000, 43000],
    "city": ["Mohali", "Chandigarh", "Delhi", "Kharar", "Mohali", "Chandigarh", "Delhi", "Kharar"],
    "age": [35, 28, 30, 27, 29, 38, 26, 31]
}

d2 = pd.DataFrame(data)
print(2)

# task 1.add coluumn bonus >= 4000 5%
# 2.add column  hra salary 10%
# 3.add column caalculate gross salary
# 4.add column calculate net salary

# 1. Bonus = 5% if salary >= 4000
 d2["bonus"] = np.where(d2["salary"] >= 4000,d2["salary"] * 5 / 100,0)

# 2. HRA = 10% of salary
d2["hra"] = d2["salary"] * 10 / 100

# 3. Gross Salary
d2["gross_salary"] = d2["salary"] + d2["bonus"] + d2["hra"]

# 4. Net Salary
d2["net_salary"] = d2["gross_salary"]

print(d2)
