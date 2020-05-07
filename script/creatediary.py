GPHEADER =[ '[_metadata_:encoding]: - "utf-8"',
        '[_metadata_:language]: - "zh-Hant-TW"',
        '[_metadata_:fileformat]: - "markdown"',
        '[_metadata_:MIME_type]: - "text/plain"',
        '[_metadata_:markdown_version]: - "commonmark version 0.29"',
        '[_metadata_:markdown_spec]: - "https://spec.commonmark.org/0.29/"']
zhweekday = ["星期日", "星期一", "星期二",
            "星期三", "星期四", "星期五", "星期六"]

from datetime import datetime
from datetime import timedelta
from dateutil import relativedelta
import os.path
from pathlib import Path
import lazymdwriter

def from_my_birthday (d):
    """
        Calculate time difference between given datetime d and 1986-4-23.
    """
    birthday = datetime(1986, 4, 23)
    return relativedelta.relativedelta(d, birthday) 

def from_licence (d):
    """
        Calculate time difference between given datetime d and 2017-10-12.
    """
    birthday = datetime(2017, 10, 12)
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
    rocyear = "(中華民國{0}年，令和{1}年)".format(d.year-1911, d.year-2018)
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
    li = lazymdwriter.convenient_list("年齡 Age")
    age = from_my_birthday (d)
    licence_age = from_licence (d)
    years = age.years
    months = age.months
    days = age.days
    licence_years = licence_age.years
    licence_months = licence_age.months
    licence_days = licence_age.days
    li.add_ul('{} years {} months {} days old / {} years {} months {} days after acquiring ROC Surgical Pathology Licence'.format(years, months, days, licence_years, licence_months, licence_days))
    li.add_ul('{} 歲 {} 個月 {} 天 / 成為病理專科醫師 {} 年 {} 個月 {} 天'.format(years, months, days, licence_years, licence_months, licence_days))
    return li.compile()

def format_date_information (d):
    li = lazymdwriter.convenient_list("日期 Date")
    date_information_zh = format_utc_zh(d) + " / " + format_epoch_zh(d) + \
        " / " + format_weekday_zh(d) + " / " + format_gp_zh (d)
    date_information_en = format_utc_en(d) + " / " + format_epoch_en(d) + \
        " / " + format_weekday_en(d) + " / " + format_gp_en(d)    
    li.add_ul(date_information_zh)
    li.add_ul(date_information_en)
    li.add_ul("特殊註記:")
    return li.compile()

def format_title (d):
    n = from_gp (d)
    gpserial = "%04d"%n
    briefdate = d.strftime ("%Y%m%d")
    return "蒼白球日誌{}_gpdiary{}_{}".format(gpserial, gpserial, briefdate)

def format_filename (d):    
    n = from_gp (d)
    gpserial = "%04d"%n
    briefdate = d.strftime ("%Y%m%d")
    return "gpdiary{}_{}".format(gpserial, briefdate) + ".md"

def create_filehead(d):
    date_information = format_date_information(d)
    age_information = format_age(d)
    title = lazymdwriter.lazy_header(format_title (d), 1)
    return title + date_information + age_information 


def create_template_body():
    upper_body = lazymdwriter.convenient_list("本文 Content")
    lower_body = lazymdwriter.convenient_list("注釋 Comment")
    appendix = lazymdwriter.convenient_list("附錄 Appendix")
    upper_body.add_ol("", 1)
    upper_body.add_ol("防疫筆記[1]", 2)
    upper_body.add_ol("蒼白球飲食誌暨物價筆記[2]", 3)
    lower_body.add_comment("指武漢肺炎(COVID-19)疫情，有關此瘟疫請見蒼白球日誌0155，此瘟疫造成的慘況請見蒼白球日誌0155-0220", 1)
    lower_body.add_comment("新台幣計價。有關新台幣請參見蒼白球日誌0155。此刻匯率為1美元兌新台幣，金價每盎司美元，西德州中級(WTI)原油價格每桶美元。", 2)
    return upper_body.compile() + lower_body.compile() + appendix.compile()

def create_template(d):
    head = "\n".join(GPHEADER)
    return head + "\n\n" + create_filehead(d) + create_template_body()

def create_file(d, path):
    newfilepath = path / format_filename (d)
    if os.path.exists(newfilepath):
        print("file already exists")
        pass
    else:
        with newfilepath.open("w", encoding="utf-8") as f:
            f.write(create_template(d))

current_path = Path(os.path.realpath(__file__))
root = current_path.parent.parent
rootpath = root / "source"
for i in range(25):
    newday = datetime.now() + timedelta(days=i)
    create_file(newday, rootpath)

