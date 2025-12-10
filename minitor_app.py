import time
from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException
import re
import login_app
import var_app
import module_other_app
import requests
import json
from retry import retry
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction
import report_app
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime


# from appium.webdriver.common.touch_action import TouchAction
# from appium.webdriver.common.multi_action import MultiAction



def select_detail(field, row):
    var_app.driver.implicitly_wait(0.05)  # nhiên liệu
    n = 0
    while (n < 75):
        n += 1
        n = str(n)
        pathtenphuongtien = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[" + n + "]/android.view.ViewGroup[1]/android.widget.TextView"
        print(n)
        try:
            tenphuongtien = var_app.driver.find_element(By.XPATH, pathtenphuongtien).text
            if tenphuongtien == field:
                detail_fuel1 = var_app.driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[" + n + "]/android.widget.TextView").text
                module_other_app.writeData1(var_app.path_luutamthoi, "Sheet1", row, 3, detail_fuel1)
                print(detail_fuel1)
                break
        except:
            pass
        n = int(n)


def status_general_information(field_name, row):
    var_app.driver.implicitly_wait(0.05)
    n = 0
    while (n < 16):
        n += 1
        n = str(n)
        pathtenphuongtien = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[4]/android.view.ViewGroup[" + n + "]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView"
        print(n)
        try:
            tenphuongtien = var_app.driver.find_element(By.XPATH, pathtenphuongtien).text
            print(tenphuongtien)
            if tenphuongtien == field_name:
                detail_name = var_app.driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[4]/android.view.ViewGroup[" + n + "]/android.view.ViewGroup/android.widget.TextView").text
                module_other_app.writeData1(var_app.path_luutamthoi, "Sheet1", row, 3, detail_name)
                print(tenphuongtien + ": "+ detail_name)
                break
        except:
            pass
        n = int(n)


def status_general_information1(field_name, row):
    var_app.driver.implicitly_wait(0.05)
    n = 0
    while (n < 16):
        n += 1
        n = str(n)
        pathtenphuongtien = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[" + n + "]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView"
        print(n)
        try:
            tenphuongtien = var_app.driver.find_element(By.XPATH, pathtenphuongtien).text
            print(tenphuongtien)
            if tenphuongtien == field_name:
                detail_name = var_app.driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[" + n + "]/android.view.ViewGroup/android.widget.TextView").text
                module_other_app.writeData1(var_app.path_luutamthoi, "Sheet1", row, 3, detail_name)
                print(tenphuongtien + ": "+ detail_name)
                break
        except:
            pass
        n = int(n)



def status_general_information2(field_name, row):
    var_app.driver.implicitly_wait(0.05)
    n = 0
    while (n < 16):
        n += 1
        n = str(n)
        pathtenphuongtien = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[" + n + "]/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.TextView"
        print(n)
        try:
            tenphuongtien = var_app.driver.find_element(By.XPATH, pathtenphuongtien).text
            print(tenphuongtien)
            if tenphuongtien == field_name:
                detail_name = var_app.driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[" + n + "]/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.TextView").text
                module_other_app.writeData1(var_app.path_luutamthoi, "Sheet1", row, 3, detail_name)
                print(tenphuongtien + ": "+ detail_name)
                break
        except:
            pass
        n = int(n)




def status_general_information3(field_name, row):
    var_app.driver.implicitly_wait(0.05)
    n = 0
    while (n < 16):
        n += 1
        n = str(n)
        pathtenphuongtien = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup[" + n + "]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView"
        print(n)
        try:
            tenphuongtien = var_app.driver.find_element(By.XPATH, pathtenphuongtien).text
            print(tenphuongtien)
            if tenphuongtien == field_name:
                detail_name = var_app.driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup[" + n + "]/android.view.ViewGroup/android.widget.TextView").text
                module_other_app.writeData1(var_app.path_luutamthoi, "Sheet1", row, 3, detail_name)
                print(tenphuongtien + ": "+ detail_name)
                break
        except:
            pass
        n = int(n)



def minitor_back():
    var_app.driver.implicitly_wait(0.2)
    try:
        var_app.driver.find_element(By.XPATH, var_app.minitor_back1).click()
        time.sleep(1.2)
    except:
        pass
    try:
        var_app.driver.find_element(By.XPATH, var_app.minitor_back2).click()
        time.sleep(1.2)
    except:
        pass
    try:
        var_app.driver.find_element(By.XPATH, var_app.minitor_back3).click()
        time.sleep(1.2)
    except:
        pass
    try:
        var_app.driver.find_element(By.XPATH, var_app.minitor_back4).click()
        time.sleep(1.2)
    except:
        pass




def get_detail(path_get, row, column):
    var_app.driver.implicitly_wait(1)
    try:
        get_data = var_app.driver.find_element(By.XPATH, path_get).text
        module_other_app.writeData1(var_app.path_luutamthoi, "Sheet1", row, column, get_data)
        print(get_data)
    except:
        pass


@retry(tries=3, delay=2, backoff=1, jitter=5)
def call_api950(vehicle_plate):
    api_url = "https://gps.binhanh.vn/HttpHandlers/OnlineHandler.ashx"

    todo = {
            'method': 'getVehicleOnlineByCompanyIDAndGroupNew',
            'groupIDs': ""
            }
    headers = {"cookie": "_ga=GA1.1.987778944.1710466198; route_column_truongvck1=chkVgps,chkCoVong,chkKm; route_column_class_truongvck1=vtgps,vtcovong,km; route_column_partner1001=chkVgps,chkCoVong,chkKm; route_column_class_partner1001=vtgps,vtcovong,km; route_column_ungroup_1=chkVgps,chkCoVong,chkKm; route_column_class_ungroup_1=vtgps,vtcovong,km; route_column_truongtq@bagroup.vn=chkVgps,chkCoVong,chkKm; route_column_class_truongtq@bagroup.vn=vtgps,vtcovong,km; route_column_ungroup=chkVgps,chkCoVong,chkKm,chkCua,chkVbgt; route_column_class_ungroup=vtgps,vtcovong,km,cua,vtbgt; route_column_43e02743=chkVgps,chkCoVong; route_column_class_43e02743=vtgps,vtcovong; route_column_viconshipdanang1=chkCoVong,chkAddress; route_column_class_viconshipdanang1=vtcovong,addr; route_column_43e02740=chkVgps,chkCoVong,chkKm; route_column_class_43e02740=vtgps,vtcovong,km; _ga_9LVRP2FDNH=GS1.1.1719632056.14.1.1719634757.0.0.0; route_column_vuthingocgls=chkVgps,chkCoVong,chkKm; route_column_class_vuthingocgls=vtgps,vtcovong,km; CultureInfo=vi-VN; ASP.NET_SessionId=0bkekxfychfah4p11f4l0ily; ARRAffinity=369bb8b1dab68ca0e7a2dc8719a27d710fd20d197411d8ead2a35c03dfd4c644; __AntiXsrfToken=7bb760b14fc54556afe537fb33316950; browsers=[{'PK_BrowserVersionID':1,'Name':'Chrome','Version':'90','CreatedDate':'2022-03-21T00:00:00'},{'PK_BrowserVersionID':2,'Name':'Edg','Version':'100','CreatedDate':'2022-03-21T00:00:00'},{'PK_BrowserVersionID':3,'Name':'Firefox','Version':'90','CreatedDate':'2022-03-21T00:00:00'},{'PK_BrowserVersionID':4,'Name':'OPR','Version':'38','CreatedDate':'2022-03-21T00:00:00'},{'PK_BrowserVersionID':6,'Name':'Safari','Version':'10','CreatedDate':'2022-03-21T00:00:00'},{'PK_BrowserVersionID':7,'Name':'IE','Version':'21','CreatedDate':'2022-03-21T00:00:00'}]; ResourceVersion=20240703v1; __zi=2000.SSZzejyD6jSbWlwbsKiDrs-0ghkNHHMLCvAWfOK71uCYr__ZXG1EpINIykE71a-38jRxhuK9I8icr_kbDW.1; Login_.ASPXFORMSAUTH=7712804AF7378C97AC05FCC2FF80B6D593BFCFCBF01646D3CAA2D9BA9D678B726468DB2ED706F288079022FA89A20694648C5D36D1F072C1FABE7C601060F5E2632B1E6539FA2110231BD5D1D6AA3E60A314AE508C8CE23E4BF41E7B0F64316F; _ga_02FC5P5V42=GS1.1.1719977763.271.1.1719977784.0.0.0"}


    response = requests.request("POST", api_url, data=todo, headers=headers)
    response.json()
    res = json.loads(response.text)
    print(res)
    try:
        print("Phương tiện 0: ", res['data'][0]['plate'])
    except:
        pass

    n = -1
    while (n < 100):
        n += 1
        print(n)
        # print("Phương tiện số {} : {}".format(n, res['data'][n]['plate']))
        try:
            if res['data'][n]['plate'] == vehicle_plate:
                module_other_app.writeData1(var_app.path_luutamthoi, "Sheet1", 6, 4, res['data'][n]['plate'])   #biển số
                module_other_app.writeData1(var_app.path_luutamthoi, "Sheet1", 7, 4, res['data'][n]['db_time'])   #giờ cập nhật
                module_other_app.writeData1(var_app.path_luutamthoi, "Sheet1", 8, 4, res['data'][n]['v_gps'])   #vận tốc gps
                module_other_app.writeData1(var_app.path_luutamthoi, "Sheet1", 10, 4, res['data'][n]['t_km'])   #km trong ngày
                module_other_app.writeData1(var_app.path_luutamthoi, "Sheet1", 14, 4, res['data'][n]['adds'])   #địa chỉ
                module_other_app.writeData1(var_app.path_luutamthoi, "Sheet1", 26, 4, res['data'][n]['bgt']['name'])   #lái xe
                module_other_app.writeData1(var_app.path_luutamthoi, "Sheet1", 27, 4, res['data'][n]['bgt']['license'])   #bằng lái
                module_other_app.writeData1(var_app.path_luutamthoi, "Sheet1", 29, 4, res['data'][n]['bgt']['t_continus'])   #thời gian lái xe liên tục
                module_other_app.writeData1(var_app.path_luutamthoi, "Sheet1", 30, 4, res['data'][n]['bgt']['t_day'])   #thời gian lái xe trong ngày
                module_other_app.writeData1(var_app.path_luutamthoi, "Sheet1", 31, 4, res['data'][n]['bgt']['speed_o'])   #số lần quá tốc dộ
                module_other_app.writeData1(var_app.path_luutamthoi, "Sheet1", 36, 4, res['data'][n]['bgt']['vin'])   #số vin

                break
        except:
            pass






def scroll_and_click_precent(startX, startY, endX, endY, duration, path_check):
    var_app.driver.implicitly_wait(0.5)
    n = 0
    while (n < 10):
        n += 1
        try:
            var_app.driver.find_element(By.XPATH, path_check).is_displayed()
            break
        except:
            module_other_app.swipe_percent(var_app.driver, startX, startY, endX, endY, duration)
        time.sleep(0.5)
    try:
        var_app.driver.find_element(By.XPATH, path_check).click()
        try:
            var_app.driver.find_element(By.XPATH, path_check).click()
        except:
            pass
    except:
        module_other_app.swipe_percent(var_app.driver, endX, startY, startX, endY, duration)
        var_app.driver.find_element(By.XPATH, path_check).click()
    time.sleep(2.5)




def scroll_and_click_reverse(startX, startY, endX, endY, duration, path_check):
    var_app.driver.implicitly_wait(1)
    n = 0
    while (n < 6):
        n += 1
        try:
            var_app.driver.find_element(By.XPATH, path_check).is_displayed()
            break
        except:
            module_other_app.swipe_scaled(var_app.driver, endX, startY, startX, endY, duration)
            print("n1")
        time.sleep(1)
    var_app.driver.find_element(By.XPATH, path_check).click()
    try:
        var_app.driver.find_element(By.XPATH, path_check).click()
    except:
        pass
    time.sleep(2.5)

#725, 1100, 175, 1100




def get_status_vehicle(field_name):
    module_other_app.clearData_luutamthoi(var_app.path_luutamthoi, "Sheet1", "", "", "")

    var_app.driver.implicitly_wait(0.05)
    n = 0
    while (n < 16):
        n += 1
        n = str(n)
        status_that   = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.FrameLayout[1]/androidx.viewpager.widget.ViewPager/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[" + n + "]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.widget.TextView"
        quantity_that = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.FrameLayout[1]/androidx.viewpager.widget.ViewPager/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[" + n + "]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.TextView"

        status_test   = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.FrameLayout[1]/androidx.viewpager.widget.ViewPager/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[" + n + "]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.widget.TextView"
        quantity_test = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.FrameLayout[1]/androidx.viewpager.widget.ViewPager/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[" + n + "]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.TextView"
        print(n)

        try:
            status = var_app.driver.find_element(By.XPATH, status_that).text
            path_status = status_that
            path_quantity = quantity_that
        except:
            path_status = status_test
            path_quantity = quantity_test

        try:
            status = var_app.driver.find_element(By.XPATH, path_status).text
            print(status)
            if status == field_name:
                quantity = var_app.driver.find_element(By.XPATH, path_quantity).text
                quantity = ''.join(re.findall(r'\d+', quantity))
                print("Trạng thái: {} {}Phương tiện".format(status, quantity))

                module_other_app.writeData1(var_app.path_luutamthoi, "Sheet1", 108, 2, status)
                module_other_app.writeData1(var_app.path_luutamthoi, "Sheet1", 109, 2, quantity)
                var_app.driver.find_element(By.XPATH, path_status).click()
                time.sleep(2)

                break
        except:
            pass
        n = int(n)


def get_status_vehicle1(field_name):
    var_app.driver.implicitly_wait(0.02)
    n = 0
    while (n < 16):
        n += 1
        n = str(n)
        path_status = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/androidx.viewpager.widget.ViewPager/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[" + n + "]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.widget.TextView"
        path_quantity = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/androidx.viewpager.widget.ViewPager/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[" + n + "]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.TextView"
        print(n)
        try:
            status = var_app.driver.find_element(By.XPATH, path_status).text
            print(status)
            if status == field_name:
                quantity = var_app.driver.find_element(By.XPATH, path_quantity).text
                quantity = ''.join(re.findall(r'\d+', quantity))

                if status == " Nợ phí":
                    module_other_app.writeData1(var_app.path_luutamthoi, "Sheet1", 88, 2, status)
                    module_other_app.writeData1(var_app.path_luutamthoi, "Sheet1", 89, 2, quantity)
                if status == " Di chuyển":
                    module_other_app.writeData1(var_app.path_luutamthoi, "Sheet1", 90, 2, status)
                    module_other_app.writeData1(var_app.path_luutamthoi, "Sheet1", 91, 2, quantity)
                if status == " Dừng - Tắt":
                    module_other_app.writeData1(var_app.path_luutamthoi, "Sheet1", 92, 2, status)
                    module_other_app.writeData1(var_app.path_luutamthoi, "Sheet1", 93, 2, quantity)
                if status == " Dừng - Bật":
                    module_other_app.writeData1(var_app.path_luutamthoi, "Sheet1", 94, 2, status)
                    module_other_app.writeData1(var_app.path_luutamthoi, "Sheet1", 95, 2, quantity)
                if status == " Bật máy":
                    module_other_app.writeData1(var_app.path_luutamthoi, "Sheet1", 96, 2, status)
                    module_other_app.writeData1(var_app.path_luutamthoi, "Sheet1", 97, 2, quantity)
                if status == " Tắt máy":
                    module_other_app.writeData1(var_app.path_luutamthoi, "Sheet1", 98, 2, status)
                    module_other_app.writeData1(var_app.path_luutamthoi, "Sheet1", 99, 2, quantity)
                if status == " Quá tốc độ":
                    module_other_app.writeData1(var_app.path_luutamthoi, "Sheet1", 100, 2, status)
                    module_other_app.writeData1(var_app.path_luutamthoi, "Sheet1", 101, 2, quantity)
                if status == " Mất GPS":
                    module_other_app.writeData1(var_app.path_luutamthoi, "Sheet1", 102, 2, status)
                    module_other_app.writeData1(var_app.path_luutamthoi, "Sheet1", 103, 2, quantity)
                if status == " Mất GSM":
                    module_other_app.writeData1(var_app.path_luutamthoi, "Sheet1", 104, 2, status)
                    module_other_app.writeData1(var_app.path_luutamthoi, "Sheet1", 105, 2, quantity)
                if status == "Tất cả":
                    module_other_app.writeData1(var_app.path_luutamthoi, "Sheet1", 106, 2, status)
                    module_other_app.writeData1(var_app.path_luutamthoi, "Sheet1", 107, 2, quantity)
                print("Trạng thái: {} {}Phương tiện".format(status, quantity))

                module_other_app.writeData1(var_app.path_luutamthoi, "Sheet1", 108, 2, status)
                module_other_app.writeData1(var_app.path_luutamthoi, "Sheet1", 109, 2, quantity)
                time.sleep(2)
                break
        except:
            pass
        n = int(n)




def zoom(type_zoom, number):
    var_app.driver.implicitly_wait(1)
    # Tạo các đối tượng hành động cho thu nhỏ
    action1 = TouchAction(var_app.driver)
    action2 = TouchAction(var_app.driver)
    i = 0
    if type_zoom == "Thu nhỏ":
        for i in range(number):
            i = i + 1
            # Ngón tay thứ nhất kéo từ xa về gần trung tâm
            action1.press(x=890, y=270).move_to(x=500, y=700).release()

            # Ngón tay thứ hai kéo từ xa về gần trung tâm
            action2.press(x=50, y=1400).move_to(x=400, y=900).release()

            # Kết hợp hai hành động thành MultiAction
            pinch_action = MultiAction(var_app.driver)
            pinch_action.add(action1, action2)
            pinch_action.perform()
            time.sleep(1)
            print("Đã thu nhỏ lần: ", i)

    if type_zoom == "Phóng to":
        for i in range(number):
            i = i + 1
            # Ngón tay thứ nhất kéo từ xa về gần trung tâm
            action1.press(x=500, y=700).move_to(x=890, y=270).release()

            # Ngón tay thứ hai kéo từ xa về gần trung tâm
            action2.press(x=400, y=900).move_to(x=50, y=1400).release()

            # Kết hợp hai hành động thành MultiAction
            pinch_action = MultiAction(var_app.driver)
            pinch_action.add(action1, action2)
            pinch_action.perform()
            time.sleep(1)
            print("Đã phóng to lần: ", i)





class overview:


    def select_many_vehicle(self, code, eventname, result):
        var_app.driver.implicitly_wait(5)
        login_app.login.login_v3(self, var_app.data['login']['conhom_quantri_tk'], var_app.data['login']['conhom_quantri_mk'])
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.minitor).click()
            time.sleep(1.5)
        except:
            pass

        var_app.logging.info("--------------")
        var_app.logging.info("Giám sát - Chọn nhiều xe")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)

        n = 0
        while (n < 7):
            n += 1
            n = str(n)
            path_vehicle_that = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[" + n + "]/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.TextView[1]"
            path_vehicle_test = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[" + n + "]/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.TextView[1]"

            try:
                var_app.driver.find_element(By.XPATH, var_app.search_vehicle).click()
                time.sleep(2)

                try:
                    name = var_app.driver.find_element(By.XPATH, path_vehicle_that).text
                    path_vehicle = path_vehicle_that
                except:
                    path_vehicle = path_vehicle_test

                name = var_app.driver.find_element(By.XPATH, path_vehicle).text
                # name = var_app.driver.find_element(By.XPATH, path_vehicle).get_attribute("content-desc")
                var_app.driver.find_element(By.XPATH, path_vehicle).click()
                time.sleep(2.5)
                address = var_app.driver.find_element(By.XPATH, var_app.path_address).text
                var_app.logging.info("True")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Pass")
                print(address)
                print(name)
                if address == "Đang xác định địa chỉ.....":
                    try:
                        time.sleep(5)
                        address_wait = var_app.driver.find_element(By.XPATH, var_app.path_address).text
                        if address_wait == "Đang xác định địa chỉ.....":
                            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, f"Phương tiện: {name}, Địa chỉ: {address_wait}")
                            var_app.logging.info("False")
                            var_app.driver.save_screenshot(var_app.imagepath + code + "_GiamSat_ChonNhieuXe.png")
                            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Fail")
                            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 13, code + "_GiamSat_ChonNhieuXe.png")
                            break
                    except:
                        pass
            except:
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, f"Đã văng app sau lần chọn thứ {n}")
                var_app.logging.info("False")
                var_app.driver.save_screenshot(var_app.imagepath + code + "_GiamSat_ChonNhieuXe.png")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Fail")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 13, code + "_GiamSat_ChonNhieuXe.png")
                break
            n = int(n)



    def search_vehicle(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        login_app.login.login_v3(self, var_app.data['login']['conhom_quantri_tk'],var_app.data['login']['conhom_quantri_mk'])

        try:
            var_app.driver.implicitly_wait(0.5)
            var_app.driver.find_element(By.XPATH, var_app.search_vehicle).click()
        except:
            login_app.login.login_v3(self, var_app.data['login']['conhom_quantri_tk'], var_app.data['login']['conhom_quantri_mk'])
            var_app.driver.find_element(By.XPATH, var_app.search_vehicle).click()
            print("vao day roi")
        var_app.driver.implicitly_wait(2)
        time.sleep(2)
        try:
            var_app.driver.find_element(By.XPATH, var_app.search_vehicle_input).send_keys(var_app.data['minitor']['search'])
        except:
            var_app.driver.find_element(By.XPATH, var_app.search_vehicle).click()
            time.sleep(2)
            var_app.driver.find_element(By.XPATH, var_app.search_vehicle_input).send_keys(var_app.data['minitor']['search'])
        time.sleep(1.5)
        module_other_app.tap_scaled(var_app.driver, [(193, 352)])
        time.sleep(2.5)
        module_other_app.write_result_text_try_if(code, eventname, result, "Giám sát - Tìm kiếm xe",
                                              var_app.check_search_vehicle, var_app.data['minitor']['search'], "_GiamSat_TimKiemXe.png")
        try:
            var_app.driver.find_element(By.XPATH, var_app.detail_vehicle_iconx1).click()
            time.sleep(1)
        except:
            pass


    def select_1group(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(2)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.find_element(By.XPATH, var_app.select_group_icon).click()
        except:
            login_app.login.login_v3(self, var_app.data['login']['conhom_quantri_tk'], var_app.data['login']['conhom_quantri_mk'])
            var_app.driver.find_element(By.XPATH, var_app.select_group_icon).click()
        time.sleep(1.5)
        var_app.driver.find_element(By.XPATH, var_app.select_group_input).send_keys(var_app.data['minitor']['search_group'])
        time.sleep(2)
        module_other_app.swipe_scaled(var_app.driver, 400, 400, 400, 1000, 500)
        module_other_app.tap_scaled(var_app.driver, [(40, 490)])
        time.sleep(0.5)
        var_app.driver.find_element(By.XPATH, var_app.minitor_name_group_choose).click()
        time.sleep(3)
        var_app.driver.implicitly_wait(1)
        module_other_app.write_result_text_try_if_conten(code, eventname, result, "Giám sát - chọn nhóm",
                                              "(//android.view.View[@content-desc='"+var_app.data['minitor']['check_search_group']+"'])[1]",
                                                  var_app.data['minitor']['check_search_group'], "_GiamSat_Chon1Nhom.png")


        var_app.driver.find_element(By.XPATH, var_app.select_group_icon).click()
        time.sleep(1.5)
        module_other_app.swipe_scaled(var_app.driver, 400, 400, 400, 1000, 500)
        module_other_app.tap_scaled(var_app.driver, [(40, 490)])
        time.sleep(0.5)
        var_app.driver.find_element(By.XPATH, var_app.minitor_name_group_choose).click()
        time.sleep(2.5)


    def select_manygroup(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(2)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.find_element(By.XPATH, var_app.select_group_icon).click()
        except:
            login_app.login.login_v3(self, var_app.data['login']['conhom_quantri_tk'], var_app.data['login']['conhom_quantri_mk'])
            var_app.driver.find_element(By.XPATH, var_app.select_group_icon).click()
        time.sleep(1.5)
        var_app.driver.find_element(By.XPATH, var_app.select_group_icon_all).click()
        time.sleep(0.5)
        var_app.driver.find_element(By.XPATH, var_app.minitor_name_group_choose).click()
        time.sleep(3)
        module_other_app.write_result_text_try_if_conten(code, eventname, result, "Giám sát - chọn nhóm",
                                              "(//android.view.View[@content-desc='"+var_app.data['minitor']['check_search_group1']+"'])[1]",
                                                  var_app.data['minitor']['check_search_group1'], "_GiamSat_ChonTatCaNhom.png")

        var_app.driver.find_element(By.XPATH, var_app.select_group_icon).click()
        time.sleep(1.5)
        var_app.driver.find_element(By.XPATH, var_app.select_group_icon_all).click()
        time.sleep(0.5)
        var_app.driver.find_element(By.XPATH, var_app.minitor_name_group_choose).click()
        time.sleep(3)


    def vehicle_status(self, code, eventname, result, status_name, path_image):
        module_other_app.writeData1(var_app.path_luutamthoi, "Sheet2", 3, 2, "")
        try:
            var_app.driver.implicitly_wait(0.2)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(1)
        if code == "Minitor04":
            login_app.login.login_v3(self, var_app.data['login']['conhom_quantri_tk3'], var_app.data['login']['conhom_quantri_mk3'])
        if code == "Minitor14":
            login_app.login.login_v3(self, var_app.data['login']['conhom_thuong_tk2'], var_app.data['login']['conhom_thuong_mk2'])
        if code == "Minitor24":
            login_app.login.login_v3(self, var_app.data['login']['conhom_quantri_tk2'], var_app.data['login']['conhom_quantri_mk2'])
        if code == "Minitor34":
            login_app.login.login_v3(self, var_app.data['login']['khongnhom_thuong_tk3'], var_app.data['login']['khongnhom_thuong_mk3'])
        if code == "Minitor44":
            login_app.login.login_v3(self, var_app.data['login']['conhom_quantri_tk'], var_app.data['login']['conhom_quantri_mk'])
        if code == "Minitor54":
            login_app.login.login_v3(self, var_app.data['login']['conhom_thuong_tk'], var_app.data['login']['conhom_thuong_mk'])
        if code == "Minitor64":
            login_app.login.login_v3(self, var_app.data['login']['khongnhom_quantri_tk'], var_app.data['login']['khongnhom_quantri_mk'])
        if code == "Minitor74":
            login_app.login.login_v3(self, var_app.data['login']['khongnhom_thuong_tk2'], var_app.data['login']['khongnhom_thuong_mk2'])


        var_app.driver.implicitly_wait(1)
        module_other_app.writeData1(var_app.path_luutamthoi, "Sheet2", 3, 2, "0")
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.minitor).click()
            time.sleep(1.5)
        except:
            pass
        try:
            var_app.driver.find_element(By.XPATH, var_app.vehicle_status_icon).click()
            time.sleep(2)
            var_app.driver.find_element(By.XPATH, var_app.status_all1)
        except:
            var_app.driver.implicitly_wait(0.5)
            module_other_app.close_app()
            module_other_app.writeData1(var_app.path_luutamthoi, "Sheet2", 3, 2, "1")
            print("n4")
            if code == "Minitor04" or code == "Minitor05" or code == "Minitor06" or code == "Minitor07" or code == "Minitor08" or code == "Minitor09"\
                    or code == "Minitor10" or code == "Minitor11" or code == "Minitor12" or code == "Minitor03":
                login_app.login.check_logout1(self, "CÔNG TY TNHH DỊCH VỤ TIẾP VẬN TOÀN CẦU (GLS)", var_app.data['login']['conhom_quantri_tk3'], var_app.data['login']['conhom_quantri_mk3'])
            if code == "Minitor14" or code == "Minitor15" or code == "Minitor16" or code == "Minitor17" or code == "Minitor18" or code == "Minitor19"\
                    or code == "Minitor20" or code == "Minitor21" or code == "Minitor22" or code == "Minitor23":
                login_app.login.check_logout1(self, "HTX DVVT HUYỆN LONG KHÁNH", var_app.data['login']['conhom_thuong_tk2'], var_app.data['login']['conhom_thuong_mk2'])
            if code == "Minitor24" or code == "Minitor25" or code == "Minitor26" or code == "Minitor27" or code == "Minitor28" or code == "Minitor29"\
                    or code == "Minitor30" or code == "Minitor31" or code == "Minitor32" or code == "Minitor33":
                login_app.login.check_logout1(self, "CTYANHNGOCMINH", var_app.data['login']['conhom_quantri_tk2'], var_app.data['login']['conhom_quantri_mk2'])
            if code == "Minitor34" or code == "Minitor35" or code == "Minitor36" or code == "Minitor37" or code == "Minitor38" or code == "Minitor39"\
                    or code == "Minitor40" or code == "Minitor41" or code == "Minitor42" or code == "Minitor43":
                login_app.login.check_logout1(self, "CÔNG TY TNHH MTV XDTM VÀ DVVT TRƯỜNG AN PHÁT", var_app.data['login']['khongnhom_thuong_tk3'], var_app.data['login']['khongnhom_thuong_mk3'])

            if code == "Minitor44" or code == "Minitor45" or code == "Minitor46" or code == "Minitor47" or code == "Minitor48" or code == "Minitor49"\
                    or code == "Minitor50" or code == "Minitor51" or code == "Minitor52" or code == "Minitor53":
                login_app.login.check_logout1(self, "43E02740", var_app.data['login']['conhom_quantri_tk'], var_app.data['login']['conhom_quantri_mk'])

            if code == "Minitor54" or code == "Minitor55" or code == "Minitor56" or code == "Minitor57" or code == "Minitor58" or code == "Minitor59"\
                    or code == "Minitor60" or code == "Minitor61" or code == "Minitor62" or code == "Minitor63":
                login_app.login.check_logout1(self, "43E02743", var_app.data['login']['conhom_thuong_tk'], var_app.data['login']['conhom_thuong_mk'])

            if code == "Minitor64" or code == "Minitor65" or code == "Minitor66" or code == "Minitor67" or code == "Minitor68" or code == "Minitor69" \
                    or code == "Minitor70" or code == "Minitor71" or code == "Minitor72" or code == "Minitor73":
                login_app.login.check_logout1(self, "KHÔNG NHÓM ĐỘI", var_app.data['login']['khongnhom_quantri_tk'], var_app.data['login']['khongnhom_quantri_mk'])

            if code == "Minitor64" or code == "Minitor75" or code == "Minitor76" or code == "Minitor77" or code == "Minitor78" or code == "Minitor79" \
                        or code == "Minitor80" or code == "Minitor81" or code == "Minitor82" or code == "Minitor83":
                    login_app.login.check_logout1(self, "KHÔNG NHÓM ĐỘI", var_app.data['login']['khongnhom_quantri_tk'], var_app.data['login']['khongnhom_quantri_mk'])

            var_app.driver.find_element(By.XPATH, var_app.vehicle_status_icon).click()

        time.sleep(1.5)

        get_status_vehicle(status_name)

        try:
            quantity = int(module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 109, 2))
        except:
            module_other_app.writeData1(var_app.path_luutamthoi, "Sheet1", 109, 2, 0)
            time.sleep(1)

        quantity = int(module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 109, 2))



        if path_image == "_GiamSat_TrangThai_DiChuyen.png" or path_image == "_GiamSat_TrangThai_BatMay.png" or path_image == "_GiamSat_TrangThai_Tatca.png":
            zoom("Thu nhỏ", 5)



        if quantity == 0:
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, "{}: {} phương tiện".format(status_name, quantity))
            module_other_app.write_result_not_displayed_try(code, eventname, result, "Giám sát - Trạng thái xe",
                                                    var_app.check_minotor_not_vehicle, path_image)

        else:
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, "{}: {} phương tiện".format(status_name, quantity))
            module_other_app.write_result_displayed_try(code, eventname, result, "Giám sát - Trạng thái xe",
                                                    var_app.check_minotor_not_vehicle, path_image)

        # check_logout_minitor = int(module_other_app.readData(var_app.path_luutamthoi, "Sheet2", 3, 2))
        # if check_logout_minitor == 1:
        #     module_other_app.close_app()


    def warm_passengers(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        login_app.login.login_v3(self, var_app.data['login']['test_canhbao_hanhkhach_tk'],var_app.data['login']['test_canhbao_hanhkhach_mk'])

        var_app.driver.find_element(By.XPATH, var_app.minitor).click()
        time.sleep(1)
        var_app.driver.find_element(By.XPATH, var_app.warm_passengers).click()
        time.sleep(3)
        module_other_app.write_result_text_try_if(code, eventname, result, "Giám sát - Icon Cảnh báo hành khách",
                                                    var_app.check_warm_passengers, "CẢNH BÁO HÀNH KHÁCH", "_GiamSat_CanhBaoKhanhKhach.png")
        module_other_app.close_app()


    def goto_google(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        login_app.login.login_v3(self, var_app.data['login']['conhom_quantri_tk'],var_app.data['login']['conhom_quantri_mk'])
        var_app.driver.find_element(By.XPATH, var_app.minitor).click()
        time.sleep(1)
        var_app.driver.find_element(By.XPATH, var_app.goto_google).click()
        time.sleep(3)
        try:
            var_app.driver.implicitly_wait(0.5)
            var_app.driver.find_element(By.XPATH, var_app.ALLOW).click()
            time.sleep(1.5)
        except:
            pass

        # module_other_app.write_result_text_try_if_cut(code, eventname, result, "Quản trị - Danh sách xe",
        #                                       var_app.check_goto_google, 0, 31, "https://www.google.com/maps/dir", "_GiamSat_Goto_Google.png")

        module_other_app.write_result_not_displayed_try(code, eventname, result, "Giám sát - Icon đi tới Google",
                                                    var_app.check_minitor, "_GiamSat_Goto_Google.png")

        var_app.driver.press_keycode(4)
        time.sleep(2)
        var_app.driver.press_keycode(4)
        time.sleep(2)


    def turn_on_location(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.5)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.find_element(By.XPATH, var_app.turn_on_location).click()
        except:
            login_app.login.login_v3(self, var_app.data['login']['conhom_quantri_tk'],var_app.data['login']['conhom_quantri_mk'])
            var_app.driver.find_element(By.XPATH, var_app.turn_on_location).click()
        time.sleep(2)

        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.ALLOW).click()
            time.sleep(1.5)
        except:
            pass
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.DENY).click()
            time.sleep(1.5)
        except:
            pass

        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.later).click()
            time.sleep(1.5)
        except:
            pass
        var_app.logging.info("--------------")
        var_app.logging.info("Giám sát - Icon bật vị trí")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("True")
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Pass")


    def icon_change_map(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.5)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.find_element(By.XPATH, var_app.minitor).click()
        except:
            login_app.login.login_v3(self, var_app.data['login']['conhom_quantri_tk'], var_app.data['login']['conhom_quantri_mk'])
            var_app.driver.find_element(By.XPATH, var_app.minitor).click()
        time.sleep(1)
        var_app.driver.find_element(By.XPATH, var_app.icon_change_map).click()
        time.sleep(2.5)
        var_app.logging.info("--------------")
        var_app.logging.info("Giám sát - Icon thay đổi map")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        try:
            map_type1 = var_app.driver.find_element(By.XPATH, var_app.map_type1).text
            map_type2 = var_app.driver.find_element(By.XPATH, var_app.map_type2).text
            map_type3 = var_app.driver.find_element(By.XPATH, var_app.map_type3).text
            map_type4 = var_app.driver.find_element(By.XPATH, var_app.map_type4).text

            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, f"{map_type1}, {map_type2}, {map_type3}, {map_type4}")
            var_app.logging.info(f"{map_type1}, {map_type2}, {map_type3}, {map_type4}")
            if (map_type1 == "Mặc định") and (map_type2 == "Vệ tinh") and (map_type3 == "Địa hình") and (map_type4 == "Giao thông"):
                var_app.logging.info("True")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Pass")
            else:
                var_app.logging.info("False")
                var_app.driver.save_screenshot(var_app.imagepath + code + "_GiamSat_IconMap.png")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Fail")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 13, code + "_GiamSat_IconMap.png")
        except:
            var_app.logging.info("False")
            var_app.driver.save_screenshot(var_app.imagepath + code + "_GiamSat_IconMap.png")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Fail")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 13, code + "_GiamSat_IconMap.png")

        var_app.driver.find_element(By.XPATH, var_app.map_type1).click()
        time.sleep(2)
        var_app.driver.find_element(By.XPATH, var_app.APPLY).click()
        time.sleep(3)








    def penalty_noticep(self, code, eventname, result):
        module_other_app.writeData1(var_app.path_luutamthoi, "Sheet1", 77, 2, "")
        module_other_app.writeData1(var_app.path_luutamthoi, "Sheet1", 77, 3, "")

        try:
            var_app.driver.implicitly_wait(0.5)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        login_app.login.login_v3(self, var_app.data['login']['binhanh_tk'], var_app.data['login']['binhanh_mk'])
        var_app.driver.find_element(By.XPATH, var_app.minitor).click()
        time.sleep(1)
        var_app.driver.find_element(By.XPATH, var_app.minitor).click()
        time.sleep(1.5)

        var_app.driver.find_element(By.XPATH, var_app.icon_company).click()
        time.sleep(2)
        var_app.driver.find_element(By.XPATH, var_app.icon_company_input).send_keys("7643")
        time.sleep(2)
        var_app.driver.find_element(By.XPATH, var_app.icon_goto_cty_search).click()
        time.sleep(2.5)
        var_app.driver.find_element(By.XPATH, var_app.icon_goto_cty_goto).click()

        time.sleep(2.5)
        not_yet_processed_out = var_app.driver.find_element(By.XPATH, var_app.not_yet_processed_out).text
        module_other_app.writeData1(var_app.path_luutamthoi, "Sheet1", 77, 2, not_yet_processed_out)
        var_app.driver.find_element(By.XPATH, var_app.icon_penalty_noticep).click()
        time.sleep(2.5)
        not_yet_processed_in = var_app.driver.find_element(By.XPATH, var_app.red_data).text
        module_other_app.writeData1(var_app.path_luutamthoi, "Sheet1", 77, 3, not_yet_processed_in)

        module_other_app.write_result_text_try_if(code, eventname, result, "Giám sát - Thông tin phạt nguội",
                                              var_app.check_penalty_noticep, "THÔNG TIN PHẠT NGUỘI", "_GiamSat_ThongTinPhatNguoi.png")

    def penalty_noticep_check_count(self, code, eventname, result):
        count_violet_out = module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 77, 2)
        count_violet_in = module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 77, 3)
        try:
            var_app.driver.implicitly_wait(0.5)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        if (count_violet_out == "None") or (count_violet_in == "None"):
            overview.penalty_noticep(self, "", "", "")

        var_app.logging.info("--------------")
        var_app.logging.info("Giám sát - Thông tin phạt nguội")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        try:
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, f"Số vi phạm màn giám sát: {count_violet_out}"
                                                                                    f"\nSố vi phạm màn THÔNG TIN PHẠT NGUỘI: {count_violet_in}")
            var_app.logging.info(f"Số vi phạm màn giám sát: {count_violet_out}\nSố vi phạm màn THÔNG TIN PHẠT NGUỘI: {count_violet_in}")
            if count_violet_out == count_violet_in:
                var_app.logging.info("True")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Pass")
            else:
                var_app.logging.info("False")
                var_app.driver.save_screenshot(var_app.imagepath + code + "_ThongTinPhatNguoi_SoLuongViPham.png")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Fail")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 13, code + "_ThongTinPhatNguoi_SoLuongViPham.png")
        except:
            var_app.logging.info("False")
            var_app.driver.save_screenshot(var_app.imagepath + code + "_ThongTinPhatNguoi_SoLuongViPham.png")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Fail")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 13, code + "_ThongTinPhatNguoi_SoLuongViPham.png")

    def penalty_noticep_search(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.5)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_penalty_noticep)
        except:
            overview.penalty_noticep(self, "", "", "")

        vehicle_list = var_app.driver.find_element(By.XPATH, var_app.penalty_noticep_vehicle).text

        var_app.driver.find_element(By.XPATH, var_app.penalty_noticep_search).click()
        time.sleep(2.5)
        var_app.driver.find_element(By.XPATH, var_app.penalty_noticep_search_input).send_keys(vehicle_list)
        time.sleep(2)
        try:
            var_app.driver.find_element(By.XPATH, var_app.penalty_noticep_checkbox1).click()
        except:
            module_other_app.tap_scaled(var_app.driver, [(37, 493)])
        time.sleep(1.5)
        var_app.driver.find_element(By.XPATH, var_app.SELECT).click()
        time.sleep(3)
        module_other_app.write_result_text_try_if(code, eventname, result, "Giám sát - Thông tin phạt nguội",
                                              var_app.check_penalty_noticep_search, vehicle_list, "_ThongTinPhatNguoi_TimKiem.png")

        var_app.driver.find_element(By.XPATH, var_app.penalty_noticep_search).click()
        time.sleep(2.5)
        try:
            var_app.driver.find_element(By.XPATH, var_app.penalty_noticep_checkbox_all).click()
        except:
            module_other_app.tap_scaled(var_app.driver, [(37, 392)])
        time.sleep(1)
        var_app.driver.find_element(By.XPATH, var_app.SELECT).click()
        time.sleep(3)

    def penalty_noticep_filter(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_penalty_noticep)
        except:
            overview.penalty_noticep(self, "", "", "")


        var_app.driver.find_element(By.XPATH, var_app.penalty_noticep_filter).click()
        time.sleep(2.5)
        module_other_app.write_result_text_try_if(code, eventname, result, "Giám sát - Thông tin phạt nguội",
                                              var_app.check_penalty_noticep_filter, "Trạng thái xử lý", "_ThongTinPhatNguoi_BoLoc.png")

        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.penalty_noticep_filter_x).click()
            time.sleep(1)
        except:
            pass

    def penalty_noticep_export_excel(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_penalty_noticep)
        except:
            overview.penalty_noticep(self, "", "", "")


        var_app.driver.find_element(By.XPATH, var_app.penalty_noticep_export_excel).click()
        time.sleep(2.5)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.ALLOW).click()
            time.sleep(2)
        except:
            pass

        module_other_app.write_result_not_displayed_try(code, eventname, result, "Giám sát - Thông tin phạt nguội",
                                              var_app.check_report_stop_export_excel, "_ThongTinPhatNguoi_XuatExcel.png")

        report_app.general.back_excel(self, 4, var_app.check_penalty_noticep)

    def penalty_noticep_check_info(self, code, eventname, result, path_name, path_data, name, name_image):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_penalty_noticep)
            var_app.driver.find_element(By.XPATH, var_app.penalty_noticep_eror_name)
        except:
            overview.penalty_noticep(self, "", "", "")

        var_app.logging.info("--------------")
        var_app.logging.info("Giám sát - Thông tin phạt nguội")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        try:
            check_name = var_app.driver.find_element(By.XPATH, path_name).text
            check_data = var_app.driver.find_element(By.XPATH, path_data).text

            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, f"{check_name}: {check_data}")
            var_app.logging.info(f"{check_name}: {check_data}")
            if (check_name == name) and (check_data != ""):
                var_app.logging.info("True")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Pass")
            else:
                var_app.logging.info("False")
                var_app.driver.save_screenshot(var_app.imagepath + code + name_image)
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Fail")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 13, code + name_image)
        except:
            var_app.logging.info("False")
            var_app.driver.save_screenshot(var_app.imagepath + code + name_image)
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Fail")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 13, code + name_image)

    def penalty_noticep_check_inf_orange(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_penalty_noticep)
        except:
            overview.penalty_noticep(self, "", "", "")

        var_app.logging.info("--------------")
        var_app.logging.info("Giám sát - Thông tin phạt nguội")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)

        try:
            phuongtienvipham = var_app.driver.find_element(By.XPATH, var_app.blu_data).text
            daxuly = var_app.driver.find_element(By.XPATH, var_app.green_data).text
            chuaxuly = var_app.driver.find_element(By.XPATH, var_app.red_data).text
            tongsovipham = var_app.driver.find_element(By.XPATH, var_app.orange_data).text

            tongsovipham_name = var_app.driver.find_element(By.XPATH, var_app.orange_name).text

            sum_tongsovipham = int(daxuly) + int(chuaxuly)


            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, f"{tongsovipham_name}: {tongsovipham}\nPHƯƠNG TIỆN VI PHẠM: {phuongtienvipham}"
                                                                                    f"ĐÃ XỬ LÝ: {daxuly}\nCHƯA XỬ LÝ: {chuaxuly}")

            var_app.logging.info(f"{tongsovipham_name}: {tongsovipham}\nPHƯƠNG TIỆN VI PHẠM: {phuongtienvipham}"
                                                                                    f"ĐÃ XỬ LÝ: {daxuly}\nCHƯA XỬ LÝ: {chuaxuly}")

            if (tongsovipham_name == "TỔNG SỐ VI PHẠM") and (int(tongsovipham) == sum_tongsovipham):
                var_app.logging.info("True")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Pass")
            else:
                var_app.logging.info("False")
                var_app.driver.save_screenshot(var_app.imagepath + code + "_ThongTinPhatNguoi_TongSoViPham.png")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Fail")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 13, code + "_ThongTinPhatNguoi_TongSoViPham.png")
        except:
            var_app.logging.info("False")
            var_app.driver.save_screenshot(var_app.imagepath + code + "_ThongTinPhatNguoi_TongSoViPham.png")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Fail")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 13, code + "_ThongTinPhatNguoi_TongSoViPham.png")

    def penalty_noticep_link(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_penalty_noticep)
        except:
            overview.penalty_noticep(self, "", "", "")


        var_app.driver.find_element(By.XPATH, var_app.penalty_noticep_link).click()
        time.sleep(5)
        # module_other_app.write_result_text_try_if(code, eventname, result, "Giám sát - Thông tin phạt nguội",
        #                                           var_app.check_penalty_noticep_link, "BỘ CÔNG AN - CỤC CẢNH SÁT GIAO THÔNG",
        #                                           "_ThongTinPhatNguoi_Link.png")
        module_other_app.write_result_not_displayed_try(code, eventname, result, "Giám sát - Thông tin phạt nguội",
                                                  var_app.penalty_noticep_link, "_ThongTinPhatNguoi_Link.png")

        #

        report_app.general.back_excel(self, 2, var_app.check_penalty_noticep)

    def penalty_noticep_route(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_penalty_noticep)
            var_app.driver.find_element(By.XPATH, var_app.penalty_noticep_eror_name)
        except:
            overview.penalty_noticep(self, "", "", "")


        time_violet = var_app.driver.find_element(By.XPATH, var_app.penalty_noticep_time_data).text

        try:
            var_app.driver.find_element(By.XPATH, var_app.route1)
        except:
            module_other_app.swipe_scaled(var_app.driver, 400, 1350, 400, 1150, 1000)
        time.sleep(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.see_route).click()
        except:
            module_other_app.swipe_scaled(var_app.driver, 400, 1350, 400, 1000, 1000)
            time.sleep(1)
            var_app.driver.find_element(By.XPATH, var_app.see_route).click()
        time.sleep(2.5)
        var_app.logging.info("--------------")
        var_app.logging.info("Giám sát - Thông tin phạt nguội")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)

        try:
            not_route = var_app.driver.find_element(By.XPATH, var_app.not_route).text
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, f"{not_route}")
            var_app.logging.info("True")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Pass")
        except:
            try:
                module_other_app.tap_scaled(var_app.driver, [(46, 1554)])
            except:
                var_app.driver.find_element(By.XPATH, var_app.icon_pause).click()
            time.sleep(1.5)
            var_app.driver.find_element(By.XPATH, var_app.icon_3_gach).click()
            time.sleep(2)
            time_violet_route = var_app.driver.find_element(By.XPATH, var_app.time_violet_route).text

            fmt = "%H:%M:%S %d/%m/%Y"
            time_violet = datetime.strptime(time_violet, fmt)
            time_violet_route = datetime.strptime(time_violet_route, fmt)

            # Tính chênh lệch thời gian
            diff = abs(time_violet - time_violet_route)

            # So sánh
            if diff.total_seconds() <= 120:
                print("Hai thời gian xem như bằng nhau (chênh không quá 2 phút).")
            else:
                print("Hai thời gian khác nhau quá 2 phút.")

            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, f"Thời gian vi phạm: {time_violet}\n"
                                                                                    f"Thời gian lộ trình: {time_violet_route}\n"
                                                                                    f"Thời gian chênh: {diff.total_seconds()}")
            if diff.total_seconds() <= 121:
                var_app.logging.info("True")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Pass")
            else:
                var_app.logging.info("False")
                var_app.driver.save_screenshot(var_app.imagepath + code + "_ThongTinPhatNguoi_LoTrinh.png")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Fail")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 13, code + "_ThongTinPhatNguoi_LoTrinh.png")













    def share_vehicle(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.5)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.find_element(By.XPATH, var_app.minitor).click()
        except:
            login_app.login.login_v3(self, var_app.data['login']['conhom_quantri_tk'], var_app.data['login']['conhom_quantri_mk'])
            var_app.driver.find_element(By.XPATH, var_app.minitor).click()
        time.sleep(1)
        var_app.driver.find_element(By.XPATH, var_app.icon_share_vehicle).click()
        time.sleep(2.5)
        module_other_app.write_result_text_try_if(code, eventname, result, "Giám sát - Chia sẻ phương tiện",
                                              var_app.check_share_vehicle, "CHIA SẺ PHƯƠNG TIỆN", "_GiamSat_ChiaSePhuongTien.png")


    def share_vehicle_create(self, code, eventname, result, page, path_check, desire, name_image):
        try:
            var_app.driver.implicitly_wait(0.5)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_share_vehicle)
            var_app.driver.find_element(By.XPATH, var_app.coordinates)
        except:
            overview.share_vehicle(self, "", "", "")

        var_app.driver.find_element(By.XPATH, var_app.share_vehicle_page).click()
        time.sleep(2.5)
        try:
            var_app.driver.find_element(By.XPATH, var_app.select_share_vehicle_page + "//*[@text='" + page + "']")
        except:
            var_app.driver.find_element(By.XPATH, var_app.share_vehicle_page_back).click()
            time.sleep(2.5)
            var_app.driver.find_element(By.XPATH, var_app.share_vehicle_page).click()
            time.sleep(2.5)

        var_app.driver.find_element(By.XPATH, var_app.select_share_vehicle_page + "//*[@text='"+page+"']").click()
        time.sleep(2)

        var_app.driver.find_element(By.XPATH, var_app.share_vehicle_group).click()
        time.sleep(2.5)
        try:
            var_app.driver.find_element(By.XPATH, var_app.share_vehicle_group_all).click()
        except:
            module_other_app.tap_scaled(var_app.driver, [(37, 392)])
        time.sleep(1)
        var_app.driver.find_element(By.XPATH, var_app.SELECT).click()
        time.sleep(2.5)


        var_app.driver.find_element(By.XPATH, var_app.share_vehicle_vehicle).click()
        time.sleep(2.5)
        try:
            var_app.driver.find_element(By.XPATH, var_app.share_vehicle_vehicle1).click()
        except:
            module_other_app.tap_scaled(var_app.driver, [(40, 493)])
        time.sleep(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.SELECT).click()
            time.sleep(2.5)
        except:
            pass

        var_app.driver.find_element(By.XPATH, var_app.start_share)
        var_app.driver.find_element(By.XPATH, var_app.end_share)


        if page == "Lộ trình":
            var_app.driver.find_element(By.XPATH, var_app.time_end_share)
            var_app.driver.find_element(By.XPATH, var_app.display_company).click()
            time.sleep(1)
            var_app.driver.find_element(By.XPATH, var_app.coordinates).click()
            time.sleep(1)
            var_app.driver.find_element(By.XPATH, var_app.all).click()
            time.sleep(1)
        else:
            var_app.driver.find_element(By.XPATH, var_app.coordinates).click()
            time.sleep(1)
            var_app.driver.find_element(By.XPATH, var_app.gplx).click()
            time.sleep(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.CREATE_AND_SHARE).click()
        except:
            var_app.driver.find_element(By.XPATH, var_app.SELECT).click()
            time.sleep(2.5)
            var_app.driver.find_element(By.XPATH, var_app.CREATE_AND_SHARE).click()
        time.sleep(2.5)
        module_other_app.write_result_text_try_if(code, eventname, result, "Giám sát - Chia sẻ phương tiện",
                                              path_check, desire, name_image)

        var_app.driver.press_keycode(4)
        time.sleep(2)


    def share_vehicle_link(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.5)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.find_element(By.XPATH, var_app.share_vehicle_link)
        except:
            overview.share_vehicle_create(self, "", "", "", "Lộ trình", "", "", "")




        try:
            var_app.driver.find_element(By.XPATH, var_app.share_vehicle_link1)
            module_other_app.write_result_text_try_if_other(code, eventname, result, "Giám sát - Chia sẻ phương tiện",
                                                            var_app.check_share_vehicle_link1, "","__ChiaSePhuongTien_LienKetChiaSe.png")
            var_app.driver.find_element(By.XPATH, var_app.share_vehicle_link1).click()

        except:
            module_other_app.write_result_text_try_if_other(code, eventname, result, "Giám sát - Chia sẻ phương tiện",
                                                            var_app.check_share_vehicle_link, "","__ChiaSePhuongTien_LienKetChiaSe.png")

            var_app.driver.find_element(By.XPATH, var_app.share_vehicle_link).click()


        time.sleep(2.5)
        var_app.driver.press_keycode(4)
        time.sleep(2)





    def enter_temperature(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.5)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(5)
        # login_app.login.login_v3(self, var_app.data['login']['testlaixe111_tk'], var_app.data['login']['testlaixe111_mk'])
        login_app.login.login_READED(self, var_app.data['login']['testlaixe111_tk'], var_app.data['login']['testlaixe111_mk'], "", "", "", "", "", "")

        var_app.driver.find_element(By.XPATH, var_app.minitor).click()
        time.sleep(1)
        var_app.driver.find_element(By.XPATH, var_app.minitor).click()
        time.sleep(1.5)
        var_app.driver.find_element(By.XPATH, var_app.icon_enter_temperature).click()
        time.sleep(2.5)
        module_other_app.write_result_text_try_if(code, eventname, result, "Giám sát - Nhập nhiệt độ",
                                              var_app.check_enter_temperature, "NHẬP NHIỆT ĐỘ", "_GiamSat_NhapNhietDo.png")

    def enter_temperature_save(self, code, eventname, result, temperature):
        module_other_app.writeData1(var_app.path_luutamthoi, "Sheet1", 76, 2, "")
        try:
            var_app.driver.implicitly_wait(0.5)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_enter_temperature)
        except:
            overview.enter_temperature(self, "", "", "")

        var_app.driver.find_element(By.XPATH, var_app.enter_temperature_vehicle).click()
        time.sleep(2.5)
        try:
            vehicle = var_app.driver.find_element(By.XPATH, var_app.enter_temperature_vehicle2).text
        except:
            var_app.driver.find_element(By.XPATH, var_app.enter_temperature_vehicle_back).click()
            time.sleep(2.5)
            var_app.driver.find_element(By.XPATH, var_app.enter_temperature_vehicle).click()
            time.sleep(2.5)

        vehicle = var_app.driver.find_element(By.XPATH, var_app.enter_temperature_vehicle2).text
        module_other_app.writeData1(var_app.path_luutamthoi, "Sheet1", 76, 2, vehicle)
        var_app.driver.find_element(By.XPATH, var_app.enter_temperature_vehicle2).click()
        time.sleep(2.5)
        var_app.driver.find_element(By.XPATH, var_app.enter_temperature_time)
        var_app.driver.find_element(By.XPATH, var_app.enter_temperature_temperature).send_keys(temperature)
        time.sleep(0.5)
        var_app.driver.find_element(By.XPATH, var_app.SAVE).click()

        wait = WebDriverWait(var_app.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, var_app.enter_temperature_success)))
        module_other_app.write_result_text_try_if(code, eventname, result, "Giám sát - Nhập nhiệt độ",
                                              var_app.enter_temperature_success, "Nhập nhiệt độ thành công", "_GiamSat_NhapNhietDo_Luu.png")

        time.sleep(1)
        var_app.driver.find_element(By.XPATH, var_app.enter_temperature_x).click()
        time.sleep(2)

    def enter_temperature_check(self, code, eventname, result):
        module_other_app.writeData1(var_app.path_luutamthoi, "Sheet1", 76, 3, "")

        var_app.driver.implicitly_wait(5)
        try:
            var_app.driver.implicitly_wait(0.5)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        try:
            var_app.driver.implicitly_wait(0.5)#
            var_app.driver.find_element(By.XPATH, var_app.icon_enter_temperature)
            var_app.driver.find_element(By.XPATH, var_app.search_vehicle).click()
            time.sleep(3)
            var_app.driver.find_element(By.XPATH, var_app.check_enter_temperature)
        except:
            module_other_app.reset_driver()
            overview.enter_temperature_save(self, "", "", "", 50)
            var_app.driver.find_element(By.XPATH, var_app.search_vehicle).click()
            time.sleep(3)

        var_app.driver.implicitly_wait(2)
        vehicle = module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 76, 2)

        #m111
        try:
            print("n1")
            wait = WebDriverWait(var_app.driver, 10)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_app.search_vehicle_input))).click()
            print("n2")
            try:
                var_app.driver.find_element(By.XPATH, var_app.search_vehicle_input).send_keys(vehicle)
            except:
                var_app.driver.execute_script("mobile: type", {"text": vehicle})
            print("n3")
        except:
            print("n4")
            var_app.driver.find_element(By.XPATH, var_app.search_vehicle).click()
            time.sleep(2)
            print("n5")
            var_app.driver.find_element(By.XPATH, var_app.search_vehicle_input).send_keys(vehicle)
            print("n6")
        time.sleep(1.5)
        module_other_app.tap_scaled(var_app.driver, [(193, 352)])
        time.sleep(2.5)
        var_app.driver.find_element(By.XPATH, var_app.detail_vehicle).click()
        time.sleep(2.5)
        module_other_app.swipe_scaled(var_app.driver, 400, 1350, 400, 1150, 1000)
        time.sleep(1)
        status_general_information3("Nhiệt độ", 76)

        temperature = module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 76, 3)
        temperature1 = ''.join(re.findall(r'\d+', temperature))

        var_app.logging.info("--------------")
        var_app.logging.info("Nhập nhiệt độ")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        try:
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, f"Phương tiện: {vehicle}\nNhiệt độ nhập: 50\nNhiệt độ hiển thị: {temperature}")
            var_app.logging.info(f"Phương tiện: {vehicle}\nNhiệt độ nhập: 50\nNhiệt độ hiển thị: {temperature}")
            if temperature1 == "50":
                var_app.logging.info("True")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Pass")
            else:
                var_app.logging.info("False")
                var_app.driver.save_screenshot(var_app.imagepath + code + "_GiamSat_NhapNhietDo_CheckSauLuu.png")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Fail")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 13, code + "_GiamSat_NhapNhietDo_CheckSauLuu.png")
        except:
            var_app.logging.info("False")
            var_app.driver.save_screenshot(var_app.imagepath + code + "_GiamSat_NhapNhietDo_CheckSauLuu.png")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Fail")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 13, code + "_GiamSat_NhapNhietDo_CheckSauLuu.png")

        # var_app.driver.find_element(By.XPATH, var_app.detail_vehicle_x).click()
        # time.sleep(2.5)
        # overview.enter_temperature_save(self, "", "", "", 43)






    def find_a_branch(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.5)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(5)
        login_app.login.login_v3(self, var_app.data['login']['khongnhom_quantri_tk'], var_app.data['login']['khongnhom_quantri_mk'])

        var_app.driver.find_element(By.XPATH, var_app.minitor).click()
        time.sleep(1)
        var_app.driver.find_element(By.XPATH, var_app.minitor).click()
        time.sleep(1.5)
        var_app.driver.find_element(By.XPATH, var_app.icon_find_a_branch).click()
        time.sleep(2.5)
        module_other_app.write_result_text_try_if(code, eventname, result, "Giám sát - Tìm điểm chi nhánh",
                                              var_app.check_find_a_branch, "TÌM ĐIỂM CHI NHÁNH", "_GiamSat_TimDiemChiNhanh.png")


    def find_a_branch_search(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.5)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_find_a_branch)
        except:
            overview.find_a_branch(self, "", "", "")

        try:
            name = var_app.driver.find_element(By.XPATH, var_app.branch_field1)
        except:
            var_app.driver.find_element(By.XPATH, var_app.branch_back).click()
            time.sleep(2.5)
            var_app.driver.find_element(By.XPATH, var_app.icon_find_a_branch).click()
            time.sleep(2.5)

        name_branch = var_app.driver.find_element(By.XPATH, var_app.branch_field1).text

        var_app.driver.find_element(By.XPATH, var_app.branch_search_input).clear()
        time.sleep(0.5)
        var_app.driver.find_element(By.XPATH, var_app.branch_search_input).send_keys(name_branch)
        time.sleep(2)
        module_other_app.write_result_text_try_if(code, eventname, result, "Giám sát - Tìm điểm chi nhánh",
                                              var_app.branch_field1, name_branch, "_TimDiemChiNhanh_TimKiem.png")

        var_app.driver.find_element(By.XPATH, var_app.branch_search_input).clear()
        time.sleep(0.5)


    def find_a_branch_setting(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.5)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_find_a_branch)
        except:
            overview.find_a_branch(self, "", "", "")

        try:
            name = var_app.driver.find_element(By.XPATH, var_app.branch_field1)
        except:
            var_app.driver.find_element(By.XPATH, var_app.branch_back).click()
            time.sleep(2.5)
            var_app.driver.find_element(By.XPATH, var_app.icon_find_a_branch).click()
            time.sleep(2.5)


        var_app.driver.find_element(By.XPATH, var_app.branch_setting).click()
        time.sleep(2.5)
        var_app.driver.find_element(By.XPATH, var_app.branch_setting_input).clear()
        time.sleep(0.5)
        var_app.driver.find_element(By.XPATH, var_app.branch_setting_input).send_keys("60")
        time.sleep(0.5)
        var_app.driver.find_element(By.XPATH, var_app.APPLY).click()
        time.sleep(2.5)


        var_app.logging.info("--------------")
        var_app.logging.info("Giám sát - Tìm điểm chi nhánh")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        try:
            popup = var_app.driver.find_element(By.XPATH, var_app.branch_setting).text
            km = var_app.driver.find_element(By.XPATH, var_app.branch_field2).text
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, f"Popup cài đặt: {popup}\nKhoảng cách điểm: {km}")
            var_app.logging.info(f"Popup cài đặt: {popup}\nKhoảng cách điểm: {km}")

            popup = float(popup)  # popup = "60" → 60.0
            km_cv = float(km.split()[0].replace(",", "."))

            if (popup == 60.0) and (km_cv < 60):
                var_app.logging.info(f"Popup cài đặt: {popup}\nKhoảng cách điểm: {km_cv}")
                var_app.logging.info("True")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Pass")
            else:
                var_app.logging.info("False")
                var_app.driver.save_screenshot(var_app.imagepath + code + "_TimDiemChiNhanh_CaiDatBanKinh.png")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Fail")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 13, code + "_TimDiemChiNhanh_CaiDatBanKinh.png")
        except:
            var_app.logging.info("False")
            var_app.driver.save_screenshot(var_app.imagepath + code + "_TimDiemChiNhanh_CaiDatBanKinh.png")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Fail")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 13, code + "_TimDiemChiNhanh_CaiDatBanKinh.png")


    def find_a_branch_filter(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.5)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_find_a_branch)
        except:
            overview.find_a_branch(self, "", "", "")

        var_app.driver.find_element(By.XPATH, var_app.branch_filter).click()
        time.sleep(2.5)

        var_app.logging.info("--------------")
        var_app.logging.info("Giám sát - Tìm điểm chi nhánh")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        try:
            branch_filter1_name = var_app.driver.find_element(By.XPATH, var_app.branch_filter1_name).text
            branch_filter1_data = var_app.driver.find_element(By.XPATH, var_app.branch_filter1_data).text

            branch_filter2_name = var_app.driver.find_element(By.XPATH, var_app.branch_filter2_name).text
            branch_filter2_data = var_app.driver.find_element(By.XPATH, var_app.branch_filter2_data).text

            branch_filter3_name = var_app.driver.find_element(By.XPATH, var_app.branch_filter3_name).text
            branch_filter3_data = var_app.driver.find_element(By.XPATH, var_app.branch_filter3_data).text

            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, f"{branch_filter1_name}\n{branch_filter1_data}\n\n"
                                                                                    f"{branch_filter2_name}\n{branch_filter2_data}\n\n"
                                                                                    f"{branch_filter3_name}\n{branch_filter3_data}")

            var_app.logging.info(f"{branch_filter1_name}\n{branch_filter1_data}\n\n"
                                f"{branch_filter2_name}\n{branch_filter2_data}\n\n"
                                f"{branch_filter3_name}\n{branch_filter3_data}")

            if (branch_filter1_name == "Tất cả") and (branch_filter1_data != "") and (branch_filter2_name != "") \
                    and (branch_filter2_data != "") and (branch_filter3_name != "") and (branch_filter3_data != ""):
                var_app.logging.info("True")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Pass")
            else:
                var_app.logging.info("False")
                var_app.driver.save_screenshot(var_app.imagepath + code + "_TimDiemChiNhanh_Filter.png")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Fail")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 13, code + "_TimDiemChiNhanh_Filter.png")
        except:
            var_app.logging.info("False")
            var_app.driver.save_screenshot(var_app.imagepath + code + "_TimDiemChiNhanh_Filter.png")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Fail")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 13, code + "_TimDiemChiNhanh_Filter.png")

        module_other_app.tap_scaled(var_app.driver, [(265, 210)])
        time.sleep(1)
        var_app.driver.find_element(By.XPATH, var_app.branch_search_input).click()
        time.sleep(1)


    def find_a_branch_other(self, code, eventname, result, path_check, name_image):
        try:
            var_app.driver.implicitly_wait(0.5)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_find_a_branch)
        except:
            overview.find_a_branch(self, "", "", "")

        try:
            name = var_app.driver.find_element(By.XPATH, var_app.branch_field1)
        except:
            var_app.driver.find_element(By.XPATH, var_app.branch_back).click()
            time.sleep(2.5)
            var_app.driver.find_element(By.XPATH, var_app.icon_find_a_branch).click()
            time.sleep(2.5)

        module_other_app.write_result_text_try_if_other(code, eventname, result, "Giám sát - Tìm điểm chi nhánh",
                                              path_check, "", name_image)


    def find_a_branch_button(self, code, eventname, result, button, name_image):
        try:
            var_app.driver.implicitly_wait(0.5)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_find_a_branch)
        except:
            overview.find_a_branch(self, "", "", "")

        try:
            name = var_app.driver.find_element(By.XPATH, var_app.branch_field1)
        except:
            var_app.driver.find_element(By.XPATH, var_app.branch_back).click()
            time.sleep(2.5)
            var_app.driver.find_element(By.XPATH, var_app.icon_find_a_branch).click()
            time.sleep(2.5)

        try:
            wait = WebDriverWait(var_app.driver, 10)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, button)))
            element.click()
        except:
            pass

        time.sleep(2)
        try:
            var_app.driver.implicitly_wait(0.5)
            var_app.driver.find_element(By.XPATH, var_app.ALLOW).click()
            time.sleep(1.5)
        except:
            pass
        time.sleep(5)

        module_other_app.write_result_not_displayed_try(code, eventname, result, "Giám sát - Tìm điểm chi nhánh",
                                              var_app.check_find_a_branch, name_image)

        if name_image == "_TimDiemChiNhanh_IconGGMap":
            module_other_app.reset_app_image()










class detail:

    def detail_vehicle(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        login_app.login.login_v3(self, var_app.data['login']['conhom_quantri_tk'], var_app.data['login']['conhom_quantri_mk'])

        try:
            var_app.driver.find_element(By.XPATH, var_app.detail_vehicle_choose1).click()
        except:
            login_app.login.login_v3(self, var_app.data['login']['conhom_quantri_tk'], var_app.data['login']['conhom_quantri_mk'])
            var_app.driver.find_element(By.XPATH, var_app.detail_vehicle_choose1).click()
        time.sleep(2.5)


        try:
            check_detail = var_app.driver.find_element(By.XPATH, var_app.detail_vehicle)
        except:
            module_other_app.swipe_scaled(var_app.driver, 730, 1360, 160, 1360, 1000)
            time.sleep(1)

        try:
            check_detail = var_app.driver.find_element(By.XPATH, var_app.detail_vehicle)
        except:
            var_app.driver.find_element(By.XPATH, var_app.setting).click()
            time.sleep(2.5)
            var_app.driver.find_element(By.XPATH, var_app.detail_custom_search_input).clear()
            time.sleep(0.5)
            var_app.driver.find_element(By.XPATH, var_app.detail_custom_search_input).send_keys("Chi tiết")
            time.sleep(2)
            var_app.driver.find_element(By.XPATH, var_app.favorite_path_detail).click()
            time.sleep(1)
            var_app.driver.find_element(By.XPATH, var_app.setup_favorite_save).click()
            time.sleep(3)


        try:
            var_app.driver.find_element(By.XPATH, var_app.detail_vehicle_choose1).click()
            time.sleep(2.5)
        except:
            pass

        try:
            check_detail = var_app.driver.find_element(By.XPATH, var_app.detail_vehicle)
        except:
            module_other_app.swipe_scaled(var_app.driver, 730, 1360, 160, 1360, 1000)
            time.sleep(1)

        get_detail(var_app.overview_vehicleplate, 6, 2)
        get_detail(var_app.overview_time, 7, 2)
        get_detail(var_app.overview_adress, 14, 2)
        get_detail(var_app.overview_speed, 8, 2)
        get_detail(var_app.overview_engine, 12, 2)
        get_detail(var_app.overview_ari_condition, 13, 2)
        get_detail(var_app.overview_ari_vehicle_door, 18, 2)
        bienso = module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 6, 2)
        call_api950(bienso)

        try:
            var_app.driver.find_element(By.XPATH, var_app.detail_vehicle).click()
        except:
            module_other_app.swipe_scaled(var_app.driver, 675, 1360, 234, 1360, 1000)
            time.sleep(1)
            var_app.driver.find_element(By.XPATH, var_app.detail_vehicle).click()
        time.sleep(2.5)

        #info vehicle
        get_detail(var_app.detail_number_sim, 19, 3)
        get_detail(var_app.detail_registration_date, 20, 3)

        status_general_information("Biển kiểm soát", 6)
        status_general_information("Địa chỉ", 14)
        status_general_information("Thời gian", 7)
        status_general_information("Vận tốc", 8)
        status_general_information("Động cơ", 12)
        status_general_information("KM trong ngày", 10)
        status_general_information("KM tích luỹ", 22)
        status_general_information("Dừng đỗ", 11)
        status_general_information("Đang đỗ", 59)
        status_general_information("Dừng đỗ nổ máy", 60)
        status_general_information("Điều hoà", 13)
        time.sleep(1)
        module_other_app.swipe_scaled(var_app.driver, 400, 1350, 450, 400, 500)
        time.sleep(1)
        status_general_information2("Bình 1", 16)
        status_general_information2("Nhiên liệu", 16)
        time.sleep(1)
        module_other_app.swipe_scaled(var_app.driver, 400, 1350, 450, 400, 500)
        time.sleep(1)
        status_general_information1("Nhiệt độ", 17)
        status_general_information1("Thẻ nhớ", 24)
        status_general_information1("Nhóm đội", 25)
        status_general_information1("Số lần mở cửa", 23)



        get_detail(var_app.detail_driver, 26, 3)
        get_detail(var_app.detail_driver_liscense, 27, 3)
        get_detail(var_app.detail_phone_number, 28, 3)
        get_detail(var_app.detail_continuous_driving_time, 29, 3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.detail_driving_time_during_the_day)
        except:
            module_other_app.swipe_scaled(var_app.driver, 500, 1000, 500, 500, 1000)
            time.sleep(2)
        get_detail(var_app.detail_driving_time_during_the_day, 30, 3)
        get_detail(var_app.detail_driving_time_during_the_week, 74, 3)
        get_detail(var_app.detail_too_speed, 31, 3)
        get_detail(var_app.detail_management_department, 32, 3)


        #devide
        var_app.driver.find_element(By.XPATH, var_app.detail_vehicle_device).click()
        time.sleep(1.5)
        get_detail(var_app.detail_vin, 36, 3)
        get_detail(var_app.detail_the_first_active, 61, 3)
        get_detail(var_app.detail_most_recent_news, 62, 3)
        get_detail(var_app.detail_status_gps, 63, 3)
        get_detail(var_app.detail_number_sim2, 64, 3)
        get_detail(var_app.detail_subscription_type, 65, 3)
        get_detail(var_app.detail_the_remaining_amount, 69, 3)
        get_detail(var_app.detail_status_sim, 70, 3)
        get_detail(var_app.detail_time_update, 71, 3)
        get_detail(var_app.detail_battery_level, 66, 3)
        get_detail(var_app.detail_power_status, 67, 3)

        #Camera



        var_app.driver.find_element(By.XPATH, var_app.detail_vehicle_camera1).click()
        time.sleep(1.5)
        get_detail(var_app.detail_package_name, 37, 3)
        get_detail(var_app.detail_home_network, 38, 3)
        get_detail(var_app.detail_package_capacity, 39, 3)
        get_detail(var_app.detail_number_of_days_of_storage, 40, 3)
        get_detail(var_app.detail_number_of_channel_of_storage, 41, 3)
        get_detail(var_app.detail_location, 42, 3)
        get_detail(var_app.detail_image, 43, 3)
        get_detail(var_app.detail_video, 44, 3)
        get_detail(var_app.detail_channel_camera, 45, 3)
        get_detail(var_app.detail_channel_active, 46, 3)
        get_detail(var_app.detail_connection_network, 68, 3)

        var_app.driver.press_keycode(4)
        time.sleep(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.overview_vehicleplate)
            var_app.driver.press_keycode(4)
            time.sleep(2)
        except:
            pass
        var_app.logging.info("--------------")
        var_app.logging.info("Giám sát - Thông tin chi tiết xe")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("True")
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Pass")


    def detail_vehicle_sim_number1(self, code, eventname, result):
        vehicle_sim1 = str(module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 19, 3))
        vehicle_sim2 = str(module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 64, 3))
        var_app.logging.info("--------------")
        var_app.logging.info("Giám sát - Thông tin chi tiết xe")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("Hiện trạng - Số SIM" + vehicle_sim1)
        var_app.logging.info("Thiết bị - Số SIM" + vehicle_sim2)
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, "Hiện trạng: {}\nThiết bị: {}".format(vehicle_sim1, vehicle_sim2))
        if vehicle_sim1 == vehicle_sim2:
            var_app.logging.info("True")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Pass")
        else:
            var_app.logging.info("False")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Fail")


    def detail_vehicle_day_register(self, code, eventname, result):
        check_detail = str(module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 20, 3))
        print("dettail: " + check_detail)
        var_app.logging.info("--------------")
        var_app.logging.info("Giám sát - Thông tin chi tiết xe")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("Hiện trạng - Ngày đăng ký - " + check_detail)
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, "Hiện trạng: {}".format(check_detail))
        if check_detail != "None":
            var_app.logging.info("True")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Pass")
        else:
            var_app.logging.info("False")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Fail")


    def detail_vehicle_liscense_plate(self, code, eventname, result):
        vehicle_overview = str(module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 6, 2))
        vehicle_detail = str(module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 6, 3))
        var_app.logging.info("--------------")
        var_app.logging.info("Giám sát - Thông tin chi tiết xe")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("Tổng quan - biển số xe - " + vehicle_overview)
        var_app.logging.info("Hiện trạng - biển số xe - " + vehicle_detail)
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, "Tổng quan: {}\nHiện trạng: {}".format(vehicle_overview, vehicle_detail))
        if vehicle_overview[0:8] == vehicle_detail[0:8]:
            var_app.logging.info("True")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Pass")
        else:
            var_app.logging.info("False")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Fail")


    def detail_vehicle_adress(self, code, eventname, result):
        check_overview = str(module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 14, 2))
        print("overview: " + check_overview)

        check_detail = str(module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 14, 3))
        print("detail: " + check_detail)
        var_app.logging.info("--------------")
        var_app.logging.info("Giám sát - Thông tin chi tiết xe")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("Tổng quan - Địa chỉ - " + check_overview)
        var_app.logging.info("Hiện trạng - Địa chỉ - " + check_detail)
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, "Tổng quan: {}\nHiện trạng: {}".format(check_overview, check_detail))
        if check_overview == check_detail:
            var_app.logging.info("True")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Pass")
        else:
            var_app.logging.info("False")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Fail")


    def detail_vehicle_time_update(self, code, eventname, result):
        check_overview = str(module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 7, 2))
        check_overview_hour_minute = check_overview[0:5]
        print("overview: " + check_overview_hour_minute)
        check_overview_day_month_year = check_overview[9::]
        print("overview: " + check_overview_day_month_year)
        check_overview = check_overview_hour_minute + " " + check_overview_day_month_year
        print("overview: " + check_overview)

        check_detail = str(module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 7, 3))
        check_detail_hour_minute = check_detail[0:5]
        print("detail: " + check_detail_hour_minute)
        check_detail_day_month_year = check_detail[9::]
        print("detail: " + check_detail_day_month_year)
        check_detail = check_detail_hour_minute + " " + check_detail_day_month_year
        print("detail: " + check_detail)

        var_app.logging.info("--------------")
        var_app.logging.info("Giám sát - Thông tin chi tiết xe")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("Tổng quan - Thời gian - " + check_overview)
        var_app.logging.info("Hiện trạng - Thời gian - " + check_detail)
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, "Tổng quan: {}\nHiện trạng: {}".format(check_overview, check_detail))
        if check_overview == check_detail:
            var_app.logging.info("True")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Pass")
        else:
            var_app.logging.info("False")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Fail")


    def detail_vehicle_speed_gps(self, code, eventname, result):
        check_overview = str(module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 8, 2))
        print("overview: " + check_overview)

        check_detail = str(module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 8, 3))
        print("detail: " + check_detail)

        var_app.logging.info("--------------")
        var_app.logging.info("Giám sát - Thông tin chi tiết xe")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("Tổng quan - Vận tốc gps - " + check_overview)
        var_app.logging.info("Hiện trạng - Vận tốc gps - " + check_detail)
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, "Tổng quan: {}\nHiện trạng: {}".format(check_overview, check_detail))
        if check_overview == check_detail:
            var_app.logging.info("True")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Pass")
        else:
            var_app.logging.info("False")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Fail")


    def detail_vehicle_engine(self, code, eventname, result):
        check_overview = str(module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 12, 2))
        print("overview: " + check_overview)
        check_detail = str(module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 12, 3))
        print("detail: " + check_detail)

        var_app.logging.info("--------------")
        var_app.logging.info("Giám sát - Thông tin chi tiết xe")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("Tổng quan - Động cơ - " + check_overview)
        var_app.logging.info("Hiện trạng - Động cơ - " + check_detail)
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, "Tổng quan: {}\nHiện trạng: {}".format(check_overview, check_detail))
        if check_overview == check_detail:
            var_app.logging.info("True")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Pass")
        else:
            var_app.logging.info("False")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Fail")


    def detail_vehicle_km_in_day(self, code, eventname, result):
        vehicle_detail = module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 10, 3)
        # vehicle_detail = ''.join(re.findall(r'\d+', vehicle_detail))

        var_app.logging.info("--------------")
        var_app.logging.info("Giám sát - Thông tin chi tiết xe")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("Hiện trạng - Km trong ngày - " + vehicle_detail)
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, "Hiện trạng: {}".format(vehicle_detail))
        if vehicle_detail != "None":
            var_app.logging.info("True")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Pass")
        else:
            var_app.logging.info("False")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Fail")


    def detail_vehicle_cumulative_kilometers(self, code, eventname, result):
        check_detail = str(module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 22, 3))
        print("dettail: " + check_detail)

        var_app.logging.info("--------------")
        var_app.logging.info("Giám sát - Thông tin chi tiết xe")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("Hiện trạng - Km tích lũy - " + check_detail)
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, "Hiện trạng: {}".format(check_detail))
        if check_detail != "None":
            var_app.logging.info("True")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Pass")
        else:
            var_app.logging.info("False")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Fail")


    def detail_vehicle_stop(self, code, eventname, result):
        check_detail = str(module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 11, 3))
        print("dettail: " + check_detail)

        var_app.logging.info("--------------")
        var_app.logging.info("Giám sát - Thông tin chi tiết xe")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("Hiện trạng - Dừng đỗ - " + check_detail)
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, "Hiện trạng: {}".format(check_detail))
        if check_detail != "None":
            var_app.logging.info("True")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Pass")
        else:
            var_app.logging.info("False")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Fail")


    def detail_vehicle_stoping(self, code, eventname, result):
        check_detail = str(module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 59, 3))
        print("dettail: " + check_detail)

        var_app.logging.info("--------------")
        var_app.logging.info("Giám sát - Thông tin chi tiết xe")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("Hiện trạng - Đang đỗ - " + check_detail)
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, check_detail)
        if check_detail != "None":
            var_app.logging.info("True")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Pass")


    def detail_vehicle_stop_and_start_the_engine(self, code, eventname, result):
        check_detail = str(module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 60, 3))
        print("dettail: " + check_detail)

        var_app.logging.info("--------------")
        var_app.logging.info("Giám sát - Thông tin chi tiết xe")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, check_detail)
        if check_detail != "None":
            var_app.logging.info("True")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Pass")


    def detail_vehicle_air_condition(self, code, eventname, result):
        check_overview = str(module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 13, 2))
        print("overview: " + check_overview)
        check_detail = str(module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 13, 3))
        print("detail: " + check_detail)

        var_app.logging.info("--------------")
        var_app.logging.info("Giám sát - Thông tin chi tiết xe")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("Tổng quan - Điều hòa - " + check_overview)
        var_app.logging.info("Hiện trạng - Điều hòa - " + check_detail)
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, "Tổng quan: {}\nHiện trạng: {}".format(check_overview, check_detail))
        if check_overview == check_detail:
            var_app.logging.info("True")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Pass")
        else:
            var_app.logging.info("False")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Fail")


    def detail_vehicle_door_vehicle(self, code, eventname, result):
        check_overview = str(module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 18, 2))
        print("overview: " + check_overview)

        var_app.logging.info("--------------")
        var_app.logging.info("Giám sát - Thông tin chi tiết xe")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("Tổng quan - Cửa xe - " + check_overview)
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, "Tổng quan: {}".format(check_overview))
        if check_overview != "None":
            var_app.logging.info("True")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Pass")
        else:
            var_app.logging.info("False")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Fail")


    def detail_vehicle_fuel(self, code, eventname, result):
        check_detail = str(module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 16, 3))
        print("dettail: " + check_detail)

        var_app.logging.info("--------------")
        var_app.logging.info("Giám sát - Thông tin chi tiết xe")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("Hiện trạng - Bình 1 - " + check_detail)
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, "Hiện trạng: {}".format(check_detail))
        if check_detail != "None":
            var_app.logging.info("True")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Pass")
        # else:
        #     var_app.logging.info("False")
        #     module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Fail")


    def detail_vehicle_temperature(self, code, eventname, result):
        check_detail = str(module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 17, 3))
        print("dettail: " + check_detail)

        var_app.logging.info("--------------")
        var_app.logging.info("Giám sát - Thông tin chi tiết xe")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("Hiện trạng - Nhiệt độ - " + check_detail)
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, check_detail)
        if check_detail != "None":
            var_app.logging.info("True")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Pass")



    def detail_vehicle_merory_card(self, code, eventname, result):
        check_detail = str(module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 24, 3))
        print("dettail: " + check_detail)

        var_app.logging.info("--------------")
        var_app.logging.info("Giám sát - Thông tin chi tiết xe")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("Hiện trạng - Thẻ nhớ - " + check_detail)
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, "Hiện trạng: {}".format(check_detail))
        if check_detail != "None":
            var_app.logging.info("True")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Pass")
        else:
            var_app.logging.info("False")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Fail")


    def detail_vehicle_group(self, code, eventname, result):
        check_detail = module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 25, 3)
        print("dettail: " + check_detail)

        var_app.logging.info("--------------")
        var_app.logging.info("Giám sát - Thông tin chi tiết xe")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("Hiện trạng - Nhóm đội - " + check_detail)
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, "Hiện trạng: {}".format(check_detail))
        if check_detail != "None":
            var_app.logging.info("True")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Pass")
        else:
            var_app.logging.info("False")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Fail")


    def detail_vehicle_drive(self, code, eventname, result):
        vehicle_detail = str(module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 26, 3))
        var_app.logging.info("--------------")
        var_app.logging.info("Giám sát - Thông tin chi tiết xe")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("Hiện trạng - Lái xe - " + vehicle_detail)
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, "Hiện trạng: {}".format(vehicle_detail))
        if vehicle_detail != "None":
            var_app.logging.info("True")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Pass")
        else:
            var_app.logging.info("False")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Fail")


    def detail_vehicle_license(self, code, eventname, result):
        vehicle_detail = str(module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 27, 3))
        var_app.logging.info("--------------")
        var_app.logging.info("Giám sát - Thông tin chi tiết xe")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("Hiện trạng - Bằng lái - " + vehicle_detail)
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, "Hiện trạng: {}".format(vehicle_detail))
        if vehicle_detail != "None":
            var_app.logging.info("True")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Pass")
        else:
            var_app.logging.info("False")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Fail")


    def detail_vehicle_phone(self, code, eventname, result):
        check_detail = str(module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 28, 3))
        print("dettail: " + check_detail)

        var_app.logging.info("--------------")
        var_app.logging.info("Giám sát - Thông tin chi tiết xe")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("Hiện trạng - Điện thoại - " + check_detail)
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, "Hiện trạng: {}".format(check_detail))
        if check_detail != "None":
            var_app.logging.info("True")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Pass")



    def detail_vehicle_continuous_driving_time(self, code, eventname, result):
        vehicle_detail = str(module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 29, 3))

        var_app.logging.info("--------------")
        var_app.logging.info("Giám sát - Thông tin chi tiết xe")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("Hiện trạng - Thời gian lái xe liên tục - " + vehicle_detail)
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, "Hiện trạng: {}".format(vehicle_detail))
        if vehicle_detail != "None":
            var_app.logging.info("True")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Pass")
        else:
            var_app.logging.info("False")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Fail")


    def detail_vehicle_driving_time_during_the_day(self, code, eventname, result):
        vehicle_detail = str(module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 30, 3))

        var_app.logging.info("--------------")
        var_app.logging.info("Giám sát - Thông tin chi tiết xe")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("Hiện trạng - Thời gian lái xe trong ngày - " + vehicle_detail)
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, "Hiện trạng: {}".format(vehicle_detail))
        if vehicle_detail != "None":
            var_app.logging.info("True")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Pass")
        else:
            var_app.logging.info("False")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Fail")

    def detail_vehicle_driving_time_during_the_week(self, code, eventname, result):
        vehicle_detail = str(module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 74, 3))

        var_app.logging.info("--------------")
        var_app.logging.info("Giám sát - Thông tin chi tiết xe")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("Hiện trạng - Thời gian lái xe trong tuần - " + vehicle_detail)
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, "Hiện trạng: {}".format(vehicle_detail))
        if vehicle_detail != "None":
            var_app.logging.info("True")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Pass")
        else:
            var_app.logging.info("False")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Fail")



    def detail_vehicle_number_too_speed(self, code, eventname, result):
        vehicle_detail = str(module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 31, 3))

        var_app.logging.info("--------------")
        var_app.logging.info("Giám sát - Thông tin chi tiết xe")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("Hiện trạng - Sô lần quá tốc độ - " + vehicle_detail)
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, "Hiện trạng: {}".format(vehicle_detail))
        if vehicle_detail != "None":
            var_app.logging.info("True")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Pass")
        else:
            var_app.logging.info("False")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Fail")


    def detail_vehicle_management_department(self, code, eventname, result):
        check_detail = str(module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 32, 3))
        print("dettail: " + check_detail)

        var_app.logging.info("--------------")
        var_app.logging.info("Giám sát - Thông tin chi tiết xe")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("Hiện trạng - Sở quản lý - " + check_detail)
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, "Hiện trạng: {}".format(check_detail))
        if check_detail != "None":
            var_app.logging.info("True")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Pass")
        else:
            var_app.logging.info("False")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Fail")


    #Thiết bị
    def detail_vehicle_vin(self, code, eventname, result):
        check_detail = str(module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 36, 3))
        print("dettail: " + check_detail)

        var_app.logging.info("--------------")
        var_app.logging.info("Giám sát - Thông tin chi tiết xe")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("Thiết bị - Vin - " + check_detail)
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, "Thiết bị: {}".format(check_detail))
        if check_detail != "None":
            var_app.logging.info("True")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Pass")


    def detail_vehicle_the_frist_activity(self, code, eventname, result):
        check_detail = str(module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 61, 3))
        print("dettail: " + check_detail)

        var_app.logging.info("--------------")
        var_app.logging.info("Giám sát - Thông tin chi tiết xe")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("Thiết bị - Hoạt động lần đầu - " + check_detail)
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, "Thiết bị: {}".format(check_detail))
        if check_detail != "None":
            var_app.logging.info("True")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Pass")
        else:
            var_app.logging.info("False")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Fail")


    def detail_vehicle_news_recently(self, code, eventname, result):
        check_detail = str(module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 62, 3))
        print("dettail: " + check_detail)

        var_app.logging.info("--------------")
        var_app.logging.info("Giám sát - Thông tin chi tiết xe")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("Thiết bị - Bản tin gần nhất - " + check_detail)
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, "Thiết bị: {}".format(check_detail))
        if check_detail != "None":
            var_app.logging.info("True")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Pass")
        else:
            var_app.logging.info("False")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Fail")


    def detail_vehicle_status_gps(self, code, eventname, result):
        check_detail = str(module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 63, 3))
        print("dettail: " + check_detail)

        var_app.logging.info("--------------")
        var_app.logging.info("Giám sát - Thông tin chi tiết xe")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("Thiết bị - Trạng thái GPS - " + check_detail)
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, "Thiết bị: {}".format(check_detail))
        if check_detail != "None":
            var_app.logging.info("True")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Pass")
        else:
            var_app.logging.info("False")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Fail")


    def detail_vehicle_sim_number2(self, code, eventname, result):
        vehicle_sim1 = str(module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 19, 3))
        vehicle_sim2 = str(module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 64, 3))
        var_app.logging.info("--------------")
        var_app.logging.info("Giám sát - Thông tin chi tiết xe")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("Hiện trạng - Số SIM" + vehicle_sim1)
        var_app.logging.info("Thiết bị - Số SIM" + vehicle_sim2)
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, "Hiện trạng: {}\nThiết bị: {}".format(vehicle_sim1, vehicle_sim2))
        if vehicle_sim1 == vehicle_sim2:
            var_app.logging.info("True")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Pass")
        else:
            var_app.logging.info("False")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Fail")


    def detail_vehicle_subscription_type(self, code, eventname, result):
        check_detail = str(module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 65, 3))
        print("dettail: " + check_detail)

        var_app.logging.info("--------------")
        var_app.logging.info("Giám sát - Thông tin chi tiết xe")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("Thiết bị - Loại thuê bao - " + check_detail)
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, "Thiết bị: {}".format(check_detail))
        if check_detail != "None":
            var_app.logging.info("True")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Pass")
        else:
            var_app.logging.info("False")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Fail")


    def detail_vehicle_the_remaining_amount(self, code, eventname, result):
        check_detail = str(module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 69, 3))
        print("dettail: " + check_detail)

        var_app.logging.info("--------------")
        var_app.logging.info("Giám sát - Thông tin chi tiết xe")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("Thiết bị - Số tiền còn lại - " + check_detail)
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, "Thiết bị: {}".format(check_detail))
        if check_detail != "None":
            var_app.logging.info("True")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Pass")




    def detail_vehicle_status_sim(self, code, eventname, result):
        check_detail = str(module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 70, 3))
        print("dettail: " + check_detail)

        var_app.logging.info("--------------")
        var_app.logging.info("Giám sát - Thông tin chi tiết xe")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("Thiết bị - Trạng thái SIM - " + check_detail)
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, "Thiết bị: {}".format(check_detail))
        if check_detail != "None":
            var_app.logging.info("True")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Pass")


    def detail_vehicle_time_update2(self, code, eventname, result):
        check_detail_the_remaining_amount = str(module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 69, 3))
        check_status_sim = str(module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 70, 3))
        check_detail_timeupdate = str(module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 71, 3))
        print("dettail: " + check_detail_timeupdate)

        var_app.logging.info("--------------")
        var_app.logging.info("Giám sát - Thông tin chi tiết xe")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("Thiết bị - Cập nhật lúc - " + check_detail_timeupdate)
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, check_detail_timeupdate)
        if (check_detail_the_remaining_amount == check_status_sim == check_detail_timeupdate) or (check_detail_timeupdate!= "None"):
            var_app.logging.info("True")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Pass")



    def detail_vehicle_battert_level(self, code, eventname, result):
        check_detail = str(module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 66, 3))
        print("dettail: " + check_detail)

        var_app.logging.info("--------------")
        var_app.logging.info("Giám sát - Thông tin chi tiết xe")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("Thiết bị - Mức ắc quy - " + check_detail)
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, "Thiết bị: {}".format(check_detail))
        if check_detail != "None":
            var_app.logging.info("True")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Pass")
        else:
            var_app.logging.info("False")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Fail")


    def detail_vehicle_power_status(self, code, eventname, result):
        check_detail = str(module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 67, 3))
        print("dettail: " + check_detail)

        var_app.logging.info("--------------")
        var_app.logging.info("Giám sát - Thông tin chi tiết xe")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("Thiết bị - Trạng thái nguồn - " + check_detail)
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, "Thiết bị: {}".format(check_detail))
        if check_detail != "None":
            var_app.logging.info("True")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Pass")







    #Camera
    def detail_vehicle_package_name(self, code, eventname, result):
        check_detail = str(module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 37, 3))
        print("dettail: " + check_detail)

        var_app.logging.info("--------------")
        var_app.logging.info("Giám sát - Thông tin chi tiết xe")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("Camera - Tên gói cước - " + check_detail)
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, "Camera: {}".format(check_detail))
        if check_detail != "None":
            var_app.logging.info("True")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Pass")
        else:
            var_app.logging.info("False")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Fail")


    def detail_vehicle_home_network(self, code, eventname, result):
        check_detail = str(module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 38, 3))
        print("dettail: " + check_detail)

        var_app.logging.info("--------------")
        var_app.logging.info("Giám sát - Thông tin chi tiết xe")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("Camera - Nhà mạng - " + check_detail)
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, "Camera: {}".format(check_detail))
        if check_detail != "None":
            var_app.logging.info("True")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Pass")
        else:
            var_app.logging.info("False")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Fail")


    def detail_vehicle_package_capacity(self, code, eventname, result):
        check_detail = str(module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 39, 3))
        print("dettail: " + check_detail)

        var_app.logging.info("--------------")
        var_app.logging.info("Giám sát - Thông tin chi tiết xe")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("Camera - Dung lượng gói cước - " + check_detail)
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, "Camera: {}".format(check_detail))
        if check_detail != "None":
            var_app.logging.info("True")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Pass")
        else:
            var_app.logging.info("False")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Fail")


    def detail_vehicle_number_of_days_of_storage(self, code, eventname, result):
        check_detail = str(module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 40, 3))
        print("dettail: " + check_detail)

        var_app.logging.info("--------------")
        var_app.logging.info("Giám sát - Thông tin chi tiết xe")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("Camera - Số ngày lưu trữ - " + check_detail)
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, "Camera: {}".format(check_detail))
        if check_detail != "None":
            var_app.logging.info("True")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Pass")
        else:
            var_app.logging.info("False")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Fail")


    def detail_vehicle_number_of_chanels_of_storage(self, code, eventname, result):
        check_detail = str(module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 41, 3))
        print("dettail: " + check_detail)

        var_app.logging.info("--------------")
        var_app.logging.info("Giám sát - Thông tin chi tiết xe")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("Camera - Số kênh lưu trữ - " + check_detail)
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, "Camera: {}".format(check_detail))
        if check_detail != "None":
            var_app.logging.info("True")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Pass")
        else:
            var_app.logging.info("False")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Fail")


    def detail_vehicle_location(self, code, eventname, result):
        check_detail = str(module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 42, 3))
        print("dettail: " + check_detail)

        var_app.logging.info("--------------")
        var_app.logging.info("Giám sát - Thông tin chi tiết xe")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("Camera - Định vị - " + check_detail)
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, "Camera: {}".format(check_detail))
        if check_detail != "None":
            var_app.logging.info("True")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Pass")
        else:
            var_app.logging.info("False")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Fail")


    def detail_vehicle_image(self, code, eventname, result):
        check_detail = str(module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 43, 3))
        print("dettail: " + check_detail)

        var_app.logging.info("--------------")
        var_app.logging.info("Giám sát - Thông tin chi tiết xe")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("Camera - Ảnh - " + check_detail)
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, "Camera: {}".format(check_detail))
        if check_detail != "None":
            var_app.logging.info("True")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Pass")
        else:
            var_app.logging.info("False")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Fail")


    def detail_vehicle_video(self, code, eventname, result):
        check_detail = str(module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 44, 3))
        print("dettail: " + check_detail)

        var_app.logging.info("--------------")
        var_app.logging.info("Giám sát - Thông tin chi tiết xe")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("Camera - Video - " + check_detail)
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, "Camera: {}".format(check_detail))
        if check_detail != "None":
            var_app.logging.info("True")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Pass")
        else:
            var_app.logging.info("False")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Fail")


    def detail_vehicle_channel_camera(self, code, eventname, result):
        check_detail = str(module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 45, 3))
        print("dettail: " + check_detail)

        var_app.logging.info("--------------")
        var_app.logging.info("Giám sát - Thông tin chi tiết xe")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("Camera - Kênh lắp camera - " + check_detail)
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, "Camera: {}".format(check_detail))
        if check_detail != "None":
            var_app.logging.info("True")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Pass")
        else:
            var_app.logging.info("False")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Fail")


    def detail_vehicle_channel_active(self, code, eventname, result):
        check_detail = str(module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 46, 3))
        print("dettail: " + check_detail)

        var_app.logging.info("--------------")
        var_app.logging.info("Giám sát - Thông tin chi tiết xe")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("Camera - Kênh hoạt động - " + check_detail)
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, "Camera: {}".format(check_detail))
        if check_detail != "None":
            var_app.logging.info("True")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Pass")
        else:
            var_app.logging.info("False")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Fail")


    def detail_vehicle_network_connection(self, code, eventname, result):
        check_detail = str(module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 68, 3))
        print("dettail: " + check_detail)

        var_app.logging.info("--------------")
        var_app.logging.info("Giám sát - Thông tin chi tiết xe")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("Camera - Mạng kết nối - " + check_detail)
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, "Camera: {}".format(check_detail))
        if check_detail != "None":
            var_app.logging.info("True")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Pass")
        else:
            var_app.logging.info("False")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Fail")


    def detail_vehicle_icon_update(self, code, eventname, result):
        var_app.driver.implicitly_wait(5)
        try:
            var_app.driver.find_element(By.XPATH, var_app.detail_vehicle_icon_update).click()
        except:
            login_app.login.login_v3(self, var_app.data['login']['conhom_quantri_tk'], var_app.data['login']['conhom_quantri_mk'])
            time.sleep(1)
            var_app.driver.implicitly_wait(3)
            var_app.driver.find_element(By.XPATH, var_app.detail_vehicle_choose1).click()
            time.sleep(2.5)
            var_app.driver.find_element(By.XPATH, var_app.detail_vehicle).click()
            time.sleep(2.5)
            var_app.driver.find_element(By.XPATH, var_app.detail_vehicle_icon_update).click()
        var_app.logging.info("--------------")
        var_app.logging.info("Giám sát - Thông tin chi tiết xe")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("Icon cập nhật")
        var_app.logging.info("True")
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Pass")






    def icon_support_customer(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        detail.detail_vehicle_monitor_back(self)
        try:
            var_app.driver.find_element(By.XPATH, var_app.detail_vehicle_choose1).click()
        except:
            login_app.login.login_v3(self, var_app.data['login']['conhom_quantri_tk'], var_app.data['login']['conhom_quantri_mk'])
            var_app.driver.find_element(By.XPATH, var_app.detail_vehicle_choose1).click()
        time.sleep(2.5)

        var_app.driver.find_element(By.XPATH, var_app.minitor_icon_support_customer).click()
        time.sleep(2.5)
        module_other_app.write_result_text_try_if(code, eventname, result, "Giám sát - Thông tin chi tiết xe",
                                              var_app.check_support_customer, "HỖ TRỢ KHÁCH HÀNG", "_GiamSat_ChiTietXe_HoTroKhachHang.png")

        try:
            var_app.driver.find_element(By.XPATH, var_app.support_customer_iconx1).click()
            time.sleep(2)
        except:
            pass




    def setting_favorite(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        detail.detail_vehicle_monitor_back(self)
        try:
            var_app.driver.find_element(By.XPATH, var_app.detail_vehicle_choose1).click()
        except:
            login_app.login.login_v3(self, var_app.data['login']['conhom_quantri_tk'], var_app.data['login']['conhom_quantri_mk'])
            var_app.driver.find_element(By.XPATH, var_app.detail_vehicle_choose1).click()
        time.sleep(2.5)

        var_app.driver.find_element(By.XPATH, var_app.setting).click()
        time.sleep(2.5)
        module_other_app.write_result_text_try_if(code, eventname, result, "Giám sát - Thông tin chi tiết xe - Tùy chỉnh",
                                              var_app.check_detail_custom, "THIẾT LẬP MỤC ƯA THÍCH", "_GiamSat_ChiTietXe_TuyChinh.png")


    def setting_favorite_choose(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        try:
            var_app.driver.find_element(By.XPATH, var_app.detail_custom_search_input)
        except:
            detail.setting_favorite(self, "", "", "")


        var_app.driver.find_element(By.XPATH, var_app.detail_custom_search_input).clear()
        time.sleep(0.5)
        var_app.driver.find_element(By.XPATH, var_app.detail_custom_search_input).send_keys(var_app.data['minitor']['favorite_search'])
        time.sleep(2)
        try:
            var_app.driver.find_element(By.XPATH, var_app.checkbox_favorite2_full)
        except:
            var_app.driver.find_element(By.XPATH, var_app.checkbox_favorite1_full).click()
        time.sleep(1)
        var_app.driver.find_element(By.XPATH, var_app.setup_favorite_save).click()
        time.sleep(1.5)
        module_other_app.write_result_text_try_if(code, eventname, result, "Giám sát - Thông tin chi tiết xe - Tùy chỉnh",
                                                  var_app.check_detail_choose_min_favorites, "Lưu mục ưa thích thành công", "_GiamSat_TuyChon_Luu.png")
        time.sleep(3)


    def setting_favorite_search(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        try:
            var_app.driver.find_element(By.XPATH, var_app.detail_vehicle_choose1).click()
            time.sleep(2.5)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.find_element(By.XPATH, var_app.setting)
        except:
            detail.setting_favorite_choose(self, "", "", "")
            var_app.driver.find_element(By.XPATH, var_app.detail_vehicle_choose1).click()
            time.sleep(2.5)

        try:
            var_app.driver.find_element(By.XPATH, "//*[@text='"+var_app.data['minitor']['favorite_search']+"']")
        except:
            module_other_app.swipe_scaled(var_app.driver, 740, 1360, 150, 160, 1360)
            time.sleep(1)

        module_other_app.write_result_text_try_if(code, eventname, result, "Giám sát - Thông tin chi tiết xe - Tùy chỉnh",
                                                  "//*[@text='"+var_app.data['minitor']['favorite_search']+"']",
                                                  var_app.data['minitor']['favorite_search'], "_GiamSat_TuyChon_Search.png")

        var_app.driver.find_element(By.XPATH, var_app.setting).click()
        time.sleep(2.5)
        var_app.driver.find_element(By.XPATH, var_app.detail_custom_search_input).clear()
        time.sleep(0.5)
        var_app.driver.find_element(By.XPATH, var_app.detail_custom_search_input).send_keys(var_app.data['minitor']['favorite_search'])
        time.sleep(2)

        try:
            var_app.driver.find_element(By.XPATH, var_app.checkbox_favorite2).click()
            time.sleep(1)
        except:
            module_other_app.tap_scaled(var_app.driver, [(863, 388)])
        time.sleep(1)
        var_app.driver.find_element(By.XPATH, var_app.detail_custom_search_input).clear()
        time.sleep(0.5)
        var_app.driver.find_element(By.XPATH, var_app.setup_favorite_save).click()
        time.sleep(1.5)








    def detail_vehicle_monitor_back(self):
        var_app.driver.implicitly_wait(0.2)
        try:
            var_app.driver.find_element(By.XPATH, var_app.detail_vehicle_monitor_back1).click()
            time.sleep(1.3)
        except:
            pass
        try:
            var_app.driver.find_element(By.XPATH, var_app.detail_vehicle_monitor_back2).click()
            time.sleep(1.3)
        except:
            pass

        try:
            var_app.driver.find_element(By.XPATH, var_app.detail_vehicle_monitor_back3).click()
            time.sleep(1.3)
        except:
            pass
        try:
            var_app.driver.find_element(By.XPATH, var_app.detail_vehicle_monitor_back4).click()
            time.sleep(1.3)
        except:
            pass
        try:
            var_app.driver.find_element(By.XPATH, var_app.detail_vehicle_monitor_back5).click()
            time.sleep(1.3)
        except:
            pass
        try:
            var_app.driver.find_element(By.XPATH, var_app.detail_vehicle_monitor_back6).click()
            time.sleep(1.3)
        except:
            pass
        try:
            var_app.driver.find_element(By.XPATH, var_app.detail_vehicle_monitor_back7).click()
            time.sleep(1.3)
        except:
            pass
        try:
            var_app.driver.find_element(By.XPATH, var_app.support_customer_iconx1).click()
            time.sleep(1.3)
        except:
            pass



    def detail_vehicle_monitor_video(self, code, eventname, result):
        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.find_element(By.XPATH, var_app.detail_vehicle_monitor_video).click()
        except:
            login_app.login.login_v3(self, var_app.data['login']['conhom_quantri_tk'], var_app.data['login']['conhom_quantri_mk'])
            time.sleep(1)
            var_app.driver.find_element(By.XPATH, var_app.detail_vehicle_choose1).click()
            time.sleep(2.5)
            var_app.driver.find_element(By.XPATH, var_app.detail_vehicle).click()
            time.sleep(2.5)
            var_app.driver.find_element(By.XPATH, var_app.detail_vehicle_monitor_video).click()

        time.sleep(3.5)
        module_other_app.write_result_text_try_if_not_fail(code, eventname, result, "Giám sát - Thông tin chi tiết xe - Link liên kết",
                                              var_app.check_detail_vehicle_monitor_video, "GIÁM SÁT NHIỀU CAMERA", "_GiamSat_ChiTietXe_GiamSatCamera.png")

        try:
            var_app.driver.find_element(By.XPATH, var_app.detail_vehicle_monitor_video_iconx).click()
            time.sleep(1.5)
        except:
            pass


    def detail_vehicle_monitor_image(self, code, eventname, result):
        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.find_element(By.XPATH, var_app.detail_vehicle_monitor_image).click()
        except:
            login_app.login.login_v3(self, var_app.data['login']['conhom_quantri_tk'], var_app.data['login']['conhom_quantri_mk'])
            time.sleep(1)
            var_app.driver.find_element(By.XPATH, var_app.detail_vehicle_choose1).click()
            time.sleep(2.5)
            var_app.driver.find_element(By.XPATH, var_app.detail_vehicle).click()
            time.sleep(2.5)
            var_app.driver.find_element(By.XPATH, var_app.detail_vehicle_monitor_image).click()
        time.sleep(3.5)
        module_other_app.write_result_text_try_if_not_fail(code, eventname, result, "Giám sát - Thông tin chi tiết xe - Link liên kết",
                                              var_app.check_image_monitoring, "GIÁM SÁT HÌNH ẢNH", "_GiamSat_ChiTietXe_GiamSatHinhAnh.png")

        try:
            var_app.driver.find_element(By.XPATH, var_app.detail_vehicle_monitor_image_iconx).click()
            time.sleep(1.5)
        except:
            pass


    def detail_vehicle_fuel_chart(self, code, eventname, result):
        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.find_element(By.XPATH, var_app.detail_vehicle_fuel_chart).click()
        except:
            login_app.login.login_v3(self, var_app.data['login']['conhom_quantri_tk'], var_app.data['login']['conhom_quantri_mk'])
            time.sleep(1)
            var_app.driver.find_element(By.XPATH, var_app.detail_vehicle_choose1).click()
            time.sleep(2.5)
            var_app.driver.find_element(By.XPATH, var_app.detail_vehicle).click()
            time.sleep(2.5)
            var_app.driver.find_element(By.XPATH, var_app.detail_vehicle_fuel_chart).click()
        time.sleep(7)
        module_other_app.write_result_text_try_if_not_fail(code, eventname, result, "Giám sát - Thông tin chi tiết xe - Link liên kết",
                                              var_app.check_detail_vehicle_fuel_chart, "BIỂU ĐỒ NHIÊN LIỆU", "_GiamSat_ChiTietXe_BieuDoNhiienLieu.png")

        detail.detail_vehicle_monitor_back(self)


    def detail_vehicle_imei(self, code, eventname, result):
        check_detail = str(module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 21, 3))
        print("dettail: " + check_detail)

        var_app.logging.info("--------------")
        var_app.logging.info("Giám sát - Thông tin chi tiết xe")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("Tổng quan - Imei - " + check_detail)
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 11, check_detail)
        if check_detail != "None":
            var_app.logging.info("True")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Pass")
        else:
            var_app.logging.info("False")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Fail")


    def detail_vehicle_open_door_number(self, code, eventname, result):
        check_detail = str(module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 23, 3))
        print("dettail: " + check_detail)

        var_app.logging.info("--------------")
        var_app.logging.info("Giám sát - Thông tin chi tiết xe")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("Tổng quan - Số lần mở cửa - " + check_detail)
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 11, check_detail)
        if check_detail != "None":
            var_app.logging.info("True")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Pass")
        else:
            var_app.logging.info("False")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Fail")















class affiliate_link:

    def route(self, code, eventname, result):
        var_app.driver.implicitly_wait(2)
        login_app.login.login_v3(self, var_app.data['login']['conhom_quantri_tk'], var_app.data['login']['conhom_quantri_mk'])
        var_app.driver.find_element(By.XPATH, var_app.detail_vehicle_choose1).click()
        time.sleep(2.5)
        try:
            var_app.driver.find_element(By.XPATH, var_app.minitor_route).click()
        except:
            minitor_back()
            var_app.driver.find_element(By.XPATH, var_app.detail_vehicle_choose1).click()
            time.sleep(2)
            var_app.driver.find_element(By.XPATH, var_app.minitor_route).click()

        time.sleep(4)
        module_other_app.tap_scaled(var_app.driver, [(50, 1440)])
        time.sleep(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.detail_vehicle_iconx).click()
        except:
            pass
        module_other_app.write_result_text_try_if(code, eventname, result, "Giám sát - đi tới link liên kết click vào xe",
                                              var_app.check_route, "1H", "_GiamSat_LoTrinh.png")

        var_app.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Giám sát").click()
        time.sleep(2)


    def affiliate_link_overview(self, code, eventname, result, link, link_iconx, path_check, desire, path_image):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass
        var_app.driver.implicitly_wait(1.5)
        try:
            var_app.driver.find_element(By.XPATH, var_app.detail_vehicle_choose1).click()
        except:
            login_app.login.login_v3(self, var_app.data['login']['conhom_quantri_tk'], var_app.data['login']['conhom_quantri_mk'])
            var_app.driver.find_element(By.XPATH, var_app.detail_vehicle_choose1).click()
        time.sleep(2.5)
        var_app.driver.find_element(By.XPATH, link).click()
        time.sleep(3)

        module_other_app.write_result_text_try_if(code, eventname, result, "Giám sát - Chi tiết xe - link liên kết click vào xe",
                                              path_check, desire, path_image)

        try:
            var_app.driver.find_element(By.XPATH, link_iconx).click()
            time.sleep(2.3)
        except:
            pass





    @retry(tries=2, delay=2, backoff=1, jitter=5, )
    def affiliate_link_detail(self, code, eventname, result, startX, startY, endX, endY, duration,
                              link, link_iconx, path_check, desire, path_image, type=None):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(1.5)
        try:
            vehicle = var_app.driver.find_element(By.XPATH, var_app.detail_vehicle_choose1).get_attribute("content-desc")
            var_app.driver.find_element(By.XPATH, var_app.search_vehicle).click()
            time.sleep(2)
            var_app.driver.find_element(By.XPATH, var_app.search_vehicle_input).send_keys(vehicle)
            time.sleep(1.5)
            module_other_app.tap_scaled(var_app.driver, [(193, 352)])
            time.sleep(2.5)
            print("m1")
            var_app.driver.find_element(By.XPATH, var_app.detail_vehicle_choose1).click()
        except:
            print("m2")
            login_app.login.login_v3(self, var_app.data['login']['conhom_quantri_tk'], var_app.data['login']['conhom_quantri_mk'])
            print("m3")
            # overview.vehicle_status(self, "", eventname, result, "Tất cả", "")
            vehicle = var_app.driver.find_element(By.XPATH, var_app.detail_vehicle_choose1).get_attribute("content-desc")
            var_app.driver.find_element(By.XPATH, var_app.search_vehicle).click()
            time.sleep(2)
            var_app.driver.find_element(By.XPATH, var_app.search_vehicle_input).send_keys(vehicle)
            time.sleep(1.5)
            module_other_app.tap_scaled(var_app.driver, [(193, 352)])
            time.sleep(2.5)
            var_app.driver.find_element(By.XPATH, var_app.detail_vehicle_choose1).click()
            print("m4")

        time.sleep(2)
        try:
            print("m5")
            try:
                var_app.driver.find_element(By.XPATH, var_app.see_more).click()
            except:
                var_app.driver.find_element(By.XPATH, var_app.detail_vehicle_choose1).click()
                time.sleep(2)
                var_app.driver.find_element(By.XPATH, var_app.see_more).click()
            print("m6")
            time.sleep(2.5)
        except:
            print("m7")
            login_app.login.login_v3(self, var_app.data['login']['conhom_quantri_tk'], var_app.data['login']['conhom_quantri_mk'])
            print("m8")
            # overview.vehicle_status(self, "", eventname, result, "Tất cả", "")
            print("m9")
            vehicle = var_app.driver.find_element(By.XPATH, var_app.detail_vehicle_choose1).get_attribute("content-desc")
            var_app.driver.find_element(By.XPATH, var_app.search_vehicle).click()
            time.sleep(2)
            var_app.driver.find_element(By.XPATH, var_app.search_vehicle_input).send_keys(vehicle)
            time.sleep(1.5)
            module_other_app.tap_scaled(var_app.driver, [(193, 352)])
            time.sleep(2.5)
            var_app.driver.find_element(By.XPATH, var_app.detail_vehicle_choose1).click()
            time.sleep(2)
            print("m10")
            var_app.driver.find_element(By.XPATH, var_app.see_more).click()
            time.sleep(2.5)
            print("m11")

        var_app.driver.implicitly_wait(1)
        if type == 1:
            try:
                scroll_and_click_precent(startX, startY, endX, endY, duration, link)
            except:
                var_app.driver.find_element(By.XPATH, var_app.see_more).click()
                var_app.driver.find_element(By.XPATH, link_iconx).click()
                time.sleep(2.3)



        if code == "Minitor170":
            module_other_app.write_result_displayed_try(code, eventname, result, "Giám sát - đi tới link liên kết click vào xe",
                                                    path_check, path_image)
        else:
            module_other_app.write_result_text_try_if(code, eventname, result, "Giám sát - đi tới link liên kết click vào xe",
                                                  path_check, desire, path_image)


        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, link_iconx).click()
            time.sleep(2)
        except:
            try:
                module_other_app.back(self='')
            except:
                module_other_app.close_app()
            time.sleep(1)



