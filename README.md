# AI-Powered Website Link Analysis API

A Python FastAPI application that accepts a public website URL, extracts available page content, and uses Google Gemini to generate an AI-powered website analysis.

## Features

The API generates:

1. **Website Summary:** Website title and summary.
2. **Competitor Analysis:** Up to 3 competitor suggestions with strengths and weaknesses.
3. **Target Search Queries:** Five suggested queries each for Google, Facebook, Instagram, LinkedIn, and X.
4. **SEO Recommendations:** Suggested keywords, SEO title, meta description, and content improvements.
5. **Top Services:** Up to 5 suggested services.
6. **Target Audience:** Customer segments, industries, and customer needs.

> AI-generated recommendations are advisory. Competitors, services, and audience assumptions should be independently verified.

## Technologies Used

- Python 3.10+
- FastAPI
- Google Gemini API
- Google Gen AI Python SDK
- HTTPX
- BeautifulSoup
- Pydantic
- Pytest

## Requirements

- Python 3.10 or later
- Git
- A GitHub account
- A Google Gemini API key

## Project Structure

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
├── README.md
└── MODEL_COMPARISON_TEMPLATE.md
```

## Setup on Windows

Open the project folder in VS Code and open its PowerShell terminal.

Create a virtual environment:

```powershell
py -m venv .venv
```

Activate it:

```powershell
.venv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Create your environment file:

```powershell
Copy-Item .env.example .env
```

Open `.env` and add your Gemini API key using the variable name specified in `.env.example`.

**Security:** Never upload `.env` or expose your API key in GitHub, screenshots, or API responses.

If PowerShell blocks virtual environment activation, run:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
```

Then activate the environment again.

## Run the API

From the project directory, run:

```powershell
python -m uvicorn app.main:app --reload
```

Open these URLs in your browser:

- API home: http://127.0.0.1:8000/
- Swagger UI: http://127.0.0.1:8000/docs
- Health check: http://127.0.0.1:8000/health

## Test the API

Open Swagger UI:

http://127.0.0.1:8000/docs

1. Expand `POST /analyze`.
2. Click **Try it out**.
3. Enter the following request:

```json
{
  "url": "https://example.com"
}
```

4. Click **Execute**.

The API returns a structured JSON response containing the website analysis and benchmark information.

### PowerShell alternative

```powershell
Invoke-RestMethod -Method Post `
  -Uri "http://127.0.0.1:8000/analyze" `
  -ContentType "application/json" `
  -Body '{"url":"https://example.com"}'
```

## Run Tests

Run the test suite:

```powershell
python -m pytest -v
```

The current tests verify URL validation, including rejection of invalid URL schemes and localhost addresses.

**Latest test result:** 2 tests passed.

## API Contract

**Endpoint:** `POST /analyze`

Request:

```json
{
  "url": "https://example.com"
}
```

The response contains:

- `analyzed_url`
- `website_title`
- `website_summary`
- `competitors`
- `target_search_queries`
- `seo_improvements`
- `top_services`
- `target_audience`
- `disclaimer`
- `benchmark`

The benchmark records the configured provider, model, response time, token usage, and JSON validity.

## LLM Comparison

The current application uses Google Gemini through the official Google Gen AI Python SDK.

### Actual Gemini test record

| Metric | Recorded result |
|---|---|
| Model ID configured | gemini-3.5-flash |
| Test date | 18 November 2026 |
| Website | https://www.amazon.in/ |
| Response time | 26.716239 seconds |
| Input tokens | 410 |
| Output tokens | 1,129 |
| Total tokens reported | 2,878 |
| Valid JSON | Yes |

**Comparison limitations:**

- Gemini was tested through the application.
- OpenAI and Anthropic Claude were not tested.
- Their performance, response times, token usage, and JSON validity are therefore not available.
- No comparative accuracy or completeness scores are claimed.
- Pricing should be checked against current official provider documentation before calculating costs.

See `MODEL_COMPARISON_TEMPLATE.md` for the comparison record and methodology.

Official pricing references:

- OpenAI: https://developers.openai.com/api/docs/pricing
- Google Gemini: https://ai.google.dev/gemini-api/docs/pricing
- Anthropic: https://platform.claude.com/docs/en/about-claude/pricing

## Design Decisions and Limitations

- HTTPX is used to retrieve website HTML.
- BeautifulSoup extracts available page text, titles, headings, metadata, and links.
- JavaScript-rendered content may not be available through basic HTML scraping.
- Some websites block automated requests or require login.
- AI-generated competitor and audience suggestions may require manual verification.
- Public URL validation helps block private and local network destinations. Production deployment requires additional protections against DNS rebinding and unsafe redirects.
- The API is configured for local assessment use. CORS, authentication, rate limiting, and outbound network restrictions should be strengthened before production deployment.

## GitHub Repository

Repository:

https://github.com/potugarimounika/AI-Website-Link-Analyzer

The project source code and comparison document are maintained in this repository.

## Submission Checklist

- [x] FastAPI application implemented.
- [x] Gemini integration completed.
- [x] Website analysis endpoint tested.
- [x] Structured JSON response received.
- [x] Basic URL validation tests passed.
- [x] LLM comparison document prepared.
- [x] Code pushed to GitHub.
- [ ] Review README and sample response.
- [ ] Capture final API and test screenshots.
- [ ] Verify repository contents and ensure `.env` is not public.
- [ ] Submit the GitHub repository link to the assessment team.