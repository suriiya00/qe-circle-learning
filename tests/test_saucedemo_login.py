
from playwright.sync_api import Page, expect

BASE_URL = "https://www.saucedemo.com/"
PASSWORD = "secret_sauce"


def test_login_page_elements_visible(page: Page):
    page.goto(BASE_URL)

    expect(page.locator("#user-name")).to_be_visible()
    expect(page.locator("#password")).to_be_visible()
    expect(page.locator("#login-button")).to_be_visible()


def test_valid_login(page: Page):
    page.goto(BASE_URL)

    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill(PASSWORD)
    page.locator("#login-button").click()

    expect(page).to_have_url(
        "https://www.saucedemo.com/inventory.html"
    )
    expect(
        page.get_by_text("Products", exact=True)
    ).to_be_visible()


def test_invalid_password(page: Page):
    page.goto(BASE_URL)

    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("wrong_password")
    page.locator("#login-button").click()

    expect(page.locator("[data-test='error']")).to_contain_text(
        "Username and password do not match"
    )


def test_empty_username(page: Page):
    page.goto(BASE_URL)

    page.locator("#password").fill(PASSWORD)
    page.locator("#login-button").click()

    expect(page.locator("[data-test='error']")).to_contain_text(
        "Username is required"
    )


def test_locked_out_user(page: Page):
    page.goto(BASE_URL)

    page.locator("#user-name").fill("locked_out_user")
    page.locator("#password").fill(PASSWORD)
    page.locator("#login-button").click()

    expect(page.locator("[data-test='error']")).to_contain_text(
        "Sorry, this user has been locked out"
    )
