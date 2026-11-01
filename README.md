# Συντονιστής Πρεσβυτερίου — Render

## Render deployment
1. Create a **private GitHub repository** and upload `index.html` and `server.py` to its root.
2. Render > New > Web Service > Connect repository.
3. Runtime: Python 3; Build command: `echo Ready`; Start command: `python server.py`; instance: choose plan.
4. Deploy and copy the actual `https://...onrender.com` URL.
5. Supabase Dashboard > Authentication > URL Configuration: Site URL = actual Render URL; Redirect URLs add `https://YOUR-ACTUAL-HOST.onrender.com/**`.
6. Supabase Authentication > Users: use the existing account. Check that RLS is enabled for all relevant tables.

## Protecting data
- This release retains the v7 Supabase project configuration and data format. Deployment does not erase existing Supabase records.
- Before migrating, export JSON backup from the currently working app and save it securely. Do NOT import an old JSON backup over existing cloud data without checking it first: the import can overwrite current records.
- Existing local-only records do not automatically move between browser origins; export from the old site, then carefully import if needed.
- Supabase publishable key is public by design, but Supabase RLS policies and Authentication must be correctly configured. Never put a service_role/secret key in the browser.
- Render URL is public. Login screen alone is not a substitute for an external access gateway or audited security controls. Do not store confidential pastoral/personally sensitive notes until access controls, MFA, backup/restore, and data-retention safeguards are reviewed.
- Render free services may sleep when idle; paid plans can reduce this limitation.
