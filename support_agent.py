import pandas as pd
import joblib

from response_generator import generate_response

# Load intent classifier
model = joblib.load("intent_classifier.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

# Load historical response data
response_df = pd.read_csv("amazon_response_pairs.csv")

# Load response retrieval system
response_vectorizer = joblib.load("response_vectorizer.pkl")
response_retriever = joblib.load("response_retriever.pkl")


def support_agent(message):
    # -----------------------------
    # 1. Predict customer intent
    # -----------------------------
    message_tfidf = vectorizer.transform([message])

    probabilities = model.predict_proba(message_tfidf)[0]

    index = probabilities.argmax()

    intent = model.classes_[index]

    confidence = probabilities[index]

    # -----------------------------
    # 2. Check confidence
    # -----------------------------
    if confidence < 0.50:
        response = (
            "I'm sorry, but I'm not completely sure I understand your issue. "
            "Could you please provide a little more detail so I can help you?"
        )

        return intent, confidence, response

    # -----------------------------
    # 3. Find similar historical conversation
    # -----------------------------
    message_vector = response_vectorizer.transform([message])

    distance, index = response_retriever.kneighbors(message_vector)

    similarity = 1 - distance[0][0]

    # -----------------------------
    # 4. Generate clean response
    # -----------------------------
    response = generate_response(intent)

    return intent, confidence, response


print("AmazonHelp Support Agent")
print("========================")

while True:
    message = input("\nCustomer: ")

    if message.lower() == "exit":
        print("Goodbye!")
        break

    intent, confidence, response = support_agent(message)

    print("Detected intent:", intent)
    print("Confidence:", round(confidence, 2))
    print("Support response:", response)