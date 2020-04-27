# Talenox Payslip Downloader

Download all your Talenox payslips in one go.

## Prerequisites

- Python 3

## Installation and Usage

```bash
git clone git@github.com:nyukhalov/talenox-payslip-downloader.git
cd talenox-payslip-downloader
python3 download.py SESSION START_YEAR DESTINATION
```

## Find your session ID

The following instruction were tested on Chrome web browser

- Log in into Talenox using your existing account
- Open the developer console (press F12)
- Go to the `Application` tab
- In the left panel click on the `https://www.talenox.com` item under the
  `Storage/Cookies` section
- Copy the value of the `tlx_session` cookie
- Use the copied value as SESSION when run the script
- DO NOT SHARE your session ID with other people as it gives them the access to
  your payslips
