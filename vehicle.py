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

    def search_vehicle(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(5)
        var_app.driver.find_element(By.XPATH, var_app.vehicle).click()
        time.sleep(1.5)
        vehiicle_namevehicle2 = var_app.driver.find_element(By.XPATH, var_app.vehiicle_namevehicle2).text

        var_app.driver.find_element(By.XPATH, var_app.search_vehicle1).send_keys(vehiicle_namevehicle2)
        time.sleep(2)
        module_other_app.write_result_text_try_if(code, eventname, result, "Phương tiện - Tìm kiếm",
                                              var_app.check_vehiicle_namevehicle1, vehiicle_namevehicle2, "_Phuongtien_TimKiemPhuongTien.png")

        var_app.driver.find_element(By.XPATH, var_app.search_vehicle1).click()
        var_app.driver.find_element(By.XPATH, var_app.search_vehicle1).clear()
        time.sleep(1)



    def vehicle_note(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(5)
        var_app.driver.find_element(By.XPATH, var_app.vehicle).click()
        time.sleep(1)
        var_app.driver.find_element(By.XPATH, var_app.vehicle_note).click()
        time.sleep(1.5)
        module_other_app.write_result_text_try_if(code, eventname, result, "Phương tiện - Chú thích",
                                              var_app.check_vehicle_note, "Chú thích", "_Phuongtien_ChuThich.png")

        try:
            var_app.driver.find_element(By.XPATH, var_app.vehicle_note_iconx).click()
        except:
            pass



    def select_group(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(5)
        var_app.driver.find_element(By.XPATH, var_app.vehicle).click()
        time.sleep(1)
        var_app.driver.find_element(By.XPATH, var_app.select_group).click()
        time.sleep(2)
        n = 0
        while (n < 14):
            n += 1
            n = str(n)
            pathphuongtien = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[" + n + "]/android.view.ViewGroup/android.widget.TextView"
            try:
                sophuongtien = var_app.driver.find_element(By.XPATH, pathphuongtien).text
                print(sophuongtien)
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 11, sophuongtien)
                sophuongtien = sophuongtien[-3::]
                sophuongtien = ''.join(re.findall(r'\d+', sophuongtien))
                sophuongtien = int(sophuongtien)
                print(sophuongtien)
                if sophuongtien > 0:
                    var_app.driver.find_element(By.XPATH, pathphuongtien).click()
                    time.sleep(1)
                    var_app.driver.find_element(By.XPATH, var_app.select_group_choose).click()
                    time.sleep(2)
                    module_other_app.write_result_displayed_try(code, eventname, result, "Phương tiện - Chọn nhóm",
                                                                var_app.check_select_group, "_PhuongTien_ChonNhom.png")

                    var_app.driver.find_element(By.XPATH, var_app.select_group).click()
                    time.sleep(2)
                    var_app.driver.find_element(By.XPATH, pathphuongtien).click()
                    time.sleep(1)
                    var_app.driver.find_element(By.XPATH, var_app.select_group_choose).click()
                    time.sleep(2)
                    break
            except:
                pass
            n = int(n)
        time.sleep(2)






