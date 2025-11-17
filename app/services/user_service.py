import os
from app.data.db import connect_database
from app.data.crud import insert_user  # if in different file, update the import

TXT_FILE = "DATA/users.txt"

def migrate_txt_to_db():
    if not os.path.exists(TXT_FILE):
        print("users.txt not found!")
        return

    with open(TXT_FILE, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            username, hashed_password = line.split(",")

            # Insert into database
            try:
                insert_user(username, hashed_password)
                print(f"Inserted: {username}")
            except Exception as e:
                print(f"Skipping {username} — already exists or error: {e}")

    print("Migration complete.")
