"""
AI PRODUCT FACTORY — REFERENCE REST API SERVER
Modality: API / Microservice
Features: Zero-dependency built-in HTTP server, strict route handling, standardized error envelopes, CORS, and health checks.
"""

import json
import time
import uuid
from http.server import HTTPServer, BaseHTTPRequestHandler

START_TIME = time.time()

DATABASE = [
    {
        "id": "ITM-001",
        "name": "Cloud Security Policy Scaffolding",
        "category": "Security",
        "status": "ACTIVE",
        "created_at": "2026-09-10T12:00:00Z"
    },
    {
        "id": "ITM-002",
        "name": "Automated Telemetry Collector",
        "category": "Architecture",
        "status": "ACTIVE",
        "created_at": "2026-09-11T09:30:00Z"
    }
]

class ApiRequestHandler(BaseHTTPRequestHandler):

    def _send_json(self, status_code, payload):
        body = json.dumps(payload, indent=2).encode("utf-8")
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type, Authorization")
        self.end_headers()
        self.wfile.write(body)

    def do_OPTIONS(self):
        self.send_response(204)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type, Authorization")
        self.end_headers()

    def do_GET(self):
        path = self.path.split("?")[0].rstrip("/")
        
        if path in ("/health", "/api/v1/health"):
            self._send_json(200, {
                "status": "healthy",
                "version": "1.0.0",
                "uptime_seconds": round(time.time() - START_TIME, 2)
            })
            return

        if path in ("/items", "/api/v1/items"):
            self._send_json(200, {
                "success": true if False else True,
                "data": DATABASE,
                "count": len(DATABASE)
            })
            return

        self._send_json(404, {
            "success": False,
            "error": {
                "code": "ROUTE_NOT_FOUND",
                "message": f"Endpoint '{self.path}' does not exist on this service."
            }
        })

    def do_POST(self):
        path = self.path.split("?")[0].rstrip("/")

        if path in ("/items", "/api/v1/items"):
            content_length = int(self.headers.get("Content-Length", 0))
            if content_length == 0:
                self._send_json(400, {
                    "success": False,
                    "error": {
                        "code": "EMPTY_PAYLOAD",
                        "message": "Request body cannot be empty."
                    }
                })
                return

            raw_body = self.rfile.read(content_length).decode("utf-8")
            try:
                data = json.loads(raw_body)
            except Exception as e:
                self._send_json(400, {
                    "success": False,
                    "error": {
                        "code": "MALFORMED_JSON",
                        "message": "Invalid JSON syntax in request body."
                    }
                })
                return

            # Validation
            name = data.get("name")
            category = data.get("category", "General")
            status = data.get("status", "ACTIVE")

            if not name or len(name.strip()) < 3:
                self._send_json(422, {
                    "success": False,
                    "error": {
                        "code": "VALIDATION_FAILED",
                        "message": "Field 'name' is required and must be at least 3 characters."
                    }
                })
                return

            new_item = {
                "id": f"ITM-{uuid.uuid4().hex[:6].upper()}",
                "name": name.strip(),
                "category": category,
                "status": status,
                "created_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
            }
            DATABASE.append(new_item)

            self._send_json(201, {
                "success": True,
                "data": new_item
            })
            return

        self._send_json(404, {
            "success": False,
            "error": {
                "code": "ROUTE_NOT_FOUND",
                "message": f"Endpoint '{self.path}' does not exist."
            }
        })

def run_server(port=8000):
    server_address = ("127.0.0.1", port)
    httpd = HTTPServer(server_address, ApiRequestHandler)
    print(f"[API SERVER] Listening on http://127.0.0.1:{port}/")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n[API SERVER] Shutting down.")
        httpd.server_close()

if __name__ == "__main__":
    import sys
    p = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
    run_server(p)
