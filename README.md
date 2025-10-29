# Travel Planner — Agent-based Travel Assistant

A small multi-component project that demonstrates an agent-driven travel planning system. The repo contains a React TypeScript front-end application (`travel_planner_app`) and a Python service component (`travel_planner_svc`) which implement UI, agents, tools and simple data storage for flights, hotels and travel-related features.

This README documents the repository layout, quick start instructions for development, testing information, and notes for contributors.

## Features
The capabilities of the chatbot are:

- Flight search
- Hotel recommendations
- Travel planning
- Integrated mock payments

## What this project contains

- `travel_planner_app/` — React + TypeScript front-end app (UI, WebSocket hook, SDK and small components). Built artifacts live in `travel_planner_app/build/`.
- `travel_planner_svc/` — Python-based backend/service containing agent implementations, tools, plugins, simple data files and utilities.
- Top-level helper scripts: `dev.sh`, `run.sh` (in the `travel_planner_svc` folder) and environment files `.env`, `.env.dev`.

## High-level overview

The project is split into two main parts:

- Front-end (`travel_planner_app`): a React app (TypeScript) that provides the user-facing interface and a WebSocket context to interact with the backend in real time.
- Service (`travel_planner_svc`): the backend containing agents, tools and plugins used to process travel search and planning tasks. It ships sample JSON data under `src/utils` and `output/` and includes helper scripts to run the service.

## Repository layout (important files/folders)

- `travel_planner_app/`
  - `package.json`, `tsconfig.json` — project config
  - `src/` — React source code (components in `ui/`, a `hook/webSocketContext.tsx`, an SDK helper in `sdk/`)
  - `build/` — production build output (generated)

- `travel_planner_svc/`
  - `pyproject.toml` — Python project config (dependency management)
  - `server.py` — service entrypoint (start/serve the backend)
  - `run.sh`, `dev.sh` — convenience scripts for running the service
  - `src/agents/` — agent implementations (chatbot, travel planner)
  - `src/plugins/` — plugin modules for flights, hotels, chat
  - `src/utils/` — helper utilities and sample JSON files (`flights.json`, `hotels.json`)
  - `output/` — output data snapshots

## Prerequisites

- Node.js (recommended v16+ or a version compatible with the project). Yarn or npm is fine.
- Python 3.10+ (project uses `pyproject.toml`; a modern Python and a tool like Poetry or a venv is recommended).

## Quick start — Frontend (development)

1. Open a terminal and go to the front-end folder:

	cd travel_planner_app

2. Install dependencies and run dev server:

	npm install
	npm start

3. The dev server will start (by default on http://localhost:3000 unless configured otherwise). The front-end expects the backend to be reachable via the WebSocket/API URL defined in its environment or code (see `travel_planner_app/src/hook/webSocketContext.tsx` and `travel_planner_app/src/sdk/index.ts`).

4. To create a production build:

	npm run build

The `build/` directory already contains an example production build included in this repo.

## Quick start — Backend / Service (development)

This service uses a modern Python project layout. There are two common ways to run it depending on your preferred Python workflow.

Using uv (recommended if you have it):

1. Change to the service folder:

	cd travel_planner_svc

2. Install dependencies and run:

	install uv: `curl -LsSf https://astral.sh/uv/install.sh | sh`

	install the dependencies: `uv sync --locked`
	
3. Run the service:

	`uv run fastapi dev server.py --port 4000`


Alternatively, you can run the included convenience script (make sure it is executable):

	./run.sh or ./dev.sh

Environment files: two env templates exist `.env` and `.env.dev`. Edit them to configure ports, hostnames and API/WebSocket endpoints as needed. The front-end and back-end must agree on the WebSocket/API addresses for real-time features to function properly.

## Running both locally

1. Start the backend (see above).
2. Start the front-end (`npm start`) and ensure the front-end WebSocket/HTTP target points to the backend (edit environment or `travel_planner_app/src/sdk/index.ts` / `webSocketContext.tsx` to match).

When both are running, you can interact with the UI and the agents will use the tools and sample data in `travel_planner_svc/src`.

## Notes for developers

- Agents and tools: `travel_planner_svc/src/agents` contains agent code and tool implementations. The `plugins` folder contains pydantic models and simple repository code for flights and hotels.
- Sample data: `travel_planner_svc/src/utils/flights.json` and `hotels.json` provide example datasets useful for development.
- WebSockets: The front-end uses a WebSocket context (`webSocketContext.tsx`) for real-time interactions. The service includes helper utilities such as `socket_sender.py`.

## Common tasks

- Update front-end dependencies: `cd travel_planner_app && npm install <pkg>`
- Run a production build of the front-end: `cd travel_planner_app && npm run build`
- Start backend in dev mode: `cd travel_planner_svc && ./dev.sh`

## Troubleshooting

- If the front-end cannot connect to the backend, verify the WebSocket URL and that the backend is running on the expected host/port. Check `.env` files and `webSocketContext.tsx`.
- If Python dependencies are missing, ensure you installed them via Poetry or pip in an activated virtual environment.

## Contributing

If you'd like to contribute:

1. Open an issue to discuss larger changes.
2. Create a branch for your work.
3. Add tests for new features or bug fixes where appropriate.

## License

This repository includes a `LICENSE` file at the repository root. See `LICENSE` for the full license text and terms.

---

If you'd like, I can also:

- Run the front-end build or start the front-end and backend locally and verify they connect.
- Add a small troubleshooting checklist or docker-compose for a one-command local start.

Tell me which of these you'd like next.
