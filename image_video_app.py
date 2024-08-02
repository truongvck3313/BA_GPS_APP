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
import homepage_app







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
            homepage_app.move_module(self, "Media01", eventname, result, var_app.image_monitoring, 725, 765, 175, 765, 500, "", "", "", "")

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
            homepage_app.move_module(self, "Media01", eventname, result, var_app.image_monitoring, 725, 765, 175, 765, 500, "", "", "", "")

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
            homepage_app.move_module(self, "Media01", eventname, result, var_app.image_monitoring, 725, 765, 175, 765, 500, "", "", "", "")


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
            homepage_app.move_module(self, "Media01", eventname, result, var_app.image_monitoring, 725, 765, 175, 765, 500, "", "", "", "")

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
            homepage_app.move_module(self, "Media01", eventname, result, var_app.image_monitoring, 725, 765, 175, 765, 500, "", "", "", "")

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
            homepage_app.move_module(self, "Media01", eventname, result, var_app.image_monitoring, 725, 765, 175, 765, 500, "", "", "", "")


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
            homepage_app.move_module(self, "Media01", eventname, result, var_app.image_monitoring, 725, 765, 175, 765, 500, "", "", "", "")

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

        var_app.logging.info("--------------")
        var_app.logging.info("Trang chủ - Giám sát camera - Thêm camera")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("False")
        var_app.driver.save_screenshot(var_app.imagepath + code + "_TrangChu_GiamSatCamera_ThemCamera_DatLai.png")
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Fail")
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 9, code + "_TrangChu_GiamSatCamera_ThemCamera_DatLai.png")
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 11, "Đang bị chữ hoa chữ thường")

        time.sleep(2)
        var_app.driver.find_element(By.XPATH, var_app.IGREE).click()
        time.sleep(3)

        image_video.camera_monitoring_back(self)















    def see_again_video_search(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(7)
        except:
            pass

        try:
            var_app.driver.find_element(By.XPATH, var_app.login_user)
            login_app.login.login_v3(self, "43E02740", "12341234")
        except:
            pass

        var_app.driver.implicitly_wait(5)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_see_again_video)
        except:
            homepage_app.move_module(self, "", "", "", var_app.see_again_video, 740, 650, 160, 650, 600, "", "", "", "")


        # name2 = var_app.driver.find_element(By.XPATH, var_app.see_again_video_search_name2).text
        var_app.driver.find_element(By.XPATH, var_app.check_see_again_search_vehicle).click()
        time.sleep(2)
        # var_app.driver.find_element(By.XPATH, var_app.check_see_again_search_vehicle_input).send_keys(name2)
        # time.sleep(2)
        # var_app.driver.find_element(By.XPATH, var_app.check_see_again_search_vehicle_radio1).click()
        var_app.driver.find_element(By.XPATH, var_app.check_see_again_search_vehicle_all).click()
        var_app.driver.find_element(By.XPATH, var_app.check_see_again_search_vehicle_select).click()
        time.sleep(1.5)
        var_app.driver.find_element(By.XPATH, var_app.check_see_again_search_vehicle_iconsearch).click()
        time.sleep(2)
        # module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Xem lại video - Tổng quan",
        #                                       var_app.see_again_video_search_name1, name2, "_TrangChu_XemLaiVideo_TimKiem.png")


        module_other_app.write_result_displayed_try(code, eventname, result, "Trang chủ - Xem lại video - Tổng quan",
                                                var_app.check_see_again_video_search, "_TrangChu_XemLaiVideo_TimKiem.png")

    def see_again_video_search_see_video(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(7)
        except:
            pass

        try:
            var_app.driver.find_element(By.XPATH, var_app.login_user)
            login_app.login.login_v3(self, "43E02740", "12341234")
        except:
            pass

        var_app.driver.implicitly_wait(5)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_see_again_video)
        except:
            homepage_app.move_module(self, "", "", "", var_app.see_again_video, 740, 650, 160, 650, 600, "", "", "", "")
        var_app.driver.find_element(By.XPATH, var_app.see_again_video_search_name1).click()
        time.sleep(2)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Xem lại video - Tổng quan",
                                              var_app.check_see_again_video_search_see_video, "Xem nhiều kênh của phương tiện", "_TrangChu_XemLaiVideo_Click_Video.png")


    def see_again_video_see_device_search(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(7)
        except:
            pass

        try:
            var_app.driver.find_element(By.XPATH, var_app.login_user)
            login_app.login.login_v3(self, "43E02740", "12341234")
        except:
            pass

        var_app.driver.implicitly_wait(5)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_see_again_video_search_see_video)
        except:
            homepage_app.move_module(self, "", "", "", var_app.see_again_video, 740, 650, 160, 650, 600, "", "", "", "")
            var_app.driver.find_element(By.XPATH, var_app.see_again_video_see_device).click()
        pass


        var_app.driver.implicitly_wait(0.05)
        n = 0
        while (n < 15):
            n += 1
            n = str(n)
            try:
                var_app.driver.find_element(By.XPATH, var_app.see_again_video_see_device_search).click()
                pathtenphuongtien = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[" + n + "]/android.view.ViewGroup/android.widget.TextView[1]"
                var_app.driver.find_element(By.XPATH, pathtenphuongtien).click()
                time.sleep(2)
                var_app.driver.find_element(By.XPATH, var_app.see_again_video_see_device_search_icon).click()
                time.sleep(2)
                check_video = var_app.driver.find_element(By.XPATH, var_app.check_see_again_video1).text
                print(check_video)
                if check_video != None:
                    module_other_app.writeData(var_app.checklistpath, "Checklist", code, 11, check_video)
                    break
            except:
                pass
            n = int(n)

        module_other_app.write_result_displayed_try(code, eventname, result, "Trang chủ - Xem lại video - Tổng quan - Xem thiết bị",
                                                var_app.check_see_again_video1, "_TrangChu_XemLaiVideo_XemThietBi.png")


    def see_again_video_see_device_see_many_channel(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(7)
        except:
            pass

        try:
            var_app.driver.find_element(By.XPATH, var_app.login_user)
            login_app.login.login_v3(self, "43E02740", "12341234")
        except:
            pass

        var_app.driver.implicitly_wait(5)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_see_again_video_search_see_video)
        except:
            homepage_app.move_module(self, "", "", "", var_app.see_again_video, 740, 650, 160, 650, 600, "", "", "", "")
            var_app.driver.find_element(By.XPATH, var_app.see_again_video_search_name1).click()

        var_app.driver.find_element(By.XPATH, var_app.see_again_video_see_device_see_many_channel).click()
        time.sleep(2)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Xem lại video - Tổng quan - Xem thiết bị",
                                              var_app.check_see_again_video_see_device_see_many_channel, "Xem lại nhiều video", "_TrangChu_XemLaiVideo_XemThietBi_XemNhieuKenhCuaPhuongTien.png")


    def see_again_manny_video_iconselect_channel(self, code, eventname, result):
        var_app.driver.implicitly_wait(5)
        try:
            var_app.driver.find_element(By.XPATH, var_app.see_again_manny_video_iconselect_channel).click()
        except:
            image_video.see_again_video_see_device_see_many_channel(self, "", "", "")

        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Xem lại video - Tổng quan - Xem thiết bị",
                                              var_app.check_see_again_manny_video_iconselect_channel, "Chọn kênh", "_TrangChu_XemLaiVideo_XemThietBi_XemNhieuKenhCuaPhuongTien_IconChonKenh.png")

        try:
            var_app.driver.find_element(By.XPATH, var_app.see_again_manny_video_iconselect_channel_iconselect).click()
            time.sleep(2)
        except:
            pass


    def see_again_video_see_device_play_automatically(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(7)
        except:
            pass

        try:
            var_app.driver.find_element(By.XPATH, var_app.login_user)
            login_app.login.login_v3(self, "43E02740", "12341234")
        except:
            pass

        var_app.driver.implicitly_wait(5)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_see_again_video_see_device_see_many_channel)
        except:
            image_video.see_again_video_see_device_see_many_channel(self, "", "", "")


        check_play_automatically = var_app.driver.find_element(By.XPATH, var_app.check_play_automatically).get_attribute("checked")
        print("checkbox: ", check_play_automatically)
        if check_play_automatically == "false":
            var_app.driver.find_element(By.XPATH, var_app.check_play_automatically).click()
        time.sleep(0.5)
        var_app.logging.info("--------------")
        var_app.logging.info("Trang chủ - Xem lại video - Tổng quan - Xem thiết bị")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        check_play_automatically1 = var_app.driver.find_element(By.XPATH, var_app.check_play_automatically).get_attribute("checked")
        if check_play_automatically1 == "true":
            var_app.logging.info("True")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Pass")
        else:
            var_app.logging.info("False")
            var_app.driver.save_screenshot(var_app.imagepath + code + "_TrangChu_XemLaiVideo_XemThietBi_XemNhieuKenhCuaPhuongTien_PhatTuDong.png")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Fail")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 9, code + "_TrangChu_XemLaiVideo_XemThietBi_XemNhieuKenhCuaPhuongTien_PhatTuDong.png")


        check_play_automatically = var_app.driver.find_element(By.XPATH, var_app.check_play_automatically).get_attribute("checked")
        print("checkbox: ", check_play_automatically)
        if check_play_automatically == "true":
            var_app.driver.find_element(By.XPATH, var_app.check_play_automatically).click()


    def see_again_video_see_device_detail(self, code, eventname, result, path_check, desire, path_image):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(7)
        except:
            pass

        try:
            var_app.driver.find_element(By.XPATH, var_app.login_user)
            login_app.login.login_v3(self, "43E02740", "12341234")
        except:
            pass

        var_app.driver.implicitly_wait(5)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_see_again_video_see_device_see_many_channel)
        except:
            image_video.see_again_video_see_device_see_many_channel(self, "", "", "")
            print("a1")

        module_other_app.write_result_text_try_if_other(code, eventname, result, "Trang chủ - Xem lại video - Tổng quan - Xem thiết bị",
                                              path_check, desire, path_image)

        if path_image == "_TrangChu_XemLaiVideo_XemThietBi_XemNhieuKenhCuaPhuongTien_DiaChi.png" or "_TrangChu_XemLaiVideo_XemThietBi_Kenh.png":
            var_app.driver.press_keycode(4)
            time.sleep(1.5)


    def see_again_video_see_device_seevideo(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(7)
        except:
            pass

        try:
            var_app.driver.find_element(By.XPATH, var_app.login_user)
            login_app.login.login_v3(self, "43E02740", "12341234")
        except:
            pass

        var_app.driver.implicitly_wait(5)
        try:
            var_app.driver.find_element(By.XPATH, var_app.see_again_video_see_device_seevideo).click()
        except:
            image_video.see_again_video_see_device_search(self, "", "", "")
            var_app.driver.find_element(By.XPATH, var_app.see_again_video_see_device_seevideo).click()
        time.sleep(2)
        module_other_app.write_result_text_try_if_other(code, eventname, result, "Trang chủ - Xem lại video - Tổng quan - Xem thiết bị",
                                              var_app.check_see_again_video_see_device_seevideo, None, "_TrangChu_XemLaiVideo_XemThietBi_XemVideo.png")


    def see_again_video_see_again_video_iconn(self, code, eventname, result, path_icon, desire, path_image):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(7)
        except:
            pass

        try:
            var_app.driver.find_element(By.XPATH, var_app.login_user)
            login_app.login.login_v3(self, "43E02740", "12341234")
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.find_element(By.XPATH, path_icon).click()
        except:
            pass
        time.sleep(1)
        var_app.logging.info("--------------")
        var_app.logging.info("Trang chủ - Xem lại video - Tổng quan - Xem thiết bị")
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
            time.sleep(7)
        except:
            pass

        try:
            var_app.driver.find_element(By.XPATH, var_app.login_user)
            login_app.login.login_v3(self, "43E02740", "12341234")
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.find_element(By.XPATH, var_app.see_again_video_see_again_video_iconcloud).click()
            time.sleep(2)
        except:
            pass
        module_other_app.write_result_text_try_if_other(code, eventname, result, "Trang chủ - Xem lại video - Tổng quan - Xem thiết bị",
                                              var_app.check_see_again_video_see_again_video_iconcloud, None,
                                                  "_TrangChu_XemLaiVideo_XemThietBi_ClickVideo_IconCloud.png")

        try:
            var_app.driver.find_element(By.XPATH, var_app.see_again_video_see_again_video_iconcloud_iconx).click()
            time.sleep(2)
        except:
            pass


    # def see_again_video_see_device_info(self, code, eventname, result, path_check, desire, path_image):
    #     var_app.driver.implicitly_wait(1)
    #     try:
    #         var_app.driver.find_element(By.XPATH, var_app.bagps).click()
    #         time.sleep(7)
    #     except:
    #         pass
    #
    #     try:
    #         var_app.driver.find_element(By.XPATH, var_app.login_user)
    #         login_app.login.login_v3(self, "43E02740", "12341234")
    #     except:
    #         pass
    #
    #     var_app.driver.implicitly_wait(5)
    #     try:
    #         var_app.driver.find_element(By.XPATH, var_app.see_again_video_icon_camera).click()
    #     except:
    #         image_video.see_again_video_see_device_search(self, "", "", "")
    #         var_app.driver.find_element(By.XPATH, var_app.see_again_video_see_device_seevideo).click()
    #     time.sleep(2)
    #     module_other_app.write_result_text_try_if_other(code, eventname, result, "Trang chủ - Xem lại video - Tổng quan - Xem thiết bị",
    #                                           path_check, desire, path_image)









    def see_again_video_see_device_icon_icloud(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(7)
        except:
            pass

        try:
            var_app.driver.find_element(By.XPATH, var_app.login_user)
            login_app.login.login_v3(self, "43E02740", "12341234")
        except:
            pass

        try:
            var_app.driver.find_element(By.XPATH, var_app.see_again_video_see_device_detail_iconx).click()
            time.sleep(1.5)
        except:
            pass

        var_app.driver.implicitly_wait(5)
        var_app.driver.find_element(By.XPATH, var_app.see_again_video_see_device_icon_icloud).click()
        time.sleep(2)
        module_other_app.write_result_text_try_if_other(code, eventname, result, "Trang chủ - Xem lại video - Tổng quan - Xem thiết bị",
                                              var_app.check_see_again_video_see_device_icon_icloud, None, "_TrangChu_XemLaiVideo_XemThietBi_IconCloud.png")

        try:
            var_app.driver.find_element(By.XPATH, var_app.download_cloud).click()
            time.sleep(2)
            var_app.driver.find_element(By.XPATH, var_app.download_cloud_close).click()
            time.sleep(1)
        except:
            pass

