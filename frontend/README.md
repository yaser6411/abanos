# Abanos Frontend (Vite + React)

This folder is a minimal React + Vite frontend scaffold for the Abanos project.

Run locally:

```bash
# from repo root
cd frontend
npm install
npm run dev
```

The demo calls the backend `/db-check` endpoint that exists in the repository.
When the backend implements product endpoints (e.g. `/api/products`) you can update src/components/ProductList.jsx to fetch and display them.
