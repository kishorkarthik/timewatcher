# TimeWatcher

> Keep your hands on the keyboard—log your active work hours via the CLI.

TimeWatcher is a CLI-first time tracking application built for developers. It helps you track focused work sessions without leaving the terminal, making time tracking a natural part of your development workflow.

## Why Time Tracking?

Software development is a craft where progress is often invisible. Hours can disappear into debugging, learning, research, meetings, and deep work without a clear understanding of where the time went.

Time tracking is not about measuring every minute or turning work into a spreadsheet. It is about building awareness.

By making time tracking part of the developer workflow, TimeWatcher helps you understand your work patterns, reflect on progress, and make better decisions about where your time goes.

## Features

### CLI-first workflow

Manage your work sessions directly from the terminal.

```bash
timewatcher start "Implement authentication"

timewatcher status

timewatcher stop

timewatcher history
```

### Session-based tracking

Organize work around focused sessions. Each session records what you are working on and helps build a clearer picture of your time.

### Local-first storage

Your data stays on your machine. TimeWatcher uses local SQLite persistence to provide a reliable workflow without requiring external services.

### Developer-focused experience

Built with developers in mind, TimeWatcher prioritizes speed, simplicity, and minimal interruption.

## Installation

Clone the repository:

```bash
git clone https://github.com/kishorkarthik/timewatcher.git
cd timewatcher
```

Install dependencies:

```bash
uv sync
```

Run TimeWatcher:

```bash
uv run timewatcher --help
```

## Current Commands

### Start a session

```bash
timewatcher start "Working on API design"
```

### Check active session

```bash
timewatcher status
```

### Stop current session

```bash
timewatcher stop
```

### View completed sessions

```bash
timewatcher history
```

## Roadmap

TimeWatcher is being developed as a reliable, keyboard-first time tracking tool for developers.

### v0.1.0 — Foundation ✅

* [x] Establish project architecture
* [x] Bootstrap CLI application
* [x] Build session-based tracking
* [x] Implement local SQLite persistence
* [x] Add core time tracking commands
  * [x] Start session
  * [x] Stop session
  * [x] View active status
  * [x] View session history
* [x] Add automated test coverage
* [x] Add documentation

### Future

* Task switching
* Improved insights and reporting
* Richer session analytics
* Additional ways to interact with TimeWatcher
* Synchronization and collaboration features

## Contributing

Contributions are welcome.

For substantial changes, open an issue first to discuss the proposed direction before submitting a pull request.

## License

TimeWatcher is licensed under the MIT [License](LICENSE).
