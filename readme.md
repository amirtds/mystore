## Installation

Follow these steps to get your development environment set up:

1. Clone the repository and navigate to the directory:

   ```sh
    mkdir django-performance && cd django-performance
    python3.12 -m venv venv
    source venv/bin/activate
    git clone -b main https://github.com/amirtds/mystore
    cd mystore
   ```
2. Install requirements and dependancies

    ```sh
    python3.12 -m pip install -r requirements.txt
    ```
3. Run migration and the development server

    ```sh
    python3.12 manage.py migrate
    python3.12 manage.py runserver
    ```
4. visit [127.0.0.1:8000](https://127.0.0.1:8000)