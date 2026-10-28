
import re

from playwright.sync_api import Page, expect

BASE_URL = "https://playwright.dev/"


# TC01: Open homepage
def test_homepage_loads(page: Page):
    page.goto(BASE_URL)

    expect(page.locator("body")).to_be_visible()


# TC02: Verify page title
def test_homepage_title(page: Page):
    page.goto(BASE_URL)

    expect(page).to_have_title(re.compile("Playwright"))


# TC03: Click Get started
def test_get_started_navigation(page: Page):
    page.goto(BASE_URL)

    page.get_by_role("link", name="Get started").click()

    expect(page).to_have_url(
        re.compile(r"playwright\.dev/docs/intro/?$")
    )
    expect(
        page.get_by_role("heading", name="Installation")
    ).to_be_visible()


# TC04: Verify Get started link
def test_get_started_link_is_visible(page: Page):
    page.goto(BASE_URL)

    expect(
        page.get_by_role("link", name="Get started")
    ).to_be_visible()



# TC05: Navigate to an unavailable page
def test_unavailable_page_behavior(page: Page):
    response = page.goto(
        "https://playwright.dev/nonexistent-learning-test-page"
    )

    assert response is not None, "No HTTP response was received"
    assert response.status == 404, (
        f"Expected HTTP 404, received HTTP {response.status}"
    )