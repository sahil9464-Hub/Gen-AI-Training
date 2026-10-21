import numpy as np

sales = np.array([120, 150, 180, 90, 200, 250, 175, 300, 220, 160])

# 1.find array information using the sales array 
# number of elements 
print("Number of elements: ",sales.size) 
# dimension 
print("Dimension: ",sales.ndim)
# data type 
print("Data type: ",sales.dtype) 
# shape 
print("Shape: ",sales.shape)

# 2.Calculate Total Sales
print("Total Sales: ",np.sum(sales))

# 3.Calculate Average Sales
print("Average Sales: ",np.average(sales))

# 4. Find Maximum and Minimum
# Maximum sales
print("Maximum Sales: ",np.max(sales))
# Minimum sales
print("Minimum Sales: ",np.min(sales))
# Index of maximum sales
print("Index of maximum sales: ",np.argmax(sales))
# Index of minimum sales
print("Index of minimum sales: ",np.argmin(sales))

# 5. Access Array Elements
# From the sales array:
print("Print first element: ",sales[0])
# Print last element
print("Print last element: ",sales[-1])
# Print 5th element
print("Print 5th element: ",sales[4])
# Print elements from index 2 to 6
print("Print elements from index 2 to 6: ",sales[2:7])

# 6. Reverse an Sales Array 
print("Reverse an Sales Array: ",sales[::-1])

# 7. Find Sales Greater Than 200
print("Find Sales Greater Than 200: ",sales[sales<200])


ages = np.array([22, 35, 28, 41, 19, 32, 25, 45, 30, 27])

# 8. Find Ages Between 25 and 35
print("Find Ages Between 25 and 35: ",ages[(ages>25) & (ages<35)])

marks = np.array([
    [85, 78, 92],
    [67, 75, 80],
    [90, 88, 95],
    [55, 60, 65],
    [72, 85, 78]
])

# 9. Display Student marks
# First student's marks
print("First student's marks: ",marks[0])
# Second student's marks
print("Second student's marks: ",marks[1])
# Marks of all students in first subject
print("Marks of all students in first subject: ",marks[:,0])
# Marks of all students in second subject
print("Marks of all students in second subject: ",marks[:,1])
# 10. Calculate Subject-wise Average
print("Calculate Subject-wise Average: ",np.mean(marks , axis=0))

prices = np.array([100, 250, 150, 500, 350, 120, 450, 200])

# 11. Increase Prices by 10%
prices = prices * 1.10
print("Prices Increases by 10% : ",prices)