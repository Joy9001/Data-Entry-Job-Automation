# Data Entry Job Automation

This Python script automates the process of data entry for rental properties in San Francisco, CA from Zillow to a Google Form. It uses web scraping techniques to extract property information from Zillow and then fills out the corresponding fields in a Google Form.

## Prerequisites

- Python 3.x
- Selenium
- BeautifulSoup
- Requests
- Chrome WebDriver

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/data-entry-automation.git
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Set up the Google Form link:

    - Replace `os.environ.get("GFORM")` with the actual Google Form link in the `main.py` file.

4. Run the script:

    ```bash
    python main.py
    ```

## How it works

1. The script sends a GET request to Zillow's rental listings page in San Francisco, CA and retrieves the HTML response.

2. It uses BeautifulSoup to parse the HTML and extract the addresses, prices, and links of the rental properties.

3. The script then uses Selenium to automate the process of filling out the Google Form.

4. For each rental property, it enters the address, price, and link into the corresponding fields in the Google Form and submits the form.

5. The script repeats this process for all the rental properties extracted from Zillow.

