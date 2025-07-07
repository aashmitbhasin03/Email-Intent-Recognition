# Intent Recognition

Intent Recognition is a Django web application for processing and classifying user queries, with a focus on email intent detection and automation workflows.

---

## Features

- Modular Django app structure for easy extension
- Handles user queries and processes them using Django views and utility functions
- Includes a template for email intent detection (`email_intent.html`)
- Easily extendable for new query types, APIs, or business logic

## Project Structure

```
flan_api/         # Main Django project (settings, URLs, WSGI, etc.)
queryapp/         # Django app for handling queries
  models.py       # Database models
  views.py        # Application views
  urls.py         # App-specific URL routes
  admin.py        # Django admin configuration
  utils.py        # Utility functions
  templates/      # HTML templates (e.g., email_intent.html)
  migrations/     # Database migrations
manage.py         # Django management script
db.sqlite3        # SQLite database file
```

## Getting Started

### 1. Clone the repository

```powershell
git clone https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git
cd flan_api
```

### 2. Create a virtual environment (recommended)

```powershell
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```powershell
pip install django
```

### 4. Apply migrations

```powershell
python manage.py migrate
```

### 5. Run the development server

```powershell
python manage.py runserver
```

Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser to access the app.

---

## Customization

- Update `settings.py` for your environment as needed
- Add new models, views, and templates in the `queryapp` app
- For email intent features, see `templates/email_intent.html`

## License

Specify your license here (e.g., MIT, Apache 2.0, etc.)
