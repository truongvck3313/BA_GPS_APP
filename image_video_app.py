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

    def image_monitoring_search(self, code, eventname, result):
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
            var_app.driver.find_element(By.XPATH, var_app.check_image_monitoring)
        except:
            homepage_app.move_module(self, "", "", "", var_app.image_monitoring, 740, 650, 160, 650, 600, "", "", "", "")


        var_app.driver.find_element(By.XPATH, var_app.image_monitoring_search).click()
        time.sleep(2)
        name1 = var_app.driver.find_element(By.XPATH, var_app.image_monitoring_search_name2).text

        var_app.driver.find_element(By.XPATH, var_app.image_monitoring_search_input).send_keys(name1)
        time.sleep(2)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Hình ảnh, video - Giám sát hình ảnh",
                                              var_app.check_image_monitoring_search, name1, "_TrangChu_HinhAnhVideo_GiamSatHinhAnh_TimKiem.png")

        var_app.driver.find_element(By.XPATH, var_app.image_monitoring_search_input).clear()
        time.sleep(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.image_monitoring_search_iconx).click()
            time.sleep(1.5)
        except:
            pass

    def image_monitoring_select_group(self, code, eventname, result):
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
            homepage_app.move_module(self, "", "", "", var_app.image_monitoring, 740, 650, 160, 650, 600, "", "", "", "")


        var_app.driver.find_element(By.XPATH, var_app.image_monitoring_select_group).click()
        time.sleep(2)
        n = 0
        while (n < 14):
            n += 1
            n = str(n)
            pathphuongtien = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[" + n + "]/android.view.ViewGroup/android.widget.TextView"
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
                    try:
                        var_app.driver.find_element(By.XPATH, var_app.check_image_monitoring_select_group)
                        module_other_app.write_result_displayed_try(code, eventname, result, "Trang chủ - Hình ảnh, video - Giám sát hình ảnh",
                                                                    var_app.check_image_monitoring_select_group, "_TrangChu_HinhAnhVideo_GiamSatHinhAnh_ChonNhom.png")
                    except:
                        check_select_group = var_app.driver.find_element(By.XPATH,var_app.check_image_monitoring_select_group1)
                        module_other_app.write_result_displayed_try(code, eventname, result, "Trang chủ - Hình ảnh, video - Giám sát hình ảnh",
                                                                    var_app.check_image_monitoring_select_group1, "_TrangChu_HinhAnhVideo_GiamSatHinhAnh_ChonNhom.png")

                    var_app.driver.find_element(By.XPATH, var_app.image_monitoring_select_group).click()
                    time.sleep(2)
                    var_app.driver.find_element(By.XPATH, pathphuongtien).click()
                    time.sleep(1)
                    var_app.driver.find_element(By.XPATH, var_app.select_group_choose).click()
                    time.sleep(2)
                    break
            except:
                pass
            n = int(n)

    def image_monitoring_arrange_image(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(7)
        except:
            pass
        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_image_monitoring)
        except:
            homepage_app.move_module(self, "", "", "", var_app.image_monitoring, 740, 650, 160, 650, 600, "", "", "", "")
        try:
            name1 = var_app.driver.find_element(By.XPATH, var_app.image_monitoring_search_name1).text
        except:
            name1 = var_app.driver.find_element(By.XPATH, var_app.image_monitoring_search_name1a).text

        try:
            var_app.driver.find_element(By.XPATH, var_app.image_monitoring_arrange_image).click()
        except:
            var_app.driver.find_element(By.XPATH, var_app.image_monitoring_arrange_image1).click()

        time.sleep(2)
        try:
            var_app.driver.find_element(By.XPATH, var_app.image_monitoring_search_name1)
            module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Hình ảnh, video - Giám sát hình ảnh",
                                                  var_app.image_monitoring_search_name1, name1, "_TrangChu_HinhAnhVideo_GiamSatHinhAnh_SapXepAnh.png")
        except:
            var_app.driver.find_element(By.XPATH, var_app.image_monitoring_search_name1a)
            module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Hình ảnh, video - Giám sát hình ảnh",
                                                  var_app.image_monitoring_search_name1a, name1, "_TrangChu_HinhAnhVideo_GiamSatHinhAnh_SapXepAnh.png")



        try:
            var_app.driver.find_element(By.XPATH, var_app.image_monitoring_arrange_image).click()
        except:
            var_app.driver.find_element(By.XPATH, var_app.image_monitoring_arrange_image1).click()
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
            homepage_app.move_module(self, "", "", "", var_app.image_monitoring, 740, 650, 160, 650, 600, "", "", "", "")

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
            time.sleep(7)
        except:
            pass
        var_app.driver.implicitly_wait(5)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_image_monitoring)
        except:
            homepage_app.move_module(self, "", "", "", var_app.image_monitoring, 740, 650, 160, 650, 600, "", "", "", "")

        try:
            var_app.driver.find_element(By.XPATH, var_app.image_monitoring_favorite).click()
        except:
            var_app.driver.find_element(By.XPATH, var_app.image_monitoring_favorite1).click()
        time.sleep(1.5)
        var_app.logging.info("--------------")
        var_app.logging.info("Trang chủ - Hình ảnh, video - Giám sát hình ảnh")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("True")
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Pass")
        try:
            var_app.driver.find_element(By.XPATH, var_app.image_monitoring_favorite).click()
        except:
            var_app.driver.find_element(By.XPATH, var_app.image_monitoring_favorite1).click()
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
            homepage_app.move_module(self, "", "", "", var_app.image_monitoring, 740, 650, 160, 650, 600, "", "", "", "")
        try:
            var_app.driver.find_element(By.XPATH, var_app.image_monitoring_see_all_image).click()
        except:
            var_app.driver.find_element(By.XPATH, var_app.image_monitoring_see_all_imag2).click()
        time.sleep(2)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Hình ảnh, video - Giám sát hình ảnh_Camera",
                                              var_app.check_image_monitoring_see_all_image, "Camera", "_TrangChu_HinhAnhVideo_GiamSatHinhAnh_XemTatCaAnh.png")

    def image_monitoring_see_all_image_search(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(7)
        except:
            pass
        var_app.driver.implicitly_wait(5)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_image_monitoring_see_all_image)
        except:
            homepage_app.move_module(self, "", "", "", var_app.image_monitoring, 740, 650, 160, 650, 600, "", "", "", "")
            image_video.image_monitoring_see_all_image(self, "", "", "")

        var_app.driver.find_element(By.XPATH, var_app.image_monitoring_see_all_image_search_icondown).click()
        time.sleep(2)
        var_app.driver.find_element(By.XPATH, var_app.image_monitoring_see_all_image_search_vehicle1).click()
        time.sleep(2)
        module_other_app.write_result_displayed_try(code, eventname, result, "Trang chủ - Hình ảnh, video - Giám sát hình ảnh - Camera - Camera",
                                                var_app.check_image_monitoring_see_all_image_search, "_TrangChu_HinhAnhVideo_GiamSatHinhAnh_XemTatCaAnh_TimKiem.png")

    def image_monitoring_see_all_image_announce(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(7)
        except:
            pass
        var_app.driver.implicitly_wait(5)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_image_monitoring_see_all_image)
        except:
            homepage_app.move_module(self, "", "", "", var_app.image_monitoring, 740, 650, 160, 650, 600, "", "", "", "")
            image_video.image_monitoring_see_all_image(self, "", "", "")

        var_app.driver.find_element(By.XPATH, var_app.image_monitoring_see_all_image_announce).click()
        time.sleep(2)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Hình ảnh, video - Giám sát hình ảnh - Camera - Camera",
                                              var_app.check_image_monitoring_see_all_image_announce, "Các xe sử dụng gói cước không tích hợp tính năng xem video sẽ không được hiển thị trên tính năng này", "_TrangChu_HinhAnhVideo_GiamSatHinhAnh_IconThongBao.png")

        try:
            var_app.driver.find_element(By.XPATH, var_app.image_monitoring_see_all_image_announce_skip).click()
            time.sleep(1)
        except:
            pass

        try:
            var_app.driver.find_element(By.XPATH, var_app.image_monitoring_see_all_image_announce_iconx).click()
            time.sleep(1)
        except:
            pass

        try:
            var_app.driver.find_element(By.XPATH, var_app.image_monitoring_iconx).click()
            time.sleep(1)
        except:
            pass





    def camera_monitoring_add_camera(self, code, eventname, result):
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
            var_app.driver.find_element(By.XPATH, var_app.check_camera_monitoring)
        except:
            homepage_app.move_module(self, "", "", "", var_app.camera_monitoring, 740, 650, 160, 650, 600, "", "", "", "")


        var_app.driver.find_element(By.XPATH, var_app.camera_monitoring_add_camera).click()
        time.sleep(2)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Hình ảnh, video - Giám sát camera",
                                              var_app.check_camera_monitoring_add_camera, "Thêm camera", "_TrangChu_HinhAnhVideo_GiamSatCamera_IconThemcamera.png")

    def camera_monitoring_add_camera_search(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(7)
        except:
            pass
        var_app.driver.implicitly_wait(5)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_camera_monitoring)
        except:
            homepage_app.move_module(self, "", "", "", var_app.camera_monitoring, 740, 650, 160, 650, 600, "", "", "", "")
            image_video.camera_monitoring_add_camera(self, "", "", "")

        name2 = var_app.driver.find_element(By.XPATH, var_app.camera_monitoring_add_camera_search_name2).text
        var_app.driver.find_element(By.XPATH, var_app.camera_monitoring_add_camera_search).send_keys(name2)
        time.sleep(1)
        var_app.driver.find_element(By.XPATH, var_app.camera_monitoring_add_camera_search1).click()
        time.sleep(1.7)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Hình ảnh, video - Giám sát camera - Thêm camera",
                                              var_app.check_camera_monitoring_add_camera_search, name2, "_TrangChu_HinhAnhVideo_GiamSatCamera_IconThemcamera_TimKiem.png")
        time.sleep(0.5)
        var_app.driver.find_element(By.XPATH, var_app.camera_monitoring_add_camera_search).clear()
        time.sleep(1.5)

    def camera_monitoring_add_camera_choose_channel(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(7)
        except:
            pass
        var_app.driver.implicitly_wait(5)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_camera_monitoring)
        except:
            homepage_app.move_module(self, "", "", "", var_app.camera_monitoring, 740, 650, 160, 650, 600, "", "", "", "")
            image_video.camera_monitoring_add_camera(self, "", "", "")
        try:
            var_app.driver.find_element(By.XPATH, var_app.vehicle1_channel1).click()
        except:
            pass
        try:
            var_app.driver.find_element(By.XPATH, var_app.vehicle1_channel2).click()
        except:
            pass
        try:
            var_app.driver.find_element(By.XPATH, var_app.vehicle2_channel1).click()
        except:
            pass
        try:
            var_app.driver.find_element(By.XPATH, var_app.vehicle2_channel2).click()
        except:
            pass
        try:
            var_app.driver.find_element(By.XPATH, var_app.vehicle3_channel1).click()
        except:
            pass
        try:
            var_app.driver.find_element(By.XPATH, var_app.vehicle3_channel2).click()
        except:
            pass
        try:
            var_app.driver.find_element(By.XPATH, var_app.vehicle4_channel1).click()
        except:
            pass
        try:
            var_app.driver.find_element(By.XPATH, var_app.vehicle4_channel2).click()
        except:
            pass
        time.sleep(1)
        var_app.driver.find_element(By.XPATH, var_app.igree).click()
        time.sleep(3)
        module_other_app.write_result_displayed_try(code, eventname, result, "Trang chủ - Hình ảnh, video - Giám sát camera - Thêm camera",
                                                var_app.check_camera_monitoring_add_camera_choose_channel, "_TrangChu_HinhAnhVideo_GiamSatCamera_IconThemcamera_ChonKenh12.png")

    def camera_monitoring_check_info(self, code, eventname, result, path_text, name_image):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(7)
        except:
            pass
        var_app.driver.implicitly_wait(5)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_camera_monitoring_add_camera_choose_channel)
        except:
            image_video.camera_monitoring_add_camera_choose_channel(self, "", "", "")

        print("check: " + path_text)
        module_other_app.write_result_text_try_if_other(code, eventname, result, "Trang chủ - Giám sát camera - Check thông tin xe",
                                              path_text, None, name_image)

    def camera_monitoring_get_icon(self):
        var_app.driver.implicitly_wait(0.2)
        n = 0
        m = 0
        while (n < 9):
            n += 1
            n = str(n)
            pathtenphuongtien = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.FrameLayout[" + n + "]/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.TextView"
            pathtenphuongtien3 = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.FrameLayout[" + n + "]/android.view.ViewGroup/android.view.ViewGroup/android.view.View"
            try:
                tenphuongtien = var_app.driver.find_element(By.XPATH, pathtenphuongtien).text
            except:
                m += 1
                m = str(m)
                pathtenphuongtien2 = "(//android.widget.FrameLayout[@content-desc='Busy Indicator with Cupertino type animation.'])[" + m + "]/android.view.View[2]"
                try:
                    var_app.driver.find_element(By.XPATH, pathtenphuongtien2)
                except:
                    print("đang dừng ở camera số " + n)
                    var_app.driver.find_element(By.XPATH, pathtenphuongtien3).click()
                    break
                m = int(m)
            n = int(n)

    def camera_monitoring_check_icon(self, code, eventname, result, button, desire, path_image):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(7)
        except:
            pass
        # var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_camera_monitoring_add_camera_choose_channel)
        except:
            image_video.camera_monitoring_add_camera_choose_channel(self, "", "", "")
            image_video.camera_monitoring_get_icon(self)
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
            time.sleep(7)
        except:
            pass
        var_app.driver.implicitly_wait(5)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_camera_monitoring_add_camera_choose_channel)
        except:
            image_video.camera_monitoring_add_camera_choose_channel(self, "", "", "")
            image_video.camera_monitoring_get_icon(self)
        try:
            var_app.driver.find_element(By.XPATH, var_app.camera_monitoring_check_icon_close).click()
            time.sleep(1.5)
        except:
            pass

        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Giám sát camera - Check icon chức năng camera",
                                              var_app.check_camera_monitoring_check_icon_close, "Bạn có thực sự muốn tắt kênh này không?", "_TrangChu_GiamSatCamera_IconDongCamera.png")

        try:
            var_app.driver.find_element(By.XPATH, var_app.camera_monitoring_check_icon_igree).click()
            time.sleep(1.5)
        except:
            pass

    def camera_monitoring_on_the_camera(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(7)
        except:
            pass
        var_app.driver.implicitly_wait(5)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_camera_monitoring_add_camera_choose_channel)
        except:
            image_video.camera_monitoring_add_camera(self, "", "", "")

        try:
            var_app.driver.find_element(By.XPATH, var_app.camera_monitoring_add_camera).click()
            time.sleep(2)
        except:
            pass
        checkcamera = var_app.driver.find_element(By.XPATH, var_app.camera_monitoring_check_vehicle_on_the_camera)
        if checkcamera.text == "TẮT":
            checkcamera.click()
            time.sleep(1)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Giám sát camera - Thêm camera",
                                              var_app.camera_monitoring_check_vehicle_on_the_camera, "BẬT", "_TrangChu_GiamSatCamera_ThemCamera_BatTat.png")

        if checkcamera.text == "BẬT":
            checkcamera.click()
            time.sleep(1)

    def camera_monitoring_reset(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(7)
        except:
            pass
        var_app.driver.implicitly_wait(5)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_camera_monitoring_add_camera)
        except:
            image_video.camera_monitoring_add_camera(self, "", "", "")

        var_app.driver.find_element(By.XPATH, var_app.camera_monitoring_add_camera_reset).click()
        time.sleep(2)
        var_app.driver.find_element(By.XPATH, var_app.igree).click()
        time.sleep(3)
        module_other_app.write_result_not_displayed_try(code, eventname, result, "Trang chủ - Giám sát camera - Thêm camera",
                                                var_app.check_camera_monitoring_reset, "_TrangChu_GiamSatCamera_ThemCamera_DatLai.png")

        try:
            var_app.driver.find_element(By.XPATH, var_app.camera_monitoring_iconx).click()
            time.sleep(1.5)
        except:
            pass




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


        name2 = var_app.driver.find_element(By.XPATH, var_app.see_again_video_search_name2).text
        var_app.driver.find_element(By.XPATH, var_app.check_see_again_search_vehicle).click()
        time.sleep(2)
        var_app.driver.find_element(By.XPATH, var_app.check_see_again_search_vehicle_input).send_keys(name2)
        time.sleep(2)
        var_app.driver.find_element(By.XPATH, var_app.check_see_again_search_vehicle_radio1).click()
        var_app.driver.find_element(By.XPATH, var_app.check_see_again_search_vehicle_select).click()
        time.sleep(1.5)
        var_app.driver.find_element(By.XPATH, var_app.check_see_again_search_vehicle_iconsearch).click()
        time.sleep(2)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Xem lại video - Tổng quan",
                                              var_app.see_again_video_search_name1, name2, "_TrangChu_XemLaiVideo_TimKiem.png")


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

        var_app.driver.implicitly_wait(5)
        var_app.logging.info("--------------")
        var_app.logging.info("Trang chủ - Xem lại video - Tổng quan - Xem thiết bị")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.driver.find_element(By.XPATH, path_icon).click()
        time.sleep(1)
        if desire == "True":
            var_app.logging.info("True")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Pass")
        else:
            var_app.logging.info("False")
            var_app.driver.save_screenshot(var_app.imagepath + code + path_image)
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Fail")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 9, code + path_image)

        var_app.driver.find_element(By.XPATH, path_icon).click()
        time.sleep(1)






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

