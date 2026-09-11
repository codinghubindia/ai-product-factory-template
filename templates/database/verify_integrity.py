"""
AI PRODUCT FACTORY — DATABASE INTEGRITY VERIFICATION SCRIPT
Runs PRAGMA integrity_check, foreign_key_check, and query benchmarks on SQLite database deliverables.
"""

import sys
import sqlite3

def verify_database(db_path):
    print(f"[DB INTEGRITY] Verifying SQLite database: {db_path}")
    conn = sqlite3.connect(db_path)
    conn.execute("PRAGMA foreign_keys = ON;")
    cursor = conn.cursor()

    passed = 0
    failed = 0

    def check(name, condition, error_msg=""):
        nonlocal passed, failed
        if condition:
            print(f"  [PASS] {name}")
            passed += 1
        else:
            print(f"  [FAIL] {name} - {error_msg}")
            failed += 1

    try:
        # 1. Structural Integrity Check
        cursor.execute("PRAGMA integrity_check;")
        res = cursor.fetchone()[0]
        check("Structural integrity_check is ok", res == "ok", f"Got: {res}")

        # 2. Foreign Key Constraints Check
        cursor.execute("PRAGMA foreign_key_check;")
        fk_violations = cursor.fetchall()
        check("Foreign key check has zero violations", len(fk_violations) == 0, f"Violations found: {fk_violations}")

        # 3. Table existence and population
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%';")
        tables = [t[0] for t in cursor.fetchall()]
        check("Database contains application tables", len(tables) >= 3, f"Tables: {tables}")

        for tbl in ["workspaces", "products", "audit_records"]:
            if tbl in tables:
                cursor.execute(f"SELECT COUNT(*) FROM {tbl};")
                cnt = cursor.fetchone()[0]
                check(f"Table '{tbl}' has rows", cnt > 0, f"Row count: {cnt}")

        # 4. Join Query Verification
        cursor.execute("""
            SELECT p.id, p.name, w.name, COUNT(a.id)
            FROM products p
            JOIN workspaces w ON p.workspace_id = w.id
            LEFT JOIN audit_records a ON a.product_id = p.id
            GROUP BY p.id;
        """)
        join_rows = cursor.fetchall()
        check("Relational join query executes cleanly", len(join_rows) > 0, f"Rows returned: {len(join_rows)}")

    except Exception as e:
        print(f"  [FAIL] Database verification error: {e}")
        failed += 1
    finally:
        conn.close()

    print(f"\n[DB INTEGRITY SUMMARY] Passed: {passed}, Failed: {failed}")
    return failed == 0

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "database.sqlite"
    success = verify_database(target)
    sys.exit(0 if success else 1)
