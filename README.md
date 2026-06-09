# Recipe_App

## Description

A simple Django-based web application for managing recipes. Users can create, view, edit, and delete recipes, each consisting of a title, description, ingredients, and instructions. it's a basic project that makes us understand how CRUD operations are performed and what actually happens when we create, read, update or delete any data.

## Features

- List all recipes
- Create recipes via a form
- Read recipe details
- Update recipes inline 
- Delete recipes
- Responsive UI using Django templates for CRUD Operations

## Prerequisites

- Python 3.9+ (tested with 3.11)
- pip (Python package manager)
- Virtual environment (recommended)

## Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Recipe_App
   ```
2. **Create and activate a virtual environment**
   ```bash
   python -m venv .venv
   # Windows
   .venv\Scripts\activate
   # macOS/Linux
   source .venv/bin/activate
   ```
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
4. **Apply database migrations**
   ```bash
   python manage.py migrate
   ```
5. **Run the development server**
   ```bash
   python manage.py runserver
   ```
   Open a browser and navigate to `http://127.0.0.1:8000/` to view the app.

## Usage

- **Add a recipe**: Use the form on the homepage. The page will refresh automatically to show the new recipe.
- **Edit a recipe**: Click the *Edit* button on a recipe detail page; changes are saved via AJAX.
- **Delete a recipe**: Click the *Delete* button; the recipe is removed without a full page reload.

## Development

- To create a new app or modify the existing one, edit files under `web_app/` and templates under `templates/`.
- Static files (CSS/JS) can be placed in `static/` (create the folder if needed) and referenced in templates.

## Testing

*No automated tests are included yet.* You can add unit tests using Django's `TestCase` in a `tests.py` module inside `web_app/`.

## Contributing

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Ensure code follows the existing style.
4. Submit a pull request with a clear description of changes.

## License

This project is licensed under the MIT License – see the `LICENSE` file for details.

## Repository Structure

```
Recipe_App/
├─ .git/                 # Git metadata (do not modify manually)
├─ .gitignore            # Files/folders ignored by git
├─ README.md             # Project documentation (this file)
├─ requirements.txt      # Python dependencies
├─ manage.py             # Django command-line utility
├─ db.sqlite3            # **Do NOT commit** – local development database
├─ web_project/          # Django project settings
│   ├─ __init__.py
│   ├─ settings.py
│   ├─ urls.py
│   └─ wsgi.py
├─ web_app/              # Main application
│   ├─ __init__.py
│   ├─ models.py
│   ├─ views.py
│   ├─ forms.py
│   └─ templates/       # HTML templates (templates/ folder can also be at root)
├─ templates/            # Shared templates folder (referenced in settings)
└─ static/               # (Optional) static assets like CSS/JS
```

## What to Keep in GitHub

- All source code (`web_project/`, `web_app/`, `templates/`, `static/` if present)
- `manage.py`
- `requirements.txt`
- `README.md`
- `.gitignore`
- License file (e.g., `LICENSE`)
- Any migration files under `web_app/migrations/` (if created)

## What NOT to Commit

- `db.sqlite3` (local SQLite database)
- Virtual environment folders (`.venv/`, `env/`, etc.)
- `__pycache__/` directories and `.pyc` files
- Secret keys or local settings (avoid committing `SECRET_KEY` changes; consider using environment variables for production)
- IDE/editor specific files (`.vscode/`, `.idea/`)
- OS generated files (`Thumbs.db`, `.DS_Store`)

Ensure your `.gitignore` file contains the above patterns (it already does).

---

*Happy coding!*