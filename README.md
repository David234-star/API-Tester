# ⚡ Neon API Tester

![GitHub release (latest by date)](https://img.shields.io/github/v/release/David234-star/API-Tester?style=for-the-badge)
![GitHub License](https://img.shields.io/github/license/David234-star/API-Tester?style=for-the-badge)
![Python Version](https://img.shields.io/badge/python-3.9+-blue.svg?style=for-the-badge)

A lightweight, offline-capable API testing tool for Windows, designed with a retro-futuristic aesthetic blending 80s neon with modern glassmorphism.

![App Screenshot](assets\images\Screenshot.png)

---

## Features

- **Full CRUD Support:** Send `GET`, `POST`, `PUT`, `DELETE`, and `PATCH` requests.
- **Customizable Requests:** Easily add URL parameters, headers, and a JSON body.
- **Detailed Responses:** View the status code, response time, and a syntax-highlighted JSON response body.
- **Request History:** Automatically saves a history of your requests, allowing you to re-run them with a single click.
- **Retro-Futuristic UI:** A unique interface with neon, glassmorphism, and custom retro fonts.
- **Light & Dark Themes:** Toggle between a dark neon theme and a retro-inspired light theme.
- **Standalone & Offline:** No accounts, no cloud sync. Everything is local.
- **Export Responses:** Save API responses to a `.json` or `.txt` file.

## Tech Stack

- **GUI Framework:** [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)
- **HTTP Requests:** [Requests](https://requests.readthedocs.io/en/latest/)
- **Packaging:** [PyInstaller](https://www.pyinstaller.org/)
- **UI Design Assets:** [Pillow](https://python-pillow.org/)
- **Syntax Highlighting:** [Pygments](https://pygments.org/)

---

## Installation & Usage

There are two ways to use Neon API Tester.

### 1. For End-Users (Recommended)

Simply download the latest standalone executable. No installation needed!

1.  Go to the [**Releases Page**](https://github.com/David234-star/API-Tester/releases).
2.  Under the latest release, download the `NeonAPITester.zip` file.
3.  Unzip the file and run `NeonAPITester.exe`.

### 2. For Developers (Running from Source)

If you want to run the application from the source code:

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/David234-star/API-Tester.git
    cd API-Tester
    ```

2.  **Create and activate a virtual environment:**

    ```bash
    # Create the environment
    python -m venv API-venv

    # Activate it (Windows-CMD)
    API-venv\Scripts\activate

    # Activate it (macOS/Linux)
    source API-venv/bin/activate
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the application:**
    ```bash
    python main.py
    ```

---

## Building from Source

To create your own standalone `.exe` file from the source code, make sure you have PyInstaller installed (`pip install pyinstaller`) and run the following command from the project root:

```bash
pyinstaller --noconfirm --onefile --windowed --name "NeonAPITester" --add-data "assets;assets" main.py
```
