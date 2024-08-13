import time

import appium.webdriver.common.touch_action
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
import homepage_app
from selenium.webdriver.common.keys import Keys





class image_video:

    def image_monitoring_back(self):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.image_monitoring_iconx0).click()
            time.sleep(1)
        except:
            pass
        try:
            var_app.driver.find_element(By.XPATH, var_app.image_monitoring_iconx1).click()
            time.sleep(1)
        except:
            pass
        try:
            var_app.driver.find_element(By.XPATH, var_app.image_monitoring_iconx2).click()
            time.sleep(1)
        except:
            pass

    def image_monitoring_select_group(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass
        var_app.driver.implicitly_wait(5)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_image_monitoring)
        except:
            image_video.image_monitoring_back(self)
            homepage_app.move_module(self, "", eventname, result, var_app.image_monitoring, 725, 765, 175, 765, 500, "", "", "", "")

        var_app.driver.find_element(By.XPATH, var_app.image_monitoring_select_group).click()
        time.sleep(2)
        var_app.driver.find_element(By.XPATH, var_app.image_monitoring_select_group_input).send_keys(var_app.data['home_page']['search_group'])
        time.sleep(2)
        # var_app.driver.tap([(178, 358)])
        # time.sleep(2)
        var_app.logging.info("--------------")
        var_app.logging.info("Trang chủ - Hình ảnh, video - Giám sát hình ảnh")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("False")
        var_app.driver.save_screenshot(var_app.imagepath + code + "_TrangChu_GiamSatHinhAnh_TimKiemNhom.png")
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Fail")
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 9, code + "_TrangChu_GiamSatHinhAnh_TimKiemNhom.png")


    def image_monitoring_select_group1(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass
        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.select_group_icon_all).click()
        except:
            image_video.image_monitoring_back(self)
            image_video.image_monitoring_select_group(self, "", "", "")
            var_app.driver.find_element(By.XPATH, var_app.select_group_icon_all).click()
        time.sleep(0.5)
        var_app.driver.find_element(By.XPATH, var_app.select_group_choose).click()
        time.sleep(2.5)
        module_other_app.write_result_displayed_try(code, eventname, result, "Trang chủ - Hình ảnh, video - Giám sát hình ảnh",
                                                    var_app.check_image_monitoring_select_group, "_TrangChu_GiamSatHinhAnh_ChonNhom.png")


    def image_monitoring_arrange_image(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass
        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_image_monitoring)
        except:
            image_video.image_monitoring_back(self)
            homepage_app.move_module(self, "", eventname, result, var_app.image_monitoring, 725, 765, 175, 765, 500, "", "", "", "")

        try:
            var_app.driver.find_element(By.XPATH, var_app.image_monitoring_arrange_image1).click()
        except:
            var_app.driver.find_element(By.XPATH, var_app.image_monitoring_arrange_image2).click()

        time.sleep(2)
        var_app.logging.info("--------------")
        var_app.logging.info("Trang chủ - Hình ảnh, video - Giám sát hình ảnh")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("True")
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Pass")

        try:
            var_app.driver.find_element(By.XPATH, var_app.image_monitoring_arrange_image1).click()
        except:
            var_app.driver.find_element(By.XPATH, var_app.image_monitoring_arrange_image2).click()
            time.sleep(2)


    def image_monitoring_refresh(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(7)
        except:
            pass
        var_app.driver.implicitly_wait(5)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_image_monitoring)
        except:
            image_video.image_monitoring_back(self)
            homepage_app.move_module(self, "", eventname, result, var_app.image_monitoring, 725, 765, 175, 765, 500, "", "", "", "")


        var_app.driver.find_element(By.XPATH, var_app.image_monitoring_refresh).click()
        time.sleep(1.5)
        var_app.logging.info("--------------")
        var_app.logging.info("Trang chủ - Hình ảnh, video - Giám sát hình ảnh")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("True")
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Pass")


    def image_monitoring_favorite(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass
        var_app.driver.implicitly_wait(5)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_image_monitoring)
        except:
            image_video.image_monitoring_back(self)
            homepage_app.move_module(self, "", eventname, result, var_app.image_monitoring, 725, 765, 175, 765, 500, "", "", "", "")

        var_app.driver.tap([(291, 448)])
        time.sleep(1.5)
        var_app.logging.info("--------------")
        var_app.logging.info("Trang chủ - Hình ảnh, video - Giám sát hình ảnh")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("True")
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Pass")
        var_app.driver.tap([(291, 448)])
        time.sleep(1.5)


    def image_monitoring_see_all_image(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(7)
        except:
            pass
        var_app.driver.implicitly_wait(5)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_image_monitoring)
        except:
            image_video.image_monitoring_back(self)
            homepage_app.move_module(self, "", eventname, result, var_app.image_monitoring, 725, 765, 175, 765, 500, "", "", "", "")

        var_app.driver.tap([(861, 448)])

        time.sleep(2)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Hình ảnh, video - Giám sát hình ảnh_Camera",
                                              var_app.camera, "CAMERA", "_TrangChu_HinhAnhVideo_GiamSatHinhAnh_XemTatCaAnh.png")


    def image_monitoring_see_all_image_search(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass
        var_app.driver.implicitly_wait(5)
        try:
            print("n0")
            var_app.driver.find_element(By.XPATH, var_app.camera)
        except:
            image_video.image_monitoring_back(self)
            image_video.image_monitoring_see_all_image(self, "", "", "")
            print("n2")
        time.sleep(1.5)
        var_app.driver.find_element(By.XPATH, var_app.image_monitoring_see_all_image_search_icondown).click()
        print("n1")
        time.sleep(3)
        var_app.driver.tap([(180, 350)])
        time.sleep(2)

        module_other_app.write_result_displayed_try(code, eventname, result, "Trang chủ - Hình ảnh, video - Giám sát hình ảnh - Camera - Camera",
                                                var_app.check_image_monitoring_see_all_image_search, "_TrangChu_GiamSatHinhAnh_XemTatCaAnh_TimKiem.png")


    def image_monitoring_see_all_image_announce(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass
        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.camera)
        except:
            image_video.image_monitoring_back(self)
            image_video.image_monitoring_see_all_image(self, "", "", "")

        var_app.driver.find_element(By.XPATH, var_app.image_monitoring_see_all_image_announce).click()
        time.sleep(2)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Hình ảnh, video - Giám sát hình ảnh - Camera - Camera",
                                              var_app.check_image_monitoring_see_all_image_announce, "Các xe sử dụng gói cước không tích hợp tính năng xem video sẽ không được hiển thị trên tính năng này", "_TrangChu_HinhAnhVideo_GiamSatHinhAnh_IconThongBao.png")

        try:
            var_app.driver.find_element(By.XPATH, var_app.IGREE).click()
            time.sleep(1)
        except:
            pass

        try:
            var_app.driver.find_element(By.XPATH, var_app.image_monitoring_see_all_image_announce_iconx).click()
            time.sleep(1)
        except:
            pass


    def image_monitoring_search(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(5)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_image_monitoring)
        except:
            image_video.image_monitoring_back(self)
            homepage_app.move_module(self, "", eventname, result, var_app.image_monitoring, 725, 765, 175, 765, 500, "", "", "", "")


        var_app.driver.find_element(By.XPATH, var_app.image_monitoring_search2).click()
        time.sleep(2)
        var_app.driver.find_element(By.XPATH, var_app.image_monitoring_search_input).send_keys(var_app.data['home_page']['search_image_monitoring'])
        time.sleep(2)
        var_app.driver.tap([(170, 355)])
        time.sleep(2)
        module_other_app.write_result_displayed_try(code, eventname, result, "Trang chủ - Hình ảnh, video - Giám sát hình ảnh",
                                                var_app.check_image_monitoring_search, "_TrangChu_HinhAnhVideo_GiamSatHinhAnh_TimKiem.png")


    def image_monitoring_select(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(5)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_image_monitoring)
        except:
            image_video.image_monitoring_back(self)
            homepage_app.move_module(self, "", eventname, result, var_app.image_monitoring, 725, 765, 175, 765, 500, "", "", "", "")

        time.sleep(2)
        var_app.driver.tap([(200, 725)])
        time.sleep(2)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Hình ảnh, video - Giám sát hình ảnh",
                                              var_app.check_image_monitoring_select, "CHI TIẾT ẢNH", "_TrangChu_HinhAnhVideo_GiamSatHinhAnh_ClickAnh.png")


    def check_image_monitoring_select(self, code, eventname, result, path_check, path_image):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass
        module_other_app.write_result_text_try_if_other(code, eventname, result, "Trang chủ - Hình ảnh, video - Giám sát hình ảnh",
                                              path_check, "None", path_image)


    def check_image_monitoring_select1(self, code, eventname, result, path_check, path_image):
        var_app.driver.implicitly_wait(1)
        var_app.logging.info("--------------")
        var_app.logging.info("Trang chủ - Hình ảnh, video - Giám sát hình ảnh")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        try:
            check_text = var_app.driver.find_element(By.XPATH, path_check).get_attribute("content-desc")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 11, check_text)
            var_app.logging.info(check_text)
            if check_text != "None":
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


        try:
            var_app.driver.find_element(By.XPATH, var_app.image_monitoring_iconx1).click()
            time.sleep(1.3)
        except:
            pass

        try:
            var_app.driver.find_element(By.XPATH, var_app.image_monitoring_iconx2).click()
            time.sleep(1.3)
        except:
            pass










    def camera_monitoring_back(self):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.camera_monitoring_back1).click()
            time.sleep(1.2)
        except:
            pass

        try:
            var_app.driver.find_element(By.XPATH, var_app.camera_monitoring_back2).click()
            time.sleep(1.2)
        except:
            pass


    def camera_monitoring_search(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(5)
        try:
            var_app.driver.find_element(By.XPATH, var_app.camera_monitoring_search).click()
        except:
            image_video.camera_monitoring_back(self)
            homepage_app.move_module(self, "", "", "", var_app.camera_monitoring, 725, 765, 175, 765, 500, "", "", "", "")
            var_app.driver.find_element(By.XPATH, var_app.camera_monitoring_search).click()
        time.sleep(2)
        var_app.driver.find_element(By.XPATH, var_app.camera_monitoring_search_input).send_keys(var_app.data['image_video']['search'])
        time.sleep(2)
        var_app.driver.tap([(156, 356)])
        time.sleep(3)
        module_other_app.write_result_text_try_if_other(code, eventname, result, "Trang chủ - Giám sát camera",
                                              var_app.check_camera_monitoring_search, "None", "_TrangChu_GiamSatCamera.png")


    def camera_monitoring_check_info(self, code, eventname, result, path_text, name_image):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass
        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_camera_monitoring_search)
        except:
            image_video.camera_monitoring_back(self)
            image_video.camera_monitoring_search(self, "", "", "")

        module_other_app.write_result_text_try_if_other(code, eventname, result, "Trang chủ - Giám sát nhiều camera - Check thông tin xe",
                                              path_text, "None", name_image)


    def camera_monitoring_check_icon(self, code, eventname, result, button, desire, path_image):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass
        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_camera_monitoring_search)
        except:
            image_video.camera_monitoring_back(self)
            image_video.camera_monitoring_search(self, "", "", "")


        try:
            var_app.driver.find_element(By.XPATH, button).click()
        except:
            pass
        time.sleep(1)
        try:
            var_app.driver.find_element(By.XPATH, button).click()
        except:
            pass
        var_app.logging.info("--------------")
        var_app.logging.info("Trang chủ - Giám sát camera - Check icon chức năng camera")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        if desire == "True":
            var_app.logging.info("True")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Pass")
        if desire == "False":
            var_app.logging.info("False")
            var_app.driver.save_screenshot(var_app.imagepath + code + path_image)
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Fail")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 9, code + path_image)


    def camera_monitoring_check_icon_close(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass
        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_camera_monitoring_search)
        except:
            image_video.camera_monitoring_back(self)
            image_video.camera_monitoring_search(self, "", "", "")

        try:
            var_app.driver.find_element(By.XPATH, var_app.camera_monitoring_check_icon_close).click()
            time.sleep(1.5)
        except:
            pass

        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Giám sát camera - Check icon chức năng camera",
                                              var_app.check_camera_monitoring_check_icon_close, "Bạn thực sự muốn xóa kênh camera đang xem này không?", "_TrangChu_GiamSatCamera_IconDongCamera.png")

        try:
            var_app.driver.find_element(By.XPATH, var_app.camera_monitoring_check_icon_igree).click()
            time.sleep(1.5)
        except:
            pass

        try:
            var_app.driver.find_element(By.XPATH, var_app.camera_monitoring_check_icon_close).click()
            time.sleep(1.5)
            var_app.driver.find_element(By.XPATH, var_app.camera_monitoring_check_icon_igree).click()
            time.sleep(1.5)
        except:
            pass





    def camera_monitoring_add_camera(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(5)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_camera_monitoring)
        except:
            image_video.camera_monitoring_back(self)
            homepage_app.move_module(self, "", "", "", var_app.camera_monitoring, 725, 765, 175, 765, 500, "", "", "", "")


        var_app.driver.find_element(By.XPATH, var_app.camera_monitoring_add_camera).click()
        time.sleep(2.5)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Giám sát camera",
                                              var_app.check_camera_monitoring_add_camera, "THÊM CAMERA", "_TrangChu_HinhAnhVideo_GiamSatCamera_IconThemcamera.png")

    def camera_monitoring_add_camera_search(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass
        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_camera_monitoring_add_camera)
        except:
            image_video.camera_monitoring_back(self)
            image_video.camera_monitoring_add_camera(self, "", "", "")


        var_app.driver.find_element(By.XPATH, var_app.camera_monitoring_add_camera_search).send_keys(var_app.data['image_video']['search_add_camera'])
        time.sleep(2)

        var_app.driver.tap([(80, 570)])
        var_app.driver.tap([(220, 570)])
        var_app.driver.tap([(80, 760)])
        var_app.driver.tap([(220, 760)])
        var_app.driver.tap([(80, 870)])
        var_app.driver.tap([(220, 870)])
        var_app.driver.tap([(80, 1060)])
        var_app.driver.tap([(220, 1060)])
        var_app.driver.tap([(87, 1254)])
        var_app.driver.tap([(220, 1254)])








        var_app.driver.find_element(By.XPATH, var_app.IGREE).click()
        time.sleep(3)



        module_other_app.write_result_text_try_if_other(code, eventname, result, "Trang chủ - Hình ảnh, video - Giám sát camera - Thêm camera",
                                              var_app.checkcamera_vehicle, "None", "_TrangChu_GiamSatCamera_IconThemcamera_TimKiem.png")
        time.sleep(0.5)
        var_app.driver.find_element(By.XPATH, var_app.camera_monitoring_add_camera).clear()
        time.sleep(1.5)

    def camera_monitoring_on_the_camera(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass
        var_app.driver.implicitly_wait(3)

        try:
            var_app.driver.find_element(By.XPATH, var_app.camera_monitoring_add_camera).click()
            time.sleep(2.5)
        except:
            pass



        try:
            var_app.driver.find_element(By.XPATH, var_app.camera_monitoring_on_the_camera)
        except:
            image_video.camera_monitoring_back(self)
            image_video.camera_monitoring_add_camera_search(self, "", "", "")



        checkcamera = var_app.driver.find_element(By.XPATH, var_app.camera_monitoring_on_the_camera)
        print("lần 1" + checkcamera.text)
        if checkcamera.text == "OFF":
            checkcamera.click()
            time.sleep(1)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Giám sát camera - Thêm camera",
                                              var_app.camera_monitoring_on_the_camera, "ON", "_TrangChu_GiamSatCamera_ThemCamera_BatTat.png")

        checkcamera = var_app.driver.find_element(By.XPATH, var_app.camera_monitoring_on_the_camera)
        print("lần 1" + checkcamera.text)
        if checkcamera.text == "ON":
            checkcamera.click()
            time.sleep(1)
            print("lần 2" + checkcamera.text)

    def camera_monitoring_reset(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass
        var_app.driver.implicitly_wait(5)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_camera_monitoring_add_camera)
        except:
            image_video.camera_monitoring_back(self)
            image_video.camera_monitoring_add_camera(self, "", "", "")
        try:
            var_app.driver.find_element(By.XPATH, var_app.camera_monitoring_add_camera_reset).click()
        except:
            var_app.driver.find_element(By.XPATH, var_app.camera_monitoring_add_camera_reset1).click()

        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Giám sát camera - Thêm camera",
                                              var_app.RESET, "ĐẶT LẠI", "_TrangChu_GiamSatCamera_ThemCamera_DatLai.png")


        try:
            checkdata = var_app.driver.find_element(By.XPATH, var_app.RESET).text
            if checkdata == "Đặt lại":
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 11, "Đang bị chữ hoa chữ thường")
        except:
            pass


        time.sleep(2)
        var_app.driver.find_element(By.XPATH, var_app.IGREE).click()
        time.sleep(3)

        image_video.camera_monitoring_back(self)










    def see_again_video_back(self):
        var_app.driver.implicitly_wait(0.2)
        try:
            var_app.driver.find_element(By.XPATH, var_app.see_again_video_back1).click()
            time.sleep(1)
        except:
            pass

        try:
            var_app.driver.find_element(By.XPATH, var_app.see_again_video_back2).click()
            time.sleep(1)
        except:
            pass

        try:
            var_app.driver.find_element(By.XPATH, var_app.see_again_video_back3).click()
            time.sleep(1)
        except:
            pass


    def see_again_video_search(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_see_again_video)
        except:
            image_video.see_again_video_back(self)
            homepage_app.move_module(self, "", "", "", var_app.see_again_video, 725, 765, 175, 765, 500, "", "", "", "")

        var_app.driver.find_element(By.XPATH, var_app.see_again_video_search).click()
        time.sleep(2)
        var_app.driver.find_element(By.XPATH, var_app.see_again_video_search_input).send_keys(var_app.data['image_video']['search'])
        time.sleep(1)
        var_app.driver.find_element(By.XPATH, var_app.check_see_again_search_vehicle_all).click()
        time.sleep(1)
        var_app.driver.find_element(By.XPATH, var_app.check_see_again_search_vehicle_select).click()
        time.sleep(1.5)
        var_app.driver.find_element(By.XPATH, var_app.check_see_again_search_vehicle_iconsearch).click()
        time.sleep(2)
        var_app.logging.info("--------------")
        var_app.logging.info("Trang chủ - Xem lại video - Tổng quan")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        try:
            check_text = var_app.driver.find_element(By.XPATH, var_app.check_see_again_video_search1).text
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 11, check_text)
            var_app.logging.info(check_text)
            print(check_text[0:4])
            if check_text[0:4] == var_app.data['image_video']['search']:
                var_app.logging.info("True")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Pass")
            else:
                var_app.logging.info("False")
                var_app.driver.save_screenshot(var_app.imagepath + code + "_TrangChu_XemLaiVideo_TimKiem.png")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Fail")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 9, code + "_TrangChu_XemLaiVideo_TimKiem.png")
        except:
            var_app.logging.info("False")
            var_app.driver.save_screenshot(var_app.imagepath + code + "_TrangChu_XemLaiVideo_TimKiem.png")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Fail")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 9, code + "_TrangChu_XemLaiVideo_TimKiem.png")


    def see_again_video_search_see_video(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass


        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_see_again_video)
        except:
            image_video.see_again_video_search(self, "", "", "")

        var_app.driver.tap([(150, 500)])
        time.sleep(2)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Xem lại video - Tổng quan",
                                              var_app.check_see_again_video_search_see_video, "XEM LẠI VIDEO", "_TrangChu_XemLaiVideo_ClickVaoVideo.png")








    def see_again_video_see_device_search(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_see_again_video_search_see_video)
        except:
            image_video.see_again_video_back(self)
            homepage_app.move_module(self, "", eventname, result, var_app.see_again_video, 725, 765, 175, 765, 500, "", "", "", "")
            var_app.driver.find_element(By.XPATH, var_app.see_again_video_see_device).click()
            # image_video.see_again_video_search_see_video(self, "", "", "")

        var_app.driver.implicitly_wait(2)
        n = 210
        while (n < 850):
            n += 150
            try:
                var_app.driver.find_element(By.XPATH, var_app.see_again_video_see_device_search).click()
                time.sleep(2)
                var_app.driver.tap([(200, n)])

                time.sleep(2)
                var_app.driver.find_element(By.XPATH, var_app.see_again_video_see_device_search_icon).click()
                time.sleep(2)
                var_app.driver.find_element(By.XPATH, var_app.see_again_video_see_device_see_many_channel).click()
                time.sleep(2)
                var_app.logging.info("--------------")
                var_app.logging.info("Trang chủ - Xem lại video - Tổng quan - Xem thiết bị")
                var_app.logging.info("Mã - " + code)
                var_app.logging.info("Tên sự kiện - " + eventname)
                try:
                    check_video = var_app.driver.find_element(By.XPATH, var_app.check_see_again_video1).text
                    print("check text:" + check_video)
                    var_app.driver.find_element(By.XPATH, var_app.see_again_video_see_device_see_many_channel_iconx).click()
                    time.sleep(1.5)
                    module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "")
                    module_other_app.writeData(var_app.checklistpath, "Checklist", code, 9, "")
                    var_app.logging.info("True")
                    module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Pass")
                    module_other_app.writeData(var_app.checklistpath, "Checklist", code, 11, check_video)

                    break
                except:
                    var_app.driver.find_element(By.XPATH, var_app.see_again_video_see_device_see_many_channel_iconx).click()
                    time.sleep(1.5)
                    var_app.logging.info("False")
                    var_app.driver.save_screenshot(var_app.imagepath + code + "_TrangChu_XemLaiVideo_XemThietBi.png")
                    module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Fail")
                    module_other_app.writeData(var_app.checklistpath, "Checklist", code, 9, code + "_TrangChu_XemLaiVideo_XemThietBi.png")
            except:
                print("n3")
                pass


    def see_again_video_see_device_see_many_channel(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass


        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_see_again_video_search_see_video)
        except:
            image_video.see_again_video_see_device_search(self, "", "", "")

        var_app.driver.find_element(By.XPATH, var_app.see_again_video_see_device_see_many_channel).click()
        time.sleep(2)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Xem lại video - Tổng quan - Xem thiết bị",
                                              var_app.check_see_again_video_see_device_see_many_channel, "XEM LẠI VIDEO - TỔNG QUAN", "_TrangChu_XemLaiVideo_XemThietBi_XemNhieuKenhCuaPhuongTien.png")


    def see_again_manny_video_iconselect_channel(self, code, eventname, result):
        var_app.driver.implicitly_wait(5)
        try:
            var_app.driver.find_element(By.XPATH, var_app.see_again_manny_video_iconselect_channel).click()
        except:
            image_video.see_again_video_see_device_see_many_channel(self, "", "", "")
            var_app.driver.find_element(By.XPATH, var_app.see_again_manny_video_iconselect_channel).click()
        time.sleep(2)


        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Xem lại video - Tổng quan - Xem thiết bị",
                                              var_app.check_see_again_manny_video_iconselect_channel, "XEM LẠI VIDEO", "_TrangChu_XemLaiVideo_XemThietBi_XemNhieuKenhCuaPhuongTien_IconChonKenh.png")

        try:
            var_app.driver.find_element(By.XPATH, var_app.see_again_manny_video_iconselect_channel_iconx).click()
            time.sleep(2)
        except:
            pass


    def see_again_video_see_device_play_automatically(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_see_again_video1)   #Biển số xe(XEM LẠI VIDEO - TỔNG QUAN)
        except:
            image_video.see_again_video_see_device_see_many_channel(self, "", "", "")

        var_app.logging.info("--------------")
        var_app.logging.info("Trang chủ - Xem lại video - Tổng quan - Xem thiết bị - Xem nhiều kênh của phương tiện")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_play_automatically2)        # bật  checkbox
        except:
            var_app.driver.find_element(By.XPATH, var_app.check_play_automatically1).click()
        time.sleep(1)


        try:
            var_app.driver.find_element(By.XPATH, var_app.check_play_automatically2).click()       #tắt checkbox
            time.sleep(1.5)
        except:
            pass

        try:
            var_app.driver.find_element(By.XPATH, var_app.check_play_automatically2)            #
            var_app.logging.info("False")
            var_app.driver.save_screenshot(var_app.imagepath + code + "_TrangChu_XemLaiVideo_XemThietBi_XemNhieuKenhCuaPhuongTien_PhatTuDong.png")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Fail")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 9, code + "_TrangChu_XemLaiVideo_XemThietBi_XemNhieuKenhCuaPhuongTien_PhatTuDong.png")

        except:
            var_app.logging.info("True")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Pass")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 11, "Đã tắt checkbox")




        # check_play_automatically = var_app.driver.find_element(By.XPATH, var_app.check_play_automatically).get_attribute("checked")
        # print("checkbox: ", check_play_automatically)
        # if check_play_automatically == "false":
        #     var_app.driver.find_element(By.XPATH, var_app.check_play_automatically).click()
        # time.sleep(0.5)
        # var_app.logging.info("--------------")
        # var_app.logging.info("Trang chủ - Xem lại video - Tổng quan - Xem thiết bị")
        # var_app.logging.info("Mã - " + code)
        # var_app.logging.info("Tên sự kiện - " + eventname)
        # var_app.logging.info("Kết quả - " + result)
        # check_play_automatically1 = var_app.driver.find_element(By.XPATH, var_app.check_play_automatically).get_attribute("checked")
        # if check_play_automatically1 == "true":
        #     var_app.logging.info("True")
        #     module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Pass")
        # else:
        #     var_app.logging.info("False")
        #     var_app.driver.save_screenshot(var_app.imagepath + code + "_TrangChu_XemLaiVideo_XemThietBi_XemNhieuKenhCuaPhuongTien_PhatTuDong.png")
        #     module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Fail")
        #     module_other_app.writeData(var_app.checklistpath, "Checklist", code, 9, code + "_TrangChu_XemLaiVideo_XemThietBi_XemNhieuKenhCuaPhuongTien_PhatTuDong.png")
        #
        #
        # check_play_automatically = var_app.driver.find_element(By.XPATH, var_app.check_play_automatically).get_attribute("checked")
        # print("checkbox: ", check_play_automatically)
        # if check_play_automatically == "true":
        #     var_app.driver.find_element(By.XPATH, var_app.check_play_automatically).click()


    def see_again_video_see_device_detail(self, code, eventname, result, path_check, desire, path_image):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_see_again_video_see_device_see_many_channel)
        except:
            image_video.see_again_video_see_device_see_many_channel(self, "", "", "")

        module_other_app.write_result_text_try_if_other(code, eventname, result, "Trang chủ - Xem lại video - Tổng quan - Xem thiết bị - Xem nhiều kênh của phương tiện",
                                              path_check, desire, path_image)


        var_app.driver.implicitly_wait(1)

        if path_image == "_TrangChu_XemLaiVideo_XemThietBi_XemNhieuKenhCuaPhuongTien_DiaChi.png":
            var_app.driver.find_element(By.XPATH, var_app.see_again_video_see_device_see_many_channel_iconx).click()
            time.sleep(2)

        if path_image == "_TrangChu_XemLaiVideo_XemThietBi_ClickVideo_Kenh.png":
            var_app.driver.find_element(By.XPATH, var_app.see_again_video_see_device_see_many_channel_iconx).click()
            time.sleep(2)


    def see_again_video_see_device_detail1(self, code, eventname, result, path_check, desire, path_image):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_see_again_video_see_device_see_many_channel)
        except:
            image_video.see_again_video_see_device_seevideo(self, "", "", "")

        module_other_app.write_result_text_try_if_other(code, eventname, result, "Trang chủ - Xem lại video - Tổng quan - Xem thiết bị - Click vo video",
                                              path_check, desire, path_image)


        var_app.driver.implicitly_wait(1)

        if path_image == "_TrangChu_XemLaiVideo_XemThietBi_XemNhieuKenhCuaPhuongTien_DiaChi.png":
            var_app.driver.find_element(By.XPATH, var_app.see_again_video_see_device_see_many_channel_iconx).click()
            time.sleep(2)

        if path_image == "_TrangChu_XemLaiVideo_XemThietBi_ClickVideo_Kenh.png":
            var_app.driver.find_element(By.XPATH, var_app.see_again_video_see_device_see_many_channel_iconx).click()
            time.sleep(2)


    def see_again_video_see_device_seevideo(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.tap([(385, 675)])
            time.sleep(2)
            var_app.driver.find_element(By.XPATH, var_app.see_again_video_see_device_seevideo_vehicle)
        except:
            image_video.see_again_video_see_device_search(self, "", "", "")
            var_app.driver.tap([(385, 675)])
        time.sleep(2)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Xem lại video - Tổng quan - Xem thiết bị",
                                              var_app.check_see_again_video_see_device_seevideo, "XEM LẠI VIDEO - TỔNG QUAN", "_TrangChu_XemLaiVideo_XemThietBi_XemVideo.png")


    def see_again_video_see_again_video_iconn(self, code, eventname, result, path_icon, desire, path_image):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.find_element(By.XPATH, path_icon).click()
        except:
            if path_image == "_TrangChu_XemLaiVideo_XemThietBi_ClickVideo_IconToanManHinh.png":
                pass
            else:
                image_video.see_again_video_see_device_seevideo(self, "", "", "")
        time.sleep(1)
        var_app.logging.info("--------------")
        var_app.logging.info("Trang chủ - Xem lại video - Tổng quan - Xem thiết bị - Click vào video")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        if desire == "True":
            var_app.logging.info("True")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Pass")
        else:
            var_app.logging.info("False")
            var_app.driver.save_screenshot(var_app.imagepath + code + path_image)
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Fail")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 9, code + path_image)
        try:
            var_app.driver.find_element(By.XPATH, path_icon).click()
            time.sleep(1)
        except:
            pass


    def see_again_video_see_again_video_iconcloud(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass


        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.see_again_video_see_again_video_iconcloud).click()
        except:
            image_video.see_again_video_see_device_seevideo(self, "", "", "")
            var_app.driver.find_element(By.XPATH, var_app.see_again_video_see_again_video_iconcloud).click()
        time.sleep(2)

        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Xem lại video - Tổng quan - Xem thiết bị - Click vào video",
                                              var_app.check_see_again_video_see_again_video_iconcloud, "TẢI VỀ SERVER",
                                                  "_TrangChu_XemLaiVideo_XemThietBi_ClickVideo_IconCloud.png")

        try:
            var_app.driver.find_element(By.XPATH, var_app.see_again_video_see_again_video_iconcloud_iconx).click()
            time.sleep(2)
        except:
            pass


    def see_again_video_see_device_icon_icloud(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass


        var_app.driver.implicitly_wait(3)
        var_app.driver.tap([(845, 934)])
        time.sleep(2)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_see_again_video_see_again_video_iconcloud)
        except:
            image_video.see_again_video_see_device_search(self, "", "", "")
            var_app.driver.tap([(845, 934)])
            time.sleep(2)

        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Xem lại video - Tổng quan - Xem thiết bị",
                                              var_app.check_see_again_video_see_again_video_iconcloud, "TẢI VỀ SERVER", "_TrangChu_XemLaiVideo_XemThietBi_IconCloud.png")

        try:
            var_app.driver.find_element(By.XPATH, var_app.download_cloud).click()
            time.sleep(1.5)

        except:
            pass

        try:
            var_app.driver.find_element(By.XPATH, var_app.IGREE).click()
            time.sleep(1.5)
        except:
            pass

        try:
            var_app.driver.find_element(By.XPATH, var_app.download_cloud_close).click()
            time.sleep(2)
        except:
            pass


    def see_again_video_dowload_and_cloud_search(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.see_again_video_dowload_and_cloud).click()
        except:
            image_video.see_again_video_back(self)
            homepage_app.move_module(self, "", eventname, result, var_app.see_again_video, 725, 765, 175, 765, 500, "", "", "", "")
            var_app.driver.find_element(By.XPATH, var_app.see_again_video_dowload_and_cloud).click()
        time.sleep(2)
        var_app.driver.find_element(By.XPATH, var_app.see_again_video_dowload_and_cloud_select_vehicle).click()
        time.sleep(2)
        var_app.driver.tap([(200, 350)])
        time.sleep(2)
        var_app.driver.find_element(By.XPATH, var_app.see_again_video_dowload_and_cloud_search).click()
        time.sleep(1.5)
        var_app.logging.info("--------------")
        var_app.logging.info("Trang chủ - Xem lại video - Tổng quan - Xem thiết bị")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("True")
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Pass")
        image_video.see_again_video_back(self)










    def see_image_camera_back(self):
        var_app.driver.implicitly_wait(0.2)
        try:
            var_app.driver.find_element(By.XPATH, var_app.see_image_camera_back5).click()
            time.sleep(1)
        except:
            pass
        try:
            var_app.driver.find_element(By.XPATH, var_app.see_image_camera_back1).click()
            time.sleep(1)
        except:
            pass
        try:
            var_app.driver.find_element(By.XPATH, var_app.see_image_camera_back2).click()
            time.sleep(1)
        except:
            pass

        try:
            var_app.driver.find_element(By.XPATH, var_app.see_image_camera_back4).click()
            time.sleep(1)
        except:
            pass
        try:
            var_app.driver.find_element(By.XPATH, var_app.see_image_camera_back3).click()
            time.sleep(1)
        except:
            pass


    def see_image_camera_search(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_see_nd10)
        except:
            image_video.see_image_camera_back(self)
            homepage_app.move_module(self, "", "", "", var_app.see_nd10, 725, 765, 175, 765, 500, "", "", "", "")


        var_app.driver.implicitly_wait(1)
        n = 210
        while (n < 1000):
            n += 150
            try:
                var_app.driver.find_element(By.XPATH, var_app.see_image_camera_search_select).click()
                time.sleep(2)
                var_app.driver.tap([(200, n)])
                time.sleep(2)
                var_app.driver.find_element(By.XPATH, var_app.see_image_camera_search_select_icon).click()
                time.sleep(2)
                check_data = var_app.driver.find_element(By.XPATH, var_app.check_see_image_camera_search).text
                print(check_data)
                if check_data != "Tổng số hình ảnh: 0":
                    print("đã click vào tọa độ 200, {}".format(n))
                    break
                else:
                    print("đã click vào tọa độ 200, {}".format(n))
            except:
                print("đã click vào tọa độ 200, {}".format(n))
                pass

        module_other_app.write_result_text_try_if_other(code, eventname, result, "Trang chủ - Xem ảnh Camera - NĐ10",
                                              var_app.check_see_image_camera_search, "Tổng số hình ảnh: 0", "_TrangChu_XemAnhCamera_TimKiem.png")


    def see_image_camera_icon_notification(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_see_nd10)
        except:
            image_video.see_image_camera_back(self)
            homepage_app.move_module(self, "", "", "", var_app.see_nd10, 725, 765, 175, 765, 500, "", "", "", "")

        var_app.driver.find_element(By.XPATH, var_app.see_image_camera_icon_notification).click()
        time.sleep(1.5)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Xem ảnh Camera - NĐ10",
                                              var_app.check_see_image_camera_icon_notification,
                                                  "Các xe sử dụng gói cước không tích hợp tính năng xem video sẽ không được hiển thị trên tính năng này", "_TrangChu_XemAnhCamera_IconThongBao.png")

        try:
            var_app.driver.find_element(By.XPATH, var_app.IGREE).click()
            time.sleep(1.5)
        except:
            pass


    def see_image_camera_select_image(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(3)
        try:
            check_data = var_app.driver.find_element(By.XPATH, var_app.check_see_image_camera_search).text
            if check_data != "Tổng số hình ảnh: 0":
                var_app.driver.tap([(200, 600)])
            else:
                image_video.see_image_camera_search(self, "", "", "")
                var_app.driver.tap([(200, 600)])
        except:
            image_video.see_image_camera_search(self, "", "", "")
            var_app.driver.tap([(200, 600)])

        time.sleep(2.5)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Xem ảnh Camera - NĐ10",
                                              var_app.check_see_image_camera_select_image, "CHI TIẾT ẢNH", "_TrangChu_XemAnhCamera_ClickVaoAnh.png")


    def see_image_camera_select_image_detail_vehicle(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_see_image_camera_select_image)
        except:
            image_video.see_image_camera_search(self, "", "", "")

        var_app.logging.info("--------------")
        var_app.logging.info("Trang chủ - Xem ảnh Camera - NĐ10")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        try:
            check_text = var_app.driver.find_element(By.XPATH, var_app.check_see_image_camera_vehicle).get_attribute("content-desc")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 11, check_text)
            var_app.logging.info(check_text)
            if check_text != "":
                var_app.logging.info("True")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Pass")
            else:
                var_app.logging.info("False")
                var_app.driver.save_screenshot(var_app.imagepath + code + "_TrangChu_XemAnhCamera_ClickVaoAnh_BienSo.png")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Fail")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 9, code + "_TrangChu_XemAnhCamera_ClickVaoAnh_BienSo.png")
        except:
            var_app.logging.info("False")
            var_app.driver.save_screenshot(var_app.imagepath + code + "_TrangChu_XemAnhCamera_ClickVaoAnh_BienSo.png")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Fail")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 9, code + "_TrangChu_XemAnhCamera_ClickVaoAnh_BienSo.png")


    def see_image_camera_select_image_detail(self, code, eventname, result, path_check, desire, path_image):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_see_image_camera_select_image)
        except:
            image_video.see_image_camera_select_image(self, "", "", "")

        module_other_app.write_result_text_try_if_other(code, eventname, result, "Trang chủ - Xem ảnh Camera - NĐ10",
                                              path_check, desire, path_image)



    def see_image_camera_select_image_icon_download(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_see_image_camera_select_image)
        except:
            image_video.see_image_camera_select_image(self, "", "", "")

        var_app.driver.find_element(By.XPATH, var_app.see_image_camera_select_image_icon_download).click()
        time.sleep(2)

        try:
            check_data = var_app.driver.find_element(By.XPATH, var_app.check_see_image_camera_select_image_icon_download).text
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 11, check_data)
        except:
            pass
        module_other_app.write_result_displayed_try(code, eventname, result, "Quản trị - Danh sách xe",
                                                var_app.check_see_image_camera_select_image_icon_download, "_TrangChu_XemAnhCamera_ClickVaoAnh_IconTaiXuong.png")

        var_app.driver.press_keycode(4)
        time.sleep(1)



        image_video.see_image_camera_back(self)




        # var_app.driver.implicitly_wait(1)
        # if path_image == "_TrangChu_XemAnhCamera_ClickVaoAnh_DiaChi.png":
        #     var_app.driver.find_element(By.XPATH, var_app.see_image_camera_select_image_detail_iconx).click()
        #     time.sleep(2)









    def export_video_back(self):
        var_app.driver.implicitly_wait(0.2)
        try:
            var_app.driver.find_element(By.XPATH, var_app.export_video_back1).click()
            time.sleep(1.3)
        except:
            pass
        try:
            var_app.driver.find_element(By.XPATH, var_app.export_video_back2).click()
            time.sleep(1.3)
        except:
            pass
        try:
            var_app.driver.find_element(By.XPATH, var_app.export_video_back3).click()
            time.sleep(1.3)
        except:
            pass


    def export_video_search(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_export_video)
        except:
            image_video.see_image_camera_back(self)
            homepage_app.move_module(self, "", "", "", var_app.export_video, 725, 765, 175, 765, 500, "", "", "", "")


        var_app.driver.implicitly_wait(1)
        n = 210
        while (n < 1000):
            n += 150
            try:
                var_app.driver.find_element(By.XPATH, var_app.export_video_search_select).click()
                time.sleep(2)
                var_app.driver.tap([(200, n)])
                time.sleep(2)
                check_data = var_app.driver.find_element(By.XPATH, var_app.check_export_video_search).text
                print(check_data)
                if check_data != "":
                    print("đã click vào tọa độ 200, {} thiết bị {}.".format(n, check_data))
                    break
                else:
                    print("đã click vào tọa độ 200, {} Không tìm thấy thiết bị {}.".format(n, check_data))
            except:
                print("đã click vào tọa độ 200, {} Không tìm thấy thiết bị.".format(n))
                pass

        module_other_app.write_result_text_try_if_other(code, eventname, result, "Trang chủ - Trích xuất video",
                                              var_app.check_export_video_search, "", "_TrangChu_XemAnhCamera_TimKiem.png")


    def export_video_Turn_on_wifi(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_export_video_search)
        except:
            image_video.export_video_search(self, "", "", "")

        var_app.driver.find_element(By.XPATH, var_app.export_video_Turn_on_wifi).click()
        time.sleep(1.5)
        var_app.logging.info("--------------")
        var_app.logging.info("Trang chủ - Trích xuất video")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        try:
            check_text = var_app.driver.find_element(By.XPATH, var_app.check_export_video_Turn_on_wifi).text
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 11, check_text)
            var_app.logging.info(check_text)
            if check_text[0:29] == "Bật wifi thiết bị thành công!":
                var_app.logging.info("True")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Pass")
            else:
                var_app.logging.info("False")
                var_app.driver.save_screenshot(var_app.imagepath + code + "_TrangChu_TrichXuat_TimKiem.png")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Fail")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 9, code + "_TrangChu_TrichXuat_TimKiem.png")
        except:
            var_app.logging.info("False")
            var_app.driver.save_screenshot(var_app.imagepath + code + "_TrangChu_TrichXuat_TimKiem.png")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Fail")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 9, code + "_TrangChu_TrichXuat_TimKiem.png")


        try:
            var_app.driver.find_element(By.XPATH, var_app.CANCEL).click()
            time.sleep(1.3)
        except:
            pass


    def export_video_help(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_export_video)
        except:
            image_video.see_image_camera_back(self)
            homepage_app.move_module(self, "", "", "", var_app.export_video, 725, 765, 175, 765, 500, "", "", "", "")

        var_app.driver.find_element(By.XPATH, var_app.export_video_help).click()
        time.sleep(4)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Trích xuất video",
                                              var_app.check_export_video_help, "[BA-SMARTCAMERA] HƯỚNG DẪN TRÍCH XUẤT DỮ LIỆU QUA USB TỪ CAMERA NGHỊ ĐỊNH 10",
                                            "_TrangChu_XemAnhCamera_XemHuongDan.png")

        var_app.driver.press_keycode(4)
        time.sleep(0.5)
        var_app.driver.press_keycode(4)
        image_video.export_video_back(self)














