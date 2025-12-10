import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import report_app
import var_app
import module_other_app
import homepage_app
import minitor_app
import login_app
import random
import re
from datetime import datetime







wait = WebDriverWait(var_app.driver, 10)


def move_module1(self, code, eventname, result, link, startX, startY, endX, endY, duration,
                path_module, path_check, desire, path_image):
    var_app.driver.implicitly_wait(2)
    login_app.login.login_v3(self, var_app.data['login']['khongnhom_quantri_tk'], var_app.data['login']['khongnhom_quantri_mk'])
    try:
        var_app.driver.find_element(By.XPATH, var_app.homepage).click()
        time.sleep(2)
    except:
        login_app.other_function.delete_nofitication(self)

    try:
        var_app.driver.find_element(By.XPATH, var_app.homepage).click()
    except:
        pass
    time.sleep(1.5)

    try:#check xem chức năng tiện ích 1 có hiện ở trang chủ không
        var_app.driver.find_element(By.XPATH, var_app.utilities1)
    except:
        module_other_app.swipe_percent(var_app.driver, 0.5, 0.8, 0.5, 0.7, 1000)


    var_app.driver.implicitly_wait(1)
    minitor_app.scroll_and_click_precent(startX, startY, endX, endY, duration, link)

    time.sleep(3.5)
    module_other_app.write_result_text_try_if(code, eventname, result, path_module,
                                              path_check, desire, path_image)


def move_module2(self, code, eventname, result, link, startX, startY, endX, endY, duration,
                path_module, path_check, desire, path_image, user, password):
    var_app.driver.implicitly_wait(1)

    login_app.login.login_v3(self, user, password)
    var_app.driver.find_element(By.XPATH, var_app.homepage).click()
    time.sleep(2)
    try:
        var_app.driver.find_element(By.XPATH, var_app.homepage).click()
    except:
        pass
    time.sleep(1.5)
    try:#check xem chức năng tiện ích 1 có hiện ở trang chủ không
        var_app.driver.find_element(By.XPATH, var_app.utilities1)
    except:
        module_other_app.swipe_percent(var_app.driver, 0.5, 0.8, 0.5, 0.7, 1000)

    minitor_app.scroll_and_click_precent(startX, startY, endX, endY, duration, link)


    wait = WebDriverWait(var_app.driver, 15)
    try:
        element = wait.until(EC.element_to_be_clickable((By.XPATH, path_check)))
        time.sleep(1)
    except:
        pass
    module_other_app.write_result_text_try_if(code, eventname, result, path_module,
                                              path_check, desire, path_image)




class general:

    def utilities_back(self):
        var_app.driver.implicitly_wait(0.15)
        try:
            var_app.driver.find_element(By.XPATH, var_app.utilities_back1).click()
            time.sleep(1.3)
        except:
            pass
        try:
            var_app.driver.find_element(By.XPATH, var_app.utilities_back2).click()
            time.sleep(1.3)
        except:
            pass
        try:
            var_app.driver.find_element(By.XPATH, var_app.utilities_back3).click()
            time.sleep(1.3)
        except:
            pass
        try:
            var_app.driver.find_element(By.XPATH, var_app.utilities_back4).click()
            time.sleep(1.3)
        except:
            pass

        try:
            var_app.driver.find_element(By.XPATH, var_app.utilities_back5).click()
            time.sleep(1.3)
        except:
            pass
        try:
            var_app.driver.find_element(By.XPATH, var_app.utilities_back6).click()
            time.sleep(1.3)
        except:
            pass
        try:
            var_app.driver.find_element(By.XPATH, var_app.utilities_back7).click()
            time.sleep(1.3)
        except:
            pass
        try:
            var_app.driver.find_element(By.XPATH, var_app.utilities_back8).click()
            time.sleep(1.3)
        except:
            pass
        try:
            var_app.driver.find_element(By.XPATH, var_app.CANCEL).click()
            time.sleep(1.3)
        except :
            pass
        try:
            var_app.driver.find_element(By.XPATH, var_app.warn_passengers_detail_vehicle_back).click()
            time.sleep(1.3)
        except :
            pass



class utilities:


    def hide_and_show_the_car_filter(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.check_hide_and_show_the_car)
        except:
            move_module1(self, "", "", "", var_app.hide_and_show_the_car, 0.8, 0.85, 0.2, 0.85, 1000, "", "", "", "")

        var_app.driver.find_element(By.XPATH, var_app.hide_and_show_the_car_filter).click()
        time.sleep(2)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Ẩn hiện xe",
                                              var_app.SUPPORT_CUSTOMER, "BỘ LỌC TÌM KIẾM", "_TrangChu_AnHienXe_Loc.png")

        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.APPLY).click()
            time.sleep(1.5)
        except:
            pass


    def hide_and_show_the_car_excel(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.check_hide_and_show_the_car)
        except:
            move_module1(self, "", "", "", var_app.hide_and_show_the_car, 0.8, 0.85, 0.2, 0.85, 1000, "", "", "", "")

        var_app.driver.find_element(By.XPATH, var_app.hide_and_show_the_car_excel).click()
        time.sleep(2)
        report_app.general.back_excel(self, 4, var_app.check_hide_and_show_the_car)

        module_other_app.write_result_not_displayed_try(code, eventname, result, "Trang chủ - Ẩn hiện xe",
                                              var_app.check_export_excel, "_TrangChu_AnHienXe_XuatExcel.png")


    def hide_and_show_the_car_search(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.check_hide_and_show_the_car)
        except:
            move_module1(self, "", "", "", var_app.hide_and_show_the_car, 0.8, 0.85, 0.2, 0.85, 1000, "", "", "", "")

        # try:
        #     var_app.driver.find_element(By.XPATH, var_app.hide_and_show_the_car_select_vehicle).click()
        # except:
        #     var_app.driver.find_element(By.XPATH, var_app.hide_and_show_the_car_select_vehicle1).click()
        # time.sleep(2)
        # var_app.driver.find_element(By.XPATH, var_app.hide_and_show_the_car_select_vehicle_input).send_keys(var_app.data['utilities']['hide_show_vihicle_search'])
        # time.sleep(1.5)
        # module_other_app.tap_scaled(var_app.driver, [(350, 350)])
        # time.sleep(3)
        # module_other_app.swipe_scaled(var_app.driver, 720, 500, 150, 500, 500)
        # module_other_app.tap_scaled(var_app.driver, [(820, 500)])
        # time.sleep(1)
        # try:
        #     var_app.driver.implicitly_wait(0.3)
        #     var_app.driver.find_element(By.XPATH, var_app.CANCEL_HIDE).click()
        #     time.sleep(2)
        # except:
        #     pass
        #
        # try:
        #     var_app.driver.implicitly_wait(0.3)
        #     var_app.driver.find_element(By.XPATH, var_app.select_vehilce_hide_iconx).click()
        #     time.sleep(1)
        # except:
        #     pass
        #
        # try:
        #     var_app.driver.implicitly_wait(0.3)
        #     var_app.driver.find_element(By.XPATH, var_app.IGREE).click()
        #     time.sleep(1.5)
        # except:
        #     pass
        time.sleep(1.2)
        try:
            var_app.driver.find_element(By.XPATH, var_app.hide_and_show_the_car_select_vehicle).click()
        except:
            var_app.driver.find_element(By.XPATH, var_app.hide_and_show_the_car_select_vehicle1).click()
        time.sleep(2)
        try:
            var_app.driver.find_element(By.XPATH, var_app.hide_and_show_the_car_select_vehicle_input).send_keys(var_app.data['utilities']['hide_show_vihicle_search'])
        except:
            var_app.driver.find_element(By.XPATH, var_app.hide_and_show_the_car_select_vehicle).click()
            time.sleep(2)
            var_app.driver.find_element(By.XPATH, var_app.hide_and_show_the_car_select_vehicle_input).send_keys(var_app.data['utilities']['hide_show_vihicle_search'])
        time.sleep(1.5)
        module_other_app.tap_scaled(var_app.driver, [(350, 350)])
        time.sleep(3)
        # module_other_app.tap_scaled(var_app.driver, [(90, 500)])
        # time.sleep(2.5)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Ẩn hiện xe",
                                              var_app.check_hide_and_show_the_car_search, var_app.data['utilities']['hide_show_vihicle_search'], "_TrangChu_AnHienXe_TimKiem.png")

        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.select_vehilce_hide_iconx1).click()
            time.sleep(1.3)
        except:
            pass


    def hide_and_show_the_car_checkbox(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.check_hide_and_show_the_car)
        except:
            move_module1(self, "", "", "", var_app.hide_and_show_the_car, 0.8, 0.85, 0.2, 0.85, 1000, "", "", "", "")


        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.check_hide_and_show_the_car_checkbox2b)
        except:
            try:
                var_app.driver.find_element(By.XPATH, var_app.check_hide_and_show_the_car_checkbox1b).click()
            except:
                pass

        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.check_hide_and_show_the_car_checkbox2a)
        except:
            try:
                var_app.driver.find_element(By.XPATH, var_app.check_hide_and_show_the_car_checkbox1a).click()
            except:
                pass

        module_other_app.write_result_displayed_try(code, eventname, result, "Trang chủ - Ẩn hiện xe",
                                              var_app.check_hide_and_show_the_car_checkbox2, "_TrangChu_AnHienXe_Tat/BatThongBaoXe.png")

        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.check_hide_and_show_the_car_checkbox2b)
        except:
            try:
                var_app.driver.find_element(By.XPATH, var_app.check_hide_and_show_the_car_checkbox1b).click()
            except:
                pass

        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.check_hide_and_show_the_car_checkbox2a)
        except:
            try:
                var_app.driver.find_element(By.XPATH, var_app.check_hide_and_show_the_car_checkbox1a).click()
            except:
                pass


    def hide_and_show_the_car_icon_hide(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.check_hide_and_show_the_car)
        except:
            move_module1(self, "", "", "", var_app.hide_and_show_the_car, 0.8, 0.85, 0.2, 0.85, 1000, "", "", "", "")

        try:
            var_app.driver.find_element(By.XPATH, var_app.hide_and_show_the_car_icon_hide).click()
        except:
            var_app.driver.find_element(By.XPATH, var_app.hide_and_show_the_car_icon_hide1).click()
        time.sleep(2)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Ẩn hiện xe",
                                              var_app.check_hide_and_show_the_car_icon_hide, "CHỌN PHƯƠNG TIỆN ẨN", "_TrangChu_AnHienXe_IconAnXe.png")


    def hide_and_show_the_car_hide_vehicle(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.check_hide_and_show_the_car_icon_hide)
        except:
            utilities.hide_and_show_the_car_icon_hide(self, "", "", "")

        try:
            var_app.driver.find_element(By.XPATH, var_app.hide_vehicle_input).send_keys(var_app.data['utilities']['select_hide_vehicle'])
        except:
            var_app.driver.find_element(By.XPATH, var_app.hide_vehicle_input1).send_keys(var_app.data['utilities']['select_hide_vehicle'])
        time.sleep(1)
        module_other_app.tap_scaled(var_app.driver, [(38, 492)])
        time.sleep(0.5)
        var_app.driver.find_element(By.XPATH, var_app.APPLY).click()
        time.sleep(3)

        try:
            var_app.driver.find_element(By.XPATH, var_app.select_vehilce_hide_bca).click()
        except:
            var_app.driver.find_element(By.XPATH, var_app.select_vehilce_hide_bca1).click()
        time.sleep(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.select_vehilce_hide_select_reason).click()
        except:
            var_app.driver.find_element(By.XPATH, var_app.select_vehilce_hide_select_reason1).click()
        time.sleep(2)
        module_other_app.tap_scaled(var_app.driver, [(150, 450)])
        time.sleep(1.5)
        try:
            var_app.driver.find_element(By.XPATH, var_app.select_vehilce_hide_note).send_keys(var_app.data['utilities']['select_hide_note'])
        except:
            var_app.driver.find_element(By.XPATH, var_app.select_vehilce_hide_note1).send_keys(var_app.data['utilities']['select_hide_note'])
        time.sleep(0.5)
        var_app.driver.find_element(By.XPATH, var_app.SAVE).click()
        time.sleep(1)
        var_app.driver.find_element(By.XPATH, var_app.IGREE).click()

        wait = WebDriverWait(var_app.driver, 20)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, var_app.check_hide_and_show_the_car_hide_vehicle)))
        time.sleep(0.5)

        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Ẩn hiện xe",
                                              var_app.check_hide_and_show_the_car_hide_vehicle, "Ẩn phương tiện thành công", "_TrangChu_AnHienXe_AnXe.png")


    def hide_and_show_the_car_un_hide_vehicle(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.check_hide_and_show_the_car)
        except:
            move_module1(self, "", "", "", var_app.hide_and_show_the_car, 0.8, 0.85, 0.2, 0.85, 1000, "", "", "", "")


        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.hide_and_show_the_car_select_vehicle).click()
        except:
            var_app.driver.find_element(By.XPATH, var_app.hide_and_show_the_car_select_vehicle1).click()
        time.sleep(2)

        try:
            var_app.driver.find_element(By.XPATH, var_app.hide_and_show_the_car_select_vehicle_input).send_keys(var_app.data['utilities']['select_hide_vehicle'])
        except:
            var_app.driver.find_element(By.XPATH, var_app.hide_and_show_the_car_select_vehicle_input1).send_keys(var_app.data['utilities']['select_hide_vehicle'])
        time.sleep(1.5)
        module_other_app.tap_scaled(var_app.driver, [(350, 350)])
        time.sleep(3)


        module_other_app.swipe_scaled(var_app.driver, 720, 500, 150, 500, 500)


        var_app.driver.find_element(By.XPATH, var_app.data2_column6).click()#icon x
        time.sleep(1)
        var_app.driver.find_element(By.XPATH, var_app.CANCEL_HIDE).click()
        time.sleep(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.IGREE).click()
            time.sleep(1.5)
        except:
            pass
        try:
            wait = WebDriverWait(var_app.driver, 10)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_app.check_hide_and_show_the_car_un_hide_vehicle)))
        except:
            pass
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Ẩn hiện xe", var_app.check_hide_and_show_the_car_un_hide_vehicle,
                                                  "Bỏ ẩn phương tiện thành công", "_TrangChu_AnHienXe_BoAnXe.png")








    def add_driver_fill_info(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        random_number = str(random.randint(100000, 999999))
        random_number1 = str(random.randint(10000000, 99999999))
        print(random_number)

        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.check_add_driver)
        except:
            move_module1(self, "", "", "", var_app.add_driver, 0.8, 0.85, 0.2, 0.85, 1000, "", "", "", "")

        var_app.driver.find_element(By.XPATH, var_app.driver_info_driver_code).send_keys(random_number1)
        var_app.driver.find_element(By.XPATH, var_app.driver_info_lastname_and_fristname).send_keys(var_app.data['utilities']['fill_vehicle_name'] + random_number)
        var_app.driver.find_element(By.XPATH, var_app.driver_info_number_liscense).send_keys(var_app.data['utilities']['fill_vehicle_number_liscense'] + random_number)
        var_app.driver.find_element(By.XPATH, var_app.driver_info_type_liscense).click()
        time.sleep(1.5)
        module_other_app.tap_scaled(var_app.driver, [(131, 366)])
        time.sleep(1.5)
        var_app.driver.find_element(By.XPATH, var_app.driver_info_release_date).click() #ngày cấp
        time.sleep(1.5)
        var_app.driver.find_element(By.XPATH, var_app.IGREE).click()
        time.sleep(1.5)
        var_app.driver.find_element(By.XPATH, var_app.driver_info_expiration_date).click()  #ngày hết hạn
        time.sleep(1.5)
        var_app.driver.find_element(By.XPATH, var_app.IGREE).click()
        time.sleep(1.5)
        var_app.driver.find_element(By.XPATH, var_app.place_of_issue).send_keys(var_app.data['utilities']['place_of_issue']) #Nơi cấp
        time.sleep(0.5)

        var_app.driver.find_element(By.XPATH, var_app.employee_type).click()  #Loại nhân viên
        time.sleep(1.5)
        module_other_app.tap_scaled(var_app.driver, [(52, 306)])
        time.sleep(1.5)

        module_other_app.swipe_percent(var_app.driver, 0.5, 0.8, 0.5, 0.2, 1000)
        time.sleep(1)
        var_app.driver.find_element(By.XPATH, var_app.driver_info_date_of_birth).click()    #ngày sinh

        time.sleep(1.5)
        var_app.driver.find_element(By.XPATH, var_app.IGREE).click()
        time.sleep(1.5)

        try:
            var_app.driver.find_element(By.XPATH, var_app.driver_info_sex).click()
        except:
            var_app.driver.find_element(By.XPATH, var_app.driver_info_sex1).click()
        time.sleep(1.5)
        module_other_app.tap_scaled(var_app.driver, [(57, 364)])
        time.sleep(1.5)

        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.driver_info_number_cccd).send_keys(var_app.data['utilities']['fill_vehicle_cccd']  + random_number)
        except:
            var_app.driver.find_element(By.XPATH, var_app.driver_info_number_cccd1).send_keys(var_app.data['utilities']['fill_vehicle_cccd']  + random_number)

        try:
            var_app.driver.find_element(By.XPATH, var_app.driver_info_number_phone).send_keys(var_app.data['utilities']['fill_vehicle_phone'] + random_number)
        except:
            var_app.driver.find_element(By.XPATH, var_app.driver_info_number_phone1).send_keys(var_app.data['utilities']['fill_vehicle_phone'] + random_number)

        try:
            var_app.driver.find_element(By.XPATH, var_app.driver_info_adress).send_keys(var_app.data['utilities']['fill_vehicle_address'])
        except:
            var_app.driver.find_element(By.XPATH, var_app.driver_info_adress1).send_keys(var_app.data['utilities']['fill_vehicle_address'])

        # try:
        #     var_app.driver.find_element(By.XPATH, var_app.driver_info_assign_vehicle).click()
        # except:
        #     var_app.driver.find_element(By.XPATH, var_app.driver_info_assign_vehicle1).click()
        # time.sleep(1.5)
        # module_other_app.tap_scaled(var_app.driver, [(125, 358)])
        # time.sleep(1.5)
        var_app.driver.find_element(By.XPATH, var_app.driver_info_i_commit).click()
        time.sleep(1)
        var_app.driver.find_element(By.XPATH, var_app.SAVE).click()
        time.sleep(2)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Thêm lái xe",
                                              var_app.check_add_driver_fill_info, "Thêm lái xe thành công", "_TrangChu_ThemLaiXe_Luu.png")










    def list_driver_search(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.check_list_driver)
        except:
            move_module1(self, "", "", "", var_app.list_driver, 0.8, 0.85, 0.2, 0.85, 1000, "", "", "", "")

        var_app.driver.find_element(By.XPATH, var_app.list_driver_search_input).send_keys(var_app.data['utilities']['list_driver_search'])
        time.sleep(3)

        var_app.driver.find_element(By.XPATH, var_app.list_driver_name).click()
        time.sleep(2)
        try:
            wait = WebDriverWait(var_app.driver, 10)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_app.check_list_driver_search)))
        except:
            pass

        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Danh sách lái xe", var_app.check_list_driver_search,
                                                      var_app.data['utilities']['list_driver_search'], "_TrangChu_DanhSachLaiXe_TimKiem.png")

        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.see_info_vehicle_back).click()
            time.sleep(1.3)
        except:
            pass


    def list_driver_select_vehicle(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.check_list_driver)
        except:
            move_module1(self, "", "", "", var_app.list_driver, 0.8, 0.85, 0.2, 0.85, 1000, "", "", "", "")

        var_app.driver.find_element(By.XPATH, var_app.list_driver_name).click()
        time.sleep(3)


        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Danh sách lái xe",
                                              var_app.check_add_driver, "THÔNG TIN LÁI XE", "_TrangChu_DanhSachLaiXe_CickVaoXe.png")


    def list_driver_check_info(self, code, eventname, result, path_detail, desire, path_image):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.check_add_driver)
        except:
            utilities.list_driver_select_vehicle(self, "", "", "")
        try:
            var_app.driver.find_element(By.XPATH, path_detail)
        except:
            module_other_app.swipe_percent(var_app.driver, 0.5, 0.8, 0.5, 0.25, 1000)

        module_other_app.write_result_text_try_if_other(code, eventname, result, "Trang chủ - Danh sách lái xe",
                                              path_detail, desire, path_image)


        if path_image == "_TrangChu_DanhSachPhuongTien_SoDienThoai":
            try:
                var_app.driver.implicitly_wait(0.3)
                var_app.driver.find_element(By.XPATH, var_app.see_info_vehicle_back).click()
                time.sleep(1.3)
            except:
                pass


    def list_driver_icon_add(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            try:
                var_app.driver.find_element(By.XPATH, var_app.list_driver_icon_add).click()
            except:
                var_app.driver.find_element(By.XPATH, var_app.list_driver_icon_add1).click()
        except:
            move_module1(self, "", "", "", var_app.list_driver, 0.8, 0.85, 0.2, 0.85, 1000, "", "", "", "")
            try:
                var_app.driver.find_element(By.XPATH, var_app.list_driver_icon_add).click()
            except:
                var_app.driver.find_element(By.XPATH, var_app.list_driver_icon_add1).click()

        time.sleep(3)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Ẩn hiện xe",
                                              var_app.check_add_driver, "THÔNG TIN LÁI XE", "_TrangChu_DanhSachLaiXe_IconThemLaiXe.png")









    def info_fee_vehicle_owes_fees(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.check_info_fee)
        except:
            move_module1(self, "", "", "", var_app.info_fee, 0.8, 0.85, 0.2, 0.85, 1000, "", "", "", "")

        var_app.driver.find_element(By.XPATH, var_app.info_fee_vehicle_owes_fees).click()
        time.sleep(0.5)
        module_other_app.write_result_text_try_if_other(code, eventname, result, "Trang chủ - Thông tin phí",
                                              var_app.check_info_fee_vehicle_owes_fees, "", "_TrangChu_ThongTinPhi_PhuongTienNoPhi.png")


    def info_fee_search_fee(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.check_info_fee)
        except:
            move_module1(self, "", "", "", var_app.info_fee, 0.8, 0.85, 0.2, 0.85, 1000, "", "", "", "")

        var_app.driver.find_element(By.XPATH, var_app.info_fee_search_fee).click()
        time.sleep(1)

        var_app.driver.find_element(By.XPATH, var_app.info_fee_search_fee_input).send_keys("12Z100438")
        time.sleep(1)

        var_app.driver.find_element(By.XPATH, var_app.info_fee_search_fee_input).clear()
        time.sleep(1)
        var_app.driver.find_element(By.XPATH, var_app.info_fee_search_fee_input).send_keys("15F00083_C")
        time.sleep(1)

        module_other_app.write_result_text_try_if_other(code, eventname, result, "Trang chủ - Thông tin phí",
                                              var_app.check_info_fee_search_fee, "", "_TrangChu_ThongTinPhi_TraCuuPhi.png")


    def info_fee_iconbagps(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.check_info_fee)
        except:
            move_module1(self, "", "", "", var_app.info_fee, 0.8, 0.85, 0.2, 0.85, 1000, "", "", "", "")

        var_app.driver.find_element(By.XPATH, var_app.info_fee_iconbagps).click()
        time.sleep(1)

        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Thông tin phí",
                                              var_app.check_info_fee_iconbagps, "BA GPS", "_TrangChu_ThongTinPhi_IconGps.png")

        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.IGREE).click()
            time.sleep(1.3)
        except:
            pass








    def support_customer_tab(self, code, eventname, result, button, path_check, desire, name_image):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.check_support_customer)
        except:
            move_module1(self, "", "", "", var_app.support_customer, 0.8, 0.85, 0.2, 0.85, 1000, "", "", "", "")

        # module_other_app.swipe_scaled(var_app.driver, 400, 1400, 400, 700, 500)
        var_app.driver.find_element(By.XPATH, button).click()
        time.sleep(2)

        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Hỗ trợ khách hàng",
                                              path_check, desire, name_image)


    def support_customer_track_feedback(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.check_support_customer)
        except:
            move_module1(self, "", "", "", var_app.support_customer, 0.8, 0.85, 0.2, 0.85, 1000, "", "", "", "")

        var_app.driver.find_element(By.XPATH, var_app.support_customer_track_feedback).click()
        time.sleep(1)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Hỗ trợ khách hàng",
                                              var_app.search_feeback, "Tìm kiếm phản hồi", "_TrangChu_HoTroKhachHang_TheoDoiPhanHoi.png")








    def transmission_report_search(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.check_transmission_report)
        except:
            move_module1(self, "", "", "", var_app.transmission_report, 0.8, 0.85, 0.2, 0.85, 1000, "", "", "", "")

        var_app.driver.find_element(By.XPATH, var_app.transmission_report_search_input).send_keys(var_app.data['utilities']['transmission_warning_search'])
        time.sleep(1.5)
        module_other_app.tap_scaled(var_app.driver, [(858, 492)])
        time.sleep(2)
        module_other_app.write_result_text_try_if_other(code, eventname, result, "Trang chủ - Cảnh báo tích truyền",
                                              var_app.check_transmission_report_search, "", "_TrangChu_CanhBaoTichTruyen_TimKiem.png")

        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.transmission_report_search_back).click()
            time.sleep(1.3)
        except:
            pass


    def transmission_report_select_vehicle(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.check_transmission_report)
        except:
            move_module1(self, "", "", "", var_app.transmission_report, 0.8, 0.85, 0.2, 0.85, 1000, "", "", "", "")

        module_other_app.tap_scaled(var_app.driver, [(858, 492)])
        time.sleep(2)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Cảnh báo tích truyền",
                                              var_app.check_transmission_report_select_vehicle, "NHẬP THÔNG TIN XE", "_TrangChu_CanhBaoTichTruyen_ClickVaoXe.png")

        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.transmission_report_search_back).click()
            time.sleep(1.3)
        except:
            pass


    def transmission_report_checkbox(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.check_transmission_report)
        except:
            move_module1(self, "", "", "", var_app.transmission_report, 0.8, 0.85, 0.2, 0.85, 1000, "", "", "", "")

        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.transmission_report_checkbox).click()
        except:
            pass

        try:
            var_app.driver.find_element(By.XPATH, var_app.transmission_report_checkbox).click()
        except:
            pass
        time.sleep(2)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Cảnh báo tích truyền",
                                              var_app.check_transmission_report_checkbox, "Bạn đã tắt nhận cảnh báo. Bạn có thể xem lại trong menu tiện ích Cảnh báo tích truyền", "_TrangChu_CanhBaoTichTruyen_Checkbox.png")

        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.IGREE).click()
            time.sleep(1.3)
        except:
            pass










    def record_driver_card_fill_info(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.check_record_driver_card)
        except:
            move_module1(self, "", "", "", var_app.record_driver_card, 0.8, 0.85, 0.2, 0.85, 1000, "", "", "", "")

        var_app.driver.find_element(By.XPATH, var_app.record_driver_card_fill_info_vehicle).click()
        time.sleep(1.5)
        module_other_app.tap_scaled(var_app.driver, [(185, 365)])
        time.sleep(1.5)
        var_app.driver.find_element(By.XPATH, var_app.record_driver_card_fill_info_name_driver).click()
        time.sleep(1.5)
        module_other_app.tap_scaled(var_app.driver, [(135, 303)])
        time.sleep(2)
        var_app.driver.find_element(By.XPATH, var_app.record_driver_card_fill_info).click()
        time.sleep(1)
        var_app.driver.find_element(By.XPATH, var_app.record_driver_card_fill_info).click()

        wait = WebDriverWait(var_app.driver, 30)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, var_app.check_record_driver_card_fill_info)))
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Ghi thẻ lái xe",
                                              var_app.check_record_driver_card_fill_info, "Thiết bị không online", "_TrangChu_GhiTheLaiXe_GhiThe.png")


    def record_driver_card_help(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.check_record_driver_card)
        except:
            move_module1(self, "", "", "", var_app.record_driver_card, 0.8, 0.85, 0.2, 0.85, 1000, "", "", "", "")

        var_app.driver.find_element(By.XPATH, var_app.record_driver_card_help).click()
        time.sleep(1.5)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Ghi thẻ lái xe",
                                              var_app.check_record_driver_card_help, "1. Đối với đầu đọc thẻ BARD: Đưa thẻ lại gần tem mặt trước của đầu đọc thẻ",
                                                  "_TrangChu_GhiTheLaiXe_HuongDan.png")


    def record_driver_card_icon(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.check_record_driver_card)
        except:
            move_module1(self, "", "", "", var_app.record_driver_card, 0.8, 0.85, 0.2, 0.85, 1000, "", "", "", "")

        try:
            var_app.driver.find_element(By.XPATH, var_app.record_driver_card_icon).click()
        except:
            var_app.driver.find_element(By.XPATH, var_app.record_driver_card_icon1).click()
        time.sleep(1)
        wait = WebDriverWait(var_app.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, var_app.day_record_driver_card)))

        var_app.logging.info("--------------")
        var_app.logging.info("Trang chủ - Ghi thẻ lái xe")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        try:
            day_record_driver_card = var_app.driver.find_element(By.XPATH, var_app.day_record_driver_card).text
            vehicle_record_driver_card = var_app.driver.find_element(By.XPATH, var_app.vehicle_record_driver_card).text
            gplx_record_driver_card = var_app.driver.find_element(By.XPATH, var_app.gplx_record_driver_card).text
            name_record_driver_card = var_app.driver.find_element(By.XPATH, var_app.name_record_driver_card).text

            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, "Ngày giờ: {}\nPhương tiện: {}\nGPLX: {}\nTên lái xe: {}"
                                       .format(day_record_driver_card, vehicle_record_driver_card, gplx_record_driver_card, name_record_driver_card))
            if day_record_driver_card and vehicle_record_driver_card and gplx_record_driver_card and name_record_driver_card != "None":
                var_app.logging.info("True")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Pass")
            else:
                var_app.logging.info("False")
                var_app.driver.save_screenshot(var_app.imagepath + code + "_TrangChu_GhiTheLaiXe_IconLichSuGhiThe.png")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Fail")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 13, code + "_TrangChu_GhiTheLaiXe_IconLichSuGhiThe.png")
        except:
            var_app.logging.info("True")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Pass")











    def record_driver_card_write_nfc(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.manager)
        except:
            move_module1(self, "", "", "", var_app.record_driver_card_nfc, 0.8, 0.85, 0.2, 0.85, 1000, "", "", "", "")

        var_app.driver.find_element(By.XPATH, var_app.manager).click()
        time.sleep(2)

        var_app.driver.find_element(By.XPATH, var_app.record_driver_card_name_drive).click()
        time.sleep(1.5)
        module_other_app.tap_scaled(var_app.driver, [(120, 310)])
        time.sleep(1.5)
        var_app.driver.find_element(By.XPATH, var_app.record_driver_card_checkbox)
        var_app.driver.find_element(By.XPATH, var_app.record_driver_card_liscense_plate)

        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Ghi thẻ lái xe NFC",
                                              var_app.WRITE_CARD_NFC, "GHI THẺ NFC", "_TrangChu_GhiTheLaiXe_GhiTheNFC.png")


    def record_driver_card_read_nfc(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.manager)
        except:
            move_module1(self, "", "", "", var_app.record_driver_card_nfc, 0.8, 0.85, 0.2, 0.85, 1000, "", "", "", "")

        var_app.driver.find_element(By.XPATH, var_app.manager).click()
        time.sleep(2)
        var_app.driver.find_element(By.XPATH, var_app.record_driver_card_checkbox).click()
        time.sleep(2)
        var_app.driver.find_element(By.XPATH, var_app.record_driver_card_name_drive_input).send_keys("Nguyễn Ngọc Sơn")
        time.sleep(0.5)
        var_app.driver.find_element(By.XPATH, var_app.record_driver_card_liscense_plate_input).send_keys("791193379520")
        time.sleep(0.5)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Ghi thẻ lái xe NFC",
                                              var_app.READ_CARD_NFC, "ĐỌC THẺ NFC", "_TrangChu_GhiTheLaiXe_DocTheNFC.png")


    def record_driver_card_nfc_help(self, code, eventname, result, path_icon1, path_icon2, path_check, desire, name_image):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.manager)
        except:
            move_module1(self, "", "", "", var_app.record_driver_card_nfc, 0.8, 0.85, 0.2, 0.85, 1000, "", "", "", "")

        var_app.driver.find_element(By.XPATH, var_app.help).click()
        time.sleep(2)
        var_app.driver.find_element(By.XPATH, path_icon1).click()
        time.sleep(2)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Ghi thẻ lái xe NFC",
                                              path_check, desire, name_image)

        var_app.driver.find_element(By.XPATH, path_icon2).click()
        time.sleep(2)


    def record_driver_card_icon_history(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.manager)
        except:
            move_module1(self, "", "", "", var_app.record_driver_card_nfc, 0.8, 0.85, 0.2, 0.85, 1000, "", "", "", "")

        var_app.driver.find_element(By.XPATH, var_app.help).click()
        time.sleep(2)
        var_app.driver.find_element(By.XPATH, var_app.record_driver_card_icon_history).click()
        time.sleep(2)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Ghi thẻ lái xe NFC",
                                              var_app.HISTORY_WRITE_CARD, "LỊCH SỬ GHI THẺ", "_TrangChu_GhiTheLaiXeNFC_IconLichSu.png")

        var_app.driver.find_element(By.XPATH, var_app.HISTORY_WRITE_CARD_back).click()
        time.sleep(2)













    def remote_control(self, code, eventname, result):
        # login_app.login.login_v3(self, var_app.data['login']['binhanh_tk'], var_app.data['login']['binhanh_mk'])

        move_module2(self, code, eventname, result, var_app.remote_control, 0.8, 0.85, 0.2, 0.85, 1000,
                               "Trang chủ - Điều khuyển thiết bị từ xa", var_app.check_remote_control,
                               "ĐIỀU KHIẾN THIẾT BỊ TỪ XA", "_TrangChu_DieuKhuyenThietBiTuXa.png", var_app.data['login']['binhanh_tk'], var_app.data['login']['binhanh_mk'])



    def fee_management(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)

        move_module2(self, code, eventname, result, var_app.fee_management, 0.8, 0.85, 0.2, 0.85, 1000,
                               "Trang chủ - Quản lý chi phí xe", var_app.check_fee_management,
                               "QUẢN LÝ CHI PHÍ XE", "_TrangChu_QyanLyChiPhiXe.png", var_app.data['login']['binhanh_tk'], var_app.data['login']['binhanh_mk'])



    def shipping_order(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        # login_app.login.login_v3(self, var_app.data['login']['binhanh_tk'], var_app.data['login']['binhanh_mk'])

        move_module2(self, code, eventname, result, var_app.shipping_order, 0.8, 0.85, 0.2, 0.85, 1000,
                               "Trang chủ - Lệnh vận chuyển", var_app.check_shipping_order,
                               "LỆNH VẬN CHUYỂN", "_TrangChu_LenhVanChuyen.png", var_app.data['login']['binhanh_tk'], var_app.data['login']['binhanh_mk'])



    def take_photos_of_delivery(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        move_module2(self, code, eventname, result, var_app.take_photos_of_delivery, 0.8, 0.85, 0.2, 0.85, 1000,
                               "Trang chủ - Chụp ảnh giao hàng", var_app.check_take_photos_of_delivery,
                               "CHỤP ẢNH GIAO HÀNG", "_TrangChu_ChupAnhGiaoHang.png", var_app.data['login']['binhanh_tk'], var_app.data['login']['binhanh_mk'])



    def warn_passengers_see_detail(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.check_warn_passengers)
        except:
            move_module1(self, "", eventname, result, var_app.warn_passengers, 0.8, 0.85, 0.2, 0.85, 1000,
                         "", "",  "", "")

        module_other_app.tap_scaled(var_app.driver, [(350, 420)])
        time.sleep(2)
        var_app.logging.info("--------------")
        var_app.logging.info("Trang chủ - Cảnh báo hành khách")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        try:
            var_app.driver.find_element(By.XPATH, var_app.handle)
            try:
                check_text = var_app.driver.find_element(By.XPATH, var_app.check_warn_passengers_see_detail).text
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, check_text)
                var_app.logging.info(check_text)
                if check_text == "CHI TIẾT CẢNH BÁO":
                    var_app.logging.info("True")
                    module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Pass")
                else:
                    var_app.logging.info("False")
                    var_app.driver.save_screenshot(var_app.imagepath + code + "_TrangChu_CanhBaoHanhKhach_ClickVaoCanhBao.png")
                    module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Fail")
                    module_other_app.writeData(var_app.checklistpath, "Checklist", code, 13, code + "_TrangChu_CanhBaoHanhKhach_ClickVaoCanhBao.png")
            except:
                var_app.logging.info("True")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Pass")
        except:
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, "Không có cảnh báo")


    def warn_passengers_detail(self, code, eventname, result, path_check, desire, path_image):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.check_warn_passengers_see_detail)
        except:
            utilities.warn_passengers_see_detail(self, "", "", "")

        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.check_warn_passengers_see_detail)
            module_other_app.write_result_text_try_if_other(code, eventname, result, "Trang chủ - Cảnh báo hành khách",
                                                  path_check, desire, path_image)
        except:
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, "Không có cảnh báo hôm nay")


    def warn_passengers_detail_vehicle(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.check_warn_passengers_see_detail)
        except:
            utilities.warn_passengers_see_detail(self, "", "", "")

        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.check_warn_passengers_see_detail)
            var_app.logging.info("--------------")
            var_app.logging.info("Trang chủ - Cảnh báo hành khách")
            var_app.logging.info("Mã - " + code)
            var_app.logging.info("Tên sự kiện - " + eventname)
            var_app.logging.info("Kết quả - " + result)
            try:
                check_text = var_app.driver.find_element(By.XPATH, var_app.warn_passengers_detail_vehicle).get_attribute("content-desc")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, check_text)
                var_app.logging.info(check_text)
                if check_text != "":
                    var_app.logging.info("True")
                    module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Pass")
                else:
                    var_app.logging.info("False")
                    var_app.driver.save_screenshot(var_app.imagepath + code + "_TrangChu_CanhBaoHanhKhach_ClickVaoCanhBao_BienSo.png")
                    module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Fail")
                    module_other_app.writeData(var_app.checklistpath, "Checklist", code, 13, code + "_TrangChu_CanhBaoHanhKhach_ClickVaoCanhBao_BienSo.png")
            except:
                var_app.logging.info("True")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Pass")
        except:
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, "Không có cảnh báo hôm nay")


    def warn_passengers_handle(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.check_warn_passengers_see_detail)
        except:
            utilities.warn_passengers_see_detail(self, "", "", "")

        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.check_warn_passengers_see_detail)
            var_app.driver.find_element(By.XPATH, var_app.handle).click()
            time.sleep(2)
            module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Cảnh báo hành khách",
                                                  var_app.check_warn_passengers_handle, "XỬ LÝ CẢNH BÁO", "_TrangChu_CanhBaoHanhKhach_XuLyCanhBao.png")
            time.sleep(1)
            var_app.driver.find_element(By.XPATH, var_app.CANCEL).click()
            time.sleep(1.5)
            var_app.driver.find_element(By.XPATH, var_app.warn_passengers_detail_vehicle_back).click()
            time.sleep(2)
        except:
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, "Không có cảnh báo hôm nay")


    def warn_passengers_see_all(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.check_warn_passengers)
        except:
            move_module1(self, "", eventname, result, var_app.warn_passengers, 0.8, 0.85, 0.2, 0.85, 1000,
                         "", var_app.check_warn_passengers,  "", "")


        var_app.driver.find_element(By.XPATH, var_app.warn_passengers_see_all).click()
        time.sleep(1.5)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Cảnh báo hành khách",
                                              var_app.check_warn_passengers_see_all, "Bạn chắc chắn muốn chuyển tất cả cảnh báo thành đã đọc?",
                                                  "_TrangChu_CanhBaoHanhKhach_IconDocTatCaCanhBao.png")

        var_app.driver.find_element(By.XPATH, var_app.IGREE).click()
        time.sleep(2)
        general.utilities_back(self)












    def transmission_business(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.check_transmission_bca)
            var_app.driver.find_element(By.XPATH, var_app.busines).click()
        except:
            move_module1(self, "", eventname, result, var_app.transmission_bca, 0.8, 0.85, 0.2, 0.85, 1000, "", "", "", "")
            var_app.driver.find_element(By.XPATH, var_app.busines).click()
        time.sleep(2)

        var_app.logging.info("--------------")
        var_app.logging.info("Trang chủ - Truyền dữ liệu BCA - Doanh nghiệp")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)

        try:


            busines_company = var_app.driver.find_element(By.XPATH, var_app.busines_company).text
            busines_tax_code = var_app.driver.find_element(By.XPATH, var_app.busines_tax_code).text
            busines_phone_number = var_app.driver.find_element(By.XPATH, var_app.busines_phone_number).text
            busines_department_gtvt = var_app.driver.find_element(By.XPATH, var_app.busines_department_gtvt).text
            busines_address = var_app.driver.find_element(By.XPATH, var_app.busines_address).text

            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, "{}\n{}\n{}\n{}\n{}"
                                       .format(busines_company, busines_tax_code, busines_phone_number, busines_department_gtvt, busines_address))
            if (busines_company != "") and (busines_tax_code[0:11] == "Mã số thuế:") and (busines_phone_number[0:14] == "Số điện thoại:") and (busines_department_gtvt[0:8] == "Sở GTVT:") and (busines_address[0:8] == "Địa chỉ:"):
                var_app.logging.info("True")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Pass")
            else:
                var_app.logging.info("False")
                var_app.driver.save_screenshot(var_app.imagepath + code + "_TruyenDuLieuBCA_DoanhNghiep_CheckThongTin.png")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Fail")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 13, code + "_TruyenDuLieuBCA_DoanhNghiep_CheckThongTin.png")
        except:
            var_app.logging.info("False")
            var_app.driver.save_screenshot(var_app.imagepath + code + "_TruyenDuLieuBCA_DoanhNghiep_CheckThongTin.png")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Fail")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 13, code + "_TruyenDuLieuBCA_DoanhNghiep_CheckThongTin.png")

    def transmission_business_search(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.check_transmission_bca)
            var_app.driver.find_element(By.XPATH, var_app.busines).click()
            time.sleep(1)
            name_company = var_app.driver.find_element(By.XPATH, var_app.busines_company2).text

        except:
            move_module1(self, "", eventname, result, var_app.transmission_bca, 0.8, 0.85, 0.2, 0.85, 1000, "", "", "", "")
            var_app.driver.find_element(By.XPATH, var_app.busines).click()
            time.sleep(2)

        name_company = var_app.driver.find_element(By.XPATH, var_app.busines_company2).text
        var_app.driver.find_element(By.XPATH, var_app.transmission_business_input).clear()
        var_app.driver.find_element(By.XPATH, var_app.transmission_business_input).send_keys(name_company)
        time.sleep(2)

        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Truyền dữ liệu BCA - Doanh nghiệp",
                                              var_app.busines_company, name_company, "_TruyenDuLieuBCA_DoanhNghiep_Timkiem.png")

        var_app.driver.find_element(By.XPATH, var_app.transmission_business_input).clear()
        time.sleep(2)

    def transmission_business_add_new(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.check_transmission_bca)
            var_app.driver.find_element(By.XPATH, var_app.busines).click()
            time.sleep(1)
        except:
            move_module1(self, "", eventname, result, var_app.transmission_bca, 0.8, 0.85, 0.2, 0.85, 1000, "", "", "", "")
            var_app.driver.find_element(By.XPATH, var_app.busines).click()
            time.sleep(2)

        try:
            var_app.driver.find_element(By.XPATH, var_app.transmission_add_new).click()
        except:
            var_app.driver.find_element(By.XPATH, var_app.transmission_add_new1).click()
        time.sleep(2.5)
        number_random = random.randint(1, 999999)
        number_random = str(number_random)
        print(number_random)

        try:
            var_app.driver.find_element(By.XPATH, var_app.info_busines_busines).send_keys("CÔNG TY TNHH MỘC HẠ"+number_random)     #Doanh nghiệp
        except:
            var_app.driver.find_element(By.XPATH, var_app.info_busines_busines1).send_keys("CÔNG TY TNHH MỘC HẠ"+number_random)     #Doanh nghiệp
        time.sleep(0.5)

        try:
            var_app.driver.find_element(By.XPATH, var_app.info_busines_tax_code).send_keys("3500"+number_random)     #Mã số thuế
        except:
            var_app.driver.find_element(By.XPATH, var_app.info_busines_tax_code1).send_keys("3500"+number_random)     #Mã số thuế
        time.sleep(0.5)

        try:
            var_app.driver.find_element(By.XPATH, var_app.info_busines_phone).send_keys("0359"+number_random)     #Số điện thoại
        except:
            var_app.driver.find_element(By.XPATH, var_app.info_busines_phone1).send_keys("0359"+number_random)     #Số điện thoại
        time.sleep(0.5)

        try:
            var_app.driver.find_element(By.XPATH, var_app.info_busines_address).send_keys("190 Phan Trọng Tuệ, Thanh Trì, Hà Nội")     #Địa chỉ
        except:
            var_app.driver.find_element(By.XPATH, var_app.info_busines_address1).send_keys("0359"+number_random)     #Số điện thoại
        time.sleep(0.5)

        try:
            var_app.driver.find_element(By.XPATH, var_app.info_busines_department_gtvt).click()    #Sở GTVT
        except:
            var_app.driver.find_element(By.XPATH, var_app.info_busines_department_gtvt1).click()    #Sở GTVT
        time.sleep(2)

        module_other_app.tap_scaled(var_app.driver, [(95, 303)])
        time.sleep(2)
        try:
            var_app.driver.find_element(By.XPATH, var_app.info_busines_commit).click()    #Tôi cam kết
        except:
            var_app.driver.find_element(By.XPATH, var_app.info_busines_commit1).click()    #Tôi cam kết
        time.sleep(0.5)
        var_app.driver.find_element(By.XPATH, var_app.save).click()
        time.sleep(2)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Truyền dữ liệu BCA - Doanh nghiệp",
                                              var_app.check_transmission_business_add_new, "Thêm mới doanh nghiệp thành công", "_TruyenDuLieuBCA_DoanhNghiep_ThemMoi.png")
        module_other_app.writeData1(var_app.path_luutamthoi, "Sheet1", 72, 2, "CÔNG TY TNHH MỘC HẠ"+number_random)
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 14, "CÔNG TY TNHH MỘC HẠ"+number_random)
        print("CÔNG TY TNHH MỘC HẠ"+number_random)

        try:
            var_app.driver.find_element(By.XPATH, var_app.info_busines)
            var_app.driver.find_element(By.XPATH, var_app.cancel).click()
            time.sleep(2)
            var_app.driver.find_element(By.XPATH, var_app.IGREE).click()
            time.sleep(2)
        except:
            pass

    def transmission_business_update(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.check_transmission_bca)
            var_app.driver.find_element(By.XPATH, var_app.busines).click()
            time.sleep(1)
        except:
            utilities.transmission_business_add_new(self, "", "", "")

        name_company = module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 72, 2)
        try:
            var_app.driver.find_element(By.XPATH, var_app.transmission_business_input).clear()
            time.sleep(0.5)
            var_app.driver.find_element(By.XPATH, var_app.transmission_business_input).send_keys(name_company)
        except:
            var_app.driver.find_element(By.XPATH, var_app.transmission_business_input1).clear()
            time.sleep(0.5)
            var_app.driver.find_element(By.XPATH, var_app.transmission_business_input1).send_keys(name_company)
        time.sleep(2.5)

        var_app.driver.find_element(By.XPATH, var_app.busines_company1).click()
        time.sleep(2.5)
        try:
            var_app.driver.find_element(By.XPATH, var_app.info_busines_address).clear()
            time.sleep(0.5)
            var_app.driver.find_element(By.XPATH, var_app.info_busines_address).send_keys("910 Kim Giang, Đại Kim, Hà Nội")     #Địa chỉ
            time.sleep(0.5)
            var_app.driver.find_element(By.XPATH, var_app.info_busines_commit).click()    #Tôi cam kết
        except:
            var_app.driver.find_element(By.XPATH, var_app.info_busines_address1).clear()
            time.sleep(0.5)
            var_app.driver.find_element(By.XPATH, var_app.info_busines_address1).send_keys("910 Kim Giang, Đại Kim, Hà Nội")     #Địa chỉ
            time.sleep(0.5)
            var_app.driver.find_element(By.XPATH, var_app.info_busines_commit1).click()    #Tôi cam kết

        time.sleep(0.5)
        var_app.driver.find_element(By.XPATH, var_app.save).click()
        time.sleep(2)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Truyền dữ liệu BCA - Doanh nghiệp",
                                          var_app.check_transmission_business_update, "Cập nhật doanh nghiệp thành công", "_TruyenDuLieuBCA_DoanhNghiep_CapNhat.png")


        try:
            var_app.driver.find_element(By.XPATH, var_app.info_busines)
            var_app.driver.find_element(By.XPATH, var_app.cancel).click()
            time.sleep(2)
            var_app.driver.find_element(By.XPATH, var_app.IGREE).click()
            time.sleep(2)
        except:
            pass

    def transmission_business_delete(self, code, eventname, result):
        name_company = module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 72, 2)

        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.busines_company_all+"//*[@text='"+name_company+"']")
        except:
            move_module1(self, "", eventname, result, var_app.transmission_bca, 0.8, 0.85, 0.2, 0.85, 1000, "", "", "", "")
            var_app.driver.find_element(By.XPATH, var_app.busines).click()
        time.sleep(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.transmission_business_input).clear()
            time.sleep(0.5)
            var_app.driver.find_element(By.XPATH, var_app.transmission_business_input).send_keys(name_company)
        except:
            var_app.driver.find_element(By.XPATH, var_app.transmission_business_input1).clear()
            time.sleep(0.5)
            var_app.driver.find_element(By.XPATH, var_app.transmission_business_input1).send_keys(name_company)
        time.sleep(2.5)
        try:
            name_company1 = var_app.driver.find_element(By.XPATH, var_app.busines_company).text
        except:
            name_company1 = var_app.driver.find_element(By.XPATH, var_app.busines_company1).text

        if name_company1 == name_company:
            module_other_app.swipe_scaled(var_app.driver, 650, 400, 150, 400, 1000)
            time.sleep(1)
            module_other_app.swipe_scaled(var_app.driver, 650, 400, 150, 400, 1000)
            time.sleep(1)
            var_app.driver.find_element(By.XPATH, var_app.delete).click()
            time.sleep(2)
            var_app.driver.find_element(By.XPATH, var_app.IGREE).click()
            time.sleep(2)
            module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Truyền dữ liệu BCA - Doanh nghiệp",
                                                  var_app.transmission_business_delete, "Xóa doanh nghiệp thành công", "_TruyenDuLieuBCA_DoanhNghiep_Xoa.png")
            try:
                var_app.driver.find_element(By.XPATH, var_app.transmission_business_input).clear()
            except:
                var_app.driver.find_element(By.XPATH, var_app.transmission_business_input1).clear()








    def transmission_drive(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.drive).click()
            time.sleep(2)
            drive_name_drive = var_app.driver.find_element(By.XPATH, var_app.drive_name_drive).text
        except:
            move_module1(self, "", eventname, result, var_app.transmission_bca, 0.8, 0.85, 0.2, 0.85, 1000, "", "", "", "")
            var_app.driver.find_element(By.XPATH, var_app.drive).click()
            time.sleep(2)

        var_app.logging.info("--------------")
        var_app.logging.info("Trang chủ - Truyền dữ liệu BCA - Lái xe")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)

        try:
            drive_name_drive = var_app.driver.find_element(By.XPATH, var_app.drive_name_drive).text
            drive_type_liscense = var_app.driver.find_element(By.XPATH, var_app.drive_type_liscense).text
            drive_place_of_issue = var_app.driver.find_element(By.XPATH, var_app.drive_place_of_issue).text
            drive_date_of_issue = var_app.driver.find_element(By.XPATH, var_app.drive_date_of_issue).text
            drive_expiration_date_of_issue = var_app.driver.find_element(By.XPATH, var_app.drive_expiration_date_of_issue).text

            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, "{}\n{}\n{}\n{}\n{}"
                                       .format(drive_name_drive, drive_type_liscense, drive_place_of_issue, drive_date_of_issue, drive_expiration_date_of_issue))
            if (drive_name_drive != "") and (drive_type_liscense[0:10] == "Loại bằng:") and (drive_place_of_issue[0:8] == "Nơi cấp:") and (drive_date_of_issue[0:9] == "Ngày cấp:") and (drive_expiration_date_of_issue[0:13] == "Ngày hết hạn:"):
                var_app.logging.info("True")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Pass")
            else:
                var_app.logging.info("False")
                var_app.driver.save_screenshot(var_app.imagepath + code + "_TruyenDuLieuBCA_LaiXe_CheckThongTin.png")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Fail")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 13, code + "_TruyenDuLieuBCA_LaiXe_CheckThongTin.png")
        except:
            var_app.logging.info("False")
            var_app.driver.save_screenshot(var_app.imagepath + code + "_TruyenDuLieuBCA_LaiXe_CheckThongTin.png")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Fail")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 13, code + "_TruyenDuLieuBCA_LaiXe_CheckThongTin.png")

    def transmission_drive_search(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.check_list_driver)
            var_app.driver.find_element(By.XPATH, var_app.drive).click()
            time.sleep(1)
            name_drive2 = var_app.driver.find_element(By.XPATH, var_app.name_drive2).text

        except:
            move_module1(self, "", eventname, result, var_app.transmission_bca, 0.8, 0.85, 0.2, 0.85, 1000, "", "", "", "")
            var_app.driver.find_element(By.XPATH, var_app.drive).click()
            time.sleep(2)

        name_drive2 = var_app.driver.find_element(By.XPATH, var_app.name_drive2).text
        name_drive2 = name_drive2.split(" - ")[0]
        len_name_drive2 = len(name_drive2)

        try:
            var_app.driver.find_element(By.XPATH, var_app.transmission_drive_input).clear()
            var_app.driver.find_element(By.XPATH, var_app.transmission_drive_input).send_keys(name_drive2)
        except:
            var_app.driver.find_element(By.XPATH, var_app.transmission_drive_input1).clear()
            var_app.driver.find_element(By.XPATH, var_app.transmission_drive_input1).send_keys(name_drive2)
        time.sleep(2)

        var_app.logging.info("--------------")
        var_app.logging.info("Trang chủ - Truyền dữ liệu BCA - Lái xe")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        try:
            check_text = var_app.driver.find_element(By.XPATH, var_app.name_drive1).text
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, check_text)
            var_app.logging.info(check_text)
            if check_text[0:len_name_drive2] == name_drive2:
                var_app.logging.info("True")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Pass")
            else:
                var_app.logging.info("False")
                var_app.driver.save_screenshot(var_app.imagepath + code + "_TruyenDuLieuBCA_LaiXe_Timkiem.png")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Fail")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 13, code + "_TruyenDuLieuBCA_LaiXe_Timkiem.png")
        except:
            var_app.logging.info("False")
            var_app.driver.save_screenshot(var_app.imagepath + code + "_TruyenDuLieuBCA_LaiXe_Timkiem.png")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Fail")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 13, code + "_TruyenDuLieuBCA_LaiXe_Timkiem.png")

        try:
            var_app.driver.find_element(By.XPATH, var_app.transmission_drive_input).clear()
        except:
            var_app.driver.find_element(By.XPATH, var_app.transmission_drive_input1).clear()
        time.sleep(2)

    def transmission_drive_combobox(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.check_list_driver)
            var_app.driver.find_element(By.XPATH, var_app.drive_type_liscense)
            var_app.driver.find_element(By.XPATH, var_app.drive).click()
            time.sleep(1)
        except:
            move_module1(self, "", eventname, result, var_app.transmission_bca, 0.8, 0.85, 0.2, 0.85, 1000, "", "", "", "")
            var_app.driver.find_element(By.XPATH, var_app.drive).click()
            time.sleep(2)


        try:
            var_app.driver.find_element(By.XPATH, var_app.transmission_drive_combobox).click()
        except:
            var_app.driver.find_element(By.XPATH, var_app.transmission_drive_combobox1).click()
        time.sleep(2.5)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.drive_combobox_all).click()
            time.sleep(1)
        except:
            pass

        var_app.driver.find_element(By.XPATH, var_app.drive_combobox_input).send_keys("A1")
        time.sleep(2)

        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.drive_combobo_a1).click()
        except:
            module_other_app.tap_scaled(var_app.driver, [(37, 496)])
        time.sleep(1)
        var_app.driver.find_element(By.XPATH, var_app.save).click()
        time.sleep(2.5)

        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Truyền dữ liệu BCA - Lái xe",
                                              var_app.drive_type_liscense, "Loại bằng: A1", "_TruyenDuLieuBCA_LaiXe_LoaiBang.png")

        try:
            var_app.driver.find_element(By.XPATH, var_app.transmission_drive_combobox).click()
        except:
            var_app.driver.find_element(By.XPATH, var_app.transmission_drive_combobox1).click()
        time.sleep(2.5)
        module_other_app.tap_scaled(var_app.driver, [(40, 495)])
        time.sleep(0.5)
        var_app.driver.find_element(By.XPATH, var_app.save).click()
        time.sleep(2.5)

    def transmission_drive_add_new(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.check_list_driver)
            var_app.driver.find_element(By.XPATH, var_app.drive).click()
            time.sleep(1)
        except:
            move_module1(self, "", eventname, result, var_app.transmission_bca, 0.8, 0.85, 0.2, 0.85, 1000, "", "", "", "")
            var_app.driver.find_element(By.XPATH, var_app.drive).click()
            time.sleep(2)


        var_app.driver.find_element(By.XPATH, var_app.transmission_drive_add_new).click()


        time.sleep(2.5)
        random_number = random.randint(100000, 999999)
        random_number = str(random_number)
        print(random_number)

        var_app.driver.find_element(By.XPATH, var_app.driver_info_driver_code).send_keys(random_number)


        var_app.driver.find_element(By.XPATH, var_app.driver_info_lastname_and_fristname).send_keys("Trần Mạnh" + random_number)
        var_app.driver.find_element(By.XPATH, var_app.driver_info_number_liscense).send_keys("7720127" + random_number)
        var_app.driver.find_element(By.XPATH, var_app.driver_info_type_liscense).click()
        time.sleep(1.5)
        module_other_app.tap_scaled(var_app.driver, [(131, 366)])
        time.sleep(1.5)
        var_app.driver.find_element(By.XPATH, var_app.driver_info_release_date).click() #ngày cấp
        time.sleep(1.5)
        var_app.driver.find_element(By.XPATH, var_app.IGREE).click()
        time.sleep(1.5)
        var_app.driver.find_element(By.XPATH, var_app.driver_info_expiration_date).click()  #ngày hết hạn
        time.sleep(1.5)
        var_app.driver.find_element(By.XPATH, var_app.IGREE).click()
        time.sleep(1.5)
        var_app.driver.find_element(By.XPATH, var_app.place_of_issue).send_keys(var_app.data['utilities']['place_of_issue']) #Nơi cấp
        time.sleep(0.5)
        module_other_app.swipe_scaled(var_app.driver, 440, 1290, 440, 220, 500)
        time.sleep(2)

        var_app.driver.find_element(By.XPATH, var_app.employee_type).click()  # Loại nhân viên
        time.sleep(1.5)
        module_other_app.tap_scaled(var_app.driver, [(52, 306)])
        time.sleep(1.5)

        module_other_app.swipe_percent(var_app.driver, 0.5, 0.8, 0.5, 0.2, 1000)
        time.sleep(1)
        var_app.driver.find_element(By.XPATH, var_app.driver_info_date_of_birth).click()  # ngày sinh

        time.sleep(1.5)
        var_app.driver.find_element(By.XPATH, var_app.IGREE).click()
        time.sleep(1.5)

        try:
            var_app.driver.find_element(By.XPATH, var_app.driver_info_sex).click()
        except:
            var_app.driver.find_element(By.XPATH, var_app.driver_info_sex1).click()
        time.sleep(1.5)
        module_other_app.tap_scaled(var_app.driver, [(57, 364)])
        time.sleep(1.5)

        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.driver_info_number_cccd).send_keys(
                var_app.data['utilities']['fill_vehicle_cccd'] + random_number)
        except:
            var_app.driver.find_element(By.XPATH, var_app.driver_info_number_cccd1).send_keys(
                var_app.data['utilities']['fill_vehicle_cccd'] + random_number)

        try:
            var_app.driver.find_element(By.XPATH, var_app.driver_info_number_phone).send_keys(
                var_app.data['utilities']['fill_vehicle_phone'] + random_number)
        except:
            var_app.driver.find_element(By.XPATH, var_app.driver_info_number_phone1).send_keys(
                var_app.data['utilities']['fill_vehicle_phone'] + random_number)

        try:
            var_app.driver.find_element(By.XPATH, var_app.driver_info_adress).send_keys(
                var_app.data['utilities']['fill_vehicle_address'])
        except:
            var_app.driver.find_element(By.XPATH, var_app.driver_info_adress1).send_keys(
                var_app.data['utilities']['fill_vehicle_address'])

        var_app.driver.find_element(By.XPATH, var_app.driver_info_i_commit).click()
        time.sleep(1)



        # try:
        #     var_app.driver.find_element(By.XPATH, var_app.employee_type).click()  #Loại nhân viên
        # except:
        #     var_app.driver.find_element(By.XPATH, var_app.employee_type1).click()  #Loại nhân viên
        # time.sleep(1.5)
        # module_other_app.tap_scaled(var_app.driver, [(76, 389)])
        # time.sleep(1.5)
        #
        # try:
        #     var_app.driver.find_element(By.XPATH, var_app.driver_info_date_of_birth).click()    #ngày sinh
        # except:
        #     var_app.driver.find_element(By.XPATH, var_app.driver_info_date_of_birth1).click()    #ngày sinh
        # time.sleep(1.5)
        # var_app.driver.find_element(By.XPATH, var_app.IGREE).click()
        # time.sleep(1.5)
        #
        # try:
        #     var_app.driver.find_element(By.XPATH, var_app.driver_info_sex).click()     #Giowsi tính
        # except:
        #     var_app.driver.find_element(By.XPATH, var_app.driver_info_sex1).click()     #Giowsi tính
        # time.sleep(1.5)
        # module_other_app.tap_scaled(var_app.driver, [(57, 364)])
        # time.sleep(1.5)
        #
        # var_app.driver.implicitly_wait(1)
        #
        # var_app.driver.find_element(By.XPATH, var_app.driver_info_number_cccd3).send_keys(var_app.data['utilities']['fill_vehicle_cccd'] + random_number)
        # time.sleep(0.5)
        #
        # var_app.driver.find_element(By.XPATH, var_app.driver_info_number_phone3).send_keys(var_app.data['utilities']['fill_vehicle_phone'] + random_number)
        # time.sleep(0.5)
        #
        # try:
        #     var_app.driver.find_element(By.XPATH, var_app.driver_info_adress1).send_keys(var_app.data['utilities']['fill_vehicle_address1'])
        # except:
        #     var_app.driver.find_element(By.XPATH, var_app.driver_info_adress2).send_keys(var_app.data['utilities']['fill_vehicle_address1'])
        # time.sleep(0.5)
        #
        # var_app.driver.find_element(By.XPATH, var_app.driver_info_more).click()     #icon xem thêm
        # time.sleep(1.5)
        # module_other_app.swipe_scaled(var_app.driver, 440, 1290, 440, 220, 500)
        # time.sleep(1)
        #
        # var_app.driver.find_element(By.XPATH, var_app.driver_info_assign_user1)       #gán người dùng
        #
        # var_app.driver.find_element(By.XPATH, var_app.driver_info_assign_vehicle1).click()  #gán phương tiện
        # time.sleep(1.5)
        # module_other_app.tap_scaled(var_app.driver, [(61, 340)])
        # time.sleep(1.5)
        #
        # var_app.driver.find_element(By.XPATH, var_app.driver_info_assign_card1)  #số thẻ
        # # time.sleep(1.5)
        # # module_other_app.tap_scaled(var_app.driver, [(70, 306)])
        # # time.sleep(1.5)
        # try:
        #     var_app.driver.find_element(By.XPATH, var_app.driver_info_commit).click()  #Tôi cam kết
        # except:
        #     var_app.driver.find_element(By.XPATH, var_app.driver_info_commit1).click()  #Tôi cam kết
        # time.sleep(1)



        var_app.driver.find_element(By.XPATH, var_app.SAVE).click()
        time.sleep(2)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Truyền dữ liệu BCA - Lái xe",
                                              var_app.check_add_driver_fill_info, "Thêm lái xe thành công", "_TruyenDuLieuBCA_LaiXe_ThemMoi.png")

        module_other_app.writeData1(var_app.path_luutamthoi, "Sheet1", 73, 2, "Trần Mạnh" + random_number)
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 14, "Trần Mạnh" + random_number)
        print("Trần Mạnh" + random_number)

        try:
            var_app.driver.find_element(By.XPATH, var_app.info_drive)
            var_app.driver.find_element(By.XPATH, var_app.cancel).click()
            time.sleep(2)
            var_app.driver.find_element(By.XPATH, var_app.IGREE).click()
            time.sleep(2)
        except:
            pass

    def transmission_drive_update(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.find_element(By.XPATH, var_app.drive_name_drive)
        except:
            utilities.transmission_drive(self, "", "", "")


        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.check_list_driver)
            var_app.driver.find_element(By.XPATH, var_app.drive).click()
            time.sleep(1)
        except:
            utilities.transmission_drive_add_new(self, "", "", "")

        name_drive = module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 73, 2)
        try:
            var_app.driver.find_element(By.XPATH, var_app.transmission_drive_input).clear()
            time.sleep(0.5)
            var_app.driver.find_element(By.XPATH, var_app.transmission_drive_input).send_keys(name_drive)
        except:
            var_app.driver.find_element(By.XPATH, var_app.transmission_drive_input1).clear()
            time.sleep(0.5)
            var_app.driver.find_element(By.XPATH, var_app.transmission_drive_input1).send_keys(name_drive)
        time.sleep(2.5)

        var_app.driver.find_element(By.XPATH, var_app.drive_name_drive).click()
        time.sleep(3)


        random_number = random.randint(1, 999999)
        random_number = str(random_number)

        try:
            var_app.driver.find_element(By.XPATH, var_app.driver_info_driver_code).clear()
            time.sleep(0.5)
            var_app.driver.find_element(By.XPATH, var_app.driver_info_driver_code).send_keys(random_number)
            time.sleep(0.5)
        except:
            var_app.driver.find_element(By.XPATH, var_app.driver_info_driver_code1).clear()
            time.sleep(0.5)
            var_app.driver.find_element(By.XPATH, var_app.driver_info_driver_code1).send_keys(random_number)
        time.sleep(0.5)

        try:
            var_app.driver.find_element(By.XPATH, var_app.driver_info_i_commit).click()  #Tôi cam kết
        except:
            try:
                var_app.driver.find_element(By.XPATH, var_app.driver_info_commit1).click()  #Tôi cam kết
            except:
                var_app.driver.find_element(By.XPATH, var_app.driver_info_commit2).click()  #Tôi cam kết
        time.sleep(1)

        var_app.driver.find_element(By.XPATH, var_app.save).click()
        time.sleep(2)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Truyền dữ liệu BCA - Lái Xe",
                                              var_app.check_transmission_drive_update, "Sửa lái xe thành công", "_TruyenDuLieuBCA_LaiXe_CapNhat.png")


        try:
            var_app.driver.find_element(By.XPATH, var_app.info_drive)
            var_app.driver.find_element(By.XPATH, var_app.cancel).click()
            time.sleep(2)
            var_app.driver.find_element(By.XPATH, var_app.IGREE).click()
            time.sleep(2)
        except:
            pass

    def transmission_drive_delete(self, code, eventname, result):
        name_drive = module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 73, 2)

        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.check_list_driver)
            var_app.driver.find_element(By.XPATH, var_app.drive).click()
            time.sleep(1)
            try:
                var_app.driver.find_element(By.XPATH, var_app.transmission_drive_input).clear()
                time.sleep(0.5)
                var_app.driver.find_element(By.XPATH, var_app.transmission_drive_input).send_keys(name_drive)
            except:
                var_app.driver.find_element(By.XPATH, var_app.transmission_drive_input1).clear()
                time.sleep(0.5)
                var_app.driver.find_element(By.XPATH, var_app.transmission_drive_input1).send_keys(name_drive)
            time.sleep(2.5)
            name_drive1 = var_app.driver.find_element(By.XPATH, var_app.name_drive1).text

        except:
            move_module1(self, "", eventname, result, var_app.transmission_bca, 0.8, 0.85, 0.2, 0.85, 1000, "", "", "", "")
            var_app.driver.find_element(By.XPATH, var_app.drive).click()
            time.sleep(1)
            try:
                var_app.driver.find_element(By.XPATH, var_app.transmission_drive_input).send_keys(name_drive)
            except:
                var_app.driver.find_element(By.XPATH, var_app.transmission_drive_input1).send_keys(name_drive)
        time.sleep(2.5)

        try:
            name_drive1 = var_app.driver.find_element(By.XPATH, var_app.name_drive).text
        except:
            name_drive1 = var_app.driver.find_element(By.XPATH, var_app.name_drive1).text

        name_drive1 = name_drive1.split(" - ")[0]
        print(name_drive1)
        print(name_drive)

        name_drive = ''.join(re.findall(r'\d+', name_drive))
        name_drive1 = ''.join(re.findall(r'\d+', name_drive1))
        print(name_drive1)
        print(name_drive)

        if name_drive1 == name_drive:
            module_other_app.swipe_scaled(var_app.driver, 731, 370, 260, 370, 1000)
            time.sleep(1)
            module_other_app.swipe_scaled(var_app.driver, 731, 370, 260, 370, 1000)
            time.sleep(1)
            var_app.driver.find_element(By.XPATH, var_app.delete).click()
            time.sleep(2)
            var_app.driver.find_element(By.XPATH, var_app.IGREE).click()
            time.sleep(2)
            module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Truyền dữ liệu BCA - Lái xe",
                                                  var_app.transmission_drive_delete, "Xóa lái xe thành công", "_TruyenDuLieuBCA_LaiXe_Xoa.png")
            try:
                var_app.driver.find_element(By.XPATH, var_app.transmission_drive_input).clear()
            except:
                var_app.driver.find_element(By.XPATH, var_app.transmission_drive_input1).clear()
            time.sleep(0.5)







    def transmission_vehicle(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.transmission_vehicle).click()
            time.sleep(2)
            vehicle_dv_kdvt = var_app.driver.find_element(By.XPATH, var_app.vehicle_dv_kdvt).text
        except:
            move_module1(self, "", eventname, result, var_app.transmission_bca, 0.8, 0.85, 0.2, 0.85, 1000, "", "", "", "")
            var_app.driver.find_element(By.XPATH, var_app.transmission_vehicle).click()
            time.sleep(2)

        try:
            wait = WebDriverWait(var_app.driver, 10)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_app.vehicle_vehicle)))
        except:
            pass

        var_app.logging.info("--------------")
        var_app.logging.info("Trang chủ - Truyền dữ liệu BCA - Phương tiện")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)

        try:
            vehicle_vehicle = var_app.driver.find_element(By.XPATH, var_app.vehicle_vehicle).text
            vehicle_status = var_app.driver.find_element(By.XPATH, var_app.vehicle_status).text
            vehicle_dv_kdvt = var_app.driver.find_element(By.XPATH, var_app.vehicle_dv_kdvt).text
            vehicle_type_kdvt = var_app.driver.find_element(By.XPATH, var_app.vehicle_type_kdvt).text       #Loại hình gtvt
            vehicle_number_of_seats_tonnage = var_app.driver.find_element(By.XPATH, var_app.vehicle_number_of_seats_tonnage).text   #Số chỗ, trọng tải
            vehicle_frame_number = var_app.driver.find_element(By.XPATH, var_app.vehicle_frame_number).text         #Số khung
            vehicle_transmission_max_speed = var_app.driver.find_element(By.XPATH, var_app.vehicle_transmission_max_speed).text       #Tốc độ giới hạn
            vehicle_transmission_date = var_app.driver.find_element(By.XPATH, var_app.vehicle_transmission_date).text       #Ngày truyền

            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, "{}\n{}\n{}\n{}\n{}\n{}\n{}"
                                       .format(vehicle_vehicle, vehicle_status, vehicle_dv_kdvt, vehicle_type_kdvt, vehicle_number_of_seats_tonnage, vehicle_frame_number, vehicle_transmission_max_speed, vehicle_transmission_date))

            if (vehicle_vehicle != "") and (vehicle_status != "") and (vehicle_dv_kdvt[0:8] == "ĐV KDVT:") and (vehicle_type_kdvt[0:15] == "Loại hình KDVT:") and (vehicle_number_of_seats_tonnage[0:17] == "Số chỗ/Trọng tải:") \
                    and (vehicle_frame_number[0:9] == "Số khung:") and (vehicle_transmission_date[0:12] == "Ngày truyền:") and (vehicle_transmission_max_speed[0:16] == "Tốc độ giới hạn:"):
                var_app.logging.info("True")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Pass")
            else:
                var_app.logging.info("False")
                var_app.driver.save_screenshot(var_app.imagepath + code + "_TruyenDuLieuBCA_PhuongTien_CheckThongTin.png")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Fail")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 13, code + "_TruyenDuLieuBCA_PhuongTien_CheckThongTin.png")
        except:
            var_app.logging.info("False")
            var_app.driver.save_screenshot(var_app.imagepath + code + "_TruyenDuLieuBCA_PhuongTien_CheckThongTin.png")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Fail")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 13, code + "_TruyenDuLieuBCA_PhuongTien_CheckThongTin.png")

    def transmission_vehicle_search(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.transmission_vehicle).click()
            time.sleep(1)
            name_drive2 = var_app.driver.find_element(By.XPATH, var_app.name_vehicle2).text

        except:
            move_module1(self, "", eventname, result, var_app.transmission_bca, 0.8, 0.85, 0.2, 0.85, 1000, "", "", "", "")
            var_app.driver.find_element(By.XPATH, var_app.transmission_vehicle).click()
            time.sleep(2)

        name_vehicle2 = var_app.driver.find_element(By.XPATH, var_app.name_vehicle2).text

        var_app.driver.find_element(By.XPATH, var_app.transmission_vehicle_input).clear()
        time.sleep(0.5)
        var_app.driver.find_element(By.XPATH, var_app.transmission_vehicle_input).send_keys(name_vehicle2[0:4])
        time.sleep(2)
        module_other_app.write_result_text_try_if_cut(code, eventname, result, "Trang chủ - Truyền dữ liệu BCA - Phương tiện",
                                                  var_app.name_vehicle1, 0, 4, name_vehicle2[0:4], "_TruyenDuLieuBCA_PhuongTien_Timkiem.png")

        var_app.driver.find_element(By.XPATH, var_app.transmission_vehicle_input).clear()
        time.sleep(2)

    def transmission_vehicle_combobox(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.transmission_vehicle).click()
            time.sleep(1)
            vehicle_status = var_app.driver.find_element(By.XPATH, var_app.vehicle_status).text

        except:
            move_module1(self, "", eventname, result, var_app.transmission_bca, 0.8, 0.85, 0.2, 0.85, 1000, "", "", "", "")
            var_app.driver.find_element(By.XPATH, var_app.transmission_vehicle).click()
            time.sleep(2)


        var_app.driver.find_element(By.XPATH, var_app.transmission_vehicle_combobox).click()
        time.sleep(2.5)

        var_app.driver.find_element(By.XPATH, var_app.vehicle_combobox_input).send_keys("Chưa tích truyền")
        time.sleep(2)

        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.vehicle_combobox_input_chuatich).click()
        except:
            module_other_app.tap_scaled(var_app.driver, [(61, 306)])
        time.sleep(2.5)

        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Truyền dữ liệu BCA - Phương Tiện",
                                              var_app.vehicle_status, "Chưa tích truyền", "_TruyenDuLieuBCA_PhuongTien_TichTruyen.png")


        var_app.driver.find_element(By.XPATH, var_app.transmission_vehicle_combobox).click()
        time.sleep(2.5)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.vehicle_combobox_input_all).click()
        except:
            module_other_app.tap_scaled(var_app.driver, [(61, 306)])
            time.sleep(2.5)

    def transmission_vehicle_group(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.transmission_vehicle).click()
            time.sleep(1)
        except:
            move_module1(self, "", eventname, result, var_app.transmission_bca, 0.8, 0.85, 0.2, 0.85, 1000, "", "", "", "")
            var_app.driver.find_element(By.XPATH, var_app.transmission_vehicle).click()
            time.sleep(1)

        var_app.driver.find_element(By.XPATH, var_app.transmission_vehicle_group).click()
        time.sleep(2.5)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Truyền dữ liệu BCA - Phương Tiện",
                                              var_app.select_group_vehicle, "CHỌN NHÓM PHƯƠNG TIỆN", "_TruyenDuLieuBCA_PhuongTien_ChonNhom.png")


        var_app.driver.find_element(By.XPATH, var_app.select_group_vehicle_x).click()
        time.sleep(2)

    def transmission_vehicle_add_new(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.transmission_vehicle).click()
        except:
            move_module1(self, "", eventname, result, var_app.transmission_bca, 0.8, 0.85, 0.2, 0.85, 1000, "", "", "", "")
            var_app.driver.find_element(By.XPATH, var_app.transmission_vehicle).click()
        time.sleep(1.5)

        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.transmission_add_new).click()
        except:
            var_app.driver.find_element(By.XPATH, var_app.transmission_add_new1).click()

        time.sleep(2.5)
        try:
            var_app.driver.find_element(By.XPATH, var_app.info_vehicle_vehicle).click()  #Chọn phương tiện
        except:
            var_app.driver.find_element(By.XPATH, var_app.info_vehicle_vehicle1).click()  #Chọn phương tiện
        time.sleep(1.5)
        module_other_app.tap_scaled(var_app.driver, [(174, 352)])
        time.sleep(1.5)

        try:
            var_app.driver.find_element(By.XPATH, var_app.driver_info_commit).click()  #Tôi cam kết
        except:
            try:
                var_app.driver.find_element(By.XPATH, var_app.driver_info_commit1).click()  # Tôi cam kết
            except:
                var_app.driver.find_element(By.XPATH, var_app.driver_info_commit2).click()  # Tôi cam kết
        time.sleep(1)

        var_app.driver.find_element(By.XPATH, var_app.SAVE).click()
        time.sleep(1.5)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.IGREE).click()
        except:
            pass

        wait = WebDriverWait(var_app.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, var_app.check_transmission_vehicle_add_new)))
        time.sleep(0.5)

        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Truyền dữ liệu BCA - Phương tiện",
                                              var_app.check_transmission_vehicle_add_new, "Thêm mới thông tin tích truyền thành công", "_TruyenDuLieuBCA_PhuongTien_ThemMoi.png")


        try:
            var_app.driver.find_element(By.XPATH, var_app.info_vehicle)
            var_app.driver.find_element(By.XPATH, var_app.cancel).click()
            time.sleep(2)
            var_app.driver.find_element(By.XPATH, var_app.IGREE).click()
            time.sleep(2)
        except:
            pass

    def transmission_vehicle_update(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass



        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.vehicle_vehicle)
            var_app.driver.find_element(By.XPATH, var_app.transmission_vehicle).click()
        except:
            move_module1(self, "", eventname, result, var_app.transmission_bca, 0.8, 0.85, 0.2, 0.85, 1000, "", "", "", "")
            var_app.driver.find_element(By.XPATH, var_app.transmission_vehicle).click()
        time.sleep(1.5)

        var_app.driver.find_element(By.XPATH, var_app.vehicle_vehicle).click()
        time.sleep(2.5)
        try:
            var_app.driver.find_element(By.XPATH, var_app.driver_info_vantai).click()  #Vận tải chạy nội thành, đô thi
            time.sleep(0.5)
            var_app.driver.find_element(By.XPATH, var_app.driver_info_vantai).click()  #Vận tải chạy nội thành, đô thi
        except:
            var_app.driver.find_element(By.XPATH, var_app.driver_info_vantai1).click()  #Vận tải chạy nội thành, đô thi
            time.sleep(0.5)
            var_app.driver.find_element(By.XPATH, var_app.driver_info_vantai1).click()  #Vận tải chạy nội thành, đô thi
        time.sleep(0.5)

        var_app.driver.find_element(By.XPATH, var_app.tichtruyen)

        try:
            var_app.driver.find_element(By.XPATH, var_app.driver_info_commit1).click()  #Tôi cam kết
        except:
            var_app.driver.find_element(By.XPATH, var_app.driver_info_commit2).click()  #Tôi cam kết
        time.sleep(1)

        var_app.driver.find_element(By.XPATH, var_app.SAVE).click()
        time.sleep(1)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.IGREE).click()
        except:
            pass

        wait = WebDriverWait(var_app.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, var_app.check_transmission_vehicle_update)))
        time.sleep(0.5)


        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Truyền dữ liệu BCA - Phương tiện",
                                              var_app.check_transmission_vehicle_update, "Cập nhật thông tin tích truyền thành công", "_TruyenDuLieuBCA_PhuongTien_CapNhat.png")


        try:
            var_app.driver.find_element(By.XPATH, var_app.info_vehicle)
            var_app.driver.find_element(By.XPATH, var_app.cancel).click()
            time.sleep(2)
            var_app.driver.find_element(By.XPATH, var_app.IGREE).click()
            time.sleep(2)
        except:
            pass








    def transmission_image(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        # try:
        #     var_app.driver.implicitly_wait(0.3)
        #     var_app.driver.find_element(By.XPATH, var_app.check_transmission_bca)
        #     var_app.driver.find_element(By.XPATH, var_app.image).click()
        #     time.sleep(2)
        #     image_vehicle = var_app.driver.find_element(By.XPATH, var_app.image_vehicle).text
        # except:
        #     move_module1(self, "", eventname, result, var_app.transmission_bca, 0.8, 0.85, 0.2, 0.85, 1000, "", "", "", "")
        #     var_app.driver.find_element(By.XPATH, var_app.image).click()
        #     time.sleep(2)

        move_module2(self, code, eventname, result, var_app.transmission_bca, 0.8, 0.85, 0.2, 0.85, 1000,
                     "", var_app.image, "", "", var_app.data['login']['testlaixe111_tk'], var_app.data['login']['testlaixe111_mk'])
        var_app.driver.find_element(By.XPATH, var_app.image).click()
        time.sleep(2)



        var_app.logging.info("--------------")
        var_app.logging.info("Trang chủ - Truyền dữ liệu BCA - Hình ảnh")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)


        try:
            image_vehicle = var_app.driver.find_element(By.XPATH, var_app.image_vehicle).text
            image_frequency = var_app.driver.find_element(By.XPATH, var_app.image_frequency).text       #Tần suất
            image_transmission_date = var_app.driver.find_element(By.XPATH, var_app.image_transmission_date).text   #Ngày truyền
            image_day_of_discontinuation = var_app.driver.find_element(By.XPATH, var_app.image_day_of_discontinuation).text     #Ngày bỏ truyền
            image_channel = var_app.driver.find_element(By.XPATH, var_app.image_channel).text

            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, "{}\n{}\n{}\n{}\n{}"
                                       .format(image_vehicle, image_frequency, image_transmission_date, image_day_of_discontinuation, image_channel))

            if (image_vehicle != "") and (image_frequency[0:9] == "Tần suất:") and (image_transmission_date[0:12] == "Ngày truyền:") and (image_day_of_discontinuation[0:15] == "Ngày bỏ truyền:") and (image_channel[0:12] == "Kênh truyền:"):
                var_app.logging.info("True")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Pass")
            else:
                var_app.logging.info("False")
                var_app.driver.save_screenshot(var_app.imagepath + code + "_TruyenDuLieuBCA_HinhAnh_CheckThongTin.png")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Fail")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 13, code + "_TruyenDuLieuBCA_HinhAnh_CheckThongTin.png")
        except:
            var_app.logging.info("False")
            var_app.driver.save_screenshot(var_app.imagepath + code + "_TruyenDuLieuBCA_HinhAnh_CheckThongTin.png")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Fail")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 13, code + "_TruyenDuLieuBCA_HinhAnh_CheckThongTin.png")

    def transmission_image_search(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.image).click()
            time.sleep(1)
            var_app.driver.find_element(By.XPATH, var_app.name_image2)

        except:
            # move_module1(self, "", eventname, result, var_app.transmission_bca, 0.8, 0.85, 0.2, 0.85, 1000, "", "", "", "")
            move_module2(self, code, eventname, result, var_app.transmission_bca, 0.8, 0.85, 0.2, 0.85, 1000,
                         "", var_app.image, "", "", var_app.data['login']['testlaixe111_tk'],var_app.data['login']['testlaixe111_mk'])
            var_app.driver.find_element(By.XPATH, var_app.image).click()
            time.sleep(2)

        name_image2 = var_app.driver.find_element(By.XPATH, var_app.name_image2).text
        var_app.driver.find_element(By.XPATH, var_app.transmission_image_input).clear()
        time.sleep(0.5)
        var_app.driver.find_element(By.XPATH, var_app.transmission_image_input).send_keys(name_image2)
        time.sleep(2)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Truyền dữ liệu BCA - Hình ảnh",
                                                  var_app.name_image1, name_image2, "_TruyenDuLieuBCA_HinhAnh_Timkiem.png")

        var_app.driver.find_element(By.XPATH, var_app.transmission_image_input).clear()
        time.sleep(2)

    def transmission_image_combobox(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.image).click()
            time.sleep(1)
            vehicle_status = var_app.driver.find_element(By.XPATH, var_app.vehicle_status).text

        except:
            move_module2(self, code, eventname, result, var_app.transmission_bca, 0.8, 0.85, 0.2, 0.85, 1000,
                         "", var_app.image, "", "", var_app.data['login']['testlaixe111_tk'], var_app.data['login']['testlaixe111_mk'])

            # move_module1(self, "", eventname, result, var_app.transmission_bca, 0.8, 0.85, 0.2, 0.85, 1000, "", "", "", "")
            var_app.driver.find_element(By.XPATH, var_app.image).click()
            time.sleep(2)


        var_app.driver.find_element(By.XPATH, var_app.transmission_image_combobox).click()
        time.sleep(2.5)

        var_app.driver.find_element(By.XPATH, var_app.image_combobox_input).send_keys("Cửa ra vào")
        time.sleep(2)

        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.image_combobox_input_cuaravao).click()
        except:
            module_other_app.tap_scaled(var_app.driver, [(37, 502)])
        time.sleep(1)

        var_app.driver.find_element(By.XPATH, var_app.save).click()
        time.sleep(2.5)
        var_app.logging.info("--------------")
        var_app.logging.info("Trang chủ - Truyền dữ liệu BCA - Hình ảnh")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        try:
            check_text = var_app.driver.find_element(By.XPATH, var_app.image_channel).text
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, check_text)
            var_app.logging.info(check_text)
            if "Cửa ra vào" in check_text:
                var_app.logging.info("True")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Pass")
            else:
                var_app.logging.info("False")
                var_app.driver.save_screenshot(var_app.imagepath + code + "_TruyenDuLieuBCA_HinhAnh_Kenh.png")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Fail")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 13, code + "_TruyenDuLieuBCA_HinhAnh_Kenh.png")
        except:
            var_app.logging.info("False")
            var_app.driver.save_screenshot(var_app.imagepath + code + "_TruyenDuLieuBCA_HinhAnh_Kenh.png")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Fail")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 13, code + "_TruyenDuLieuBCA_HinhAnh_Kenh.png")


        var_app.driver.find_element(By.XPATH, var_app.transmission_image_combobox).click()
        time.sleep(2.5)
        module_other_app.tap_scaled(var_app.driver, [(37, 395)])
        time.sleep(1)
        module_other_app.tap_scaled(var_app.driver, [(37, 395)])
        time.sleep(1)
        var_app.driver.find_element(By.XPATH, var_app.save).click()
        time.sleep(2.5)

    def transmission_image_update(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.image).click()
            var_app.driver.find_element(By.XPATH, var_app.image_vehicle)
        except:
            move_module2(self, code, eventname, result, var_app.transmission_bca, 0.8, 0.85, 0.2, 0.85, 1000,
                         "", var_app.image, "", "", var_app.data['login']['testlaixe111_tk'], var_app.data['login']['testlaixe111_mk'])

            # move_module1(self, "", eventname, result, var_app.transmission_bca, 0.8, 0.85, 0.2, 0.85, 1000, "", "", "", "")
            var_app.driver.find_element(By.XPATH, var_app.image).click()
        time.sleep(1.5)

        try:
            var_app.driver.find_element(By.XPATH, var_app.transmission_image_input).clear()
            time.sleep(0.5)
            var_app.driver.find_element(By.XPATH, var_app.transmission_image_input).send_keys("29B12345_C")
        except:
            var_app.driver.find_element(By.XPATH, var_app.transmission_image_input1).clear()
            time.sleep(0.5)
            var_app.driver.find_element(By.XPATH, var_app.transmission_image_input1).send_keys("29B12345_C")
        time.sleep(2.5)
        var_app.driver.find_element(By.XPATH, var_app.image_vehicle).click()
        time.sleep(2.5)

        # try:
        #     var_app.driver.find_element(By.XPATH, var_app.transmission_image_channel2).click()
        # except:
        #     move_module2(self, code, eventname, result, var_app.transmission_bca, 0.8, 0.85, 0.2, 0.85, 1000,
        #                  "", var_app.image, "", "", var_app.data['login']['testlaixe111_tk'], var_app.data['login']['testlaixe111_mk'])
        #     var_app.driver.find_element(By.XPATH, var_app.image).click()
        #     time.sleep(1.5)
        #
        #     try:
        #         var_app.driver.find_element(By.XPATH, var_app.transmission_image_input).clear()
        #         time.sleep(0.5)
        #         var_app.driver.find_element(By.XPATH, var_app.transmission_image_input).send_keys("29B12345_C")
        #     except:
        #         var_app.driver.find_element(By.XPATH, var_app.transmission_image_input1).clear()
        #         time.sleep(0.5)
        #         var_app.driver.find_element(By.XPATH, var_app.transmission_image_input1).send_keys("29B12345_C")
        #     time.sleep(2.5)
        #
        #
        #     module_other_app.tap_scaled(var_app.driver, [(86, 431)])
        #     time.sleep(2.5)




        # var_app.driver.find_element(By.XPATH, var_app.select_channel_input).send_keys("Cửa ra vào")
        # time.sleep(1.5)
        # try:
        #     var_app.driver.find_element(By.XPATH, var_app.select_channel + "//*[@text='Cửa ra vào']").click()
        # except:
        #     module_other_app.tap_scaled(var_app.driver, [(61, 303)])
        # time.sleep(1.5)
        # module_other_app.swipe_scaled(var_app.driver, 150, 300, 150, 1100, 1000)
        # time.sleep(1)
        # module_other_app.swipe_scaled(var_app.driver, 150, 300, 150, 1100, 1000)
        # time.sleep(1)


        # try:
        #     var_app.driver.find_element(By.XPATH, var_app.transmission_image_channel2_checkbox_a).click()
        # except:
        #     pass
        # time.sleep(1.5)
        #
        #
        # try:
        #     var_app.driver.find_element(By.XPATH, var_app.driver_info_commit).click()  #Tôi cam kết
        # except:
        #     try:
        #         var_app.driver.find_element(By.XPATH, var_app.driver_info_commit1).click()  # Tôi cam kết
        #     except:
        #         var_app.driver.find_element(By.XPATH, var_app.driver_info_commit2).click()  # Tôi cam kết
        # time.sleep(1)
        #
        # var_app.driver.find_element(By.XPATH, var_app.SAVE).click()
        # time.sleep(1.5)


        var_app.driver.find_element(By.XPATH, var_app.driver_info_commit).click()  #Tôi cam kết
        time.sleep(1)
        var_app.driver.find_element(By.XPATH, var_app.SAVE).click()
        time.sleep(1.5)
        try:
            wait = WebDriverWait(var_app.driver, 10)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_app.check_transmission_image_update)))
        except:
            pass

        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Truyền dữ liệu BCA - Phương tiện",
                                              var_app.check_transmission_image_update, "Lưu thông tin tích truyền thành công", "_TruyenDuLieuBCA_HinhAnh_CapNhat.png")
        time.sleep(2)

        try:
            var_app.driver.find_element(By.XPATH, var_app.transmission_image)
            var_app.driver.find_element(By.XPATH, var_app.cancel).click()
            time.sleep(2)
            var_app.driver.find_element(By.XPATH, var_app.IGREE).click()
            time.sleep(2)
        except:
            pass

        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.transmission_image_update_back).click()
            time.sleep(2)
        except:
            try:
                var_app.driver.find_element(By.XPATH, var_app.transmission_image_update_back1).click()
                time.sleep(2)
            except:
                pass


        try:
            time.sleep(1)
            var_app.driver.find_element(By.XPATH, var_app.CANCEL).click()
            time.sleep(2)
            var_app.driver.find_element(By.XPATH, var_app.IGREE).click()
            time.sleep(2)
        except:
            pass

        try:
            var_app.driver.find_element(By.XPATH, var_app.transmission_image_input).clear()
        except:
            var_app.driver.find_element(By.XPATH, var_app.transmission_image_input1).clear()
        time.sleep(0.5)

    def transmission_image_add_new(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.image).click()
        except:
            move_module2(self, code, eventname, result, var_app.transmission_bca, 0.8, 0.85, 0.2, 0.85, 1000,
                         "", var_app.image, "", "", var_app.data['login']['testlaixe111_tk'], var_app.data['login']['testlaixe111_mk'])

            # move_module1(self, "", eventname, result, var_app.transmission_bca, 0.8, 0.85, 0.2, 0.85, 1000, "", "", "", "")
            var_app.driver.find_element(By.XPATH, var_app.image).click()
        time.sleep(1.5)

        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.transmission_add_new).click()
        except:
            var_app.driver.find_element(By.XPATH, var_app.transmission_add_new1).click()

        time.sleep(2.5)
        try:
            var_app.driver.find_element(By.XPATH, var_app.transmission_image_vehicle).click()
        except:
            module_other_app.tap_scaled(var_app.driver, [(150, 265)])
        time.sleep(1.5)


        var_app.driver.find_element(By.XPATH, var_app.transmission_image_vehicle_input).send_keys("29B14426_C")#12B02533
        time.sleep(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            # var_app.driver.find_element(By.XPATH, var_app.transmission_image_vehicle_12B02533).click()
            var_app.driver.find_element(By.XPATH, var_app.transmission_image_vehicle_29B14426_C).click()
        except:
            time.sleep(1.5)
            module_other_app.tap_scaled(var_app.driver, [(180, 355)])
        time.sleep(1.5)


        try:
            var_app.driver.find_element(By.XPATH, var_app.transmission_image_frequency).click()      #Tần suất
        except:
            var_app.driver.find_element(By.XPATH, var_app.transmission_image_frequency1).click()      #Tần suất

        time.sleep(1.5)
        var_app.driver.find_element(By.XPATH, var_app.transmission_image_frequency_4p).click()
        time.sleep(1.5)
        module_other_app.swipe_scaled(var_app.driver, 150, 300, 150, 1100, 1000)
        time.sleep(1)
        module_other_app.swipe_scaled(var_app.driver, 150, 300, 150, 1100, 1000)
        time.sleep(1)




        try:
            var_app.driver.find_element(By.XPATH, var_app.transmission_image_channel1).click()
        except:
            module_other_app.tap_scaled(var_app.driver, [(350, 580)])
        time.sleep(1.5)
        var_app.driver.find_element(By.XPATH, var_app.select_channel_input).send_keys("Lái xe")
        time.sleep(1.5)
        try:
            var_app.driver.find_element(By.XPATH, var_app.select_channel + "//*[@text='Lái xe']").click()
        except:
            module_other_app.tap_scaled(var_app.driver, [(61, 303)])
        time.sleep(1.5)
        try:
            var_app.driver.find_element(By.XPATH, var_app.transmission_image_channel1_checkbox).click()
        except:
            module_other_app.tap_scaled(var_app.driver, [(40, 580)])
        time.sleep(1)




        try:
            var_app.driver.find_element(By.XPATH, var_app.transmission_image_channel2).click()
        except:
            module_other_app.tap_scaled(var_app.driver, [(350, 685)])
        time.sleep(1.5)
        var_app.driver.find_element(By.XPATH, var_app.select_channel_input).send_keys("Hành khách")
        time.sleep(1.5)
        try:
            var_app.driver.find_element(By.XPATH, var_app.select_channel + "//*[@text='Hành khách']").click()
        except:
            module_other_app.tap_scaled(var_app.driver, [(61, 303)])
        time.sleep(1.5)
        try:
            var_app.driver.find_element(By.XPATH, var_app.transmission_image_channel2_checkbox).click()
        except:
            module_other_app.tap_scaled(var_app.driver, [(40, 685)])
        time.sleep(1)





        try:
            var_app.driver.find_element(By.XPATH, var_app.transmission_image_channel3).click()
        except:
            module_other_app.tap_scaled(var_app.driver, [(350, 785)])
        time.sleep(1.5)
        var_app.driver.find_element(By.XPATH, var_app.select_channel_input).send_keys("Cửa ra vào")
        time.sleep(1.5)
        try:
            var_app.driver.find_element(By.XPATH, var_app.select_channel + "//*[@text='Cửa ra vào']").click()
        except:
            module_other_app.tap_scaled(var_app.driver, [(61, 303)])
        time.sleep(1.5)
        try:
            var_app.driver.find_element(By.XPATH, var_app.transmission_image_channel3_checkbox).click()
        except:
            module_other_app.tap_scaled(var_app.driver, [(40, 785)])
        time.sleep(1)




        try:
            var_app.driver.find_element(By.XPATH, var_app.transmission_image_channel4).click()
        except:
            module_other_app.tap_scaled(var_app.driver, [(350, 885)])
        time.sleep(1.5)
        var_app.driver.find_element(By.XPATH, var_app.select_channel_input).send_keys("Tất cả")
        time.sleep(1.5)
        try:
            var_app.driver.find_element(By.XPATH, var_app.select_channel + "//*[@text='Tất cả']").click()
        except:
            module_other_app.tap_scaled(var_app.driver, [(61, 303)])
        time.sleep(1.5)
        try:
            var_app.driver.find_element(By.XPATH, var_app.transmission_image_channel4_checkbox).click()
        except:
            module_other_app.tap_scaled(var_app.driver, [(40, 885)])
        time.sleep(1)



        try:
            var_app.driver.find_element(By.XPATH, var_app.transmission_image_vehicle).click()
        except:
            module_other_app.tap_scaled(var_app.driver, [(150, 265)])
        time.sleep(1.5)
        var_app.driver.find_element(By.XPATH, var_app.transmission_image_vehicle_input).send_keys("29B12345_C")# #11A11225
        time.sleep(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            # var_app.driver.find_element(By.XPATH, var_app.transmission_image_vehicle_11A11225).click()
            var_app.driver.find_element(By.XPATH, var_app.transmission_image_vehicle_29B12345_C).click()
        except:
            time.sleep(1.5)
            module_other_app.tap_scaled(var_app.driver, [(180, 355)])
        time.sleep(1.5)
        #chọn xe và lưu
        module_other_app.swipe_scaled(var_app.driver, 150, 300, 150, 1100, 1000)
        time.sleep(1)
        module_other_app.swipe_scaled(var_app.driver, 150, 300, 150, 1100, 1000)
        time.sleep(1)

        try:
            var_app.driver.find_element(By.XPATH, var_app.transmission_image_channel1).click()
        except:
            module_other_app.tap_scaled(var_app.driver, [(350, 580)])
        time.sleep(1.5)

        var_app.driver.find_element(By.XPATH, var_app.select_channel_input).send_keys("Lái xe")
        time.sleep(1.5)
        try:
            var_app.driver.find_element(By.XPATH, var_app.select_channel + "//*[@text='Lái xe']").click()
        except:
            module_other_app.tap_scaled(var_app.driver, [(61, 303)])
        time.sleep(1.5)





        try:
            var_app.driver.find_element(By.XPATH, var_app.transmission_image_channel1_checkbox).click()
        except:
            module_other_app.tap_scaled(var_app.driver, [(40, 580)])
        time.sleep(1)

        try:
            var_app.driver.find_element(By.XPATH, var_app.transmission_image_coppy_all)
            time.sleep(0.5)
            var_app.driver.find_element(By.XPATH, var_app.transmission_image_commit).click()
            time.sleep(0.5)
        except:
            try:
                var_app.driver.find_element(By.XPATH, var_app.transmission_image_coppy_all1)
                time.sleep(0.5)
                var_app.driver.find_element(By.XPATH, var_app.transmission_image_commit1).click()
            except:
                module_other_app.tap_scaled(var_app.driver, [(37, 1087)])
                time.sleep(1)
                module_other_app.tap_scaled(var_app.driver, [(37, 1413)])
            time.sleep(1)
        var_app.driver.find_element(By.XPATH, var_app.SAVE).click()

        wait = WebDriverWait(var_app.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, var_app.check_transmission_image_update)))
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Truyền dữ liệu BCA - Hình ảnh",
                                              var_app.check_transmission_image_update, "Lưu thông tin tích truyền thành công", "_TruyenDuLieuBCA_HinhAnh_ThemMoi.png")

        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.cancel).click()
            time.sleep(2)
            var_app.driver.find_element(By.XPATH, var_app.IGREE).click()
            time.sleep(2)
        except:
            pass

        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.CANCEL).click()
            time.sleep(2)
            var_app.driver.find_element(By.XPATH, var_app.IGREE).click()
            time.sleep(2)
        except:
            pass

        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.transmission_image_add_new_back).click()
            time.sleep(2)
        except:
            pass

    def transmission_help(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.help).click()
        except:
            move_module1(self, "", eventname, result, var_app.transmission_bca, 0.8, 0.85, 0.2, 0.85, 1000, "", "", "", "")
            var_app.driver.find_element(By.XPATH, var_app.help).click()
        time.sleep(1.5)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Truyền dữ liệu BCA - Hướng dẫn",
                                              var_app.HELP, "HƯỚNG DẪN", "_TruyenDuLieuBCA_HuongDan.png")

        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.transmission_help_x).click()
            time.sleep(2)
        except:
            pass







    def maintenance_vehicle(self, code, eventname, result):
        var_app.driver.implicitly_wait(5)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.check_maintenance)
        except:
            move_module1(self, "Utilities73", eventname, result, var_app.maintenance,
                         0.8, 0.85, 0.2, 0.85, 1000, "Trang chủ - Bảo dưỡng", var_app.check_maintenance,
                                                         "DANH SÁCH BẢO DƯỠNG", "_TrangChu_BaoDuong.png")

        try:
            vehicle2 = var_app.driver.find_element(By.XPATH, var_app.maintenance_vehicle2).text
        except:
            var_app.driver.find_element(By.XPATH, var_app.maintenance_back).click()
            time.sleep(2)
            var_app.driver.find_element(By.XPATH, var_app.maintenance).click()
            time.sleep(3.5)
            vehicle2 = var_app.driver.find_element(By.XPATH, var_app.maintenance_vehicle2).text

        var_app.driver.find_element(By.XPATH, var_app.maintenance_vehicle).click()
        time.sleep(2.5)
        var_app.driver.find_element(By.XPATH, var_app.maintenance_vehicle_input).send_keys(vehicle2)
        time.sleep(2.5)
        try:
            var_app.driver.find_element(By.XPATH, var_app.maintenance_vehicle_input1).click()
        except:
            module_other_app.tap_scaled(var_app.driver, [(200, 355)])
        time.sleep(3)

        var_app.logging.info("--------------")
        var_app.logging.info("Trang chủ - Bảo dưỡng ")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        try:
            vehicle_search = var_app.driver.find_element(By.XPATH, var_app.maintenance_vehicle).text
            vehicle1 = var_app.driver.find_element(By.XPATH, var_app.maintenance_vehicle1).text
            summary = var_app.driver.find_element(By.XPATH, var_app.maintenance_summary).text

            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, f"{summary}\nPhương tiện: {vehicle1}")
            var_app.logging.info(vehicle1)
            var_app.logging.info(vehicle2)
            var_app.logging.info(vehicle_search)
            var_app.logging.info(summary)

            if (vehicle1 == vehicle2 == vehicle_search) and (summary == "Tổng số: 1 phương tiện"):
                var_app.logging.info("True")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Pass")
            else:
                var_app.logging.info("False")
                var_app.driver.save_screenshot(var_app.imagepath + code + "_BaoDuong_PhuongTien.png")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Fail")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 13, code + "_BaoDuong_PhuongTien.png")
        except:
            var_app.logging.info("False")
            var_app.driver.save_screenshot(var_app.imagepath + code + "_BaoDuong_PhuongTien.png")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Fail")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 13, code + "_BaoDuong_PhuongTien.png")

        # var_app.driver.find_element(By.XPATH, var_app.maintenance_back).click()
        # time.sleep(2)
        # try:
        #     var_app.driver.find_element(By.XPATH, var_app.maintenance).click()
        #     time.sleep(3)
        # except:
        #     pass

    def maintenance_category(self, code, eventname, result):
        var_app.driver.implicitly_wait(5)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.check_maintenance)
        except:
            utilities.maintenance_vehicle(self, "", "", "")
            #
            # move_module1(self, "Utilities73", eventname, result, var_app.maintenance,
            #              0.8, 0.85, 0.2, 0.85, 1000, "", "", "", "")


        var_app.driver.find_element(By.XPATH, var_app.maintenance_category).click()
        time.sleep(2.5)
        var_app.driver.find_element(By.XPATH, var_app.maintenance_category_input).send_keys("Dán kính")
        time.sleep(2.5)
        try:
            var_app.driver.find_element(By.XPATH, var_app.maintenance_category_input1).click()
        except:
            module_other_app.tap_scaled(var_app.driver, [(77, 305)])
        time.sleep(3)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Bảo dưỡng",
                                              var_app.maintenance_category, "Dán kinh", "_BaoDuong_HangMucBaoDuong.png")

        var_app.driver.find_element(By.XPATH, var_app.maintenance_category).click()
        time.sleep(2.5)
        try:
            var_app.driver.find_element(By.XPATH, var_app.maintenance_category_input_all).click()
        except:
            module_other_app.tap_scaled(var_app.driver, [(55, 305)])
        time.sleep(3)

    def maintenance_status(self, code, eventname, result):
        var_app.driver.implicitly_wait(5)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.check_maintenance)
        except:
            utilities.maintenance_vehicle(self, "", "", "")

            # move_module1(self, "Utilities73", eventname, result, var_app.maintenance,
            #              0.8, 0.85, 0.2, 0.85, 1000, "", "", "", "")


        var_app.driver.find_element(By.XPATH, var_app.maintenance_status).click()
        time.sleep(2.5)
        try:
            var_app.driver.find_element(By.XPATH, var_app.maintenance_status_input).clear()
        except:
            var_app.driver.find_element(By.XPATH, var_app.maintenance_status).click()
            time.sleep(2.5)
            var_app.driver.find_element(By.XPATH, var_app.maintenance_status_input).clear()

        time.sleep(0.5)
        var_app.driver.find_element(By.XPATH, var_app.maintenance_status_input).send_keys("Chưa đến hạn")
        time.sleep(2.5)
        try:
            var_app.driver.find_element(By.XPATH, var_app.maintenance_status_input1).click()
        except:
            module_other_app.tap_scaled(var_app.driver, [(90, 308)])
        time.sleep(3)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Bảo dưỡng",
                                              var_app.maintenance_status, "Chưa đến hạn", "_BaoDuong_TrangThai.png")

        var_app.driver.find_element(By.XPATH, var_app.maintenance_status).click()
        time.sleep(2.5)
        try:
            var_app.driver.find_element(By.XPATH, var_app.maintenance_status_input).clear()
        except:
            var_app.driver.find_element(By.XPATH, var_app.maintenance_status).click()
            time.sleep(2.5)
            var_app.driver.find_element(By.XPATH, var_app.maintenance_status_input).clear()
        time.sleep(0.5)
        var_app.driver.find_element(By.XPATH, var_app.maintenance_status_input).send_keys("Tất cả")
        time.sleep(2.5)
        try:
            var_app.driver.find_element(By.XPATH, var_app.maintenance_status_input1).click()
        except:
            module_other_app.tap_scaled(var_app.driver, [(55, 306)])
        time.sleep(3)

    def maintenance_group(self, code, eventname, result):
        var_app.driver.implicitly_wait(5)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.check_maintenance)
        except:
            utilities.maintenance_vehicle(self, "", "", "")
            #
            # move_module1(self, "Utilities73", eventname, result, var_app.maintenance,
            #              0.8, 0.85, 0.2, 0.85, 1000, "", "", "", "")


        var_app.driver.find_element(By.XPATH, var_app.maintenance_group).click()
        time.sleep(2.5)

        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Bảo dưỡng",
                                              var_app.SELECT_GROUP_VEHICLE, "CHỌN NHÓM PHƯƠNG TIỆN", "_BaoDuong_ChonNhomPhuongTien.png")

        var_app.driver.find_element(By.XPATH, var_app.SELECT_GROUP_VEHICLE_x).click()
        time.sleep(2.5)

    def maintenance_fill_maintenance(self, code, eventname, result):
        var_app.driver.implicitly_wait(5)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.check_maintenance)
        except:
            utilities.maintenance_vehicle(self, "", "", "")

            # move_module1(self, "Utilities73", eventname, result, var_app.maintenance,
            #              0.8, 0.85, 0.2, 0.85, 1000, "", "", "", "")


        try:
            var_app.driver.find_element(By.XPATH, var_app.maintenance_fill_maintenance).click()
        except:
            var_app.driver.find_element(By.XPATH, var_app.maintenance_fill_maintenance1).click()
        time.sleep(2.5)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Bảo dưỡng",
                                              var_app.check_maintenance_fill_maintenance, "NHẬP BẢO DƯỠNG", "_BaoDuong_NhapBaoDuong.png")

    def maintenance_fill_maintenance_SELECT(self, code, eventname, result):
        var_app.driver.implicitly_wait(5)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.check_maintenance_fill_maintenance)
        except:
            utilities.maintenance_fill_maintenance(self, "", "", "")

        try:
            try:
                var_app.driver.find_element(By.XPATH, var_app.fill_maintenance_vehicle).click()
            except:
                var_app.driver.find_element(By.XPATH, var_app.fill_maintenance_vehicle1).click()
            time.sleep(2.5)
            var_app.driver.find_element(By.XPATH, var_app.fill_maintenance_vehicle_input).send_keys("36B02529")
            time.sleep(2)
            try:
                var_app.driver.find_element(By.XPATH, var_app.fill_maintenance_vehicle_input1).click()
            except:
                module_other_app.tap_scaled(var_app.driver, [(200, 355)])
            time.sleep(3)
        except:
            print("đã chọn xe màn đầu tiên nên màn này tự chọn xe")

        try:
            var_app.driver.find_element(By.XPATH, var_app.fill_maintenance_category_input).send_keys("Thay dầu")
        except:
            var_app.driver.find_element(By.XPATH, var_app.fill_maintenance_category_input1).send_keys("Thay dầu")
        time.sleep(2)

        #Hạng mục chưa chọn
        try:
            var_app.driver.find_element(By.XPATH, var_app.category_not_select_checkbox1).click()
        except:
            var_app.driver.find_element(By.XPATH, var_app.category_not_select_checkbox1_a).click()
        time.sleep(1.5)
        #sau khi tích data checkbox 1 sẽ chuyển thành mục hạng mục đã chọn
        try:
            var_app.driver.find_element(By.XPATH, var_app.category_selected_checkbox1)
        except:
            var_app.driver.find_element(By.XPATH, var_app.category_selected_checkbox1_a)

        time.sleep(0.5)
        var_app.driver.find_element(By.XPATH, var_app.SELECT).click()
        time.sleep(1.5)
        var_app.driver.find_element(By.XPATH, var_app.MORE).click()
        time.sleep(1.5)
        # element = wait.until(EC.element_to_be_clickable((By.XPATH, var_app.check_maintenance_fill_maintenance_SELECT)))
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Bảo dưỡng",
                                              var_app.check_maintenance_fill_maintenance_SELECT, "Thêm bảo dưỡng thành công", "_BaoDuong_NhapBaoDuong_Chon.png")
        time.sleep(2.5)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_maintenance_fill_maintenance)
            var_app.driver.find_element(By.XPATH, var_app.maintenance_fill_maintenance_back).click()
            time.sleep(2.5)
        except:
            pass

    def maintenance_history(self, code, eventname, result):
        var_app.driver.implicitly_wait(5)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.check_maintenance)
        except:
            utilities.maintenance_vehicle(self, "", "", "")

            # move_module1(self, "Utilities73", eventname, result, var_app.maintenance,
            #              0.8, 0.85, 0.2, 0.85, 1000, "", "", "", "")


        var_app.driver.find_element(By.XPATH, var_app.maintenance_history).click()
        time.sleep(2)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Bảo dưỡng - Lịch sử bảo dưỡng",
                                              var_app.check_maintenance_history, "LỊCH SỬ BẢO DƯỠNG", "_BaoDuong_LichBaoDuong.png")

    def maintenance_history_vehicle(self, code, eventname, result):
        var_app.driver.implicitly_wait(5)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.check_maintenance_history)
        except:
            utilities.maintenance_history(self, "", "", "")

        var_app.driver.find_element(By.XPATH, var_app.maintenance_history_fromdate)
        var_app.driver.find_element(By.XPATH, var_app.maintenance_history_todate)
        var_app.driver.find_element(By.XPATH, var_app.maintenance_history_vehicle).click()
        time.sleep(2.5)
        var_app.driver.find_element(By.XPATH, var_app.maintenance_history_vehicle_input).send_keys("36B02529")
        time.sleep(2)
        try:
            var_app.driver.find_element(By.XPATH, var_app.maintenance_history_vehicle_input1).click()
        except:
            module_other_app.tap_scaled(var_app.driver, [(200, 355)])
        time.sleep(3.4)

        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Bảo dưỡng - Lịch sử bảo dưỡng",
                                              var_app.maintenance_history_vehicle, "36B02529", "_BaoDuong_LichBaoDuong_PhuongTien.png")

    def maintenance_history_category(self, code, eventname, result):
        var_app.driver.implicitly_wait(5)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.check_maintenance_history_category)
        except:
            utilities.maintenance_history_vehicle(self, "", "", "")


        var_app.driver.find_element(By.XPATH, var_app.maintenance_history_category).click()
        time.sleep(2)
        var_app.driver.find_element(By.XPATH, var_app.maintenance_history_category_input).send_keys("Thay dầu")
        time.sleep(2)

        try:
            var_app.driver.find_element(By.XPATH, var_app.maintenance_history_category_input1).click()
        except:
            module_other_app.tap_scaled(var_app.driver, [(95, 305)])
        time.sleep(4)

        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Bảo dưỡng - Lịch sử bảo dưỡng",
                                              var_app.check_maintenance_history_category, "Thay dầu", "_BaoDuong_LichBaoDuong_HangMuc.png")

    def maintenance_history_excel(self, code, eventname, result):
        var_app.driver.implicitly_wait(5)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.check_maintenance_history_category)
        except:
            utilities.maintenance_history_vehicle(self, "", "", "")



        var_app.driver.find_element(By.XPATH, var_app.maintenance_history_excel).click()
        time.sleep(2.5)

        module_other_app.write_result_not_displayed_try(code, eventname, result, "Trang chủ - Bảo dưỡng - Lịch sử bảo dưỡng",
                                              var_app.check_export_excel, "_BaoDuong_LichBaoDuong_XuatExcel.png")
        report_app.general.back_excel(self, 4, var_app.check_maintenance_history)

        var_app.driver.find_element(By.XPATH, var_app.maintenance_history_back).click()
        time.sleep(2.5)

    def maintenance_detail(self, code, eventname, result):
        var_app.driver.implicitly_wait(5)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.check_maintenance)
        except:
            utilities.maintenance_vehicle(self, "", "", "")

            # move_module1(self, "Utilities73", eventname, result, var_app.maintenance,
            #              0.8, 0.85, 0.2, 0.85, 1000, "", "", "", "")

        try:
            var_app.driver.find_element(By.XPATH, var_app.table1_1).click()
        except:
            var_app.driver.find_element(By.XPATH, var_app.maintenance_back).click()
            time.sleep(2)
            var_app.driver.find_element(By.XPATH, var_app.maintenance).click()
            time.sleep(3)
            try:
                var_app.driver.find_element(By.XPATH, var_app.table1_1).click()
            except:
                module_other_app.tap_scaled(var_app.driver, [(125, 1120)])
        time.sleep(2.5)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Bảo dưỡng - Chi tiết bảo dưỡng",
                                              var_app.check_maintenance_detail, "CHI TIẾT BẢO DƯỠNG", "_BaoDuong_ChiTietBaoDuong.png")

    def maintenance_detail_category_check_info(self, code, eventname, result):
        var_app.driver.implicitly_wait(5)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.check_maintenance_detail)
        except:
            utilities.maintenance_detail(self, "", "", "")

        try:
            var_app.driver.find_element(By.XPATH, var_app.table1_1_1)
        except:
            var_app.driver.find_element(By.XPATH, var_app.maintenance_detail_back).click()
            time.sleep(2.5)
            try:
                var_app.driver.find_element(By.XPATH, var_app.table1_1).click()
            except:
                module_other_app.tap_scaled(var_app.driver, [(125, 1120)])
            time.sleep(2.5)


        var_app.logging.info("--------------")
        var_app.logging.info("Trang chủ - Bảo dưỡng - Chi tiết bảo dưỡng")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        try:
            table1_1_1 = var_app.driver.find_element(By.XPATH, var_app.table1_1_1).text
            table1_1_2 = var_app.driver.find_element(By.XPATH, var_app.table1_1_2).text
            table1_2_1 = var_app.driver.find_element(By.XPATH, var_app.table1_2_1).text
            table1_2_2 = var_app.driver.find_element(By.XPATH, var_app.table1_2_2).text
            table1_2_3 = var_app.driver.find_element(By.XPATH, var_app.table1_2_3).text
            table1_2_4 = var_app.driver.find_element(By.XPATH, var_app.table1_2_4).text

            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, f"Ngày bảo dưỡng: {table1_1_1}\nNgày bảo dưỡng kế tiếp: {table1_1_2}\n{table1_2_1}\n"
                                                                                    f"Định mức: {table1_2_2}\nTrong kỳ: {table1_2_3}\nCòn lại: {table1_2_4}")
            var_app.logging.info(f"Ngày bảo dưỡng: {table1_1_1}\nNgày bảo dưỡng kế tiếp: {table1_1_2}\n{table1_2_1}\n"
                                                                                    f"Định mức: {table1_2_2}\nTrong kỳ: {table1_2_3}\nCòn lại: {table1_2_4}")
            if (table1_1_1 != "") and (table1_1_2 != "") and (table1_2_1 != "") and (table1_2_2 != "") and (table1_2_3 != "") and (table1_2_4 != ""):
                var_app.logging.info("True")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Pass")
            else:
                var_app.logging.info("False")
                var_app.driver.save_screenshot(var_app.imagepath + code + "_BaoDuong_ChiTietBaoDuong_CheckThongTin.png")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Fail")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 13, code + "_BaoDuong_ChiTietBaoDuong_CheckThongTin.png")
        except:
            var_app.logging.info("False")
            var_app.driver.save_screenshot(var_app.imagepath + code + "_BaoDuong_ChiTietBaoDuong_CheckThongTin.png")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Fail")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 13, code + "_BaoDuong_ChiTietBaoDuong_CheckThongTin.png")

    def maintenance_detail_category(self, code, eventname, result):
        var_app.driver.implicitly_wait(5)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.check_maintenance_detail)
        except:
            utilities.maintenance_detail(self, "", "", "")


        try:
            var_app.driver.find_element(By.XPATH, var_app.table1_1_1)
        except:
            var_app.driver.find_element(By.XPATH, var_app.maintenance_detail_back).click()
            time.sleep(2.5)
            try:
                var_app.driver.find_element(By.XPATH, var_app.table1_1).click()
            except:
                module_other_app.tap_scaled(var_app.driver, [(125, 1120)])
            time.sleep(2.5)


        var_app.driver.find_element(By.XPATH, var_app.maintenance_detail_category).click()
        time.sleep(2)
        var_app.driver.find_element(By.XPATH, var_app.maintenance_detail_category_input).send_keys("Thay dầu")
        time.sleep(2)

        try:
            var_app.driver.find_element(By.XPATH, var_app.maintenance_detail_category_input1).click()
        except:
            module_other_app.tap_scaled(var_app.driver, [(95, 305)])
        time.sleep(3)

        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Bảo dưỡng - Chi tiết bảo dưỡng",
                                              var_app.maintenance_detail_category, "Thay dầu", "_BaoDuong_ChiTietBaoDuong_HangMuc.png")

    def maintenance_detail_status(self, code, eventname, result):
        var_app.driver.implicitly_wait(5)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.check_maintenance_detail)
        except:
            utilities.maintenance_detail(self, "", "", "")


        var_app.driver.find_element(By.XPATH, var_app.maintenance_detail_status).click()
        time.sleep(2)
        var_app.driver.find_element(By.XPATH, var_app.maintenance_detail_status_input).send_keys("Tất cả")
        time.sleep(2)

        try:
            var_app.driver.find_element(By.XPATH, var_app.maintenance_detail_status_input1).click()
        except:
            module_other_app.tap_scaled(var_app.driver, [(70, 305)])
        time.sleep(3)

        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Bảo dưỡng - Chi tiết bảo dưỡng",
                                              var_app.maintenance_detail_status, "Tất cả", "_BaoDuong_ChiTietBaoDuong_TrangThai.png")

    def maintenance_detail_icon_fill(self, code, eventname, result):
        var_app.driver.implicitly_wait(5)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.check_maintenance_detail)
        except:
            utilities.maintenance_detail(self, "", "", "")


        var_app.driver.find_element(By.XPATH, var_app.maintenance_detail_icon_fill).click()
        time.sleep(2.5)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Bảo dưỡng - Chi tiết bảo dưỡng",
                                              var_app.check_maintenance_fill_maintenance, "NHẬP BẢO DƯỠNG", "_BaoDuong_ChiTietBaoDuong_IconNhapBaoDuong.png")







    def timekeeping(self, code, eventname, result):
        var_app.driver.implicitly_wait(5)
        move_module2(self, code, eventname, result, var_app.timekeeping, 0.8, 0.85, 0.2, 0.85, 1000,
                     "Trang chủ - Chấm công", var_app.check_timekeeping, "CHẤM CÔNG", "_TrangChu_ChamCong.png",
                     var_app.data['login']['testlaixe111_tk'], var_app.data['login']['testlaixe111_mk'])

        try:
            var_app.driver.find_element(By.XPATH, var_app.in_use_app).click()
            time.sleep(3)
            module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Chấm công",
                                                      var_app.check_timekeeping, "CHẤM CÔNG", "_TrangChu_ChamCong.png")
        except:
            pass
        try:
            var_app.driver.find_element(By.XPATH, var_app.just_this_time).click()
            time.sleep(3)
            module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Chấm công",
                                                      var_app.check_timekeeping, "CHẤM CÔNG", "_TrangChu_ChamCong.png")
        except:
            pass

        try:
            wait = WebDriverWait(var_app.driver, 10)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_app.check_timekeeping)))
            module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Chấm công",
                                                      var_app.check_timekeeping, "CHẤM CÔNG", "_TrangChu_ChamCong.png")
        except:
            pass



    def timekeeping_compensatory(self, code, eventname, result):
        var_app.driver.implicitly_wait(5)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.check_timekeeping)
        except:
            utilities.timekeeping(self, "", "", "")

        var_app.driver.find_element(By.XPATH, var_app.timekeeping_compensatory).click()
        time.sleep(2.5)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Chấm công",
                                              var_app.check_timekeeping_compensatory, "CHẤM CÔNG BÙ", "_ChamCong_ChamCongBu.png")


    def timekeeping_compensatory_confirm(self, code, eventname, result):
        var_app.driver.implicitly_wait(5)
        wait = WebDriverWait(var_app.driver, 15)

        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.check_timekeeping_compensatory)
        except:
            # utilities.timekeeping(self, "", "", "")
            utilities.timekeeping_compensatory(self, "", "", "")


        var_app.driver.find_element(By.XPATH, var_app.timekeeping_compensatory_vehicle).click()
        time.sleep(2.5)
        # var_app.driver.find_element(By.XPATH, var_app.timekeeping_compensatory_vehicle_input).send_keys("29")
        var_app.driver.find_element(By.XPATH, var_app.timekeeping_compensatory_vehicle_input).send_keys("29A12345_C")
        time.sleep(2)
        try:
            var_app.driver.find_element(By.XPATH, var_app.timekeeping_compensatory_vehicle_input1).click()
        except:
            module_other_app.tap_scaled(var_app.driver, [(155, 350)])
        time.sleep(2)

        var_app.driver.find_element(By.XPATH, var_app.timekeeping_compensatory_starttime).click()
        time.sleep(2)
        module_other_app.swipe_scaled(var_app.driver, 590, 1068, 590, 1130, 1000)
        time.sleep(1)
        module_other_app.swipe_scaled(var_app.driver, 315, 1068, 315, 1130, 1000)
        time.sleep(1)
        var_app.driver.find_element(By.XPATH, var_app.IGREE).click()
        time.sleep(2)
        var_app.driver.find_element(By.XPATH, var_app.timekeeping_compensatory_from_location).click()
        time.sleep(2)
        module_other_app.tap_scaled(var_app.driver, [(838, 700)])
        module_other_app.tap_scaled(var_app.driver, [(838, 700)])
        time.sleep(2)

        element = wait.until(EC.element_to_be_clickable((By.XPATH, var_app.timekeeping_compensatory_endtime)))
        element.click()

        # var_app.driver.find_element(By.XPATH, var_app.timekeeping_compensatory_endtime).click()
        time.sleep(2)
        var_app.driver.find_element(By.XPATH, var_app.IGREE).click()
        time.sleep(2)

        element = wait.until(EC.element_to_be_clickable((By.XPATH, var_app.timekeeping_compensatory_to_location)))
        element.click()

        # var_app.driver.find_element(By.XPATH, var_app.timekeeping_compensatory_to_location).click()
        time.sleep(2)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, var_app.timekeeping_compensatory_note)))
        element.send_keys("Trường test chấm công bù")
        # var_app.driver.find_element(By.XPATH, var_app.timekeeping_compensatory_note).send_keys("Trường test chấm công bù")
        time.sleep(2)

        #ghi dữ liệu vào lưutamthoi
        vehicle = var_app.driver.find_element(By.XPATH, var_app.timekeeping_compensatory_vehicle_data).text
        module_other_app.writeData1(var_app.path_luutamthoi, "Sheet1", 113, 2, vehicle)


        start_time = var_app.driver.find_element(By.XPATH, var_app.timekeeping_compensatory_start_time_data).text
        from_location = var_app.driver.find_element(By.XPATH, var_app.timekeeping_compensatory_from_location_data).text
        end_time = var_app.driver.find_element(By.XPATH, var_app.timekeeping_compensatory_end_time_data).text
        to_location = var_app.driver.find_element(By.XPATH, var_app.timekeeping_compensatory_to_location_data).text

        var_app.driver.find_element(By.XPATH, var_app.CONFIRM).click()
        time.sleep(2.5)
        var_app.logging.info("--------------")
        var_app.logging.info("Trang chủ - Chấm công")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        try:
            var_app.driver.find_element(By.XPATH, var_app.time_not)
            try:
                check_text = var_app.driver.find_element(By.XPATH, var_app.time_not).text
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, check_text)
                var_app.logging.info(check_text)
                if check_text in ['Thời gian bắt đầu đã tồn tại. Vui lòng chọn lại', 'Thời gian bắt đầu, kết thúc đang thuộc chuyến khác. Vui lòng chọn lại']:
                    var_app.logging.info("True")
                    module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Pass")
                else:
                    var_app.logging.info("False")
                    var_app.driver.save_screenshot(var_app.imagepath + code + "_ChamCong_ChamCongBu.png")
                    module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Fail")
                    module_other_app.writeData(var_app.checklistpath, "Checklist", code, 13, code + "_ChamCong_ChamCongBu.png")
            except:
                var_app.logging.info("False")
                var_app.driver.save_screenshot(var_app.imagepath + code + "_ChamCong_ChamCongBu.png")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Fail")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 13, code + "_ChamCong_ChamCongBu.png")




            var_app.driver.find_element(By.XPATH, var_app.timekeeping_compensatory_x).click()
            time.sleep(2.5)

        except:
            var_app.driver.find_element(By.XPATH, var_app.history).click()
            time.sleep(10)

            try:
                check_vehicle = var_app.driver.find_element(By.XPATH, var_app.timekeeping_check_vehicle).text
                check_start_time = var_app.driver.find_element(By.XPATH, var_app.timekeeping_check_start_time).text
                check_from_location = var_app.driver.find_element(By.XPATH, var_app.timekeeping_check_from_location).text
                check_end_time = var_app.driver.find_element(By.XPATH, var_app.timekeeping_check_end_time).text
                check_to_location = var_app.driver.find_element(By.XPATH, var_app.timekeeping_check_to_location).text

                start_time = datetime.strptime(start_time, "%H:%M %d/%m/%Y")
                check_start_time = datetime.strptime(check_start_time, "%H:%M:%S %d/%m/%Y")

                end_time = datetime.strptime(end_time, "%H:%M %d/%m/%Y")
                check_end_time = datetime.strptime(check_end_time, "%H:%M:%S %d/%m/%Y")

                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, f"Phương tiện(Chấm công): {vehicle}\nPhương tiện(Lịch sử): {check_vehicle}\n"
                                                                                        f"Thời gian bắt đầu(Chấm công): {start_time}\nThời gian bắt đầu(Lịch sử): {check_start_time}\n"
                                                                                        f"Vị trí bắt đầu(Chấm công): {from_location}\nVị trí bắt đầu(Lịch sử): {check_from_location}\n"
                                                                                        f"Thời gian kết thúc(Chấm Công): {end_time}\nThời gian kết thúc(Lịch sử): {check_end_time}\n"
                                                                                        f"Vị trí kết thúc(Chấm công): {to_location}\nVị trí kết thúc(Lịch sử): {check_to_location}")
                if (vehicle == check_vehicle) and (start_time == check_start_time) and (from_location == check_from_location) and (end_time == check_end_time) and (to_location == check_to_location):
                    var_app.logging.info("True")
                    module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Pass")
                else:
                    var_app.logging.info("False")
                    var_app.driver.save_screenshot(var_app.imagepath + code + "_ChamCong_ChamCongBu_XacNhan.png")
                    module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Fail")
                    module_other_app.writeData(var_app.checklistpath, "Checklist", code, 13, code + "_ChamCong_ChamCongBu_XacNhan.png")
            except:
                var_app.logging.info("False")
                var_app.driver.save_screenshot(var_app.imagepath + code + "_ChamCong_ChamCongBu_XacNhan.png")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Fail")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 13, code + "_ChamCong_ChamCongBu_XacNhan.png")

    def check_timekeeping(self, code, eventname, result):
        var_app.driver.implicitly_wait(5)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        try:
            var_app.driver.find_element(By.XPATH, var_app.timekeeping).click()
            time.sleep(2)
        except:
            pass

        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.check_timekeeping)
        except:
            utilities.timekeeping(self, "", "", "")

        vehicle = module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 113, 2)

        var_app.driver.find_element(By.XPATH, var_app.timekeeping_vehicle).click()
        time.sleep(2.5)
        var_app.driver.find_element(By.XPATH, var_app.timekeeping_vehicle_input).send_keys(vehicle)
        time.sleep(2)
        try:
            var_app.driver.find_element(By.XPATH, var_app.timekeeping_vehicle_input1).click()
        except:
            module_other_app.tap_scaled(var_app.driver, [(147, 358)])
        time.sleep(3)

        try:
            wait = WebDriverWait(var_app.driver, 15)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_app.timekeeping_time_current)))
        except:
            pass


        var_app.logging.info("--------------")
        var_app.logging.info("Trang chủ - Chấm công")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        try:
            time_current = var_app.driver.find_element(By.XPATH, var_app.timekeeping_time_current).text
            drive = var_app.driver.find_element(By.XPATH, var_app.timekeeping_drive).text
            location = var_app.driver.find_element(By.XPATH, var_app.timekeeping_location).text
            vehicle = var_app.driver.find_element(By.XPATH, var_app.timekeeping_vehicle_a).text

            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, f"Thời gian hiện tại: {time_current}\n"
                                                                                    f"Lái xe: {drive}\n"
                                                                                    f"Vị trí: {location}\n"
                                                                                    f"Biển số xe: {vehicle}")

            if (time_current != "") and (drive != "") and (location != "") and (vehicle != ""):
                var_app.logging.info("True")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Pass")
            else:
                var_app.logging.info("False")
                var_app.driver.save_screenshot(var_app.imagepath + code + "_ChamCong_CheckThongTin.png")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Fail")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 13, code + "_ChamCong_CheckThongTin.png")
        except:
            var_app.logging.info("False")
            var_app.driver.save_screenshot(var_app.imagepath + code + "_ChamCong_CheckThongTin.png")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Fail")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 13, code + "_ChamCong_CheckThongTin.png")

    def timekeeping_start(self, code, eventname, result):
        var_app.driver.implicitly_wait(5)
        wait = WebDriverWait(var_app.driver, 15)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.check_timekeeping)
        except:
            utilities.timekeeping(self, "", "", "")
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_app.timekeeping_vehicle)))
            element.click()
            time.sleep(2.5)

            vehicle = module_other_app.readData(var_app.path_luutamthoi, "Sheet1", 113, 2)
            try:
                var_app.driver.find_element(By.XPATH, var_app.timekeeping_vehicle_input).send_keys(vehicle)
            except:
                var_app.driver.find_element(By.XPATH, var_app.timekeeping_vehicle_input).send_keys("29B07865")
            time.sleep(2)

            try:
                var_app.driver.find_element(By.XPATH, var_app.timekeeping_vehicle_input1).click()
            except:
                module_other_app.tap_scaled(var_app.driver, [(147, 358)])
            time.sleep(3)

            try:
                element = wait.until(EC.element_to_be_clickable((By.XPATH, var_app.timekeeping_time_current)))
            except:
                pass

        element = wait.until(EC.element_to_be_clickable((By.XPATH, var_app.START)))
        element.click()
        time.sleep(15)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.ALLOW).click()
            time.sleep(2)
        except:
            pass
        try:
            var_app.driver.find_element(By.XPATH, var_app.in_use_app).click()
            time.sleep(2)
        except:
            pass
        try:
            var_app.driver.find_element(By.XPATH, var_app.just_this_time).click()
            time.sleep(2)
        except:
            pass


        try:
            var_app.driver.find_element(By.XPATH, var_app.TAKE_A_PHOTO).click()
        except:
            try:
                var_app.driver.find_element(By.XPATH, var_app.in_use_app).click()
                time.sleep(2)
            except:
                pass
            var_app.driver.find_element(By.XPATH, var_app.TAKE_A_PHOTO).click()
        time.sleep(2.5)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, var_app.CONFIRM)))
        element.click()
        time.sleep(2)
        try:
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_app.check_timekeeping_start)))
        except:
            pass

        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Chấm công",
                                              var_app.check_timekeeping_start, "Chấm công thành công", "_ChamCong_BatDau.png")
        time.sleep(3)

    def check_timekeeping_start(self, code, eventname, result):
        var_app.driver.implicitly_wait(5)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        try:
            var_app.driver.implicitly_wait(10)
            var_app.driver.find_element(By.XPATH, var_app.timekeeping_image)
        except:
            utilities.timekeeping_start(self, "", "", "")
            # utilities.timekeeping(self, "", "", "")


        var_app.logging.info("--------------")
        var_app.logging.info("Trang chủ - Chấm công")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        timekeeping_current_time = var_app.driver.find_element(By.XPATH, var_app.timekeeping_current_time).text
        print(timekeeping_current_time)
        timekeeping_start_time = var_app.driver.find_element(By.XPATH, var_app.timekeeping_start_time).text
        print(timekeeping_start_time)
        timekeeping_start_vehicle = var_app.driver.find_element(By.XPATH, var_app.timekeeping_start_vehicle).text
        print(timekeeping_start_vehicle)
        timekeeping_start_location = var_app.driver.find_element(By.XPATH, var_app.timekeeping_start_location).text
        print(timekeeping_start_location)
        timekeeping_start_image = var_app.driver.find_element(By.XPATH, var_app.timekeeping_start_image).text
        print(timekeeping_start_image)

        try:
            timekeeping_current_time = var_app.driver.find_element(By.XPATH, var_app.timekeeping_current_time).text
            timekeeping_start_time = var_app.driver.find_element(By.XPATH, var_app.timekeeping_start_time).text
            timekeeping_start_vehicle = var_app.driver.find_element(By.XPATH, var_app.timekeeping_start_vehicle).text
            timekeeping_start_location = var_app.driver.find_element(By.XPATH, var_app.timekeeping_start_location).text
            timekeeping_start_image = var_app.driver.find_element(By.XPATH, var_app.timekeeping_start_image).text

            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, f"Thời gian hiện tại: {timekeeping_current_time}\n"
                                                                                    f"Thời gian: {timekeeping_start_time}"
                                                                                    f"Biển số: {timekeeping_start_vehicle}\n"
                                                                                    f"Vị trí: {timekeeping_start_location}\n"
                                                                                    f"{timekeeping_start_image}")

            if (timekeeping_current_time != "") and (timekeeping_start_time != "") and (timekeeping_start_vehicle != "") \
                    and (timekeeping_start_location != "") and (timekeeping_start_image != ""):
                var_app.logging.info("True")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Pass")
            else:
                var_app.logging.info("False")
                var_app.driver.save_screenshot(var_app.imagepath + code + "_ChamCong_CheckThongTin_batdau.png")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Fail")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 13, code + "_ChamCong_CheckThongTin_batdau.png")
        except:
            var_app.logging.info("False")
            var_app.driver.save_screenshot(var_app.imagepath + code + "_ChamCong_CheckThongTin_batdau.png")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Fail")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 13, code + "_ChamCong_CheckThongTin_batdau.png")

    def timekeeping_end(self, code, eventname, result):
        var_app.driver.implicitly_wait(5)
        wait = WebDriverWait(var_app.driver, 10)

        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.timekeeping_image)
        except:
            utilities.timekeeping_start(self, "", "", "")


        element = wait.until(EC.element_to_be_clickable((By.XPATH, var_app.END)))
        element.click()
        time.sleep(2.5)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.ALLOW).click()
            time.sleep(2)
        except:
            pass

        try:
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_app.TAKE_A_PHOTO)))
            element.click()
        except:
            pass
        time.sleep(2.5)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, var_app.CONFIRM)))
        element.click()
        time.sleep(3)

        # try:
        #     element = wait.until(EC.element_to_be_clickable((By.XPATH, var_app.check_timekeeping_start)))
        # except:
        #     pass

        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Chấm công",
                                              var_app.check_timekeeping_start, "Chấm công thành công", "_ChamCong_KetThuc.png")
        time.sleep(3)





    def history(self, code, eventname, result):
        var_app.driver.implicitly_wait(5)
        utilities.timekeeping(self, "", "", "")

        element = wait.until(EC.element_to_be_clickable((By.XPATH, var_app.history)))
        element.click()
        time.sleep(2.5)

        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - CHẤM CÔNG - Lịch sử",
                                              var_app.check_timekeeping_history, "Số lần chấm công", "_ChamCong_LichSu.png")

    def history_calendar(self, code, eventname, result):
        var_app.driver.implicitly_wait(5)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.check_timekeeping_history)
        except:
            utilities.history(self, "", "", "")

        element = wait.until(EC.element_to_be_clickable((By.XPATH, var_app.history_calendar)))
        month = element.text

        var_app.driver.find_element(By.XPATH, var_app.history_calendar).click()
        time.sleep(2.5)
        var_app.driver.find_element(By.XPATH, var_app.IGREE).click()
        time.sleep(2)
        module_other_app.write_result_text_try_if_in(code, eventname, result, "Trang chủ - CHẤM CÔNG - Lịch sử",
                                              var_app.check_history_calendar, month, "_ChamCong_LichSu.png")

    def history_vehicle(self, code, eventname, result):
        wait = WebDriverWait(var_app.driver, 10)

        var_app.driver.implicitly_wait(5)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.check_timekeeping_history)
        except:
            utilities.history(self, "", "", "")

        try:
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_app.timekeeping_start_vehicle1)))
            vehicle = element.text
        except:
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_app.timekeeping_back)))
            element.click()
            time.sleep(2.5)
            var_app.driver.find_element(By.XPATH, var_app.timekeeping).click()
            time.sleep(2.5)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_app.history)))
            element.click()
            time.sleep(2.5)
            vehicle = var_app.driver.find_element(By.XPATH, var_app.timekeeping_start_vehicle1).text

        element = wait.until(EC.element_to_be_clickable((By.XPATH, var_app.history_vehicle)))
        element.click()
        time.sleep(2.5)
        var_app.driver.find_element(By.XPATH, var_app.history_vehicle_input).send_keys(vehicle)
        time.sleep(2)

        try:
            var_app.driver.find_element(By.XPATH, var_app.history_vehicle_input1).click()
        except:
            module_other_app.tap_scaled(var_app.driver, [(187, 258)])
        time.sleep(2.5)

        try:
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_app.history_vehicle)))
        except:
            pass

        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - CHẤM CÔNG - Lịch sử",
                                              var_app.history_vehicle, vehicle, "_ChamCong_LichSu_PhuongTien.png")

    def history_vehicle_other(self, code, eventname, result, path_check, name_image):
        var_app.driver.implicitly_wait(5)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.timekeeping_time)
        except:
            utilities.history(self, "", "", "")

        module_other_app.write_result_text_try_if_other(code, eventname, result, "Trang chủ - CHẤM CÔNG - Lịch sử",
                                                  path_check, "", name_image)

    def history_vehicle_display(self, code, eventname, result, path_check, name_image):
        var_app.driver.implicitly_wait(5)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.timekeeping_time)
        except:
            utilities.history(self, "", "", "")

        module_other_app.write_result_displayed_try(code, eventname, result, "Trang chủ - CHẤM CÔNG - Lịch sử",
                                                  path_check, name_image)

    def history_delete(self, code, eventname, result):
        var_app.driver.implicitly_wait(5)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.timekeeping_time)
        except:
            utilities.history(self, "", "", "")

        element = wait.until(EC.element_to_be_clickable((By.XPATH, var_app.history_delete)))
        element.click()
        time.sleep(2.5)
        var_app.driver.find_element(By.XPATH, var_app.IGREE).click()
        time.sleep(2)

        try:
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_app.check_history_delete)))
        except:
            pass

        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - CHẤM CÔNG - Lịch sử",
                                              var_app.check_history_delete, "Xóa chấm công thành công", "_ChamCong_LichSu_Xoa.png")



















