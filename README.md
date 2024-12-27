# Discord Nation Alpha

Discord Nation Alpha is a community of gamers, developers, and artists. Our goal is to provide a platform for people to connect, collaborate, and create together. We are committed to fostering a safe and welcoming environment where creativity, innovation, and collaboration thrive.

## What we do

- Community management
- Influencer marketing
- Consultancy

## Technologies Used

- Django
- HTML
- CSS
- JavaScript
- PostgreSQL
- Neon (Cloud Database)

## Setup and Installation

### Prerequisites

- Python 3.x
- Django
- PostgreSQL
- pip (Python package installer)

### Installation

1. **Clone the repository:**

   ```sh
   git clone https://github.com/yourusername/discord-nation-alpha.git
   cd discord-nation-alpha
   ```

2. **Create and activate a virtual environment:**

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the dependencies:**

   ```sh
   pip install -r requirements.txt
   ```

4. **Set up the PostgreSQL database:**

   - Create a PostgreSQL database and user.
   - Update the `DATABASES` setting in `DNA/settings.py` with your database credentials.

5. **Run the migrations:**

   ```sh
   python manage.py migrate
   ```

6. **Collect static files:**

   ```sh
   python manage.py collectstatic
   ```

7. **Run the development server:**

   ```sh
   python manage.py runserver
   ```

8. **Access the application:**

   Open your web browser and go to `http://127.0.0.1:8000/`.

9. **Access the Health Check Endpoint:**

   Open your web browser and go to `https://your-render-service-url/api/health/`.
   You should see a JSON response: {"status": "ok"}.

## Running Tests

To run tests, use the following command:

```sh
python manage.py test
```

## License

This project is licensed under the MIT License.
