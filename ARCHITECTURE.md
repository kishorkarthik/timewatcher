# Architecture

This document describes the architecture and design principles behind TimeWatcher.

The goal is to keep the project **modular**, **maintainable**, and **easy to extend** as it grows.

---

# Repository Structure

```
timewatcher/
│
├── apps/
│   └── cli/          # Command-line interface
│
├── packages/
│   ├── core/         # Business logic
│   ├── database/     # Data persistence
│   └── shared/       # Shared utilities
│
└── docs/
```

Each package has a single, well-defined responsibility.

---

# High-Level Architecture

```
User
 │
 ▼
CLI
 │
 ▼
Core
 │
 ▼
Database
```

The responsibility of each layer is simple:

* **CLI** receives commands from the user.
* **Core** decides what should happen.
* **Database** stores and retrieves data.

Each layer should focus only on its own responsibility.

---

# Components

## CLI (`apps/cli`)

The CLI is responsible for interacting with the user.

Responsibilities:

* Parse commands
* Validate input
* Display output
* Call the core package

The CLI should **not** contain business logic.

Example:

```text
timewatcher start "Build README"
```

The CLI should translate this command into a request for the core instead of implementing session logic itself.

---

## Core (`packages/core`)

The core package contains the business logic of TimeWatcher.

Examples:

* Session
* Task
* Timer
* SessionManager

Responsibilities:

* Manage work sessions
* Apply business rules
* Coordinate application behavior

The core should remain independent of the CLI and database.

This allows future interfaces—such as a desktop application or web API—to reuse the same business logic.

---

## Database (`packages/database`)

The database package is responsible for persistence.

Initial implementation:

* SQLite

Responsibilities:

* Store sessions
* Retrieve historical data
* Manage persistence

The database should not contain business rules. Its job is simply to save and retrieve data.

---

## Shared (`packages/shared`)

The shared package contains reusable components used across multiple packages.

Examples:

* Configuration
* Shared types
* Utility functions

Only place code here when it is genuinely shared.

---

# Dependency Rules

Dependencies should always flow in one direction.

```text
CLI
 │
 ▼
Core
 │
 ▼
Database
```

Good:

* CLI → Core
* Core → Database

Avoid:

* Database → Core
* Core → CLI

Keeping dependencies one-way makes the codebase easier to understand, test, and maintain.

---

# Design Principles

TimeWatcher follows these software engineering principles:

* **Single Responsibility Principle (SRP)** — Each package should have a single responsibility.
* **Separation of Concerns (SoC)** — Keep the CLI, business logic, and persistence separate.
* **Dependency Inversion Principle (DIP)** — The core should remain independent of interfaces and storage implementations.
* **Don't Repeat Yourself (DRY)** — Reuse shared code instead of duplicating logic.
* **Keep It Simple, Stupid (KISS)** — Prefer simple solutions over unnecessary complexity.


# Future Direction

The current implementation starts with a CLI and local database, but the architecture is designed to support additional interfaces in the future.