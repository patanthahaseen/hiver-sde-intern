import pandas as pd
import joblib
import matplotlib.pyplot as plt

from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Load test data
test = pd.read_csv("test.csv")

# Load trained model and vectorizer
model = joblib.load("intent_classifier.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

# Prepare test messages
X_test = test["text"].fillna("")
y_test = test["intent"]

# Convert text to TF-IDF
X_test_tfidf = vectorizer.transform(X_test)

# Predict intents
predictions = model.predict(X_test_tfidf)

# Accuracy
accuracy = accuracy_score(y_test, predictions)

print("Model Evaluation")
print("================")
print("Accuracy:", round(accuracy, 4))

# Classification report
print("\nClassification Report:")
print(classification_report(y_test, predictions))

# Confusion matrix
labels = sorted(y_test.unique())

cm = confusion_matrix(
    y_test,
    predictions,
    labels=labels
)

print("\nConfusion Matrix:")
print("Labels:", labels)
print(cm)

# Create confusion matrix chart
fig, ax = plt.subplots(figsize=(10, 8))

image = ax.imshow(cm)

ax.set_xticks(range(len(labels)))
ax.set_yticks(range(len(labels)))
ax.set_xticklabels(labels, rotation=45, ha="right")
ax.set_yticklabels(labels)

ax.set_xlabel("Predicted Intent")
ax.set_ylabel("Actual Intent")
ax.set_title("AmazonHelp Intent Classifier - Confusion Matrix")

# Add numbers to each cell
for i in range(len(labels)):
    for j in range(len(labels)):
        ax.text(j, i, cm[i, j], ha="center", va="center")

plt.tight_layout()

# Save chart
plt.savefig("confusion_matrix.png", dpi=200)

print("\nSaved: confusion_matrix.png")