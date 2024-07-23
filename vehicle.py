import time
from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import AppiumBy
import re
import login_app
import var_app
import module_other_app
from retry import retry







class overview:

    def search_vehicle(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(7)
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


    def arrange_vehicle(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(5)
        var_app.driver.find_element(By.XPATH, var_app.vehicle).click()
        time.sleep(1)

        vehicle1 = var_app.driver.find_element(By.XPATH, var_app.stt_vehicle1).text
        vehicle2 = var_app.driver.find_element(By.XPATH, var_app.stt_vehicle2).text
        vehicle1 = int(''.join(re.findall(r'\d+', vehicle1)))
        vehicle2 = int(''.join(re.findall(r'\d+', vehicle2)))

        var_app.driver.find_element(By.XPATH, var_app.icon_arrange_vehicle).click()
        time.sleep(1)
        var_app.driver.find_element(By.XPATH, var_app.arrange_vehicle).click()
        time.sleep(1)
        vehicle_latter1 = var_app.driver.find_element(By.XPATH, var_app.stt_vehicle1).text
        vehicle_latter2 = var_app.driver.find_element(By.XPATH, var_app.stt_vehicle2).text
        vehicle_latter1 = int(''.join(re.findall(r'\d+', vehicle_latter1)))
        vehicle_latter2 = int(''.join(re.findall(r'\d+', vehicle_latter2)))

        var_app.logging.info("--------------")
        var_app.logging.info("Phương tiện - Icon sắp xếp")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        if vehicle1 > vehicle2:
            if vehicle_latter2 > vehicle_latter1:
                var_app.logging.info("True")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Pass")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 11, "Sắp xếp tăng dần")
            else:
                var_app.logging.info("False")
                var_app.driver.save_screenshot(var_app.imagepath + code + "_Phuongtien_SapXepTheo_BienKiemSoat.png")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Fail")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 11, "Sắp xếp tăng dần")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 9, code + "_Phuongtien_SapXepTheo_BienKiemSoat.png")
        if  vehicle1 < vehicle2:
            if vehicle_latter2 < vehicle_latter1:
                var_app.logging.info("True")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Pass")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 11, "Sắp xếp giảm dần")
            else:
                var_app.logging.info("False")
                var_app.driver.save_screenshot(var_app.imagepath + code + "_Phuongtien_SapXepTheo_BienKiemSoat.png")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 11, "Sắp xếp giảm dần")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Fail")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 9, code + "_Phuongtien_SapXepTheo_BienKiemSoat.png")


    def arrange_time(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(5)
        var_app.driver.find_element(By.XPATH, var_app.vehicle).click()
        time.sleep(1)
        overview.status_vehicle(self, "Vehicle08", eventname, result,
                                        var_app.status_move1, var_app.name_move1, var_app.quaility_move1,
                                        "_PhuongTien_TrangThai_DiChuyen.png")


        time1 = var_app.driver.find_element(By.XPATH, var_app.stt_time1).text
        time2 = var_app.driver.find_element(By.XPATH, var_app.stt_time2).text
        time1 = time1[9::]
        time2 = time2[9::]

        time1 = int(''.join(re.findall(r'\d+', time1)))
        time2 = int(''.join(re.findall(r'\d+', time2)))
        print(time1)
        print(time2)

        var_app.driver.find_element(By.XPATH, var_app.icon_arrange_vehicle).click()
        time.sleep(1)
        var_app.driver.find_element(By.XPATH, var_app.arrange_time).click()
        time.sleep(1)
        time_latter1 = var_app.driver.find_element(By.XPATH, var_app.stt_time1).text
        time_latter2 = var_app.driver.find_element(By.XPATH, var_app.stt_time2).text
        print(time_latter1)
        print(time_latter2)
        time_latter1 = time_latter1[9::]
        time_latter2 = time_latter2[9::]

        time_latter1 = int(''.join(re.findall(r'\d+', time_latter1)))
        time_latter2 = int(''.join(re.findall(r'\d+', time_latter2)))
        print(time_latter1)
        print(time_latter2)

        var_app.logging.info("--------------")
        var_app.logging.info("Phương tiện - Icon sắp xếp")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        if time1 >= time2:
            if time_latter2 >= time_latter1:
                var_app.logging.info("True")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Pass")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 11, "Sắp xếp tăng dần")
            else:
                var_app.logging.info("False")
                var_app.driver.save_screenshot(var_app.imagepath + code + "_Phuongtien_SapXepTheo_ThoiGian.png")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Fail")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 11, "Sắp xếp tăng dần")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 9, code + "_Phuongtien_SapXepTheo_ThoiGian.png")
        if time1 < time2:
            if time_latter2 <= time_latter1:
                var_app.logging.info("True")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Pass")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 11, "Sắp xếp giảm dần")
            else:
                var_app.logging.info("False")
                var_app.driver.save_screenshot(var_app.imagepath + code + "_Phuongtien_SapXepTheo_ThoiGian.png")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 11, "Sắp xếp giảm dần")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Fail")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 9, code + "_Phuongtien_SapXepTheo_ThoiGian.png")


    def arrange_default(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(5)
        var_app.driver.find_element(By.XPATH, var_app.vehicle).click()
        time.sleep(1)

        var_app.driver.find_element(By.XPATH, var_app.icon_arrange_vehicle).click()
        time.sleep(1)
        var_app.driver.find_element(By.XPATH, var_app.arrange_default).click()
        time.sleep(1)
        var_app.logging.info("--------------")
        var_app.logging.info("Phương tiện - Icon sắp xếp")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("True")
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Pass")


    def status_vehicle(self, code, eventname, result, status_vehicle, name_status, quaility_vehicle, path_image):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass


        var_app.driver.implicitly_wait(5)
        try:
            var_app.driver.find_element(By.XPATH, var_app.vehicle).click()
            time.sleep(1)
            var_app.driver.find_element(By.XPATH, var_app.vehicle_status_icon1)
            time.sleep(1.5)
        except:
            login_app.login.check_logout(self)
            login_app.login.login_v3(self, "43E02740", "12341234")
            var_app.driver.find_element(By.XPATH, var_app.vehicle).click()
            time.sleep(1)
            var_app.driver.find_element(By.XPATH, var_app.vehicle_status_icon).click()
            time.sleep(1.5)

        var_app.driver.find_element(By.XPATH, var_app.vehicle_status_icon1).click()
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
            var_app.driver.find_element(By.XPATH, var_app.vehicle).click()
            time.sleep(1)
            var_app.driver.find_element(By.XPATH, var_app.vehicle_status_icon1).click()
            time.sleep(1.5)
            var_app.driver.find_element(By.XPATH, status_vehicle).click()
            time.sleep(1)
        time.sleep(2)
        if quaility_vehicle == 0:
            module_other_app.write_result_not_displayed_try(code, eventname, result, "Phương tiện - Trạng thái xe",
                                                    var_app.path_vehicle_status1, path_image)

        else:
            module_other_app.write_result_displayed_try(code, eventname, result, "Phương tiện - Trạng thái xe",
                                                    var_app.path_vehicle_status1, path_image)
        var_app.logging.info("trạng thái phương tiện {}, số lượng {}".format(name_status, quaility_vehicle))


    @retry(tries=3, delay=2, backoff=1, jitter=5, )
    def detailinfnfo_vehicle(self, code, eventname, result, info_vehicle, path_image):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(5)
            var_app.driver.find_element(By.XPATH, var_app.vehicle).click()
            time.sleep(1)
        except:
            pass

        var_app.driver.implicitly_wait(5)
        var_app.driver.find_element(By.XPATH, var_app.vehicle_status_icon1).click()
        time.sleep(1.5)
        var_app.driver.find_element(By.XPATH, var_app.status_move1).click()
        time.sleep(1.5)

        check_info = var_app.driver.find_element(By.XPATH, info_vehicle).text

        module_other_app.write_result_text_try_if_other(code, eventname, result, "Phương tiện - Thông tin xe",
                                              info_vehicle, None, path_image)

        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 11, check_info)









    def detail_custom(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(5)
        except:
            pass

        var_app.driver.implicitly_wait(5)
        var_app.driver.find_element(By.XPATH, var_app.vehicle).click()
        time.sleep(1)
        var_app.driver.find_element(By.XPATH, var_app.vehicle_status_icon1).click()
        time.sleep(1.5)
        var_app.driver.find_element(By.XPATH, var_app.status_total1).click()
        time.sleep(1)
        var_app.driver.find_element(By.XPATH, var_app.vehicle1).click()
        time.sleep(2)
        var_app.driver.find_element(By.XPATH, var_app.detail_custom).click()
        time.sleep(2)
        module_other_app.write_result_text_try_if(code, eventname, result, "Phương tiện - Trạng thái xe",
                                              var_app.check_detail_custom, "Thiết lập mục ưa thích", "_PhuongTien_TuyChon.png")


    def detail_custom_search(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(5)
        except:
            pass

        var_app.driver.implicitly_wait(5)
        tinhnang3 = var_app.driver.find_element(By.XPATH, var_app.detail_custom_search3).text
        var_app.driver.find_element(By.XPATH, var_app.detail_custom_search_input).send_keys(tinhnang3)
        time.sleep(1.5)
        module_other_app.write_result_text_try_if(code, eventname, result, "Phương tiện - Tùy chọn",
                                              var_app.check_detail_custom_search, tinhnang3, "_PhuongTien_TimKiem.png")

        var_app.driver.find_element(By.XPATH, var_app.detail_custom_search_input).clear()


    def detail_choose_max_favorites(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(5)
        except:
            pass


        try:
            var_app.driver.find_element(By.XPATH, var_app.detail_custom_search3)
        except:
            overview.detail_custom(self, "Vehicle25", eventname, result)


        setup_favorite1 = var_app.driver.find_element(By.XPATH, var_app.setup_favorite1).get_attribute("checked")
        print("checkbox: ", setup_favorite1)
        if setup_favorite1 == "false":
            var_app.driver.find_element(By.XPATH, var_app.setup_favorite1).click()

        setup_favorite2 = var_app.driver.find_element(By.XPATH, var_app.setup_favorite2).get_attribute("checked")
        print("checkbox: ", setup_favorite2)
        if setup_favorite2 == "false":
            var_app.driver.find_element(By.XPATH, var_app.setup_favorite2).click()

        setup_favorite3 = var_app.driver.find_element(By.XPATH, var_app.setup_favorite3).get_attribute("checked")
        print("checkbox: ", setup_favorite3)
        if setup_favorite3 == "false":
            var_app.driver.find_element(By.XPATH, var_app.setup_favorite3).click()

        setup_favorite4 = var_app.driver.find_element(By.XPATH, var_app.setup_favorite4).get_attribute("checked")
        print("checkbox: ", setup_favorite4)
        if setup_favorite4 == "false":
            var_app.driver.find_element(By.XPATH, var_app.setup_favorite4).click()

        module_other_app.write_result_text_try_if(code, eventname, result, "Phương tiện - Thiết lập mục ưu thích",
                                              var_app.check_detail_choose_max_favorites, "Bạn đã chọn số tiện ích tối đa. Vui lòng bỏ chọn một tiện ích trước", "_PhuongTien_ThietLapMucUaThich1.png")

        time.sleep(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.detail_favorites_iconx1).click()
            time.sleep(0.5)
            var_app.driver.find_element(By.XPATH, var_app.detail_favorites_iconx).click()
        except:
            time.sleep(5)
            var_app.driver.find_element(By.XPATH, var_app.detail_favorites_iconx).click()
        time.sleep(1)


    def detail_choose_min_favorites(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(5)
        except:
            pass

        try:
            var_app.driver.find_element(By.XPATH, var_app.detail_custom_search3)
        except:
            overview.detail_custom(self, "Vehicle25", eventname, result)

        setup_favorite1 = var_app.driver.find_element(By.XPATH, var_app.setup_favorite1).get_attribute("checked")
        print("checkbox: ", setup_favorite1)
        if setup_favorite1 == "false":
            var_app.driver.find_element(By.XPATH, var_app.setup_favorite1).click()

        time.sleep(1)
        var_app.driver.find_element(By.XPATH, var_app.setup_favorite_save).click()
        time.sleep(1.5)
        module_other_app.write_result_text_try_if(code, eventname, result, "Phương tiện - Thiết lập mục ưu thích",
                                              var_app.check_detail_choose_min_favorites, "Lưu mục ưa thích thành công", "_PhuongTien_ThietLapMucUaThich2.png")


        var_app.driver.find_element(By.XPATH, var_app.vehicle1).click()
        time.sleep(2)
        var_app.driver.find_element(By.XPATH, var_app.detail_custom).click()
        time.sleep(2)
        setup_favorite1 = var_app.driver.find_element(By.XPATH, var_app.setup_favorite1).get_attribute("checked")
        print("checkbox: ", setup_favorite1)
        if setup_favorite1 == "true":
            var_app.driver.find_element(By.XPATH, var_app.setup_favorite1).click()

        time.sleep(1)
        var_app.driver.find_element(By.XPATH, var_app.setup_favorite_save).click()
        time.sleep(1.5)










