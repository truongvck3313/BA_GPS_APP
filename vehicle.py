import time
from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import AppiumBy
import re
import login_app
import var_app
import module_other_app
from retry import retry
import minitor_app




def get_status_vehicle(field_name):
    module_other_app.clearData_luutamthoi(var_app.path_luutamthoi, "Sheet1", "", "", "")

    var_app.driver.implicitly_wait(0.05)
    n = 0
    while (n < 16):
        n += 1
        n = str(n)
        path_status = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.FrameLayout[1]/androidx.viewpager.widget.ViewPager/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[" + n + "]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.widget.TextView"
        path_quantity = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.FrameLayout[1]/androidx.viewpager.widget.ViewPager/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[" + n + "]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.TextView"
        print(n)
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






def vehicle_back():
    var_app.driver.implicitly_wait(0.2)
    try:
        var_app.driver.find_element(By.XPATH, var_app.vehicle_back1).click()
        time.sleep(1.2)
    except:
        pass
    try:
        var_app.driver.find_element(By.XPATH, var_app.vehicle_back2).click()
        time.sleep(1.2)
    except:
        pass
    try:
        var_app.driver.find_element(By.XPATH, var_app.vehicle_back3).click()
        time.sleep(1.2)
    except:
        pass
    try:
        var_app.driver.find_element(By.XPATH, var_app.vehicle_back4).click()
        time.sleep(1.2)
    except:
        pass




class overview:

    def search_vehicle(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        login_app.login.login_v3(self, var_app.data['login']['conhom_quantri_tk'], var_app.data['login']['conhom_quantri_mk'])
        var_app.driver.find_element(By.XPATH, var_app.vehicle).click()
        time.sleep(0.5)
        var_app.driver.find_element(By.XPATH, var_app.vehicle).click()
        time.sleep(1.5)
        var_app.driver.find_element(By.XPATH, var_app.search_vehicle1).send_keys(var_app.data['vehicle']['search'])
        time.sleep(2)
        module_other_app.tap_scaled(var_app.driver, [(150, 330)])
        time.sleep(2)

        module_other_app.write_result_text_try_if(code, eventname, result, "Phương tiện - Tìm kiếm",
                                              var_app.check_vehiicle_namevehicle1, var_app.data['vehicle']['search'], "_Phuongtien_TimKiemPhuongTien.png")

        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.search_vehicle1_iconx1).click()
            time.sleep(1)
        except:
            pass

        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.search_vehicle1_iconx2).click()
            time.sleep(1)
        except:
            pass
        var_app.driver.find_element(By.XPATH, var_app.search_vehicle1).clear()
        time.sleep(1.5)


    def vehicle_note(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.find_element(By.XPATH, var_app.vehicle).click()
            time.sleep(0.5)
            var_app.driver.find_element(By.XPATH, var_app.vehicle).click()
            time.sleep(1.5)
            var_app.driver.find_element(By.XPATH, var_app.vehicle_note).click()
        except:
            login_app.login.login_v3(self, var_app.data['login']['conhom_quantri_tk'], var_app.data['login']['conhom_quantri_mk'])
            var_app.driver.find_element(By.XPATH, var_app.vehicle).click()
            time.sleep(0.5)
            var_app.driver.find_element(By.XPATH, var_app.vehicle).click()
            time.sleep(1.5)
            var_app.driver.find_element(By.XPATH, var_app.vehicle_note).click()
        time.sleep(1.5)
        module_other_app.write_result_text_try_if(code, eventname, result, "Phương tiện - Chú thích",
                                              var_app.check_vehicle_note, "Chú thích", "_Phuongtien_ChuThich.png")

        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.vehicle_note_iconx).click()
            time.sleep(1)
        except:
            pass


    def select_group_search(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        var_app.driver.find_element(By.XPATH, var_app.vehicle).click()
        time.sleep(0.5)
        var_app.driver.find_element(By.XPATH, var_app.vehicle).click()
        time.sleep(1.5)
        try:
            var_app.driver.find_element(By.XPATH, var_app.select_group).click()
        except:
            login_app.login.login_v3(self, var_app.data['login']['conhom_quantri_tk'], var_app.data['login']['conhom_quantri_mk'])
            var_app.driver.find_element(By.XPATH, var_app.vehicle).click()
            time.sleep(0.5)
            var_app.driver.find_element(By.XPATH, var_app.vehicle).click()
            time.sleep(1.5)
            var_app.driver.find_element(By.XPATH, var_app.select_group).click()
        time.sleep(2)
        var_app.driver.find_element(By.XPATH, var_app.select_group_input1).send_keys(var_app.data['vehicle']['search_group'])
        time.sleep(2)
        module_other_app.write_result_text_try_if_cut(code, eventname, result, "Quản trị - Danh sách xe",
                                              var_app.check_search_group1, 0, 3, var_app.data['vehicle']['search_group'], "_PhuongTien_ChonNhom_TimKiem.png")


        # module_other_app.write_result_displayed_try(code, eventname, result, "Phương tiện - Chọn nhóm",
        #                                         var_app.check_select_group_search, "_PhuongTien_ChonNhom_TimKiem.png")


    def select_group_select(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass
        try:
            var_app.driver.find_element(By.XPATH, var_app.select_group_checkbox2a).click()
        except:
            overview.select_group_search(self, "Vehicle03", eventname, result)
            var_app.driver.find_element(By.XPATH, var_app.select_group_checkbox2a).click()
        time.sleep(0.5)

        var_app.driver.find_element(By.XPATH, var_app.select_group_choose).click()
        time.sleep(3.5)

        # var_app.logging.info("--------------")
        # var_app.logging.info("Phương tiện - Chọn nhóm")
        # var_app.logging.info("Mã - " + code)
        # var_app.logging.info("Tên sự kiện - " + eventname)
        # var_app.logging.info("Kết quả - " + result)
        # try:
        #     check_text = var_app.driver.find_element(By.XPATH, var_app.check_select_group1).text
        #     module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, check_text)
        #     var_app.logging.info(check_text[-3::])
        #     if check_text[-3::] == "KPI":
        #         var_app.logging.info("True")
        #         module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Pass")
        #     else:
        #         var_app.logging.info("False")
        #         var_app.driver.save_screenshot(var_app.imagepath + code + "_PhuongTien_ChonNhom.png")
        #         module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Fail")
        #         module_other_app.writeData(var_app.checklistpath, "Checklist", code, 13, code + "_PhuongTien_ChonNhom.png")
        # except:
        #     var_app.logging.info("False")
        #     var_app.driver.save_screenshot(var_app.imagepath + code + "_PhuongTien_ChonNhom.png")
        #     module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Fail")
        #     module_other_app.writeData(var_app.checklistpath, "Checklist", code, 13, code + "_PhuongTien_ChonNhom.png")

        module_other_app.write_result_displayed_try(code, eventname, result, "Phương tiện - Chọn nhóm",
                                                    var_app.check_select_group, "_PhuongTien_ChonNhom.png")

        # var_app.driver.find_element(By.XPATH, var_app.select_group1).click()
        # time.sleep(1.5)
        # var_app.driver.find_element(By.XPATH, var_app.select_group_checkbox1).click()
        # time.sleep(0.5)
        # var_app.driver.find_element(By.XPATH, var_app.select_group_checkbox1).click()
        # time.sleep(0.5)
        # var_app.driver.find_element(By.XPATH, var_app.select_group_choose).click()
        # time.sleep(3)
        # var_app.driver.press_keycode(4)
        # time.sleep(1)
        # var_app.driver.press_keycode(4)
        # time.sleep(2)
        # var_app.driver.press_keycode(4)
        # var_app.driver.press_keycode(4)


    def arrange_vehicle(self, code, eventname, result, type_arrange):
        var_app.driver.implicitly_wait(1)
        login_app.login.login_v3(self, var_app.data['login']['conhom_quantri_tk'], var_app.data['login']['conhom_quantri_mk'])
        var_app.driver.find_element(By.XPATH, var_app.vehicle).click()
        time.sleep(0.5)
        var_app.driver.find_element(By.XPATH, var_app.vehicle).click()
        time.sleep(1.5)
        var_app.driver.find_element(By.XPATH, var_app.icon_arrange_vehicle).click()
        time.sleep(1.5)
        var_app.driver.find_element(By.XPATH, type_arrange).click()
        time.sleep(2)
        vehicle1 = var_app.driver.find_element(By.XPATH, var_app.arrange_vehicle1).text
        vehicle2 = var_app.driver.find_element(By.XPATH, var_app.arrange_vehicle2).text
        vehicle3 = var_app.driver.find_element(By.XPATH, var_app.arrange_vehicle3).text
        print(vehicle1)

        # time1 = var_app.driver.find_element(By.XPATH, var_app.arrange_time1).text
        # print(time1)

        vehicle1 = ''.join(re.findall(r'\d+', vehicle1))
        vehicle2 = ''.join(re.findall(r'\d+', vehicle2))
        vehicle3 = ''.join(re.findall(r'\d+', vehicle3))

        var_app.logging.info("--------------")
        var_app.logging.info("Phương tiện - Icon sắp xếp")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, "Phương tiện 1: {}\nPhương tiện 2: {}\nPhương tiện 3: {}".format(vehicle1, vehicle2, vehicle3))
        if int(vehicle1) > int(vehicle2) > int(vehicle3) or int(vehicle1) < int(vehicle2) < int(vehicle3):
            var_app.logging.info("True")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Pass")
        else:
            var_app.logging.info("False")
            var_app.driver.save_screenshot(var_app.imagepath + code + "_PhuongTien_IconXapXep_BienKiemSoat.png")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Fail")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 13, code + "_PhuongTien_IconXapXep_BienKiemSoat.png")


    def arrange_time(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.find_element(By.XPATH, var_app.arrange_time1)
        except:
            login_app.login.login_v3(self, var_app.data['login']['conhom_quantri_tk'], var_app.data['login']['conhom_quantri_mk'])
            var_app.driver.find_element(By.XPATH, var_app.vehicle).click()
            time.sleep(0.5)
            var_app.driver.find_element(By.XPATH, var_app.vehicle).click()
        time.sleep(1.5)

        var_app.driver.find_element(By.XPATH, var_app.icon_arrange_vehicle).click()
        time.sleep(1.5)
        var_app.driver.find_element(By.XPATH, var_app.arrange_time).click()
        time.sleep(2)
        time1 = var_app.driver.find_element(By.XPATH, var_app.arrange_time1).text
        time1_hour = int(time1[0:2])
        time1_minute = int(time1[3:5])
        time1_second = int(time1[6:8])
        time1_all = (time1_hour*3600) + (time1_minute*60) + time1_second

        time2 = var_app.driver.find_element(By.XPATH, var_app.arrange_time2).text
        time2_hour = int(time2[0:2])
        time2_minute = int(time2[3:5])
        time2_second = int(time2[6:8])
        time2_all = (time2_hour*3600) + (time2_minute*60) + time2_second

        time3 = var_app.driver.find_element(By.XPATH, var_app.arrange_time3).text
        time3_hour = int(time3[0:2])
        time3_minute = int(time3[3:5])
        time3_second = int(time3[6:8])
        time3_all = (time3_hour*3600) + (time3_minute*60) + time3_second


        var_app.logging.info("--------------")
        var_app.logging.info("Phương tiện - Icon sắp xếp")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("Giây xe 1: " + str(time1_all))
        var_app.logging.info("Giây xe 2: " + str(time2_all))
        var_app.logging.info("Giây xe 3: " + str(time3_all))
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, "Thời gian phương tiện 1: {}\nThời gian phương tiện 2: {}\nThời gian phương tiện 3: {}".format(time1, time2, time3))
        if int(time1_all) >= int(time2_all) >= int(time3_all) or int(time1_all) <= int(time3_all) <= int(time3_all):
            var_app.logging.info("True")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Pass")
        else:
            var_app.logging.info("False")
            var_app.driver.save_screenshot(var_app.imagepath + code + "_PhuongTien_IconXapXep_ThoiGian.png")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Fail")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 13, code + "_PhuongTien_IconXapXep_ThoiGian.png")


    def arrange_default(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.find_element(By.XPATH, var_app.vehicle).click()
            time.sleep(0.5)
            var_app.driver.find_element(By.XPATH, var_app.vehicle).click()
            time.sleep(1.5)
            var_app.driver.find_element(By.XPATH, var_app.icon_arrange_vehicle).click()
        except:
            login_app.login.login_v3(self, var_app.data['login']['conhom_quantri_tk'], var_app.data['login']['conhom_quantri_mk'])
            var_app.driver.find_element(By.XPATH, var_app.vehicle).click()
            time.sleep(0.5)
            var_app.driver.find_element(By.XPATH, var_app.vehicle).click()
            time.sleep(1.5)
            var_app.driver.find_element(By.XPATH, var_app.icon_arrange_vehicle).click()

        time.sleep(1.5)
        var_app.driver.find_element(By.XPATH, var_app.arrange_default).click()
        time.sleep(1.5)
        var_app.logging.info("--------------")
        var_app.logging.info("Phương tiện - Icon sắp xếp")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("True")
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Pass")







    def vehicle_status(self, code, eventname, result, status_name, path_image):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.find_element(By.XPATH, var_app.vehicle_status_icon2).click()
            time.sleep(1.5)
            var_app.driver.find_element(By.XPATH, var_app.status_all1)
        except:
            login_app.login.login_v3(self, var_app.data['login']['conhom_quantri_tk'], var_app.data['login']['conhom_quantri_mk'])
            var_app.driver.find_element(By.XPATH, var_app.vehicle).click()
            time.sleep(0.5)
            var_app.driver.find_element(By.XPATH, var_app.vehicle).click()
            time.sleep(1.5)
            var_app.driver.find_element(By.XPATH, var_app.vehicle_status_icon2).click()
            time.sleep(1.5)

        get_status_vehicle(status_name)

        try:
            quantity = int(module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 109, 2))
        except:
            module_other_app.writeData1(var_app.path_luutamthoi, "Sheet1", 109, 2, 0)
            time.sleep(1)

        quantity = int(module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 109, 2))


        if quantity == 0:
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, "{}: {} phương tiện".format(status_name, quantity))
            module_other_app.write_result_not_displayed_try(code, eventname, result, "Phương tiện - Trạng thái xe",
                                                    var_app.arrange_vehicle1, path_image)

        else:
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, "{}: {} phương tiện".format(status_name, quantity))
            module_other_app.write_result_displayed_try(code, eventname, result, "Phương tiện - Trạng thái xe",
                                                    var_app.arrange_vehicle1, path_image)


    def detail_vehicle(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        module_other_app.clearData_luutamthoi(var_app.path_luutamthoi, "Sheet1", "", "", "")
        login_app.login.login_v3(self, var_app.data['login']['hungvinh_tk'], var_app.data['login']['hungvinh_mk'])
        var_app.driver.find_element(By.XPATH, var_app.vehicle).click()
        time.sleep(0.5)
        var_app.driver.find_element(By.XPATH, var_app.vehicle).click()
        time.sleep(1.5)
        vehicle = var_app.driver.find_element(By.XPATH, var_app.vehicle_detail_vehicle).text
        time1 = var_app.driver.find_element(By.XPATH, var_app.vehicle_detail_time).text
        enginer = var_app.driver.find_element(By.XPATH, var_app.vehicle_detail_enginer).text
        km_in_day = var_app.driver.find_element(By.XPATH, var_app.vehicle_detail_km_in_day).text
        speed = var_app.driver.find_element(By.XPATH, var_app.vehicle_detail_speed).text
        stop = var_app.driver.find_element(By.XPATH, var_app.vehicle_detail_stop).text
        adress = var_app.driver.find_element(By.XPATH, var_app.vehicle_detail_adress).text
        temperature = var_app.driver.find_element(By.XPATH, var_app.vehicle_detail_temperature).text


        module_other_app.writeData1(var_app.path_luutamthoi, "Sheet1", 6, 2, vehicle)
        module_other_app.writeData1(var_app.path_luutamthoi, "Sheet1", 7, 2, time1)
        module_other_app.writeData1(var_app.path_luutamthoi, "Sheet1", 12, 2, enginer)
        module_other_app.writeData1(var_app.path_luutamthoi, "Sheet1", 10, 2, km_in_day)
        module_other_app.writeData1(var_app.path_luutamthoi, "Sheet1", 8, 2, speed)
        module_other_app.writeData1(var_app.path_luutamthoi, "Sheet1", 11, 2, stop)
        module_other_app.writeData1(var_app.path_luutamthoi, "Sheet1", 14, 2, adress)
        module_other_app.writeData1(var_app.path_luutamthoi, "Sheet1", 17, 2, temperature)


        time.sleep(1)
        module_other_app.tap_scaled(var_app.driver, [(130, 400)])
        time.sleep(1.5)
        try:
            var_app.driver.find_element(By.XPATH, var_app.vehicle_detail).click()
        except:
            module_other_app.swipe_percent(var_app.driver, 0.85, 0.8, 0.2, 0.8, 1000)
            var_app.driver.find_element(By.XPATH, var_app.vehicle_detail).click()
        time.sleep(2)

        #info vehicle
        minitor_app.status_general_information("Biển kiểm soát", 6)
        minitor_app.status_general_information("Thời gian", 7)
        minitor_app.status_general_information("Động cơ", 12)
        minitor_app.status_general_information("KM trong ngày", 10)
        minitor_app.status_general_information("Vận tốc", 8)
        minitor_app.status_general_information("Đang đỗ", 11)
        minitor_app.status_general_information("Địa chỉ", 14)

        time.sleep(1)
        module_other_app.swipe_scaled(var_app.driver, 400, 1350, 450, 400, 500)
        time.sleep(1)
        minitor_app.status_general_information1("Nhiệt độ", 17)
        var_app.logging.info("--------------")
        var_app.logging.info("Phương Tiện - Thông tin chi tiết xe")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("True")
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Pass")

        try:
            var_app.driver.find_element(By.XPATH, var_app.vehicle_detail_iconx).click()
        except:
            pass


    def check_detail_vehicle(self, code, eventname, result, rows, path_image, type_check):
        list = str(module_other_app.readData(var_app.path_luutamthoi, "Sheet1", rows, 2))
        detail = str(module_other_app.readData(var_app.path_luutamthoi, "Sheet1", rows, 3))
        var_app.logging.info("--------------")
        var_app.logging.info("Phương Tiện - Thông tin chi tiết xe")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, "Danh sách: {}\nChi tiết xe: {}".format(list, detail))
        if type_check == "0":
            var_app.logging.info(list)
            var_app.logging.info(detail)
            if list == detail:
                var_app.logging.info("True")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Pass")
            else:
                var_app.logging.info("False")
                var_app.driver.save_screenshot(var_app.imagepath + code + path_image)
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Fail")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 13, code + path_image)


        if type_check == "1":
            if detail == "None":
                detail = "0 phút"

            if list == detail:
                var_app.logging.info("True")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Pass")
            else:
                var_app.logging.info("False")
                var_app.driver.save_screenshot(var_app.imagepath + code + path_image)
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Fail")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 13, code + path_image)


        if type_check == "2":
            list = ''.join(re.findall(r'\d+', list))
            list = int(list[0:2])

            detail = ''.join(re.findall(r'\d+', detail))
            detail = int(detail[0:2])
            var_app.logging.info(list - 1)
            var_app.logging.info(list + 1)
            var_app.logging.info(list)
            var_app.logging.info(detail)
            if list - 1 == detail or list + 1 == detail or list == detail:
                var_app.logging.info("True")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Pass")
            else:
                var_app.logging.info("False")
                var_app.driver.save_screenshot(var_app.imagepath + code + path_image)
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Fail")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 13, code + path_image)


        if type_check == "3":
            list = ''.join(re.findall(r'\d+', list))
            list = int(list[0:4])

            detail = ''.join(re.findall(r'\d+', detail))
            detail = int(detail[0:4])
            var_app.logging.info(list)
            var_app.logging.info(detail)
            if list == detail:
                var_app.logging.info("True")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Pass")
            else:
                var_app.logging.info("False")
                var_app.driver.save_screenshot(var_app.imagepath + code + path_image)
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Fail")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 13, code + path_image)


    def detail_custom(self, code, eventname, result):
        module_other_app.reset_driver()
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.find_element(By.XPATH, var_app.vehicle).click()
            time.sleep(0.5)
            try:
                var_app.driver.find_element(By.XPATH, var_app.vehicle).click()
                time.sleep(1.5)
            except:
                pass
        except:
            login_app.login.login_v3(self, var_app.data['login']['conhom_quantri_tk'], var_app.data['login']['conhom_quantri_mk'])
            var_app.driver.find_element(By.XPATH, var_app.vehicle).click()
            time.sleep(0.5)
            try:
                var_app.driver.find_element(By.XPATH, var_app.vehicle).click()
                time.sleep(1.5)
            except:
                pass
            print("n4")
        module_other_app.tap_scaled(var_app.driver, [(130, 400)])
        time.sleep(1.5)
        try:
            var_app.driver.find_element(By.XPATH, var_app.detail_custom1).click()
        except:
            module_other_app.tap_scaled(var_app.driver, [(130, 400)])
            time.sleep(1.5)
            var_app.driver.find_element(By.XPATH, var_app.detail_custom1).click()
        time.sleep(2)
        print("n5")
        module_other_app.write_result_text_try_if(code, eventname, result, "Phương tiện - Trạng thái xe",
                                              var_app.check_detail_custom, "THIẾT LẬP MỤC ƯA THÍCH", "_PhuongTien_TuyChon.png")


    def detail_choose_min_favorites(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        try:
            print("n6")
            var_app.driver.find_element(By.XPATH, var_app.detail_custom_search_input)
            print("n7")
        except:
            overview.detail_custom(self, "Vehicle27", eventname, result)
            print("n8")

        var_app.driver.find_element(By.XPATH, var_app.detail_custom_search_input).send_keys(var_app.data['vehicle']['search_custom'])
        time.sleep(1.5)
        print("n9")
        try:
            var_app.driver.find_element(By.XPATH, var_app.checkbox_favorite2_full)
        except:
            var_app.driver.find_element(By.XPATH, var_app.checkbox_favorite1_full).click()
        time.sleep(1)
        print("n10")
        # module_other_app.tap_scaled(var_app.driver, [(860, 333)])
        var_app.driver.find_element(By.XPATH, var_app.setup_favorite_save).click()
        time.sleep(1.5)
        print("n11")
        module_other_app.write_result_text_try_if(code, eventname, result, "Phương tiện - Thiết lập mục ưu thích",
                                              var_app.check_detail_choose_min_favorites, "Lưu mục ưa thích thành công", "_PhuongTien_ThietLapMucUaThich2.png")
        time.sleep(3)



    def detail_custom_search(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass
        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.find_element(By.XPATH, var_app.detail_custom_search_input)
            print("n11.1")
        except:
            overview.detail_custom(self, "Vehicle27", eventname, result)

        print("n12")
        module_other_app.tap_scaled(var_app.driver, [(130, 400)])
        time.sleep(3)
        module_other_app.write_result_text_try_if(code, eventname, result, "Phương tiện - Tùy chọn",
                                              "//*[@text='"+var_app.data['vehicle']['search_custom']+"']", var_app.data['vehicle']['search_custom'], "_PhuongTien_TimKiem.png")
        print("n13")
        try:
            var_app.driver.find_element(By.XPATH, var_app.detail_custom1).click()
        except:
            pass
        time.sleep(2)

        var_app.driver.find_element(By.XPATH, var_app.detail_custom_search_input).clear()
        time.sleep(0.5)
        var_app.driver.find_element(By.XPATH, var_app.detail_custom_search_input).send_keys(var_app.data['vehicle']['search_custom'])
        time.sleep(1.5)
        print("n14")
        try:
            var_app.driver.find_element(By.XPATH, var_app.checkbox_favorite2_full).click()
            time.sleep(1)
        except:
            pass
        time.sleep(1)
        print("n15")
        # module_other_app.tap_scaled(var_app.driver, [(860, 333)])
        var_app.driver.find_element(By.XPATH, var_app.setup_favorite_save).click()
        time.sleep(2)
        print("n16")
        bo_luu_yeuthich = var_app.driver.find_element(By.XPATH, var_app.check_favorite_save).text
        print("n17")
        print(bo_luu_yeuthich)
        if bo_luu_yeuthich == "Vui lòng chọn ít nhất 1 mục ưa thích":
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, bo_luu_yeuthich)
            var_app.logging.info("False")
            var_app.driver.save_screenshot(var_app.imagepath + code + "_PhuongTien_BoLuuYeuThich.png")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Fail")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 13, code + "_PhuongTien_BoLuuYeuThich.png")


    def detail_choose_max_favorites(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass


        try:
            var_app.driver.find_element(By.XPATH, var_app.vehicle).click()
            time.sleep(0.5)
            var_app.driver.find_element(By.XPATH, var_app.vehicle).click()
            time.sleep(1.5)
        except:
            login_app.login.login_v3(self, var_app.data['login']['conhom_quantri_tk'], var_app.data['login']['conhom_quantri_mk'])
            var_app.driver.find_element(By.XPATH, var_app.vehicle).click()
            time.sleep(0.5)
            var_app.driver.find_element(By.XPATH, var_app.vehicle).click()
        time.sleep(1.5)
        module_other_app.tap_scaled(var_app.driver, [(130, 400)])
        time.sleep(1.5)
        var_app.driver.find_element(By.XPATH, var_app.vehicle_detail).click()
        time.sleep(2)
        var_app.driver.find_element(By.XPATH, var_app.detail_custom1).click()
        time.sleep(2)

        module_other_app.tap_scaled(var_app.driver, [(130, 400)])
        module_other_app.tap_scaled(var_app.driver, [(130, 400)])
        module_other_app.tap_scaled(var_app.driver, [(130, 400)])
        module_other_app.tap_scaled(var_app.driver, [(130, 400)])

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












