import joblib

# Load the trained model and vectorizer
model = joblib.load("intent_classifier.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

# Test customer message
message = "Where is my order? I want to know when it will arrive."
# Convert message into TF-IDF
message_tfidf = vectorizer.transform([message])

# Predict intent
prediction = model.predict(message_tfidf)[0]

print("Customer message:", message)
print("Predicted intent:", prediction)