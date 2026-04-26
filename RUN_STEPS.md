# Step-by-Step Guide to Run the Enterprise AI DevOps Multi-Agent Platform

Follow these steps in order to get the platform running.

## ✅ Prerequisites Check

You should have already completed:
- ✅ Python 3.9+ installed
- ✅ Virtual environment created and activated
- ✅ All dependencies installed (langchain, fastapi, etc.)

## 📝 Step 1: Add Your OpenAI API Key

### Option A: Using Command Line (Recommended)
```bash
# Open the .env file in your default editor
nano .env

# Or use vim
vim .env

# Or use VS Code
code .env
```

### Option B: Using Echo Command
```bash
# Replace 'your-actual-api-key-here' with your real OpenAI API key
echo "OPENAI_API_KEY=sk-your-actual-api-key-here" > .env
```

### What to Add
Your `.env` file should contain:
```
OPENAI_API_KEY=sk-proj-xxxxxxxxxxxxxxxxxxxxx
OPENAI_MODEL=gpt-4
```

**Important:** 
- Get your API key from: https://platform.openai.com/api-keys
- Never share or commit your API key
- The key starts with `sk-`

### Verify the Key is Set
```bash
cat .env | grep OPENAI_API_KEY
# Should show: OPENAI_API_KEY=sk-your-key...
```

## 🚀 Step 2: Start the Application

### Run the Server
```bash
PYTHONPATH=. uvicorn services.api.main:app --reload
```

**What this command does:**
- `PYTHONPATH=.` - Tells Python where to find the services module
- `uvicorn` - ASGI server that runs FastAPI
- `services.api.main:app` - Path to your FastAPI application
- `--reload` - Auto-restart when code changes (development mode)

### Expected Output
You should see:
```
INFO:     Will watch for changes in these directories: ['/Users/.../enterprise-ai-agent-platform']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [xxxxx] using StatReload
INFO:     Started server process [xxxxx]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

**✅ Success!** If you see this, the server is running!

## 🌐 Step 3: Access the Application

### Open Your Browser

1. **API Documentation (Swagger UI)**
   ```
   http://127.0.0.1:8000/docs
   ```
   - Interactive API documentation
   - Try out endpoints directly
   - See request/response schemas

2. **Health Check**
   ```
   http://127.0.0.1:8000/health
   ```
   - Verify server is running
   - Check OpenAI configuration status

3. **API Information**
   ```
   http://127.0.0.1:8000/
   ```
   - Basic API info
   - Links to documentation

## 🧪 Step 4: Test the Platform

### Method 1: Using the Interactive Docs (Easiest)

1. Go to http://127.0.0.1:8000/docs
2. Find the `POST /query` endpoint
3. Click on it to expand
4. Click the **"Try it out"** button
5. In the Request body, enter:
   ```json
   {
     "input": "Pod crash-looping in production namespace"
   }
   ```
6. Click **"Execute"**
7. Scroll down to see the response

### Method 2: Using cURL (Command Line)

```bash
curl -X POST "http://127.0.0.1:8000/query" \
  -H "Content-Type: application/json" \
  -d '{
    "input": "Pod crash-looping in production namespace"
  }'
```

### Method 3: Using Python Script

Create a file `test_api.py`:
```python
import requests
import json

# Test the health endpoint
health = requests.get("http://127.0.0.1:8000/health")
print("Health Check:", health.json())

# Test the query endpoint
response = requests.post(
    "http://127.0.0.1:8000/query",
    json={"input": "Pod crash-looping in production namespace"}
)

print("\nQuery Response:")
print(json.dumps(response.json(), indent=2))
```

Run it:
```bash
python test_api.py
```

## 📊 Step 5: Understanding the Response

When you submit a query, you'll get a response like:

```json
{
  "plan": "Investigation plan from Planner Agent...",
  "execution": "Execution results from Executor Agent...",
  "result": "Root cause analysis and recommendations from Analysis Agent..."
}
```

**What happened:**
1. **Planner Agent** analyzed your query and created an investigation plan
2. **Executor Agent** executed the planned steps
3. **Analysis Agent** provided root cause analysis and recommendations

## 🎯 Step 6: Try More Examples

### Example Queries

```json
{"input": "High memory usage in production pods"}
```

```json
{"input": "Service returning 503 errors"}
```

```json
{"input": "Database connection timeout"}
```

```json
{"input": "Deployment rollout stuck"}
```

```json
{"input": "Node not ready in cluster"}
```

## 🛑 Step 7: Stopping the Server

To stop the server:
1. Go to the terminal where the server is running
2. Press `Ctrl+C`
3. Wait for graceful shutdown

## 🔄 Step 8: Restarting After Changes

If you make code changes:

### With --reload flag (Automatic)
- Server automatically restarts when you save files
- Just wait a few seconds after saving

### Manual Restart
```bash
# Stop the server (Ctrl+C)
# Then start again
PYTHONPATH=. uvicorn services.api.main:app --reload
```

## 🐛 Troubleshooting

### Issue: "Did not find openai_api_key"

**Solution:**
```bash
# Check if .env file exists
ls -la .env

# Check if key is set
cat .env | grep OPENAI_API_KEY

# If empty, add your key
echo "OPENAI_API_KEY=sk-your-key-here" > .env

# Restart the server
```

### Issue: "ModuleNotFoundError: No module named 'services'"

**Solution:**
```bash
# Always use PYTHONPATH=. prefix
PYTHONPATH=. uvicorn services.api.main:app --reload

# Verify you're in the project root
pwd  # Should end with /enterprise-ai-agent-platform
```

### Issue: "Address already in use"

**Solution:**
```bash
# Option 1: Kill the process using port 8000
lsof -ti:8000 | xargs kill -9

# Option 2: Use a different port
PYTHONPATH=. uvicorn services.api.main:app --reload --port 8001
```

### Issue: Slow Response

**Causes:**
- First request initializes the LLM (takes longer)
- OpenAI API latency
- Complex queries

**Solution:**
- Wait for first request to complete
- Subsequent requests will be faster
- Use gpt-3.5-turbo for faster responses (edit .env)

## 📚 Additional Resources

- **Quick Start**: [QUICK_START.md](QUICK_START.md)
- **Setup Guide**: [docs/SETUP_GUIDE.md](docs/SETUP_GUIDE.md)
- **Architecture**: [docs/architecture.md](docs/architecture.md)
- **Troubleshooting**: [docs/TROUBLESHOOTING.md](docs/TROUBLESHOOTING.md)

## ✅ Verification Checklist

Before considering setup complete, verify:

- [ ] Virtual environment is activated (`(venv)` in prompt)
- [ ] All packages installed (`pip list | grep langchain`)
- [ ] `.env` file exists with OpenAI API key
- [ ] Server starts without errors
- [ ] Health endpoint returns `{"status": "healthy"}`
- [ ] API docs accessible at `/docs`
- [ ] Test query returns a response
- [ ] No deprecation warnings in terminal

## 🎉 Success!

If all steps completed successfully, you now have:
- ✅ A running multi-agent AI platform
- ✅ Interactive API documentation
- ✅ Working Planner, Executor, and Analysis agents
- ✅ Foundation for DevOps automation

## 🚀 Next Steps

1. **Explore the API**: Try different queries in the interactive docs
2. **Read the Architecture**: Understand how agents work together
3. **Customize Agents**: Modify agent behavior in `services/agents/`
4. **Add Tools**: Create new tools in `services/tools/`
5. **Extend Workflow**: Modify the graph in `services/orchestration/graph.py`

---

**Need help?** Check the troubleshooting guide or open an issue on GitHub!