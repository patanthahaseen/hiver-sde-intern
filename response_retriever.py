import pandas as pd
import joblib

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors

# Load historical AmazonHelp conversations
df = pd.read_csv("amazon_response_pairs.csv")

# Remove empty messages
df = df.dropna(subset=["customer_message_text", "amazon_response"])

# Convert customer messages into TF-IDF features
vectorizer = TfidfVectorizer(
    lowercase=True,
    ngram_range=(1, 2),
    max_features=20000
)

X = vectorizer.fit_transform(df["customer_message_text"])

# Create nearest-neighbor search
retriever = NearestNeighbors(
    n_neighbors=1,
    metric="cosine"
)

retriever.fit(X)

# Save the retrieval components
joblib.dump(vectorizer, "response_vectorizer.pkl")
joblib.dump(retriever, "response_retriever.pkl")

print("Historical conversations:", len(df))
print("Retrieval system created successfully.")
print("Saved:")
print("response_vectorizer.pkl")
print("response_retriever.pkl")