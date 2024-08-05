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




def goto_cty(xncode):
    var_app.driver.implicitly_wait(5)
    var_app.driver.find_element(By.XPATH, var_app.homepage).click()
    time.sleep(1)
    var_app.driver.find_element(By.XPATH, var_app.icon_goto_cty).click()
    time.sleep(2)
    var_app.driver.find_element(By.XPATH, var_app.icon_goto_cty_input).send_keys(xncode)
    var_app.driver.find_element(By.XPATH, var_app.goto_cty).click()
    time.sleep(2)
    var_app.driver.tap([(860, 355)])
    time.sleep(3)

def move_module(self, code, eventname, result, link, startX, startY, endX, endY, duration,
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
        login_app.login.check_logout1(self, "43E02740", "43E02740", "12341234")
        try:
            var_app.driver.find_element(By.XPATH, var_app.homepage).click()
        except:
            login_app.login.login_v3(self, "43E02740", "12341234")
            var_app.driver.find_element(By.XPATH, var_app.homepage).click()
    time.sleep(1)
    minitor_app.scroll_and_click(startX, startY, endX, endY, duration, link)
    time.sleep(2)
    module_other_app.write_result_text_try_if(code, eventname, result, path_module,
                                              path_check, desire, path_image)






class toolbar:

    def utility_list(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(5)
        try:
            var_app.driver.find_element(By.XPATH, var_app.homepage).click()
        except:
            login_app.login.login_v3(self, "43E02740", "12341234")
            var_app.driver.find_element(By.XPATH, var_app.homepage).click()

        time.sleep(1)
        var_app.driver.find_element(By.XPATH, var_app.utility_list).click()
        time.sleep(2)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang Chủ - Thanh công cụ - Tìm kiếm danh mục",
                                              var_app.check_opeutility_list, "TÌM KIẾM DANH MỤC", "_TrangChu_TimKiemDanhMuc.png")


    def utility_list_search(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(5)
        try:
            var_app.driver.find_element(By.XPATH, var_app.utility_list_search_input)
        except:
            toolbar.utility_list(self, "Toolbar01", eventname, result)

        var_app.driver.find_element(By.XPATH, var_app.utility_list_search_input).send_keys(var_app.data['home_page']['search_category'])
        time.sleep(2)
        var_app.driver.tap([(160, 330)])
        time.sleep(2.5)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang Chủ - Thanh công cụ - Tìm kiếm danh mục",
                                              var_app.check_utility_list_search, "DANH SÁCH LÁI XE", "_TrangChu_TimKiemDanhMuc_TimKiem.png")


        try:
            var_app.driver.find_element(By.XPATH, var_app.utility_list_search_iconx).click()
            time.sleep(1)
        except:
            pass





    def notification(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass
        var_app.driver.implicitly_wait(5)
        try:
            var_app.driver.find_element(By.XPATH, var_app.homepage).click()
        except:
            login_app.login.login_v3(self, "43E02740", "12341234")
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
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_notification)
        except:
            toolbar.notification(self, "Toolbar03", eventname, result)

        var_app.driver.tap([(300, 250)])
        time.sleep(3)

        module_other_app.write_result_text_try_if(code, eventname, result, "Trang Chủ - Thanh công cụ - Thông báo",
                                              var_app.check_see_notification, "CHI TIẾT THÔNG BÁO", "_TrangChu_ThongBao_XemThongBao.png")


        try:
            var_app.driver.find_element(By.XPATH, var_app.see_notification_iconback).click()
            time.sleep(1)
        except:
            pass


    def delete_notification(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(3)
        try:
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
            var_app.driver.find_element(By.XPATH, var_app.see_notification_iconx4).click()
            time.sleep(1)
        except:
            pass






    def warning_list(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        login_app.login.login_v3(self, "truongtq@bagroup.vn", "atgmj123")

        var_app.driver.implicitly_wait(5)
        # login_app.login.check_logout1(self, "TRẦN QUANG TRƯỜNG PQA", "truongtq@bagroup.vn", "atgmj123")
        var_app.driver.find_element(By.XPATH, var_app.homepage).click()
        time.sleep(1)
        goto_cty(950)

        var_app.driver.find_element(By.XPATH, var_app.warning_list).click()
        time.sleep(2.5)

        module_other_app.write_result_text_try_if(code, eventname, result, "Trang Chủ - Thanh công cụ - Danh sách cảnh báo",
                                              var_app.check_warning_list1, "DANH SÁCH CẢNH BÁO", "_TrangChu_DanhSachCanhBao.png")


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
        time.sleep(1.5)
        var_app.driver.tap([(82, 365)])
        time.sleep(1.5)

        var_app.driver.find_element(By.XPATH, var_app.warning_list_iconsearch).click()
        time.sleep(2)
        var_app.driver.tap([(260, 470)])
        time.sleep(2)
        try:
            check_data = var_app.driver.find_element(By.XPATH, var_app.check_warning_list_search_name3).text
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 11, check_data)
        except:
            pass
        module_other_app.write_result_displayed_try(code, eventname, result, "Trang Chủ - Thanh công cụ - Danh sách cảnh báo",
                                                var_app.check_warning_list_search_name3, "_TrangChu_DanhSachCanhBao_TimKiem.png")

        try:
            var_app.driver.find_element(By.XPATH, var_app.warning_list_iconx2).click()
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

        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.type_warning)
        except:
            toolbar.warning_list(self, "Toolbar06", eventname, result)


        var_app.driver.find_element(By.XPATH, var_app.warning_list_mark_as_read).click()
        time.sleep(1.5)

        module_other_app.write_result_text_try_if(code, eventname, result, "Trang Chủ - Thanh công cụ - Danh sách cảnh báo",
                                              var_app.check_hwarning_list_mark_as_read, "Bạn chắc chắn muốn chuyển tất cả cảnh báo thành đã đọc?", "_TrangChu_DanhSachCanhBao_DanhDauLaDaDoc.png")

        var_app.driver.find_element(By.XPATH, var_app.IGREE).click()
        time.sleep(1)

        try:
            var_app.driver.find_element(By.XPATH, var_app.warning_list_iconx).click()
            time.sleep(1)
        except:
            pass





    def support_customer(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        login_app.login.login_v3(self, "43E02740", "12341234")

        var_app.driver.implicitly_wait(5)
        var_app.driver.find_element(By.XPATH, var_app.homepage).click()
        time.sleep(1)

        var_app.driver.find_element(By.XPATH, var_app.icon_support_customer).click()
        time.sleep(2.5)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang Chủ - Thanh công cụ - Hỗ trợ khách hàng",
                                              var_app.check_icon_support_customer, "HỖ TRỢ KHÁCH HÀNG", "_TrangChu_HoTroKhachHang_.png")


    def support_customer_search(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass
        var_app.driver.implicitly_wait(5)
        try:
            var_app.driver.find_element(By.XPATH, var_app.support_customer_search_input)
        except:
            login_app.login.check_logout1(self, "43E02740", "43E02740", "12341234")
            var_app.driver.find_element(By.XPATH, var_app.homepage).click()
            time.sleep(1)
            var_app.driver.find_element(By.XPATH, var_app.icon_support_customer).click()
            time.sleep(2.5)

        support_customer_search_name2 = var_app.driver.find_element(By.XPATH,var_app.support_customer_search_name2).text
        var_app.driver.find_element(By.XPATH, var_app.support_customer_search_input).send_keys(support_customer_search_name2)
        time.sleep(2)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang Chủ - Thanh công cụ - Hỗ trợ khách hàng",
                                              var_app.check_support_customer_search, support_customer_search_name2, "_TrangChu_HoTroKhachHang_TimKiem.png")

        var_app.driver.find_element(By.XPATH, var_app.support_customer_search_input).clear()
        time.sleep(1)


    def support_customer_link_affiliate(self, code, eventname, result, link_affiliate, path_check_iconx, path_check, desire, path_image):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass
        var_app.driver.implicitly_wait(5)

        try:
            var_app.driver.find_element(By.XPATH, link_affiliate).click()
        except:
            var_app.driver.implicitly_wait(1)
            try:
                var_app.driver.find_element(By.XPATH, var_app.support_customer_link_affiliate_iconx0).click()
                time.sleep(1.5)
            except:
                pass
            try:
                var_app.driver.find_element(By.XPATH, var_app.support_customer_link_affiliate_iconx).click()
                time.sleep(1.5)
            except:
                pass
            var_app.driver.implicitly_wait(5)
            login_app.login.check_logout1(self, "43E02740", "43E02740", "12341234")
            var_app.driver.find_element(By.XPATH, var_app.homepage).click()
            time.sleep(1)
            var_app.driver.find_element(By.XPATH, var_app.icon_support_customer).click()
            time.sleep(2.5)
            var_app.driver.find_element(By.XPATH, link_affiliate).click()
        time.sleep(2.5)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang Chủ - Thanh công cụ - Hỗ trợ khách hàng",
                                              path_check, desire, path_image)

        try:
            var_app.driver.find_element(By.XPATH, path_check_iconx).click()
            time.sleep(1.5)
        except:
            pass


    def support_customer_track_feedback(self, code, eventname, result, status_support, check_quantity, path_check, path_image):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass
        var_app.driver.implicitly_wait(5)
        try:
            var_app.driver.find_element(By.XPATH, var_app.track_feedback).click()
        except:
            toolbar.support_customer(self, "", "", "")
            var_app.driver.find_element(By.XPATH, var_app.track_feedback).click()
        time.sleep(1.5)
        var_app.driver.find_element(By.XPATH, status_support).click()
        time.sleep(1)
        var_app.logging.info("--------------")
        var_app.logging.info("Trang Chủ - Thanh công cụ - Hỗ trợ khách hàng - Theo dõi phản hồi")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("True")
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Pass")
        # try:
        #     check_quantity1 = var_app.driver.find_element(By.XPATH, check_quantity).text
        #     path_check1 = var_app.driver.find_element(By.XPATH, path_check).text
        #     module_other_app.writeData(var_app.checklistpath, "Checklist", code, 11, path_check1)
        #
        #     if (int(check_quantity1) == 0 and path_check1 == "Chưa có dữ liệu tìm kiếm") \
        #             or (int(check_quantity1) > 0 and path_check1 != "Chưa có dữ liệu tìm kiếm"):
        #         var_app.logging.info("True")
        #         module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Pass")
        #     else:
        #         var_app.logging.info("False")
        #         var_app.driver.save_screenshot(var_app.imagepath + code + path_image)
        #         module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Fail")
        #         module_other_app.writeData(var_app.checklistpath, "Checklist", code, 9, code + path_image)
        # except:
        #     pass


    def support_customer_track_complete(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(7)
        except:
            pass
        var_app.driver.implicitly_wait(5)
        try:
            var_app.driver.find_element(By.XPATH, var_app.track_feedback).click()
        except:
            toolbar.support_customer(self, "", "", "")
            var_app.driver.find_element(By.XPATH, var_app.track_feedback).click()
        time.sleep(1.5)
        var_app.driver.find_element(By.XPATH, var_app.complete).click()
        time.sleep(1)
        var_app.logging.info("--------------")
        var_app.logging.info("Trang Chủ - Thanh công cụ - Hỗ trợ khách hàng - Theo dõi phản hồi")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("True")
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Pass")


    def support_customer_track_follow_search(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(7)
        except:
            pass
        var_app.driver.implicitly_wait(5)
        try:
            var_app.driver.find_element(By.XPATH, var_app.track_follow_search).click()
        except:
            toolbar.support_customer(self, "", "", "")
            var_app.driver.find_element(By.XPATH, var_app.track_follow_search).click()
        time.sleep(1.5)
        var_app.logging.info("--------------")
        var_app.logging.info("Trang Chủ - Thanh công cụ - Hỗ trợ khách hàng - Theo dõi phản hồi")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("True")
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Pass")


    def support_customer_track_follow_filter(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(7)
        except:
            pass
        var_app.driver.implicitly_wait(5)
        try:
            var_app.driver.find_element(By.XPATH, var_app.support_customer_track_follow_filter).click()
        except:
            toolbar.support_customer(self, "", "", "")
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
            var_app.driver.find_element(By.XPATH, var_app.support_customer_track_follow_filter_apply).click()
            time.sleep(1.5)
        except:
            pass

        try:
            var_app.driver.find_element(By.XPATH, var_app.support_customer_iconx1).click()
            time.sleep(1.5)
        except:
            pass




    def sos(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(5)
        try:
            var_app.driver.find_element(By.XPATH, var_app.homepage).click()
        except:
            login_app.login.login_v3(self, "43E02740", "12341234")
            var_app.driver.find_element(By.XPATH, var_app.homepage).click()
        time.sleep(1.5)
        var_app.driver.find_element(By.XPATH, var_app.icon_sos).click()
        time.sleep(2.5)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang Chủ - Thanh công cụ - icon SOS",
                                                  var_app.check_icon_sos, "CHỌN PHƯƠNG TIỆN", "_TrangChu_SOS.png")

    def sos_send_sos(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass
        var_app.driver.implicitly_wait(5)
        var_app.driver.tap([(150, 330)])
        time.sleep(2)

        module_other_app.write_result_text_try_if(code, eventname, result, "Trang Chủ - Thanh công cụ - icon SOS",
                                                  var_app.check_sos_send_sos, "Bạn có muốn gửi cảnh báo SOS không ?", "_TrangChu_SOS_GuiCanhBao.png")

        try:
            var_app.driver.find_element(By.XPATH, var_app.sos_send_sos_skip).click()
            time.sleep(1)
        except:
            pass
        try:
            var_app.driver.find_element(By.XPATH, var_app.sos_send_sos_iconx1).click()
            time.sleep(1.5)
        except:
            pass





class favorite:

    def more(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(5)
        try:
            var_app.driver.find_element(By.XPATH, var_app.homepage).click()
        except:
            login_app.login.login_v3(self, "43E02740", "12341234")
            var_app.driver.find_element(By.XPATH, var_app.homepage).click()

        time.sleep(1)
        var_app.driver.find_element(By.XPATH, var_app.more).click()
        time.sleep(1.5)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang Chủ - Yêu thích - Thêm",
                                                  var_app.check_more, "THIẾT LẬP MỤC ƯA THÍCH", "_TrangChu_Them.png")


    def mor_choose_min_favorite(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass
        var_app.driver.implicitly_wait(5)
        try:
            var_app.driver.find_element(By.XPATH, var_app.more_search_input)
        except:
            favorite.more(self, "", "", "")

        var_app.driver.find_element(By.XPATH, var_app.more_search_input).send_keys(var_app.data['home_page']['search_more'])
        time.sleep(2)
        var_app.driver.tap([(860, 335)])
        time.sleep(0.5)
        var_app.driver.find_element(By.XPATH, var_app.more_save).click()
        time.sleep(2)
        module_other_app.write_result_text_try_if(code, eventname, result, "Phương tiện - Thiết lập mục ưu thích",
                                              var_app.check_mor_choose_min_favorite, "Lưu mục ưa thích thành công", "_TrangChu_Them_ChonMucTienIch.png")


    def more_search(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(5)
        try:
            var_app.driver.find_element(By.XPATH, var_app.homepage).click()
        except:
            login_app.login.login_v3(self, "43E02740", "12341234")
            var_app.driver.find_element(By.XPATH, var_app.homepage).click()

        var_app.driver.swipe(720, 375, 180, 375, 500)
        time.sleep(1)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang Chủ - Yêu thích - Thêm",
                                              var_app.check_more_search, "Thêm lái xe", "_TrangChu_Them_TimKiem.png")


        var_app.driver.swipe(180, 375, 720, 375, 500)
        time.sleep(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.more).click()
        except:
            var_app.driver.swipe(180, 375, 720, 375, 500)
            time.sleep(1)
            var_app.driver.find_element(By.XPATH, var_app.more).click()
        time.sleep(2)
        var_app.driver.tap([(864, 534)])
        var_app.driver.find_element(By.XPATH, var_app.more_save).click()
        time.sleep(2)


    def mor_choose_max_favorite(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(7)
        except:
            pass
        var_app.driver.implicitly_wait(5)
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
            var_app.driver.find_element(By.XPATH, var_app.more_favorites_iconx1).click()
        except:
            pass
        time.sleep(1)


    def favorite_toward(self, code, eventname, result, towards, path_check, desire, path_image):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(5)
        try:
            var_app.driver.find_element(By.XPATH, var_app.homepage).click()
        except:
            login_app.login.login_v3(self, "43E02740", "12341234")
            var_app.driver.find_element(By.XPATH, var_app.homepage).click()

        time.sleep(1)
        var_app.driver.find_element(By.XPATH, towards).click()
        time.sleep(1.5)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Yêu thích",
                                              path_check, desire, path_image)
        time.sleep(1)
        var_app.driver.find_element(By.XPATH, var_app.homepage).click()
        time.sleep(1)














