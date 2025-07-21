import os
import json
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
import smtplib
from email.mime.text import MIMEText
import schedule
import time
import datetime

def driver_settings():
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36")
    options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)
    return driver

def saving_settings(sending_email, sending_email_password, receiving_email, time_for_alert):
    settings_data = {
        "sending_email": sending_email,
        "sending_email_password": sending_email_password,
        "receiving_email": receiving_email,
        "alert_time": time_for_alert,
    }
    with open("lib/settings.json", "w") as json_file:
        json.dump(settings_data, json_file, indent=4)
    print("Data saved in the lib/settings.json file")
    return print("Run Again! please")

def reading_settings():
    with open("lib/settings.json", "r") as json_file:
        settings_data = json.load(json_file)
    sending_email = settings_data["sending_email"]
    sending_email_password = settings_data["sending_email_password"]
    receiving_email = settings_data["receiving_email"]
    time_for_alert = settings_data["alert_time"]
    return sending_email, sending_email_password, receiving_email, time_for_alert

def grabing_content():
    news_found = []
    print("Scraping Website")
    driver = driver_settings()
    driver.get("https://www.aljazeera.com/news/")
    WebDriverWait(driver, 10).until(lambda d: d.find_elements(By.CLASS_NAME, "u-clickable-card__link"))
    links = driver.find_elements(By.CLASS_NAME, "u-clickable-card__link")
    for link in links:
        news_found.append({
            "header": link.text,
            "link": link.get_attribute('href'),
        })
    driver.quit()
    sending_emails(news_found)

def sending_emails(news_found):
    sending_email, sending_email_password, receiving_email,*_ = reading_settings()
    email_body = ""
    for news in news_found:
        email_body += f"📰 {news['header']}\n🔗 {news['link']}\n\n"
    sender_email = sending_email
    app_password = sending_email_password
    receiver_email = receiving_email
    subject = "News Alert"
    body = email_body
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = receiver_email
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login(sender_email, app_password)
            server.send_message(msg)
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")
    print(email_body)

if __name__ == '__main__':
    if os.path.isfile("lib/settings.json"):
        print("File Found in lib/settings.json")
        *_, time_for_alert = reading_settings()
        print(time_for_alert)
        schedule.every().day.at(time_for_alert).do(grabing_content)
        while True:
            schedule.run_pending()
            time.sleep(1)
    else:
        sending_email = input('Lets Set it up First! Settings:\n[+] Enter Email to send from: ')
        sending_email_password = input('[+] Sending email password: ')
        receiving_email = input('[+] Enter the email to receive the alerts: ')
        time_for_alert = input('[+] Enter time for alerts 24 hour example: 09:00:00 or 14:40:00: ')
        saving_settings(sending_email, sending_email_password, receiving_email, time_for_alert)
