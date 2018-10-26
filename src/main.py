# main.py
#
# written by yuxq in 2018/10/26. all rights reserved.

import json
import requests

from utils import *
from curriculum import *
from prettytable import PrettyTable

json_link_header = "https://raw.githubusercontent.com/yuxiqian/finda-studyroom/master/json_output/"

start_year = int(input("输入学年的起始年份。\n例如，输入 [2018] 代表 2018-2019 学年\n>>> "))
separator()

term = int(input("输入学期代码。\n[1] 代表秋季学期\t[2] 代表春季学期\t[3] 代表夏季小学期\n>>> "))
separator()

json_url = json_link_header + \
    "%d_%d_%d.json" % (start_year, start_year + 1, term)

print("客官稍等")
separator()

r = requests.get(json_url)
try:
    result = json.loads(r.text, encoding="utf-8")
except:
    print("无法从 %s 获取数据（摊手）" % json_url)
    exit()

course_count = len(result['data'])
if course_count == 0:
    print("没有从 %s 获取到数据吭（挥手）" % json_url)
    exit()
else:
    print("成功获取 %d 枚数据～" % course_count)
    separator()

building = int(input("""输入教学楼代码。
[1] 代表上院\t[2] 代表中院\t[3] 代表下院
[4] 代表东上院\t[5] 代表东中院\t[6] 代表东下院
>>> """))
separator()

room = input("""输入教学楼门牌号。
东中院楼栋号和门牌号使用半角 “-” 符号分割。
>>> %s """ % building_list[building])
separator()

full_name = building_list[building] + room

week = int(input("""请输入周数。
暑假小学期周数从春季学期的开始进行计算。
>>> """))
separator()

week_day = int(input("""周几？
[1] 代表星期一\t[2] 代表星期二\t[3] 代表星期三\t
[4] 代表星期四\t[5] 代表星期五\t
>>> """))
separator()

for part in result['data']:
    i = Curriculum()
    i.identifier = part['identifier']
    i.holder_school = part['holder_school']
    i.title_name = part['name']
    i.school_year = part['year']
    i.term = part['term']
    i.target_grade = part['target_grade']
    i.teacher_name = part['teacher']
    i.teacher_title = part['teacher_title']
    i.credit_score = part['credit']
    i.start_week = part['start_week']
    i.end_week = part['end_week']

    for comp in part['odd_week']:
        arr = Arrangement()
        arr.week_day = comp['week_day'],
        arr.start_lesson = comp['start_from'],
        arr.end_lesson = comp['end_at'],
        arr.classroom = comp['classroom']
        i.odd_week.append(arr)

    for comp in part['even_week']:
        arr = Arrangement()
        arr.week_day = comp['week_day'],
        arr.start_lesson = comp['start_from'],
        arr.end_lesson = comp['end_at'],
        arr.classroom = comp['classroom']
        i.even_week.append(arr)
    i.student_number = part['student_number']
