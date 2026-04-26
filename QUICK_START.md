# Quick Start Guide

Get the Enterprise AI DevOps Multi-Agent Platform running in 5 minutes!

## 🚀 Quick Setup

### 1. Prerequisites Check
```bash
python --version  # Should be 3.9+
pip --version
```

### 2. Clone & Setup
```bash
# Clone the repository
git clone <your-repo-url>
cd enterprise-ai-agent-platform

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
# Upgrade pip first
pip install --upgrade pip

# Install all dependencies
pip install -r requirements.txt
```

### 4. Configure Environment
```bash
# Copy environment template
cp .env.example .env

# Edit .env and add your OpenAI API key
# OPENAI_API_KEY=sk-your-key-here
```

### 5. Run the Platform
```bash
PYTHONPATH=. uvicorn services.api.main:app --reload
```

### 6. Test It!
Open your browser to:
- **API Docs**: http://127.0.0.1:8000/docs
- **Health Check**: http://127.0.0.1:8000/health

## 🧪 Quick Test

### Using the Interactive Docs
1. Go to http://127.0.0.1:8000/docs
2. Click on `POST /query`
3. Click "Try it out"
4. Enter this test query:
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

## 🎯 What Happens?

When you submit a query, the platform:

1. **Planner Agent** analyzes the issue and creates an investigation plan
2. **Executor Agent** executes the planned steps (simulated)
3. **Analysis Agent** provides root cause analysis and recommendations

## 🔧 Common Issues

### "Did not find openai_api_key"
**Fix**: Add your OpenAI API key to `.env` file
```bash
echo "OPENAI_API_KEY=sk-your-key-here" > .env
```

### "ModuleNotFoundError: No module named 'services'"
**Fix**: Always use `PYTHONPATH=.` when running
```bash
PYTHONPATH=. uvicorn services.api.main:app --reload
```

### Port 8000 already in use
**Fix**: Use a different port
```bash
PYTHONPATH=. uvicorn services.api.main:app --reload --port 8001
```

## 📚 Next Steps

- Read the [Full README](README.md) for detailed information
- Check [Setup Guide](docs/SETUP_GUIDE.md) for troubleshooting
- Review [Architecture](docs/architecture.md) to understand the system

## 🎓 Example Queries to Try

```json
{"input": "High memory usage in production pods"}
{"input": "Service returning 503 errors"}
{"input": "Database connection timeout"}
{"input": "Deployment rollout stuck"}
{"input": "Node not ready in cluster"}
```

## 💡 Tips

- Use `--reload` flag during development for auto-restart
- Check logs in the terminal for debugging
- Use `/health` endpoint to verify OpenAI configuration
- Explore the interactive docs at `/docs` for all endpoints

---

**Ready to build intelligent DevOps automation? Let's go! 🚀**