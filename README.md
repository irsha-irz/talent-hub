# TALENT HUB Platform using Django

![Project Banner](https://raw.githubusercontent.com/irsha-irz/talent-hub/refs/heads/master/socialmedia/media/profile_images/show.png)

Welcome to the Talen Hub Platform project built using Django! This project aims to create a basic social media platform for schools and collages where students (users) can register, log in, post images, rate images, connect with friends, and more. The platform provides a foundation that you can extend and customize to create your own unique social media experience.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)

## Features

- User registration and authentication
- User profiles with profile pictures and bio
- News feed displaying posts from friends
- Post creation and deletion
- Rate a posts
- User search functionality
- Responsive and user-friendly design

## Getting Started

### Prerequisites

Before you begin, ensure you have the following installed:

- Python (version 3.6 or higher)
- Django (version 3.2 or higher)
- Git

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/irsha-irz/talent-hub.git
   ```

2. Create a virtual environment (recommended) if not created already:

   ```bash
   virtualenv venv
   ```

   or
   python -m venv venv

3. Activate the virtual environment:

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS and Linux:

     ```bash
     source venv/bin/activate
     ```

4. Install the project dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Navigate to the project directory:

   ```bash
   cd social-media
   ```
   
6. Perform database migrations:

   ```bash
   python manage.py migrate
   ```

7. Create a superuser account for administrative access:

   ```bash
   python manage.py createsuperuser
   ```

8. Run the development server:

   ```bash
   python manage.py runserver
   ```

9. Access the application in your web browser at `http://127.0.0.1:8000/`.

## Usage

- Register a new account or log in with an existing account.
- Customize your profile by adding a profile picture and bio.
- Search for other users.
- Create and delete your own posts.
- Like on posts from friends.
- Follow to a user & see its post on home feed
- unfollow to a user
- Explore the news feed to see posts from friends.
- Log out when you're done using the platform.

## Contributing

Contributions to this project are welcome! To contribute, follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix: `git checkout -b feature-name`.
3. Make your changes and commit them: `git commit -m "Add feature"`.
4. Push to the branch: `git push origin feature-name`.
5. Open a pull request describing your changes.

🚀
