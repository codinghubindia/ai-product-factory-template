"""
AI PRODUCT FACTORY — DATABASE MIGRATION ENGINE
Executes schema initialization, version tracking, and seed data population for SQLite products.
"""

import os
import sys
import sqlite3

def run_migrations(db_path, schema_file="schema.sql", seed_file="seed.sql"):
    os.makedirs(os.path.dirname(os.path.abspath(db_path)), exist_ok=True)
    base_dir = os.path.dirname(__file__)
    
    schema_path = os.path.join(base_dir, schema_file) if not os.path.isabs(schema_file) else schema_file
    seed_path = os.path.join(base_dir, seed_file) if not os.path.isabs(seed_file) else seed_file

    print(f"[DB MIGRATION] Connecting to SQLite database: {db_path}")
    conn = sqlite3.connect(db_path)
    conn.execute("PRAGMA foreign_keys = ON;")

    try:
        with conn:
            # 1. Schema Migration History Table
            conn.execute("""
                CREATE TABLE IF NOT EXISTS _schema_migrations (
                    version TEXT PRIMARY KEY,
                    applied_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL
                );
            """)

            # 2. Apply Schema DDL
            if os.path.exists(schema_path):
                print(f"[DB MIGRATION] Applying schema from: {schema_path}")
                with open(schema_path, "r", encoding="utf-8") as f:
                    conn.executescript(f.read())
                conn.execute("INSERT OR REPLACE INTO _schema_migrations (version) VALUES ('001_initial_schema');")

            # 3. Apply Seed Data
            if os.path.exists(seed_path):
                print(f"[DB MIGRATION] Seeding realistic data from: {seed_path}")
                with open(seed_path, "r", encoding="utf-8") as f:
                    conn.executescript(f.read())

        print(f"[DB MIGRATION] Successfully built and migrated database: {db_path}")
        return True

    except Exception as e:
        print(f"[DB MIGRATION ERROR] Failed to execute database migrations: {e}")
        return False
    finally:
        conn.close()

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "database.sqlite"
    success = run_migrations(target)
    sys.exit(0 if success else 1)
