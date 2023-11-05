import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Load the dataset
df = pd.read_csv('emails.csv')

# Drop the 'Email No.' column as it's not needed for the model
df.drop(['Email No.'], axis=1, inplace=True)

# Split data
X = df.drop('Prediction', axis=1)
y = df['Prediction']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# K-Nearest Neighbors
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)
knn_pred = knn.predict(X_test)

# Support Vector Machine
svm = SVC(kernel='linear')
svm.fit(X_train, y_train)
svm_pred = svm.predict(X_test)

# Performance Analysis
# K-Nearest Neighbors
knn_accuracy = accuracy_score(y_test, knn_pred)
knn_conf_matrix = confusion_matrix(y_test, knn_pred)
knn_class_report = classification_report(y_test, knn_pred)

# Support Vector Machine
svm_accuracy = accuracy_score(y_test, svm_pred)
svm_conf_matrix = confusion_matrix(y_test, svm_pred)
svm_class_report = classification_report(y_test, svm_pred)

print("K-Nearest Neighbors:")
print(f"Accuracy: {knn_accuracy}")
print("Confusion Matrix:")
print(knn_conf_matrix)
print("Classification Report:")
print(knn_class_report)

print("\nSupport Vector Machine:")
print(f"Accuracy: {svm_accuracy}")
print("Confusion Matrix:")
print(svm_conf_matrix)
print("Classification Report:")
print(svm_class_report)