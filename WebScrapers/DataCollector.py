import selenium
from selenium import webdriver
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def write_to_file(st):
    File_Object = open("AdvancedDataByDate.txt", "a")
    File_Object.write(st + "\n")
    print(st)
    File_Object.close()


# Gets NBA.com season url format for season from date
def get_season(string):
    mon = int(string[0:string.index("%2F")])
    yr = int(string[string.rindex("%2F") + 3:])
    if mon > 8:
        return str(yr) + "-" + str(yr + 1)[2:]
    else:
        return str(yr - 1) + "-" + str(yr)[2:]


# Returns url
# Date in Format MM/DD/YYYY
def get_url(date):
    url1 = "https://stats.nba.com/teams/advanced/?sort=TEAM_NAME&dir=1&" + "Season=" + get_season(
        date) + "&SeasonType=Regular%20Season"
    return url1 + "&DateFrom=" + date + "&DateTo=" + date


def get_stats(date):
    url = get_url(date)
    path_to_chromedriver = 'D:\Downloads\chromedriver_win32\chromedriver.exe'  # Path to access a chrome driver
    browser = webdriver.Chrome(executable_path=path_to_chromedriver)
    browser.get(url)
    try:
        wait = WebDriverWait(browser, 10)
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "nba-stat-table__overflow")))
    except selenium.common.exceptions.TimeoutException:
        browser.quit()
        print("timeout")
        return "101"
    try:
        table = browser.find_element_by_class_name('nba-stat-table__overflow')
    except selenium.common.exceptions.NoSuchElementException:
        browser.quit()
        print("error")
        return "101"
    team_names = []
    team_stats = []
    for line_id, lines in enumerate(table.text.split('\n')):
        if len(lines) == 0:
            print()
        elif line_id == 0:
            column_names = lines.split(' ')[1:]
        elif line_id == 1:
            column_names
        else:
            if line_id % 2 == 1:
                team_names.append(lines)
            if line_id % 2 == 0:
                team_stats.append([float(i) for i in lines.split(' ')])
    team_stats_used = []
    for stat in team_stats:
        stat2 = stat[4:]
        team_stats_used.append(stat2)

    date_string = date
    for x in range(0, len(team_names)):
        teamName = team_names[x]
        teamStats = team_stats_used[x]
        date_string += "{" + teamName + ":"
        for y in range(0, len(teamStats)):
            date_string += str(teamStats[y]) + ","
        date_string = date_string[0:-1] + "}"
    browser.quit()
    return date_string


months_to_days = {
    1: 31,
    2: 28,
    3: 32,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}


def get_days_to(date):
    month = int(date[0:date.index("%2F")])
    day = int(date[date.index("%2F") + 3: date.rindex("%2F")])
    year = int(date[date.rindex("%2F") + 3:])
    leap_year = year % 4 == 0
    if month == 2:
        if leap_year:
            return 29
    return months_to_days[month]


# exclusive
end_date = "2%2F21%2F2020"

# inclusive
start_date = "10%2F16%2F2018"

start_time = datetime.now()
while start_date != end_date:
    start_time = datetime.now()
    s = get_stats(start_date)
    if s != "101":
        write_to_file(s)
    print(datetime.now() - start_time)
    month = int(start_date[0:start_date.index("%2F")])
    day = int(start_date[start_date.index("%2F") + 3: start_date.rindex("%2F")])
    year = int(start_date[start_date.rindex("%2F") + 3:])
    if day < get_days_to(start_date):
        day = day + 1
    else:
        if month == 12:
            year = year + 1
            month = 1
            day = 1
        else:
            month = month + 1
            day = 1
    start_date = str(month) + "%2F" + str(day) + "%2F" + str(year)
