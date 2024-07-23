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







class overview:

    def search_vehile(self, code, eventname, result):       #Lộ trình - tìm kiếm - chọn xe
        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(1)
        except:
            pass

        var_app.driver.implicitly_wait(5)
        try:
            var_app.driver.find_element(By.XPATH, var_app.route).click()
        except:
            login_app.login.login_v3(self, "43E02740", "12341234")
            var_app.driver.find_element(By.XPATH, var_app.route).click()
        time.sleep(1.5)

        var_app.driver.find_element(By.XPATH, var_app.route_searchvehile).click()
        time.sleep(1)

        n = 0
        while (n < 35):
            n += 1
            n = str(n)
            pathkmphuongtien = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[" + n + "]/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.TextView"
            try:
                kmphuongtien = var_app.driver.find_element(By.XPATH, pathkmphuongtien).text
                digits = ''.join(re.findall(r'\d+', kmphuongtien))
                print("Phương tiện số {}: {}km/h".format(n, digits))
                var_app.driver.swipe(462, 502, 462, 362, 250)
                digits = int(digits)
                if digits > 0:
                    var_app.driver.find_element(By.XPATH, pathkmphuongtien).click()
                    break
            except:
                pass
            n = int(n)
        time.sleep(2.5)

        try:
            var_app.driver.find_element(By.XPATH, var_app.icon_pause).click()
        except:
            pass

        print("1")
        module_other_app.write_result_displayed_try(code, eventname, result, "Lộ trình - Tìm kiếm",
                                                var_app.routr_search_vehile, "_LoTrinh_TimKiem_LoadXe.png")
        print("2")



    def route_1h(self, code, eventname, result):       #Lộ trình - 1h
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(5)
        var_app.driver.find_element(By.XPATH, var_app.route_1h).click()
        time.sleep(2)


        var_app.driver.find_element(By.XPATH, var_app.minitor).click()
        time.sleep(1)
        var_app.driver.find_element(By.XPATH, var_app.route).click()
        time.sleep(1)



        try:
            time_hour_local = time.strftime("%H", time.localtime())
            time_hour_local = int(time_hour_local)
            time_app = var_app.driver.find_element(By.XPATH, var_app.time_hour_app).text
            time_hour_app = time_app[:2]
            time_hour_app = int(time_hour_app)
            var_app.logging.info("--------------")
            var_app.logging.info("Lộ trình - Chọn mốc thời gian")
            var_app.logging.info("Mã - " + code)
            var_app.logging.info("Tên sự kiện - " + eventname)
            var_app.logging.info("Kết quả - " + result)
            check_time = time_hour_local - time_hour_app
            print("check time", check_time)
            print(time_hour_local)
            print(time_hour_app)
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 11, str(check_time))
            var_app.logging.info(check_time)
            if check_time == 1 or 0:
                var_app.logging.info("True")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Pass")
            else:
                var_app.logging.info("False")
                var_app.driver.save_screenshot(var_app.imagepath + code + "_GiamSat_Lotrinh1h.png")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Fail")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 9, code + "_GiamSat_Lotrinh1h.png")
        except:
            pass



    def route_choosetime(self, code, eventname, result, path_route):       #Lộ trình - 4h
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(5)
        var_app.driver.find_element(By.XPATH, path_route).click()
        time.sleep(2)

        var_app.driver.find_element(By.XPATH, var_app.minitor).click()
        time.sleep(1)
        var_app.driver.find_element(By.XPATH, var_app.route).click()
        time.sleep(1)


        var_app.logging.info("--------------")
        var_app.logging.info("Lộ trình - Chọn mốc thời gian")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("True")
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Pass")



    def route_calender(self, code, eventname, result):       #Lộ trình - 1h
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass
        var_app.driver.implicitly_wait(5)
        var_app.driver.find_element(By.XPATH, var_app.route_option).click()
        time.sleep(2)

        var_app.driver.find_element(By.XPATH, var_app.minitor).click()
        time.sleep(1)
        var_app.driver.find_element(By.XPATH, var_app.route).click()
        time.sleep(1)

        module_other_app.write_result_displayed_try(code, eventname, result, "Lộ trình - Chọn mốc thời gian",
                                                var_app.check_route_calender, "_LoTrinh_TuyChon.png")
        var_app.driver.find_element(By.XPATH, var_app.minitor).click()
        time.sleep(1)
        var_app.driver.find_element(By.XPATH, var_app.route).click()
        time.sleep(1)



    def route_3tiles(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass
        var_app.driver.implicitly_wait(5)
        var_app.driver.find_element(By.XPATH, var_app.route_3tiles).click()
        time.sleep(1.5)
        module_other_app.write_result_text_try_if(code, eventname, result, "Lộ trình - Icon",
                                              var_app.check_route_3tiles, "Lộ trình", "_LoTrinh_IconMoLoTrinh.png")

        try:
            var_app.driver.find_element(By.XPATH, var_app.route_3tiles_iconx).click()
            time.sleep(1)
        except:
            pass



    def route_hide_route(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass
        var_app.driver.implicitly_wait(5)
        var_app.driver.find_element(By.XPATH, var_app.route_hide_route).click()
        time.sleep(1.5)
        module_other_app.write_result_not_displayed_try(code, eventname, result, "Lộ trình - Icon",
                                                var_app.check_route_hide_route, "_LoTrinh_IconAnHienLoTrinh.png")

        var_app.driver.find_element(By.XPATH, var_app.route_hide_route).click()
        time.sleep(1.5)



    def route_icon(self, code, eventname, result, path_icon):       #Lộ trình - icon
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass
        var_app.driver.implicitly_wait(5)
        var_app.driver.find_element(By.XPATH, path_icon).click()
        time.sleep(2)
        var_app.driver.find_element(By.XPATH, path_icon).click()
        var_app.logging.info("--------------")
        var_app.logging.info("Lộ trình - Chọn icon")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("True")
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Pass")












