# 📧 Python Email API

A lightweight, production-ready email-sending API built with **FastAPI**. This API enables you to easily send emails using simple HTTP requests. It’s designed for seamless integration in Python, Dart, or any application that supports HTTP.

---

## 🚀 Features

- Built with **FastAPI** – fast, modern, and lightweight.
- Easy to use and integrate into any project.
- Supports default email credentials or custom sender configurations.
- Supports email subject, title, and body customization.
- Compatible with both Python and Dart clients.

---

## 📦 Installation

Clone the repository and install required dependencies:

```bash
git clone https://github.com/yourusername/pythonemailapi.git
cd pythonemailapi
pip install -r requirements.txt
```

---

## ▶️ Running the Server

To start the FastAPI server locally:

```bash
python main.py
```

Once running, the API will be available at: `http://0.0.0.0:8000`

---

## 🧪 Usage Examples

### ✅ Health Check

```python
import requests

response = requests.get('http://0.0.0.0:8000')
print(response.json())
```

### 📤 Send Email (Minimal Example)

```python
import requests

response = requests.post('http://0.0.0.0:8000/sendEmail', json={
    "toEmail": "toemail@gmail.com"
})
print(response.json())
```

### 📤 Send Email (With Custom Credentials)

```python
import requests

response = requests.post('http://0.0.0.0:8000/sendEmail', json={
    "fromEmail": "fromemail@gmail.com",
    "passkey": "your-16-digit-app-password",
    "toEmail": "toemail@gmail.com",
    "title": "Your Title",
    "subject": "Your Subject",
    "body": "Your body message"
})
print(response.json())
```

> 💡 If `fromEmail` and `passkey` are not provided, the API will use default credentials.

---

## 🔑 Generate App Password (Gmail)

If you're using Gmail, enable 2-Step Verification and generate an app-specific password to use as the `passkey`.

👉 [Generate App Password →](https://support.google.com/accounts/answer/185833?hl=en)

---

## 🧰 Default Credentials

Used if `fromEmail` and `passkey` are omitted from the request:

```json
{
  "fromEmail": "defaultemailapi@gmail.com",
  "passkey": "your-16-digit-app-password"
}
```

---

## 📜 JSON Payload Structure

```json
{
  "fromEmail": "fromemail@gmail.com",
  "passkey": "16-digit-app-password",
  "toEmail": "toemail@gmail.com",
  "title": "Email Title",
  "subject": "Email Subject",
  "body": "Email Body Content"
}
```

---

## 🔗 Packages & Integrations

- [Dart Package (email_sender)](https://pub.dev/packages/email_sender)

---

## 👤 Author

**Shaik Afrid**  
GitHub: [@afriddev](https://github.com/afriddev)

---

## 🛡️ License

This project is licensed under the MIT License – feel free to use and contribute.
