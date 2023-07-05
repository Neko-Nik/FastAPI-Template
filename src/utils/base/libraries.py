"""
This file has all the necessary libraries for the project to run
any new library should be added here and imported in the respective files
"""

# FastAPI libraries
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse , PlainTextResponse , HTMLResponse
from fastapi import FastAPI, File, UploadFile , Form, Request, status, Response
from fastapi.templating import Jinja2Templates
import uvicorn


# other libraries
import json
import re
from functools import wraps

# read env variables
import dotenv
import configparser
import os


# Getting some constants from the constants.py file
from src.utils.base.constants import LOG_LEVEL, LOG_FILE_PATH

# Configure logging 
from src.utils.base.log_utils import configure_return_logger
logging = configure_return_logger(LOG_LEVEL=LOG_LEVEL,
                                  LOG_FILE_PATH=LOG_FILE_PATH)
