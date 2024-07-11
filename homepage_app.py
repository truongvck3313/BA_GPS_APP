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




def goto_cty(xncode, check_cty):
    var_app.driver.implicitly_wait(5)
    # var_app.driver.find_element(By.XPATH, var_app.homepage).click()
    # time.sleep(1)
    var_app.driver.find_element(By.XPATH, var_app.icon_goto_cty).click()
    time.sleep(2)
    var_app.driver.find_element(By.XPATH, var_app.icon_goto_cty_input).send_keys(xncode)
    var_app.driver.find_element(By.XPATH, var_app.goto_cty).click()
    time.sleep(2)
    check_cty1 = var_app.driver.find_element(By.XPATH, var_app.check_cty1).text
    print("1", check_cty1)
    print("2", check_cty)
    if check_cty1 == check_cty:
        try:
            var_app.driver.find_element(By.XPATH, var_app.goto_cty).click()
            var_app.driver.find_element(By.XPATH, var_app.goto_cty).click()
        except:
            var_app.driver.find_element(By.XPATH, var_app.goto_cty1).click()
        print("sdsd")
        time.sleep(2)




class toolbar:

    def utility_list(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(7)
        except:
            pass

        var_app.driver.implicitly_wait(5)
        var_app.driver.find_element(By.XPATH, var_app.homepage).click()
        time.sleep(1)
        var_app.driver.find_element(By.XPATH, var_app.utility_list).click()
        time.sleep(2)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang Chủ - Thanh công cụ - Danh sách tiện ích",
                                              var_app.check_opeutility_list, "Danh sách tiện ích", "_TrangChu_DanhSachTienIch.png")


    def utility_list_search(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(7)
        except:
            pass

        var_app.driver.implicitly_wait(5)

        utility_list_name2 = var_app.driver.find_element(By.XPATH, var_app.utility_list_name2).text

        var_app.driver.find_element(By.XPATH, var_app.utility_list_search_input).send_keys(utility_list_name2)
        time.sleep(2)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang Chủ - Thanh công cụ - Danh sách tiện ích",
                                              var_app.check_utility_list_search, utility_list_name2, "_TrangChu_DanhSachTienIch_TimKiem.png")

        var_app.driver.find_element(By.XPATH, var_app.utility_list_search_input).clear()

        try:
            var_app.driver.find_element(By.XPATH, var_app.utility_list_search_iconx).click()
            time.sleep(1)
        except:
            pass





    def notification(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(7)
        except:
            pass

        var_app.driver.implicitly_wait(5)
        var_app.driver.find_element(By.XPATH, var_app.homepage).click()
        time.sleep(1)
        var_app.driver.find_element(By.XPATH, var_app.notification).click()
        time.sleep(2)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang Chủ - Thanh công cụ - Thông báo",
                                              var_app.check_notification, "THÔNG BÁO", "_TrangChu_ThongBao.png")


    def see_notification(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(7)
        except:
            pass

        var_app.driver.implicitly_wait(3)
        var_app.driver.find_element(By.XPATH, var_app.see_notification1).click()
        time.sleep(2)
        module_other_app.write_result_displayed_try(code, eventname, result, "Trang Chủ - Thanh công cụ - Thông báo",
                                                var_app.check_hsee_notification, "_TrangChu_ThongBao_XemThongBao.png")

        try:
            var_app.driver.find_element(By.XPATH, var_app.see_notification_iconx).click()
            time.sleep(1)
        except:
            pass


    def delete_notification(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(7)
        except:
            pass

        var_app.driver.implicitly_wait(3)
        var_app.driver.find_element(By.XPATH, var_app.delete_notification).click()
        time.sleep(2)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang Chủ - Thanh công cụ - Thông báo",
                                              var_app.check_delete_notification, "Bạn chắc chắn xóa tất cả thông báo?", "_TrangChu_ThongBao_XoaThongBao.png")

        var_app.driver.find_element(By.XPATH, var_app.delete_notification_skip).click()
        time.sleep(1.2)
        try:
            var_app.driver.find_element(By.XPATH, var_app.see_notification_iconx1).click()
            time.sleep(1)
        except:
            pass






    def warning_list(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(7)
        except:
            pass

        var_app.driver.implicitly_wait(5)

        login_app.login.check_logout1(self, "TRẦN QUANG TRƯỜNG PQA", "truongtq@bagroup.vn", "atgmj123")
        var_app.driver.find_element(By.XPATH, var_app.homepage).click()
        time.sleep(1)
        # goto_cty(950, "[950] Viconship Đà Nẵng")

        var_app.driver.find_element(By.XPATH, var_app.warning_list).click()
        time.sleep(2.5)
        var_app.driver.find_element(By.XPATH, var_app.icon_goto_cty1).click()
        time.sleep(1.5)
        var_app.driver.find_element(By.XPATH, var_app.icon_goto_cty_input1).send_keys("950")
        var_app.driver.find_element(By.XPATH, var_app.goto_cty_buttonsearch).click()
        time.sleep(2)
        check_cty2 = var_app.driver.find_element(By.XPATH, var_app.check_cty2).text
        print("1", check_cty2)
        print("2", "[950] Viconship Đà Nẵng")
        if check_cty2 == "[950] Viconship Đà Nẵng":
            var_app.driver.find_element(By.XPATH, var_app.check_cty2).click()
            print("sdsd")
            time.sleep(2)

        module_other_app.write_result_displayed_try(code, eventname, result, "Trang Chủ - Thanh công cụ - Danh sách cảnh báo",
                                                var_app.check_warning_list1, "_TrangChu_DanhSachCanhBao.png")


    def warning_list_search(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(7)
        except:
            pass

        var_app.driver.implicitly_wait(5)
        try:
            var_app.driver.find_element(By.XPATH, var_app.type_warning)
        except:
            toolbar.warning_list(self, "Toolbar06", eventname, result)


        var_app.driver.find_element(By.XPATH, var_app.type_warning).click()
        time.sleep(1)
        var_app.driver.find_element(By.XPATH, var_app.type_warning_all).click()
        time.sleep(1.5)
        try:
            name_vehicle1 = var_app.driver.find_element(By.XPATH, var_app.warning_list_search_name1).text
        except:
            name_vehicle1 = var_app.driver.find_element(By.XPATH, var_app.warning_list_search_name2).text
        var_app.driver.find_element(By.XPATH, var_app.warning_list_search_button).click()
        time.sleep(1.5)
        var_app.driver.find_element(By.XPATH, var_app.warning_list_search_input).send_keys(name_vehicle1)
        print(name_vehicle1)
        time.sleep(2)
        var_app.driver.find_element(By.XPATH, var_app.warning_list_search1).click()
        time.sleep(2)
        var_app.driver.find_element(By.XPATH, var_app.warning_list_iconsearch).click()
        time.sleep(3)
        var_app.driver.find_element(By.XPATH, var_app.check_warning_list_search_name1).click()
        time.sleep(2)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang Chủ - Thanh công cụ - Danh sách cảnh báo",
                                              var_app.check_warning_list_search_name2, name_vehicle1, "_TrangChu_DanhSachCanhBao_TimKiem.png")

        try:
            var_app.driver.find_element(By.XPATH, var_app.warning_list_iconx1).click()
            time.sleep(1)
        except:
            pass


    def warning_list_mark_as_read(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(7)
        except:
            pass

        var_app.driver.implicitly_wait(5)
        try:
            var_app.driver.find_element(By.XPATH, var_app.warning_list_mark_as_read)
        except:
            toolbar.warning_list(self, "Toolbar06", eventname, result)
        var_app.driver.find_element(By.XPATH, var_app.warning_list_mark_as_read).click()
        time.sleep(1.5)
        var_app.driver.find_element(By.XPATH, var_app.YES).click()
        module_other_app.write_result_displayed_try(code, eventname, result, "Trang Chủ - Thanh công cụ - Danh sách cảnh báo",
                                                var_app.check_hwarning_list_mark_as_read, "_TrangChu_DanhSachCanhBao_DanhDauLaDaDoc.png")

        try:
            var_app.driver.find_element(By.XPATH, var_app.warning_list_iconx).click()
        except:
            pass





    def support_customer(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(7)
        except:
            pass

        var_app.driver.implicitly_wait(5)

        login_app.login.check_logout1(self, "43E02740", "43E02740", "12341234")
        var_app.driver.find_element(By.XPATH, var_app.homepage).click()
        time.sleep(1)
        var_app.driver.find_element(By.XPATH, var_app.icon_support_customer).click()
        time.sleep(2.5)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang Chủ - Thanh công cụ - Hỗ trợ khách hàng",
                                              var_app.check_icon_support_customer, "Hỗ trợ khách hàng", "_TrangChu_HoTroKhachHang_.png")


    def support_customer_search(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(7)
        except:
            pass
        var_app.driver.implicitly_wait(5)
        support_customer_search_name2 = var_app.driver.find_element(By.XPATH, var_app.support_customer_search_name2).text
        var_app.driver.find_element(By.XPATH, var_app.support_customer_search_input).send_keys(support_customer_search_name2)
        time.sleep(2)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang Chủ - Thanh công cụ - Hỗ trợ khách hàng",
                                              var_app.check_support_customer_search, support_customer_search_name2, "_TrangChu_HoTroKhachHang_TimKiem.png")

        var_app.driver.find_element(By.XPATH, var_app.support_customer_search_input).clear()
        time.sleep(1)


    def support_customer_link_affiliate(self, code, eventname, result, link_affiliate, path_check, desire, path_image):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(7)
        except:
            pass
        var_app.driver.implicitly_wait(5)
        var_app.driver.find_element(By.XPATH, link_affiliate).click()
        time.sleep(2.5)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang Chủ - Thanh công cụ - Hỗ trợ khách hàng",
                                              path_check, desire, path_image)

        var_app.driver.press_keycode(4)
        time.sleep(2)






















# class favorite:
#
#     def more(self, code, eventname, result):
#         var_app.driver.implicitly_wait(1)
#         try:
#             var_app.driver.find_element(By.XPATH, var_app.bagps).click()
#             time.sleep(7)
#         except:
#             pass
#
#         var_app.driver.implicitly_wait(5)
#         var_app.driver.find_element(By.XPATH, var_app.homepage).click()
#         time.sleep(1)
#         var_app.driver.find_element(By.XPATH, var_app.more).click()












