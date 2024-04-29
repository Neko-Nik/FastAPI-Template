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

To run the application locally, using Uvicorn or Gunicorn:

Using Uvicorn: `uvicorn api.main:app --reload --port 8086`

Using Gunicorn: `gunicorn -k uvicorn.workers.UvicornWorker api.main:app`

The application will start running on [http://localhost:8086](http://localhost:8086).

## Deployment

For production deployment, the template provides docker CI pipeline and `docker-compose` configuration files for easy deployment.

## Contributing

Contributions are welcome! If you'd like to contribute to FastAPI Template, please follow these steps:

1. Fork the repository
2. Create a new branch for your feature or bug fix
3. Make your changes and commit them
4. Push your changes to your fork
5. Submit a pull request to the `master` branch of the original repository

Please make sure to follow the existing code style and add tests for any new features or bug fixes.

## License

FastAPI Template is released under the [MIT License](https://github.com/Neko-Nik/FastAPI-Template/blob/main/LICENSE). You are free to use, modify, and distribute this template for any purpose.
