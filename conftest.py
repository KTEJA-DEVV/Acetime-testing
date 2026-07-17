from config.browser_config import Browser_config
from playwright.sync_api import sync_playwright
import pytest
@pytest.fixture(scope='session')
def playwright_instance():
    pw = sync_playwright().start()
    yield pw
    pw.stop()
def pytest_addoption(parser):
    parser.addoption("--test-browser", action="store", default=None)

@pytest.fixture(scope="session")
def browser(request,playwright_instance):
    browser_name = request.config.getoption("--test-browser") or Browser_config['default_browser']
    if browser_name == "firefox":
        browser= playwright_instance.firefox.launch(headless=Browser_config['headless'],args=[
        '--use-fake-device-for-media-stream',
        '--use-fake-ui-for-media-stream',
    ])
    elif browser_name == "webkit":
        browser=playwright_instance.webkit.launch(headless=Browser_config['headless'],args=[
        '--use-fake-device-for-media-stream',
        '--use-fake-ui-for-media-stream',
    ])
    else:
        browser = playwright_instance.chromium.launch(headless=Browser_config['headless'],args=[
        '--use-fake-device-for-media-stream',
        '--use-fake-ui-for-media-stream',
    ])

    yield browser
    browser.close()

@pytest.fixture
def api_request(playwright_instance):
    request = playwright_instance.request.new_context(
        base_url=Browser_config['base_url']
    )
    yield request
    request.dispose()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if page:
            page.screenshot(path=f"{item.name}_failure.png")


