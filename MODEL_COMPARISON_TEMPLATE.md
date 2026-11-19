# LLM Comparison Record

**Comparison date:** 19 November 2026  
**Website tested:** https://www.amazon.in/  
**Test method:** One website-analysis API request. Only Google Gemini was tested in this project.

## 1. Performance comparison

| Metric | OpenAI | Google Gemini | Anthropic Claude |
|---|---|---|---|
| Exact model ID | gpt-6-luna | gemini-3.5-flash | claude-sonnet-5-5 |
| Test date | Not tested | 18 November 2026 | Not tested |
| Response time | Not tested | 26.716239 seconds | Not tested |
| Input tokens | Not tested | 410 | Not tested |
| Output tokens | Not tested | 1,129 | Not tested |
| Cost for this run | Not measured | Approximately $0.010776* | Not measured |
| Valid JSON? | Not tested | Yes | Not tested |
| Correctness score (1–5) | Not evaluated | Not independently evaluated | Not evaluated |
| Completeness score (1–5) | Not evaluated | Not independently evaluated | Not evaluated |
| Final notes | No API test performed | Successfully returned the expected JSON structure | No API test performed |

*Gemini cost is a provisional paid-tier estimate using reported input/output token counts. Actual billing may differ because the reported total token count (2,878) does not equal input plus output tokens (1,539). Thinking-token usage and account tier should be checked before treating this as an actual charge.

## 2. Official model pricing and specifications

Prices are USD per million tokens.

| Provider | Model | Input price | Output price | Context window |
|---|---|---:|---:|---|
| OpenAI | GPT-6 Luna | $0.10 | $0.50 | 1.05M tokens |
| Google | Gemini 3.5 Flash | $1.50 | $9.00 | Not independently verified here |
| Anthropic | Claude Sonnet 5.5 | $2.00 | $10.00 | 1M tokens |

These are published standard API rates, not measured costs for the three providers.

## 3. Gemini cost estimate

Input cost:

410 × $1.50 / 1,000,000 = $0.000615

Output cost:

1,129 × $9.00 / 1,000,000 = $0.010161

Estimated total:

**$0.010776 USD**

This is an estimate based on reported token counts and paid-tier pricing, not a verified billing record.

## 4. Recommendation

Google Gemini 3.5 Flash is the provisional recommendation for this project because it is already integrated into the application and successfully generated the required structured JSON response.

However, OpenAI and Claude have not been tested using the same prompt and website. Therefore, this project cannot claim that Gemini is more accurate, faster, or cheaper than those models based on actual performance.

A fair comparison requires testing all three models with the same URL, prompt, and output schema.

## 5. Limitations

- Only Gemini was tested through the project API.
- OpenAI and Claude performance measurements are unavailable.
- Correctness and completeness scores have not been independently evaluated.
- Amazon may restrict automated scraping or serve dynamically rendered content.
- Competitor, service, and audience suggestions require independent verification.
- Gemini token accounting needs further investigation before confirming the estimated cost.

## 6. Official references

- OpenAI pricing: https://developers.openai.com/api/docs/pricing
- OpenAI GPT-6 Luna: https://developers.openai.com/api/docs/models/gpt-6-luna
- Gemini pricing: https://ai.google.dev/gemini-api/docs/pricing
- Gemini models: https://ai.google.dev/gemini-api/docs/models
- Anthropic pricing: https://platform.claude.com/docs/en/about-claude/pricing
- Claude models: https://platform.claude.com/docs/en/models/overview