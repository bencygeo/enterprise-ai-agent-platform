# Setup Guide

This guide will help you set up and run the Enterprise AI Agent Platform.

## Prerequisites

- Python 3.9 or higher
- pip (Python package manager)
- OpenAI API account and API key
- Git (for cloning the repository)

## Step-by-Step Setup

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd enterprise-ai-agent-platform
```

### 2. Create Virtual Environment

It's recommended to use a virtual environment to isolate dependencies:

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

You should see `(venv)` in your terminal prompt indicating the virtual environment is active.

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

This will install all required packages including:
- FastAPI and Uvicorn (API server)
- LangChain and LangGraph (AI orchestration)
- OpenAI SDK (AI models)
- Kubernetes client (K8s integration)
- And other dependencies

### 4. Configure Environment Variables

Create a `.env` file in the project root:

```bash
cp .env.example .env
```

Edit the `.env` file and add your OpenAI API key:

```env
OPENAI_API_KEY=sk-your-actual-openai-api-key-here
OPENAI_MODEL=gpt-4
```

**Important:** Never commit your `.env` file to version control. It's already included in `.gitignore`.

### 5. Verify Installation

Check that everything is installed correctly:

```bash
python -c "import fastapi, langchain, openai; print('All packages installed successfully!')"
```

## Running the Application

### Start the API Server

```bash
PYTHONPATH=. uvicorn services.api.main:app --reload
```

**Explanation:**
- `PYTHONPATH=.` - Ensures Python can find the services module
- `uvicorn` - ASGI server for running FastAPI
- `services.api.main:app` - Path to the FastAPI application
- `--reload` - Auto-reload on code changes (development only)

### Access the Application

Once the server is running, you can access:

- **API Base URL:** http://127.0.0.1:8000
- **Interactive API Docs (Swagger):** http://127.0.0.1:8000/docs
- **Alternative API Docs (ReDoc):** http://127.0.0.1:8000/redoc

## Testing the API

### Using the Interactive Docs

1. Open http://127.0.0.1:8000/docs in your browser
2. Click on the `/query` endpoint
3. Click "Try it out"
4. Enter a test query in the request body:
   ```json
   {
     "input": "Pod crash-looping in production namespace"
   }
   ```
5. Click "Execute"

### Using cURL

```bash
curl -X POST "http://127.0.0.1:8000/query" \
  -H "Content-Type: application/json" \
  -d '{"input": "Pod crash-looping in production namespace"}'
```

### Using Python

```python
import requests

response = requests.post(
    "http://127.0.0.1:8000/query",
    json={"input": "Pod crash-looping in production namespace"}
)

print(response.json())
```

## Troubleshooting

### Issue: "Did not find openai_api_key"

**Solution:** 
1. Ensure you've created a `.env` file from `.env.example`
2. Add your actual OpenAI API key to the `.env` file
3. Restart the application

### Issue: "ModuleNotFoundError: No module named 'services'"

**Solution:**
Run the application with `PYTHONPATH=.` prefix:
```bash
PYTHONPATH=. uvicorn services.api.main:app --reload
```

### Issue: "ImportError: cannot import name 'ChatOpenAI'"

**Solution:**
Ensure you've installed the correct packages:
```bash
pip install langchain-openai langchain-community
```

### Issue: Deprecated LangChain warnings

**Solution:**
The code has been updated to use the latest LangChain packages. If you still see warnings:
```bash
pip install --upgrade langchain langchain-openai langchain-community
```

### Issue: Port 8000 already in use

**Solution:**
Either stop the process using port 8000, or run on a different port:
```bash
PYTHONPATH=. uvicorn services.api.main:app --reload --port 8001
```

## Development Tips

### Auto-reload on Changes

The `--reload` flag enables auto-reload during development. The server will automatically restart when you modify code files.

### Viewing Logs

Uvicorn provides detailed logs in the console. Watch for:
- Request logs (incoming API calls)
- Error messages
- Deprecation warnings

### Testing Changes

After making code changes:
1. Save the file
2. Wait for auto-reload (if using `--reload`)
3. Test the endpoint using the interactive docs or cURL

## Next Steps

- Read the [Architecture Documentation](architecture.md)
- Explore the agent implementations in `services/agents/`
- Add custom tools in `services/tools/`
- Extend the workflow in `services/orchestration/graph.py`

## Getting Help

If you encounter issues:
1. Check this troubleshooting section
2. Review the error messages carefully
3. Ensure all environment variables are set correctly
4. Verify all dependencies are installed
5. Check the GitHub issues for similar problems