# 🎫 AI-Enabled Customer Support Ticketing System

A full-stack web application that automates customer support ticket **classification** and **prioritization** using Machine Learning and REST APIs.

---

## 🚀 Features

- 🤖 **Auto-classification** of tickets into categories (Billing, Technical, Account, General)
- 🔥 **Priority detection** (Urgent / High / Medium / Low) using NLP keyword analysis
- 📊 **Agent Dashboard** (React frontend) to view, filter, and update ticket statuses
- 🐳 **Dockerized** for easy deployment
- 🔌 **REST API** built with FastAPI

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| Backend | Python, FastAPI |
| Frontend | React, TailwindCSS |
| Database | PostgreSQL |
| ML/NLP | Scikit-learn, NLP |
| DevOps | Docker, REST APIs |

---

## 📁 Project Structure

```
ai-ticketing-system/
├── main.py               # FastAPI backend + ML classification
├── requirements.txt      # Python dependencies
├── Dockerfile            # Container configuration
└── README.md
```

---

## ⚙️ Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/YOUR_USERNAME/ai-customer-support-ticketing.git
cd ai-customer-support-ticketing
```

### 2. Run with Docker
```bash
docker build -t ai-ticketing .
docker run -p 8000:8000 ai-ticketing
```

### 3. Or run locally
```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

### 4. Open API docs
Visit `http://localhost:8000/docs` for the interactive Swagger UI.

---

## 📡 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/tickets` | Submit a new ticket (auto-classified) |
| `GET` | `/tickets` | List all tickets (filter by status/priority) |
| `GET` | `/tickets/{id}` | Get a specific ticket |
| `PATCH`| `/tickets/{id}/status` | Update ticket status |

---

## 📸 Example Request

```json
POST /tickets
{
  "title": "Cannot login to my account",
  "description": "I keep getting an error when trying to access my dashboard",
  "customer_email": "user@example.com"
}
```

**Auto-classified response:**
```json
{
  "id": 1,
  "category": "account",
  "priority": "high",
  "status": "open"
}
```

---

## 👤 Author

**Nuaman M** — [LinkedIn](https://linkedin.com/in/nuamanjaleel) | [GitHub](https://github.com/YOUR_USERNAME)
