# Enterprise AI DevOps Multi-Agent Platform

A production-oriented multi-agent AI platform designed to automate DevOps incident analysis and resolution using agentic AI principles.

## 🚀 Overview
This project simulates an intelligent SRE system that can analyze infrastructure issues, plan resolution steps, execute diagnostic actions, and provide root-cause analysis with recommended fixes.

Unlike traditional chatbots, this platform uses a **multi-agent architecture** to break down complex operational problems into structured workflows, enabling scalable and reliable AI-driven decision-making.

## 🧠 Key Capabilities
- Multi-agent orchestration for complex problem solving
- Intelligent planning, execution, and analysis pipeline
- Simulation of real-world DevOps scenarios (e.g., Kubernetes failures)
- Modular architecture for extensibility and enterprise use

## 🧱 Architecture Overview

- **API Layer**: FastAPI for external interaction
- **Agent Orchestration**: LangGraph for workflow coordination
- **Agents**:
  - **Planner Agent**: Task decomposition and investigation planning
  - **Executor Agent**: Action simulation and diagnostic execution
  - **Analysis Agent**: Root cause analysis + resolution recommendations
- **Tools Layer**: Simulated infrastructure tools (logs, metrics, K8s operations)
- **Deployment Ready**: Designed for Kubernetes-based environments

### Directory Structure

```
enterprise-ai-agent-platform/
│
├── services/
│   ├── api/              # FastAPI REST endpoints
│   ├── agents/           # AI agent implementations
│   │   ├── planner_agent.py    # Task decomposition
│   │   ├── executor_agent.py   # Action execution
│   │   ├── analysis_agent.py   # Root cause analysis
│   │   └── router.py           # Query routing
│   ├── tools/            # Tool integrations (K8s, etc.)
│   └── orchestration/    # LangGraph workflow orchestration
│
├── infrastructure/
│   ├── docker/           # Docker configurations
│   └── k8s/              # Kubernetes manifests
│
├── observability/
│   ├── logging/          # Logging configuration
│   └── monitoring/       # Monitoring setup
│
├── docs/                 # Documentation
│   ├── architecture.md   # Detailed architecture
│   └── SETUP_GUIDE.md    # Setup instructions
├── tests/                # Test suite
└── requirements.txt      # Python dependencies
```

## 🎯 Use Cases
- **Kubernetes Incident Troubleshooting**: Automated analysis of pod failures, crashes, and resource issues
- **Automated Root Cause Analysis**: Multi-step investigation with intelligent reasoning
- **AI-Assisted DevOps/SRE Workflows**: Structured problem-solving for operational issues
- **Enterprise AI Platform Prototyping**: Foundation for building production-grade agentic systems

## 🔥 Why This Matters
This project demonstrates how **Agentic AI systems move beyond simple LLM responses** to structured, multi-step reasoning systems capable of solving real-world engineering problems.

Unlike traditional chatbots that provide single-turn responses, this platform:
- **Decomposes complex problems** into manageable investigation steps
- **Executes actions** through simulated or real tool integrations
- **Reasons about results** to identify root causes
- **Provides actionable recommendations** based on analysis

This architecture is production-ready and can be extended with:
- Real Kubernetes API integrations
- Cloud provider tools (AWS, GCP, Azure)
- Monitoring system integrations (Prometheus, Grafana)
- Ticketing system automation (Jira, ServiceNow)

## 🛠 Tech Stack

- **Python 3.9+**: Core programming language
- **FastAPI**: Modern, high-performance web framework
- **LangGraph**: Multi-agent workflow orchestration
- **LangChain**: LLM application framework
- **OpenAI GPT**: Language model for intelligent reasoning
- **Kubernetes Client**: Infrastructure integration (design-ready)
- **Uvicorn**: ASGI server for production deployment

## 📋 Prerequisites

- Python 3.9 or higher
- OpenAI API key (or Watsonx-ready for enterprise)
- Virtual environment (recommended)
- Git for version control

## 🚀 Quick Start

**Want to get started immediately?** Check out the [Quick Start Guide](QUICK_START.md) for a 5-minute setup!

## 📖 Detailed Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd enterprise-ai-agent-platform
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp .env.example .env
   ```
   
   Edit `.env` and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_actual_api_key_here
   ```

## Running the Application

1. **Start the API server**
   ```bash
   PYTHONPATH=. uvicorn services.api.main:app --reload
   ```

2. **Access the API**
   - API: http://127.0.0.1:8000
   - Interactive docs: http://127.0.0.1:8000/docs
   - Alternative docs: http://127.0.0.1:8000/redoc

## 🌐 API Endpoints

### Main Endpoints
- **POST /query** - Submit a query to the multi-agent system
  ```json
  {
    "input": "Pod crash-looping in production namespace"
  }
  ```
  
- **GET /health** - Health check and configuration status
- **GET /** - API information and documentation links

### Response Format
```json
{
  "plan": "Investigation plan from Planner Agent",
  "execution": "Execution results from Executor Agent",
  "result": "Root cause analysis and recommendations from Analysis Agent"
}
```

## Development

### Project Structure

- **services/agents/**: Contains individual agent implementations
  - `planner_agent.py` - Plans investigation steps
  - `executor_agent.py` - Executes planned steps
  - `analysis_agent.py` - Analyzes results
  - `router.py` - Routes queries to appropriate agents

- **services/orchestration/**: LangGraph workflow definitions
  - `graph.py` - Defines the agent workflow graph

- **services/tools/**: External tool integrations
  - `k8s_tools.py` - Kubernetes operations

### Adding New Agents

1. Create a new agent file in `services/agents/`
2. Implement the agent function following the existing pattern
3. Update `services/orchestration/graph.py` to include the new agent
4. Add necessary tools in `services/tools/`

### Running Tests

```bash
pytest tests/
```

## 🚀 Future Enhancements

### Short-term Roadmap
- [ ] **Tool-calling agents with real Kubernetes APIs**: Move from simulation to actual K8s cluster operations
- [ ] **Memory layer (Redis)**: Persistent state management for long-running investigations
- [ ] **Enhanced observability**: Distributed tracing with OpenTelemetry, structured logging
- [ ] **Authentication & Authorization**: Secure API access with JWT/OAuth2

### Medium-term Goals
- [ ] **Autonomous remediation workflows**: Self-healing capabilities for common issues
- [ ] **Multi-cloud support**: AWS, GCP, Azure integrations
- [ ] **Custom agent builder**: UI for creating domain-specific agents
- [ ] **Real-time notifications**: Slack, PagerDuty, email integrations

### Long-term Vision
- [ ] **Self-learning agents**: Continuous improvement from historical incidents
- [ ] **Predictive analysis**: Proactive issue detection before failures occur
- [ ] **Multi-tenancy**: Enterprise-grade isolation and resource management
- [ ] **Watsonx integration**: IBM enterprise AI platform support

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/amazing-feature`
3. **Make your changes**: Follow the existing code style and patterns
4. **Add tests**: Ensure your changes are well-tested
5. **Commit your changes**: `git commit -m 'Add amazing feature'`
6. **Push to the branch**: `git push origin feature/amazing-feature`
7. **Open a Pull Request**: Describe your changes and their benefits

### Development Guidelines
- Follow PEP 8 style guide for Python code
- Add docstrings to all functions and classes
- Write unit tests for new features
- Update documentation as needed
- Keep commits atomic and well-described

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support & Troubleshooting

### Common Issues

**Missing OpenAI API Key**
```bash
# Ensure .env file exists and contains your API key
cp .env.example .env
# Edit .env and add: OPENAI_API_KEY=your_key_here
```

**Import Errors**
```bash
# Always use PYTHONPATH=. when running the application
PYTHONPATH=. uvicorn services.api.main:app --reload
```

**Deprecated LangChain Warnings**
The code uses the latest LangChain packages (`langchain-openai`, `langchain-community`) to avoid deprecation warnings. If you still see warnings, update your packages:
```bash
pip install --upgrade langchain langchain-openai langchain-community
```

### Getting Help
- 📖 Read the [Setup Guide](docs/SETUP_GUIDE.md)
- 🏗️ Review the [Architecture Documentation](docs/architecture.md)
- 🐛 Open an issue on GitHub for bugs
- 💡 Start a discussion for feature requests

## 🌟 Acknowledgments

Built with:
- [LangChain](https://python.langchain.com/) - LLM application framework
- [LangGraph](https://langchain-ai.github.io/langgraph/) - Multi-agent orchestration
- [FastAPI](https://fastapi.tiangolo.com/) - Modern web framework
- [OpenAI](https://openai.com/) - GPT models

## 📧 Contact

For questions, suggestions, or collaboration opportunities, please open an issue or reach out through GitHub.

---

**⭐ If you find this project useful, please consider giving it a star!**