# Nike Shoes Scraper

This project is a web scraping script designed to extract data about men's shoes from the Nike website. The script uses `requests` and `BeautifulSoup` to fetch and parse the webpage content, and then extracts specific information about each shoe. The extracted data is saved in a JSON file.

## Features

-   Extracts title, subtitle, price, and image URL of men's shoes.
-   Handles exceptions during the data extraction process.
-   Outputs the data to a JSON file.

## Requirements

-   Python 3.x
-   `requests` library
-   `beautifulsoup4` library
-   `pandas` library (optional, if you want to further manipulate data)

## Installation

1. Clone the repository:

    ```python
    git clone https://github.com/yourusername/nike-shoes-scraper.git
    ```

2. Navigate to the project directory:

    ```python
    cd nike-shoes-scraper
    ```

3. Install the required libraries:

    ```python
    pip install requests beautifulsoup4 pandas
    ```

# Usage

-   Run the script

    ```python
    python nike_scarping.py
    ```
