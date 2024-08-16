import time
from selenium.webdriver.common.by import By

import report_app
import var_app
import module_other_app
import homepage_app
import minitor_app
import login_app
import random


def move_module1(self, code, eventname, result, link, startX, startY, endX, endY, duration,
                path_module, path_check, desire, path_image):
    var_app.driver.implicitly_wait(1)
    try:
        var_app.driver.find_element(By.XPATH, var_app.bagps).click()
        time.sleep(4)
    except:
        pass

    var_app.driver.implicitly_wait(3)
    try:
        var_app.driver.find_element(By.XPATH, var_app.homepage).click()
    except:
        login_app.login.check_logout1(self, "KHÔNG NHÓM ĐỘI", "ungroup", "12341234")
        try:
            var_app.driver.find_element(By.XPATH, var_app.homepage).click()
        except:
            login_app.login.login_v3(self, "ungroup", "12341234")
            var_app.driver.find_element(By.XPATH, var_app.homepage).click()
    time.sleep(1)

    var_app.driver.implicitly_wait(0.5)
    try:
        var_app.driver.swipe(450, 400, 450, 1300, 1000)
    except:
        pass
    try:
        var_app.driver.find_element(By.XPATH, var_app.favorite)
        var_app.driver.swipe(400, 1300, 400, 940, 1000)
    except:
        pass

    var_app.driver.implicitly_wait(1)
    try:
        minitor_app.scroll_and_click(startX, startY, endX, endY, duration, link)
    except:
        minitor_app.scroll_and_click_reverse(endX, startY, startX, endY, duration, link)
    time.sleep(2)
    module_other_app.write_result_text_try_if(code, eventname, result, path_module,
                                              path_check, desire, path_image)






class general:

    def utilities_back(self):
        var_app.driver.implicitly_wait(0.2)
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




class utilities:


    def hide_and_show_the_car_filter(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_hide_and_show_the_car)
        except:
            general.utilities_back(self)
            move_module1(self, "", "", "", var_app.hide_and_show_the_car, 725, 1100, 175, 1100, 500, "", "", "", "")

        var_app.driver.find_element(By.XPATH, var_app.hide_and_show_the_car_filter).click()
        time.sleep(2)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Ẩn hiện xe",
                                              var_app.filter, "BỘ LỌC TÌM KIẾM", "_TrangChu_AnHienXe_Loc.png")

        try:
            var_app.driver.find_element(By.XPATH, var_app.APPLY).click()
            time.sleep(1.5)
        except:
            pass


    def hide_and_show_the_car_excel(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_hide_and_show_the_car)
        except:
            general.utilities_back(self)
            move_module1(self, "", "", "", var_app.hide_and_show_the_car, 725, 1100, 175, 1100, 500, "", "", "", "")

        var_app.driver.find_element(By.XPATH, var_app.check_hide_and_show_the_car).click()
        time.sleep(2)
        report_app.general.back_excel(self, 4, var_app.check_vehicle_speed)


        module_other_app.write_result_text_try_if_other(code, eventname, result, "Trang chủ - Ẩn hiện xe",
                                              var_app.check_export_excel, "Lỗi xuất excel", "_TrangChu_AnHienXe_XuatExcel.png")


    def hide_and_show_the_car_search(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_hide_and_show_the_car)
        except:
            general.utilities_back(self)
            move_module1(self, "", "", "", var_app.hide_and_show_the_car, 725, 1100, 175, 1100, 500, "", "", "", "")

        var_app.driver.find_element(By.XPATH, var_app.hide_and_show_the_car_select_vehicle).click()
        time.sleep(2)
        var_app.driver.find_element(By.XPATH, var_app.hide_and_show_the_car_select_vehicle_input).send_keys(var_app.data['utilities']['hide_show_vihicle_search'])
        time.sleep(1.5)
        var_app.driver.tap([(350, 350)])
        time.sleep(3)
        var_app.driver.tap([(90, 500)])
        time.sleep(2.5)
        module_other_app.write_result_text_try_if_other(code, eventname, result, "Trang chủ - Ẩn hiện xe",
                                              var_app.check_hide_and_show_the_car_search, "", "_TrangChu_AnHienXe_TimKiem.png")

        try:
            var_app.driver.find_element(By.XPATH, var_app.select_vehilce_hide_iconx).click()
            time.sleep(1.3)
        except:
            pass


    def hide_and_show_the_car_checkbox(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_hide_and_show_the_car)
        except:
            general.utilities_back(self)
            move_module1(self, "", "", "", var_app.hide_and_show_the_car, 725, 1100, 175, 1100, 500, "", "", "", "")


        try:
            var_app.driver.find_element(By.XPATH, var_app.check_hide_and_show_the_car_checkbox2)
        except:
            var_app.driver.find_element(By.XPATH, var_app.check_hide_and_show_the_car_checkbox1).click()


        module_other_app.write_result_displayed_try(code, eventname, result, "Trang chủ - Ẩn hiện xe",
                                              var_app.check_hide_and_show_the_car_checkbox2, "_TrangChu_AnHienXe_Tat/BatThongBaoXe.png")

        try:
            var_app.driver.find_element(By.XPATH, var_app.check_hide_and_show_the_car_checkbox2)
            var_app.driver.find_element(By.XPATH, var_app.check_hide_and_show_the_car_checkbox1).click()
        except:
            pass


    def hide_and_show_the_car_icon_hide(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_hide_and_show_the_car)
        except:
            general.utilities_back(self)
            move_module1(self, "", "", "", var_app.hide_and_show_the_car, 725, 1100, 175, 1100, 500, "", "", "", "")


        var_app.driver.find_element(By.XPATH, var_app.hide_and_show_the_car_icon_hide).click()
        time.sleep(2)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Ẩn hiện xe",
                                              var_app.check_hide_and_show_the_car_icon_hide, "CHỌN PHƯƠNG TIỆN ẨN", "_TrangChu_AnHienXe_IconAnXe.png")


    def hide_and_show_the_car_hide_vehicle(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_hide_and_show_the_car_icon_hide)
        except:
            general.utilities_back(self)
            utilities.hide_and_show_the_car_icon_hide(self, "", "", "")

        var_app.driver.find_element(By.XPATH, var_app.hide_vehicle_input).send_keys(var_app.data['utilities']['select_hide_vehicle'])
        time.sleep(1)
        var_app.driver.tap([(38, 492)])
        time.sleep(0.5)
        var_app.driver.find_element(By.XPATH, var_app.APPLY).click()
        time.sleep(3)
        var_app.driver.find_element(By.XPATH, var_app.select_vehilce_hide_tcdb).click()
        var_app.driver.find_element(By.XPATH, var_app.select_vehilce_hide_select_reason).click()
        time.sleep(2)
        var_app.driver.tap([(150, 450)])
        time.sleep(1.5)
        var_app.driver.find_element(By.XPATH, var_app.select_vehilce_hide_note).send_keys(var_app.data['utilities']['select_hide_note'])
        time.sleep(0.5)
        var_app.driver.find_element(By.XPATH, var_app.SAVE).click()
        time.sleep(1)
        var_app.driver.find_element(By.XPATH, var_app.IGREE).click()
        time.sleep(2)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Ẩn hiện xe",
                                              var_app.check_hide_and_show_the_car_hide_vehicle, "Ẩn phương tiện thành công", "_TrangChu_AnHienXe_AnXe.png")


    def hide_and_show_the_car_un_hide_vehicle(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(3)

        var_app.driver.swipe(720, 500, 150, 500, 500)
        var_app.driver.tap([(820, 600)])
        time.sleep(1)
        var_app.driver.find_element(By.XPATH, var_app.CANCEL_HIDE).click()
        time.sleep(2)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Ẩn hiện xe", var_app.check_hide_and_show_the_car_un_hide_vehicle,
                                                  "Bỏ ẩn phương tiện thành công", "_TrangChu_AnHienXe_BoAnXe.png")
        general.utilities_back(self)








    def add_driver_fill_info(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        random_number = str(random.randint(100000, 999999))
        print(random_number)

        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_add_driver)
        except:
            general.utilities_back(self)
            move_module1(self, "", "", "", var_app.add_driver, 725, 1100, 175, 1100, 500, "", "", "", "")

        var_app.driver.find_element(By.XPATH, var_app.driver_info_lastname_and_fristname).send_keys(var_app.data['utilities']['fill_vehicle_name'] + random_number)
        var_app.driver.find_element(By.XPATH, var_app.driver_info_date_of_birth).click()
        time.sleep(1.5)
        var_app.driver.find_element(By.XPATH, var_app.IGREE).click()
        time.sleep(1.5)

        var_app.driver.find_element(By.XPATH, var_app.driver_info_sex).click()
        time.sleep(1.5)
        var_app.driver.tap([(57, 364)])
        time.sleep(1.5)
        var_app.driver.find_element(By.XPATH, var_app.driver_info_number_cccd).send_keys(var_app.data['utilities']['fill_vehicle_cccd']  + random_number)
        var_app.driver.find_element(By.XPATH, var_app.driver_info_number_phone).send_keys(var_app.data['utilities']['fill_vehicle_phone'] + random_number)
        var_app.driver.find_element(By.XPATH, var_app.driver_info_adress).send_keys(var_app.data['utilities']['fill_vehicle_address'])
        var_app.driver.swipe(430, 1370, 430, 568, 500)

        var_app.driver.find_element(By.XPATH, var_app.driver_info_vehicle).click()
        time.sleep(1.5)
        var_app.driver.tap([(210, 360)])
        time.sleep(1.5)
        var_app.driver.find_element(By.XPATH, var_app.driver_info_type_liscense).click()
        time.sleep(1.5)
        var_app.driver.tap([(131, 366)])
        time.sleep(1.5)
        var_app.driver.find_element(By.XPATH, var_app.driver_info_number_liscense).send_keys(var_app.data['utilities']['fill_vehicle_number_liscense'] + random_number)
        var_app.driver.find_element(By.XPATH, var_app.driver_info_release_date).click()
        time.sleep(1.5)
        var_app.driver.find_element(By.XPATH, var_app.IGREE).click()
        time.sleep(1.5)

        var_app.driver.find_element(By.XPATH, var_app.driver_info_expiration_date).click()
        time.sleep(1.5)
        var_app.driver.find_element(By.XPATH, var_app.IGREE).click()
        time.sleep(1.5)
        var_app.driver.find_element(By.XPATH, var_app.SAVE).click()
        time.sleep(2)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Thêm lái xe",
                                              var_app.check_add_driver_fill_info, "Thêm lái xe thành công", "_TrangChu_ThemLaiXe_Luu.png")

        general.utilities_back(self)









    def list_driver_search(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_list_driver)
        except:
            general.utilities_back(self)
            move_module1(self, "", "", "", var_app.list_driver, 725, 1100, 175, 1100, 500, "", "", "", "")

        var_app.driver.find_element(By.XPATH, var_app.list_driver_search_input).send_keys(var_app.data['utilities']['list_driver_search'])
        time.sleep(1.5)
        var_app.driver.tap([(230, 341)])
        time.sleep(2)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Ẩn hiện xe",
                                              var_app.check_list_driver_search, var_app.data['utilities']['list_driver_search'], "_TrangChu_DanhSachLaiXe_TimKiem.png")

        try:
            var_app.driver.find_element(By.XPATH, var_app.see_info_vehicle_back).click()
            time.sleep(1.3)
        except:
            pass


    def list_driver_select_vehicle(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_list_driver)
        except:
            general.utilities_back(self)
            move_module1(self, "", "", "", var_app.list_driver, 725, 1100, 175, 1100, 500, "", "", "", "")

        var_app.driver.tap([(230, 341)])
        time.sleep(2)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Ẩn hiện xe",
                                              var_app.check_list_driver_select_vehicle, "XEM THÔNG TIN LÁI XE", "_TrangChu_DanhSachLaiXe_CickVaoXe.png")


    def list_driver_check_info(self, code, eventname, result, path_detail, path_image):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_list_driver_select_vehicle)
        except:
            utilities.list_driver_select_vehicle(self, "", "", "")

        var_app.driver.swipe(450, 1400, 450, 550, 500)
        module_other_app.write_result_text_try_if_other(code, eventname, result, "Trang chủ - Danh sách lái xe",
                                              path_detail, "", path_image)


        if path_image == "_TrangChu_DanhSachPhuongTien_NgayHetHan.png":
            try:
                var_app.driver.find_element(By.XPATH, var_app.see_info_vehicle_back).click()
                time.sleep(1.3)
            except:
                pass


    def list_driver_icon_add(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_list_driver)
        except:
            general.utilities_back(self)
            move_module1(self, "", "", "", var_app.list_driver, 725, 1100, 175, 1100, 500, "", "", "", "")

        var_app.driver.find_element(By.XPATH, var_app.list_driver_icon_add).click()
        time.sleep(2)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Ẩn hiện xe",
                                              var_app.check_list_driver_icon_add, "NHẬP THÔNG TIN LÁI XE", "_TrangChu_DanhSachLaiXe_IconThemLaiXe.png")

        general.utilities_back(self)








    def info_fee_vehicle_owes_fees(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_info_fee)
        except:
            general.utilities_back(self)
            move_module1(self, "", "", "", var_app.info_fee, 725, 1100, 175, 1100, 500, "", "", "", "")

        var_app.driver.find_element(By.XPATH, var_app.info_fee_vehicle_owes_fees).click()
        time.sleep(0.5)
        module_other_app.write_result_text_try_if_other(code, eventname, result, "Trang chủ - Thông tin phí",
                                              var_app.check_info_fee_vehicle_owes_fees, "", "_TrangChu_ThongTinPhi_PhuongTienNoPhi.png")


    def info_fee_search_fee(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_info_fee)
        except:
            general.utilities_back(self)
            move_module1(self, "", "", "", var_app.info_fee, 725, 1100, 175, 1100, 500, "", "", "", "")

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
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_info_fee)
        except:
            general.utilities_back(self)
            move_module1(self, "", "", "", var_app.info_fee, 725, 1100, 175, 1100, 500, "", "", "", "")

        var_app.driver.find_element(By.XPATH, var_app.info_fee_iconbagps).click()
        time.sleep(1)

        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Thông tin phí",
                                              var_app.check_info_fee_iconbagps, "BA GPS", "_TrangChu_ThongTinPhi_IconGps.png")

        try:
            var_app.driver.find_element(By.XPATH, var_app.IGREE).click()
            time.sleep(1.3)
        except:
            pass
        general.utilities_back(self)








    def support_customer_list_support(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_support_customer)
        except:
            general.utilities_back(self)
            move_module1(self, "", "", "", var_app.support_customer, 725, 1100, 175, 1100, 500, "", "", "", "")


        var_app.driver.swipe(400, 1400, 400, 700, 500)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Hỗ trợ khách hàng",
                                              var_app.check_support_customer_list_support, "Tiện ích nhanh", "_TrangChu_HoTroKhachHang_DanhMucHoTro.png")


    def support_customer_track_feedback(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_support_customer)
        except:
            general.utilities_back(self)
            move_module1(self, "", "", "", var_app.support_customer, 725, 1100, 175, 1100, 500, "", "", "", "")

        var_app.driver.find_element(By.XPATH, var_app.support_customer_track_feedback).click()
        time.sleep(1)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Hỗ trợ khách hàng",
                                              var_app.check_support_customer_track_feedback, "Tìm kiếm phản hồi", "_TrangChu_HoTroKhachHang_TheoDoiPhanHoi.png")
        general.utilities_back(self)








    def transmission_report_search(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_transmission_report)
        except:
            general.utilities_back(self)
            move_module1(self, "", "", "", var_app.transmission_report, 725, 1100, 175, 1100, 500, "", "", "", "")

        var_app.driver.find_element(By.XPATH, var_app.transmission_report_search_input).send_keys(var_app.data['utilities']['transmission_warning_search'])
        time.sleep(1.5)
        var_app.driver.tap([(858, 492)])
        time.sleep(2)
        module_other_app.write_result_text_try_if_other(code, eventname, result, "Trang chủ - Cảnh báo tích truyền",
                                              var_app.check_transmission_report_search, "", "_TrangChu_CanhBaoTichTruyen_TimKiem.png")

        try:
            var_app.driver.find_element(By.XPATH, var_app.transmission_report_search_back).click()
            time.sleep(1.3)
        except:
            pass


    def transmission_report_select_vehicle(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_transmission_report)
        except:
            general.utilities_back(self)
            move_module1(self, "", "", "", var_app.transmission_report, 725, 1100, 175, 1100, 500, "", "", "", "")

        var_app.driver.tap([(858, 492)])
        time.sleep(2)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Cảnh báo tích truyền",
                                              var_app.check_transmission_report_select_vehicle, "NHẬP THÔNG TIN XE", "_TrangChu_CanhBaoTichTruyen_ClickVaoXe.png")

        try:
            var_app.driver.find_element(By.XPATH, var_app.transmission_report_search_back).click()
            time.sleep(1.3)
        except:
            pass


    def transmission_report_checkbox(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_transmission_report)
        except:
            general.utilities_back(self)
            move_module1(self, "", "", "", var_app.transmission_report, 725, 1100, 175, 1100, 500, "", "", "", "")

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
            var_app.driver.find_element(By.XPATH, var_app.IGREE).click()
            time.sleep(1.3)
        except:
            pass
        general.utilities_back(self)










    def record_driver_card_fill_info(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_record_driver_card)
        except:
            general.utilities_back(self)
            move_module1(self, "", "", "", var_app.record_driver_card, 725, 1100, 175, 1100, 500, "", "", "", "")

        var_app.driver.find_element(By.XPATH, var_app.record_driver_card_fill_info_vehicle).click()
        time.sleep(1.5)
        var_app.driver.tap([(185, 365)])
        time.sleep(1.5)
        var_app.driver.find_element(By.XPATH, var_app.record_driver_card_fill_info_name_driver).click()
        time.sleep(1.5)
        var_app.driver.tap([(215, 360)])
        time.sleep(1.5)
        var_app.driver.find_element(By.XPATH, var_app.record_driver_card_fill_info).click()
        time.sleep(2)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Ghi thẻ lái xe",
                                              var_app.check_record_driver_card_fill_info, "Thiết bị không online", "_TrangChu_GhiTheLaiXe_GhiThe.png")


    def record_driver_card_help(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_record_driver_card)
        except:
            general.utilities_back(self)
            move_module1(self, "", "", "", var_app.record_driver_card, 725, 1100, 175, 1100, 500, "", "", "", "")

        var_app.driver.find_element(By.XPATH, var_app.record_driver_card_help).click()
        time.sleep(1.5)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Ghi thẻ lái xe",
                                              var_app.check_record_driver_card_help, "1. Đối với đầu đọc thẻ BARD: Đưa thẻ lại gần tem mặt trước của đầu đọc thẻ", "_TrangChu_GhiTheLaiXe_HuongDan.png")


    def record_driver_card_icon(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_record_driver_card)
        except:
            general.utilities_back(self)
            move_module1(self, "", "", "", var_app.record_driver_card, 725, 1100, 175, 1100, 500, "", "", "", "")

        var_app.driver.find_element(By.XPATH, var_app.record_driver_card_icon).click()
        time.sleep(1.5)
        module_other_app.write_result_text_try_if_other(code, eventname, result, "Trang chủ - Ghi thẻ lái xe",
                                              var_app.check_record_driver_card_icon, "", "_TrangChu_GhiTheLaiXe_IconLichSuGhiThe.png")
        general.utilities_back(self)













