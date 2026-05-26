import pytest
from playwright.sync_api import expect


@pytest.mark.login
def test_logout_valid(page):
    # Open the success page where the user is considered logged in.
    page.goto("https://practicetestautomation.com/logged-in-successfully")
    # Click the "Log out" link/button to end the session.
    page.click("text=Log out")
    # Verify the browser is redirected back to the login page URL.
    expect(page).to_have_url("https://practicetestautomation.com/practice-test-login/")
    # Find the page subtitle/header shown on the login page.
    success_logout_header = page.locator("h2")
    # Confirm the subtitle/header text matches the expected login page text.
    expect(success_logout_header).to_have_text("Test login")


@pytest.mark.login
def test_login_valid(page):
    page.goto("https://practicetestautomation.com/practice-test-login/")
    page.fill("#username", "student")
    page.fill("#password", "Password123")
    page.click("#submit")
    expect(page).to_have_url("https://practicetestautomation.com/logged-in-successfully/")
    success_header = page.locator("h1")
    expect(success_header).to_have_text("Logged In Successfully")
    