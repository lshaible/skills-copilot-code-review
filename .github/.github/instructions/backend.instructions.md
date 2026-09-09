---
applyTo: "backend/**/*,*.py"
---

## Backend Guidelines

- All API endpoints must be defined in the `routers` folder.
- Load example database content from the `database.py` file.
- Log detailed errors on the server, but return sanitized HTTP status codes and user-safe messages to the frontend.
- Ensure all APIs are explained in the documentation.
- Verify changes in the backend are reflected in the frontend (`src/static/**`). If possible breaking changes are found, mention them to the developer.