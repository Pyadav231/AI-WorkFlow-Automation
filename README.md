# 🚀 AI Email Automation System

## 📌 Overview

This project is a **full-stack AI Workflow Automation System** that processes emails end-to-end.
It classifies emails using a Machine Learning model, assigns priority, and generates automated responses.

The system consists of:

* 🧠 ML Model (TF-IDF + Naive Bayes)
* ⚙️ Backend API (FastAPI)
* 🎨 Frontend UI (Streamlit)

---

## 🎯 Features

* ✅ Email classification (Complaint, Inquiry, Feedback)
* ✅ Priority assignment (High, Medium, Low)
* ✅ Automated response generation
* ✅ REST API using FastAPI
* ✅ Interactive UI using Streamlit
* ✅ Logging and error handling
* ✅ End-to-end workflow automation

---

## 🧠 Tech Stack

* Python
* FastAPI
* Streamlit
* Scikit-learn (ML)
* Uvicorn

---

## 📂 Project Structure

```
ai-workflow-automation/
│
├── app.py
├── ml_classifier.py
├── classifier.py
├── response_generator.py
├── ui.py
├── requirements.txt
└── README.md
```

---

## ⚙️ How It Works

```
User Input (Email)
        ↓
ML Classification (TF-IDF + Naive Bayes)
        ↓
Priority Assignment
        ↓
Response Generation
        ↓
API Response (FastAPI)
        ↓
Displayed on UI (Streamlit)
```

---

## ▶️ Installation & Setup

### 1. Clone Repository

```bash
git clone https://github.com/Pyadav231/AI-WorkFlow-Automation.git
cd ai-workflow-automation
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🚀 Run the Project

### 🔹 Start FastAPI Backend

```bash
uvicorn app:app --reload
```

👉 Runs on: http://127.0.0.1:8000

---

### 🔹 Start Streamlit UI

```bash
streamlit run ui.py
```

👉 Runs on: http://localhost:8501

---

##  API Testing (Swagger UI)

👉 Open:

```
http://127.0.0.1:8000/docs
```

### Sample Input:

```json
{
  "email": "I have an issue with your service"
}
```

### Sample Output:

```json
{
  "category": "Complaint",
  "priority": "High",
  "response": "We are sorry for the inconvenience. Our team will resolve this issue soon."
}
```

---

## 📸 Screenshots

### 🔹 Streamlit UI
https://1drv.ms/i/c/fb772e05d8606035/IQD1nNIxB6VtTq2s4nem0VPPATTEyYLMa4H0rTxqaYgNYqg?e=CwQBX8


### 🔹 FastAPI Swagger
https://1drv.ms/i/c/fb772e05d8606035/IQD1nNIxB6VtTq2s4nem0VPPATTEyYLMa4H0rTxqaYgNYqg?e=X2KDRo

---

## 🧠 Machine Learning Model

* TF-IDF Vectorizer
* Multinomial Naive Bayes
* Trained on sample email dataset

---

## ⚠️ Error Handling

* Handles empty input
* Logs requests and responses
* Returns meaningful error messages

---

## 🔮 Future Improvements

* Use advanced NLP models (BERT / LLM)
* Add database integration
* Deploy on cloud (Render / AWS)
* Multi-language support
* Email auto-reply integration

---

## 👨‍💻 Author

**Pawan Kumar Yadav**
yadavpawan3167@gmail.com
 GitHub: @Pyadav231
---

## ⭐ Conclusion

This project demonstrates a complete **AI-powered workflow automation system** combining Machine Learning, Backend APIs, and Frontend UI — making it a strong real-world project for internships and job applications.
