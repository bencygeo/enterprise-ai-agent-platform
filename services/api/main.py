from fastapi import FastAPI, HTTPException
from fastapi.responses import Response
from pydantic import BaseModel
from typing import Dict, Any
import os
from services.orchestration.graph import build_graph

app = FastAPI(
    title="Enterprise AI DevOps Multi-Agent Platform",
    description="Production-oriented multi-agent AI platform for DevOps automation using agentic AI principles",
    version="1.0.0"
)

# Initialize graph
graph = build_graph()


@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    """Return empty favicon to prevent 404 errors"""
    return Response(status_code=204)


class QueryRequest(BaseModel):
    input: str
    
    class Config:
        json_schema_extra = {
            "example": {
                "input": "Pod crash-looping in production namespace"
            }
        }


class QueryResponse(BaseModel):
    plan: Any
    execution: Any
    result: Any


@app.get("/")
def root():
    """Root endpoint with API information"""
    return {
        "name": "Enterprise AI Agent Platform",
        "version": "1.0.0",
        "status": "running",
        "docs": "/docs"
    }


@app.get("/health")
def health_check():
    """Health check endpoint"""
    openai_key_set = bool(os.getenv("OPENAI_API_KEY"))
    return {
        "status": "healthy",
        "openai_configured": openai_key_set
    }


@app.post("/query", response_model=QueryResponse)
def process_query(request: QueryRequest):
    """
    Process a query through the agent workflow.
    
    The query will be processed by:
    1. Planner Agent - Creates investigation plan
    2. Executor Agent - Executes the plan
    3. Analysis Agent - Analyzes results and provides recommendations
    """
    try:
        result = graph.invoke({"input": request.input})
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Legacy endpoint for backward compatibility
@app.post("/incident")
def resolve_incident(input: str):
    """Legacy endpoint - use /query instead"""
    try:
        result = graph.invoke({"input": input})
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))