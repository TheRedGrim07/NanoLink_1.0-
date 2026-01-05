<div align="center">

# 🔗 NanoLink  
### *Small Links, Big Reach*

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Flask](https://img.shields.io/badge/Flask-Backend-black.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

A **high-performance URL shortener** built with a strong focus on **system design, backend architecture, and scalability**.

</div>

---

## 📌 Overview

**NanoLink** is a TinyURL-style service that converts long URLs into short, shareable links and efficiently redirects users to the original destination.  
The project is designed to demonstrate **production-ready backend engineering practices** and **clean system design**, making it suitable for **resume reviews** and **GSoC evaluations**.

---

## 🧠 System Design

NanoLink follows a **stateless REST-based architecture** backed by a relational database for persistence.

### Design Principles

- **Base62 Encoding**  
  Short URLs are generated using Base62 encoding (`a-zA-Z0-9`), allowing compact, URL-safe identifiers.
- **Collision-Proof ID Generation**  
  Each URL is assigned a unique auto-incremented database ID, which is deterministically encoded into a Base62 string.
- **HTTP 302 Redirects**  
  Redirection is handled using HTTP 302 to ensure flexibility and support future analytics.
- **Persistent Storage**  
  URL mappings are stored using SQLite with SQLAlchemy ORM for reliability and maintainability.

### Request Flow

User Browser
|
v
+------------+
| Flask API |
+------------+
|
v
+------------+
| Database |
+------------+
|
v
HTTP 302 Redirect
|
v
Original URL

yaml
Copy code

---

## ⚙️ Features

- High-performance URL redirection
- Base62 short ID generation
- Collision-safe hashing strategy
- RESTful API design
- Input validation and sanitization
- Lightweight relational persistence
- Clean, modular Flask architecture

---

## 🧩 Tech Stack

| Layer     | Technology            |
|-----------|-----------------------|
| Backend   | Python, Flask         |
| Database  | SQLite, SQLAlchemy    |
| Frontend  | HTML, CSS, JavaScript |
| API Style | REST                  |

---

## 🚀 Setup Instructions

### Prerequisites
- Python 3.x
- pip

### Installation

```bash
# Clone the repository
git clone https://github.com/your-username/NanoLink.git
cd NanoLink

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
```

Server will be available at:
```bash
http://127.0.0.1:5000
```


## 📡 API Documentation

### Endpoints

| Method | Endpoint      | Description                    |
|--------|---------------|--------------------------------|
| POST   | `/shorten`    | Generate a short URL           |
| GET    | `/<short_id>` | Redirect to the original URL   |

### Example Request

**POST `/shorten`**

```json
{
  "url": "https://example.com/very/long/url"
}
```

**Response**
```json
{
   "short_url": "http://localhost:5000/aZ3k"
}
```

## 🔐 Validation & Error Handling

- URL format validation before storage
- Graceful handling of invalid short IDs
- Controlled HTTP redirects using HTTP status code **302**

---

## 📈 Scalability Considerations

NanoLink’s architecture supports future enhancements such as:

- Migration to PostgreSQL or MySQL
- Horizontal scaling with stateless Flask services
- Caching using Redis for hot URLs
- Click analytics and rate limiting

---

## 📄 License

This project is licensed under the **MIT License**.

---

## 👤 Author

Built with a focus on **backend engineering excellence**, **system design clarity**, and **production readiness**.
