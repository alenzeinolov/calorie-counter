# calorie-counter
API for calorie counter

## Setup
Need to create a `config.json` in project root directory and fill `SECRET_KEY` key/value, it is the only requirement so far.

## Endpoints:
- `/api/accounts/register/` - register into the system (POST)
- `/api/accounts/info/` - info about user (GET)
- `/api/accounts/set_goal/` - set daily calorie goal (PUT/PATCH)
- `/api/counter/records/` - get list of records or create a new one (GET/POST)
    - Filters: `date_after`, `date_before`, `user`
- `/api/counter/records/<record_id>/` - retrieve record or update it (GET/PUT/PATCH)
- `/api/reports/records/` - retrieve statistical about calories (total, average, maximum)
    - Filters: `date_after`. `date_before`, `user`
- `/api/reports/users/` - retrieve number of users who have exceeded the daily calorie goal in a given day
    - Filters: `date`
    
## Authentication
Basic Authentication using username and password
