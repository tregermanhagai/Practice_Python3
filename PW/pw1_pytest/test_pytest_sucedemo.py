import pytest  # Import pytest for fixtures, markers, and test discovery.
from playwright.sync_api import expect  # Import Playwright expect assertions for UI validation.


@pytest.fixture
def setup_teardown(page):  # Define setup and teardown steps using Playwright's page fixture.
    page.goto("https://www.saucedemo.com/")  # Open the SauceDemo login page.
    page.fill("#user-name", "standard_user")  # Type the username into the username field.
    page.fill("#password", "secret_sauce")  # Type the password into the password field.
    page.click("#login-button")  # Submit login credentials by clicking the login button.
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")  # Verify login success by checking the inventory URL.
    yield  # Hand control to the test, then continue after the test finishes: close the browser page.

def test_sanity_saucedemo(setup_teardown, page):  # Define the sanity scenario using fixture dependencies.
    print("Running sanity test example.")  # Print a log message indicating test execution started.
    page.click("text=Sauce Labs Bolt T-Shirt")  # Open product details by clicking the product name.
    expect(page.locator(".inventory_details_desc")).to_be_visible()  # Verify the product description element exists.
    expect(page.locator(".inventory_details_price")).to_be_visible()  # Verify the product price element exists.
    page.click("text=Add to cart")  # Add the product to the cart.
    expect(page.locator(".shopping_cart_badge")).to_have_text("1")  # Verify the cart badge count is 1.
    page.click("text=Remove")  # Remove the product from the cart.
    expect(page.locator(".shopping_cart_badge")).not_to_be_visible()  # Verify the cart badge disappears after removal.

