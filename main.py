from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, List
import uvicorn
import random
from datetime import datetime

app = FastAPI(title="AI Customer Support Ticketing System", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Models ---
class Ticket(BaseModel):
    title: str
    description: str
    customer_email: str

class TicketResponse(BaseModel):
    id: int
    title: str
    description: str
    customer_email: str
    category: str
    priority: str
    status: str
    created_at: str

# --- In-memory DB (replace with PostgreSQL in production) ---
tickets_db = []
ticket_id_counter = 1

# --- ML Classification Logic ---
CATEGORIES = {
    "billing": ["payment", "invoice", "charge", "refund", "subscription", "price"],
    "technical": ["error", "bug", "crash", "not working", "broken", "issue", "fail"],
    "account": ["login", "password", "account", "access", "locked", "signup"],
    "general": []
}

PRIORITY_KEYWORDS = {
    "urgent": ["urgent", "asap", "immediately", "critical", "down", "outage"],
    "high": ["important", "serious", "broken", "error", "cannot"],
    "medium": ["problem", "issue", "help", "need"],
    "low": []
}

def classify_ticket(title: str, description: str) -> dict:
    text = (title + " " + description).lower()

    # Classify category
    category = "general"
    for cat, keywords in CATEGORIES.items():
        if any(word in text for word in keywords):
            category = cat
            break

    # Classify priority
    priority = "low"
    for prio, keywords in PRIORITY_KEYWORDS.items():
        if any(word in text for word in keywords):
            priority = prio
            break

    return {"category": category, "priority": priority}


# --- Routes ---
@app.get("/")
def root():
    return {"message": "AI Ticketing System API is running"}

@app.post("/tickets", response_model=TicketResponse)
def create_ticket(ticket: Ticket):
    global ticket_id_counter
    classification = classify_ticket(ticket.title, ticket.description)
    new_ticket = {
        "id": ticket_id_counter,
        "title": ticket.title,
        "description": ticket.description,
        "customer_email": ticket.customer_email,
        "category": classification["category"],
        "priority": classification["priority"],
        "status": "open",
        "created_at": datetime.now().isoformat()
    }
    tickets_db.append(new_ticket)
    ticket_id_counter += 1
    return new_ticket

@app.get("/tickets", response_model=List[TicketResponse])
def get_tickets(status: Optional[str] = None, priority: Optional[str] = None):
    result = tickets_db
    if status:
        result = [t for t in result if t["status"] == status]
    if priority:
        result = [t for t in result if t["priority"] == priority]
    return result

@app.get("/tickets/{ticket_id}", response_model=TicketResponse)
def get_ticket(ticket_id: int):
    ticket = next((t for t in tickets_db if t["id"] == ticket_id), None)
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return ticket

@app.patch("/tickets/{ticket_id}/status")
def update_ticket_status(ticket_id: int, status: str):
    ticket = next((t for t in tickets_db if t["id"] == ticket_id), None)
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    ticket["status"] = status
    return {"message": f"Ticket {ticket_id} updated to '{status}'"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
