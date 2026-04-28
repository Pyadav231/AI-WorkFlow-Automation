from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

# 🔹 Training data (simple demo)
texts = [
    "I have an issue with product",
    "Your service is not working",
    "I want details about pricing",
    "Can you share product information",
    "Great service, I liked it",
    "This is amazing experience"
]

labels = [
    "Complaint",
    "Complaint",
    "Inquiry",
    "Inquiry",
    "Feedback",
    "Feedback"
]

# 🔹 Train
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(texts)

model = MultinomialNB()
model.fit(X, labels)

# 🔹 Predict function
def classify_email_ml(text):
    X_test = vectorizer.transform([text])
    return model.predict(X_test)[0]