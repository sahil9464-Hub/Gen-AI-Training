import pandas as pd

data = {
    "ID": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    "Product Name": [
        "Laptop", "Mouse", "Keyboard", "Monitor", "Printer",
        "USB Drive", "Router", "Webcam", "Headphones", "Speaker"
    ],
    "Price": [55000, 500, 1200, 15000, 9000, 700, 2500, 1800, 2200, 3500],
    "Quantity": [10, 50, 30, 15, 8, 100, 20, 18, 25, 12],
    "Seller Name": [
        "Amit Traders", "Tech World", "Digital Hub", "Screen House",
        "Print Solutions", "Storage Mart", "Net Zone", "Vision Tech",
        "Audio Store", "Sound Hub"
    ],
    "Mobile": [
        9876543210, 8765501234, 9811122233, 9898989898, 9123456780,
        9988776655, 9090909090, 934567890, 9765432109, 9012345678
    ],
    "City": [
        "Delhi", "Mumbai", "Pune", "Bengaluru", "Chennai",
        "Hyderabad", "Kolkata", "Jaipur", "Lucknow", "Ahmedabad"
    ]
}

df = pd.DataFrame(data)

# particular row using loc
print(df.loc[3])

# particular row using iloc
print(df.iloc[3])

# particular cell using loc
print(df.loc[2, "City"])

# particular cell using iloc
print(df.iloc[2, 6])

# particular column using loc
print(df.loc[:, "Product Name"])

# particular column using iloc
print(df.iloc[:, 1])

# multiple columns using loc
print(df.loc[:, ["Product Name", "Price", "City"]])

# multiple columns using iloc
print(df.iloc[:, [1, 2, 6]])

# multiple rows using loc
print(df.loc[[1, 3, 5]])

# multiple rows using iloc
print(df.iloc[[1, 3, 5]])

# rows from index 2 to 6 using loc
print(df.loc[2:6])

# rows from position 2 to 6 using iloc
print(df.iloc[2:7])

# rows 2 to 6 and selected columns using loc
print(df.loc[2:6, ["Product Name", "Price"]])

# rows 2 to 6 and selected columns using iloc
print(df.iloc[2:7, [1, 2]])

# first five rows using loc
print(df.loc[:4])

# first five rows using iloc
print(df.iloc[:5])

# last three rows using loc
print(df.loc[7:])

# last three rows using iloc
print(df.iloc[-3:])

# first three columns using loc
print(df.loc[:, "ID":"Price"])

# first three columns using iloc
print(df.iloc[:, :3])

# price greater than 5000
print(df.loc[df["Price"] > 5000])

# quantity greater than 20
print(df.loc[df["Quantity"] > 20])

# products from Delhi
print(df.loc[df["City"] == "Delhi"])

# products with price less than 5000
print(df.loc[df["Price"] < 5000])

# products with price equal to 15000
print(df.loc[df["Price"] == 15000])

# products with quantity equal to 10
print(df.loc[df["Quantity"] == 10])

# price greater than 5000 and quantity greater than 10
print(df.loc[(df["Price"] > 5000) & (df["Quantity"] > 10)])

# price greater than 5000 or quantity greater than 50
print(df.loc[(df["Price"] > 5000) | (df["Quantity"] > 50)])

# products from Delhi or Mumbai
print(df.loc[(df["City"] == "Delhi") | (df["City"] == "Mumbai")])

# price between 1000 and 5000
print(df.loc[(df["Price"] >= 1000) & (df["Price"] <= 5000)])

# get only product name where price is greater than 5000
print(df.loc[df["Price"] > 5000, "Product Name"])

# get product name and price where price is greater than 5000
print(df.loc[df["Price"] > 5000, ["Product Name", "Price"]])

# get seller name and city where quantity is greater than 20
print(df.loc[df["Quantity"] > 20, ["Seller Name", "City"]])

# get product name, price and quantity where city is Mumbai
print(df.loc[df["City"] == "Mumbai", ["Product Name", "Price", "Quantity"]])

# get rows where price is greater than 5000 using iloc
print(df.iloc[(df["Price"] > 5000).values])

# get rows where quantity is greater than 20 using iloc
print(df.iloc[(df["Quantity"] > 20).values])

# change price of a particular row using loc
df.loc[0, "Price"] = 60000

# change quantity of a particular row using loc
df.loc[1, "Quantity"] = 60

# change city of a particular row using loc
df.loc[2, "City"] = "Delhi"

# change price using iloc
df.iloc[3, 2] = 16000

# change multiple columns of a particular row using loc
df.loc[4, ["Price", "Quantity"]] = [10000, 10]

# change multiple columns using iloc
df.iloc[5, [2, 3]] = [800, 120]

# change price of all products where price is less than 2000
df.loc[df["Price"] < 2000, "Price"] = 2000

# change quantity where quantity is greater than 50
df.loc[df["Quantity"] > 50, "Quantity"] = 50

# select rows and columns using loc
print(df.loc[2:6, "Product Name":"City"])

# select rows and columns using iloc
print(df.iloc[2:7, 1:7])

# select alternate rows using iloc
print(df.iloc[::2])

# select alternate columns using iloc
print(df.iloc[:, ::2])

# select last column using iloc
print(df.iloc[:, -1])

# select last row using iloc
print(df.iloc[-1])

# select second last row using iloc
print(df.iloc[-2])

# select last two columns using iloc
print(df.iloc[:, -2:])

# select first two rows and first three columns
print(df.iloc[:2, :3])
