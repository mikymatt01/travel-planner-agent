# Travel Planner

The **Travel Planner** project is a hands-on implementation designed to explore how to use **CrewAI** in a real-world environment.

It consists of two main components:

* A **server** (backend) built with **Python** and **FastAPI**, responsible for handling APIs and agent execution.
* A **web application** (frontend) built with **React**, which provides a simple UI for displaying results.

Communication between the server and the webapp is handled via **WebSockets**, enabling real-time updates on the execution status of the agents.

---

## Project Structure

### Travel Planner App (Frontend)

The main frontend code lives in the `src` directory, which includes:

* **`hook/`**

  * Contains `webSocketContext.tsx`, a context provider with all the logic required for WebSocket communication with the backend.

* **`ui/`**

  * Contains reusable UI components such as buttons, cards, chatbot, and input fields.

---

### Travel Planner Service (Backend)

The backend service is organized into:

* **`config/`**

  * Includes `config.py`, which manages environment variable imports.

* **`src/`**

  * The main directory containing all API implementations.

* **`utils/`**

  * Includes `db.py`, which handles dataset imports and defines MongoDB collections.
