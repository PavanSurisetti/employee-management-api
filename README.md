# 🚀 Employee Management API

### *From REST API concepts to real database operations — one employee at a time*

---

## 📌 Overview

**Employee Management API** is a backend project built with **FastAPI, SQLAlchemy, and SQLite** to practice building REST APIs that communicate with a relational database.

This project represents an important step in my backend development journey — moving from learning individual FastAPI concepts to building an application that performs real database operations.

The application provides API endpoints for retrieving, filtering, updating, and deleting employee records.

---

## 🔗 Repository

👉 [Employee Management API](https://github.com/PavanSurisetti/employee-management-api)

---

## 🛠️ Technologies Used

* 🐍 Python
* ⚡ FastAPI
* 🗄️ SQLAlchemy
* 💾 SQLite
* 📦 Uvicorn
* 🌐 REST APIs
* 📖 Swagger / OpenAPI

---

## ✨ Features

* 👥 Retrieve all employees
* 🔍 Filter employees by department
* 💰 Update employee salaries based on department
* 🗑️ Delete employees based on salary conditions
* 🗄️ SQLite database integration
* 🔗 SQLAlchemy ORM
* 💉 FastAPI dependency injection using `Depends()`
* 🔄 Database session management
* 📊 Database filtering and querying
* ✏️ Database record updates
* ❌ Conditional record deletion
* 📖 Interactive Swagger API documentation

---

## 🔄 Application Flow

The application follows a simple backend request-response flow:

```text
        Client
          │
          ▼
      FastAPI API
          │
          ▼
   Dependency Injection
          │
          ▼
   Database Session
          │
          ▼
      SQLAlchemy
          │
          ▼
       SQLite
          │
          ▼
    API Response
```

This helped me understand how different backend components work together instead of treating them as separate concepts.

---

## 🧩 Core Concepts Practiced

### ⚡ FastAPI

* Creating API endpoints
* HTTP methods
* Path parameters
* Query parameters
* Request handling
* API responses
* Dependency injection
* Automatic API documentation

### 🗄️ SQLAlchemy

* Creating database models
* ORM concepts
* Database queries
* Filtering records
* Updating records
* Deleting records
* Committing database changes

### 💾 SQLite

* Creating a relational database
* Storing employee records
* Connecting SQLite with SQLAlchemy
* Performing database operations

---

## 📂 Project Structure

```bash
employee-management-api/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   └── schemas.py
│
├── tests/
│   └── test_employee.py
│
├── .gitignore
├── requirements.txt
├── README.md
└── LICENSE
```

> Update this structure according to the actual files and folders in the project.

---

## 🚀 Getting Started

Follow the steps below to run the project locally.

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/PavanSurisetti/employee-management-api.git
```

```bash
cd employee-management-api
```

---

### 2️⃣ Create a Virtual Environment

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### macOS / Linux

```bash
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Run the Application

If your application entry point is `app/main.py`:

```bash
uvicorn app.main:app --reload
```

If your `main.py` is in the root directory:

```bash
uvicorn main:app --reload
```

---

## 🌐 Access the API

Once the server is running:

### API

👉 http://127.0.0.1:8000

### Swagger UI

👉 http://127.0.0.1:8000/docs

### ReDoc

👉 http://127.0.0.1:8000/redoc

FastAPI automatically generates interactive API documentation, making it easy to test the endpoints directly from the browser.

---

## 🔌 API Endpoints

| Method   | Endpoint                             | Description                         |
| -------- | ------------------------------------ | ----------------------------------- |
| `GET`    | `/employees`                         | Retrieve all employees              |
| `GET`    | `/employees/department/{department}` | Filter employees by department      |
| `PUT`    | `/employees/salary/{department}`     | Update salaries based on department |
| `DELETE` | `/employees/salary/{salary}`         | Delete employees based on salary    |

> Update these endpoints if the actual routes in the project are different.

---

## 👨‍💼 Employee Data

An employee record can contain information such as:

```json
{
    "id": 1,
    "name": "John Doe",
    "department": "IT",
    "salary": 60000
}
```

The actual fields depend on the SQLAlchemy model implemented in the project.

---

## 🗄️ Database Architecture

The project uses **SQLite** as the database and **SQLAlchemy** as the ORM.

```text
FastAPI
   │
   ▼
SQLAlchemy ORM
   │
   ▼
SQLite Database
```

Instead of writing raw SQL for every operation, SQLAlchemy allows the application to work with database records through Python objects and queries.

---

## 💉 Dependency Injection

One of the important FastAPI concepts practiced in this project is **Dependency Injection**.

FastAPI's:

```python
Depends()
```

is used to provide database sessions to API endpoints.

Conceptually:

```text
API Request
     │
     ▼
FastAPI Endpoint
     │
     ▼
Database Dependency
     │
     ▼
SQLAlchemy Session
     │
     ▼
Database Operation
```

This makes database session management cleaner and reusable.

---

## 🔍 Database Operations

The project demonstrates several important database operations.

### 📥 Retrieve

Retrieve employee records from the database.

### 🔎 Filter

Filter employees based on their department.

### 💰 Update

Update employee salaries based on department conditions.

### 🗑️ Delete

Delete employee records when they satisfy salary-based conditions.

### 💾 Commit

Database changes are committed so that updates and deletions are persisted.

---

## 📚 What I Learned

This project helped me understand how an API communicates with a database.

### I practiced:

* Creating SQLAlchemy models
* Creating and connecting to a database
* Managing database sessions
* Using FastAPI dependency injection
* Working with `Depends()`
* Querying database records
* Filtering database records
* Updating records with SQLAlchemy
* Deleting records using conditions
* Committing database transactions
* Connecting REST APIs with a database

---

## 🔮 Future Improvements

There are several features I plan to add as I continue improving this project.

### 👥 Employee Management

* [ ] Add new employees
* [ ] Get employee by ID
* [ ] Update employee details
* [ ] Delete employee by ID
* [ ] Search employees by name

### 🔍 Advanced Filtering

* [ ] Filter by multiple departments
* [ ] Filter employees by salary range
* [ ] Sort employees by salary
* [ ] Sort employees by name
* [ ] Add pagination

### ✅ Validation

* [ ] Add Pydantic schemas
* [ ] Validate employee data
* [ ] Validate salary values
* [ ] Handle invalid department values
* [ ] Add meaningful error responses

### 🔐 Authentication & Security

* [ ] Add user authentication
* [ ] Add JWT authentication
* [ ] Add password hashing
* [ ] Add role-based authorization
* [ ] Protect sensitive endpoints

### 🧪 Testing

* [ ] Add unit tests
* [ ] Add API endpoint tests
* [ ] Add database tests
* [ ] Test success and error cases
* [ ] Add test coverage

### 🗄️ Database Improvements

* [ ] Move from SQLite to PostgreSQL
* [ ] Add database migrations with Alembic
* [ ] Improve database relationships
* [ ] Add indexes where required
* [ ] Improve transaction handling

### 🐳 Deployment

* [ ] Dockerize the application
* [ ] Add Docker Compose
* [ ] Add environment variables
* [ ] Deploy the API to the cloud
* [ ] Add CI/CD with GitHub Actions



---

## 🤝 Contribution

This is primarily a learning project, but suggestions and improvements are welcome.

If you would like to contribute:

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Commit your changes
5. Push the branch
6. Open a Pull Request

Please keep contributions clean, simple, and well documented.

---

## 📬 Contact

* 🐙 GitHub: [PavanSurisetti](https://github.com/PavanSurisetti)
* 💼 LinkedIn: [Pavan Surisetti](https://www.linkedin.com/in/pavan-surisetti-b3281228b/)

---

## ⭐ Support

If you find this project useful or are also learning backend development, feel free to ⭐ the repository.

---

## 📄 License

This project is licensed under the **MIT License**.

---

###
