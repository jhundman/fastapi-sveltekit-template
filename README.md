# fastapi-sveltekit-template
The goal of this template is to combine a basic fastapi, pydantic, sqlite backend with a sveltekit
frontend for shipping fullstack web apps. It is a very basic todo list but

## Stack

#### Backend
- ⚡️ Fastapi for API
- 🦺 Pydantic for data validation / type safety
- ⏳ SQLite / APSW for simple, cheap, reliable, non-ORM, database experience
  - [ ] TODO: SQLite backups to bucket (R2?)
  - [ ] TODO: Authentication


#### Frontend
- 🚄 Sveltekit for a fast, compiled, reactive frontend
- 🧩 Shadcn-Svelte for UI Components


## Deploy
- Plan on setting up deploy to Cloudflare pages (frontend) and Fly.io (backend)
