
# 🌱 LinkPlant

**LinkPlant** is a Django-based web application that allows users to create a personalized **Linktree-style** profile. It enables users to manage and share multiple links through a single, customizable profile page.

![LinkPlant Home](./screenshots/Screenshot%20(7).png)

## 🚀 Features

- 🌐 **Public Profile Page** – Share a single link to display all your social or personal links.
- ➕ **Add/Edit/Delete Links** – Easily manage links via the dashboard.
- 🎨 **Responsive UI** – Clean design with dark mode support based on system preferences.
- 📱 **Mobile Friendly** – Fully responsive design works on all screen sizes.
- 🌱 **"Made with LinkPlant"** badge for public branding.

![Public Profile](./screenshots/Screenshot%20(8).png)
![Link Management](./screenshots/Screenshot%20(9).png)

## 🔧 Tech Stack

- **Framework:** Django (Python)
- **Frontend:** HTML, CSS,  Tailwind CSS 
- **Database:** SQLite (default Django DB)
- **Hosting:** [Replit](https://replit.com)

## 🛠️ How to Run Locally

1. **Clone the repo:**
   ```bash
   git clone https://github.com/your-username/linkplant.git
   cd linkplant
   ```

2. **Create a virtual environment and activate it:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Start the server:**
   ```bash
   python manage.py runserver
   ```

6. **Open your browser and visit:**
   ```
   http://127.0.0.1:8000/
   ```


## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you'd like to change.

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
