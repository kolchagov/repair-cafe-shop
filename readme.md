# Repair cafe shop - Neighborhood Repair Café Log

Coffee lovers, think green: don't throw away what can be repaired.

## Concept

A small community repair café app for cataloguing items brought in for repair,
assigning volunteer repairers, and tracking each repair ticket.
It needs no user accounts: owners and repairers are represented as ordinary domain data.

## Tech stack

- Python 3.12+, Django 6.1 (see `requirements.txt`: `Django`, `Pillow`)
- SQLite (default, `db.sqlite3`), no external services
- Bootstrap 5 (local static files), Django Template Engine

## It is composed of three apps and several _models_:

1. catalog - handles received coffee machines by category and item

- `Category`: unique name and description; `__str__`
- `Item`: owner name, category (`ForeignKey`), brand, problem description,
  optional photo URL.

2. `volunteers` - handles voluntary repair technicians

- `Repairer`: name, skill choice, phone, optional email, and optional notes.

3. `repairs`

- `RepairTicket`: unique generated code, item (`ForeignKey`), serial number,
  status choices (`received`, `in_progress`, `fixed`, `unfixable`),
  intake date, diagnosis, non-negative cost estimate,
  and repairers (`ManyToManyField`).

## Setup and configuration

```shell
git clone https://github.com/kolchagov/repair-cafe-shop.git
cd repair-cafe-shop
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
````

Open http://127.0.0.1:8000/. No custom migrations, no admin panel needed.
Works with an empty database — every object is created through the UI.
`catalog/fixtures/sample_data.json` is optional local sample data and is never
loaded automatically; you can delete it safely.

## Environment variables and credentials

- None required for local evaluation.
- SECRET_KEY and DEBUG=True ship with safe dev defaults in repair_cafe_shop/settings.py
- Database: SQLite file db.sqlite3 is created on migrate.
- Uploads: MEDIA_URL=/media/, MEDIA_ROOT=media/ (item photos, optional).
- No login, no passwords, no API keys.

## First run walk-through

1. **Categories**
    - nav: Settings → Categories (/catalog/categories/)
    - Add category (/catalog/categories/add/). Create e.g. "Espresso machines".
      __Needed before items (item requires a category)__.
2. **Items**
    - Dashboard → Add item for repair
    - Fill owner, select category, fill brand, serial number, problem description
    - (≥4 words), optional photo.
    - Saving does two things:
        - Persist the item data, showing the repair code
        - Auto-creates a received ticket in pending state - find it under
          _Repairers only_ → _Pending repair tickets_.
3. **Repairers**
    - To create new volunteer repairer use Settings → Add repairer (/volunteers/add/)
    - There is a full CRUD in Settings → Repairers list
4. **Tickets**
    - To process tickets you have to have Item for repair and at least one repairer
    - Open a ticket details → To repair
    - Assign repairers (Ctrl/Cmd selects multiple),
    - Set diagnosis + spare-parts cost
    - Status should be set from "RECEIVED" to "IN PROGRESS"
    - If repair need some spare parts, this status can prolong until parts delivery
    - Complete the repair by setting status to "FIXED" or "UNFIXABLE"
    - New repair ticket button on any ticket list (/repair/edit)

Every page is reachable from the navbar. Page template consists of the same nav + footer.  
Delete actions always ask for confirmation.  
Dashboard shows basic statisitics and repair efficiency

## Check ticket repair state

Each ticket has its own code (uuid). Customers can check the status of their
repairs using generated code from dashboard.

## Project structure
```
catalog/        Category (list/add/edit/delete), Item (list/detail/add/edit/delete)
volunteers/     Repairer (list/detail-readonly/edit/delete)
repairs/        RepairTicket (lookup, pending/in-progress/finished lists, detail, create/edit)
templates/      index.html (base), navbar.html, footer.html, paginator.html, 404.html, bs5/form.html
repairs/templatetags/  custom `status_badge` filter
repair_cafe_shop/  settings, urls (media serving, dashboard view)
static/         Bootstrap CSS/JS + logo
Models:         Category ←(FK) Item ←(FK) RepairTicket ↔(M2M) Repairer.
Forms (5):      CategoryForm, ItemForm, RepairerForm, RepairTicketForm, TicketSearchForm 
                - custom labels, help texts, placeholders, error messages,
                  disabled read-only detail, code/updated_at excluded.
```

## Custom 404 - Not found page
The app has custom 404 page. To make it active, set `DEBUG=False` in settings.py and
run the server with `--insecure` flag:
```bash
python manage.py runserver --insecure 
```
Without it, Django stops serving static files when DEBUG is off and protocol is http, 
so the page would load unstyled.

