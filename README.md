# 📘 TIFF Page Downloader (Web Scraper)

This Python script automates the download of `.tif` images (TIFF format) from a web-based viewer using Selenium and Requests. It navigates to each page of a digitized book or document and saves the image locally.

## 🚀 Features

- Uses `Selenium` to interact with a website that dynamically loads pages
- Downloads `.tif` images for a specified range of pages
- Automatically creates folders for each page
- Runs headlessly using Chrome in the background

## 📂 Project Structure
├── chromedriver.exe
├── script.py
└── page_<number>
└── page_<number>.tif


## 🧰 Requirements

- Python 3.x
- Google Chrome installed
- ChromeDriver (compatible with your Chrome version)

### Install dependencies
base_url = "https://example.com/viewer?docid=12345"
image_url = driver.find_element(By.TAG_NAME, "img").get_attribute("src")


```bash
pip install selenium requests


