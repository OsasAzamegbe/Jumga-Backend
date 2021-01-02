from dotenv import load_dotenv
from pathlib import Path
import os

env_path = Path(__file__).resolve().parent.parent / 'Jumga/.env'
load_dotenv(env_path, verbose=True)