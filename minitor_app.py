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



def get_detail(path_get, row, column):
    var_app.driver.implicitly_wait(2)
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
    headers = {"cookie": "_ga=GA1.1.987778944.1710466198; route_column_truongvck1=chkVgps,chkCoVong,chkKm; route_column_class_truongvck1=vtgps,vtcovong,km; route_column_partner1001=chkVgps,chkCoVong,chkKm; route_column_class_partner1001=vtgps,vtcovong,km; route_column_ungroup_1=chkVgps,chkCoVong,chkKm; route_column_class_ungroup_1=vtgps,vtcovong,km; route_column_truongtq@bagroup.vn=chkVgps,chkCoVong,chkKm; route_column_class_truongtq@bagroup.vn=vtgps,vtcovong,km; route_column_ungroup=chkVgps,chkCoVong,chkKm,chkCua,chkVbgt; route_column_class_ungroup=vtgps,vtcovong,km,cua,vtbgt; route_column_43e02743=chkVgps,chkCoVong; route_column_class_43e02743=vtgps,vtcovong; route_column_viconshipdanang1=chkCoVong,chkAddress; route_column_class_viconshipdanang1=vtcovong,addr; route_column_43e02740=chkVgps,chkCoVong,chkKm; route_column_class_43e02740=vtgps,vtcovong,km; _ga_9LVRP2FDNH=GS1.1.1719224668.12.0.1719224668.0.0.0; CultureInfo=vi-VN; ResourceVersion=20240625v1; ASP.NET_SessionId=dxyzbsn2ec5ab4kchynfzxx1; ARRAffinity=369bb8b1dab68ca0e7a2dc8719a27d710fd20d197411d8ead2a35c03dfd4c644; browsers=[{'PK_BrowserVersionID':1,'Name':'Chrome','Version':'90','CreatedDate':'2022-03-21T00:00:00'},{'PK_BrowserVersionID':2,'Name':'Edg','Version':'100','CreatedDate':'2022-03-21T00:00:00'},{'PK_BrowserVersionID':3,'Name':'Firefox','Version':'90','CreatedDate':'2022-03-21T00:00:00'},{'PK_BrowserVersionID':4,'Name':'OPR','Version':'38','CreatedDate':'2022-03-21T00:00:00'},{'PK_BrowserVersionID':6,'Name':'Safari','Version':'10','CreatedDate':'2022-03-21T00:00:00'},{'PK_BrowserVersionID':7,'Name':'IE','Version':'21','CreatedDate':'2022-03-21T00:00:00'}]; __zi=2000.SSZzejyD6jSbWlwbsKiDrs-0ghkNHHMLCvAWfOK71uCYrF_ZXGDEpINHykE71K-38jNxhuKAI8icrFkbDW.1; Login_.ASPXFORMSAUTH=73662042ADEB03EC4B32DAC13D82D3A45575430EDC7BD8688D7864E675031261CD109BF70A6293B62A2F42F18A07988FA9949F4C5016EBCB7BF647F71F0A2D7EB646946B3C5C6980F99A141DA6194D22AE666EE66CB8ABD2C8A59C194995CBAC; __AntiXsrfToken=52ca4293c31f4526b4e4c79c1a49f192; _ga_02FC5P5V42=GS1.1.1719285456.251.1.1719285919.0.0.0"}

    response = requests.request("POST", api_url, data=todo, headers=headers)
    response.json()
    res = json.loads(response.text)
    print(res)
    print("Phương tiện 0: ", res['data'][0]['plate'])

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






class overview:

    def search_vehicle(self, code, eventname, result):
        var_app.driver.implicitly_wait(5)

        login_app.login.login_v3(self, "43E02740", "12341234")
        try:
            var_app.driver.find_element(By.XPATH, var_app.search_vehicle).click()
            time.sleep(1)
            name_vehicle1 = var_app.driver.find_element(By.XPATH, var_app.minitor_name_vehicle1).text
            var_app.driver.find_element(By.XPATH, var_app.search_vehicle_input).send_keys(name_vehicle1)
            time.sleep(1.5)
            var_app.driver.find_element(By.XPATH, var_app.minitor_name_vehicle).click()
        except:
            var_app.driver.find_element(by=AppiumBy.XPATH, value=var_app.login_buttonlogin).click()
            time.sleep(2)
            var_app.driver.find_element(By.XPATH, var_app.search_vehicle).click()
            time.sleep(1)
            name_vehicle1 = var_app.driver.find_element(By.XPATH, var_app.minitor_name_vehicle1).text
            var_app.driver.find_element(By.XPATH, var_app.search_vehicle_input).send_keys(name_vehicle1)
            time.sleep(1.5)
            var_app.driver.find_element(By.XPATH, var_app.minitor_name_vehicle).click()
        time.sleep(2.5)
        module_other_app.write_result_text_try_if(code, eventname, result, "Giám sát - Tìm kiếm xe",
                                              var_app.check_search_vehicle, name_vehicle1, "_GiamSat_TimKiemXe.png")

        try:
            var_app.driver.find_element(By.XPATH, var_app.detail_vehicle_iconx).click()
            time.sleep(1)
        except:
            pass



    def select_1group(self, code, eventname, result):
        var_app.driver.implicitly_wait(5)
        try:
            var_app.driver.find_element(By.XPATH, var_app.select_group_icon).click()
        except:
            login_app.login.login_v3(self, "43E02740", "12341234")
            var_app.driver.find_element(By.XPATH, var_app.select_group_icon).click()
        time.sleep(1.5)
        try:
            var_app.driver.find_element(By.XPATH, var_app.select_group_input).send_keys("0")
            time.sleep(1)
            name_group1 = var_app.driver.find_element(By.XPATH, var_app.minitor_name_group1).text
            print(name_group1[:-4])
            time.sleep(1)
            var_app.driver.find_element(By.XPATH, var_app.minitor_name_group1_checkbox).click()
        except:
            var_app.driver.find_element(by=AppiumBy.XPATH, value=var_app.login_buttonlogin).click()
            time.sleep(2)
            var_app.driver.find_element(By.XPATH, var_app.select_group_icon).click()
            time.sleep(1.5)
            var_app.driver.find_element(By.XPATH, var_app.select_group_input).send_keys("0")
            time.sleep(1)
            name_group1 = var_app.driver.find_element(By.XPATH, var_app.minitor_name_group1).text
            print(name_group1[:-4])
            time.sleep(1)
            var_app.driver.find_element(By.XPATH, var_app.minitor_name_group1_checkbox).click()
        time.sleep(0.5)
        var_app.driver.find_element(By.XPATH, var_app.minitor_name_group_choose).click()
        time.sleep(2.5)
        var_app.logging.info("--------------")
        var_app.logging.info("Giám sát - chọn nhóm")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        print("(//android.view.View[@content-desc='"+name_group1[:-4]+ "_C. '])[1]")
        try:
            check_displayed = var_app.driver.find_element(By.XPATH, "(//android.view.View[@content-desc='"+name_group1[:-4]+ "_C. '])[1]").is_displayed()
            var_app.logging.info("True")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Pass")
        except NoSuchElementException:
            var_app.logging.info("False")
            var_app.driver.save_screenshot(var_app.imagepath + code + "_GiamSat_Chon1Nhom.png")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Fail")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 9, code + "_GiamSat_Chon1Nhom.png")

        var_app.driver.find_element(By.XPATH, var_app.select_group_icon).click()
        time.sleep(1)
        var_app.driver.find_element(By.XPATH, var_app.minitor_name_group1_checkbox).click()
        time.sleep(0.5)
        var_app.driver.find_element(By.XPATH, var_app.minitor_name_group_choose).click()
        time.sleep(3)



    def select_manygroup(self, code, eventname, result):
        var_app.driver.implicitly_wait(5)
        try:
            var_app.driver.find_element(By.XPATH, var_app.select_group_icon).click()
        except:
            login_app.login.login_v3(self, "43E02740", "12341234")
            var_app.driver.find_element(By.XPATH, var_app.select_group_icon).click()
        time.sleep(1.5)
        try:
            var_app.driver.find_element(By.XPATH, var_app.select_group_input).send_keys("0")
            time.sleep(1)
            var_app.driver.find_element(By.XPATH, var_app.minitor_name_group1_checkbox).click()
            var_app.driver.find_element(By.XPATH, var_app.minitor_name_group1_checkbox2).click()

        except:
            var_app.driver.find_element(by=AppiumBy.XPATH, value=var_app.login_buttonlogin).click()
            time.sleep(2)
            var_app.driver.find_element(By.XPATH, var_app.select_group_icon).click()
            time.sleep(1.5)
            var_app.driver.find_element(By.XPATH, var_app.select_group_input).send_keys("0")
            time.sleep(1)
            var_app.driver.find_element(By.XPATH, var_app.minitor_name_group1_checkbox).click()
            var_app.driver.find_element(By.XPATH, var_app.minitor_name_group1_checkbox2).click()

        time.sleep(0.5)
        var_app.driver.find_element(By.XPATH, var_app.minitor_name_group_choose).click()
        time.sleep(3)
        var_app.logging.info("--------------")
        var_app.logging.info("Giám sát - chọn nhóm")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("True")
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Pass")

        var_app.driver.find_element(By.XPATH, var_app.select_group_icon).click()
        time.sleep(1)
        var_app.driver.find_element(By.XPATH, var_app.minitor_name_group1_checkbox).click()
        time.sleep(0.5)
        var_app.driver.find_element(By.XPATH, var_app.minitor_name_group1_checkbox2).click()
        time.sleep(0.5)
        var_app.driver.find_element(By.XPATH, var_app.minitor_name_group_choose).click()
        time.sleep(3)



    def vehicle_status(self, code, eventname, result, status_vehicle, name_status, quaility_vehicle, path_image):
        var_app.driver.implicitly_wait(5)
        try:
            var_app.driver.find_element(By.XPATH, var_app.vehicle_status_icon).click()
            time.sleep(1.5)
        except:
            login_app.login.check_logout(self)
            login_app.login.login_v3(self, "43E02740", "12341234")
            var_app.driver.find_element(By.XPATH, var_app.vehicle_status_icon).click()
            time.sleep(1.5)

        name_status = var_app.driver.find_element(By.XPATH, name_status).text
        quaility_vehicle = var_app.driver.find_element(By.XPATH, quaility_vehicle).text
        quaility_vehicle = ''.join(re.findall(r'\d+', quaility_vehicle))
        quaility_vehicle = int(quaility_vehicle)

        print("trạng thái phương tiện {}, số lượng {}".format(name_status, quaility_vehicle))
        print(type(quaility_vehicle))
        try:
            var_app.driver.find_element(By.XPATH, status_vehicle).click()
            time.sleep(1)
        except:
            var_app.driver.find_element(by=AppiumBy.XPATH, value=var_app.login_buttonlogin).click()
            time.sleep(2)
            var_app.driver.find_element(By.XPATH, var_app.vehicle_status_icon).click()
            time.sleep(1.5)
            var_app.driver.find_element(By.XPATH, status_vehicle).click()
            time.sleep(1)
        time.sleep(2)
        if quaility_vehicle == 0:
            module_other_app.write_result_not_displayed_try(code, eventname, result, "Giám sát - Trạng thái xe",
                                                    var_app.path_vehicle_status, path_image)

        else:
            module_other_app.write_result_displayed_try(code, eventname, result, "Giám sát - Trạng thái xe",
                                                    var_app.path_vehicle_status, path_image)
        var_app.logging.info("trạng thái phương tiện {}, số lượng {}".format(name_status, quaility_vehicle))



    def goto_google(self, code, eventname, result):
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
        var_app.driver.implicitly_wait(2)
        module_other_app.clearData_luutamthoi(var_app.path_luutamthoi, "Sheet1", "", "", "")


        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
        except:
            pass

        var_app.driver.implicitly_wait(5)
        try:
            overview.vehicle_status(self, "Minitor05", eventname, result,
                                                var_app.status_move, var_app.name_move, var_app.quaility_move,
                                                "_GiamSat_TrangThai_DiChuyen.png")
        except:
            login_app.login.check_logout(self)
            login_app.login.login_v3(self, "43E02740", "12341234")
            overview.vehicle_status(self, "Minitor05", eventname, result,
                                                var_app.status_move, var_app.name_move, var_app.quaility_move,
                                                "_GiamSat_TrangThai_DiChuyen.png")


        var_app.driver.find_element(By.XPATH, var_app.detail_vehicle_choose1).click()
        time.sleep(2.5)

        var_app.driver.implicitly_wait(3)
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
        time.sleep(2)
        get_detail(var_app.detail_number_sim, 19, 3)
        get_detail(var_app.detail_registration_date, 20, 3)
        get_detail(var_app.detail_vehicle_plate, 6, 3)
        get_detail(var_app.detail_imei, 21, 3)
        get_detail(var_app.detail_adress, 14, 3)
        get_detail(var_app.detail_time, 7, 3)
        get_detail(var_app.detail_speed, 8, 3)
        get_detail(var_app.detail_engine, 12, 3)
        get_detail(var_app.detail_km_in_day, 10, 3)
        get_detail(var_app.detail_km_cumulative, 22, 3)
        get_detail(var_app.detail_stop, 11, 3)
        get_detail(var_app.detail_ari_condition, 13, 3)

        # swipe(startX, startY, endX, endY, duration)
        var_app.driver.swipe(400, 1350, 450, 400, 1000)
        time.sleep(1)
        get_detail(var_app.detail_open_of_nember, 23, 3)
        select_detail("Nhiên liệu", 16)
        select_detail("Nhiệt độ", 17)
        select_detail("Nhóm đội", 25)
        select_detail("VIN", 36)
        select_detail("Số lần mở cửa", 23)
        select_detail("Thẻ nhớ", 24)
        get_detail(var_app.detail_driver, 26, 3)
        get_detail(var_app.detail_driver_liscense, 27, 3)
        get_detail(var_app.detail_phone_number, 28, 3)
        get_detail(var_app.detail_continuous_driving_time, 29, 3)
        get_detail(var_app.detail_driving_time_during_the_day, 30, 3)
        get_detail(var_app.detail_too_speed, 31, 3)
        get_detail(var_app.detail_management_department, 32, 3)

        var_app.driver.find_element(By.XPATH, var_app.detail_vehicle_bacam).click()
        time.sleep(1)
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



    def detail_vehicle_liscense_plate(self, code, eventname, result):
        vehicle_overview = str(module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 6, 2))
        vehicle_detail = str(module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 6, 3))
        vehicle_api = str(module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 6, 4))
        var_app.logging.info("--------------")
        var_app.logging.info("Giám sát - Thông tin chi tiết xe")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("Tổng quan - biển số xe - " + vehicle_overview)
        var_app.logging.info("Chi tiết - biển số xe - " + vehicle_detail)
        var_app.logging.info("Check api - biển số xe - " + vehicle_api)
        if vehicle_overview == vehicle_detail == vehicle_api:
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

        check_api = str(module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 7, 4))
        check_api_hour_minute = check_api[11:16]
        print("api: " + check_api_hour_minute)
        check_api_day = check_api[8:10]
        print("api: " + check_api_day)
        check_api_month = check_api[5:7]
        print("api: " + check_api_month)
        check_api_year = check_api[0:4]
        print("api: " + check_api_year)
        check_api = check_api_hour_minute + " " + check_api_day + "/" + check_api_month + "/" + check_api_year
        print(check_api)

        var_app.logging.info("--------------")
        var_app.logging.info("Giám sát - Thông tin chi tiết xe")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("Tổng quan - Thời gian - " + check_overview)
        var_app.logging.info("Chi tiết - Thời gian - " + check_detail)
        var_app.logging.info("Check api - Thời gian - " + check_api)
        if check_overview == check_detail == check_api:
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

        check_api = str(module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 14, 4))
        print("api: ", check_api)

        var_app.logging.info("--------------")
        var_app.logging.info("Giám sát - Thông tin chi tiết xe")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("Tổng quan - Địa chỉ - " + check_overview)
        var_app.logging.info("Chi tiết - Địa chỉ - " + check_detail)
        var_app.logging.info("Check api - Địa chỉ - " + check_api)
        if check_overview == check_detail == check_api:
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

        check_api = str(module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 8, 4))
        check_api = check_api + " Km/h"
        print("api: ", check_api)

        var_app.logging.info("--------------")
        var_app.logging.info("Giám sát - Thông tin chi tiết xe")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("Tổng quan - Vận tốc gps - " + check_overview)
        var_app.logging.info("Chi tiết - Vận tốc gps - " + check_detail)
        var_app.logging.info("Check api - Vận tốc gps - " + check_api)
        if check_overview == check_detail == check_api:
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
        var_app.logging.info("Chi tiết - Động cơ - " + check_detail)
        if check_overview == check_detail:
            var_app.logging.info("True")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Pass")
        else:
            var_app.logging.info("False")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Fail")



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
        var_app.logging.info("Chi tiết - Điều hòa - " + check_detail)
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
        if check_overview != None:
            var_app.logging.info("True")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Pass")
        else:
            var_app.logging.info("False")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Fail")



    def detail_vehicle_sim_number(self, code, eventname, result):
        check_detail = str(module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 19, 3))
        print("overview: " + check_detail)

        var_app.logging.info("--------------")
        var_app.logging.info("Giám sát - Thông tin chi tiết xe")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("Tổng quan - Số sim - " + check_detail)
        if check_detail != None:
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
        var_app.logging.info("Tổng quan - Ngày đăng ký - " + check_detail)
        if check_detail != None:
            var_app.logging.info("True")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Pass")
        else:
            var_app.logging.info("False")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Fail")



    def detail_vehicle_imei(self, code, eventname, result):
        check_detail = str(module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 21, 3))
        print("dettail: " + check_detail)

        var_app.logging.info("--------------")
        var_app.logging.info("Giám sát - Thông tin chi tiết xe")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("Tổng quan - Imei - " + check_detail)
        if check_detail != None:
            var_app.logging.info("True")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Pass")
        else:
            var_app.logging.info("False")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Fail")



    def detail_vehicle_km_in_day(self, code, eventname, result):
        vehicle_detail = module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 10, 3)
        vehicle_detail = ''.join(re.findall(r'\d+', vehicle_detail))

        vehicle_api = str(module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 10, 4))
        vehicle_api = ''.join(re.findall(r'\d+', vehicle_api))

        var_app.logging.info("--------------")
        var_app.logging.info("Giám sát - Thông tin chi tiết xe")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("Chi tiết - Km trong ngày - " + vehicle_detail)
        var_app.logging.info("Check api - Km trong ngày - " + vehicle_api)
        if vehicle_detail == vehicle_api:
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
        var_app.logging.info("Tổng quan - Km tích lũy - " + check_detail)
        if check_detail != None:
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
        var_app.logging.info("Tổng quan - Dừng đỗ - " + check_detail)
        if check_detail != None:
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
        if check_detail != None:
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
        var_app.logging.info("Tổng quan - Nhiên liệu - " + check_detail)
        if check_detail != None:
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
        var_app.logging.info("Tổng quan - Nhiệt độ - " + check_detail)
        if check_detail != None:
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
        var_app.logging.info("Tổng quan - Thẻ nhớ - " + check_detail)
        if check_detail != None:
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
        var_app.logging.info("Tổng quan - Nhóm đội - " + check_detail)
        if check_detail != None:
            var_app.logging.info("True")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Pass")
        else:
            var_app.logging.info("False")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Fail")



    def detail_vehicle_vin(self, code, eventname, result):
        check_detail = str(module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 36, 3))
        print("dettail: " + check_detail)

        var_app.logging.info("--------------")
        var_app.logging.info("Giám sát - Thông tin chi tiết xe")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("Tổng quan - Vin - " + check_detail)
        if check_detail != None:
            var_app.logging.info("True")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Pass")
        else:
            var_app.logging.info("False")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Fail")



    def detail_vehicle_drive(self, code, eventname, result):
        vehicle_detail = str(module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 26, 3))
        vehicle_api = str(module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 26, 4))
        var_app.logging.info("--------------")
        var_app.logging.info("Giám sát - Thông tin chi tiết xe")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("Chi tiết - Lái xe - " + vehicle_detail)
        var_app.logging.info("Check api - Lái xe - " + vehicle_api)
        if vehicle_detail == vehicle_api:
            var_app.logging.info("True")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Pass")
        else:
            var_app.logging.info("False")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Fail")



    def detail_vehicle_license(self, code, eventname, result):
        vehicle_detail = str(module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 27, 3))
        vehicle_api = str(module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 27, 4))
        var_app.logging.info("--------------")
        var_app.logging.info("Giám sát - Thông tin chi tiết xe")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("Chi tiết - Bằng lái - " + vehicle_detail)
        var_app.logging.info("Check api - Bằng lái - " + vehicle_api)
        if vehicle_detail == vehicle_api:
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
        var_app.logging.info("Tổng quan - Điện thoại - " + check_detail)
        if check_detail != None:
            var_app.logging.info("True")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Pass")
        else:
            var_app.logging.info("False")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Fail")



    def detail_vehicle_continuous_driving_time(self, code, eventname, result):
        vehicle_detail = str(module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 29, 3))
        vehicle_api = str(module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 29, 4))
        vehicle_api = vehicle_api + " phút"

        var_app.logging.info("--------------")
        var_app.logging.info("Giám sát - Thông tin chi tiết xe")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("Chi tiết - Thời gian lái xe liên tục - " + vehicle_detail)
        var_app.logging.info("Check api -Thời gian lái xe liên tục - " + vehicle_api)
        if vehicle_detail == vehicle_api:
            var_app.logging.info("True")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Pass")
        else:
            var_app.logging.info("False")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Fail")



    def detail_vehicle_driving_time_during_the_day(self, code, eventname, result):
        vehicle_detail = str(module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 30, 3))
        vehicle_api = str(module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 30, 4))
        vehicle_api = vehicle_api + " phút"

        var_app.logging.info("--------------")
        var_app.logging.info("Giám sát - Thông tin chi tiết xe")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("Chi tiết - Thời gian lái xe trong ngày - " + vehicle_detail)
        var_app.logging.info("Check api -Thời gian lái xe trong ngày - " + vehicle_api)
        if vehicle_detail == vehicle_api:
            var_app.logging.info("True")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Pass")
        else:
            var_app.logging.info("False")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Fail")



    def detail_vehicle_number_too_speed(self, code, eventname, result):
        vehicle_detail = str(module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 31, 3))
        vehicle_api = str(module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 31, 4))
        vehicle_api = vehicle_api + " lần"

        var_app.logging.info("--------------")
        var_app.logging.info("Giám sát - Thông tin chi tiết xe")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("Chi tiết - Sô lần quá tốc độ - " + vehicle_detail)
        var_app.logging.info("Check api -Thời gian lái xe trong ngày - " + vehicle_api)
        if vehicle_detail == vehicle_api:
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
        var_app.logging.info("Tổng quan - Sở quản lý - " + check_detail)
        if check_detail != None:
            var_app.logging.info("True")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Pass")
        else:
            var_app.logging.info("False")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Fail")



    def detail_vehicle_package_name(self, code, eventname, result):
        check_detail = str(module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 37, 3))
        print("dettail: " + check_detail)

        var_app.logging.info("--------------")
        var_app.logging.info("Giám sát - Thông tin chi tiết xe")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("Tổng quan - Tên gói cước - " + check_detail)
        if check_detail != None:
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
        var_app.logging.info("Tổng quan - Nhà mạng - " + check_detail)
        if check_detail != None:
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
        var_app.logging.info("Tổng quan - Dung lượng gói cước - " + check_detail)
        if check_detail != None:
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
        var_app.logging.info("Tổng quan - Số ngày lưu trữ - " + check_detail)
        if check_detail != None:
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
        var_app.logging.info("Tổng quan - Số kênh lưu trữ - " + check_detail)
        if check_detail != None:
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
        var_app.logging.info("Tổng quan - Định vị - " + check_detail)
        if check_detail != None:
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
        var_app.logging.info("Tổng quan - Ảnh - " + check_detail)
        if check_detail != None:
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
        var_app.logging.info("Tổng quan - Video - " + check_detail)
        if check_detail != None:
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
        var_app.logging.info("Tổng quan - Kênh lắp camera - " + check_detail)
        if check_detail != None:
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
        var_app.logging.info("Tổng quan - Kênh hoạt động - " + check_detail)
        if check_detail != None:
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
        except:
            pass


        var_app.driver.find_element(By.XPATH, var_app.detail_vehicle_choose1).click()
        time.sleep(2.5)
        var_app.driver.find_element(By.XPATH, var_app.minitor_route).click()

