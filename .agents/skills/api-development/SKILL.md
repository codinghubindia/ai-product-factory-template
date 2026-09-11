---
name: api-development
description: REST/FastAPI/Express API architecture, OpenAPI 3.1 specification, request/response validation, standardized error envelopes, and automated contract testing.
---

# API Development Skill

This skill governs backend service, microservice, and REST/JSON API product engineering, ensuring clear interface contracts, deterministic error handling, security, and developer ergonomics.

## 1. Core Invariants

- **OpenAPI 3.1 Specification:** Every API product must maintain an authoritative `openapi.yaml` or `openapi.json` defining all routes, query parameters, request bodies, and response schemas.
- **Strict Input Validation:** All payloads must be strictly validated against schemas (e.g., Pydantic or Zod) before reaching business logic. Disallow extra unexpected fields.
- **Standardized Response Envelopes:**
  - Success envelope:
    ```json
    {
      "success": true,
      "data": { ... },
      "metadata": { "timestamp": "...", "version": "1.0.0" }
    }
    ```
  - Error envelope:
    ```json
    {
      "success": false,
      "error": {
        "code": "VALIDATION_FAILED",
        "message": "Human-readable description of error",
        "details": [ ... ]
      }
    }
    ```
- **Consistent HTTP Status Codes:**
  - `200 OK`: Successful retrieval or update.
  - `201 Created`: Successful resource creation.
  - `400 Bad Request`: Validation failure or malformed payload.
  - `401 Unauthorized`: Missing or invalid authentication token.
  - `403 Forbidden`: Authenticated user lacks permission.
  - `404 Not Found`: Target resource does not exist.
  - `422 Unprocessable Entity`: Semantic data validation error.
  - `500 Internal Server Error`: Unhandled server exception (stack trace never leaked to client).
- **Mandatory System Endpoints:**
  - `GET /health` or `GET /api/v1/health`: Returns `{ "status": "healthy", "uptime_seconds": 120, "version": "..." }`.

## 2. Tools & Templates

- Starter: `templates/api/`
- Spec: `templates/api/openapi.json`
- Server: `templates/api/server.py`
- Contract Tests: `templates/api/test_contract.py`

## 3. Step-by-Step Procedure

### Step 1: Interface Contract Definition
1. Define endpoints, paths, HTTP methods, and models in `openapi.yaml`.
2. Review parameter types, bounds, and required attributes.

### Step 2: Implementation
1. Implement routes using lightweight Python FastAPI / Flask or Node.js Express.
2. Implement CORS middleware with explicit allowed origins.
3. Wire in rate-limiting headers (`RateLimit-Limit`, `RateLimit-Remaining`).
4. Keep all credentials in environment variables (`.env.example` provided with zero real secrets).

### Step 3: Contract & Endpoint Testing
1. Run automated endpoint test suite:
   ```bash
   pytest templates/api/test_contract.py
   ```
2. Test both positive flows (valid requests return 200/201) and negative edge cases (invalid body returns 400/422, non-existent ID returns 404).
