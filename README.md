# AI-Powered Website Link Analysis API

A Python FastAPI project that accepts a public website URL, extracts visible page content, and uses Google Gemini to generate:
1. Competitor suggestions (up to 3), with strengths and weaknesses
2. Five target search queries each for Google, Facebook, Instagram, LinkedIn, and X
3. SEO recommendations (keywords, title, meta description, content improvements)
4. The website's top five services
5. Likely target audience segments, industries, and needs

> AI output is advisory. Competitors and audience assumptions must be independently verified.

## Requirements
- Python 3.10+
- Git and a GitHub account
- A Gemini API key

## Setup on Windows (VS Code terminal / PowerShell)

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
Copy-Item .env.example .env
```

Open `.env` and replace the placeholder with your own Gemini API key. Never commit `.env`.

If PowerShell blocks activation, run this in the current terminal:
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.venv\Scripts\Activate.ps1
```

## Run the API

```powershell
uvicorn app.main:app --reload
```

Open:
- API home: http://127.0.0.1:8000/
- Swagger UI: http://127.0.0.1:8000/docs
- Health check: http://127.0.0.1:8000/health

## Test the endpoint

In Swagger UI:
1. Expand `POST /analyze`
2. Click **Try it out**
3. Enter a public website URL, for example:

```json
{
  "url": "https://example.com"
}
```

4. Click **Execute**. A successful response contains all five analysis sections.

PowerShell alternative:
```powershell
Invoke-RestMethod -Method Post `
  -Uri "http://127.0.0.1:8000/analyze" `
  -ContentType "application/json" `
  -Body '{"url":"https://example.com"}'
```

## Run tests

```powershell
pytest -v
```

The included tests check URL validation. Add more tests for successful scraping, provider failures, and response-schema validation before production use.

## Project structure

```text
website_link_analyzer/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── scraper.py
│   └── analyzer.py
├── tests/
│   └── test_scraper_helpers.py
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## API contract

`POST /analyze`

Request:
```json
{"url": "https://example.com"}
```

Response keys:
- `analyzed_url`
- `website_title`
- `website_summary`
- `competitors`
- `target_search_queries`
- `seo_improvements`
- `top_services`
- `target_audience`
- `disclaimer`

## LLM comparison notes

The project currently uses Gemini through the official Google Gen AI Python SDK. For the assessment's model-comparison section, compare the same prompt and same website input across at least three models (for example, OpenAI, Gemini, and Claude). Record the date, exact model ID, input/output token usage if available, measured response time, API price from each provider's current pricing page, JSON validity, and a human-reviewed quality score. Do not copy old prices: provider prices and model names change.

Suggested evaluation rubric (score each 1–5):
- Correctness and relevance
- Completeness of the five requested sections
- Valid JSON / schema compliance
- Response latency
- Cost for the same input and output size

Choose a winner based on measured results, not brand preference. The code uses Gemini as the default implementation; you can adapt `app/analyzer.py` to another provider if your comparison supports that choice.

## Design decisions and limitations

- Uses HTTPX and BeautifulSoup to retrieve and parse server-rendered HTML.
- JavaScript-rendered content may not appear in the extracted text.
- The AI may suggest competitors that need manual verification.
- Some sites block automated requests or require login; those cannot be analyzed by this basic scraper.
- Public URL validation blocks obvious private/local destinations. For a production deployment, add DNS-rebinding-safe outbound network controls, request-size limits, rate limiting, authentication, and stricter redirect validation.
- CORS is open for local assessment convenience; restrict allowed origins before production.
- Never expose your API key in source code, screenshots, GitHub, or API responses.

## GitHub upload

Create an empty public repository on GitHub named `ai-website-link-analyzer`.

Then, from the project folder:

```powershell
git init
git add .
git commit -m "Build AI website link analysis API"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/ai-website-link-analyzer.git
git push -u origin main
```

Replace `YOUR-USERNAME` with your GitHub username. Do not paste a real API key into README or source files.

## Before submitting

- [ ] Install dependencies successfully
- [ ] Add a valid key to local `.env`
- [ ] Start the server
- [ ] Confirm `/health` returns `{"status":"ok"}`
- [ ] Test `/analyze` with a public website
- [ ] Run `pytest -v`
- [ ] Review the AI output for unsupported claims
- [ ] Complete the model comparison with current measured data
- [ ] Check `git status` and ensure `.env` is not staged
- [ ] Push the repository and open its GitHub URL in a private/incognito window
