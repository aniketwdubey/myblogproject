# MyBlogProject

MyBlogProject is a simple Django-based blogging GraphQL API developed using the Strawberry framework. It focuses on providing basic functionalities for a blogging platform, including creating posts and adding comments.

## Table of Contents

- [Project Structure](#project-structure)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Project Structure

The project structure is as follows:


- `blog/`: Contains the Django app for the blogging functionalities.
- `myblogproject/`: Main project directory.
- `db.sqlite3`: SQLite database file.
- `manage.py`: Django's command-line utility for administrative tasks.

## Features

- **Post Creation**: Users can create new blog posts with titles, content, and author information.
- **Commenting**: Users can add comments to existing blog posts.
- **GraphQL API**: The API is implemented using the Strawberry framework, providing a GraphQL endpoint for interacting with the blog data.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/myblogproject.git
    ```

2. Navigate to the project directory:

    ```bash
    cd myblogproject
    ```

3. Create a virtual environment:

    ```bash
    python -m venv venv
    ```

4. Activate the virtual environment:

    - On Windows:

        ```bash
        venv\Scripts\activate
        ```

    - On macOS and Linux:

        ```bash
        source venv/bin/activate
        ```

5. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

6. Apply migrations:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```


## Usage

1. Run the development server:

    ```bash
    python manage.py runserver
    ```

2. Access the GraphQL endpoint at `http://localhost:8000/graphql/` to interact with the API.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature-name`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add some feature'`).
5. Push to the branch (`git push origin feature/your-feature-name`).
6. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


