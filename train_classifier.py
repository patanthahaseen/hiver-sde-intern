import pandas as pd
import joblib

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Load datasets
train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")

# Input text and labels
X_train = train["text"].fillna("")
y_train = train["intent"]

X_test = test["text"].fillna("")
y_test = test["intent"]

# Convert text into TF-IDF features
vectorizer = TfidfVectorizer(
    lowercase=True,
    ngram_range=(1, 2),
    max_features=30000
)

X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

# Train classifier
model = LogisticRegression(
    max_iter=1000
)

model.fit(X_train_tfidf, y_train)

# Make predictions
predictions = model.predict(X_test_tfidf)

# Evaluate
accuracy = accuracy_score(y_test, predictions)

print("\nAccuracy:", round(accuracy, 4))

print("\nClassification Report:")
print(classification_report(y_test, predictions))

# Save model and vectorizer
joblib.dump(model, "intent_classifier.pkl")
joblib.dump(vectorizer, "tfidf_vectorizer.pkl")

print("\nSaved:")
print("intent_classifier.pkl")
print("tfidf_vectorizer.pkl")