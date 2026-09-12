\# AmazonHelp AI Support Agent



\## Overview



This project builds an AI customer-support agent for AmazonHelp using the Twitter Customer Support dataset.



The system:



1\. Extracts AmazonHelp customer-support conversations.

2\. Classifies customer messages into support intents.

3\. Uses a machine-learning model to predict the customer's intent.

4\. Generates an intent-specific support response.

5\. Provides a confidence score for each prediction.

6\. Uses a fallback response when the model confidence is low.



\## Target Brand



AmazonHelp



\## Dataset



The project uses the Twitter Customer Support dataset (TWCS).



The original dataset contains customer-support conversations between customers and brands on Twitter.



For this project, AmazonHelp was selected because it contains a large number of support interactions.



\## Intent Categories



The classifier uses 8 customer-support intents:



\- delivery\_issue

\- order\_status

\- return\_refund

\- payment\_billing

\- account\_login

\- prime\_membership

\- digital\_content

\- product\_issue



\## Data Preparation



Customer messages directly associated with AmazonHelp responses were extracted from the original dataset.



The data was automatically labeled using keyword-based rules and then balanced to create:



\- 8 intents

\- 1,000 messages per intent

\- 8,000 total messages



The dataset was split into:



\- Training: 6,400 messages

\- Testing: 1,600 messages



\## Machine Learning Model



The classifier uses:



\- TF-IDF Vectorization

\- Logistic Regression



TF-IDF converts customer messages into numerical text features.



Logistic Regression then predicts the most likely customer-support intent.



\## Model Performance



The classifier achieved:



\*\*Accuracy: 86.19%\*\*



The model was evaluated using:



\- Accuracy

\- Precision

\- Recall

\- F1-score

\- Confusion Matrix



The confusion matrix is saved as:



`confusion\_matrix.png`



\## Support Agent

The support agent combines the trained classifier with response templates.



For example:



Customer:



> My package says delivered but I haven't received it.



Predicted intent:



`delivery\_issue`



The agent then generates a delivery-specific support response.

The agent also provides a confidence score.

If confidence is below the configured threshold, the system asks the customer for more information instead of providing a potentially incorrect intent-specific response.

## Historical Response Retrieval

The project also uses historical AmazonHelp customer-support conversations to find similar past customer messages.

A TF-IDF based retrieval system searches the historical conversations and calculates a similarity score for the closest match.

The retrieved response is used as a reference signal rather than being copied directly. This avoids returning responses containing unrelated usernames, links, or conversation-specific information.

The retrieval system helps the agent identify whether a customer's message is similar to previously handled AmazonHelp issues.

For example, a customer message such as:

> My package says delivered but I haven't received it.

can be matched with a similar historical AmazonHelp conversation.

The system reports the historical similarity score along with the predicted intent and classifier confidence.


## Evaluation & Demo Results

The intent classifier was evaluated on a held-out test set of 1,600 customer messages.

Accuracy: 86.19%

All 8 supported intents were manually tested using representative customer messages.

The agent successfully demonstrated:
- Intent classification
- Confidence scoring
- Historical response similarity
- Intent-specific support responses
- Low-confidence fallback behavior

Example:

> My package says delivered but I haven't received it.

Detected intent: `delivery_issue`  
Confidence: 0.58  
Historical similarity: 0.70

The agent generated a delivery-specific support response instead of directly copying the historical response.

A low-confidence example was also tested:

> help

Confidence: 0.19

The agent correctly requested additional information instead of providing an uncertain intent-specific response.



If confidence is below the configured threshold, the system asks the customer for more information instead of providing a potentially incorrect intent-specific response.



\## Project Structure

```text

hiver-sde-intern/

│

├── twcs.csv

├── amazon\_support.csv

├── amazon\_customers.csv

├── amazon\_labeled.csv

├── amazon\_labeled\_v2.csv

├── amazon\_balanced.csv

├── train.csv

├── test.csv

│

├── label\_data.py

├── train\_classifier.py

├── test\_classifier.py

├── response\_generator.py

├── support\_agent.py

├── evaluate\_model.py
├── create_response_data.py
├── response_retriever.py
├── test_retriever.py

│

├── intent\_classifier.pkl

├── tfidf\_vectorizer.pkl

├── confusion\_matrix.png

├── requirements.txt

└── README.md

