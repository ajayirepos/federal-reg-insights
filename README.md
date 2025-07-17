# Federal Reg Insights

A take-home assessment project for the U.S. Digital Service (USDS), focused on analyzing U.S. federal regulations using the [eCFR](https://www.ecfr.gov/) API. The application downloads regulatory data, calculates key metrics, and presents insights through a user-friendly interface.

---

## Features

- Fetches and stores eCFR data server-side
- Calculates and displays key metrics:
  - Word count
  - Checksum (MD5 hash)
  - Historical change detection
  - Custom metric: Top 10 most frequent keywords
- REST API for programmatic access
- Frontend interface for selecting and visualizing titles & sections
- SQLite-backed storage for offline and historical reference

---

## Tech Stack

- Backend: Python, Flask
- Frontend: HTML, CSS (Bootstrap)
- Database: SQLite
- Tools: Requests, hashlib, BeautifulSoup, matplotlib

---

## UI Preview

[Screenshot]

---

## Project Structure

```bash
federal-reg-insights/
├── app.py                  # Flask backend
├── ecfr_api.py             # API download and parsing logic
├── metrics.py              # Metrics calculation module
├── static/                 # CSS & JS
├── templates/              # HTML templates
├── data/                   # Downloaded eCFR JSON and DB files
├── screenshots/            # UI screenshots
└── README.md
