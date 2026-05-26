import pytest


pytest.mark.recommend
@pytest.fixture(scope="function")
def setup_teardown(page):
    print("\nSetting up resources before tests run.")
    page.goto("https://sv-students-recommend.onrender.com/pages/login.html")
    page.fill("#email", "hagai@svcollege.co.il")
    page.fill("#password", "test1234")
    page.click('[data-test="btn-login"]')
    yield
    print("\nTearing down resources after tests have completed.")
    
def test_recommend(setup_teardown, page):
    # Open Add Recommendation page first (adjust to your app flow)
    page.click("[data-test='nav-signup-recommendations']")
    # Select category = Book from the <select data-test="select-category">
    page.select_option('[data-test="select-category"]', value="Book")
    # You can also do: label="Book"

    # Type recommendation name
    page.fill('input[name="recommendationName"]', "The Bronze Horseman")

    # Upload image file for the recommendation.
    page.set_input_files('[data-test="input-image"]', r'c:\1.jpg')
