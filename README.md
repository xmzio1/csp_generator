# CSP Auto Generator

**CSP Auto Generator** is a professional Python tool that automatically generates **Content Security Policies (CSP)** for websites. CSP is a powerful web security feature that helps prevent **XSS attacks, data injection, and other content-based vulnerabilities**.

> ⚠️ **Important:** Use this tool **only** on websites you own or have explicit permission to test.

---

## 🚀 Features

- Automatic analysis of any website URL.
- Detects **all types of resources**:
  - **Scripts** (`script-src`) including inline scripts.
  - **Styles** (`style-src`) including inline styles.
  - **Images** (`img-src`), **fonts** (`font-src`), **iframes** (`frame-src`).
  - **AJAX/WebSocket** domains (`connect-src`) – for future enhancement.
- Generates **secure CSP** with **SHA256 hashes** for inline scripts and styles.
- Provides **detailed JSON reports** in the `reports/` folder.
- Configurable CSP policy type: **strict**, **moderate**, or **flexible**.
- CLI support for quick and easy usage.

---

## 📦 Project Structure
-csp_generator/
-├── csp_generator.py # Main Python program.
-├── utils.py # Helper functions for resource extraction & CSP generation.
-├── config.json # Configuration for policy options.
-├── requirements.txt # Required Python libraries.
-├── README.md # Project documentation (this file).
-└── reports/ # Folder to save CSP reports.


---

## ⚡ Installation

1. **Clone or download** this repository.
2. Make sure you have **Python 3.11+** installed.
3. Install required Python libraries:

```bash
pip install -r requirements.txt
```
---

## 🛠 Usage

Run the tool from the command line:
```
python csp_generator.py <website_url>
```

Example:
```
python csp_generator.py https://example.com
```
What happens next:

-The tool fetches and analyzes all website resources.

-Generates a CSP policy, including SHA256 hashes for inline scripts/styles.

-Saves a detailed JSON report in reports/example.com.json.

-Prints the CSP policy to the console, ready to use in HTTP headers or <meta> tags.
