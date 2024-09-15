---

# TV Show Management API

This project provides a RESTful API for managing TV shows, episodes, comments, and cast members. It is built using Django and Django REST Framework.

## Endpoints

### Shows

- **List Shows**
  - `GET /shows/`
  - Retrieves a list of all shows.

- **Create Show**
  - `POST /shows/`
  - Creates a new show.

- **Retrieve Show**
  - `GET /shows/{id}/`
  - Retrieves details of a specific show.

- **Update Show**
  - `PUT /shows/{id}/`
  - Updates a specific show.

- **Delete Show**
  - `DELETE /shows/{id}/`
  - Deletes a specific show.

### Episodes

- **List Episodes**
  - `GET /episodes/`
  - Retrieves a list of all episodes.

- **Create Episode**
  - `POST /episodes/`
  - Creates a new episode.

- **Retrieve Episode**
  - `GET /episodes/{id}/`
  - Retrieves details of a specific episode.

- **Update Episode**
  - `PUT /episodes/{id}/`
  - Updates a specific episode.

- **Delete Episode**
  - `DELETE /episodes/{id}/`
  - Deletes a specific episode.

### Comments

- **List Comments**
  - `GET /comments/`
  - Retrieves a list of all comments.

- **Create Comment**
  - `POST /comments/`
  - Creates a new comment.

- **Retrieve Comment**
  - `GET /comments/{id}/`
  - Retrieves details of a specific comment.

- **Update Comment**
  - `PUT /comments/{id}/`
  - Updates a specific comment.

- **Delete Comment**
  - `DELETE /comments/{id}/`
  - Deletes a specific comment.

### Cast

- **List Cast Members**
  - `GET /cast/`
  - Retrieves a list of all cast members.

- **Create Cast Member**
  - `POST /cast/`
  - Creates a new cast member.

- **Retrieve Cast Member**
  - `GET /cast/{id}/`
  - Retrieves details of a specific cast member.

- **Update Cast Member**
  - `PUT /cast/{id}/`
  - Updates a specific cast member.

- **Delete Cast Member**
  - `DELETE /cast/{id}/`
  - Deletes a specific cast member.

### Search Endpoints

- **Show Search**
  - `GET /shows/search/`
  - Search for shows based on query parameters.

- **Episode Search**
  - `GET /episodes/search/`
  - Search for episodes based on query parameters.

## Setup Instructions

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Django 3.2 or higher
- Django REST Framework

### Local Setup

1. **Clone the Repository**

   ```bash
   git clone https://github.com/ajuroshan/showtime.git
   cd showtime
   ```

2. **Create a Virtual Environment**

   ```bash
   python -m venv env
   ```

3. **Activate the Virtual Environment**

   - On Windows:
     ```bash
     .\env\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source env/bin/activate
     ```

4. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

5. **Apply Migrations**

   ```bash
   python manage.py migrate
   ```

6. **Create a Superuser (for accessing the Django admin panel)**

   ```bash
   python manage.py createsuperuser
   ```

7. **Run the Development Server**

   ```bash
   python manage.py runserver
   ```

   The API will be accessible at `http://127.0.0.1:8000/`.

8. **Access the Django Admin Panel**

   - URL: `http://127.0.0.1:8000/admin/`
   - Login with the superuser credentials created in step 6.

## Notes

Feel free to reach out if you have any questions or need further assistance!

---
