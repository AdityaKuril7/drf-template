# Django REST Framework Starter Template

A reusable Django REST Framework starter template with a custom user model, avatar support, and JWT authentication using `djangorestframework-simplejwt`.

## 🚀 Features

- **Custom User Model** – Extended Django user model.
- **Avatar Support** – User profile avatar functionality.
- **JWT Authentication** – Access and refresh token authentication using Simple JWT.
- **Django REST Framework** – REST API development setup.
- **Environment Setup** – Virtual environment and dependency management using `uv`.

## 🛠️ Tech Stack

- Python
- Django
- Django REST Framework
- Django REST Framework Simple JWT
- uv

## ⚡ Quick Setup (One Command)

For Linux users with Fish shell:

- First go to the server dir and run this command

```fish
python -m venv myenv && source myenv/bin/activate.fish && pip install uv && uv pip install -r requirement.txt
```

This command automatically:

1. Creates a virtual environment.
2. Activates the virtual environment.
3. Installs `uv`.
4. Installs all project dependencies.

**Note:** Run this command from the project root directory.

## 📦 Manual Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
cd <project-directory>
```

### 2. Create Virtual Environment

```bash
python -m venv myenv
```

### 3. Activate Virtual Environment

**Linux / macOS (Fish Shell):**

```fish
source myenv/bin/activate.fish
```

**Linux / macOS (Bash / Zsh):**

```bash
source myenv/bin/activate
```

**Windows:**

```powershell
myenv\Scripts\activate
```

### 4. Install uv

```bash
pip install uv
```

### 5. Install Dependencies

```bash
uv pip install -r requirement.txt
```

## ⚙️ Configuration

Run database migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

Create a superuser:

```bash
python manage.py createsuperuser
```

## ▶️ Run Development Server

```bash
python manage.py runserver
```

The development server will be available at:

```text
http://127.0.0.1:8000/
```

## 🔐 Authentication

This template uses `djangorestframework-simplejwt` for JWT-based authentication.

- Access Token
- Refresh Token
- Token-based API authentication

## 📁 Project Structure

```text
project/
├── myenv/
├── user/
│   ├── migrations/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
├── media/
├── manage.py
├── requirement.txt
└── README.md
```

_Note: Update the project structure according to your actual application._

## 📄 License

This project is open-source and available for personal and educational use.
