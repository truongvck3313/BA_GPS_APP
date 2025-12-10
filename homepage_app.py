import time
from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException
import re
import login_app
import var_app
import module_other_app
import minitor_app
import requests
import json
from retry import retry
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By












def goto_cty(xncode):
    var_app.driver.implicitly_wait(2)
    var_app.driver.find_element(By.XPATH, var_app.homepage).click()
    time.sleep(1)
    var_app.driver.find_element(By.XPATH, var_app.icon_goto_cty).click()
    time.sleep(2)
    var_app.driver.find_element(By.XPATH, var_app.icon_goto_cty_input).send_keys(xncode)
    var_app.driver.find_element(By.XPATH, var_app.goto_cty).click()
    time.sleep(2)
    module_other_app.tap_scaled(var_app.driver, [(860, 355)])
    time.sleep(0.5)
    module_other_app.tap_scaled(var_app.driver, [(857, 376)])
    time.sleep(3)


def move_module(self, code, eventname, result, link, startX, startY, endX, endY, duration,
                path_module, path_check, desire, path_image):
    var_app.driver.implicitly_wait(2)
    login_app.login.login_v3(self, var_app.data['login']['conhom_quantri_tk'], var_app.data['login']['conhom_quantri_mk'])
    var_app.driver.find_element(By.XPATH, var_app.homepage).click()
    time.sleep(2)
    try:
        var_app.driver.find_element(By.XPATH, var_app.homepage).click()
        time.sleep(1.5)
    except:
        pass

    minitor_app.scroll_and_click_precent(startX, startY, endX, endY, duration, link)


    try:
        wait = WebDriverWait(var_app.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, path_check)))
    except:
        pass

    module_other_app.write_result_text_try_if(code, eventname, result, path_module,
                                              path_check, desire, path_image)


def move_module1(self, code, eventname, result, link, startX, startY, endX, endY, duration,
                path_module, path_check, desire, path_image, check_user, user, password):
    var_app.driver.implicitly_wait(2)
    login_app.login.login_v3(self, user, password)
    var_app.driver.find_element(By.XPATH, var_app.homepage).click()
    time.sleep(2)
    try:
        var_app.driver.find_element(By.XPATH, var_app.homepage).click()
        time.sleep(1.5)
    except:
        pass

    minitor_app.scroll_and_click_precent(startX, startY, endX, endY, duration, link)

    module_other_app.write_result_text_try_if(code, eventname, result, path_module,
                                              path_check, desire, path_image)



def move_module2(self, code, eventname, result, link, startX, startY, endX, endY, duration,
                path_module, path_check, desire, path_image):
    var_app.driver.implicitly_wait(2)
    login_app.login.login_v3(self, var_app.data['login']['conhom_quantri_tk3'], var_app.data['login']['conhom_quantri_mk3'])
    var_app.driver.find_element(By.XPATH, var_app.homepage).click()
    time.sleep(2)
    try:
        var_app.driver.find_element(By.XPATH, var_app.homepage).click()
        time.sleep(1.5)
    except:
        pass

    minitor_app.scroll_and_click_precent(startX, startY, endX, endY, duration, link)

    module_other_app.write_result_text_try_if(code, eventname, result, path_module,
                                              path_check, desire, path_image)

def toolbar_back():
    var_app.driver.implicitly_wait(0.15)
    try:
        var_app.driver.find_element(By.XPATH, var_app.toolbar_back1).click()
        time.sleep(1.2)
    except:
        pass
    try:
        var_app.driver.find_element(By.XPATH, var_app.toolbar_back2).click()
        time.sleep(1.2)
    except:
        pass
    try:
        var_app.driver.find_element(By.XPATH, var_app.toolbar_back3).click()
        time.sleep(1.2)
    except:
        pass
    try:
        var_app.driver.find_element(By.XPATH, var_app.toolbar_back4).click()
        time.sleep(1.2)
    except:
        pass
    try:
        var_app.driver.find_element(By.XPATH, var_app.toolbar_back5).click()
        time.sleep(1.2)
    except:
        pass
    try:
        var_app.driver.find_element(By.XPATH, var_app.toolbar_back6).click()
        time.sleep(1.2)
    except:
        pass
    try:
        var_app.driver.find_element(By.XPATH, var_app.toolbar_back7).click()
        time.sleep(1.2)
    except:
        pass
    try:
        var_app.driver.find_element(By.XPATH, var_app.toolbar_back8).click()
        time.sleep(1.2)
    except:
        pass
    try:
        var_app.driver.find_element(By.XPATH, var_app.toolbar_back9).click()
        time.sleep(1.2)
    except:
        pass
    try:
        var_app.driver.find_element(By.XPATH, var_app.toolbar_back10).click()
        time.sleep(1.2)
    except:
        pass
    try:
        var_app.driver.find_element(By.XPATH, var_app.toolbar_back11).click()
        time.sleep(1.2)
    except:
        pass




class toolbar:

    def utility_list(self, code, eventname, result):
        var_app.driver.implicitly_wait(2)
        login_app.login.login_v3(self, var_app.data['login']['conhom_quantri_tk'], var_app.data['login']['conhom_quantri_mk'])
        try:
            var_app.driver.find_element(By.XPATH, var_app.homepage).click()
            time.sleep(2)
        except:
            pass
        try:
            var_app.driver.find_element(By.XPATH, var_app.homepage).click()
            time.sleep(1.5)
        except:
            pass
        var_app.driver.find_element(By.XPATH, var_app.utility_list).click()
        time.sleep(2)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang Chủ - Thanh công cụ - Tìm kiếm danh mục",
                                              var_app.check_opeutility_list, "TÌM KIẾM DANH MỤC", "_TrangChu_TimKiemDanhMuc.png")


    def utility_list_search(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.utility_list_search_input)
        except:
            toolbar.utility_list(self, "Toolbar01", eventname, result)

        var_app.driver.find_element(By.XPATH, var_app.utility_list_search_input).send_keys(var_app.data['home_page']['search_category'])
        time.sleep(2)
        module_other_app.tap_scaled(var_app.driver, [(160, 330)])
        time.sleep(2.5)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang Chủ - Thanh công cụ - Tìm kiếm danh mục",
                                              var_app.check_list_driver, "DANH SÁCH LÁI XE", "_TrangChu_TimKiemDanhMuc_TimKiem.png")


        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.utility_list_search_iconx).click()
            time.sleep(1.5)
        except:
            pass

        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.utility_list_search_iconx1).click()
            time.sleep(1.5)
        except:
            pass


    def notification(self, code, eventname, result):
        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        login_app.login.login_v3(self, var_app.data['login']['conhom_quantri_tk'], var_app.data['login']['conhom_quantri_mk'])
        var_app.driver.find_element(By.XPATH, var_app.homepage).click()
        time.sleep(2)
        try:
            var_app.driver.find_element(By.XPATH, var_app.homepage).click()
            time.sleep(1.5)
        except:
            pass
        var_app.driver.find_element(By.XPATH, var_app.notification).click()
        time.sleep(2.5)
        var_app.driver.find_element(By.XPATH, var_app.notification_system).click()
        time.sleep(2.5)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang Chủ - Thanh công cụ - Thông báo",
                                              var_app.check_notification, "THÔNG BÁO", "_TrangChu_ThongBao.png")


    def see_notification(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.check_notification)
        except:
            toolbar.notification(self, "Toolbar03", eventname, result)

        module_other_app.tap_scaled(var_app.driver, [(300, 250)])
        time.sleep(3)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang Chủ - Thanh công cụ - Thông báo",
                                              var_app.check_see_notification, "CHI TIẾT THÔNG BÁO", "_TrangChu_ThongBao_XemThongBao.png")


        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.see_notification_iconback).click()
            time.sleep(1.5)
        except:
            pass


    def delete_notification(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.check_notification)
        except:
            toolbar.notification(self, "Toolbar03", eventname, result)

        time.sleep(1)
        var_app.driver.find_element(By.XPATH, var_app.delete_notification).click()
        time.sleep(2)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang Chủ - Thanh công cụ - Thông báo",
                                              var_app.check_delete_notification, "Bạn chắc chắn xóa tất cả thông báo?", "_TrangChu_ThongBao_XoaThongBao.png")

        var_app.driver.find_element(By.XPATH, var_app.delete_notification_cancel).click()
        time.sleep(1.2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.notification_back).click()
            time.sleep(1.5)
        except:
            pass
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.notification_back1).click()
            time.sleep(1.5)
        except:
            pass





    def warning_list(self, code, eventname, result):
        login_app.login.login_v3(self, var_app.data['login']['binhanh_tk'], var_app.data['login']['binhanh_mk'])

        var_app.driver.implicitly_wait(2)
        var_app.driver.find_element(By.XPATH, var_app.homepage).click()
        time.sleep(2)
        try:
            var_app.driver.find_element(By.XPATH, var_app.homepage).click()
            time.sleep(1.5)
        except:
            pass
        goto_cty("2929_6")
        time.sleep(5)
        var_app.driver.find_element(By.XPATH, var_app.warning_list).click()
        time.sleep(2)
        try:
            wait = WebDriverWait(var_app.driver, 10)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_app.check_warning_list1)))
        except:
            pass
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang Chủ - Thanh công cụ - Danh sách cảnh báo",
                                              var_app.check_warning_list1, "DANH SÁCH CẢNH BÁO", "_TrangChu_DanhSachCanhBao.png")


    def warning_list_search(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.type_warning)
        except:
            toolbar.warning_list(self, "Toolbar06", eventname, result)


        var_app.driver.find_element(By.XPATH, var_app.type_warning).click()
        time.sleep(1.5)
        module_other_app.tap_scaled(var_app.driver, [(82, 365)])
        time.sleep(1.5)

        var_app.driver.find_element(By.XPATH, var_app.warning_list_iconsearch).click()
        time.sleep(2)
        module_other_app.tap_scaled(var_app.driver, [(260, 470)])
        time.sleep(2)
        try:
            check_data = var_app.driver.find_element(By.XPATH, var_app.check_warning_list_search_name3).text
            name_warn = var_app.driver.find_element(By.XPATH, var_app.check_warning_list_search_name4).text
            conten_warn = var_app.driver.find_element(By.XPATH, var_app.check_warning_list_search_name5).text
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, "Phương tiện: {}\nCảnh báo: {}\nNội dung cảnh báo: {}".format(check_data, name_warn, conten_warn))
        except:
            pass
        module_other_app.write_result_displayed_try(code, eventname, result, "Trang Chủ - Thanh công cụ - Danh sách cảnh báo",
                                                var_app.check_warning_list_search_name3, "_TrangChu_DanhSachCanhBao_TimKiem.png")

        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.warning_list_back).click()
            time.sleep(1.3)
        except:
            pass


    def warning_list_mark_as_read(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.type_warning)
        except:
            toolbar.warning_list(self, "Toolbar06", eventname, result)


        var_app.driver.find_element(By.XPATH, var_app.warning_list_mark_as_read).click()
        time.sleep(1.5)

        module_other_app.write_result_text_try_if(code, eventname, result, "Trang Chủ - Thanh công cụ - Danh sách cảnh báo",
                                              var_app.check_hwarning_list_mark_as_read, "Bạn chắc chắn muốn chuyển tất cả cảnh báo thành đã đọc?", "_TrangChu_DanhSachCanhBao_DanhDauLaDaDoc.png")

        var_app.driver.find_element(By.XPATH, var_app.IGREE).click()
        time.sleep(1.5)

        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.warning_list_back1).click()
            time.sleep(1.2)
        except:
            pass













    def support_customer(self, code, eventname, result):
        login_app.login.login_v3(self, var_app.data['login']['pnc_tk'], var_app.data['login']['pnc_mk'])

        var_app.driver.implicitly_wait(2)
        var_app.driver.find_element(By.XPATH, var_app.homepage).click()
        time.sleep(2)
        try:
            var_app.driver.find_element(By.XPATH, var_app.homepage).click()
            time.sleep(1.5)
        except:
            pass

        var_app.driver.find_element(By.XPATH, var_app.icon_search3).click()
        time.sleep(2.5)
        var_app.driver.find_element(By.XPATH, var_app.search_list_input).clear()
        time.sleep(0.5)
        var_app.driver.find_element(By.XPATH, var_app.search_list_input).send_keys("Hỗ trợ khách hàng")
        time.sleep(2)
        try:
            var_app.driver.find_element(By.XPATH, var_app.search_list_support_customer).click()
        except:
            module_other_app.tap_scaled(var_app.driver, [(142, 327)])

        # var_app.driver.find_element(By.XPATH, var_app.icon_support_customer).click()
        time.sleep(2.5)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang Chủ - Thanh công cụ - Hỗ trợ khách hàng",
                                              var_app.check_icon_support_customer, "HỖ TRỢ KHÁCH HÀNG", "_TrangChu_HoTroKhachHang_.png")


    def support_support(self, code, eventname, result, button):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass
        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_icon_support_customer)
        except:
            toolbar.support_customer(self, "", "", "")

        var_app.driver.find_element(By.XPATH, var_app.support).click()
        time.sleep(1.5)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang Chủ - Thanh công cụ - Hỗ trợ khách hàng",
                                              var_app.select_customer, "Chọn hỗ trợ", "_HoTroKhachHang_HoTro.png")


        try:
            var_app.driver.find_element(By.XPATH, button).click()
        except:
            module_other_app.swipe_scaled(var_app.driver, 772, 378, 126, 369, 1000)
            time.sleep(2)
            try:
                var_app.driver.find_element(By.XPATH, button).click()
            except:
                module_other_app.swipe_scaled(var_app.driver, 126, 369, 772, 378, 1000)
                time.sleep(2)
                var_app.driver.find_element(By.XPATH, button).click()
        time.sleep(2)


    def support_support_button_defaut(self, code, eventname, result, button, name_image):
        var_app.driver.implicitly_wait(5)
        toolbar.support_support(self, "", "", "", button)

        var_app.logging.info("--------------")
        var_app.logging.info("Hỗ trợ khách hàng - Hỗ trợ")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        try:
            vehicle = var_app.driver.find_element(By.XPATH, var_app.support_vehicle).text
            phone = var_app.driver.find_element(By.XPATH, var_app.support_phone).text
            note = var_app.driver.find_element(By.XPATH, var_app.support_note).text
            image = var_app.driver.find_element(By.XPATH, var_app.support_image).text
            SEND_SUPPORT = var_app.driver.find_element(By.XPATH, var_app.SEND_SUPPORT).text

            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, f"{vehicle}, {phone}, {note}, {image}, {SEND_SUPPORT}")
            var_app.logging.info(f"{vehicle}, {phone}, {note}, {image}, {SEND_SUPPORT}")

            if (vehicle == "Phương tiện") and (phone == "Số điện thoại") and (note == "Ghi chú") and ("Thêm hình ảnh" in image) and (SEND_SUPPORT == "GỬI HỖ TRỢ"):
                var_app.logging.info("True")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Pass")
            else:
                var_app.logging.info("False")
                var_app.driver.save_screenshot(var_app.imagepath + code + name_image)
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Fail")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 13, code + name_image)
        except:
            var_app.logging.info("False")
            var_app.driver.save_screenshot(var_app.imagepath + code + name_image)
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Fail")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 13, code + name_image)


    def support_support_button_lost_signal(self, code, eventname, result):
        var_app.driver.implicitly_wait(5)
        toolbar.support_support(self, "", "", "", var_app.lost_signal)

        var_app.logging.info("--------------")
        var_app.logging.info("Hỗ trợ khách hàng - Hỗ trợ")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        try:
            vehicle = var_app.driver.find_element(By.XPATH, var_app.support_vehicle).text
            checkbox1 = var_app.driver.find_element(By.XPATH, var_app.support_checkbox1).text
            checkbox2 = var_app.driver.find_element(By.XPATH, var_app.support_checkbox2).text

            phone = var_app.driver.find_element(By.XPATH, var_app.support_phone).text
            note = var_app.driver.find_element(By.XPATH, var_app.support_note).text
            image = var_app.driver.find_element(By.XPATH, var_app.support_image1).text
            SEND_SUPPORT = var_app.driver.find_element(By.XPATH, var_app.SEND_SUPPORT).text

            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, f"{vehicle}, {checkbox1}, {checkbox2}, {phone}, {note}, {image}, {SEND_SUPPORT}")
            var_app.logging.info(f"{vehicle}, {phone}, {note}, {image}, {SEND_SUPPORT}")

            if (vehicle == "Phương tiện") and (checkbox1 == "Xe đang sửa chữa, ngắt mát ?") and (checkbox2 == "Xe đang ở dưới hầm ? ") and (phone == "Số điện thoại") \
                    and (note == "Ghi chú") and ("Thêm hình ảnh" in image) and (SEND_SUPPORT == "GỬI HỖ TRỢ"):
                var_app.logging.info("True")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Pass")
            else:
                var_app.logging.info("False")
                var_app.driver.save_screenshot(var_app.imagepath + code + "_HoTroKhachHang_MatTinHieu.png")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Fail")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 13, code + "_HoTroKhachHang_MatTinHieu.png")
        except:
            var_app.logging.info("False")
            var_app.driver.save_screenshot(var_app.imagepath + code + "_HoTroKhachHang_MatTinHieu.png")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Fail")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 13, code + "_HoTroKhachHang_MatTinHieu.png")


    def support_support_button_change_license_plate(self, code, eventname, result):
        var_app.driver.implicitly_wait(5)
        toolbar.support_support(self, "", "", "", var_app.change_license_plate)

        module_other_app.swipe_scaled(var_app.driver, 500, 1200, 500, 600, 1000)
        time.sleep(1)
        var_app.logging.info("--------------")
        var_app.logging.info("Hỗ trợ khách hàng - Hỗ trợ")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        try:
            vehicle = var_app.driver.find_element(By.XPATH, var_app.support_vehicle).text
            change_license_plate_new = var_app.driver.find_element(By.XPATH, var_app.change_license_plate_new).text
            phone = var_app.driver.find_element(By.XPATH, var_app.support_phone).text
            note = var_app.driver.find_element(By.XPATH, var_app.support_note).text
            image = var_app.driver.find_element(By.XPATH, var_app.support_image2).text
            SEND_SUPPORT = var_app.driver.find_element(By.XPATH, var_app.SEND_SUPPORT).text

            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, f"{vehicle}, {phone}, {note}, {image}, {SEND_SUPPORT}")
            var_app.logging.info(f"{vehicle}, {phone}, {note}, {image}, {SEND_SUPPORT}")

            if (vehicle == "Phương tiện") and (change_license_plate_new == "Biển kiểm soát mới") and (phone == "Số điện thoại") \
                    and (note == "Ghi chú") and ("Thêm hình ảnh" in image) and (SEND_SUPPORT == "GỬI HỖ TRỢ"):
                var_app.logging.info("True")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Pass")
            else:
                var_app.logging.info("False")
                var_app.driver.save_screenshot(var_app.imagepath + code + "_HoTroKhachHang_DoiBien.png")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Fail")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 13, code + "_HoTroKhachHang_DoiBien.png")
        except:
            var_app.logging.info("False")
            var_app.driver.save_screenshot(var_app.imagepath + code + "_HoTroKhachHang_DoiBien.png")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Fail")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 13, code + "_HoTroKhachHang_DoiBien.png")
        module_other_app.swipe_scaled(var_app.driver, 500, 600, 500, 1200, 1000)
        time.sleep(1)


    def support_support_button_error_camera(self, code, eventname, result):
        var_app.driver.implicitly_wait(5)
        toolbar.support_support(self, "", "", "", var_app.error_camera)

        var_app.logging.info("--------------")
        var_app.logging.info("Hỗ trợ khách hàng - Hỗ trợ")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        try:
            vehicle = var_app.driver.find_element(By.XPATH, var_app.support_vehicle).text
            checkbox1 = var_app.driver.find_element(By.XPATH, var_app.support_checkbox1).text
            checkbox2 = var_app.driver.find_element(By.XPATH, var_app.support_checkbox2).text

            phone = var_app.driver.find_element(By.XPATH, var_app.support_phone).text
            note = var_app.driver.find_element(By.XPATH, var_app.support_note).text
            image = var_app.driver.find_element(By.XPATH, var_app.support_image1).text
            SEND_SUPPORT = var_app.driver.find_element(By.XPATH, var_app.SEND_SUPPORT).text

            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, f"{vehicle}, {checkbox1}, {checkbox2}, {phone}, {note}, {image}, {SEND_SUPPORT}")
            var_app.logging.info(f"{vehicle}, {phone}, {note}, {image}, {SEND_SUPPORT}")

            if (vehicle == "Phương tiện") and (checkbox1 == "Camera mờ, bị che ?") and (checkbox2 == "Đèn ở đầu ghi không sáng , led trên taplo có màu đỏ ?") and (phone == "Số điện thoại") \
                    and (note == "Ghi chú") and ("Thêm hình ảnh" in image) and (SEND_SUPPORT == "GỬI HỖ TRỢ"):
                var_app.logging.info("True")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Pass")
            else:
                var_app.logging.info("False")
                var_app.driver.save_screenshot(var_app.imagepath + code + "_HoTroKhachHang_MatTinHieu.png")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Fail")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 13, code + "_HoTroKhachHang_MatTinHieu.png")
        except:
            var_app.logging.info("False")
            var_app.driver.save_screenshot(var_app.imagepath + code + "_HoTroKhachHang_MatTinHieu.png")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Fail")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 13, code + "_HoTroKhachHang_MatTinHieu.png")


    def support_send_info(self, code, eventname, result):
        var_app.driver.implicitly_wait(5)
        toolbar.support_support(self, "", "", "", var_app.dong_feee)


        var_app.driver.find_element(By.XPATH, var_app.send_info_vehicle).click()
        time.sleep(2.5)
        var_app.driver.find_element(By.XPATH, var_app.send_info_vehicle_all).click()
        time.sleep(1)
        var_app.driver.find_element(By.XPATH, var_app.send_info_vehicle_all).click()
        time.sleep(1)

        var_app.driver.find_element(By.XPATH, var_app.suport_select_vehicle_input).clear()
        time.sleep(0.5)
        var_app.driver.find_element(By.XPATH, var_app.suport_select_vehicle_input).send_keys("30A12345_C")
        time.sleep(2)
        try:
            var_app.driver.find_element(By.XPATH, var_app.send_info_vehicle1).click()
        except:
            module_other_app.tap_scaled(var_app.driver, [(179, 493)])
        time.sleep(1)

        var_app.driver.find_element(By.XPATH, var_app.SELECT).click()
        time.sleep(2)

        var_app.driver.find_element(By.XPATH, var_app.send_info_phone).clear()
        time.sleep(0.5)
        var_app.driver.find_element(By.XPATH, var_app.send_info_phone).send_keys("0359667452")
        time.sleep(0.5)

        var_app.driver.find_element(By.XPATH, var_app.send_info_note).clear()
        time.sleep(0.5)
        var_app.driver.find_element(By.XPATH, var_app.send_info_note).send_keys("Phòng QA test. Nhờ PDV đóng phiếu hộ")
        time.sleep(0.5)

        # try:
        #     var_app.driver.find_element(By.XPATH, var_app.support_image).click()
        # except:
        #     var_app.driver.find_element(By.XPATH, var_app.support_image3).click()
        #
        # time.sleep(2)
        # var_app.driver.find_element(By.XPATH, var_app.CHONANHCOSAN).click()
        # time.sleep(3)
        # var_app.driver.find_element(By.XPATH, var_app.CHONANHCOSAN1).click()
        # time.sleep(2)
        # var_app.driver.find_element(By.XPATH, var_app.support_image_x).click()
        # time.sleep(2)
        # var_app.driver.find_element(By.XPATH, var_app.IGREE).click()
        # time.sleep(2)

        var_app.driver.find_element(By.XPATH, var_app.SEND_SUPPORT).click()
        time.sleep(2)
        var_app.driver.find_element(By.XPATH, var_app.IGREE).click()
        time.sleep(2)
        try:
            wait = WebDriverWait(var_app.driver, 10)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_app.check_support_send_info)))
        except:
            pass
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang Chủ - Thanh công cụ - Hỗ trợ khách hàng",
                                              var_app.check_support_send_info, "Gửi yêu cầu hỗ trợ thành công", "_HoTroKhachHang_GuiHoTro.png")










    def support_utilities(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass
        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_icon_support_customer)
        except:
            toolbar.support_customer(self, "", "", "")

        var_app.driver.find_element(By.XPATH, var_app.utilities).click()
        time.sleep(1.5)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang Chủ - Thanh công cụ - Tin ích",
                                              var_app.clock_vehicle, "Khóa xe", "_HoTroKhachHang_TienIch.png")


    def support_utilities_link(self, code, eventname, result, type, button, iconx, path_check, desire, path_image):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass
        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_icon_support_customer)
            var_app.driver.find_element(By.XPATH, var_app.clock_vehicle)
        except:
            toolbar.support_utilities(self, "", "", "")


        if type == "0":
            module_other_app.write_result_text_try_if(code, eventname, result, "Thanh công cụ - Tiện ích",
                                                  path_check, desire, path_image)

        if type == "1":
            var_app.driver.find_element(By.XPATH, button).click()
            time.sleep(1)

            wait = WebDriverWait(var_app.driver, 10)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, path_check)))
            module_other_app.write_result_text_try_if(code, eventname, result, "Thanh công cụ - Tiện ích",
                                                  path_check, desire, path_image)

            var_app.driver.find_element(By.XPATH, iconx).click()
            time.sleep(2.5)


    def support_follow(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass
        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_icon_support_customer)
        except:
            toolbar.support_customer(self, "", "", "")

        var_app.driver.find_element(By.XPATH, var_app.follow).click()
        time.sleep(2)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang Chủ - Thanh công cụ - Theo dõi",
                                              var_app.pending_processing, "Chờ xử lý", "_HoTroKhachHang_Theo dõi.png")


    def support_customer_track_feedback(self, code, eventname, result, status_support, check_quantity):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass
        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.find_element(By.XPATH, var_app.pending_processing)
        except:
            toolbar.support_follow(self, "", "", "")
        time.sleep(1.5)
        var_app.driver.find_element(By.XPATH, status_support).click()
        time.sleep(1)
        var_app.logging.info("--------------")
        var_app.logging.info("Trang Chủ - Thanh công cụ - Hỗ trợ khách hàng - Theo dõi phản hồi")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("True")
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Pass")


        try:
            var_app.driver.implicitly_wait(1)
            check_quantity1 = var_app.driver.find_element(By.XPATH, check_quantity).text
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, "Số lượng phản hồi: {}".format(check_quantity1))
        except:
            pass


    def support_customer_track_complete(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass
        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.find_element(By.XPATH, var_app.pending_processing)
        except:
            toolbar.support_follow(self, "", "", "")
        time.sleep(1.5)
        var_app.driver.find_element(By.XPATH, var_app.complete).click()
        time.sleep(1)
        var_app.logging.info("--------------")
        var_app.logging.info("Trang Chủ - Thanh công cụ - Hỗ trợ khách hàng - Theo dõi phản hồi")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("True")
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Pass")


    def support_customer_track_follow_search(self, code, eventname, result):
        var_app.driver.implicitly_wait(0.3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass
        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.find_element(By.XPATH, var_app.track_follow_search).click()
        except:
            toolbar.support_follow(self, "", "", "")
            var_app.driver.find_element(By.XPATH, var_app.track_follow_search).click()
        time.sleep(1.5)
        var_app.logging.info("--------------")
        var_app.logging.info("Trang Chủ - Thanh công cụ - Hỗ trợ khách hàng - Theo dõi phản hồi")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("True")
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Pass")


    def support_customer_track_follow_filter(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass
        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.find_element(By.XPATH, var_app.support_customer_track_follow_filter).click()
        except:
            toolbar.support_follow(self, "", "", "")
            var_app.driver.find_element(By.XPATH, var_app.support_customer_track_follow_filter).click()
        time.sleep(2)
        var_app.logging.info("--------------")
        var_app.logging.info("Trang Chủ - Thanh công cụ - Hỗ trợ khách hàng")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang Chủ - Thanh công cụ - Hỗ trợ khách hàng - Theo dõi phản hồi",
                                              var_app.check_support_customer_track_follow_filter, "BỘ LỌC TÌM KIẾM", "_TrangChu_HoTroKhachHang_BoLoc.png")

        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.support_customer_track_follow_filter_apply).click()
            time.sleep(1.5)
        except:
            pass

        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.support_customer_iconx1a).click()
            time.sleep(1.5)
        except:
            pass




    def support_customer_cancel(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass
        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.find_element(By.XPATH, var_app.pending_processing)
        except:
            toolbar.support_send_info(self, "", "", "")
        time.sleep(1.5)
        var_app.driver.find_element(By.XPATH, var_app.pending_processing).click()
        time.sleep(2)
        try:
            var_app.driver.find_element(By.XPATH, var_app.pending_processing1).click()#chọn bản ghi đầu
        except:
            module_other_app.tap_scaled(var_app.driver, [(50, 550)])
        time.sleep(2.5)
        var_app.driver.find_element(By.XPATH, var_app.CANCEL_REQUEST).click()
        time.sleep(2)
        var_app.driver.find_element(By.XPATH, var_app.IGREE).click()
        time.sleep(2)
        module_other_app.write_result_text_try_if(code, eventname, result, "Hỗ trợ khách hàng - Theo Dõi - Hủy yêu cầu",
                                              var_app.check_support_customer_cancel, "Hủy yêu cầu hỗ trợ thành công", "_HoTroKhachHang_TheoDoiHuyYeuCau.png")




    def shopping(self, code, eventname, result):
        login_app.login.login_v3(self, var_app.data['login']['khongnhom_quantri_tk'], var_app.data['login']['khongnhom_quantri_mk'])

        var_app.driver.implicitly_wait(2)
        var_app.driver.find_element(By.XPATH, var_app.homepage).click()
        time.sleep(2)
        try:
            var_app.driver.find_element(By.XPATH, var_app.homepage).click()
            time.sleep(1.5)
        except:
            pass
        var_app.driver.find_element(By.XPATH, var_app.icon_shopping).click()
        time.sleep(2.5)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang Chủ - Thanh công cụ - Mua hàng",
                                              var_app.SHOPPING, "MUA HÀNG", "_TrangChu_ThanhCongCu_MuaHang.png")

    def support_module4g(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass
        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.find_element(By.XPATH, var_app.SHOPPING)
        except:
            toolbar.shopping(self, "", "", "")

        var_app.driver.find_element(By.XPATH, var_app.shopping).click()
        time.sleep(1.5)
        var_app.driver.find_element(By.XPATH, var_app.upgrade_4g).click()
        time.sleep(1.5)
        module_other_app.swipe_scaled(var_app.driver, 450, 1150, 450, 600, 1000)
        time.sleep(1.5)

        var_app.logging.info("--------------")
        var_app.logging.info("Thanh công cụ - Mua hàng")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        try:
            text_note = var_app.driver.find_element(By.XPATH, var_app.text_note).text
            vehicle = var_app.driver.find_element(By.XPATH, var_app.shopping_vehicle).text
            phone = var_app.driver.find_element(By.XPATH, var_app.shopping_phone).text
            note = var_app.driver.find_element(By.XPATH, var_app.shopping_note).text
            image = var_app.driver.find_element(By.XPATH, var_app.shopping_image).text
            SEND_SUPPORT = var_app.driver.find_element(By.XPATH, var_app.SEND_SUPPORT).text

            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, f"{text_note}, {vehicle}, {phone}, {note}, {image}, {SEND_SUPPORT}")
            var_app.logging.info(f"{text_note}, {vehicle}, {phone}, {note}, {image}, {SEND_SUPPORT}")

            if (text_note == "HỖ TRỢ NÂNG CẤP THIẾT BỊ GSHT 2G VÀ 3G LÊN 4G") and (vehicle == "Phương tiện") and (phone == "Số điện thoại") and (note == "Ghi chú") \
                    and ("Thêm hình ảnh" in image) and (SEND_SUPPORT == "GỬI HỖ TRỢ"):
                var_app.logging.info("True")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Pass")
            else:
                var_app.logging.info("False")
                var_app.driver.save_screenshot(var_app.imagepath + code + "_MuaHang_NangCapModule4G.png")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Fail")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 13, code + "_MuaHang_NangCapModule4G.png")
        except:
            var_app.logging.info("False")
            var_app.driver.save_screenshot(var_app.imagepath + code + "_MuaHang_NangCapModule4G.png")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Fail")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 13, code + "_MuaHang_NangCapModule4G.png")

        module_other_app.swipe_scaled(var_app.driver, 450, 600, 450, 1150, 1000)
        time.sleep(1.5)

    def support_buy_a_driver_card(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass
        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.find_element(By.XPATH, var_app.SHOPPING)
        except:
            toolbar.shopping(self, "", "", "")

        var_app.driver.find_element(By.XPATH, var_app.shopping).click()
        time.sleep(1.5)
        var_app.driver.find_element(By.XPATH, var_app.buy_a_driver_card).click()
        time.sleep(1.5)
        module_other_app.swipe_scaled(var_app.driver, 450, 1150, 450, 600, 1000)
        time.sleep(1.5)

        var_app.logging.info("--------------")
        var_app.logging.info("Thanh công cụ - Mua hàng")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        try:
            number_card = var_app.driver.find_element(By.XPATH, var_app.number_card).text
            select_drive = var_app.driver.find_element(By.XPATH, var_app.select_drive).text
            delivery_address = var_app.driver.find_element(By.XPATH, var_app.delivery_address).text
            phone = var_app.driver.find_element(By.XPATH, var_app.phone).text
            note = var_app.driver.find_element(By.XPATH, var_app.note).text
            SEND_SUPPORT = var_app.driver.find_element(By.XPATH, var_app.SEND_SUPPORT).text

            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, f"{number_card}, {select_drive}, {delivery_address}, {phone}, {note}, {SEND_SUPPORT}")
            var_app.logging.info(f"{number_card}, {select_drive}, {delivery_address}, {phone}, {note}, {SEND_SUPPORT}")

            if (number_card == "Số lượng thẻ muốn mua") and (select_drive == "Chọn lái xe") and (delivery_address == "Địa chỉ nhận hàng") and (phone == "Số điện thoại") \
                    and (note == "Ghi chú") and (SEND_SUPPORT == "GỬI HỖ TRỢ"):
                var_app.logging.info("True")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Pass")
            else:
                var_app.logging.info("False")
                var_app.driver.save_screenshot(var_app.imagepath + code + "_MuaHang_MuaTheLaiXe.png")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Fail")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 13, code + "_MuaHang_MuaTheLaiXe.png")
        except:
            var_app.logging.info("False")
            var_app.driver.save_screenshot(var_app.imagepath + code + "_MuaHang_MuaTheLaiXe.png")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Fail")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 13, code + "_MuaHang_MuaTheLaiXe.png")

        module_other_app.swipe_scaled(var_app.driver, 450, 600, 450, 1150, 1000)
        time.sleep(1.5)

    def support_new_products(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass
        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.find_element(By.XPATH, var_app.SHOPPING)
        except:
            toolbar.shopping(self, "", "", "")

        var_app.driver.find_element(By.XPATH, var_app.shopping).click()
        time.sleep(1.5)
        var_app.driver.find_element(By.XPATH, var_app.new_products).click()
        time.sleep(1.5)

        var_app.logging.info("--------------")
        var_app.logging.info("Thanh công cụ - Mua hàng")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        try:
            phone = var_app.driver.find_element(By.XPATH, var_app.phone).text
            note = var_app.driver.find_element(By.XPATH, var_app.note).text
            SEND_SUPPORT = var_app.driver.find_element(By.XPATH, var_app.SEND_SUPPORT).text

            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, f"{phone}, {note}, {SEND_SUPPORT}")
            var_app.logging.info(f"{phone}, {note}, {SEND_SUPPORT}")

            if (phone == "Số điện thoại") and (note == "Ghi chú") and (SEND_SUPPORT == "GỬI HỖ TRỢ"):
                var_app.logging.info("True")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Pass")
            else:
                var_app.logging.info("False")
                var_app.driver.save_screenshot(var_app.imagepath + code + "_MuaHang_SanPhamMoi.png")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Fail")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 13, code + "_MuaHang_SanPhamMoi.png")
        except:
            var_app.logging.info("False")
            var_app.driver.save_screenshot(var_app.imagepath + code + "_MuaHang_SanPhamMoi.png")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Fail")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 13, code + "_MuaHang_SanPhamMoi.png")

    def shopping_send_info(self, code, eventname, result):
        var_app.driver.implicitly_wait(5)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass
        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.find_element(By.XPATH, var_app.SHOPPING)
        except:
            toolbar.shopping(self, "", "", "")

        var_app.driver.find_element(By.XPATH, var_app.new_products).click()
        time.sleep(1.5)


        var_app.driver.find_element(By.XPATH, var_app.shopping_phone_input).clear()
        time.sleep(0.5)
        var_app.driver.find_element(By.XPATH, var_app.shopping_phone_input).send_keys("0359667452")
        time.sleep(0.5)

        var_app.driver.find_element(By.XPATH, var_app.shopping_note_input).clear()
        time.sleep(0.5)
        var_app.driver.find_element(By.XPATH, var_app.shopping_note_input).send_keys("Phòng QA test mua hàng. Nhờ PDV đóng phiếu hộ")
        time.sleep(0.5)

        var_app.driver.find_element(By.XPATH, var_app.SEND_SUPPORT).click()
        time.sleep(2)
        var_app.driver.find_element(By.XPATH, var_app.IGREE).click()
        time.sleep(2)
        try:
            wait = WebDriverWait(var_app.driver, 10)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_app.check_support_send_info)))
        except:
            pass
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang Chủ - Thanh công cụ - Mua hàng",
                                              var_app.check_support_send_info, "Gửi yêu cầu hỗ trợ thất bại, vui lòng thử lại sau", "_MuaHang_GuiHoTro.png")






    def shopping_follow(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass
        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.find_element(By.XPATH, var_app.SHOPPING)
            var_app.driver.find_element(By.XPATH, var_app.shopping)
        except:
            toolbar.shopping(self, "", "", "")

        var_app.driver.find_element(By.XPATH, var_app.follow).click()
        time.sleep(2)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang Chủ - Thanh công cụ - Mua hàng - Theo dõi",
                                              var_app.pending_processing, "Chờ xử lý", "_MuaHang_Theo dõi.png")


    def shopping_follow_status(self, code, eventname, result, status_support, check_quantity):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass
        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.find_element(By.XPATH, var_app.shopping)
            var_app.driver.find_element(By.XPATH, var_app.pending_processing)
        except:
            toolbar.shopping_follow(self, "", "", "")
        time.sleep(1.5)
        var_app.driver.find_element(By.XPATH, status_support).click()
        time.sleep(1)
        var_app.logging.info("--------------")
        var_app.logging.info("Trang Chủ - Thanh công cụ - Mua hàng - Theo dõi")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("True")
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Pass")


        try:
            var_app.driver.implicitly_wait(1)
            check_quantity1 = var_app.driver.find_element(By.XPATH, check_quantity).text
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, "Số lượng phản hồi: {}".format(check_quantity1))
        except:
            pass


    def shopping_follow_complete(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass
        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.find_element(By.XPATH, var_app.pending_processing)
            var_app.driver.find_element(By.XPATH, var_app.shopping)
        except:
            toolbar.shopping_follow(self, "", "", "")
        time.sleep(1.5)
        var_app.driver.find_element(By.XPATH, var_app.complete).click()
        time.sleep(1)
        var_app.logging.info("--------------")
        var_app.logging.info("Trang Chủ - Thanh công cụ - Mua hàng - Theo dõi")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("True")
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Pass")


    def shopping_follow_search(self, code, eventname, result):
        var_app.driver.implicitly_wait(0.3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass
        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.find_element(By.XPATH, var_app.shopping)
            var_app.driver.find_element(By.XPATH, var_app.track_follow_search).click()
        except:
            toolbar.shopping_follow(self, "", "", "")
            var_app.driver.find_element(By.XPATH, var_app.track_follow_search).click()
        time.sleep(1.5)
        var_app.logging.info("--------------")
        var_app.logging.info("Trang Chủ - Thanh công cụ - Mua hàng - Theo dõi")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("True")
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Pass")


    def shopping_follow_filter(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass
        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.find_element(By.XPATH, var_app.support_customer_track_follow_filter).click()
        except:
            toolbar.shopping_follow(self, "", "", "")
            var_app.driver.find_element(By.XPATH, var_app.support_customer_track_follow_filter).click()
        time.sleep(2)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang Chủ - Thanh công cụ - Mua hàng - Theo dõi phản hồi",
                                              var_app.check_support_customer_track_follow_filter, "BỘ LỌC TÌM KIẾM", "_TrangChu_MuaHang_BoLoc.png")

        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.support_customer_track_follow_filter_apply).click()
            time.sleep(1.5)
        except:
            pass

        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.support_customer_iconx1a).click()
            time.sleep(1.5)
        except:
            pass













    def sos(self, code, eventname, result):
        var_app.driver.implicitly_wait(2)
        login_app.login.login_v3(self, var_app.data['login']['conhom_quantri_tk'], var_app.data['login']['conhom_quantri_mk'])
        var_app.driver.find_element(By.XPATH, var_app.homepage).click()
        time.sleep(2)
        try:
            var_app.driver.find_element(By.XPATH, var_app.homepage).click()
            time.sleep(1.5)
        except:
            pass
        var_app.driver.find_element(By.XPATH, var_app.icon_sos).click()
        time.sleep(2.5)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang Chủ - Thanh công cụ - icon SOS",
                                                  var_app.check_icon_sos, "CHỌN PHƯƠNG TIỆN", "_TrangChu_SOS.png")


    def sos_send_sos(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass
        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_icon_sos)
        except:
            toolbar.sos(self, "", "", "")

        module_other_app.tap_scaled(var_app.driver, [(150, 330)])
        time.sleep(2)

        module_other_app.write_result_text_try_if(code, eventname, result, "Trang Chủ - Thanh công cụ - icon SOS",
                                                  var_app.check_sos_send_sos, "Bạn có muốn gửi cảnh báo SOS không ?", "_TrangChu_SOS_GuiCanhBao.png")

        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.sos_send_sos_skip).click()
            time.sleep(1)
        except:
            pass

        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.sos_send_sos_iconx1).click()
            time.sleep(1.5)
        except:
            pass





class favorite:

    def more(self, code, eventname, result):
        var_app.driver.implicitly_wait(2)
        login_app.login.login_v3(self, var_app.data['login']['khongnhom_quantri_tk'], var_app.data['login']['khongnhom_quantri_mk'])
        var_app.driver.find_element(By.XPATH, var_app.homepage).click()
        time.sleep(2)
        try:
            var_app.driver.find_element(By.XPATH, var_app.homepage).click()
            time.sleep(1.5)
        except:
            pass
        time.sleep(1.5)
        var_app.driver.find_element(By.XPATH, var_app.more).click()
        time.sleep(2)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang Chủ - Yêu thích - Thêm",
                                                  var_app.check_more, "THIẾT LẬP MỤC ƯA THÍCH", "_TrangChu_Them.png")


    def mor_choose_min_favorite(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass
        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.find_element(By.XPATH, var_app.more_search_input)
        except:
            favorite.more(self, "", "", "")


        var_app.driver.find_element(By.XPATH, var_app.more_search_input).send_keys(var_app.data['home_page']['search_more'])
        time.sleep(2.5)
        try:
            var_app.driver.find_element(By.XPATH, var_app.checkbox_favorite1b).click()
            time.sleep(1)
        except:
            module_other_app.tap_scaled(var_app.driver, [(865, 390)])

        time.sleep(1)
        var_app.driver.find_element(By.XPATH, var_app.more_save).click()
        time.sleep(2)
        try:
            wait = WebDriverWait(var_app.driver, 10)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_app.check_mor_choose_min_favorite)))
        except:
            pass
        module_other_app.write_result_text_try_if(code, eventname, result, "Phương tiện - Thiết lập mục ưu thích",
                                              var_app.check_mor_choose_min_favorite, "Lưu mục ưa thích thành công", "_TrangChu_Them_ChonMucTienIch.png")


    def more_search(self, code, eventname, result):
        var_app.driver.implicitly_wait(0.3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.find_element(By.XPATH, var_app.homepage).click()
            time.sleep(2)
            try:
                var_app.driver.find_element(By.XPATH, var_app.homepage).click()
                time.sleep(1.5)
            except:
                pass
        except:
            login_app.login.login_v3(self, var_app.data['login']['khongnhom_quantri_tk'], var_app.data['login']['khongnhom_quantri_mk'])

            var_app.driver.find_element(By.XPATH, var_app.homepage).click()
            time.sleep(0.5)
            try:
                var_app.driver.find_element(By.XPATH, var_app.homepage).click()
                time.sleep(2)
            except:
                pass
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_more_search)
        except:
            module_other_app.swipe_scaled(var_app.driver, 720, 375, 180, 375, 500)
            time.sleep(1)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang Chủ - Yêu thích - Thêm",
                                              var_app.check_more_search, "Ẩn hiện xe", "_TrangChu_Them_TimKiem.png")


        module_other_app.swipe_scaled(var_app.driver, 180, 375, 720, 375, 500)
        time.sleep(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.more).click()
        except:
            module_other_app.swipe_scaled(var_app.driver, 180, 375, 720, 375, 500)
            time.sleep(1)
            var_app.driver.find_element(By.XPATH, var_app.more).click()
        time.sleep(2)
        # module_other_app.tap_scaled(var_app.driver, [(864, 534)])
        try:
            var_app.driver.find_element(By.XPATH, var_app.checkbox_favorite2b).click()
        except:
            module_other_app.tap_scaled(var_app.driver, [(865, 490)])

        time.sleep(1)
        var_app.driver.find_element(By.XPATH, var_app.more_save).click()
        time.sleep(2)


    def mor_choose_max_favorite(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass
        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.find_element(By.XPATH, var_app.more_search_name2)
        except:
            favorite.more(self, "", "", "")

        more_setup_favorite3 = var_app.driver.find_element(By.XPATH, var_app.more_setup_favorite3).get_attribute("checked")
        print("checkbox: ", more_setup_favorite3)
        if more_setup_favorite3 == "false":
            var_app.driver.find_element(By.XPATH, var_app.more_setup_favorite3).click()

        more_setup_favorite4 = var_app.driver.find_element(By.XPATH, var_app.more_setup_favorite4).get_attribute("checked")
        print("checkbox: ", more_setup_favorite4)
        if more_setup_favorite4 == "false":
            var_app.driver.find_element(By.XPATH, var_app.more_setup_favorite4).click()

        more_setup_favorite5 = var_app.driver.find_element(By.XPATH, var_app.more_setup_favorite5).get_attribute("checked")
        print("checkbox: ", more_setup_favorite5)
        if more_setup_favorite5 == "false":
            var_app.driver.find_element(By.XPATH, var_app.more_setup_favorite5).click()

        more_setup_favorite6 = var_app.driver.find_element(By.XPATH, var_app.more_setup_favorite6).get_attribute("checked")
        print("checkbox: ", more_setup_favorite6)
        if more_setup_favorite6 == "false":
            var_app.driver.find_element(By.XPATH, var_app.more_setup_favorite6).click()
        time.sleep(1)
        module_other_app.write_result_text_try_if(code, eventname, result, "Phương tiện - Thiết lập mục ưu thích",
                                              var_app.check_mor_select_too_limited, "Bạn đã chọn số tiện ích tối đa. Vui lòng bỏ chọn một tiện ích trước", "_TrangChu_Them_ChonNhieuMucTienIch.png")

        time.sleep(1)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.more_favorites_iconx1).click()
            time.sleep(1)
        except:
            pass


    def favorite_toward(self, code, eventname, result, towards, path_check, desire, path_image):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.find_element(By.XPATH, var_app.homepage).click()
            time.sleep(2)
            try:
                var_app.driver.find_element(By.XPATH, var_app.homepage).click()
                time.sleep(1.5)
            except:
                pass
        except:
            login_app.login.login_v3(self, var_app.data['login']['khongnhom_quantri_tk'], var_app.data['login']['khongnhom_quantri_mk'])
            var_app.driver.find_element(By.XPATH, var_app.homepage).click()
            time.sleep(2)
            try:
                var_app.driver.find_element(By.XPATH, var_app.homepage).click()
            except:
                pass
        time.sleep(1.5)
        var_app.driver.find_element(By.XPATH, towards).click()
        time.sleep(1.5)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Yêu thích",
                                              path_check, desire, path_image)
        time.sleep(1)
        var_app.driver.find_element(By.XPATH, var_app.homepage).click()
        time.sleep(2)
        try:
            var_app.driver.find_element(By.XPATH, var_app.homepage).click()
            time.sleep(1.5)
        except:
            pass



    def mor_drag_and_drop(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass
        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.find_element(By.XPATH, var_app.more_search_input)
        except:
            favorite.more(self, "", "", "")

        try:
            name_before1 = var_app.driver.find_element(By.XPATH, var_app.name_before1).text
        except:
            var_app.driver.find_element(By.XPATH, var_app.more_back).click()
            time.sleep(2)
            var_app.driver.find_element(By.XPATH, var_app.more).click()
            time.sleep(2.5)


        #chức năng 2
        try:
            var_app.driver.find_element(By.XPATH, var_app.favorite_list2_2)
        except:
            try:
                var_app.driver.find_element(By.XPATH, var_app.favorite_list2_1).click()
            except:
                module_other_app.tap_scaled(var_app.driver, [(865, 495)])
        time.sleep(1)

        #chức năng 3
        try:
            var_app.driver.find_element(By.XPATH, var_app.favorite_list3_2)
        except:
            try:
                var_app.driver.find_element(By.XPATH, var_app.favorite_list3_1).click()
            except:
                module_other_app.tap_scaled(var_app.driver, [(865, 595)])
        time.sleep(1)

        #chức năng 4
        try:
            var_app.driver.find_element(By.XPATH, var_app.favorite_list4_2)
        except:
            try:
                var_app.driver.find_element(By.XPATH, var_app.favorite_list4_1).click()
            except:
                module_other_app.tap_scaled(var_app.driver, [(865, 695)])
        time.sleep(1.5)

        name_before1 = var_app.driver.find_element(By.XPATH, var_app.name_before1).text
        name_before2 = var_app.driver.find_element(By.XPATH, var_app.name_before2).text
        print(f"Vị trí 1 trước: {name_before1}")
        print(f"Vị trí 2 trước: {name_before2}")


        # action = TouchAction(var_app.driver)
        #
        # start_x = 133
        # start_y = 515  # điểm nhấn ban đầu
        # end_x = 133
        # step = 30  # mỗi lần kéo lên 30px
        #
        # # Nhấn giữ 1 lần
        # action.long_press(x=start_x, y=start_y).wait(300)
        #
        # # Kéo dần lên trên trong 5 bước
        # for i in range(4):
        #     new_y = start_y - (step * (i + 1))
        #     action.move_to(x=end_x, y=new_y).wait(300)
        #
        # # Thả ra sau khi hoàn thành
        # action.release().perform()

        module_other_app.drag_scaled_steps(var_app.driver,
            start_x_old=133, start_y_old=415,
            end_x_old=133,   end_y_old=515,
            steps=4,
            old_width=900,
            old_height=1600)



        name_after1 = var_app.driver.find_element(By.XPATH, var_app.name_before1).text
        name_after2 = var_app.driver.find_element(By.XPATH, var_app.name_before2).text
        print(f"Vị trí 1 sau: {name_after1}")
        print(f"Vị trí 2 sau: {name_after2}")
        var_app.logging.info("--------------")
        var_app.logging.info("Trang chủ - Thêm - Kéo thả mục yêu thích")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, f"Vị trí 1 trước: {name_before1}"
                                                                                f"\nVị trí 2 trước: {name_before2}"
                                                                                f"\n\nVị trí 1 sau: {name_after1}"
                                                                                f"\nVị trí 2 sau: {name_after2}")
        var_app.logging.info(f"Vị trí 1 trước: {name_before1}"
                            f"\nVị trí 2 trước: {name_before2}"
                            f"\n\nVị trí 1 sau: {name_after1}"
                            f"\nVị trí 2 sau: {name_after2}")

        if (name_before2 == name_after1):
            var_app.logging.info("True")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Pass")
        else:
            var_app.logging.info("False")
            var_app.driver.save_screenshot(var_app.imagepath + code + "_TrangChu_YeuThich_KeoTha.png")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Fail")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 13, code + "_TrangChu_YeuThich_KeoTha.png")





    def overview_table_select_group(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass
        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.find_element(By.XPATH, var_app.overview_table_select_group)
        except:
            # toolbar_back(self)
            move_module(self, "", "", "", var_app.overview_table, 0.8, 0.85, 0.2, 0.85, 1000, "", "", "", "")

        var_app.driver.find_element(By.XPATH, var_app.overview_table_select_group).click()
        time.sleep(2)
        var_app.driver.find_element(By.XPATH, var_app.image_monitoring_select_group_input).send_keys(var_app.data['home_page']['search_group1'])
        time.sleep(2)
        var_app.driver.find_element(By.XPATH, var_app.overview_table_select_group_checkbox).click()
        time.sleep(1)
        var_app.driver.find_element(By.XPATH, var_app.SELECT).click()
        time.sleep(2.5)
        var_app.driver.find_element(By.XPATH, var_app.icon_search).click()
        time.sleep(7)
        module_other_app.write_result_text_try_if_other(code, eventname, result, "Trang chủ - Bảng tổng quan",
                                              var_app.check_overview_table_select_group, "", "_TrangChu_BangTongQuan_ChonNhom.png")


        var_app.driver.find_element(By.XPATH, var_app.overview_table_select_group).click()
        time.sleep(2)
        var_app.driver.find_element(By.XPATH, var_app.check_box_all).click()
        time.sleep(1)
        var_app.driver.find_element(By.XPATH, var_app.check_box_all).click()
        time.sleep(1)
        var_app.driver.find_element(By.XPATH, var_app.SELECT).click()
        time.sleep(2)
        var_app.driver.find_element(By.XPATH, var_app.icon_search).click()
        time.sleep(2)

    def overview_table_status(self, code, eventname, result, path_check, number_from, number_to, desire, path_image):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass
        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.find_element(By.XPATH, path_check)
        except:
            # toolbar_back(self)
            move_module(self, "", "", "", var_app.overview_table, 0.8, 0.85, 0.2, 0.85, 1000, "", "", "", "")


        module_other_app.write_result_text_try_if_cut(code, eventname, result, "Trang chủ - Bảng tổng quan",
                                              path_check, number_from, number_to, desire, path_image)

        #

    def overview_table_state(self, code, eventname, result, type_check):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass
        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.find_element(By.XPATH, var_app.over_table_vehicle)
        except:
            # toolbar_back(self)
            move_module(self, "", "", "", var_app.overview_table, 0.8, 0.85, 0.2, 0.85, 1000, "", "", "", "")

        vehicle = var_app.driver.find_element(By.XPATH, var_app.over_table_vehicle).text
        violate = var_app.driver.find_element(By.XPATH, var_app.over_table_violate).text
        active = var_app.driver.find_element(By.XPATH, var_app.over_table1a).text
        active = ''.join(re.findall(r'\d+', active))
        off = var_app.driver.find_element(By.XPATH, var_app.over_table2a).text
        off = ''.join(re.findall(r'\d+', off))


        if type_check == "0":
            var_app.logging.info("--------------")
            var_app.logging.info("Trang chủ - Bảng tổng quan")
            var_app.logging.info("Mã - " + code)
            var_app.logging.info("Tên sự kiện - " + eventname)
            var_app.logging.info("Kết quả - " + result)
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, "Hoạt động: {}\nTắt máy: {}\nPhương tiện: {}".format(active, off, vehicle))
            if int(vehicle) == int(active) + int(off):
                var_app.logging.info("True")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Pass")
            else:
                var_app.logging.info("False")
                var_app.driver.save_screenshot(var_app.imagepath + code + "_TrangChu_BangTongQuan_SoPuongTien.png")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Fail")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 13, code + "_TrangChu_BangTongQuan_SoPuongTien.png")


        if type_check == "1":
            module_other_app.write_result_text_try_if_other(code, eventname, result, "Trang chủ - Bảng tổng quan",
                                                  var_app.over_table_violate, "", "_TrangChu_BangTongQuan_ViPham.png")

    def overview_table_select_vehicle(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass
        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.find_element(By.XPATH, var_app.overview_table_x).click()
            time.sleep(2)
            var_app.driver.find_element(By.XPATH, var_app.overview_table).click()
            time.sleep(3)
        except:
            # toolbar_back(self)
            move_module(self, "", "", "", var_app.overview_table, 0.8, 0.85, 0.2, 0.85, 1000, "", "", "", "")

        var_app.driver.find_element(By.XPATH, var_app.overview_table_select_vehicle).click()
        time.sleep(2)
        var_app.driver.find_element(By.XPATH, var_app.overview_table_select_vehicle_input).send_keys(var_app.data['home_page']['search_vehicle'])
        time.sleep(2)
        var_app.driver.find_element(By.XPATH, var_app.overview_table_select_vehicle_checkbox).click()
        time.sleep(1)
        var_app.driver.find_element(By.XPATH, var_app.SELECT).click()
        time.sleep(2.5)
        var_app.driver.find_element(By.XPATH, var_app.icon_search1).click()
        time.sleep(2.5)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Bảng tổng quan",
                                              var_app.check_overview_table_select_vehicle, var_app.data['home_page']['search_vehicle'], "_TrangChu_BangTongQuan_ChonPhuongtien.png")

    def overview_table_info(self, code, eventname, result, path_over_view, path_detail, name_image):
        var_app.driver.implicitly_wait(0.3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass
        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup//*[@text='"+var_app.data['home_page']['search_vehicle']+"']")
        except:
            favorite.overview_table_select_vehicle(self, "", "", "")

        data_over_view = var_app.driver.find_element(By.XPATH, path_over_view).text
        data_detail = var_app.driver.find_element(By.XPATH, path_detail).text

        var_app.logging.info("--------------")
        var_app.logging.info("Trang chủ - Bảng tổng quan")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, "Tổng quan: {}\nChi tiết: {}".format(data_over_view, data_detail))
        if data_over_view == data_detail:
            var_app.logging.info("True")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Pass")
        else:
            var_app.logging.info("False")
            var_app.driver.save_screenshot(var_app.imagepath + code + name_image)
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Fail")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 13,  code + name_image)

    def overview_table_violate(self, code, eventname, result):
        var_app.driver.implicitly_wait(0.3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass
        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup//*[@text='"+var_app.data['home_page']['search_vehicle']+"']")
        except:
            favorite.overview_table_select_vehicle(self, "", "", "")

        var_app.logging.info("--------------")
        var_app.logging.info("Trang chủ - Bảng tổng quan")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        data_over_view = var_app.driver.find_element(By.XPATH, var_app.overview_table_violate1).text
        data_detail = var_app.driver.find_element(By.XPATH, var_app.overview_table_violate2).text
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, "Tổng quan: {}\nChi tiết: {}".format(data_over_view, data_detail))

        if data_over_view == "0":
            data_over_view1 = "Xe không có vi phạm"
            if data_over_view1 == data_detail:
                var_app.logging.info("True")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Pass")
            else:
                var_app.logging.info("False")
                var_app.driver.save_screenshot(var_app.imagepath + code + "_TrangChu_BangTongQuan_ViPham.png")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Fail")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 13, code + "_TrangChu_BangTongQuan_ViPham.png")
        else:
            module_other_app.write_result_text_try_if_other(code, eventname, result, "Trang chủ - Bảng tổng quan",
                                                            var_app.overview_table_violate2, "Xe không có vi phạm", "_TrangChu_BangTongQuan_ChonNhom.png")











