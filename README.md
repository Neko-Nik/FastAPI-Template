# FastAPI Template

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/Neko-Nik/FastAPI-Template/blob/master/LICENSE)
[![GitHub Issues](https://img.shields.io/github/issues/Neko-Nik/fastapi-template.svg)](https://github.com/Neko-Nik/FastAPI-Template/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/Neko-Nik/fastapi-template.svg)](https://github.com/Neko-Nik/FastAPI-Template/pulls)

## Description

FastAPI Template is a project template that provides a good file structure and setup for building FastAPI applications. It includes a pre-configured development environment, production-ready deployment scripts, and SSL configuration options. This template aims to make it easier for developers to start new FastAPI projects with a robust foundation and best practices in mind.

## Features

- Clean file structure for organizing your FastAPI application
- Virtual environment setup for isolated dependencies
- Production-ready bash scripts for deployment
- Configurable SSL setup for secure connections
- Pre-configured logging with logs saved to a file
- Web UI for viewing and searching logs with many options


## Installation

1. Clone the repository:

```bash
git clone https://github.com/Neko-Nik/FastAPI-Template.git
cd FastAPI-Template
```

2. Create a virtual environment and activate it:

```bash
python3 -m venv virtualenv
source virtualenv/bin/activate
```

3. Install the required dependencies:

```bash
pip3 install -r requirements.txt
```

## Usage

To run the application locally, use the following command:

```bash
python3 app.py
```

The application will start running on `http://localhost:8000`.

## Deployment

For production deployment, the template provides bash scripts for running the application with Gunicorn, serving it over HTTPS, and more. Customize these scripts according to your specific deployment needs.

Note: Change the following `workers, threads, timeout, keyfile, certfile` according to your needs.

To start the application in production mode, use the following command:

```bash
bash scripts/start_api.sh
```

To Restart the application in production mode, use the following command:

```bash
bash scripts/restart_api.sh
```

## Contributing

Contributions are welcome! If you'd like to contribute to FastAPI Template, please follow these steps:

1. Fork the repository
2. Create a new branch for your feature or bug fix
3. Make your changes and commit them
4. Push your changes to your fork
5. Submit a pull request to the `main` branch of the original repository

Please make sure to follow the existing code style and add tests for any new features or bug fixes.

## License

FastAPI Template is released under the [MIT License](https://github.com/Neko-Nik/FastAPI-Template/blob/main/LICENSE). You are free to use, modify, and distribute this template for any purpose.
