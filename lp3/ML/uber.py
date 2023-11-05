import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load the dataset
df = pd.read_csv('uber_data.csv')

# Step 1: Data Preprocessing
# Drop unnecessary columns
df.drop(['Unnamed: 0', 'key'], axis=1, inplace=True)

# Handle missing values
df.dropna(inplace=True)

# Convert 'pickup_datetime' to datetime and extract features
df['pickup_datetime'] = pd.to_datetime(df['pickup_datetime'])
df['hour'] = df['pickup_datetime'].dt.hour
df['day'] = df['pickup_datetime'].dt.day
df['month'] = df['pickup_datetime'].dt.month
df['year'] = df['pickup_datetime'].dt.year
df.drop(['pickup_datetime'], axis=1, inplace=True)

# Step 2: Identify Outliers
# You can use a boxplot to visualize outliers
# sns.boxplot(x=df['fare_amount'])
# plt.show()

# Remove outliers in 'fare_amount'
df = df[(df['fare_amount'] >= 0) & (df['fare_amount'] <= 100)]

# Step 3: Check Correlation
# Uncomment to plot
# sns.heatmap(df.corr(), annot=True)
# plt.show()

# Step 4: Implement Models
# Prepare data
X = df.drop('fare_amount', axis=1)
y = df['fare_amount']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Linear Regression
lr_model = LinearRegression()
lr_model.fit(X_train, y_train)
lr_pred = lr_model.predict(X_test)

# Random Forest
rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)
rf_pred = rf_model.predict(X_test)

# Step 5: Evaluate Models
# Linear Regression Metrics
lr_rmse = np.sqrt(mean_squared_error(y_test, lr_pred))
lr_r2 = r2_score(y_test, lr_pred)

# Random Forest Metrics
rf_rmse = np.sqrt(mean_squared_error(y_test, rf_pred))
rf_r2 = r2_score(y_test, rf_pred)

print(f"Linear Regression: RMSE = {lr_rmse}, R2 = {lr_r2}")
print(f"Random Forest: RMSE = {rf_rmse}, R2 = {rf_r2}")