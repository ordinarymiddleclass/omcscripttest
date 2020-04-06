zhweekday = ["星期日", "星期一", "星期二",
            "星期三", "星期四", "星期五", "星期六"]

from datetime import datetime
from dateutil import relativedelta
import os.path
from pathlib import Path


def from_my_birthday (d):
    """
        Calculate time difference between given datetime d and 1986-4-23.
    """
    birthday = datetime(1986, 4, 23)
    return relativedelta.relativedelta(d, birthday) 

def from_epoch (d):
    return (d - datetime(1970,1,1)).days

def from_gp (d):
    return (d - datetime(2019,9,28)).days

def format_utc_en (d):
    return d.strftime("%B %d, %Y (UTC)")

def format_utc_zh (d):    
    zhyear = "世界協調時間{0}年".format(d.year)
    zhday = "{0}月{1}日".format(d.month, d.day)
    rocyear = "(中華民國{0}年)".format(d.year-1911)
    return zhyear + rocyear + zhday

def format_epoch_en (d):
    return "{} days since Unix Epoch".format(from_epoch(d))

def format_epoch_zh (d):
    return "Unix 紀元 {} 日".format(from_epoch(d))

def format_weekday_en (d):
    return d.strftime ("%A")

def format_weekday_zh (d):
    return zhweekday[int(d.strftime ("%w"))]

def format_gp_en (d):
    return "Globus Pallidum day {}".format(from_gp(d))

def format_gp_zh (d):
    return "蒼白球紀元第{}日".format(from_gp(d))

def format_age (d):
    age = from_my_birthday (d)
    years = age.years
    months = age.months
    days = age.days
    age_en = ('{} years {} months {} days'.format(years, months, days))
    age_zh = ('{} 歲 {} 個月 {} 天'.format(years, months, days))
    return "### 年齡 Age\n* " + age_en + "\n* " + age_zh

def format_date_information (d):
    date_information_zh = format_utc_zh(d) + " / " + format_epoch_zh(d) + \
        " / " + format_weekday_zh(d) + " / " + format_gp_zh (d)
    date_information_en = format_utc_en(d) + " / " + format_epoch_en(d) + \
        " / " + format_weekday_en(d) + " / " + format_gp_en(d)    
    content_body = "* " + date_information_zh + "\n* " \
        + date_information_en
    return "### 日期 Date\n" + content_body + "\n* 特殊註記："

def format_title (d):
    n = from_gp (d)
    gpserial = "%04d"%n
    briefdate = d.strftime ("%Y%m%d")
    return "蒼白球日誌{}_gpdiary{}_{}".format(gpserial, gpserial, briefdate)

def format_filename ():    
    current_date = datetime.now()
    n = from_gp (current_date)
    gpserial = "%04d"%n
    briefdate = current_date.strftime ("%Y%m%d")
    return "../source/gpdiary{}_{}".format(gpserial, briefdate) + ".md"

def create_filehead():
    current_date = datetime.now()
    date_information = format_date_information(current_date)
    age_information = format_age(current_date)
    title = format_title (current_date)
    return title + "\n===\n" + date_information + "\n\n" + age_information + "\n\n"

def create_template_body():
    upper_body = "### 本文 Content\n1. \n\n---\n\n2. 雜記:物價與其他[2]\n\n---\n\n"
    lower_body = "### 注釋 Comment\n\n[1] \n\n[2] 新台幣計價。有關新台幣可見蒼白球日誌0007。\n\n"
    appendix = "### 附錄 Appendix\n"
    return upper_body + lower_body + appendix

def create_template():
    return create_filehead() + create_template_body()

current_path = Path(os.path.realpath(__file__))
root = current_path.parent.parent
newfilepath = root / "source"/ format_filename ()
print(os.path.exists(newfilepath))

if os.path.exists(newfilepath):
    pass
else:
    with newfilepath.open("w", encoding="utf-8") as f:
        f.write(create_template())
