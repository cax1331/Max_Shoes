# Shoe E-Shop UI Automation (Selenium + pytest)

This project automates UI testing for a fictional shoe e-commerce website inspired by nike.com, using Python, Selenium WebDriver, and pytest. It simulates key user interactions like searching for products, adding them to the cart, and proceeding to checkout.

## What Does It Test?

- Product Search – Searches for a specific shoe model.
- Add to Cart – Selects the first search result and adds it to the cart.
- Cart Verification – Validates that the product appears in the cart.
- Checkout Page Access – Simulates proceeding to checkout and verifies that the page is displayed.

## Technologies Used

- Python 3
- Selenium WebDriver
- pytest
- ChromeDriver
- Page Object Model (POM)

## Project Structure

qa-eshop-tests/
├── main.py                # Test class and page object logic
├── configuration.py       # Base URL, timeouts, browser settings
├── data.py                # Test data (search terms, dummy card, user info)
├── README.txt             # Project description and instructions

## How to Run the Tests

1. Install dependencies:
   pip install selenium pytest

2. Download ChromeDriver:
   https://sites.google.com/chromium.org/driver/
   Add it to your system PATH or specify its location in setup_class() in main.py

3. Run the tests:
   pytest main.py

4. Optional – Run with minimal output:
   pytest main.py -q


