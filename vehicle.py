import time
from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import AppiumBy
import re
import login_app
import var_app
import module_other_app
from retry import retry
import minitor_app






class overview:

    def search_vehicle(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(5)
        try:
            var_app.driver.find_element(By.XPATH, var_app.vehicle).click()
        except:
            login_app.login.login_v3(self, "43E02740", "12341234")
            var_app.driver.find_element(By.XPATH, var_app.vehicle).click()
        time.sleep(1.5)
        var_app.driver.find_element(By.XPATH, var_app.search_vehicle1).send_keys(var_app.data['vehicle']['search'])
        time.sleep(2)
        var_app.driver.tap([(150, 420)])
        time.sleep(2)

        module_other_app.write_result_text_try_if(code, eventname, result, "Phương tiện - Tìm kiếm",
                                              var_app.check_vehiicle_namevehicle1, var_app.data['vehicle']['search'], "_Phuongtien_TimKiemPhuongTien.png")

        try:
            var_app.driver.find_element(By.XPATH, var_app.search_vehicle1_iconx1).click()
        except:
            pass
        var_app.driver.find_element(By.XPATH, var_app.search_vehicle1).clear()
        time.sleep(1.5)


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

        try:
            var_app.driver.find_element(By.XPATH, var_app.vehicle_note).click()
        except:
            login_app.login.login_v3(self, "43E02740", "12341234")
            var_app.driver.find_element(By.XPATH, var_app.vehicle).click()
            var_app.driver.find_element(By.XPATH, var_app.vehicle_note).click()
        time.sleep(1.5)
        module_other_app.write_result_text_try_if(code, eventname, result, "Phương tiện - Chú thích",
                                              var_app.check_vehicle_note, "Chú thích", "_Phuongtien_ChuThich.png")

        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.vehicle_note_iconx).click()
            time.sleep(1)
        except:
            pass


    def select_group_search(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(5)
        var_app.driver.find_element(By.XPATH, var_app.vehicle).click()
        time.sleep(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.select_group).click()
        except:
            login_app.login.login_v3(self, "43E02740", "12341234")
            var_app.driver.find_element(By.XPATH, var_app.vehicle).click()
            var_app.driver.find_element(By.XPATH, var_app.select_group).click()
        time.sleep(2)
        var_app.driver.find_element(By.XPATH, var_app.select_group_input1).send_keys(var_app.data['vehicle']['search_group'])
        time.sleep(2)
        var_app.logging.info("--------------")
        var_app.logging.info("Phương tiện - Chọn nhóm")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("False")
        var_app.driver.save_screenshot(var_app.imagepath + code + "_PhuongTien_ChonNhom_TimKiem.png")
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Fail")
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 9, code + "_PhuongTien_ChonNhom_TimKiem.png")


    def select_group_select(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass
        try:
            var_app.driver.find_element(By.XPATH, var_app.select_group_checkbox1).click()
        except:
            overview.select_group_search(self, "Vehicle03", eventname, result)
            var_app.driver.find_element(By.XPATH, var_app.select_group_checkbox1).click()


        time.sleep(0.5)
        var_app.driver.find_element(By.XPATH, var_app.select_group_choose).click()
        time.sleep(4)
        module_other_app.write_result_displayed_try(code, eventname, result, "Phương tiện - Chọn nhóm",
                                                    var_app.check_select_group, "_PhuongTien_ChonNhom.png")
        var_app.driver.find_element(By.XPATH, var_app.select_group1).click()
        time.sleep(1.5)
        var_app.driver.find_element(By.XPATH, var_app.select_group_checkbox1).click()
        time.sleep(0.5)
        var_app.driver.find_element(By.XPATH, var_app.select_group_choose).click()
        time.sleep(3)
        var_app.driver.press_keycode(4)
        time.sleep(1)
        var_app.driver.press_keycode(4)
        time.sleep(2)
        var_app.driver.press_keycode(4)
        var_app.driver.press_keycode(4)








    def arrange_vehicle(self, code, eventname, result, type_arrange):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(5)
        try:
            var_app.driver.find_element(By.XPATH, var_app.vehicle).click()
        except:
            login_app.login.login_v3(self, "43E02740", "12341234")
            var_app.driver.find_element(By.XPATH, var_app.vehicle).click()
        time.sleep(1)


        var_app.driver.find_element(By.XPATH, var_app.icon_arrange_vehicle).click()
        time.sleep(1)
        var_app.driver.find_element(By.XPATH, type_arrange).click()
        time.sleep(1)

        var_app.logging.info("--------------")
        var_app.logging.info("Phương tiện - Icon sắp xếp")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("True")
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Pass")


    def arrange_time(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(5)
        try:
            var_app.driver.find_element(By.XPATH, var_app.vehicle).click()
        except:
            login_app.login.login_v3(self, "43E02740", "12341234")
            var_app.driver.find_element(By.XPATH, var_app.vehicle).click()
        time.sleep(1)

        var_app.driver.find_element(By.XPATH, var_app.icon_arrange_vehicle).click()
        time.sleep(1)
        var_app.driver.find_element(By.XPATH, var_app.arrange_time).click()
        time.sleep(1)
        var_app.logging.info("--------------")
        var_app.logging.info("Phương tiện - Icon sắp xếp")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("True")
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Pass")
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 11, "Sắp xếp tăng dần")


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


    def vehicle_status(self, code, eventname, result, status_name, x, y, path_image):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
        except:
            pass

        var_app.driver.implicitly_wait(5)
        try:
            var_app.driver.find_element(By.XPATH, var_app.vehicle_status_icon2).click()
        except:
            login_app.login.login_v3(self, "43E02740", "12341234")
            var_app.driver.find_element(By.XPATH, var_app.vehicle).click()
        time.sleep(1.5)

        var_app.driver.tap([(x, y)])
        time.sleep(2)
        if status_name == "Tất cả":
            module_other_app.write_result_displayed_try(code, eventname, result, "Giám sát - Trạng thái xe",
                                                    var_app.path_vehicle_status2, path_image)
        else:
            var_app.logging.info("--------------")
            var_app.logging.info("Phương tiện - Trạng thái xe")
            var_app.logging.info("Mã - " + code)
            var_app.logging.info("Tên sự kiện - " + eventname)
            var_app.logging.info("Kết quả - " + result)
            var_app.logging.info("True")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Pass")


    def detail_vehicle(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        module_other_app.clearData_luutamthoi(var_app.path_luutamthoi, "Sheet1", "", "", "")

        try:
            var_app.driver.find_element(By.XPATH, var_app.vehicle).click()
        except:
            login_app.login.login_v3(self, "43E02740", "12341234")
            var_app.driver.find_element(By.XPATH, var_app.vehicle).click()
        time.sleep(1)

        var_app.driver.tap([(130, 400)])
        time.sleep(1.5)
        var_app.driver.find_element(By.XPATH, var_app.vehicle_detail).click()
        time.sleep(2)

        #info vehicle
        minitor_app.status_general_information("Biển kiểm soát", 6)
        minitor_app.status_general_information("Thời gian", 7)
        minitor_app.status_general_information("Động cơ", 12)
        minitor_app.status_general_information("KM trong ngày", 10)
        minitor_app.status_general_information("Vận tốc", 8)
        minitor_app.status_general_information("Dừng đỗ", 11)
        minitor_app.status_general_information("Địa chỉ", 14)

        time.sleep(1)
        var_app.driver.swipe(400, 1350, 450, 400, 500)
        time.sleep(1)
        minitor_app.status_general_information1("Nhiệt độ", 17)
        var_app.logging.info("--------------")
        var_app.logging.info("Phương Tiện - Thông tin chi tiết xe")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("True")
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Pass")

        try:
            var_app.driver.find_element(By.XPATH, var_app.vehicle_detail_iconx).click()
        except:
            pass


    def check_detail_vehicle(self, code, eventname, result, rows, path_image):
        data_check = str(module_other_app.readData(var_app.path_luutamthoi, "Sheet1", rows, 3))
        var_app.logging.info("--------------")
        var_app.logging.info("Phương Tiện - Thông tin chi tiết xe")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        try:
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 11, data_check)
            var_app.logging.info(data_check)
            if data_check != "None":
                var_app.logging.info("True")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Pass")
            else:
                var_app.logging.info("False")
                var_app.driver.save_screenshot(var_app.imagepath + code + path_image)
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Fail")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 9, code + path_image)
        except:
            var_app.logging.info("False")
            var_app.driver.save_screenshot(var_app.imagepath + code + path_image)
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Fail")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 9, code + path_image)










    def detail_custom(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(5)
        except:
            pass

        var_app.driver.implicitly_wait(5)
        try:
            var_app.driver.find_element(By.XPATH, var_app.vehicle).click()
        except:
            login_app.login.login_v3(self, "43E02740", "12341234")
            var_app.driver.find_element(By.XPATH, var_app.vehicle).click()
        time.sleep(1)
        var_app.driver.tap([(130, 400)])
        time.sleep(1.5)
        var_app.driver.find_element(By.XPATH, var_app.detail_custom1).click()
        time.sleep(2)
        module_other_app.write_result_text_try_if(code, eventname, result, "Phương tiện - Trạng thái xe",
                                              var_app.check_detail_custom, "THIẾT LẬP MỤC ƯA THÍCH", "_PhuongTien_TuyChon.png")


    def detail_choose_min_favorites(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(5)
        except:
            pass

        try:
            var_app.driver.find_element(By.XPATH, var_app.detail_custom_search_input)
        except:
            overview.detail_custom(self, "Vehicle27", eventname, result)

        var_app.driver.find_element(By.XPATH, var_app.detail_custom_search_input).send_keys(var_app.data['vehicle']['search_custom'])
        time.sleep(1.5)
        var_app.driver.tap([(860, 333)])
        var_app.driver.find_element(By.XPATH, var_app.setup_favorite_save).click()
        time.sleep(1.5)
        module_other_app.write_result_text_try_if(code, eventname, result, "Phương tiện - Thiết lập mục ưu thích",
                                              var_app.check_detail_choose_min_favorites, "Lưu mục ưa thích thành công", "_PhuongTien_ThietLapMucUaThich2.png")



    def detail_custom_search(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(5)
        except:
            pass

        var_app.driver.implicitly_wait(5)
        var_app.driver.tap([(130, 400)])
        time.sleep(1.5)
        module_other_app.write_result_text_try_if(code, eventname, result, "Phương tiện - Tùy chọn",
                                              var_app.check_detail_custom_search, var_app.data['vehicle']['search_custom'], "_PhuongTien_TimKiem.png")

        var_app.driver.find_element(By.XPATH, var_app.detail_custom1).click()
        time.sleep(2)
        var_app.driver.tap([(860, 333)])
        var_app.driver.find_element(By.XPATH, var_app.setup_favorite_save).click()
        time.sleep(1.5)


    def detail_choose_max_favorites(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(5)
        except:
            pass


        try:
            var_app.driver.find_element(By.XPATH, var_app.vehicle).click()
        except:
            login_app.login.login_v3(self, "43E02740", "12341234")
            var_app.driver.find_element(By.XPATH, var_app.vehicle).click()
        time.sleep(1)
        var_app.driver.tap([(130, 400)])
        time.sleep(1.5)
        var_app.driver.find_element(By.XPATH, var_app.vehicle_detail).click()
        time.sleep(2)
        var_app.driver.find_element(By.XPATH, var_app.detail_custom1).click()
        time.sleep(2)

        var_app.driver.tap([(130, 400)])
        var_app.driver.tap([(130, 400)])
        var_app.driver.tap([(130, 400)])
        var_app.driver.tap([(130, 400)])



        module_other_app.write_result_text_try_if(code, eventname, result, "Phương tiện - Thiết lập mục ưu thích",
                                              var_app.check_detail_choose_max_favorites, "Bạn đã chọn số tiện ích tối đa. Vui lòng bỏ chọn một tiện ích trước", "_PhuongTien_ThietLapMucUaThich1.png")

        # time.sleep(1)
        # try:
        #     var_app.driver.find_element(By.XPATH, var_app.detail_favorites_iconx1).click()
        #     time.sleep(0.5)
        #     var_app.driver.find_element(By.XPATH, var_app.detail_favorites_iconx).click()
        # except:
        #     time.sleep(5)
        #     var_app.driver.find_element(By.XPATH, var_app.detail_favorites_iconx).click()
        # time.sleep(1)












