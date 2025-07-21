# News Alert Scraper

This script scrapes news headlines from Al Jazeera and sends them via email at a scheduled time.

## Prerequisites

Before you begin, ensure you have met the following requirements:

* You have installed Python 3.6 or later.
* You have a Windows/Linux/Mac machine.
* You have installed the required Python packages.
* You have a Gmail account for sending emails.

## Installing News Alert Scraper

To install the News Alert Scraper, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/Moe-Dahan/News-Alert.git

    Navigate to the project directory:

cd news-alert-scraper

Install the required packages:

    pip install -r requirements.txt

    Download and install geckodriver for Selenium to work with Firefox.

Using News Alert Scraper

To use the News Alert Scraper, follow these steps:

    Run the script:

    python main.py

    Follow the on-screen instructions to set up your email settings and schedule the news alerts.

Getting the Gmail Password Key (App Password)

To send emails using Gmail, you need to generate an App Password. Follow these steps:

    Enable 2-Step Verification:
        Go to your Google Account.
        In the navigation panel, select Security.
        Under "Signing in to Google," select 2-Step Verification and follow the steps on the screen.

    Generate an App Password:
        In the "Signing in to Google" section of your Google Account, select App Passwords. You might need to sign in.
        At the bottom, choose Select app and choose the app you're using (e.g., Mail).
        Choose Select device and choose the device you're using (e.g., Other).
        Follow the instructions to enter the App Password. The App Password is the 16-digit code that generates on your device.
        Enter this App Password in place of your regular password when setting up the script.

Configuring the Script

The script will prompt you to enter the following details:

    Sending Email: The Gmail address from which you want to send the news alerts.
    Sending Email Password: The App Password generated from your Gmail account.
    Receiving Email: The email address where you want to receive the news alerts.
    Time for Alerts: The time at which you want to receive the news alerts (in 24-hour format, e.g., 09:00:00 or 14:40:00).

These details will be saved in a settings.json file in the lib directory.
Running the Script

Once configured, the script will run continuously and send news alerts at the scheduled time. You can stop the script by pressing Ctrl+C in the terminal.
Contributing to News Alert Scraper


