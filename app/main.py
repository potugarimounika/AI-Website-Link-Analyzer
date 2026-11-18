from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field, HttpUrl
from typing import List, Optional
from app.scraper import fetch_website
from app.analyzer import analyze_website

app = FastAPI(
    title="AI Website Link Analyzer",
    description="Analyzes a public website for competitors, search queries, SEO, services, and target audience.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Restrict this list before production deployment.
    allow_credentials=False,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

class AnalyzeRequest(BaseModel):
    url: HttpUrl = Field(..., description="Public website URL to analyze")

class Competitor(BaseModel):
    name: str
    website: str
    strengths: List[str]
    weaknesses: List[str]

class SearchQueries(BaseModel):
    google: List[str]
    facebook: List[str]
    instagram: List[str]
    linkedin: List[str]
    x: List[str]

class SEOAnalysis(BaseModel):
    suggested_keywords: List[str]
    seo_title: str
    meta_description: str
    content_improvements: List[str]

class Service(BaseModel):
    name: str
    description: str

class TargetAudience(BaseModel):
    customer_segments: List[str]
    industries: List[str]
    needs: List[str]

class AnalysisResponse(BaseModel):
    analyzed_url: str
    website_title: str
    website_summary: str
    competitors: List[Competitor]
    target_search_queries: SearchQueries
    seo_improvements: SEOAnalysis
    top_services: List[Service]
    target_audience: TargetAudience
    disclaimer: str

@app.get("/")
def home():
    return {"message": "AI Website Link Analyzer is running", "docs": "/docs"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/analyze", response_model=AnalysisResponse)
async def analyze(request: AnalyzeRequest):
    url = str(request.url)
    try:
        website_data = await fetch_website(url)
        result = await analyze_website(url, website_data)
        return result
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc))
    except RuntimeError as exc:
        raise HTTPException(status_code=502, detail=str(exc))
    except Exception:
        raise HTTPException(status_code=500, detail="Analysis failed. Check server logs and configuration.")
