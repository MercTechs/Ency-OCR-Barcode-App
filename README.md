# FastAPI Multi-Service Project

A FastAPI-based project with three main applications for barcode reading, nutrition extraction, and API gateway functionality.

## Project Structure

```
project/
├── barcode_reader/
│   ├── src/
│   │   └── app/
│   │       └── main.py
│   └── .env
├── extract_nutrition/
│   ├── src/
│   │   └── app/
│   │       └── main.py
│   └── .env
├── gateway/
│   ├── src/
│   │   └── app/
│   │       └── main.py
│   └── .env
├── pyproject.toml
└── uv.lock
```

## Overview

The project consists of three main applications:

- **barcode_reader**: Reads content from barcodes in images
- **extract_nutrition**: Extracts nutrition information from images using LLM
- **gateway**: Acts as an intermediary between clients and the other two services

## Prerequisites

- Python 3.8+
- [uv](https://docs.astral.sh/uv/) package manager

## Installation

### 1. Install uv (if not already installed)

Choose one of the following methods:

#### Option A: Using the official installer (Recommended)
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

#### Option B: Using pip
```bash
pip install uv
```

#### Option C: Using pipx (Recommended for isolated installation)
```bash
# Install pipx if not already installed
pip install pipx

# Install uv using pipx
pipx install uv
```

**Note**: If using pipx, make sure your PATH includes the pipx binary directory. You can ensure this by running:
```bash
pipx ensurepath
```

### 2. Install Dependencies

You can install dependencies using any of these methods:

#### Option A: Using uv.lock (Recommended)
```bash
uv sync
```

#### Option B: Using pyproject.toml with uv sync
```bash
uv sync --no-lock-update
```

#### Option C: Using pyproject.toml with pip-style command
```bash
uv pip install -r pyproject.toml
```

**Note**: 
- Option A is recommended as it ensures exact dependency versions from the lock file
- Option B syncs from pyproject.toml without updating the lock file
- Option C uses uv's pip-compatible interface to install from pyproject.toml

## Configuration

Each application requires specific environment variables. You can set these in individual `.env` files for each service or export them to your system environment.

### Barcode Reader Service

Create `barcode_reader/.env`:
```env
BARCODE_READER_HOST=localhost
BARCODE_READER_PORT=8000
BARCODE_READER_DEBUG=True
```

### Extract Nutrition Service

Create `extract_nutrition/.env`:
```env
LLM_MODEL_PATH=/path/to/your/model.gguf
NUTRITION_EXTRACTOR_HOST=localhost
NUTRITION_EXTRACTOR_PORT=8002
NUTRITION_EXTRACTOR_DEBUG=True
```

**Note**: For the `LLM_MODEL_PATH`, we recommend using `Llama3-DocChat-1.0-8B-Q8_0.gguf` model file.

### Gateway Service

Create `gateway/.env`:
```env
GATEWAY_API_KEY=your_api_key_here
BARCODE_UPLOAD_IMG_API_URL=http://localhost:8000/api/v1/image/upload-image/
BARCODE_READ_API_URL=http://localhost:8000/api/v1/image/read-barcode/
OCR_UPLOAD_IMG_API_URL=http://localhost:8000/api/v1/image/upload-image/
OCR_EXTRACT_TEXT_API_URL=http://localhost:8000/api/v1/ocr/extract-text/
GATEWAY_HOST=localhost
GATEWAY_PORT=8001
```

## Running the Applications

### Important Notes
- Each service must run on a different port if hosted on the same machine
- Start the barcode_reader and extract_nutrition services before starting the gateway
- The gateway service depends on the other two services being available

### 1. Start Barcode Reader Service

```bash
uv run barcode_reader/src/app/main.py
```

The service will start on `http://localhost:8000` (or the configured host/port).

### 2. Start Extract Nutrition Service

```bash
uv run extract_nutrition/src/app/main.py
```

The service will start on `http://localhost:8002` (or the configured host/port).

### 3. Start Gateway Service

**Important**: Ensure both previous services are running before starting the gateway.

```bash
uv run gateway/src/app/main.py
```

The gateway will start on `http://localhost:8001` (or the configured host/port).

## Service Startup Order

1. **First**: Start `barcode_reader` service
2. **Second**: Start `extract_nutrition` service
3. **Third**: Start `gateway` service

The gateway acts as an intermediary between end users and the barcode_reader/extract_nutrition services, so it requires both services to be running.

## Environment Variables Reference

### Barcode Reader
| Variable | Description | Example |
|----------|-------------|---------|
| `BARCODE_READER_HOST` | Host address | `localhost` |
| `BARCODE_READER_PORT` | Port number | `8000` |
| `BARCODE_READER_DEBUG` | Enable debug mode | `True` |

### Extract Nutrition
| Variable | Description | Example |
|----------|-------------|---------|
| `LLM_MODEL_PATH` | Path to GGUF model file | `/models/Llama3-DocChat-1.0-8B-Q8_0.gguf` |
| `NUTRITION_EXTRACTOR_HOST` | Host address | `localhost` |
| `NUTRITION_EXTRACTOR_PORT` | Port number | `8002` |
| `NUTRITION_EXTRACTOR_DEBUG` | Enable debug mode | `True` |

### Gateway
| Variable | Description | Example |
|----------|-------------|---------|
| `GATEWAY_API_KEY` | API key for authentication | `your_secret_key` |
| `BARCODE_UPLOAD_IMG_API_URL` | Barcode image upload endpoint | `http://localhost:8000/api/v1/image/upload-image/` |
| `BARCODE_READ_API_URL` | Barcode reading endpoint | `http://localhost:8000/api/v1/image/read-barcode/` |
| `OCR_UPLOAD_IMG_API_URL` | OCR image upload endpoint | `http://localhost:8000/api/v1/image/upload-image/` |
| `OCR_EXTRACT_TEXT_API_URL` | OCR text extraction endpoint | `http://localhost:8000/api/v1/ocr/extract-text/` |
| `GATEWAY_HOST` | Gateway host address | `localhost` |
| `GATEWAY_PORT` | Gateway port number | `8001` |

## Quick Start

1. Clone the repository
2. Install dependencies: `uv sync`
3. Set up environment variables in respective `.env` files
4. Download the recommended LLM model for nutrition extraction
5. Start services in order:
   ```bash
   # Terminal 1
   uv run barcode_reader/src/app/main.py
   
   # Terminal 2
   uv run extract_nutrition/src/app/main.py
   
   # Terminal 3
   uv run gateway/src/app/main.py
   ```

## API Documentation

Once all services are running, you can access the interactive Swagger documentation at:

- **Gateway API**: `http://localhost:8001/docs` (main entry point)
- **Barcode Reader API**: `http://localhost:8000/docs` (direct access)
- **Nutrition Extractor API**: `http://localhost:8002/docs` (direct access)

## Troubleshooting

### Common Issues

1. **Port conflicts**: Ensure each service uses a different port
2. **Model not found**: Verify the `LLM_MODEL_PATH` points to a valid GGUF file
3. **Gateway connection errors**: Ensure barcode_reader and extract_nutrition services are running before starting gateway
4. **Environment variables**: Double-check all required environment variables are set