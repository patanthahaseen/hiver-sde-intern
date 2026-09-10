import joblib
from response_generator import generate_response

# Load the trained classifier and TF-IDF vectorizer
model = joblib.load("intent_classifier.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")


def support_agent(message):
    # Convert customer message into TF-IDF features
    message_tfidf = vectorizer.transform([message])

    # Get prediction probabilities
    probabilities = model.predict_proba(message_tfidf)[0]

    # Find the intent with the highest probability
    index = probabilities.argmax()
    intent = model.classes_[index]

    # Get confidence score
    confidence = probabilities[index]

    # Generate response
    # Generate response
    if confidence < 0.50:
       response = (
        "I'm sorry, but I'm not completely sure I understand your issue. "
        "Could you please provide a little more detail so I can help you?")
    else:
       response = generate_response(intent)
    return intent, confidence, response


# Test the support agent

# Interactive support agent
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