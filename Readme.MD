# AceTime Test Automation Framework

![Tests](https://github.com/KTEJA-DEVV/Acetime-testing/actions/workflows/tests.yml/badge.svg)

End-to-end and API test automation for [AceTime](https://ace-time.onrender.com), a WebRTC video-calling web app, built with **Playwright (Python)** and **Pytest**, wired into a **3-job GitHub Actions CI/CD pipeline**.

## Tech Stack

- **Playwright (sync API)** — browser automation and API request testing
- **Pytest** — test runner, fixtures, markers
- **pytest-html** — self-contained HTML test reports
- **GitHub Actions** — CI/CD pipeline (API, UI, and E2E jobs)
- **python-dotenv** — environment-based configuration

## Project Structure

```
ACETIME/
├── .github/workflows/tests.yml   # CI pipeline: api-tests, ui-tests, e2e-tests
├── config/browser_config.py      # Env-driven browser/base_url config
├── src/
│   ├── api/                      # API request wrappers (auth, calls, signin, signup)
│   ├── pages/                    # Page Object Model classes
│   └── utils/data_generator.py   # Faker-based test data generation
├── test_data/users.json          # Static test fixtures
├── tests/
│   ├── api/                      # API-layer tests
│   ├── ui/                       # UI-layer tests
│   ├── e2e/                      # Combined UI + API flow tests
│   └── conftest.py               # Function-scoped fixtures (context, page, base_url)
├── conftest.py                   # Session-scoped fixtures (browser, playwright, hooks)
├── pytest.ini
└── requirements.txt
```

## Architecture Notes

- **Page Object Model** — one class per page (`LoginPage`, `DashboardPage`, `CallsPage`, `SignupPage`), keeping locators and page interactions out of test files.
- **Two-tier `conftest.py`** — session-scoped infrastructure (browser lifecycle, Playwright instance, auto-screenshot-on-failure hook) lives in the root; function-scoped, per-test objects (`context`, `page`) live in `tests/conftest.py`.
- **Environment-based config** — `browser_config.py` reads `BASE_URL`, `BROWSER_HEADLESS`, and `DEFAULT_BROWSER` from environment variables (via `.env` locally, GitHub Secrets/workflow `env` in CI), so no environment-specific values are hardcoded in source.
- **Token-injection login for API/E2E setup** — `AuthAPI` bypasses the UI login form by writing JWT tokens directly into `localStorage` and reloading, which is faster and more reliable for tests that don't need to verify the login form itself.

## Running Tests Locally

```bash
pip install -r requirements.txt
playwright install --with-deps chromium

pytest -m api    # API tests only
pytest -m ui     # UI tests only
pytest -m e2e    # End-to-end tests only
```

Copy `.env.example` to `.env` and adjust values as needed (e.g., set `BROWSER_HEADLESS=false` to watch the browser locally).

## CI/CD Pipeline

Three jobs run on every push/PR to `main` or `develop`:

| Job | Scope | Runs |
|---|---|---|
| `api-tests` | API-only tests | in parallel |
| `ui-tests` | UI-only tests | in parallel |
| `e2e-tests` | Combined UI + API flows | after both above succeed |

Each job installs dependencies, installs Playwright's Chromium browser, runs its test subset, and uploads a self-contained HTML report as a build artifact — plus failure screenshots for UI/E2E jobs.

## Challenges Solved While Building This Pipeline

Real issues hit and fixed while wiring this up for the first time — kept here as a debugging log / interview reference:

1. **Invalid dependency pin** — `requirements.txt` had a non-existent `python-dotenv` version; CI's clean install caught it immediately where a local environment with the package already installed wouldn't have.
2. **Ubuntu 24.04 / Playwright ABI mismatch** — an older pinned Playwright version referenced the pre-24.04 package name `libasound2`, which Ubuntu renamed to `libasound2t64`. Fixed by upgrading Playwright to a version with an updated dependency installer.
3. **Silent empty-string env var** — a missing `BASE_URL` GitHub Secret didn't cause a "variable not set" error; it resolved to an empty string, which bypassed the code's fallback default and produced a confusing "Invalid URL" error deep in Playwright's API request layer.
4. **No real camera hardware in CI** — WebRTC call tests granted camera/mic *permissions* correctly, but headless CI runners have no physical camera device to actually stream from. Fixed with Chromium's `--use-fake-device-for-media-stream` / `--use-fake-ui-for-media-stream` launch flags.
5. **First-visit onboarding state** — a "Skip" onboarding button only appears for genuinely new sessions. Local runs (with browser history) never hit it; a completely fresh CI browser context always did. Fixed by treating the button as optional (`expect(...).to_be_visible(timeout=...)` + try/except) instead of assuming it either always or never appears.

## Notes

- Tests targeting a Render free-tier deployment account for cold-start latency via a session-scoped warm-up fixture.
- Screenshots are captured automatically on any UI test failure via a `pytest_runtest_makereport` hook.