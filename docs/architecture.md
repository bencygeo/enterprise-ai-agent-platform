# Enterprise AI Agent Platform - Architecture

## Overview

The Enterprise AI Agent Platform is a multi-agent system designed for DevOps automation and intelligent task orchestration. It uses LangGraph for workflow management and LangChain for AI agent implementation.

## System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     Client Applications                      │
│              (Web UI, CLI, External Services)                │
└────────────────────────┬────────────────────────────────────┘
                         │
                         │ HTTP/REST
                         │
┌────────────────────────▼────────────────────────────────────┐
│                      FastAPI Layer                           │
│                   (services/api/main.py)                     │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐     │
│  │ POST /query  │  │ GET /health  │  │   GET /      │     │
│  └──────────────┘  └──────────────┘  └──────────────┘     │
└────────────────────────┬────────────────────────────────────┘
                         │
                         │ Invoke
                         │
┌────────────────────────▼────────────────────────────────────┐
│              LangGraph Orchestration Layer                   │
│              (services/orchestration/graph.py)               │
│                                                              │
│  ┌──────────────────────────────────────────────────────┐  │
│  │              State Management                         │  │
│  │  { input, plan, execution, result }                   │  │
│  └──────────────────────────────────────────────────────┘  │
│                                                              │
│  ┌──────────┐      ┌──────────┐      ┌──────────┐         │
│  │ Planner  │─────▶│ Executor │─────▶│ Analysis │         │
│  │  Agent   │      │  Agent   │      │  Agent   │         │
│  └──────────┘      └──────────┘      └──────────┘         │
└────────────────────────┬────────────────────────────────────┘
                         │
                         │ Uses
                         │
┌────────────────────────▼────────────────────────────────────┐
│                    Agent Layer                               │
│                  (services/agents/)                          │
│                                                              │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ Planner Agent (planner_agent.py)                     │   │
│  │ - Analyzes incoming queries                          │   │
│  │ - Creates investigation plans                        │   │
│  │ - Uses ChatOpenAI for planning                       │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                              │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ Executor Agent (executor_agent.py)                   │   │
│  │ - Executes planned steps                             │   │
│  │ - Calls appropriate tools                            │   │
│  │ - Collects execution results                         │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                              │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ Analysis Agent (analysis_agent.py)                   │   │
│  │ - Analyzes execution results                         │   │
│  │ - Identifies root causes                             │   │
│  │ - Provides recommendations                           │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                              │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ Router (router.py)                                   │   │
│  │ - Routes queries to appropriate agents               │   │
│  │ - Handles different query types                      │   │
│  └─────────────────────────────────────────────────────┘   │
└────────────────────────┬────────────────────────────────────┘
                         │
                         │ Calls
                         │
┌────────────────────────▼────────────────────────────────────┐
│                     Tools Layer                              │
│                   (services/tools/)                          │
│                                                              │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ Kubernetes Tools (k8s_tools.py)                      │   │
│  │ - Pod management                                     │   │
│  │ - Deployment operations                              │   │
│  │ - Log retrieval                                      │   │
│  │ - Resource monitoring                                │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                              │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ Future Tools                                         │   │
│  │ - Cloud provider APIs                                │   │
│  │ - Monitoring systems                                 │   │
│  │ - Ticketing systems                                  │   │
│  └─────────────────────────────────────────────────────┘   │
└──────────────────────────────────────────────────────────────┘
```

## Component Details

### 1. API Layer (FastAPI)

**Location:** `services/api/main.py`

**Responsibilities:**
- Expose REST API endpoints
- Handle HTTP requests/responses
- Validate input data using Pydantic models
- Manage API documentation (Swagger/ReDoc)
- Health checks and monitoring endpoints

**Key Endpoints:**
- `POST /query` - Main endpoint for processing queries
- `GET /health` - Health check endpoint
- `GET /` - API information

### 2. Orchestration Layer (LangGraph)

**Location:** `services/orchestration/graph.py`

**Responsibilities:**
- Define agent workflow as a directed graph
- Manage state transitions between agents
- Handle data flow between agents
- Compile and execute the workflow

**Workflow:**
```
Input → Planner → Executor → Analysis → Output
```

**State Schema:**
```python
{
    "input": str,      # Original query
    "plan": Any,       # Investigation plan
    "execution": Any,  # Execution results
    "result": Any      # Final analysis and recommendations
}
```

### 3. Agent Layer

#### Planner Agent
**Location:** `services/agents/planner_agent.py`

**Purpose:** Analyze queries and create investigation plans

**Process:**
1. Receives user query
2. Uses ChatOpenAI to understand the issue
3. Breaks down the problem into steps
4. Returns structured investigation plan

**Example Output:**
```
Plan:
1. Check pod status in namespace
2. Review recent logs
3. Examine resource limits
4. Check for recent deployments
```

#### Executor Agent
**Location:** `services/agents/executor_agent.py`

**Purpose:** Execute planned investigation steps

**Process:**
1. Receives investigation plan
2. Calls appropriate tools for each step
3. Collects results from tool executions
4. Returns execution summary

#### Analysis Agent
**Location:** `services/agents/analysis_agent.py`

**Purpose:** Analyze results and provide recommendations

**Process:**
1. Receives execution results
2. Identifies patterns and root causes
3. Generates actionable recommendations
4. Returns final analysis

### 4. Tools Layer

**Location:** `services/tools/`

**Purpose:** Provide integrations with external systems

**Current Tools:**
- **Kubernetes Tools** (`k8s_tools.py`)
  - Pod operations
  - Deployment management
  - Log retrieval
  - Resource monitoring

**Future Tools:**
- Cloud provider APIs (AWS, GCP, Azure)
- Monitoring systems (Prometheus, Grafana)
- Ticketing systems (Jira, ServiceNow)
- CI/CD platforms (Jenkins, GitLab)

## Data Flow

### Request Flow

1. **Client Request**
   ```
   POST /query
   {
     "input": "Pod crash-looping in production"
   }
   ```

2. **API Layer**
   - Validates request
   - Invokes LangGraph workflow

3. **Planner Agent**
   - Analyzes query
   - Creates investigation plan
   - Updates state with plan

4. **Executor Agent**
   - Reads plan from state
   - Executes each step using tools
   - Updates state with execution results

5. **Analysis Agent**
   - Reads execution results
   - Performs root cause analysis
   - Updates state with final result

6. **Response**
   ```json
   {
     "plan": "...",
     "execution": "...",
     "result": "Root cause: Memory limit exceeded. Recommendation: Increase memory limit to 2Gi"
   }
   ```

## Technology Stack

### Core Framework
- **FastAPI** - Modern web framework for building APIs
- **Uvicorn** - ASGI server for running FastAPI
- **Pydantic** - Data validation using Python type hints

### AI/ML
- **LangChain** - Framework for building LLM applications
- **LangGraph** - Library for building stateful multi-agent workflows
- **OpenAI** - GPT models for natural language understanding

### Integrations
- **Kubernetes Client** - Python client for Kubernetes API
- **Python-dotenv** - Environment variable management

### Development
- **Pytest** - Testing framework
- **Structlog** - Structured logging

## Design Patterns

### 1. Agent Pattern
Each agent is a self-contained function that:
- Receives state as input
- Performs specific task
- Returns updated state

### 2. State Management
LangGraph manages state transitions:
- Immutable state updates
- Type-safe state schema
- Automatic state propagation

### 3. Tool Abstraction
Tools are abstracted as functions:
- Clear input/output contracts
- Error handling
- Reusable across agents

### 4. Dependency Injection
Configuration and dependencies injected at runtime:
- Environment variables for secrets
- Lazy initialization of expensive resources
- Easy testing with mocks

## Security Considerations

### API Security
- Input validation using Pydantic
- Error handling without exposing internals
- Rate limiting (to be implemented)

### Secrets Management
- API keys stored in environment variables
- `.env` file excluded from version control
- No hardcoded credentials

### Kubernetes Access
- RBAC for K8s operations
- Namespace isolation
- Audit logging

## Scalability

### Horizontal Scaling
- Stateless API design
- Multiple Uvicorn workers
- Load balancer ready

### Performance
- Async/await for I/O operations
- Connection pooling
- Caching (to be implemented)

### Monitoring
- Health check endpoints
- Structured logging
- Metrics collection (to be implemented)

## Future Enhancements

### Short Term
1. Add more tools (cloud providers, monitoring)
2. Implement caching layer
3. Add authentication/authorization
4. Enhanced error handling

### Medium Term
1. Multi-tenancy support
2. Workflow customization UI
3. Real-time notifications
4. Advanced analytics

### Long Term
1. Self-learning agents
2. Automated remediation
3. Predictive analysis
4. Multi-cloud support

## Development Guidelines

### Adding New Agents
1. Create agent file in `services/agents/`
2. Implement agent function with state parameter
3. Update `services/orchestration/graph.py`
4. Add tests in `tests/`

### Adding New Tools
1. Create tool file in `services/tools/`
2. Implement tool functions
3. Add error handling
4. Document usage
5. Add integration tests

### Modifying Workflow
1. Update `services/orchestration/graph.py`
2. Add/remove nodes and edges
3. Update state schema if needed
4. Test workflow end-to-end

## References

- [LangChain Documentation](https://python.langchain.com/)
- [LangGraph Documentation](https://langchain-ai.github.io/langgraph/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Kubernetes Python Client](https://github.com/kubernetes-client/python)