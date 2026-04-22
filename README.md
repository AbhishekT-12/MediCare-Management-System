# Medicare HMS

Medicare HMS is a Django-based hospital management system for patient registration, doctor browsing, appointment booking, lab test management, discharge summaries, and final bill generation.

## Features

- User registration, login, profile, and profile update
- Doctor listing and treatment listing
- Appointment booking with fixed consultation charge
- Lab technician dashboard
- Hospital test catalog with add test page
- Patient test referral and result tracking
- Discharge summary form
- Final bill generation with room charges, food charges, medicine charges, and A4 print layout

## Tech Stack

- Python
- Django
- SQLite for local development
- Bootstrap 5
- Crispy Forms
- django-recaptcha

## Setup

1. Create and activate a virtual environment.

```powershell
python -m venv .venv
.venv\Scripts\activate
```

2. Install dependencies.

```powershell
pip install -r requirements.txt
```

3. Create an environment file.

```powershell
copy .env.example .env
```

Update `.env` with your real values.

4. Run migrations.

```powershell
python manage.py migrate
```

5. Create a superuser.

```powershell
python manage.py createsuperuser
```

6. Start the server.

```powershell
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

## Important URLs

- Home: `/home`
- Doctors: `/doctors/`
- Treatments: `/doctors/treatments`
- Appointment booking: `/doctors/book/`
- Lab dashboard: `/labreport/dashboard/`
- All tests: `/labreport/all-tests/`
- Add hospital test: `/labreport/add-hospital-test/`
- Discharge: `/discharge/`

## Billing Rules

Final bill calculation includes:

- Bed charge
- Nursing charge
- Doctor visit charge
- Miscellaneous charge
- Food charge, if selected, at Rs. 480 per day
- Medicine charge based on room type

The final bill page includes a print button and A4-friendly print styling.

## Notes

- `db.sqlite3`, uploaded media, cache files, and local environment files are intentionally ignored by Git.
- Add sample doctors, treatments, lab tests, and users through Django admin after setup.
