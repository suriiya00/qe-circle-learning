
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


def test_inventory_has_six_products(page: Page):
    login(page)

    expect(
        page.locator(".inventory_item")
    ).to_have_count(6)


def test_product_prices_are_visible(page: Page):
    login(page)

    prices = page.locator(".inventory_item_price")
    expect(prices).to_have_count(6)

    for index in range(prices.count()):
        expect(prices.nth(index)).to_be_visible()


def test_sort_products_by_price_low_to_high(page: Page):
    login(page)

    page.locator(".product_sort_container").select_option("lohi")

    prices = page.locator(".inventory_item_price").all_text_contents()
    numeric_prices = [
        float(price.replace("$", "")) for price in prices
    ]

    assert numeric_prices == sorted(numeric_prices)


def test_sort_products_by_price_high_to_low(page: Page):
    login(page)

    page.locator(".product_sort_container").select_option("hilo")

    prices = page.locator(".inventory_item_price").all_text_contents()
    numeric_prices = [
        float(price.replace("$", "")) for price in prices
    ]

    assert numeric_prices == sorted(numeric_prices, reverse=True)


def test_inventory_product_images_are_visible(page: Page):
    login(page)

    images = page.locator(".inventory_item_img img")
    expect(images).to_have_count(6)

    for index in range(images.count()):
        expect(images.nth(index)).to_be_visible()
