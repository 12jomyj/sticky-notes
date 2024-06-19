# Django Sticky Notes Application

A simple Django application for creating, viewing, editing, and deleting sticky notes.

## Table of Contents

- [Project Description](#project-description)
- [Installation](#installation)
- [Usage](#usage)
  - [Creating a Note](#creating-a-note)
  - [Viewing Notes](#viewing-notes)
  - [Editing a Note](#editing-a-note)
  - [Deleting a Note](#deleting-a-note)
- [Tests](#tests)
- [Credits](#credits)

## Project Description

This project is a practical coding task aimed at developing a basic sticky notes application using Django. The purpose of this project is to provide hands-on experience with Django's MVC architecture, CRUD operations, and testing framework.

## Installation

To run this project locally, follow these steps:

1. **Clone the repository:**

    ```sh
    git clone https://github.com/your-username/sticky_notes.git
    cd sticky_notes
    ```

2. **Create a virtual environment:**

    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Apply migrations:**

    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Create a superuser (optional, for admin access):**

    ```sh
    python manage.py createsuperuser
    ```

6. **Run the development server:**

    ```sh
    python manage.py runserver
    ```

## Usage

### Creating a Note

1. Navigate to the main menu by accessing the root URL (`http://127.0.0.1:8000/`).
2. Click on the "Create Note" button.
3. Fill in the title and content of the note.
4. Click "Save" to create the note.

### Viewing Notes

1. Navigate to the main menu (`http://127.0.0.1:8000/`).
2. Click on any note title to view the details of that note.


### Editing a Note

1. While viewing a note, click on the "Edit" button.
2. Modify the title or content as needed.
3. Click "Save" to update the note.


### Deleting a Note

1. While viewing a note, click on the "Delete" button.
2. Confirm the deletion in the confirmation page.


## Tests

To run the tests for this application, use the following command:

```sh
python manage.py test notes

Credits 
This project was delevloped by Jyothis Jomy