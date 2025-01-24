# E2Helper

E2Helper is a simple command-line tool designed to assist users with their E2 tasks. It provides a menu-driven interface to perform various operations.

## Features

- **Menu Navigation**: Navigate through different states like Test, Setup, About, and Quit.
- **Setup State**: Configure and save settings like token, cookie, and profile URL.
- **About State**: Learn more about the tool and its creator.

## Prerequisites

- Python 3.x
- `curses` library (usually included with Python on Unix-based systems)

## Installation

1. Clone the repository:
    ```sh
    git clone <repository-url>
    cd E2Helper
    ```

## Usage

1. Run the main script:
    ```
    python main.py
    ```

2. Use the arrow keys to navigate through the menu and press Enter to select an option.

## Project Structure

- [main.py](http://_vscodecontentref_/0): The main entry point of the application.
- [resources](http://_vscodecontentref_/1): Directory containing resource files like [banner.txt](http://_vscodecontentref_/2) and [storage.txt](http://_vscodecontentref_/3).
- [states](http://_vscodecontentref_/4): Directory containing different state classes and utilities.
- [setup_project.sh](http://_vscodecontentref_/5): Script to set up the project structure.
