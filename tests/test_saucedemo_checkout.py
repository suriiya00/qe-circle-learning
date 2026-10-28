
from playwright.sync_api import Page, expect

BASE_URL = "https://www.saucedemo.com/"
USERNAME = "standard_user"
PASSWORD = "secret_sauce"


def login(page: Page):
    page.goto(BASE_URL)
    page.locator("#user-name").fill(USERNAME)
    page.locator("#password").fill(PASSWORD)
    page.locator("#login-button").click()

    expect(page).to_have_url(
        "https://www.saucedemo.com/inventory.html"
    )


def test_product_list_visible(page: Page):
    login(page)

    expect(
        page.get_by_text("Sauce Labs Backpack", exact=True)
    ).to_be_visible()


def test_add_product_to_cart(page: Page):
    login(page)

    page.get_by_role(
        "button", name="Add to cart"
    ).first.click()

    expect(
        page.locator(".shopping_cart_badge")
    ).to_have_text("1")


def test_remove_product_from_cart(page: Page):
    login(page)

    page.get_by_role("button", name="Add to cart").first.click()

    # Click the shopping cart link using its CSS class
    page.locator(".shopping_cart_link").click()

    expect(
        page.get_by_text("Sauce Labs Backpack", exact=True)
    ).to_be_visible()

    page.get_by_role("button", name="Remove").click()

    expect(
        page.get_by_text("Sauce Labs Backpack", exact=True)
    ).to_have_count(0)

def test_checkout_form(page: Page):
    login(page)

    page.get_by_role(
        "button", name="Add to cart"
    ).first.click()

    # Click the shopping cart link using its CSS class
    page.locator(".shopping_cart_link").click()

    page.get_by_role("button", name="Checkout").click()

    expect(page).to_have_url(
        "https://www.saucedemo.com/checkout-step-one.html"
    )

    page.locator("#first-name").fill("Test")
    page.locator("#last-name").fill("User")
    page.locator("#postal-code").fill("560001")

    page.get_by_role("button", name="Continue").click()

    expect(page).to_have_url(
        "https://www.saucedemo.com/checkout-step-two.html"
    )
    expect(
        page.get_by_role("button", name="Finish")
    ).to_be_visible()


def test_complete_checkout(page: Page):
    login(page)

    page.get_by_role(
        "button", name="Add to cart"
    ).first.click()

    # Click the shopping cart link using its CSS class
    page.locator(".shopping_cart_link").click()


    page.get_by_role("button", name="Checkout").click()

    page.locator("#first-name").fill("Test")
    page.locator("#last-name").fill("User")
    page.locator("#postal-code").fill("560001")

    page.get_by_role("button", name="Continue").click()
    page.get_by_role("button", name="Finish").click()

    expect(
        page.get_by_text("Thank you for your order!")
    ).to_be_visible()
