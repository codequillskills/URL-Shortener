# URLShortener

URLShortener is a web application built using Django, HTML, CSS, and JavaScript. It allows users to shorten long URLs for easier sharing and management.

## Table of Contents

- [Features](#features)
- [Technologies](#technologies)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

- URL shortening and management

## Technologies

- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Django
- **Database:** sqlite3

## Prerequisites

- Python (3.8 or above)
- Git

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/codequillskills/URL-Shortener
   ```

2. Create a virtual environment:

   ```bash
   python -m venv ./env
   cd env/scripts
   activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Add the `.env` file in the root directory with the following content:

   ```plaintext
    SECRET_KEY=Your_Secret_key
    DEBUG=False
    ALLOWED_HOSTS=localhost,127.0.0.1
   ```

5. Set up your database:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. Create a superuser:

   ```bash
   python manage.py createsuperuser
   ```

7. Run the development server:

   ```bash
   python manage.py runserver
   ```

8. Access the application at `http://localhost:8000/`

## Usage

1. Shorten your URLs.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature-name`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature-name`).
5. Open a Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.