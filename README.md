# FastAPI JWT CRUD App

A simple and fast API built with **FastAPI** and **SQLAlchemy** for performing CRUD operations on Users. This project includes basic user management endpoints with password hashing and is structured for scalability. 🚀

> **Note:** This project is currently a work in progress. More features (like full JWT authentication) will be added soon!

## 🛠️ Tech Stack

* **Framework:** FastAPI
* **Database ORM:** SQLAlchemy
* **Database Configuration:** Uses `.env` for the `DATABASE_URL` (Compatible with SQLite, PostgreSQL, MySQL)
* **Security:** Password Hashing (via `security.py`)

## 📂 Project Structure

```text
.
├── .env                # Environment variables (Database URL)
├── main.py             # FastAPI application and endpoints
├── models.py           # SQLAlchemy database models
├── schemas.py          # Pydantic models for data validation
├── crud.py             # Database CRUD operations
├── database.py         # Database connection and session management
└── security.py         # Password hashing utilities
```

## 🚀 Getting Started

### 1. Clone the repository (if applicable) or navigate to the project directory
```bash
cd <your-project-directory>
```

### 2. Create a virtual environment & install dependencies
```bash
python -m venv venv

# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate

# Install the required packages (make sure you have them installed)
pip install fastapi uvicorn sqlalchemy python-dotenv passlib
```

### 3. Setup Environment Variables
Create a `.env` file in the root directory if it does not exist and add your database URL:
```env
DATABASE_URL=sqlite:///./test.db
# Or for PostgreSQL: postgresql://user:password@localhost/dbname
```

### 4. Run the application
Start the FastAPI development server:
```bash
uvicorn main:app --reload
```
The server will start at `http://127.0.0.1:8000`.

## 📌 API Endpoints

Once the server is running, you can access the interactive API documentation (Swagger UI) at:
**[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)**

| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/users` | Create a new user (hashes password) |
| `GET` | `/users/` | Get a list of all users |
| `GET` | `/getdatabyid/{user_id}` | Get a specific user by their ID |
| `PUT` | `/updatedata/{user_id}` | Update an existing user's details |
| `DELETE` | `/deletedata/{user_id}` | Delete a user from the database |

## 🔮 Future Enhancements
- [ ] Complete JWT (JSON Web Tokens) Authentication flow
- [ ] User Login endpoint
- [ ] Protected routes using token verification
- [ ] Advanced error handling and logging

---
*Developed with FastAPI*
