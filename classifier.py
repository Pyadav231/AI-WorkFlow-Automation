def classify_email(text):
    text = text.lower()

    if "not working" in text or "issue" in text:
        return "Complaint"
    elif "price" in text or "details" in text:
        return "Inquiry"
    else:
        return "Feedback"