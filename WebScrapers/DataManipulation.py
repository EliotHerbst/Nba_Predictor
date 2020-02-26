import random

from game import Game


# Gets NBA.com season url format for season from date
def get_season(string):
    mon = int(string[0:string.index("%2F")])
    yr = int(string[string.rindex("%2F") + 3:])
    if mon > 8:
        return str(yr) + "-" + str(yr + 1)[2:]
    else:
        return str(yr - 1) + "-" + str(yr)[2:]


def reverse_file(read, write):
    File_Object = open(read, "r")
    File_To_Write = open(write, "a")
    lines = File_Object.readlines()
    File_To_Write.writelines(lines[::-1])
    File_Object.close()
    File_To_Write.close()


def find_nth(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start + len(needle))
        n -= 1
    return start


def get_nba_date(s):
    monthDayYear = s[s.index(",") + 2:]
    month = monthDayYear[0:monthDayYear.index(" ")]
    if month == "Jan":
        month = "1"
    elif month == "Feb":
        month = "2"
    elif month == "Mar":
        month = "3"
    elif month == "Apr":
        month = "4"
    elif month == "Oct":
        month = "10"
    elif month == "Nov":
        month = "11"
    elif month == "Dec":
        month = "12"

    monthDayYear = monthDayYear[monthDayYear.index(" ") + 1:]
    day = monthDayYear[0:monthDayYear.index(",")]
    monthDayYear = monthDayYear[monthDayYear.index(", ") + 2:]
    year = monthDayYear

    return month + "%2F" + day + "%2F" + year


def game_filter(game):
    season = get_season(get_nba_date(game.date))
    season_start_year = int(season[0:4])
    return season_start_year >= 2010


def get_last_n(n, date, team_name):
    reserved_game_date = open('AdvancedDataTestingReversed.txt', "r")
    return_string = ""
    lines = reserved_game_date.readlines()
    reserved_game_date.close()
    for x in range(0, len(lines)):
        line = lines[x]
        line_date = line[0: line.index("{")]
        season = get_season(line_date)
        if line_date == date:
            stats = []
            if x + n <= len(lines):
<<<<<<< HEAD
                for z in range(x+1, x + n):
                    sub_line = lines[z]
=======
                for z in range(x, x + n):
                    sub_line = lines[x]
>>>>>>> parent of a6c8e33... First CNN complete 99.35 accuracy over
                    sub_line_date = sub_line[0: sub_line.index("{")]
                    if get_season(sub_line_date) != season:
                        break
                    elif sub_line.find(team_name) != -1:
                        sub_line = sub_line[sub_line.index(team_name) + len(team_name) + 1:]
                        sub_line = sub_line[0: sub_line.index("}")]
                        string_stats = sub_line.split(",")
                        numerical_stats = [float(i) for i in string_stats]
                        stats.append(numerical_stats)
                    else:
                        pass

            else:
<<<<<<< HEAD
                for z in range(x+1, len(lines)):
                    sub_line = lines[z]
=======
                for z in range(x, len(lines)):
                    sub_line = lines[x]
>>>>>>> parent of a6c8e33... First CNN complete 99.35 accuracy over
                    sub_line_date = sub_line[0: sub_line.index("{")]
                    if get_season(sub_line_date) != season:
                        break
                    elif sub_line.find(team_name) != -1:
                        sub_line = sub_line[sub_line.index(team_name) + len(team_name) + 1:]
                        sub_line = sub_line[0: sub_line.index("}")]
                        string_stats = sub_line.split(",")
                        numerical_stats = [float(i) for i in string_stats]
                        stats.append(numerical_stats)
                    else:
                        pass
            if len(stats) == 0:
                return None
            stat_sums = stats[0]
            for xx in range(1, len(stats)):
                for zz in range(0, len(stat_sums)):
                    stat_sums[zz] = stat_sums[zz] + stats[xx][zz]
            length = float(len(stats))
            average_stats = [x / length for x in stat_sums]
            for xy in average_stats:
                return_string = return_string + str(xy) + ","
            return_string = str(return_string[0: -1])
            if return_string is not None:
                return str(return_string[0: -1])
    return None


# n is the number of previous days to take into account
def create_training_data(n):
    Game_Data = open("GameDataTesting.txt", "r")
    Training_File = open("TrainingDataTest" + str(n) + ".txt", "a")
    # Training_File = open("TestingData20.csv", "a")
    line = Game_Data.readlines()
    lines = line[0].split(":{}")
    games = []
    for x in range(0, len(lines) - 1):
        s = lines[x]
        if s.find("OT") != -1:
            s = s[0: s.index("OT")]
        date = s[0: find_nth(s, ",", 3)]
        s = s[find_nth(s, ",", 3) + 1:]
        visitor = s[0: s.index(",")]
        s = s[s.index(",") + 1:]
        home = s[0: s.index(",")]
        s = s[s.index(",") + 1:]
        visitor_score = int(s[0: s.index(",")])
        s = s[s.index(",") + 1:]
        home_score = int(s[0: s.index(",")])
        g = Game(visitor, home, date, visitor_score, home_score, "")
        games.append(g)

    filtered_games = list(filter(game_filter, games))
    for x in range(0, len(filtered_games)):
        game = filtered_games[x]
        date = get_nba_date(game.date)
        last_n_home = get_last_n(n, date, game.home)
        last_n_away = get_last_n(n, date, game.visitor)
        winner = -1
        if game.homeScore > game.visitorScore:
            winner = 1
        else:
            winner = 0
        Training_File_Lines = []
        home_string = str(last_n_home)
        away_string = str(last_n_away)
        if home_string is not None and away_string is not None:
            file_string = home_string + "," + away_string + "," + str(winner) + "\n"
            if file_string.find("None") == -1:
                Training_File_Lines.append(file_string)
        else:
            pass
        random.shuffle(Training_File_Lines)
        Training_File.writelines(Training_File_Lines)
    Game_Data.close()
    Training_File.close()


<<<<<<< HEAD
#reverse_file("AdvancedDataTesting.txt", "AdvancedDataTestingReversed.txt")
create_training_data(20)
=======
# reverse_file("AdvancedDataByDate.txt", "AdvancedDataByDataReversed.txt")
#create_training_data(1)
>>>>>>> parent of a6c8e33... First CNN complete 99.35 accuracy over
