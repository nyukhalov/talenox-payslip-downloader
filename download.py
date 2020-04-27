import sys
import os
import requests
from datetime import datetime

def download_year_month(session, path, date):
    months = {
        1: 'January',
        2: 'February',
        3: 'March',
        4: 'April',
        5: 'May',
        6: 'June',
        7: 'July',
        8: 'August',
        9: 'September',
        10: 'October',
        11: 'November',
        12: 'December'
    }
    year = date.year
    month = months[date.month]

    print(f'- {year}-{month} payslip... ', end='')

    custom_header = {
        'Cookie': f'tlx_session={session}'
    }
    response = requests.get(f'https://www.talenox.com/apps/payslip.pdf?month={month}&year={year}', headers=custom_header)

    if response.status_code == 404 or len(response.content) < 15 * 1024:
        print('NOT FOUND')
        return
    if response.status_code != 200:
        print(f'FAIL ({response.status_code})')
        return
    print('OK')

    fname = f'payslip-{year}-{month}.pdf'
    with open(os.path.join(path, fname), 'wb') as f:
        f.write(response.content)

def download(session, path, start_from, mid_this_month):
    print('Downloading payslips')
    for year in range(start_from.year, mid_this_month.year + 1):
        for month in range(1, 13):
            date = datetime(year=year, month=month, day=1)
            if date > mid_this_month:
                return
            download_year_month(session, path, date)
    print('Finished')

def main():
    if len(sys.argv) < 3:
        print('Usage: python3 download.py SESSION START_YEAR [DESTINATION]')
        sys.exit(0)

    session = sys.argv[1]
    start_year = int(sys.argv[2])
    path = sys.argv[3] if len(sys.argv) > 3 else '.'

    start_from = datetime(year=start_year, month=1, day=1)
    mid_this_month = datetime.today().replace(day=15)
    if start_from > mid_this_month:
        print(f'Start date must be in past')
        sys.exit(0)

    download(session, path, start_from, mid_this_month)

if __name__=='__main__':
    main()
