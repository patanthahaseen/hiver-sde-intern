import pandas as pd

# Load the original dataset
df = pd.read_csv(
    "twcs.csv",
    usecols=[
        "tweet_id",
        "author_id",
        "inbound",
        "text",
        "in_response_to_tweet_id"
    ]
)

# AmazonHelp responses
amazon = df[
    (df["author_id"] == "AmazonHelp") &
    (df["inbound"] == False)
].copy()

# Customer messages
customers = df[df["inbound"] == True].copy()

# Match AmazonHelp responses with the customer message they answered
pairs = amazon.merge(
    customers[["tweet_id", "text"]],
    left_on="in_response_to_tweet_id",
    right_on="tweet_id",
    suffixes=("_response", "_customer")
)

# Keep only the useful columns
response_data = pairs[
    ["tweet_id_customer", "text_customer", "text_response"]
].copy()

response_data.columns = [
    "customer_message",
    "customer_message_text",
    "amazon_response"
]

# Remove empty responses
response_data = response_data.dropna(
    subset=["customer_message_text", "amazon_response"]
)

# Remove duplicate conversations
response_data = response_data.drop_duplicates(
    subset=["customer_message_text"]
)

# Save
response_data.to_csv(
    "amazon_response_pairs.csv",
    index=False
)

print("AmazonHelp response pairs:", len(response_data))
print("Saved: amazon_response_pairs.csv")