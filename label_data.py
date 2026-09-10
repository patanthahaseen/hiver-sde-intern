import pandas as pd

df = pd.read_csv("amazon_customers.csv")

text = df["text"].fillna("").str.lower()

df["intent"] = "other"

rules = [
    (
        "account_login",
        r"password|log.?in|login|sign.?in|reset.*(password|code)|account.*(access|locked)|can.?t access"
    ),
    (
        "payment_billing",
        r"payment|charged|charge|billing|cashback|price|pricing|card.*charged"
    ),
    (
        "prime_membership",
        r"prime member|prime membership|amazon prime|prime subscription|prime account"
    ),
    (
        "digital_content",
        r"prime video|kindle|music|movie|streaming|episode|song|video.*not.*play|not.*playing"
    ),
    (
        "return_refund",
        r"refund|return|exchange|damaged|damage|broken|wrong item|missing item|replacement"
    ),
    (
        "product_issue",
        r"echo|fire stick|fire tv|device|alexa|xbox|kindle.*device|app.*not.*working|not.*working"
    ),
    (
        "delivery_issue",
        r"not delivered|not arrived|hasn.?t arrived|hasn.?t been delivered|late|delayed|delivery.*late|delivery.*delay|courier|delivered.*not|marked.*delivered|delivery date|shipping delay"
    ),
    (
        "order_status",
        r"order|pre.?order|tracking|shipment|shipping|where.*(package|parcel|order)|when.*(arrive|arriving|delivery)|expected.*delivery"
    ),
]

for intent, pattern in rules:
    mask = (df["intent"] == "other") & text.str.contains(
        pattern, regex=True, na=False
    )
    df.loc[mask, "intent"] = intent

print("\nIntent counts:")
print(df["intent"].value_counts())

df.to_csv("amazon_labeled_v2.csv", index=False)

print("\nSaved: amazon_labeled_v2.csv")