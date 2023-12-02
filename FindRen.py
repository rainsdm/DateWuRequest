import datetime

import cnlunar


def queryDay8Char(year, month, day, hour=12, miniute=0, method='beginningOfSpring'):
    '''
    为了简化调用时的操作，特此将日主的查询简化。由于23时为一天的开始，为避免混淆，默认规定12时整为当日的查询时间。
    :param year: 年
    :param month: 月
    :param day: 日
    :param hour: 时
    :param miniute: 分
    :param method: 选择常规算法或八字立春切换算法，对应的参数是'beginningOfSpring'，如果为常规算法，此项留空。
    :return:以文字表示的当日日柱
    '''

    oneday = cnlunar.Lunar(datetime.datetime(year, month, day, hour, miniute), godType='8char', year8Char=method)
    return oneday.day8Char


# print(queryDay8Char(2022,8,5))

def checkIfDay8CharIsWu(day):
    '''
    判断这一天是否为戊日。
    :param day:八字格式的日期
    :return:True表示当日为戊日。
    '''
    if day[0] == '戊':
        return True
    else:
        return False

# result = queryDay8Char(2023,5,10)
# print(result)
# print(checkIfDay8CharIsWu(result))
