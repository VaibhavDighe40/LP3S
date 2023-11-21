import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score

# Load the diabetes dataset
df = pd.read_csv("diabetes.csv")

print(df.columns)

print(df.head())

print(df.isnull().sum())

# Separate features (X) and target variable (y)
X = df.drop('Outcome', axis=1)
y = df['Outcome']

from sklearn.preprocessing import scale
X=scale(X)
print(X)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initialize the KNN classifier
knn = KNeighborsClassifier(n_neighbors=7)

# Fit the classifier to the training data
knn.fit(X_train, y_train)

# Predict the outcomes on the test set
y_pred = knn.predict(X_test)

# Compute confusion matrix
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix

# Assuming cs is the confusion matrix obtained from your previous code
cm = confusion_matrix(y_test, y_pred)
print(cm)

# Plotting the Confusion Matrix using Seaborn
plt.figure(figsize=(6, 4))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=['Predicted 0', 'Predicted 1'], yticklabels=['Actual 0', 'Actual 1'])
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix")
plt.show()

# Compute accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Compute error rate
total_misclassified = cm[0,1] + cm[1,0]
print(total_misclassified)
total_examples = cm[0,0]+cm[0,1]+cm[1,0]+cm[1,1]
print(total_examples)
print("Error rate ",total_misclassified/total_examples)

error_rate = 1 - accuracy
print("Error Rate:", error_rate)

# Compute precision
precision = precision_score(y_test, y_pred)
print("Precision:", precision)

# Compute recall
recall = recall_score(y_test, y_pred)
print("Recall:", recall)

from sklearn import metrics
print("Classification report ",metrics.classification_report(y_test,y_pred))

# Get user input for new features
new_features = []
for feature in df.columns[:-1]:
    value = float(input(f"Enter the value for {feature}: "))
    new_features.append(value)

# Scale the new features
new_features_scaled = scale([new_features])

# Make predictions for the new features
new_prediction = knn.predict(new_features_scaled)
print(f"Prediction for the new features: {new_prediction}")

