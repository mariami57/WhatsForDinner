# Whats for Dinner
"What’s for Dinner?" is a playful recipe-sharing web app built with Django that helps users answer life’s most important question: “What’s for dinner?”
Browse, share, and discover delicious dishes — from quick weekday fixes to indulgent weekend meals.

## Features
🧑‍🍳 Recipe Management - Add, edit, and browse tasty recipes with images and ingredients.

👤 Profiles – User profile pages with profile pictures and info. A profile is automatically created via a signal triggered when a new user registers. New users also receive a welcoming email through the signal.

🔑 Authentication – User registration, login/logout, and secure ownership checks for edits/deletes. Extended Django AbstractBaseUser in order to add custom functionalities.

📬 Contact Form — Easy way for users to get in touch (powered by [Formspree](https://formspree.io/)).

💌 Subscription Form - Users can opt in to subscribe to the website`s newsletter. When subscribed, users receive a welcoming email. Newsletters are sent through [MailJet](https://www.mailjet.com/).

🖼️ Image Support – The users can add a picture for each of the recipes, if they would like to do so. Static files are stored in [Cloudinary](https://cloudinary.com/).


## Tech Stack
- Backend: Django (Python)
- Frontend: HTML, CSS, JavaScript (vanilla, fetch API for AJAX)
- Database: PostgreSQL
- Authentication: Django built-in auth system
- Email/Contact: [Formspree](https://formspree.io/), [MailJet](https://www.mailjet.com/)
- Static Files: [Cloudinary](https://cloudinary.com/)

## Installation
### 1. Clone the repository:
<pre>
  git clone https://github.com/mariami57/WhatsForDinner.git
  cd weather-dashboard
</pre>

### 2. Create a virtual environment and activate it:
<pre>
  python -m venv venv
  source venv/bin/activate   # On Windows: venv\Scripts\activate
</pre>

### 3. Install dependencies:
<pre>
  pip install -r requirements.txt
</pre>

### 4. Run migrations:
<pre>
  python manage.py migrate
</pre>

### 5. Run the development server:
<pre>
  python manage.py runserver
</pre>

### 6. Open in browser:
<pre>
  http://127.0.0.1:8000/
</pre>

## Deployment
This app is deployed on Azure.
Here’s an overview of the deployment setup:

○ Database in Production:  PostgreSQL/MySQL

○ Static & Media Files: Handled by [Cloudinary](https://cloudinary.com/)


○ Environment Variables:
<br>
This project uses a .env file to manage secrets and environment configuration.
A template.env file is included in the repository – you can copy it and rename it to .env before running the project


## Live Demo
Check out the live version here:
[What`s for Dinner?](https://whats-for-dinner-eygba6hfb8b3bag4.italynorth-01.azurewebsites.net/)

