<!-- prettier-ignore -->
<div align="center">

<img src="static/img/avatar.png" alt="elxecutor avatar" align="center" height="96" />

# geekspe
*minimal django portfolio landing page with interactive particles*

[![License](https://img.shields.io/badge/License-Apache%202.0-blue?style=flat-square)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.14-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![Django](https://img.shields.io/badge/Django-6.0.3-092E20?style=flat-square&logo=django&logoColor=white)](https://djangoproj.com)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-4.3.1-7952B3?style=flat-square&logo=bootstrap&logoColor=white)](https://getbootstrap.com)

[Overview](#overview) • [Features](#features) • [Getting Started](#getting-started) • [Deployment](#deployment) • [Contributing](#contributing) • [License](#license)

</div>

A personal portfolio site for [elxecutor](https://github.com/elxecutor), an EEE student at OAU. Built with Django and featuring an interactive particle animation background.

> [!NOTE]
> Live at [geekspe.pythonanywhere.com](https://geekspe.pythonanywhere.com)

## Overview

This is a single-page portfolio website that showcases profile information and social links. The page features a dark-themed design with an interactive particle animation background powered by [particles.js](https://github.com/VincentGarreau/particles.js). All third-party assets (Bootstrap, jQuery, Font Awesome, Google Fonts, particles.js) are vendored locally rather than loaded from CDNs.

## Features

- **Interactive Particle Background** — Animated particle system with hover-to-connect interaction
- **Responsive Design** — Mobile-friendly layout with breakpoints at 765px and 785px
- **Local Assets** — All CDN dependencies served locally for reliability
- **Django Admin** — Standard admin interface available at `/admin/`
- **Environment-based Config** — `.env` file support for secrets and settings
- **PDF Resume** — Embedded resume download via `static/pdf/Profile.pdf`

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Django 6.0.3 (Python 3.14) |
| WSGI Server | Gunicorn 23.0.0 |
| Frontend | Bootstrap 4.3.1, jQuery 3.3.1 |
| Icons | Font Awesome 6.5.2 |
| Fonts | Google Fonts (Righteous, Ubuntu Mono) |
| Animation | particles.js 2.0.0 |
| Database | SQLite 3 |
| Deployment | PythonAnywhere |

## Getting started

### Prerequisites

- [Python 3.14+](https://www.python.org/downloads/)
- [Git](https://git-scm.com/downloads)

### Setup

1. Clone the repository:

```bash
git clone https://github.com/elxecutor/geekspe.git
cd geekspe
```

2. Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Configure environment variables:

```bash
cp .env.example .env
# Edit .env with your SECRET_KEY and settings
```

5. Run migrations and start the development server:

```bash
python manage.py migrate
python manage.py runserver
```

6. Open `http://127.0.0.1:8000` in your browser.

> [!TIP]
> To access the admin panel, create a superuser: `python manage.py createsuperuser`

## Deployment

This project is deployed on [PythonAnywhere](https://www.pythonanywhere.com/). To deploy:

1. Clone the repository on PythonAnywhere
2. Set up a virtual environment and install dependencies
3. Configure environment variables in your WSGI file
4. Set the working directory and virtualenv path in the web app config
5. Collect static files: `python manage.py collectstatic`

> [!WARNING]
> Ensure `DEBUG=False` and set proper `ALLOWED_HOSTS` in production.

## Contributing

Contributions are welcome. Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

This project is licensed under the Apache License 2.0 — see [LICENSE](LICENSE) for details.
