
import re
from playwright.sync_api import Page, expect


def test_homepage_title(page: Page):
    page.goto("https://playwright.dev/")
    expect(page).to_have_title(re.compile("Playwright"))


def test_get_started_navigation(page: Page):
    page.goto("https://playwright.dev/")
    page.get_by_role("link", name="Get started").click()
    expect(
        page.get_by_role("heading", name="Installation")
    ).to_be_visible()


def test_get_started_link_is_visible(page: Page):
    page.goto("https://playwright.dev/")
    expect(
        page.get_by_role("link", name="Get started")
    ).to_be_visible()
