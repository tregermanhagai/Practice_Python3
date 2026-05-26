import pytest  # Import pytest for fixtures, markers, and test discovery.
from playwright.sync_api import expect  # Import Playwright expect assertions for UI validation.


@pytest.fixture
def setup_teardown(page):  # Define setup and teardown steps using Playwright's page fixture.
    page.goto("https://automationexercise.com/login")  # Open the Automation Exercise login page.
    page.fill("[name='email']", "hagai.tregerman@gmail.com")  # Type the username into the username field.
    page.fill("[name='password']", "KMsuTYNyY@Q5y")  # Type the password into the password field.
    page.click("text='Login'")  # Submit login credentials by clicking the login button.
    expect(page.locator("[href='/logout']")).to_be_visible()  # Verify login success by checking for a specific element that appears after login.
    yield  # Hand control to the test, then continue after the test finishes: close the browser page.

def test_sanity_automationexercise(setup_teardown, page):  # Define the sanity scenario using fixture dependencies.
    print("Running sanity test example.")  # Print a log message indicating test execution started.
    page.click("[href='/products']")  # Open product details by clicking the product name.
    page.fill("[id='search_product']", "T-Shirt")  # Type the product name into the search field.
    page.click("#submit_search")  # Open product details by clicking the product name.
    expect(page.locator("h2.title.text-center", has_text="Searched Products")).to_be_visible()
