import time
from selenium.webdriver.common.by import By
import var_app
import module_other_app
import homepage_app




class general:

    def report_back(self):
        var_app.driver.implicitly_wait(0.2)
        try:
            var_app.driver.find_element(By.XPATH, var_app.report_stop_back1).click()
            time.sleep(1.3)
        except:
            pass
        try:
            var_app.driver.find_element(By.XPATH, var_app.report_stop_back2).click()
            time.sleep(1.3)
        except:
            pass
        try:
            var_app.driver.find_element(By.XPATH, var_app.report_stop_back3).click()
            time.sleep(1.3)
        except:
            pass
        try:
            var_app.driver.find_element(By.XPATH, var_app.report_stop_back4).click()
            time.sleep(1.3)
        except:
            pass


    def select_vehicle(self, select_vehicle, select_vehicle_iconsearch, check_text, desire):
        var_app.driver.implicitly_wait(1)
        n = 210
        while (n < 1000):
            n += 150
            try:
                var_app.driver.find_element(By.XPATH, select_vehicle).click()
                time.sleep(2)
                var_app.driver.tap([(200, n)])
                time.sleep(2)
                var_app.driver.find_element(By.XPATH, var_app.report_7day).click()
                time.sleep(2)
                var_app.driver.find_element(By.XPATH, select_vehicle_iconsearch).click()
                time.sleep(2)

                check_select_vehicle = var_app.driver.find_element(By.XPATH, check_text).text
                print(check_select_vehicle)
                if check_select_vehicle == desire:
                    print("đã click vào tọa độ 200, {} Phương tiện {}.".format(n, check_select_vehicle))
                    break
                else:
                    print("đã click vào tọa độ 200, {} Phương tiện {}.".format(n, check_select_vehicle))
            except:
                print("đã click vào tọa độ 200, {} Không có dữ liệu.".format(n))
                pass



    def select_vehicle1(self, select_vehicle, select_vehicle_iconsearch, check_text, desire, vehicle):
        var_app.driver.implicitly_wait(1)
        n = 210
        while (n < 1000):
            n += 150
            try:
                var_app.driver.find_element(By.XPATH, select_vehicle).click()
                time.sleep(2)
                var_app.driver.find_element(By.XPATH, var_app.select_vehicle_input).clear()
                var_app.driver.find_element(By.XPATH, var_app.select_vehicle_input).send_keys(vehicle)
                time.sleep(2)
                var_app.driver.tap([(200, n)])
                time.sleep(2)
                var_app.driver.find_element(By.XPATH, var_app.report_7day).click()
                time.sleep(2)
                var_app.driver.find_element(By.XPATH, select_vehicle_iconsearch).click()
                time.sleep(2)

                check_select_vehicle = var_app.driver.find_element(By.XPATH, check_text).text
                print(check_select_vehicle)
                if check_select_vehicle == desire:
                    print("đã click vào tọa độ 200, {} Phương tiện {}.".format(n, check_select_vehicle))
                    break
                else:
                    print("đã click vào tọa độ 200, {} Phương tiện {}.".format(n, check_select_vehicle))
            except:
                print("đã click vào tọa độ 200, {} Không có dữ liệu.".format(n))
                pass




    def search_day(self, code, eventname, result, path_day, path_module, path_check, path_image):
        var_app.driver.implicitly_wait(3)
        var_app.driver.find_element(By.XPATH, path_day).click()
        time.sleep(2.5)
        module_other_app.write_result_displayed_try(code, eventname, result, path_module,
                                                path_check, path_image)


    def check_column(self, code, startX, startY, endX, endY, duration, path_check):
        var_app.driver.implicitly_wait(0.1)
        n = 0
        while (n < 5):
            n += 1
            try:
                var_app.driver.find_element(By.XPATH, "//*[@text='"+path_check+"']")
                print(path_check)
                break
            except:
                var_app.driver.swipe(startX, startY, endX, endY, duration)
            time.sleep(0.5)
        try:
            var_app.driver.find_element(By.XPATH, "//*[@text='"+path_check+"']")
            var_app.logging.info("True")
            var_app.logging.info(path_check)
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Pass")
        except:
            var_app.logging.info("False")
            var_app.logging.info(path_check)
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Fail")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 11, "Báo cáo bị mất trường: "+path_check+"")



        time.sleep(2.5)


    def check_column1(self, code, startX, startY, endX, endY, duration, path_check):
        var_app.driver.implicitly_wait(0.1)
        n = 0
        while (n < 5):
            n += 1
            try:
                print("//*[@text='"+path_check+"']")
                var_app.driver.find_element(By.XPATH, "//*[@text='"+path_check+"']")
                print(path_check)
                break
            except:
                var_app.driver.swipe(endX, startY, startX, endY, duration)
            time.sleep(0.5)
            print("//*[@text='"+path_check+"']")

        try:
            var_app.driver.find_element(By.XPATH, "//*[@text='"+path_check+"']")
            var_app.logging.info("True")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Pass")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 11, "")
        except:
            var_app.logging.info("False")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Fail")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 11, "Báo cáo bị mất trường: "+path_check+"")



        time.sleep(2.5)










class report:




    def report_stop_search(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_report_stop)
        except:
            general.report_back(self)
            homepage_app.move_module(self, "", "", "", var_app.report_stop, 725, 1100, 175, 1100, 500,  "", "", "", "_")



        general.select_vehicle(self, var_app.report_select_vehicle, var_app.report_icon_search,
                               var_app.check_report_search, "1")

        module_other_app.write_result_text_try_if_other(code, eventname, result, "Trang chủ - báo cáo dừng đỗ",
                                              var_app.check_report_search1, "", "_BaoCao_BaoCaoDungDo_ChonPhuongTien.png")


    def report_stop_search_type(self, code, eventname, result, button, path_check, path_module, path_image):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_report_search1)
        except:
            report.report_stop_search(self, "", "", "")


        var_app.driver.find_element(By.XPATH, button).click()
        time.sleep(1)
        var_app.driver.find_element(By.XPATH, var_app.report_icon_search).click()
        time.sleep(2.5)
        module_other_app.write_result_displayed_try(code, eventname, result, path_module,
                                                path_check, path_image)


    def report_stop_setting(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_report_stop)
        except:
            general.report_back(self)
            homepage_app.move_module(self, "", "", "", var_app.report_stop, 725, 1100, 175, 1100, 500,  "", "", "", "_")


        var_app.driver.find_element(By.XPATH, var_app.report_stop_setting).click()
        time.sleep(2.5)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - báo cáo dừng đỗ",
                                              var_app.check_report_stop_setting, "Cài đặt ẩn hiện thông tin", "_BaoCao_BaoCaoDungDo_CaiDat.png")

        try:
            var_app.driver.find_element(By.XPATH, var_app.report_stop_setting_iconx).click()
            time.sleep(1)
        except:
            pass


    def report_stop_filter(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_report_stop)
        except:
            general.report_back(self)
            homepage_app.move_module(self, "", "", "", var_app.report_stop, 725, 1100, 175, 1100, 500,  "", "", "", "_")


        var_app.driver.find_element(By.XPATH, var_app.report_stop_filter).click()
        time.sleep(2.5)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - báo cáo dừng đỗ",
                                              var_app.check_report_stop_filter, "BỘ LỌC TÌM KIẾM", "_BaoCao_BaoCaoDungDo_BoLoc.png")

        try:
            var_app.driver.find_element(By.XPATH, var_app.report_stop_setting_iconx).click()
            time.sleep(1)
        except:
            pass


    def report_stop_export_excel(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_report_stop)
        except:
            general.report_back(self)
            homepage_app.move_module(self, "", "", "", var_app.report_stop, 725, 1100, 175, 1100, 500,  "", "", "", "_")


        var_app.driver.find_element(By.XPATH, var_app.report_stop_export_excel).click()
        time.sleep(2.5)
        module_other_app.write_result_text_try_if_other(code, eventname, result, "Trang chủ - báo cáo dừng đỗ",
                                              var_app.check_report_stop_export_excel, "Lỗi xuất excel", "_BaoCao_BaoCaoDungDo_XuatExcel.png")


    def report_stop_detail(self, code, eventname, result, path_check, desire, path_image):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_report_stop_detail)
        except:
            report.report_stop_search(self, "", "", "")


        module_other_app.write_result_text_try_if_other(code, eventname, result, "Trang chủ - Báo cáo dừng đỗ",
                                              path_check, desire, path_image)


    def report_stop_check_column(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(2)

        general.report_back(self)
        report.report_stop_search(self, "", "", "")
        var_app.logging.info("--------------")
        var_app.logging.info("Trang chủ - Báo cáo dừng đỗ")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)

        general.check_column1(self, code, 825, 800, 650, 800, 150, "STT")
        general.check_column(self, code, 825, 800, 650, 800, 150, "Thời gian")
        general.check_column(self, code, 825, 800, 650, 800, 150, "Thời gian (phút)")
        general.check_column(self, code, 825, 800, 650, 800, 150, "Thời gian dừng đỗ (hh:mm:ss)")
        general.check_column(self, code, 825, 800, 650, 800, 150, "Nổ máy khi dừng (phút)")
        general.check_column(self, code, 825, 800, 650, 800, 150, "Bật ĐH khi dừng (phút)")
        general.check_column(self, code, 825, 800, 650, 800, 150, "Nhiệt độ")
        general.check_column(self, code, 825, 800, 650, 800, 150, "Tên lái xe")
        general.check_column(self, code, 825, 800, 650, 800, 150, "Mã nhân viên")
        general.check_column(self, code, 825, 800, 650, 800, 150, "Số điện thoại")
        general.check_column(self, code, 825, 800, 650, 800, 150, "Địa điểm")

        general.report_back(self)









    def detailed_activity_reports_search(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_detailed_activity_reports)
        except:
            general.report_back(self)
            homepage_app.move_module(self, "", "", "", var_app.detailed_activity_reports, 725, 1100, 175, 1100, 500,  "", "", "", "_")



        general.select_vehicle(self, var_app.report_select_vehicle, var_app.report_icon_search,
                               var_app.check_report_search, "1")

        module_other_app.write_result_text_try_if_other(code, eventname, result, "Trang chủ - Báo cáo chi tiết hoạt động",
                                              var_app.check_report_search1, "", "_TrangChu_BaoCaoChiTietHoatDong_ChonPhuongTien.png")


    def detailed_activity_reports_type(self, code, eventname, result, button, path_check, path_module, path_image):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_report_search1)
        except:
            report.detailed_activity_reports_search(self, "", "", "")


        var_app.driver.find_element(By.XPATH, button).click()
        time.sleep(1)
        var_app.driver.find_element(By.XPATH, var_app.report_icon_search).click()
        time.sleep(2.5)
        module_other_app.write_result_displayed_try(code, eventname, result, path_module,
                                                path_check, path_image)


    def detailed_activity_reports_setting(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_detailed_activity_reports)
        except:
            general.report_back(self)
            homepage_app.move_module(self, "", "", "", var_app.detailed_activity_reports, 725, 1100, 175, 1100, 500,  "", "", "", "_")


        var_app.driver.find_element(By.XPATH, var_app.report_stop_setting).click()
        time.sleep(2.5)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - báo cáo dừng đỗ",
                                              var_app.check_report_stop_setting, "Cài đặt ẩn hiện thông tin", "_TrangChu_BaoCaoChiTietHoatDong_CaiDat.png")

        try:
            var_app.driver.find_element(By.XPATH, var_app.report_stop_setting_iconx).click()
            time.sleep(1)
        except:
            pass


    def detailed_activity_reports_excel(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.report_detail2)
        except:
            report.detailed_activity_reports_search(self, "", "", "")


        var_app.driver.find_element(By.XPATH, var_app.detailed_activity_reports_excel).click()
        time.sleep(2.5)
        module_other_app.write_result_text_try_if_other(code, eventname, result, "Trang chủ - Báo cáo chi tiết hoạt động",
                                              var_app.check_report_stop_export_excel, "Lỗi xuất excel", "_TrangChu_BaoCaoChiTietHoatDong_XuatExcel.png")


    def detailed_activity_reports_detail(self, code, eventname, result, path_check, desire, path_image):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.report_detail2)
        except:
            report.detailed_activity_reports_search(self, "", "", "")


        module_other_app.write_result_text_try_if_other(code, eventname, result, "Trang chủ - Báo cáo chi tiết hoạt động",
                                              path_check, desire, path_image)


    def detailed_activity_reports_column(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(2)

        general.report_back(self)
        report.detailed_activity_reports_search(self, "", "", "")
        var_app.logging.info("--------------")
        var_app.logging.info("Trang chủ - Báo cáo chi tiết hoạt động")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)

        general.check_column1(self, code, 825, 800, 650, 800, 150, "STT")
        general.check_column(self, code, 825, 800, 650, 800, 150, "Ngày tháng")
        general.check_column(self, code, 825, 800, 650, 800, 150, "Giờ đi - Giờ đến")
        general.check_column(self, code, 825, 800, 650, 800, 150, "Số lít bắt đầu")
        general.check_column(self, code, 825, 800, 650, 800, 150, "Số lít kết thúc")
        general.check_column(self, code, 825, 800, 650, 800, 150, "Số lít tiêu hao")
        general.check_column(self, code, 825, 800, 650, 800, 150, "Thời gian hoạt động")
        general.check_column(self, code, 825, 800, 650, 800, 150, "Km (GPS)")
        general.check_column(self, code, 825, 800, 650, 800, 150, "Km cơ")
        general.check_column(self, code, 825, 800, 650, 800, 150, "Loại xe")
        general.check_column(self, code, 825, 800, 650, 800, 150, "Định mức nhiên liệu")
        general.check_column(self, code, 825, 800, 650, 800, 150, "Nhiên liệu tiêu thụ")
        general.check_column(self, code, 825, 800, 650, 800, 150, "Địa chỉ đi")
        general.check_column(self, code, 825, 800, 650, 800, 150, "Địa chỉ đến")
        general.check_column(self, code, 825, 800, 650, 800, 150, "Cuốc bù")


        general.report_back(self)











    def summary_report_of_activities_search(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_summary_report_of_activities)
        except:
            general.report_back(self)
            homepage_app.move_module(self, "", "", "", var_app.summary_report_of_activities, 725, 1100, 175, 1100, 500,  "", "", "", "_")



        general.select_vehicle(self, var_app.report_select_vehicle, var_app.report_icon_search,
                               var_app.check_report_search, "1")

        module_other_app.write_result_text_try_if_other(code, eventname, result, "Trang chủ - Báo cáo tổng hợp hoạt động",
                                              var_app.check_report_search1, "", "_TrangChu_BaoCaoTongHopHoatDong_ChonPhuongTien.png")


    def summary_report_of_activities_type(self, code, eventname, result, button, path_check, path_module, path_image):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_report_search1)
        except:
            report.summary_report_of_activities_search(self, "", "", "")


        var_app.driver.find_element(By.XPATH, button).click()
        time.sleep(1)
        var_app.driver.find_element(By.XPATH, var_app.report_icon_search).click()
        time.sleep(2.5)
        module_other_app.write_result_displayed_try(code, eventname, result, path_module,
                                                path_check, path_image)


    def summary_report_of_activities_setting(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_summary_report_of_activities)
        except:
            general.report_back(self)
            homepage_app.move_module(self, "", "", "", var_app.summary_report_of_activities, 725, 1100, 175, 1100, 500,  "", "", "", "_")


        var_app.driver.find_element(By.XPATH, var_app.report_setting).click()
        time.sleep(2.5)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Báo cáo tổng hợp hoạt động",
                                              var_app.check_report_setting, "Cài đặt ẩn hiện thông tin", "_TrangChu_BaoCaoTongHopHoatDong_CaiDat.png")

        try:
            var_app.driver.find_element(By.XPATH, var_app.report_setting_iconx).click()
            time.sleep(1)
        except:
            pass


    def summary_report_of_activities_filter(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_summary_report_of_activities)
        except:
            general.report_back(self)
            homepage_app.move_module(self, "", "", "", var_app.summary_report_of_activities, 725, 1100, 175, 1100, 500,  "", "", "", "_")


        var_app.driver.find_element(By.XPATH, var_app.report_filter).click()
        time.sleep(2.5)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Báo cáo tổng hợp hoạt động",
                                              var_app.check_report_filter, "BỘ LỌC TÌM KIẾM", "_TrangChu_BaoCaoTongHopHoatDong_BoLoc.png")

        try:
            var_app.driver.find_element(By.XPATH, var_app.report_setting_iconx).click()
            time.sleep(1)
        except:
            pass


    def summary_report_of_activities_excel(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.report_detail2)
        except:
            report.summary_report_of_activities_search(self, "", "", "")


        var_app.driver.find_element(By.XPATH, var_app.summary_report_of_activities_excel).click()
        time.sleep(2.5)
        module_other_app.write_result_text_try_if_other(code, eventname, result, "Trang chủ - Báo cáo tổng hợp hoạt động",
                                              var_app.check_export_excel, "Lỗi xuất excel", "_TrangChu_BaoCaoTongHopHoatDong_XuatExcel.png")


    def summary_report_of_activities_detail(self, code, eventname, result, path_check, desire, path_image):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.report_detail2)
        except:
            report.summary_report_of_activities_search(self, "", "", "")


        module_other_app.write_result_text_try_if_other(code, eventname, result, "Trang chủ - Báo cáo tổng hợp hoạt động",
                                              path_check, desire, path_image)


    def summary_report_of_activities_column(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(2)

        general.report_back(self)
        report.summary_report_of_activities_search(self, "", "", "")
        var_app.logging.info("--------------")
        var_app.logging.info("Trang chủ - Báo cáo tổng hợp hoạt động")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)

        general.check_column1(self, code, 825, 1200, 650, 1200, 150, "STT")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Ngày tháng")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Giờ đi - Giờ đến")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Thời gian lăn bánh")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Thời gian dừng đỗ")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Km (GPS)")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Km cơ")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Loại xe")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Số lần dừng đỗ")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Bật điều hòa (phút)")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Vận tốc cực đại")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Vận tốc trung bình")

        general.report_back(self)









    def report_entering_and_exiting_the_station_search(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_report_entering_and_exiting_the_station)
        except:
            general.report_back(self)
            homepage_app.move_module(self, "", "", "", var_app.report_entering_and_exiting_the_station, 725, 1100, 175, 1100, 500,  "", "", "", "_")



        general.select_vehicle(self, var_app.report_select_vehicle, var_app.report_icon_search,
                               var_app.check_report_search, "1")

        module_other_app.write_result_text_try_if_other(code, eventname, result, "Trang chủ - Báo cáo ra vào trạm",
                                              var_app.check_report_search1, "", "_TrangChu_BaoCaoRaVaotram_ChonPhuongTien.png")


    def report_entering_and_exiting_the_station_type(self, code, eventname, result, button, path_check, path_module, path_image):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_report_search1)
        except:
            report.report_entering_and_exiting_the_station_search(self, "", "", "")


        var_app.driver.find_element(By.XPATH, button).click()
        time.sleep(1)
        var_app.driver.find_element(By.XPATH, var_app.report_icon_search).click()
        time.sleep(2.5)
        module_other_app.write_result_displayed_try(code, eventname, result, path_module,
                                                path_check, path_image)


    def report_entering_and_exiting_the_station_setting(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_report_entering_and_exiting_the_station)
        except:
            general.report_back(self)
            homepage_app.move_module(self, "", "", "", var_app.report_entering_and_exiting_the_station, 725, 1100, 175, 1100, 500,  "", "", "", "_")


        var_app.driver.find_element(By.XPATH, var_app.report_setting).click()
        time.sleep(2.5)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Báo cáo ra vào trạm",
                                              var_app.check_report_setting, "Cài đặt ẩn hiện thông tin", "_TrangChu_BaoCaoRaVaotram_CaiDat.png")

        try:
            var_app.driver.find_element(By.XPATH, var_app.report_setting_iconx).click()
            time.sleep(1)
        except:
            pass


    def report_entering_and_exiting_the_station_filter(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_report_entering_and_exiting_the_station)
        except:
            general.report_back(self)
            homepage_app.move_module(self, "", "", "", var_app.report_entering_and_exiting_the_station, 725, 1100, 175, 1100, 500,  "", "", "", "_")


        var_app.driver.find_element(By.XPATH, var_app.report_filter).click()
        time.sleep(2.5)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Báo cáo tổng hợp hoạt động",
                                              var_app.check_report_filter, "BỘ LỌC TÌM KIẾM", "_TrangChu_BaoCaoRaVaotram_BoLoc.png")

        try:
            var_app.driver.find_element(By.XPATH, var_app.report_setting_iconx).click()
            time.sleep(1)
        except:
            pass


    def report_entering_and_exiting_the_station_excel(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_report_search)
        except:
            report.summary_report_of_activities_search(self, "", "", "")


        var_app.driver.find_element(By.XPATH, var_app.summary_report_of_activities_excel).click()
        time.sleep(2.5)
        module_other_app.write_result_text_try_if_other(code, eventname, result, "Trang chủ - Báo cáo ra vào trạm",
                                              var_app.check_export_excel, "Lỗi xuất excel", "_TrangChu_BaoCaoRaVaotram_XuatExcel.png")


    def report_entering_and_exiting_the_station_column(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(2)

        general.report_back(self)
        report.report_entering_and_exiting_the_station_search(self, "", "", "")
        var_app.logging.info("--------------")
        var_app.logging.info("Trang chủ - Báo cáo ra vào trạm")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)

        general.check_column1(self, code, 825, 1200, 650, 1200, 150, "STT")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Vào trạm")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Ra trạm")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Tên trạm")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Số phút trong trạm")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Lộ trình")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Link video")

        general.report_back(self)







    def report_speeding_search(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_report_speeding)
        except:
            general.report_back(self)
            homepage_app.move_module(self, "", "", "", var_app.report_speeding, 725, 1100,
                                     175, 1100, 500, "", "", "", "_")

        var_app.driver.find_element(By.XPATH, var_app.report_select_vehicle).click()
        time.sleep(2)
        var_app.driver.tap([(200, 360)])
        time.sleep(2)
        var_app.driver.find_element(By.XPATH, var_app.report_icon_search).click()
        time.sleep(2)
        module_other_app.write_result_text_try_if_other(code, eventname, result, "Trang chủ - Báo cáo quá tốc độ",
                                              var_app.check_report_search1, "", "_TrangChu_BaoCaoQuaTocDo_ChonPhuongTien.png")


    def report_speeding_type(self, code, eventname, result, button):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_report_speeding)
        except:
            report.report_speeding_search(self, "", "", "")


        var_app.driver.find_element(By.XPATH, button).click()
        time.sleep(1)
        var_app.driver.find_element(By.XPATH, var_app.report_icon_search).click()
        time.sleep(2.5)
        var_app.logging.info("--------------")
        var_app.logging.info("Trang chủ - Báo cáo quá tốc độ")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        var_app.logging.info("True")
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Pass")
        var_app.driver.implicitly_wait(1)
        try:
            checkdata = var_app.driver.find_element(By.XPATH, var_app.no_data).text
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 11, checkdata)
        except:
            pass


    def report_speeding_setting(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_report_speeding)
        except:
            general.report_back(self)
            homepage_app.move_module(self, "", "", "", var_app.report_speeding, 725, 1100, 175, 1100, 500,  "", "", "", "_")


        var_app.driver.find_element(By.XPATH, var_app.report_setting).click()
        time.sleep(2.5)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Báo cáo quá tốc độ",
                                              var_app.check_report_setting, "Cài đặt ẩn hiện thông tin", "_TrangChu_BaoCaoQuaTocDo_CaiDat.png")

        try:
            var_app.driver.find_element(By.XPATH, var_app.report_setting_iconx).click()
            time.sleep(1)
        except:
            pass


    def report_speeding_filter(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_report_speeding)
        except:
            general.report_back(self)
            homepage_app.move_module(self, "", "", "", var_app.report_speeding, 725, 1100, 175, 1100, 500,  "", "", "", "_")


        var_app.driver.find_element(By.XPATH, var_app.report_filter).click()
        time.sleep(2.5)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Báo cáo quá tốc độ",
                                              var_app.check_report_filter, "BỘ LỌC TÌM KIẾM", "_TrangChu_BaoCaoQuaTocDo_BoLoc.png")

        try:
            var_app.driver.find_element(By.XPATH, var_app.report_setting_iconx).click()
            time.sleep(1)
        except:
            pass


    def report_speeding_excel(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_report_speeding)
        except:
            report.report_speeding_search(self, "", "", "")


        time.sleep(2.5)
        var_app.logging.info("--------------")
        var_app.logging.info("Trang chủ - Báo cáo ra vào trạm")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        try:
            check_text = var_app.driver.find_element(By.XPATH, var_app.no_data).text
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 11, check_text)
            var_app.driver.find_element(By.XPATH, var_app.report_speeding_excel).click()
            check_text2 = var_app.driver.find_element(By.XPATH, var_app.check_report_speeding_excel).text
            var_app.logging.info(check_text)
            var_app.logging.info(check_text2)
            if check_text == check_text2:
                var_app.logging.info("True")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Pass")
            else:
                var_app.logging.info("False")
                var_app.driver.save_screenshot(var_app.imagepath + code + "_TrangChu_BaoCaoQuaTocDo_XuatExcel")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Fail")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 9, code + "_TrangChu_BaoCaoQuaTocDo_XuatExcel")
        except:
            pass








    def business_trip_report_search(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_business_trip_report)
        except:
            general.report_back(self)
            homepage_app.move_module(self, "", "", "", var_app.business_trip_report, 725, 1100, 175, 1100, 500,  "", "", "", "_")



        general.select_vehicle(self, var_app.report_select_vehicle, var_app.report_icon_search,
                               var_app.check_report_search, "1")

        module_other_app.write_result_text_try_if_other(code, eventname, result, "Trang chủ - Báo cáo chuyến kinh doanh",
                                              var_app.check_report_search1, "", "_TrangChu_BaoCaoChuyenKinhDoanh_ChonPhuongTien.png")


    def business_trip_report_type(self, code, eventname, result, button, path_check, path_module, path_image):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_report_search1)
        except:
            report.business_trip_report_search(self, "", "", "")


        var_app.driver.find_element(By.XPATH, button).click()
        time.sleep(1)
        var_app.driver.find_element(By.XPATH, var_app.report_icon_search).click()
        time.sleep(2.5)
        module_other_app.write_result_displayed_try(code, eventname, result, path_module,
                                                path_check, path_image)


    def business_trip_report_setting(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_business_trip_report)
        except:
            general.report_back(self)
            homepage_app.move_module(self, "", "", "", var_app.business_trip_report, 725, 1100, 175, 1100, 500,  "", "", "", "_")


        var_app.driver.find_element(By.XPATH, var_app.report_setting).click()
        time.sleep(2.5)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Báo cáo chuyến kinh doanh",
                                              var_app.check_report_setting, "Cài đặt ẩn hiện thông tin", "_TrangChu_BaoCaoChuyenKinhDoanh_CaiDat.png")

        try:
            var_app.driver.find_element(By.XPATH, var_app.report_setting_iconx).click()
            time.sleep(1)
        except:
            pass


    def business_trip_report_filter(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_business_trip_report)
        except:
            general.report_back(self)
            homepage_app.move_module(self, "", "", "", var_app.business_trip_report, 725, 1100, 175, 1100, 500,  "", "", "", "_")


        var_app.driver.find_element(By.XPATH, var_app.report_filter).click()
        time.sleep(2.5)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Báo cáo chuyến kinh doanh",
                                              var_app.check_report_filter, "BỘ LỌC TÌM KIẾM", "_TrangChu_BaoCaoChuyenKinhDoanh_BoLoc.png")

        try:
            var_app.driver.find_element(By.XPATH, var_app.report_setting_iconx).click()
            time.sleep(1)
        except:
            pass


    def business_trip_report_excel(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_report_search)
        except:
            report.business_trip_report_search(self, "", "", "")


        var_app.driver.find_element(By.XPATH, var_app.business_trip_report_excel).click()
        time.sleep(2.5)
        module_other_app.write_result_text_try_if_other(code, eventname, result, "Trang chủ - Báo cáo chuyến kinh doanh",
                                              var_app.check_export_excel, "Lỗi xuất excel", "_TrangChu_BaoCaoChuyenKinhDoanh_XuatExcel.png")


    def business_trip_report_detail(self, code, eventname, result, path_check, desire, path_image):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.report_detail2)
        except:
            report.business_trip_report_search(self, "", "", "")


        module_other_app.write_result_text_try_if_other(code, eventname, result, "Trang chủ - Báo cáo chuyến kinh doanh",
                                              path_check, desire, path_image)


    def business_trip_report_column(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(2)

        general.report_back(self)
        report.business_trip_report_search(self, "", "", "")
        var_app.logging.info("--------------")
        var_app.logging.info("Trang chủ - Báo cáo chuyến kinh doanh")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)

        general.check_column1(self, code, 825, 1200, 650, 1200, 150, "STT")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Điểm đi")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Điểm đến")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Giờ đi")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Giờ đến")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Số phút hoạt động")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Km GPS")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Km cơ")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "NL tiêu thụ")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Định mức NL trên km")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "NL tiêu thụ định mức")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Lộ trình")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Hình ảnh")

        general.report_back(self)










    def report_loss_of_signal_search(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_report_loss_of_signal)
        except:
            general.report_back(self)
            homepage_app.move_module(self, "", "", "", var_app.report_loss_of_signal, 725, 1100, 175, 1100, 500,  "", "", "", "_")



        general.select_vehicle(self, var_app.report_select_vehicle, var_app.report_icon_search,
                               var_app.check_report_search, "1")

        module_other_app.write_result_text_try_if_other(code, eventname, result, "Trang chủ - Báo cáo mất tín hiệu",
                                              var_app.check_report_search1, "", "_TrangChu_BaoCaoMatTinHieu_ChonPhuongTien.png")


    def report_loss_of_signal_type(self, code, eventname, result, button, path_check, path_module, path_image):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_report_search1)
        except:
            report.report_loss_of_signal_search(self, "", "", "")


        var_app.driver.find_element(By.XPATH, button).click()
        time.sleep(1)
        var_app.driver.find_element(By.XPATH, var_app.report_icon_search).click()
        time.sleep(2.5)
        module_other_app.write_result_displayed_try(code, eventname, result, path_module,
                                                path_check, path_image)


    def report_loss_of_signal_setting(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_report_loss_of_signal)
        except:
            general.report_back(self)
            homepage_app.move_module(self, "", "", "", var_app.report_loss_of_signal, 725, 1100, 175, 1100, 500,  "", "", "", "_")


        var_app.driver.find_element(By.XPATH, var_app.report_setting).click()
        time.sleep(2.5)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Báo cáo mất tín hiệu",
                                              var_app.check_report_setting, "Cài đặt ẩn hiện thông tin", "_TrangChu_BaoCaoMatTinHieu_CaiDat.png")

        try:
            var_app.driver.find_element(By.XPATH, var_app.report_setting_iconx).click()
            time.sleep(1)
        except:
            pass


    def report_loss_of_signal_filter(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_report_loss_of_signal)
        except:
            general.report_back(self)
            homepage_app.move_module(self, "", "", "", var_app.report_loss_of_signal, 725, 1100, 175, 1100, 500,  "", "", "", "_")


        var_app.driver.find_element(By.XPATH, var_app.report_filter).click()
        time.sleep(2.5)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Báo cáo mất tín hiệu",
                                              var_app.check_report_filter, "BỘ LỌC TÌM KIẾM", "_TrangChu_BaoCaoMatTinHieu_BoLoc.png")

        try:
            var_app.driver.find_element(By.XPATH, var_app.report_setting_iconx).click()
            time.sleep(1)
        except:
            pass


    def report_loss_of_signal_excel(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_report_search)
        except:
            report.report_loss_of_signal_search(self, "", "", "")


        var_app.driver.find_element(By.XPATH, var_app.report_loss_of_signal_excel).click()
        time.sleep(2.5)
        module_other_app.write_result_text_try_if_other(code, eventname, result, "Trang chủ - Báo cáo mất tín hiệu",
                                              var_app.check_export_excel, "Lỗi xuất excel", "_TrangChu_BaoCaoMatTinHieu_XuatExcel.png")


    def report_loss_of_signal_detail(self, code, eventname, result, path_check, desire, path_image):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.report_detail1)
        except:
            report.report_loss_of_signal_search(self, "", "", "")


        module_other_app.write_result_text_try_if_other(code, eventname, result, "Trang chủ - Báo cáo mất tín hiệu",
                                              path_check, desire, path_image)


    def report_loss_of_signal_column(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(2)

        general.report_back(self)
        report.report_loss_of_signal_search(self, "", "", "")
        var_app.logging.info("--------------")
        var_app.logging.info("Trang chủ - Báo cáo mất tín hiệu")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)

        general.check_column1(self, code, 825, 1200, 650, 1200, 150, "STT")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Thời gian bắt đầu")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Thời gian kết thúc")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Thời gian mất tín hiệu")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Địa điểm bắt đầu")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Địa điểm kết thúc")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Trạng thái")

        general.report_back(self)











    def fuel_dump_report_search(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_fuel_dump_report)
        except:
            general.report_back(self)
            homepage_app.move_module(self, "", "", "", var_app.fuel_dump_report, 725, 1100, 175, 1100, 500,  "", "", "", "")



        general.select_vehicle(self, var_app.report_select_vehicle, var_app.report_icon_search,
                               var_app.check_report_search, "1")

        module_other_app.write_result_text_try_if_other(code, eventname, result, "Trang chủ - Báo cáo đổ hút nhiên liệu",
                                              var_app.check_report_search1, "", "_TrangChu_BaoCaoDoHutNhienLieu_ChonPhuongTien.png")


    def fuel_dump_report_type(self, code, eventname, result, button, path_check, path_module, path_image):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_report_search1)
        except:
            report.fuel_dump_report_search(self, "", "", "")


        var_app.driver.find_element(By.XPATH, button).click()
        time.sleep(1)
        var_app.driver.find_element(By.XPATH, var_app.report_icon_search).click()
        time.sleep(2.5)

        if path_image == "_TrangChu_BaoCaoDoHutNhienLieu_HomNay.png":
            var_app.logging.info("--------------")
            var_app.logging.info("Trang chủ - Báo cáo đổ hút nhiên liệu")
            var_app.logging.info("Mã - " + code)
            var_app.logging.info("Tên sự kiện - " + eventname)
            var_app.logging.info("Kết quả - " + result)
            var_app.logging.info("True")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Pass")



        else:
            module_other_app.write_result_displayed_try(code, eventname, result, path_module,
                                                    path_check, path_image)


    def fuel_dump_report_setting(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_fuel_dump_report)
        except:
            general.report_back(self)
            homepage_app.move_module(self, "", "", "", var_app.fuel_dump_report, 725, 1100, 175, 1100, 500,  "", "", "", "_")


        var_app.driver.find_element(By.XPATH, var_app.report_setting).click()
        time.sleep(2.5)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Báo cáo đổ hút nhiên liệu",
                                              var_app.check_report_setting, "Cài đặt ẩn hiện thông tin", "_TrangChu_BaoCaoDoHutNhienLieu_CaiDat.png")

        try:
            var_app.driver.find_element(By.XPATH, var_app.report_setting_iconx).click()
            time.sleep(1)
        except:
            pass


    def fuel_dump_report_filter(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_fuel_dump_report)
        except:
            general.report_back(self)
            homepage_app.move_module(self, "", "", "", var_app.fuel_dump_report, 725, 1100, 175, 1100, 500,  "", "", "", "_")


        var_app.driver.find_element(By.XPATH, var_app.report_filter).click()
        time.sleep(2.5)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Báo cáo đổ hút nhiên liệu",
                                              var_app.check_report_filter, "BỘ LỌC TÌM KIẾM", "_TrangChu_BaoCaoDoHutNhienLieu_BoLoc.png")

        try:
            var_app.driver.find_element(By.XPATH, var_app.report_setting_iconx).click()
            time.sleep(1)
        except:
            pass


    def fuel_dump_report_excel(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_report_search)
        except:
            report.fuel_dump_report_search(self, "", "", "")


        var_app.driver.find_element(By.XPATH, var_app.fuel_dump_report_excel).click()
        time.sleep(2.5)
        module_other_app.write_result_text_try_if_other(code, eventname, result, "Trang chủ - Báo cáo đổ hút nhiên liệu",
                                              var_app.check_export_excel, "Lỗi xuất excel", "_TrangChu_BaoCaoDoHutNhienLieu_XuatExcel.png")


    def fuel_dump_report_detail(self, code, eventname, result, path_check, desire, path_image):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.report_detail1)
        except:
            report.fuel_dump_report_search(self, "", "", "")


        module_other_app.write_result_text_try_if_other(code, eventname, result, "Trang chủ - Báo cáo đổ hút nhiên liệu",
                                              path_check, desire, path_image)


    def fuel_dump_report_column(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(2)

        general.report_back(self)
        report.fuel_dump_report_search(self, "", "", "")
        var_app.logging.info("--------------")
        var_app.logging.info("Trang chủ - Báo cáo đổ hút nhiên liệu")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)

        general.check_column1(self, code, 825, 1200, 650, 1200, 150, "STT")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Thời gian")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Số lít")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Trạng thái")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Địa chỉ")

        general.report_back(self)










    def engine_report_search(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_engine_report)
        except:
            general.report_back(self)
            homepage_app.move_module(self, "", "", "", var_app.engine_report, 725, 1100, 175, 1100, 500,  "", "", "", "")



        general.select_vehicle1(self, var_app.report_select_vehicle, var_app.report_icon_search,
                               var_app.check_report_search, "1", "43C10954_C")

        module_other_app.write_result_text_try_if_other(code, eventname, result, "Trang chủ - Báo cáo động cơ",
                                              var_app.check_report_search1, "", "_TrangChu_BaoCaoDongCo_ChonPhuongTien.png")


    def engine_report_type(self, code, eventname, result, button, path_check, path_module, path_image):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_report_search1)
        except:
            report.engine_report_search(self, "", "", "")


        var_app.driver.find_element(By.XPATH, button).click()
        time.sleep(1)
        var_app.driver.find_element(By.XPATH, var_app.report_icon_search).click()
        time.sleep(2.5)

        if path_image == "_TrangChu_BaoCaoDongCo_HomNay.png":
            var_app.logging.info("--------------")
            var_app.logging.info("Trang chủ - Báo cáo động cơ")
            var_app.logging.info("Mã - " + code)
            var_app.logging.info("Tên sự kiện - " + eventname)
            var_app.logging.info("Kết quả - " + result)
            var_app.logging.info("True")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Pass")



        else:
            module_other_app.write_result_displayed_try(code, eventname, result, path_module,
                                                    path_check, path_image)


    def engine_report_setting(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_engine_report)
        except:
            general.report_back(self)
            homepage_app.move_module(self, "", "", "", var_app.engine_report, 725, 1100, 175, 1100, 500,  "", "", "", "_")


        var_app.driver.find_element(By.XPATH, var_app.report_setting).click()
        time.sleep(2.5)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Báo cáo động cơ",
                                              var_app.check_report_setting, "Cài đặt ẩn hiện thông tin", "_TrangChu_BaoCaoDongCo_CaiDat.png")

        try:
            var_app.driver.find_element(By.XPATH, var_app.report_setting_iconx).click()
            time.sleep(1)
        except:
            pass


    def engine_report_filter(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_engine_report)
        except:
            general.report_back(self)
            homepage_app.move_module(self, "", "", "", var_app.engine_report, 725, 1100, 175, 1100, 500,  "", "", "", "_")


        var_app.driver.find_element(By.XPATH, var_app.report_filter).click()
        time.sleep(2.5)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Báo cáo động cơ",
                                              var_app.check_report_filter, "BỘ LỌC TÌM KIẾM", "_TrangChu_BaoCaoDongCo_BoLoc.png")

        try:
            var_app.driver.find_element(By.XPATH, var_app.report_setting_iconx).click()
            time.sleep(1)
        except:
            pass


    def engine_report_excel(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_engine_report)
        except:
            report.engine_report_search(self, "", "", "")


        var_app.driver.find_element(By.XPATH, var_app.engine_report_excel).click()
        time.sleep(2.5)
        module_other_app.write_result_text_try_if_other(code, eventname, result, "Trang chủ - Báo cáo động cơ",
                                              var_app.check_export_excel, "Lỗi xuất excel", "_TrangChu_BaoCaoDongCo_XuatExcel.png")


    def engine_report_detail(self, code, eventname, result, path_check, desire, path_image):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.report_detail1)
        except:
            report.engine_report_search(self, "", "", "")


        module_other_app.write_result_text_try_if_other(code, eventname, result, "Trang chủ - Báo cáo động cơ",
                                              path_check, desire, path_image)


    def engine_report_column(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(2)

        general.report_back(self)
        report.engine_report_search(self, "", "", "")
        var_app.logging.info("--------------")
        var_app.logging.info("Trang chủ - Báo cáo động cơ")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)

        general.check_column1(self, code, 825, 1200, 650, 1200, 150, "STT")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Giờ bắt đầu")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Giờ đến")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Số phút ")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Nhiên liệu")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Địa chỉ đi")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Địa chỉ đến")

        general.report_back(self)










    def detail_vehicle_fuel_chart_search(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_detail_vehicle_fuel_chart)
        except:
            general.report_back(self)
            homepage_app.move_module(self, "", "", "", var_app.detail_vehicle_fuel_chart, 725, 1100,
                                     175, 1100, 500, "", "", "", "_")

        var_app.driver.find_element(By.XPATH, var_app.detail_vehicle_fuel_chart_select_vehicle).click()
        time.sleep(2)
        var_app.driver.tap([(200, 360)])
        time.sleep(2)
        var_app.driver.find_element(By.XPATH, var_app.detail_vehicle_fuel_chart_icon_search).click()
        time.sleep(3.5)
        module_other_app.write_result_displayed_try(code, eventname, result, "Trang chủ - Báo cáo quá tốc độ",
                                                var_app.check_detail_vehicle_fuel_chart_search, "_TrangChu_BieuDoNhienLieu_TimKiem.png")



        # var_app.logging.info("--------------")
        # var_app.logging.info("Trang chủ - Báo cáo quá tốc độ")
        # var_app.logging.info("Mã - " + code)
        # var_app.logging.info("Tên sự kiện - " + eventname)
        # var_app.logging.info("Kết quả - " + result)
        # var_app.logging.info("False")
        # var_app.driver.save_screenshot(var_app.imagepath + code + "_TrangChu_BieuDoNhienLieu_TimKiem.png")
        # module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Fail")
        # module_other_app.writeData(var_app.checklistpath, "Checklist", code, 9, code + "_TrangChu_BieuDoNhienLieu_TimKiem.png")


    def detail_vehicle_fuel_chart_filter(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_detail_vehicle_fuel_chart)
        except:
            general.report_back(self)
            homepage_app.move_module(self, "", "", "", var_app.detail_vehicle_fuel_chart, 725, 1100, 175, 1100, 500,  "", "", "", "_")


        var_app.driver.find_element(By.XPATH, var_app.detail_vehicle_fuel_chart_filter).click()
        time.sleep(2.5)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Báo cáo quá tốc độ",
                                              var_app.check_report_filter, "BỘ LỌC TÌM KIẾM", "_TrangChu_BieuDoNhienLieu_BoLoc.png")

        try:
            var_app.driver.find_element(By.XPATH, var_app.report_setting_iconx).click()
            time.sleep(1)
        except:
            pass
        general.report_back(self)











    def fuel_consumption_report_search(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_fuel_consumption_report)
        except:
            general.report_back(self)
            homepage_app.move_module(self, "", "", "", var_app.fuel_consumption_report, 725, 1100, 175, 1100, 500,  "", "", "", "_")



        general.select_vehicle(self, var_app.report_select_vehicle, var_app.report_icon_search,
                               var_app.check_report_search, "1")

        module_other_app.write_result_text_try_if_other(code, eventname, result, "Trang chủ - Báo cáo tiêu hao nhiên liệu",
                                              var_app.check_report_search1, "", "_TrangChu_BaoCaoTieuHaoNhienLieu_ChonPhuongTien.png")


    def fuel_consumption_report_type(self, code, eventname, result, button, path_check, path_module, path_image):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_report_search1)
        except:
            report.fuel_consumption_report_search(self, "", "", "")


        var_app.driver.find_element(By.XPATH, button).click()
        time.sleep(1)
        var_app.driver.find_element(By.XPATH, var_app.report_icon_search).click()
        time.sleep(2.5)
        module_other_app.write_result_displayed_try(code, eventname, result, path_module,
                                                path_check, path_image)


    def fuel_consumption_report_bapgs(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_fuel_consumption_report)
        except:
            general.report_back(self)
            homepage_app.move_module(self, "", "", "", var_app.fuel_consumption_report, 725, 1100, 175, 1100, 500,  "", "", "", "_")


        var_app.driver.find_element(By.XPATH, var_app.report_icon_gps).click()
        time.sleep(2.5)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Báo cáo tiêu hao nhiên liệu",
                                              var_app.check_report_icon_gps, "BA GPS", "_TrangChu_BaoCaoTieuHaoNhienLieu_BaGps.png")

        try:
            var_app.driver.find_element(By.XPATH, var_app.IGREE).click()
            time.sleep(1)
        except:
            pass


    def fuel_consumption_report_setting(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_fuel_consumption_report)
        except:
            general.report_back(self)
            homepage_app.move_module(self, "", "", "", var_app.fuel_consumption_report, 725, 1100, 175, 1100, 500,  "", "", "", "_")


        var_app.driver.find_element(By.XPATH, var_app.report_setting1).click()
        time.sleep(2.5)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Báo cáo tiêu hao nhiên liệu",
                                              var_app.check_report_setting, "Cài đặt ẩn hiện thông tin", "_TrangChu_BaoCaoTieuHaoNhienLieu_CaiDat.png")

        try:
            var_app.driver.find_element(By.XPATH, var_app.report_setting_iconx).click()
            time.sleep(1)
        except:
            pass


    def fuel_consumption_report_excel(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_report_search)
        except:
            report.fuel_consumption_report_search(self, "", "", "")


        var_app.driver.find_element(By.XPATH, var_app.fuel_consumption_report_excel).click()
        time.sleep(2.5)
        module_other_app.write_result_text_try_if_other(code, eventname, result, "Trang chủ - Báo cáo tiêu hao nhiên liệu",
                                              var_app.check_export_excel, "Lỗi xuất excel", "_TrangChu_BaoCaoTieuHaoNhienLieu_XuatExcel.png")


    def fuel_consumption_report_detail(self, code, eventname, result, path_check, desire, path_image):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.report_detail1)
        except:
            report.fuel_consumption_report_search(self, "", "", "")


        module_other_app.write_result_text_try_if_other(code, eventname, result, "Trang chủ - Báo cáo tiêu hao nhiên liệu",
                                              path_check, desire, path_image)


    def fuel_consumption_report_column(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(2)

        general.report_back(self)
        report.fuel_consumption_report_search(self, "", "", "")
        var_app.logging.info("--------------")
        var_app.logging.info("Trang chủ - Báo cáo tiêu hao nhiên liệu")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)

        general.check_column1(self, code, 825, 1200, 650, 1200, 150, "STT")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Ngày tháng")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Bắt đầu - Kết thúc")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Số lần đổ")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Số lần hút")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Số lít đầu ngày")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Số lít đổ")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Số lít hút")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Số lít tồn")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Số lít tiêu hao")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Tổng Km GPS")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Thời gian nổ máy (phút)")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Thời gian dừng đỗ nổ máy (phút)")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Định mức quy định")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Định mức thực tế")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Xem biểu đồ")

        general.report_back(self)









    def Comprehensive_fuel_consumption_report_search(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_Comprehensive_fuel_consumption_report)
        except:
            general.report_back(self)
            homepage_app.move_module(self, "", "", "", var_app.Comprehensive_fuel_consumption_report, 725, 1100, 175, 1100, 500,  "", "", "", "_")



        general.select_vehicle(self, var_app.report_select_vehicle, var_app.report_icon_search,
                               var_app.check_report_search, "1")

        module_other_app.write_result_text_try_if_other(code, eventname, result, "Trang chủ - Báo cáo tổng hợp tiêu hao nhiên liệu",
                                              var_app.check_report_search1, "", "_TrangChu_BaoCaoTongHopTieuHaoNhienLieu_ChonPhuongTien.png")


    def Comprehensive_fuel_consumption_report_type(self, code, eventname, result, button, path_check, path_module, path_image):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_report_search1)
        except:
            report.Comprehensive_fuel_consumption_report_search(self, "", "", "")


        var_app.driver.find_element(By.XPATH, button).click()
        time.sleep(1)
        var_app.driver.find_element(By.XPATH, var_app.report_icon_search).click()
        time.sleep(2.5)
        module_other_app.write_result_displayed_try(code, eventname, result, path_module,
                                                path_check, path_image)


    def Comprehensive_fuel_consumption_report_bapgs(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_Comprehensive_fuel_consumption_report)
        except:
            general.report_back(self)
            homepage_app.move_module(self, "", "", "", var_app.Comprehensive_fuel_consumption_report, 725, 1100, 175, 1100, 500,  "", "", "", "_")


        var_app.driver.find_element(By.XPATH, var_app.report_icon_gps).click()
        time.sleep(2.5)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Báo cáo tổng hợp tiêu hao nhiên liệu",
                                              var_app.check_report_icon_gps, "BA GPS", "_TrangChu_BaoCaoTongHopTieuHaoNhienLieu_BaGps.png")

        try:
            var_app.driver.find_element(By.XPATH, var_app.IGREE).click()
            time.sleep(1)
        except:
            pass


    def Comprehensive_fuel_consumption_report_setting(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_Comprehensive_fuel_consumption_report)
        except:
            general.report_back(self)
            homepage_app.move_module(self, "", "", "", var_app.Comprehensive_fuel_consumption_report, 725, 1100, 175, 1100, 500,  "", "", "", "_")


        var_app.driver.find_element(By.XPATH, var_app.report_setting1).click()
        time.sleep(2.5)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Báo cáo tồng hợp tiêu hao nhiên liệu",
                                              var_app.check_report_setting, "Cài đặt ẩn hiện thông tin", "_TrangChu_BaoCaoTongHopTieuHaoNhienLieu_CaiDat.png")

        try:
            var_app.driver.find_element(By.XPATH, var_app.report_setting_iconx).click()
            time.sleep(1)
        except:
            pass


    def Comprehensive_fuel_consumption_report_excel(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_report_search)
        except:
            report.Comprehensive_fuel_consumption_report_search(self, "", "", "")


        var_app.driver.find_element(By.XPATH, var_app.Comprehensive_fuel_consumption_report_excel).click()
        time.sleep(2.5)
        module_other_app.write_result_text_try_if_other(code, eventname, result, "Trang chủ - Báo cáo tồng hợp tiêu hao nhiên liệu",
                                              var_app.check_export_excel, "Lỗi xuất excel", "_TrangChu_BaoCaoTongHopTieuHaoNhienLieu_XuatExcel.png")


    def Comprehensive_fuel_consumption_report_detail(self, code, eventname, result, path_check, desire, path_image):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.report_detail1)
        except:
            report.Comprehensive_fuel_consumption_report_search(self, "", "", "")


        module_other_app.write_result_text_try_if_other(code, eventname, result, "Trang chủ - Báo cáo tồng hợp tiêu hao nhiên liệu",
                                              path_check, desire, path_image)


    def Comprehensive_fuel_consumption_report_column(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(2)

        general.report_back(self)
        report.Comprehensive_fuel_consumption_report_search(self, "", "", "")
        var_app.logging.info("--------------")
        var_app.logging.info("Trang chủ - Báo cáo tồng hợp tiêu hao nhiên liệu")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)

        general.check_column1(self, code, 825, 1200, 650, 1200, 150, "STT")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Từ ngày - Đến ngày")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Số lần đổ")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Số lần hút")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Số lít đầu ngày")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Số lít đổ")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Số lít hút")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Số lít tồn")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Số lít tiêu hao")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Tổng Km GPS")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Thời gian nổ máy (phút)")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Thời gian dừng đỗ nổ máy (phút)")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Định mức quy định")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Định mức thực tế")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Chi tiết")

        general.report_back(self)











    def vehicle_speed_search(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_vehicle_speed)
        except:
            general.report_back(self)
            homepage_app.move_module(self, "", "", "", var_app.vehicle_speed, 725, 1100, 175, 1100, 500,  "", "", "", "")


        var_app.driver.find_element(By.XPATH, var_app.report_select_vehicle).click()
        time.sleep(2)
        var_app.driver.tap([(200, 360)])
        time.sleep(2)
        var_app.driver.find_element(By.XPATH, var_app.report_today).click()
        time.sleep(2)
        var_app.driver.find_element(By.XPATH, var_app.report_icon_search).click()
        time.sleep(3.5)
        module_other_app.write_result_text_try_if_other(code, eventname, result, "Trang chủ - Tốc độ của xe",
                                              var_app.check_report_search1, "", "_TrangChu_TocDoCuaXe_ChonPhuongTien.png")


    def vehicle_speed_type(self, code, eventname, result, button, path_check, path_module, path_image):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_report_search1)
        except:
            report.vehicle_speed_search(self, "", "", "")


        var_app.driver.find_element(By.XPATH, button).click()
        time.sleep(1)
        var_app.driver.find_element(By.XPATH, var_app.report_icon_search).click()
        time.sleep(2.5)
        try:
            checkdata = var_app.driver.find_element(By.XPATH, var_app.check_vehicle_speed_type).text
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 11, checkdata)
        except:
            pass
        module_other_app.write_result_displayed_try(code, eventname, result, path_module,
                                                path_check, path_image)


    def vehicle_speed_setting(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_vehicle_speed)
        except:
            general.report_back(self)
            homepage_app.move_module(self, "", "", "", var_app.vehicle_speed, 725, 1100, 175, 1100, 500,  "", "", "", "_")

        var_app.driver.find_element(By.XPATH, var_app.report_setting).click()
        time.sleep(2.5)

        # var_app.logging.info("--------------")
        # var_app.logging.info("Trang chủ - Tốc độ của xe")
        # var_app.logging.info("Mã - " + code)
        # var_app.logging.info("Tên sự kiện - " + eventname)
        # var_app.logging.info("Kết quả - " + result)
        # var_app.logging.info("False")
        # var_app.driver.save_screenshot(var_app.imagepath + code + "_TrangChu_TocDoCuaXe_CaiDat.png")
        # module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Fail")
        # module_other_app.writeData(var_app.checklistpath, "Checklist", code, 9, code + "_TrangChu_TocDoCuaXe_CaiDat.png")


        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Tốc độ của xe",
                                              var_app.check_report_setting, "Cài đặt ẩn hiện thông tin", "_TrangChu_TocDoCuaXe_CaiDat.png")

        try:
            var_app.driver.find_element(By.XPATH, var_app.report_setting_iconx).click()
            time.sleep(1)
        except:
            pass


    def vehicle_speed_filter(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_vehicle_speed)
        except:
            general.report_back(self)
            homepage_app.move_module(self, "", "", "", var_app.vehicle_speed, 725, 1100, 175, 1100, 500,  "", "", "", "_")


        var_app.driver.find_element(By.XPATH, var_app.report_filter).click()
        time.sleep(2.5)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Tốc độ của xe",
                                              var_app.check_report_filter, "BỘ LỌC TÌM KIẾM", "_TrangChu_TocDoCuaXe_BoLoc.png")

        try:
            var_app.driver.find_element(By.XPATH, var_app.report_setting_iconx).click()
            time.sleep(1)
        except:
            pass


    def vehicle_speed_excel(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_report_search)
        except:
            report.vehicle_speed_search(self, "", "", "")


        var_app.driver.find_element(By.XPATH, var_app.vehicle_speed_excel).click()
        time.sleep(2.5)
        module_other_app.write_result_text_try_if_other(code, eventname, result, "Trang chủ - Tốc độ của xe",
                                              var_app.check_export_excel, "Lỗi xuất excel", "_TrangChu_TocDoCuaXe_XuatExcel.png")


    def vehicle_speed_column(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        var_app.driver.implicitly_wait(2)

        general.report_back(self)
        report.vehicle_speed_search(self, "", "", "")
        var_app.logging.info("--------------")
        var_app.logging.info("Trang chủ - Tốc độ của xe")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        general.check_column1(self, code, 825, 1200, 650, 1200, 150, "STT")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Thời điểm")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Các tốc độ (km/h)")

        general.report_back(self)




