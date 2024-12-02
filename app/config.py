# app/config.py
import os

DB_CONFIG = {
    "host": os.getenv("DB_HOST", "database-test1.cbeua8es25at.us-east-2.rds.amazonaws.com"),
    "port": os.getenv("DB_PORT", "5432"),
    "user": os.getenv("DB_USER", "postgres"),
    "password": os.getenv("DB_PASSWORD", "testdatabase4"),
    "database": os.getenv("DB_NAME", "postgres")
}

