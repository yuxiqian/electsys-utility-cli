# curriculum.py
#
# written by yuxq in 2018/9/15. all rights reserved.

import re
from utils import *
from copy import deepcopy

class Arrangement:
    # 单次上课的具体参数
    # 一门课可能会在一个学期内包含不同的课程教室组合
    # 由一个 Arrangement 数组来描述
    week_day = 0
    # 星期数。约定使用 1 ～ 7 分别代表周一到周日。

    start_lesson = 0
    # 开始节数

    end_lesson = 0
    # 结束节数（怪怪的）

    classroom = ''
    # 授课教室


class Curriculum:

    def __init__(self):
        self.odd_week = []
        # 单周的行课安排

        self.even_week = []
        # 霜周的行课安排

    holder_school = ''
    # 开课院系

    teacher_name = ''
    # 教师名称

    teacher_title = ''
    # 教师职称

    title_name = ''
    # 课程名称

    identifier = ''
    # 课程唯一识别代码

    learn_hour = 0
    # 学时

    credit_score = 0.0
    # 学分

    start_week = 0
    # 起始周数

    end_week = 0
    # 终止周数

    notes = ''
    # 备注

    target_grade = 0
    # 目标年级

    school_year = 0
    # 学年

    term = 0
    # 学期

    student_number = 0
    # 上课人数
