import pandas as pd
import joblib

df = pd.read_csv("amazon_response_pairs.csv")

vectorizer = joblib.load("response_vectorizer.pkl")
retriever = joblib.load("response_retriever.pkl")

message = "My package says delivered but I haven't received it."

message_vector = vectorizer.transform([message])

distance, index = retriever.kneighbors(message_vector)

matched_row = df.iloc[index[0][0]]

similarity = 1 - distance[0][0]

print("Customer message:")
print(message)

print("\nMost similar historical customer message:")
print(matched_row["customer_message_text"])

print("\nHistorical AmazonHelp response:")
print(matched_row["amazon_response"])

print("\nSimilarity:", round(similarity, 3))