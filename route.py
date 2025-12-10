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











def route_back():
    var_app.driver.implicitly_wait(0.2)
    try:
        var_app.driver.find_element(By.XPATH, var_app.route_back1).click()
        time.sleep(1.2)
    except:
        pass
    try:
        var_app.driver.find_element(By.XPATH, var_app.route_back2).click()
        time.sleep(1.2)
    except:
        pass



class overview:


    def move_route(self):
        var_app.driver.implicitly_wait(2)
        n = 0
        while (n < 10):
            n = n + 1
            try:
                var_app.driver.find_element(By.XPATH, var_app.route).click()
                time.sleep(2)
                var_app.driver.find_element(By.XPATH, var_app.route_searchvehile)
                break
            except:
                pass
            time.sleep(1)

    def search_vehile(self, code, eventname, result):       #Lộ trình - tìm kiếm - chọn xe
        var_app.driver.implicitly_wait(2)
        login_app.login.login_v3(self, var_app.data['login']['conhom_quantri_tk'], var_app.data['login']['conhom_quantri_mk'])
        overview.move_route(self)

        var_app.driver.find_element(By.XPATH, var_app.route_searchvehile).click()

        time.sleep(1.5)
        var_app.driver.find_element(By.XPATH, var_app.route_searchvehile_input).send_keys(var_app.data['route']['search'])
        time.sleep(2)
        try:
            var_app.driver.find_element(By.XPATH, var_app.route_searchvehile1).click()
        except:
            module_other_app.tap_scaled(var_app.driver, [(200, 350)])
        time.sleep(4)
        try:
            var_app.driver.find_element(By.XPATH, var_app.route_icon_stop).click()
            time.sleep(1)
        except:
            pass
        # module_other_app.tap_scaled(var_app.driver, [(47, 1442)])
        # time.sleep(0.5)
        module_other_app.write_result_text_try_if_conten_other(code, eventname, result, "Lộ trình - Tìm kiếm",
                                                var_app.routr_search_vehile, "", "_LoTrinh_TimKiem_LoadXe.png")


    def route_1h(self, code, eventname, result):       #Lộ trình - 1h
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.find_element(By.XPATH, var_app.route_1h).click()
        except:
            login_app.login.login_v3(self, var_app.data['login']['conhom_quantri_tk'], var_app.data['login']['conhom_quantri_mk'])
            overview.move_route(self)
            var_app.driver.find_element(By.XPATH, var_app.route_1h).click()
        time.sleep(2)
        try:
            var_app.driver.find_element(By.XPATH, var_app.route_icon_stop).click()
            time.sleep(1)
        except:
            pass
        # try:
        #     module_other_app.tap_scaled(var_app.driver, [(47, 1442)])
        # except:
        #     module_other_app.tap_scaled(var_app.driver, [(44, 1444)])
        time.sleep(1)
        module_other_app.write_result_text_try_if_not_fail_other(code, eventname, result, "Lộ trình - Chọn mốc thời gian",
                                              var_app.check_route_km, "", "_GiamSat_Lotrinh1h.png")





    def route_choosetime(self, code, eventname, result, path_route, path_image):       #Lộ trình - 4h
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass
        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.find_element(By.XPATH, path_route).click()
        except:
            overview.move_route(self)
            var_app.driver.find_element(By.XPATH, path_route).click()
        time.sleep(3.5)
        try:
            var_app.driver.find_element(By.XPATH, var_app.route_icon_stop).click()
            time.sleep(1)
        except:
            pass
        # module_other_app.tap_scaled(var_app.driver, [(47, 1442)])
        # time.sleep(0.5)
        module_other_app.write_result_text_try_if_not_fail_other(code, eventname, result, "Lộ trình - Chọn mốc thời gian",
                                              var_app.check_route_km, "", path_image)


    def route_calender(self, code, eventname, result):       #Lộ trình - 1h
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass
        var_app.driver.implicitly_wait(2)

        try:
            var_app.driver.find_element(By.XPATH, var_app.route_option).click()
        except:
            login_app.login.login_v3(self, var_app.data['login']['conhom_quantri_tk'], var_app.data['login']['conhom_quantri_mk'])
            overview.move_route(self)
            var_app.driver.find_element(By.XPATH, var_app.route_option).click()
        time.sleep(2)

        module_other_app.write_result_displayed_try(code, eventname, result, "Lộ trình - Chọn mốc thời gian",
                                                var_app.check_route_calender, "_LoTrinh_TuyChon.png")
        var_app.driver.find_element(By.XPATH, var_app.minitor).click()
        time.sleep(1)
        var_app.driver.find_element(By.XPATH, var_app.route).click()
        time.sleep(1)


    def route_3tiles(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass
        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.find_element(By.XPATH, var_app.route_3tiles).click()
        except:
            overview.search_vehile(self, "", "", "")
            var_app.driver.find_element(By.XPATH, var_app.route_3tiles).click()
        time.sleep(2)

        module_other_app.write_result_text_try_if(code, eventname, result, "Lộ trình - Icon)",
                                              var_app.check_route_3tiles, "DANH SÁCH LỘ TRÌNH", "_LoTrinh_IconMoLoTrinh.png")

        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.route_3tiles_iconx).click()
            time.sleep(1)
        except:
            pass


    def route_hide_route(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass
        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.find_element(By.XPATH, var_app.route_hide_route).click()
        except:
            login_app.login.login_v3(self, var_app.data['login']['conhom_quantri_tk'], var_app.data['login']['conhom_quantri_mk'])
            overview.move_route(self)
            var_app.driver.find_element(By.XPATH, var_app.route_hide_route).click()
        time.sleep(2)

        module_other_app.write_result_not_displayed_try(code, eventname, result, "Lộ trình - Icon",
                                                var_app.check_route_hide_route, "_LoTrinh_IconAnHienLoTrinh.png")

        var_app.driver.find_element(By.XPATH, var_app.route_hide_route).click()
        time.sleep(1.5)


    def route_icon(self, code, eventname, result, path_icon):       #Lộ trình - icon
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass
        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.find_element(By.XPATH, path_icon).click()
        except:
            login_app.login.login_v3(self, var_app.data['login']['conhom_quantri_tk'], var_app.data['login']['conhom_quantri_mk'])
            overview.move_route(self)
            var_app.driver.find_element(By.XPATH, path_icon).click()
        time.sleep(2)

        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.ALLOW).click()
            time.sleep(1.5)
        except:
            pass

        var_app.driver.find_element(By.XPATH, path_icon).click()
        var_app.logging.info("--------------")
        var_app.logging.info("Lộ trình - Chọn icon")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("True")
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Pass")



    def route_icon_map(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass
        var_app.driver.implicitly_wait(2)
        var_app.driver.find_element(By.XPATH, var_app.icon_map).click()
        time.sleep(2.5)
        var_app.logging.info("--------------")
        var_app.logging.info("Lộ trình - Icon thay đổi map")
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
        var_app.driver.find_element(By.XPATH, var_app.SKIP).click()
        time.sleep(2)









