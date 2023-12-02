import calendar
import configparser
import pathlib
from datetime import date

import FindRen as find

# 列出自今日后的剩余日期
date = date.today().strftime("%Y年%m月%d日")
print(date)
year = int(date[0:4])  # 根据date参数获取年份
# print(year)
month = int(date[5:7])
# print(month)
day = int(date[8:10])
# print(day)

ini_path = pathlib.Path(__file__).parent.parent.joinpath("戊日查询结果.ini")
ini = configparser.ConfigParser()


# 将结果以ini文件的形式输出到项目的根目录中。


# 列出剩余的日期
def ListRemainingDates(Year=year, Month=month, Day=day):
    '''
    从date所处日期开始，用当前月份总日数减去当前日数，列举出完整的当月日期，
    用queryDay8Char方法算出日柱，再用checkIfDay8CharIsWu方法判断当日
    是否为戊日，如果是戊日则保存到字典中，不是则跳过。
    :param Year: 年，默认为当天的年份
    :param Month: 月，默认为当天的月份
    :param Day: 日，默认为当天的日
    :return: 戊日的日期和日柱，日期为键，日柱为值。
    '''
    result = {}
    while 1 <= Month <= 12:
        dates = calendar.monthrange(Year, Month)[1]
        DayChar = find.queryDay8Char(Year, Month, Day)
        IsRen = find.checkIfDay8CharIsWu(DayChar)
        if IsRen:
            Date = str(Year) + "年" + str(Month) + "月" + str(Day) + "日"
            result[Date] = DayChar

        if Day < dates:
            Day += 1
        elif Day == dates:
            Day = 1
            Month += 1
    return result


def OutputResults(Year=year):
    thisYear = Year.__str__()
    DateWu = ListRemainingDates()
    ini.add_section(thisYear)
    for key, value in DateWu.items():
        ini.set(thisYear, key, value)
    with open(ini_path, 'a+', encoding='utf-8') as f:
        ini.write(f)


OutputResults()
