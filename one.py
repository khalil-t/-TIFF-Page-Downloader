import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Chemin vers chromedriver.exe
chrome_driver_path = os.path.join(os.getcwd(), "chromedriver.exe")

# URL du livre
base_url = ""

# Configuration Chrome
options = webdriver.ChromeOptions()
options.add_argument("--headless")
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=options)

def download_tiff(page_number):
    try:
        driver.get(f"{base_url}&seq={page_number}")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "img")))

        folder = f"page_{page_number}"
        os.makedirs(folder, exist_ok=True)

        image_url = f""
        response = requests.get(image_url, stream=True)

        if response.status_code == 200:
            file_path = os.path.join(folder, f"page_{page_number}.tif")
            with open(file_path, "wb") as file:
                for chunk in response.iter_content(1024):
                    file.write(chunk)
            print(f"[✔] Page {page_number} téléchargée")
        else:
            print(f"[❌] Page {page_number} introuvable")

    except Exception as e:
        print(f"[⚠️] Erreur pour la page {page_number} : {e}")

for page in range(211, 229):
    download_tiff(page)
    time.sleep(2)

driver.quit()
print("✅ Tous les fichiers TIFF ont été téléchargés avec succès")

