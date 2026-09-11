"""
AI PRODUCT FACTORY — AUTOMATED API CONTRACT TEST SUITE
Can be executed via: python templates/api/test_contract.py or pytest
"""

import json
import threading
import time
import urllib.request
import urllib.error
import sys

from server import run_server

SERVER_PORT = 8991
BASE_URL = f"http://127.0.0.1:{SERVER_PORT}"

def get_opener():
    # Bypass local sandbox proxies for 127.0.0.1 loopback testing
    return urllib.request.build_opener(urllib.request.ProxyHandler({}))

def run_tests():
    # 1. Start server in daemon thread
    thread = threading.Thread(target=run_server, args=(SERVER_PORT,), daemon=True)
    thread.start()
    time.sleep(0.5)

    passed = 0
    failed = 0
    opener = get_opener()

    def assert_eq(test_name, actual, expected):
        nonlocal passed, failed
        if actual == expected:
            print(f"  [PASS] {test_name}")
            passed += 1
        else:
            print(f"  [FAIL] {test_name} — Expected: {expected}, Got: {actual}")
            failed += 1

    print("\n[API CONTRACT TEST SUITE] Starting endpoint verification...")

    # Test 1: Health Check
    try:
        req = urllib.request.Request(f"{BASE_URL}/health")
        with opener.open(req) as resp:
            assert_eq("Health endpoint returns 200", resp.status, 200)
            data = json.loads(resp.read().decode("utf-8"))
            assert_eq("Health status is healthy", data.get("status"), "healthy")
    except Exception as e:
        print(f"  [FAIL] Health endpoint crashed: {e}")
        failed += 1

    # Test 2: List Items
    try:
        req = urllib.request.Request(f"{BASE_URL}/items")
        with opener.open(req) as resp:
            assert_eq("List items returns 200", resp.status, 200)
            data = json.loads(resp.read().decode("utf-8"))
            assert_eq("Success envelope is true", data.get("success"), True)
            assert_eq("Item list is non-empty", len(data.get("data", [])) >= 2, True)
    except Exception as e:
        print(f"  [FAIL] List items crashed: {e}")
        failed += 1

    # Test 3: Create Item Success
    try:
        payload = json.dumps({"name": "New Architecture Test", "category": "Core"}).encode("utf-8")
        req = urllib.request.Request(f"{BASE_URL}/items", data=payload, headers={"Content-Type": "application/json"})
        with opener.open(req) as resp:
            assert_eq("Create item returns 201", resp.status, 201)
            data = json.loads(resp.read().decode("utf-8"))
            assert_eq("Created item has valid ID prefix", data["data"]["id"].startswith("ITM-"), True)
    except Exception as e:
        print(f"  [FAIL] Create item crashed: {e}")
        failed += 1

    # Test 4: Validation Error (Invalid short name)
    try:
        payload = json.dumps({"name": "x"}).encode("utf-8")
        req = urllib.request.Request(f"{BASE_URL}/items", data=payload, headers={"Content-Type": "application/json"})
        opener.open(req)
        print("  [FAIL] Validation test expected 422, but succeeded.")
        failed += 1
    except urllib.error.HTTPError as e:
        assert_eq("Invalid payload returns 422", e.code, 422)
        err_data = json.loads(e.read().decode("utf-8"))
        assert_eq("Error envelope success is false", err_data.get("success"), False)
        assert_eq("Error code is VALIDATION_FAILED", err_data["error"]["code"], "VALIDATION_FAILED")

    # Test 5: Route Not Found (404)
    try:
        req = urllib.request.Request(f"{BASE_URL}/non-existent-route")
        opener.open(req)
        print("  [FAIL] Expected 404, but succeeded.")
        failed += 1
    except urllib.error.HTTPError as e:
        assert_eq("Non-existent route returns 404", e.code, 404)

    print(f"\n[API TEST SUMMARY] Passed: {passed}, Failed: {failed}")
    return failed == 0

if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)
