import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression  # class

# ML implementation - Python

data = {
    "study-hour": [1, 2, 3, 4, 5, 6, 7, 8, 9],
    "marks": [35, 40, 45, 50, 55, 60, 65, 70, 75]
}

# Create DataFrame
df = pd.DataFrame(data)

print(df)

# Shape of data
print(df.shape)

# Correlation
print(df.corr())

# Scatter plot
sns.scatterplot(data=df, x="study-hour", y="marks")

plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Study Hours vs Marks")
plt.show()

# Feature and Target
# X = Feature
# y = Target

X = df[["study-hour"]]   # 2-D
y = df["marks"]          # 1-D


# Build Model
model = LinearRegression()

# Train Model

model.fit(X, y)

# Get m and c
# y = mx + c

m = model.coef_[0]
print("m =", round(m, 2))

c = model.intercept_
print("c =", round(c, 2))

# Prediction

study_hours = float(input("Enter study hours: "))

# Using trained model
predicted_marks = model.predict([[study_hours]])

print("Predicted marks =", round(predicted_marks[0], 2))
