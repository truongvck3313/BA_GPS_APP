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
        pathtenphuongtien = "/hierarchy/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[4]/android.view.ViewGroup[" + n + "]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView"
        print(n)
        try:
            tenphuongtien = var_app.driver.find_element(By.XPATH, pathtenphuongtien).text
            print(tenphuongtien)
            if tenphuongtien == field_name:
                detail_name = var_app.driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[4]/android.view.ViewGroup[" + n + "]/android.view.ViewGroup/android.widget.TextView").text
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
        pathtenphuongtien = "/hierarchy/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[" + n + "]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView"
        print(n)
        try:
            tenphuongtien = var_app.driver.find_element(By.XPATH, pathtenphuongtien).text
            print(tenphuongtien)
            if tenphuongtien == field_name:
                detail_name = var_app.driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[" + n + "]/android.view.ViewGroup/android.widget.TextView").text
                module_other_app.writeData1(var_app.path_luutamthoi, "Sheet1", row, 3, detail_name)
                print(tenphuongtien + ": "+ detail_name)
                break
        except:
            pass
        n = int(n)







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



def scroll_and_click(startX, startY, endX, endY, duration, path_check):
    var_app.driver.implicitly_wait(1)
    n = 0
    while (n < 10):
        n += 1
        try:
            var_app.driver.find_element(By.XPATH, path_check).is_displayed()
            break
        except:
            var_app.driver.swipe(startX, startY, endX, endY, duration)
        time.sleep(0.5)
    var_app.driver.find_element(By.XPATH, path_check).click()
    time.sleep(2.5)



class overview:

    def search_vehicle(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.search_vehicle).click()
        except:
            login_app.login.login_v3(self, "43E02740", "12341234")
            var_app.driver.find_element(By.XPATH, var_app.search_vehicle).click()
            print("vao day roi")
        var_app.driver.implicitly_wait(5)
        time.sleep(1)
        var_app.driver.find_element(By.XPATH, var_app.search_vehicle_input).send_keys(var_app.data['minitor']['search'])
        time.sleep(1.5)
        var_app.driver.tap([(193, 352)])
        time.sleep(3)
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

        var_app.driver.implicitly_wait(5)
        try:
            var_app.driver.find_element(By.XPATH, var_app.select_group_icon).click()
        except:
            login_app.login.login_v3(self, "43E02740", "12341234")
            var_app.driver.find_element(By.XPATH, var_app.select_group_icon).click()
        time.sleep(1.5)
        var_app.driver.find_element(By.XPATH, var_app.select_group_input).send_keys(var_app.data['minitor']['search_group'])
        time.sleep(2)
        var_app.driver.swipe(400, 400, 400, 1000, 500)
        var_app.driver.tap([(40, 490)])
        time.sleep(0.5)
        var_app.driver.find_element(By.XPATH, var_app.minitor_name_group_choose).click()
        time.sleep(3)
        var_app.driver.implicitly_wait(1)
        var_app.logging.info("--------------")
        var_app.logging.info("Giám sát - chọn nhóm")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 11, var_app.data['minitor']['search_group'])
        try:
            check_displayed = var_app.driver.find_element(By.XPATH, "(//android.view.View[@content-desc='"+var_app.data['minitor']['check_search_group']+"'])[1]").is_displayed()
            var_app.logging.info("True")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Pass")
        except NoSuchElementException:
            var_app.logging.info("False")
            var_app.driver.save_screenshot(var_app.imagepath + code + "_GiamSat_Chon1Nhom.png")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Fail")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 9, code + "_GiamSat_Chon1Nhom.png")

        try:
            check_displayed = var_app.driver.find_element(By.XPATH, "(//android.view.View[@content-desc='"+var_app.data['minitor']['check_search_group1']+"'])[1]").is_displayed()
            var_app.logging.info("False")
            var_app.driver.save_screenshot(var_app.imagepath + code + "_GiamSat_Chon1Nhom.png")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Fail")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 9, code + "_GiamSat_Chon1Nhom.png")
        except NoSuchElementException:
            var_app.logging.info("True")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Pass")

        var_app.driver.find_element(By.XPATH, var_app.select_group_icon).click()
        time.sleep(1.5)
        var_app.driver.swipe(400, 400, 400, 1000, 500)
        var_app.driver.tap([(40, 490)])
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

        var_app.driver.implicitly_wait(5)
        try:
            var_app.driver.find_element(By.XPATH, var_app.select_group_icon).click()
        except:
            login_app.login.login_v3(self, "43E02740", "12341234")
            var_app.driver.find_element(By.XPATH, var_app.select_group_icon).click()
        time.sleep(1.5)
        var_app.driver.find_element(By.XPATH, var_app.select_group_icon_all).click()
        time.sleep(0.5)
        var_app.driver.find_element(By.XPATH, var_app.minitor_name_group_choose).click()
        time.sleep(3)
        var_app.logging.info("--------------")
        var_app.logging.info("Giám sát - chọn nhóm")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("True")
        try:
            check_displayed = var_app.driver.find_element(By.XPATH, "(//android.view.View[@content-desc='"+var_app.data['minitor']['check_search_group1']+"'])[1]").is_displayed()
            var_app.logging.info("True")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Pass")
        except NoSuchElementException:
            var_app.logging.info("False")
            var_app.driver.save_screenshot(var_app.imagepath + code + "_GiamSat_ChonTatCaNhom.png")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Fail")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 9, code + "_GiamSat_ChonTatCaNhom.png")

        var_app.driver.find_element(By.XPATH, var_app.select_group_icon).click()
        time.sleep(1.5)
        var_app.driver.find_element(By.XPATH, var_app.select_group_icon_all).click()
        time.sleep(0.5)
        var_app.driver.find_element(By.XPATH, var_app.minitor_name_group_choose).click()
        time.sleep(3)

    @retry(tries=3, delay=2, backoff=1, jitter=5, )
    def vehicle_status(self, code, eventname, result, status_name, x, y, path_image):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
        except:
            pass

        if code == "Minitor04":
            login_app.login.check_logout(self)
            login_app.login.login_v3(self, "cttoancau", "12341234")
        if code == "Minitor14":
            login_app.login.check_logout(self)
            login_app.login.login_v3(self, "tranquocdungdn", "12341234")
        if code == "Minitor24":
            login_app.login.check_logout(self)
            login_app.login.login_v3(self, "ctyanhngocminh", "12341234")
        if code == "Minitor34":
            login_app.login.check_logout(self)
            login_app.login.login_v3(self, "truonganphat", "12341234")
        if code == "Minitor44":
            login_app.login.check_logout(self)
            login_app.login.login_v3(self, "43E02740", "12341234")
        if code == "Minitor54":
            login_app.login.check_logout(self)
            login_app.login.login_v3(self, "43E02743", "12341234")
        if code == "Minitor64":
            login_app.login.check_logout(self)
            login_app.login.login_v3(self, "ungroup", "12341234")
        if code == "Minitor74":
            login_app.login.check_logout(self)
            login_app.login.login_v3(self, "ungroup_1", "12341234")


        var_app.driver.implicitly_wait(5)
        try:
            var_app.driver.find_element(By.XPATH, var_app.vehicle_status_icon).click()
        except:
            login_app.login.login_v3(self, "43E02740", "12341234")
        time.sleep(1.5)

        var_app.driver.tap([(x, y)])
        time.sleep(2)
        if status_name == "Tất cả":
            module_other_app.write_result_displayed_try(code, eventname, result, "Giám sát - Trạng thái xe",
                                                    var_app.path_vehicle_status, path_image)
        else:
            var_app.logging.info("--------------")
            var_app.logging.info("Giám sát - Trạng thái xe")
            var_app.logging.info("Mã - " + code)
            var_app.logging.info("Tên sự kiện - " + eventname)
            var_app.logging.info("Kết quả - " + result)
            var_app.logging.info("True")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Pass")




    def goto_google(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
        except:
            pass

        var_app.driver.implicitly_wait(5)
        try:
            var_app.driver.find_element(By.XPATH, var_app.goto_google).click()
        except:
            login_app.login.check_logout(self)
            login_app.login.login_v3(self, "43E02740", "12341234")
            var_app.driver.find_element(By.XPATH, var_app.goto_google).click()
        time.sleep(3)
        module_other_app.write_result_displayed_try(code, eventname, result, "Giám sát - Icon đi tới Google",
                                                    var_app.check_goto_google, "_GiamSat_Goto_Google.png")

        var_app.driver.press_keycode(4)
        time.sleep(2)
        var_app.driver.press_keycode(4)
        time.sleep(2)



    def turn_on_location(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
        except:
            pass

        var_app.driver.implicitly_wait(5)
        try:
            var_app.driver.find_element(By.XPATH, var_app.turn_on_location).click()
        except:
            login_app.login.check_logout(self)
            login_app.login.login_v3(self, "43E02740", "12341234")
            var_app.driver.find_element(By.XPATH, var_app.turn_on_location).click()
        time.sleep(2)
        var_app.logging.info("--------------")
        var_app.logging.info("Giám sát - Icon bật vị trí")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("True")
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Pass")



    def icon_change_map(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
        except:
            pass

        var_app.driver.implicitly_wait(5)
        try:
            var_app.driver.find_element(By.XPATH, var_app.icon_change_map).click()
        except:
            login_app.login.check_logout(self)
            login_app.login.login_v3(self, "43E02740", "12341234")
            var_app.driver.find_element(By.XPATH, var_app.icon_change_map).click()
        time.sleep(2)
        var_app.logging.info("--------------")
        var_app.logging.info("Giám sát - Icon thay đổi map")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("True")
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Pass")

        var_app.driver.find_element(By.XPATH, var_app.icon_change_map).click()
        time.sleep(2)



class detail:

    def detail_vehicle(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        module_other_app.clearData_luutamthoi(var_app.path_luutamthoi, "Sheet1", "", "", "")
        login_app.login.check_logout1(self, "43E02740", "43E02740", "12341234")

        try:
            var_app.driver.find_element(By.XPATH, var_app.minitor).click()
        except:
            login_app.login.login_v3(self, "43E02740", "12341234")
        time.sleep(1)

        var_app.driver.implicitly_wait(3)
        overview.vehicle_status(self, "Minitor05", eventname, result,
                                            "Di chuyển", 650, 450, "")

        var_app.driver.find_element(By.XPATH, var_app.detail_vehicle_choose1).click()
        time.sleep(2.5)
        get_detail(var_app.overview_vehicleplate, 6, 2)
        get_detail(var_app.overview_time, 7, 2)
        get_detail(var_app.overview_adress, 14, 2)
        get_detail(var_app.overview_speed, 8, 2)
        get_detail(var_app.overview_engine, 12, 2)
        get_detail(var_app.overview_ari_condition, 13, 2)
        get_detail(var_app.overview_ari_vehicle_door, 18, 2)
        bienso = module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 6, 2)
        call_api950(bienso)

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
        var_app.driver.swipe(400, 1350, 450, 400, 500)
        time.sleep(1)
        status_general_information1("Nhiên liệu", 16)
        status_general_information1("Nhiệt độ", 17)
        status_general_information1("Thẻ nhớ", 24)
        status_general_information1("Nhóm đội", 25)
        status_general_information1("Số lần mở cửa", 23)



        get_detail(var_app.detail_driver, 26, 3)
        get_detail(var_app.detail_driver_liscense, 27, 3)
        get_detail(var_app.detail_phone_number, 28, 3)
        get_detail(var_app.detail_continuous_driving_time, 29, 3)
        get_detail(var_app.detail_driving_time_during_the_day, 30, 3)
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
        var_app.driver.find_element(By.XPATH, var_app.detail_vehicle_camera).click()
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
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Pass")


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
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 11, vehicle_sim1)
        if vehicle_sim1 == vehicle_sim2:
            var_app.logging.info("True")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Pass")
        else:
            var_app.logging.info("False")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Fail")


    def detail_vehicle_day_register(self, code, eventname, result):
        check_detail = str(module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 20, 3))
        print("dettail: " + check_detail)

        var_app.logging.info("--------------")
        var_app.logging.info("Giám sát - Thông tin chi tiết xe")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("Hiện trạng - Ngày đăng ký - " + check_detail)
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 11, check_detail)
        if check_detail != "None":
            var_app.logging.info("True")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Pass")
        else:
            var_app.logging.info("False")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Fail")


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
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 11, vehicle_overview)
        if vehicle_overview[0:8] == vehicle_detail[0:8]:
            var_app.logging.info("True")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Pass")
        else:
            var_app.logging.info("False")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Fail")


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
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 11, check_overview)
        if check_overview == check_detail:
            var_app.logging.info("True")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Pass")
        else:
            var_app.logging.info("False")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Fail")


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
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 11, check_overview)
        if check_overview == check_detail:
            var_app.logging.info("True")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Pass")
        else:
            var_app.logging.info("False")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Fail")


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
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 11, check_detail)
        if check_overview == check_detail:
            var_app.logging.info("True")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Pass")
        else:
            var_app.logging.info("False")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Fail")


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
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 11, check_detail)
        if check_overview == check_detail:
            var_app.logging.info("True")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Pass")
        else:
            var_app.logging.info("False")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Fail")


    def detail_vehicle_km_in_day(self, code, eventname, result):
        vehicle_detail = module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 10, 3)
        vehicle_detail = ''.join(re.findall(r'\d+', vehicle_detail))

        var_app.logging.info("--------------")
        var_app.logging.info("Giám sát - Thông tin chi tiết xe")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("Hiện trạng - Km trong ngày - " + vehicle_detail)
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 11, vehicle_detail)
        if vehicle_detail != "None":
            var_app.logging.info("True")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Pass")
        else:
            var_app.logging.info("False")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Fail")


    def detail_vehicle_cumulative_kilometers(self, code, eventname, result):
        check_detail = str(module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 22, 3))
        print("dettail: " + check_detail)

        var_app.logging.info("--------------")
        var_app.logging.info("Giám sát - Thông tin chi tiết xe")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("Hiện trạng - Km tích lũy - " + check_detail)
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 11, check_detail)
        if check_detail != "None":
            var_app.logging.info("True")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Pass")
        else:
            var_app.logging.info("False")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Fail")


    def detail_vehicle_stop(self, code, eventname, result):
        check_detail = str(module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 11, 3))
        print("dettail: " + check_detail)

        var_app.logging.info("--------------")
        var_app.logging.info("Giám sát - Thông tin chi tiết xe")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("Hiện trạng - Dừng đỗ - " + check_detail)
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 11, check_detail)
        if check_detail != "None":
            var_app.logging.info("True")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Pass")
        else:
            var_app.logging.info("False")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Fail")


    def detail_vehicle_stoping(self, code, eventname, result):
        check_detail = str(module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 59, 3))
        print("dettail: " + check_detail)

        var_app.logging.info("--------------")
        var_app.logging.info("Giám sát - Thông tin chi tiết xe")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("Hiện trạng - Đang đỗ - " + check_detail)
        var_app.logging.info("True")
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Pass")


    def detail_vehicle_stop_and_start_the_engine(self, code, eventname, result):
        check_detail = str(module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 60, 3))
        print("dettail: " + check_detail)

        var_app.logging.info("--------------")
        var_app.logging.info("Giám sát - Thông tin chi tiết xe")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 11, check_detail)
        var_app.logging.info("True")
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Pass")


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
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 11, check_detail)
        if check_overview == check_detail:
            var_app.logging.info("True")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Pass")
        else:
            var_app.logging.info("False")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Fail")


    def detail_vehicle_door_vehicle(self, code, eventname, result):
        check_overview = str(module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 18, 2))
        print("overview: " + check_overview)

        var_app.logging.info("--------------")
        var_app.logging.info("Giám sát - Thông tin chi tiết xe")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("Tổng quan - Cửa xe - " + check_overview)
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 11, check_overview)
        if check_overview != "None":
            var_app.logging.info("True")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Pass")
        else:
            var_app.logging.info("False")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Fail")


    def detail_vehicle_fuel(self, code, eventname, result):
        check_detail = str(module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 16, 3))
        print("dettail: " + check_detail)

        var_app.logging.info("--------------")
        var_app.logging.info("Giám sát - Thông tin chi tiết xe")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("Hiện trạng - Nhiên liệu - " + check_detail)
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 11, check_detail)
        if check_detail != "None":
            var_app.logging.info("True")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Pass")
        else:
            var_app.logging.info("False")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Fail")


    def detail_vehicle_temperature(self, code, eventname, result):
        check_detail = str(module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 17, 3))
        print("dettail: " + check_detail)

        var_app.logging.info("--------------")
        var_app.logging.info("Giám sát - Thông tin chi tiết xe")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("Hiện trạng - Nhiệt độ - " + check_detail)
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 11, check_detail)
        if check_detail != "None":
            var_app.logging.info("True")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Pass")
        else:
            var_app.logging.info("False")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Fail")


    def detail_vehicle_merory_card(self, code, eventname, result):
        check_detail = str(module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 24, 3))
        print("dettail: " + check_detail)

        var_app.logging.info("--------------")
        var_app.logging.info("Giám sát - Thông tin chi tiết xe")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("Hiện trạng - Thẻ nhớ - " + check_detail)
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 11, check_detail)
        if check_detail != "None":
            var_app.logging.info("True")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Pass")
        else:
            var_app.logging.info("False")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Fail")


    def detail_vehicle_group(self, code, eventname, result):
        check_detail = module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 25, 3)
        print("dettail: " + check_detail)

        var_app.logging.info("--------------")
        var_app.logging.info("Giám sát - Thông tin chi tiết xe")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("Hiện trạng - Nhóm đội - " + check_detail)
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 11, check_detail)
        if check_detail != "None":
            var_app.logging.info("True")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Pass")
        else:
            var_app.logging.info("False")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Fail")


    def detail_vehicle_drive(self, code, eventname, result):
        vehicle_detail = str(module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 26, 3))
        var_app.logging.info("--------------")
        var_app.logging.info("Giám sát - Thông tin chi tiết xe")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("Hiện trạng - Lái xe - " + vehicle_detail)
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 11, vehicle_detail)
        if vehicle_detail != "None":
            var_app.logging.info("True")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Pass")
        else:
            var_app.logging.info("False")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Fail")


    def detail_vehicle_license(self, code, eventname, result):
        vehicle_detail = str(module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 27, 3))
        var_app.logging.info("--------------")
        var_app.logging.info("Giám sát - Thông tin chi tiết xe")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("Hiện trạng - Bằng lái - " + vehicle_detail)
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 11, vehicle_detail)
        if vehicle_detail != "None":
            var_app.logging.info("True")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Pass")
        else:
            var_app.logging.info("False")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Fail")


    def detail_vehicle_phone(self, code, eventname, result):
        check_detail = str(module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 28, 3))
        print("dettail: " + check_detail)

        var_app.logging.info("--------------")
        var_app.logging.info("Giám sát - Thông tin chi tiết xe")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("Hiện trạng - Điện thoại - " + check_detail)
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 11, check_detail)
        var_app.logging.info("True")
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Pass")



    def detail_vehicle_continuous_driving_time(self, code, eventname, result):
        vehicle_detail = str(module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 29, 3))

        var_app.logging.info("--------------")
        var_app.logging.info("Giám sát - Thông tin chi tiết xe")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("Hiện trạng - Thời gian lái xe liên tục - " + vehicle_detail)
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 11, vehicle_detail)
        if vehicle_detail != "None":
            var_app.logging.info("True")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Pass")
        else:
            var_app.logging.info("False")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Fail")


    def detail_vehicle_driving_time_during_the_day(self, code, eventname, result):
        vehicle_detail = str(module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 30, 3))

        var_app.logging.info("--------------")
        var_app.logging.info("Giám sát - Thông tin chi tiết xe")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("Hiện trạng - Thời gian lái xe trong ngày - " + vehicle_detail)
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 11, vehicle_detail)
        if vehicle_detail != "None":
            var_app.logging.info("True")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Pass")
        else:
            var_app.logging.info("False")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Fail")


    def detail_vehicle_number_too_speed(self, code, eventname, result):
        vehicle_detail = str(module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 31, 3))

        var_app.logging.info("--------------")
        var_app.logging.info("Giám sát - Thông tin chi tiết xe")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("Hiện trạng - Sô lần quá tốc độ - " + vehicle_detail)
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 11, vehicle_detail)
        if vehicle_detail != "None":
            var_app.logging.info("True")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Pass")
        else:
            var_app.logging.info("False")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Fail")


    def detail_vehicle_management_department(self, code, eventname, result):
        check_detail = str(module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 32, 3))
        print("dettail: " + check_detail)

        var_app.logging.info("--------------")
        var_app.logging.info("Giám sát - Thông tin chi tiết xe")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("Hiện trạng - Sở quản lý - " + check_detail)
        if check_detail != "None":
            var_app.logging.info("True")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Pass")
        else:
            var_app.logging.info("False")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Fail")


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
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 11, check_detail)
        var_app.logging.info("True")
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Pass")


    def detail_vehicle_the_frist_activity(self, code, eventname, result):
        check_detail = str(module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 61, 3))
        print("dettail: " + check_detail)

        var_app.logging.info("--------------")
        var_app.logging.info("Giám sát - Thông tin chi tiết xe")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("Thiết bị - Hoạt động lần đầu - " + check_detail)
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 11, check_detail)
        if check_detail != "None":
            var_app.logging.info("True")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Pass")
        else:
            var_app.logging.info("False")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Fail")


    def detail_vehicle_news_recently(self, code, eventname, result):
        check_detail = str(module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 62, 3))
        print("dettail: " + check_detail)

        var_app.logging.info("--------------")
        var_app.logging.info("Giám sát - Thông tin chi tiết xe")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("Thiết bị - Bản tin gần nhất - " + check_detail)
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 11, check_detail)
        if check_detail != "None":
            var_app.logging.info("True")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Pass")
        else:
            var_app.logging.info("False")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Fail")


    def detail_vehicle_status_gps(self, code, eventname, result):
        check_detail = str(module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 63, 3))
        print("dettail: " + check_detail)

        var_app.logging.info("--------------")
        var_app.logging.info("Giám sát - Thông tin chi tiết xe")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("Thiết bị - Trạng thái GPS - " + check_detail)
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 11, check_detail)
        if check_detail != "None":
            var_app.logging.info("True")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Pass")
        else:
            var_app.logging.info("False")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Fail")


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
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 11, vehicle_sim2)
        if vehicle_sim1 == vehicle_sim2:
            var_app.logging.info("True")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Pass")
        else:
            var_app.logging.info("False")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Fail")


    def detail_vehicle_subscription_type(self, code, eventname, result):
        check_detail = str(module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 65, 3))
        print("dettail: " + check_detail)

        var_app.logging.info("--------------")
        var_app.logging.info("Giám sát - Thông tin chi tiết xe")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("Thiết bị - Loại thuê bao - " + check_detail)
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 11, check_detail)
        if check_detail != "None":
            var_app.logging.info("True")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Pass")
        else:
            var_app.logging.info("False")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Fail")


    def detail_vehicle_the_remaining_amount(self, code, eventname, result):
        check_detail = str(module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 69, 3))
        print("dettail: " + check_detail)

        var_app.logging.info("--------------")
        var_app.logging.info("Giám sát - Thông tin chi tiết xe")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("Thiết bị - Số tiền còn lại - " + check_detail)
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 11, check_detail)
        var_app.logging.info("True")
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Pass")


    def detail_vehicle_status_sim(self, code, eventname, result):
        check_detail = str(module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 70, 3))
        print("dettail: " + check_detail)

        var_app.logging.info("--------------")
        var_app.logging.info("Giám sát - Thông tin chi tiết xe")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("Thiết bị - Trạng thái SIM - " + check_detail)
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 11, check_detail)
        var_app.logging.info("True")
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Pass")


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
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 11, check_detail_timeupdate)
        if (check_detail_the_remaining_amount == check_status_sim == check_detail_timeupdate) or (check_detail_timeupdate!= "None"):
            var_app.logging.info("True")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Pass")
        else:
            var_app.logging.info("False")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Fail")


    def detail_vehicle_battert_level(self, code, eventname, result):
        check_detail = str(module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 66, 3))
        print("dettail: " + check_detail)

        var_app.logging.info("--------------")
        var_app.logging.info("Giám sát - Thông tin chi tiết xe")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("Thiết bị - Mức ắc quy - " + check_detail)
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 11, check_detail)
        if check_detail != "None":
            var_app.logging.info("True")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Pass")
        else:
            var_app.logging.info("False")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Fail")


    def detail_vehicle_power_status(self, code, eventname, result):
        check_detail = str(module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 67, 3))
        print("dettail: " + check_detail)

        var_app.logging.info("--------------")
        var_app.logging.info("Giám sát - Thông tin chi tiết xe")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("Thiết bị - Trạng thái nguồn - " + check_detail)
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 11, check_detail)
        if check_detail != "None":
            var_app.logging.info("True")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Pass")
        else:
            var_app.logging.info("False")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Fail")






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
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 11, check_detail)
        if check_detail != "None":
            var_app.logging.info("True")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Pass")
        else:
            var_app.logging.info("False")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Fail")


    def detail_vehicle_home_network(self, code, eventname, result):
        check_detail = str(module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 38, 3))
        print("dettail: " + check_detail)

        var_app.logging.info("--------------")
        var_app.logging.info("Giám sát - Thông tin chi tiết xe")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("Camera - Nhà mạng - " + check_detail)
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 11, check_detail)
        if check_detail != "None":
            var_app.logging.info("True")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Pass")
        else:
            var_app.logging.info("False")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Fail")


    def detail_vehicle_package_capacity(self, code, eventname, result):
        check_detail = str(module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 39, 3))
        print("dettail: " + check_detail)

        var_app.logging.info("--------------")
        var_app.logging.info("Giám sát - Thông tin chi tiết xe")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("Camera - Dung lượng gói cước - " + check_detail)
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 11, check_detail)
        if check_detail != "None":
            var_app.logging.info("True")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Pass")
        else:
            var_app.logging.info("False")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Fail")


    def detail_vehicle_number_of_days_of_storage(self, code, eventname, result):
        check_detail = str(module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 40, 3))
        print("dettail: " + check_detail)

        var_app.logging.info("--------------")
        var_app.logging.info("Giám sát - Thông tin chi tiết xe")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("Camera - Số ngày lưu trữ - " + check_detail)
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 11, check_detail)
        if check_detail != "None":
            var_app.logging.info("True")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Pass")
        else:
            var_app.logging.info("False")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Fail")


    def detail_vehicle_number_of_chanels_of_storage(self, code, eventname, result):
        check_detail = str(module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 41, 3))
        print("dettail: " + check_detail)

        var_app.logging.info("--------------")
        var_app.logging.info("Giám sát - Thông tin chi tiết xe")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("Camera - Số kênh lưu trữ - " + check_detail)
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 11, check_detail)
        if check_detail != "None":
            var_app.logging.info("True")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Pass")
        else:
            var_app.logging.info("False")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Fail")


    def detail_vehicle_location(self, code, eventname, result):
        check_detail = str(module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 42, 3))
        print("dettail: " + check_detail)

        var_app.logging.info("--------------")
        var_app.logging.info("Giám sát - Thông tin chi tiết xe")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("Camera - Định vị - " + check_detail)
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 11, check_detail)
        if check_detail != "None":
            var_app.logging.info("True")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Pass")
        else:
            var_app.logging.info("False")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Fail")


    def detail_vehicle_image(self, code, eventname, result):
        check_detail = str(module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 43, 3))
        print("dettail: " + check_detail)

        var_app.logging.info("--------------")
        var_app.logging.info("Giám sát - Thông tin chi tiết xe")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("Camera - Ảnh - " + check_detail)
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 11, check_detail)
        if check_detail != "None":
            var_app.logging.info("True")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Pass")
        else:
            var_app.logging.info("False")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Fail")


    def detail_vehicle_video(self, code, eventname, result):
        check_detail = str(module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 44, 3))
        print("dettail: " + check_detail)

        var_app.logging.info("--------------")
        var_app.logging.info("Giám sát - Thông tin chi tiết xe")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("Camera - Video - " + check_detail)
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 11, check_detail)
        if check_detail != "None":
            var_app.logging.info("True")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Pass")
        else:
            var_app.logging.info("False")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Fail")


    def detail_vehicle_channel_camera(self, code, eventname, result):
        check_detail = str(module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 45, 3))
        print("dettail: " + check_detail)

        var_app.logging.info("--------------")
        var_app.logging.info("Giám sát - Thông tin chi tiết xe")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("Camera - Kênh lắp camera - " + check_detail)
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 11, check_detail)
        if check_detail != "None":
            var_app.logging.info("True")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Pass")
        else:
            var_app.logging.info("False")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Fail")


    def detail_vehicle_channel_active(self, code, eventname, result):
        check_detail = str(module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 46, 3))
        print("dettail: " + check_detail)

        var_app.logging.info("--------------")
        var_app.logging.info("Giám sát - Thông tin chi tiết xe")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("Camera - Kênh hoạt động - " + check_detail)
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 11, check_detail)
        if check_detail != "None":
            var_app.logging.info("True")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Pass")
        else:
            var_app.logging.info("False")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Fail")


    def detail_vehicle_network_connection(self, code, eventname, result):
        check_detail = str(module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 68, 3))
        print("dettail: " + check_detail)

        var_app.logging.info("--------------")
        var_app.logging.info("Giám sát - Thông tin chi tiết xe")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("Camera - Mạng kết nối - " + check_detail)
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 11, check_detail)
        if check_detail != "None":
            var_app.logging.info("True")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Pass")
        else:
            var_app.logging.info("False")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Fail")


    def detail_vehicle_icon_update(self, code, eventname, result):
        var_app.driver.implicitly_wait(5)
        var_app.driver.find_element(By.XPATH, var_app.detail_vehicle_icon_update).click()

        var_app.logging.info("--------------")
        var_app.logging.info("Giám sát - Thông tin chi tiết xe")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("Icon cập nhật")
        var_app.logging.info("True")
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Pass")





    def detail_vehicle_monitor_back(self):
        var_app.driver.implicitly_wait(0.5)
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


    def detail_vehicle_monitor_video(self, code, eventname, result):
        var_app.driver.implicitly_wait(5)
        try:
            var_app.driver.find_element(By.XPATH, var_app.detail_vehicle_monitor_video).click()
        except:
            detail.detail_vehicle_monitor_back(self)
            login_app.login.login_v3(self, "43E02740", "12341234")
            time.sleep(1)
            var_app.driver.implicitly_wait(3)
            var_app.driver.find_element(By.XPATH, var_app.detail_vehicle_choose1).click()
            time.sleep(2.5)
            var_app.driver.find_element(By.XPATH, var_app.detail_vehicle).click()
            time.sleep(2.5)
            var_app.driver.find_element(By.XPATH, var_app.detail_vehicle_monitor_video).click()

        time.sleep(2)
        module_other_app.write_result_text_try_if(code, eventname, result, "Giám sát - Thông tin chi tiết xe - Link liên kết",
                                              var_app.check_detail_vehicle_monitor_video, "GIÁM SÁT NHIỀU CAMERA", "_GiamSat_ChiTietXe_GiamSatCamera.png")

        try:
            var_app.driver.find_element(By.XPATH, var_app.detail_vehicle_monitor_video_iconx).click()
            time.sleep(1.5)
        except:
            pass

    def detail_vehicle_monitor_image(self, code, eventname, result):
        var_app.driver.implicitly_wait(5)
        try:
            var_app.driver.find_element(By.XPATH, var_app.detail_vehicle_monitor_image).click()
        except:
            detail.detail_vehicle_monitor_back(self)
            login_app.login.login_v3(self, "43E02740", "12341234")
            time.sleep(1)
            var_app.driver.implicitly_wait(3)
            var_app.driver.find_element(By.XPATH, var_app.detail_vehicle_choose1).click()
            time.sleep(2.5)
            var_app.driver.find_element(By.XPATH, var_app.detail_vehicle).click()
            time.sleep(2.5)
            var_app.driver.find_element(By.XPATH, var_app.detail_vehicle_monitor_image).click()
        time.sleep(2)
        module_other_app.write_result_text_try_if(code, eventname, result, "Giám sát - Thông tin chi tiết xe - Link liên kết",
                                              var_app.check_detail_vehicle_monitor_image, "CHI TIẾT XE", "_GiamSat_ChiTietXe_GiamSatHinhAnh.png")

        try:
            var_app.driver.find_element(By.XPATH, var_app.detail_vehicle_monitor_image_iconx).click()
            time.sleep(1.5)
        except:
            pass


    def detail_vehicle_fuel_chart(self, code, eventname, result):
        var_app.driver.implicitly_wait(5)
        try:
            var_app.driver.find_element(By.XPATH, var_app.detail_vehicle_fuel_chart).click()
        except:
            detail.detail_vehicle_monitor_back(self)
            login_app.login.login_v3(self, "43E02740", "12341234")
            time.sleep(1)
            var_app.driver.implicitly_wait(3)
            var_app.driver.find_element(By.XPATH, var_app.detail_vehicle_choose1).click()
            time.sleep(2.5)
            var_app.driver.find_element(By.XPATH, var_app.detail_vehicle).click()
            time.sleep(2.5)
            var_app.driver.find_element(By.XPATH, var_app.detail_vehicle_fuel_chart).click()
        time.sleep(2)
        module_other_app.write_result_text_try_if(code, eventname, result, "Giám sát - Thông tin chi tiết xe - Link liên kết",
                                              var_app.check_detail_vehicle_fuel_chart, "BIỂU ĐỒ NHIÊN LIỆU", "_GiamSat_ChiTietXe_BieuDoNhiienLieu.png")

        # try:
        #     var_app.driver.find_element(By.XPATH, var_app.detail_vehicle_fuel_chart_iconx).click()
        #     time.sleep(1.5)
        # except:
        #     pass
        #
        # try:
        #     var_app.driver.find_element(By.XPATH, var_app.detail_vehicle_iconx).click()
        #     time.sleep(1.5)
        # except:
        #     pass
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
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        try:
            var_app.driver.find_element(By.XPATH, var_app.detail_vehicle_choose1).click()
        except:
            try:
                var_app.driver.find_element(By.XPATH, var_app.detail_vehicle_iconx3).click()
            except:
                pass
            login_app.login.check_logout(self)
            login_app.login.login_v3(self, "43E02740", "12341234")
            var_app.driver.find_element(By.XPATH, var_app.detail_vehicle_choose1).click()
        time.sleep(2.5)
        try:
            var_app.driver.find_element(By.XPATH, var_app.minitor_route).click()
        except:
            var_app.driver.find_element(By.XPATH, var_app.detail_vehicle_iconx4).click()
            time.sleep(1)
            var_app.driver.find_element(By.XPATH, var_app.detail_vehicle_choose1).click()
            time.sleep(2)
            var_app.driver.find_element(By.XPATH, var_app.minitor_route).click()

        time.sleep(4)
        var_app.driver.tap([(50, 1440)])
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
        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(2)
        except:
            pass
        try:
            var_app.driver.find_element(By.XPATH, var_app.detail_vehicle_choose1).click()
        except:
            login_app.login.check_logout(self)
            login_app.login.login_v3(self, "43E02740", "12341234")
            var_app.driver.find_element(By.XPATH, var_app.detail_vehicle_choose1).click()
        time.sleep(3)
        var_app.driver.find_element(By.XPATH, link).click()
        time.sleep(3)

        module_other_app.write_result_text_try_if(code, eventname, result, "Giám sát - Chi tiết xe - link liên kết click vào xe",
                                              path_check, desire, path_image)

        try:
            var_app.driver.find_element(By.XPATH, link_iconx).click()
        except:
            pass
        time.sleep(1)
        var_app.driver.press_keycode(4)
        time.sleep(2)



    @retry(tries=2, delay=2, backoff=1, jitter=5, )
    def affiliate_link_detail(self, code, eventname, result, startX, startY, endX, endY, duration,
                              link, link_iconx, path_check, desire, path_image):
        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(2)
        except:
            pass


        try:
            var_app.driver.find_element(By.XPATH, var_app.detail_vehicle_choose1).click()
        except:
            login_app.login.login_v3(self, "43E02740", "12341234")
            overview.vehicle_status(self, "Minitor53", eventname, result,
                                    "Tất cả", 650, 210, "")
            var_app.driver.find_element(By.XPATH, var_app.detail_vehicle_choose1).click()

        time.sleep(2)
        try:
            var_app.driver.find_element(By.XPATH, var_app.icon_up).click()
            time.sleep(2.5)
        except:
            login_app.login.login_v3(self, "43E02740", "12341234")
            overview.vehicle_status(self, "Minitor53", eventname, result,
                                    "Tất cả", 650, 210, "")
            var_app.driver.find_element(By.XPATH, var_app.detail_vehicle_choose1).click()
            time.sleep(2)
            var_app.driver.find_element(By.XPATH, var_app.icon_up).click()
            time.sleep(2.5)



        var_app.driver.implicitly_wait(1)
        scroll_and_click(startX, startY, endX, endY, duration, link)
        # module_other_app.write_result_text_try_if(code, eventname, result,
        #                                           "Giám sát - đi tới link liên kết click vào xe", path_check, desire, path_image)

        if code == "Minitor170":
            module_other_app.write_result_displayed_try(code, eventname, result, "Giám sát - đi tới link liên kết click vào xe",
                                                    path_check, path_image)
        else:
            module_other_app.write_result_text_try_if(code, eventname, result, "Giám sát - đi tới link liên kết click vào xe",
                                                  path_check, desire, path_image)


        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, link_iconx).click()
            time.sleep(2)
        except:
            var_app.driver.press_keycode(4)
            time.sleep(2)


