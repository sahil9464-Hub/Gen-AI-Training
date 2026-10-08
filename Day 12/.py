
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
df = pd.read_csv("house_price_dataset.csv")

print(df.head())
print(df.shape)
print(df.columns)
df.info()

print(df.isna().sum())
print(df.describe())


plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm", fmt=".2f")
plt.show()
sns.scatterplot(data=df)
plt.show()
sns.pairplot(data=df)
plt.show()

X = df[[
    "area",
    "bedrooms",
    "bathrooms",
    "stories",
    "parking",
    "age",
    "distance_city",
    "location_score",
    "furnished"
]]

y = df["price"]

print("Features shape:", X.shape)
print("Target shape:", y.shape)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("Training features:", X_train.shape)
print("Testing features:", X_test.shape)


model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)


print("Enter House Details for Price Prediction")

area = float(input("Enter area: "))
bedrooms = float(input("Enter number of bedrooms: "))
bathrooms = float(input("Enter number of bathrooms: "))
stories = float(input("Enter number of stories: "))
parking = float(input("Enter parking slots: "))
age = float(input("Enter house age (years): "))
distance_city = float(input("Enter distance from city center: "))
location_score = float(input("Enter location score: "))
furnished = float(input("Enter furnished status (1 for Yes, 0 for No): "))
user_data = pd.DataFrame([{
    "area": area,
    "bedrooms": bedrooms,
    "bathrooms": bathrooms,
    "stories": stories,
    "parking": parking,
    "age": age,
    "distance_city": distance_city,
    "location_score": location_score,
    "furnished": furnished
}])

prediction = model.predict(user_data)[0]
score=model.score(X_test,y_test)
print(f"\nPredicted House Price: ${prediction}")
print(f"model giving price with {score}%of accurate score price{prediction}")

