import time
from selenium.webdriver.common.by import By
import var_app
import module_other_app
import homepage_app
import login_app
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC










class general:

    def report_back(self):
        var_app.driver.implicitly_wait(0.2)
        try:
            var_app.driver.find_element(By.XPATH, var_app.report_stop_back0).click()
            time.sleep(1.3)
        except:
            pass
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
        try:
            var_app.driver.find_element(By.XPATH, var_app.report_stop_back5).click()
            time.sleep(1.3)
        except:
            pass
        try:
            var_app.driver.find_element(By.XPATH, var_app.report_stop_back6).click()
            time.sleep(1.3)
        except:
            pass
        try:
            var_app.driver.find_element(By.XPATH, var_app.report_stop_back7).click()
            time.sleep(1.3)
        except:
            pass
        try:
            var_app.driver.find_element(By.XPATH, var_app.report_stop_back8).click()
            time.sleep(1.3)
        except:
            pass
        try:
            var_app.driver.find_element(By.XPATH, var_app.report_stop_back9).click()
            time.sleep(1.3)
        except:
            pass
        try:
            var_app.driver.find_element(By.XPATH, var_app.report_stop_back10).click()
            time.sleep(1.3)
        except:
            pass
        try:
            var_app.driver.find_element(By.XPATH, var_app.report_stop_back11).click()
            time.sleep(1.3)
        except:
            pass
        try:
            var_app.driver.find_element(By.XPATH, var_app.report_stop_back12).click()
            time.sleep(1.3)
        except:
            pass
        try:
            var_app.driver.find_element(By.XPATH, var_app.report_stop_back13).click()
            time.sleep(1.3)
        except:
            pass
        try:
            var_app.driver.find_element(By.XPATH, var_app.report_stop_back14).click()
            time.sleep(1.3)
        except:
            pass
        try:
            var_app.driver.find_element(By.XPATH, var_app.report_stop_back15).click()
            time.sleep(1.3)
        except:
            pass
        try:
            var_app.driver.find_element(By.XPATH, var_app.report_stop_back16).click()
            time.sleep(1.3)
        except:
            pass





    def select_vehicle_violet(self, select_vehicle, select_vehicle_iconsearch, check_text):
        var_app.driver.implicitly_wait(0.5)
        n = 463
        while (n < 1000):
            n += 80
            try:
                var_app.driver.find_element(By.XPATH, select_vehicle).click()
                time.sleep(2)
                module_other_app.tap_scaled(var_app.driver, [(100, n)])
                time.sleep(2)
                var_app.driver.find_element(By.XPATH, var_app.report_7day).click()
                time.sleep(2)
                var_app.driver.find_element(By.XPATH, select_vehicle_iconsearch).click()

                wait = WebDriverWait(var_app.driver, 5)
                element = wait.until(EC.element_to_be_clickable((By.XPATH, check_text)))
                time.sleep(1)

                check_select_vehicle = var_app.driver.find_element(By.XPATH, check_text).text
                print("đã click vào tọa độ 100, {}, {}.".format(n, check_select_vehicle))
                break
            except:
                print("đã click vào tọa độ 100, {} Không có dữ liệu.".format(n))
                pass

    def select_vehicle(self, select_vehicle, select_vehicle_iconsearch, check_text, desire):
        var_app.driver.implicitly_wait(0.5)
        n = 210
        while (n < 1000):
            n += 150
            try:
                var_app.driver.find_element(By.XPATH, select_vehicle).click()
                time.sleep(2)
                module_other_app.tap_scaled(var_app.driver, [(200, n)])
                time.sleep(2)
                var_app.driver.find_element(By.XPATH, var_app.report_7day).click()
                time.sleep(2)
                var_app.driver.find_element(By.XPATH, select_vehicle_iconsearch).click()

                wait = WebDriverWait(var_app.driver, 10)
                element = wait.until(EC.element_to_be_clickable((By.XPATH, check_text)))
                time.sleep(1)

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


    def select_vehicle2(self, select_vehicle, select_vehicle_iconsearch, check_text, desire):
        var_app.driver.implicitly_wait(0.5)
        n = 210
        while (n < 1000):
            n += 150
            try:
                var_app.driver.find_element(By.XPATH, select_vehicle).click()
                time.sleep(2)
                module_other_app.tap_scaled(var_app.driver, [(200, n)])
                time.sleep(2)
                var_app.driver.find_element(By.XPATH, var_app.report_today).click()
                time.sleep(2)
                var_app.driver.find_element(By.XPATH, select_vehicle_iconsearch).click()

                wait = WebDriverWait(var_app.driver, 15)
                element = wait.until(EC.element_to_be_clickable((By.XPATH, check_text)))
                time.sleep(1)

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


    def select_vehicle3(self, select_vehicle, select_vehicle_iconsearch, check_text, desire):
        var_app.driver.implicitly_wait(0.5)
        n = 250
        while (n < 1200):
            n += 150
            try:
                var_app.driver.find_element(By.XPATH, select_vehicle).click()
                time.sleep(2)
                module_other_app.tap_scaled(var_app.driver, [(60, n)])
                time.sleep(2)
                var_app.driver.find_element(By.XPATH, var_app.report_today).click()
                time.sleep(2)
                var_app.driver.find_element(By.XPATH, select_vehicle_iconsearch).click()


                try:
                    wait = WebDriverWait(var_app.driver, 4)
                    element = wait.until(EC.element_to_be_clickable((By.XPATH, check_text)))
                    time.sleep(1)

                    check_select_vehicle = var_app.driver.find_element(By.XPATH, check_text).text
                    print(check_select_vehicle)
                    if check_select_vehicle == desire:
                        print("đã click vào tọa độ 200, {} Phương tiện {}.".format(n, check_select_vehicle))
                        break
                    else:
                        print("đã click vào tọa độ 200, {} Phương tiện {}.".format(n, check_select_vehicle))
                except:
                    pass
            except:
                print("đã click vào tọa độ 200, {} Không có dữ liệu.".format(n))
                pass


    def select_vehicle4(self, select_vehicle, select_vehicle_iconsearch, check_text):
        var_app.driver.implicitly_wait(0.5)
        n = 280
        while (n < 1500):
            n += 100
            try:
                var_app.driver.find_element(By.XPATH, select_vehicle).click()
                time.sleep(2)
                module_other_app.tap_scaled(var_app.driver, [(70, n)])
                time.sleep(2)
                print(n)
                var_app.driver.find_element(By.XPATH, select_vehicle_iconsearch).click()
                try:
                    var_app.driver.implicitly_wait(0.3)
                    var_app.driver.find_element(By.XPATH, select_vehicle_iconsearch).click()
                    time.sleep(1)
                except:
                    pass
                try:
                    var_app.driver.implicitly_wait(0.3)
                    var_app.driver.find_element(By.XPATH, select_vehicle_iconsearch).click()
                    time.sleep(1)
                except:
                    pass

                try:
                    wait = WebDriverWait(var_app.driver, 4)
                    element = wait.until(EC.element_to_be_clickable((By.XPATH, check_text)))
                    break
                except:
                    pass
            except:
                print("đã click vào tọa độ 200, {} Không có dữ liệu.".format(n))
                pass



    def select_vehicle5(self, select_vehicle, select_vehicle1, select_vehicle_iconsearch, select_vehicle_iconsearch1, check_text, desire):
        var_app.driver.implicitly_wait(0.5)
        n = 300
        while (n < 1200):
            n += 80
            try:
                try:
                    var_app.driver.find_element(By.XPATH, select_vehicle).click()
                except:
                    var_app.driver.find_element(By.XPATH, select_vehicle1).click()
                time.sleep(2)
                module_other_app.tap_scaled(var_app.driver, [(60, n)])
                time.sleep(2)
                var_app.driver.find_element(By.XPATH, var_app.report_7day).click()
                time.sleep(2)
                try:
                    var_app.driver.find_element(By.XPATH, select_vehicle_iconsearch).click()
                except:
                    var_app.driver.find_element(By.XPATH, select_vehicle_iconsearch1).click()

                try:
                    wait = WebDriverWait(var_app.driver, 4)
                    element = wait.until(EC.element_to_be_clickable((By.XPATH, check_text)))
                    time.sleep(1)

                    check_select_vehicle = var_app.driver.find_element(By.XPATH, check_text).text
                    print(check_select_vehicle)
                    if check_select_vehicle == desire:
                        print("đã click vào tọa độ 200, {} Phương tiện {}.".format(n, check_select_vehicle))
                        break
                    else:
                        print("đã click vào tọa độ 200, {} Phương tiện {}.".format(n, check_select_vehicle))
                except:
                    pass
            except:
                print("đã click vào tọa độ 200, {} Không có dữ liệu.".format(n))
                pass



    def select_vehicle6(self, select_vehicle, select_vehicle_iconsearch, check_text, desire):
        var_app.driver.implicitly_wait(0.5)
        n = 300
        while (n < 1200):
            n += 80
            try:
                var_app.driver.find_element(By.XPATH, select_vehicle).click()
                print("đã click vào icon chọn xe")
                try:
                    var_app.driver.find_element(By.XPATH, select_vehicle).click()
                    print("đã click vào icon chọn xe lần 2")
                except:
                    pass
                time.sleep(2)
                module_other_app.tap_scaled(var_app.driver, [(60, n)])
                time.sleep(2)
                print("đã click vào xe")
                var_app.driver.find_element(By.XPATH, var_app.report_7day).click()
                time.sleep(2)
                var_app.driver.find_element(By.XPATH, select_vehicle_iconsearch).click()


                try:
                    wait = WebDriverWait(var_app.driver, 4)
                    element = wait.until(EC.element_to_be_clickable((By.XPATH, check_text)))
                    time.sleep(1)

                    check_select_vehicle = var_app.driver.find_element(By.XPATH, check_text).text
                    print(check_select_vehicle)
                    if check_select_vehicle == desire:
                        print("đã click vào tọa độ 200, {} Phương tiện {}.".format(n, check_select_vehicle))
                        break
                    else:
                        print("đã click vào tọa độ 200, {} Phương tiện {}.".format(n, check_select_vehicle))
                except:
                    pass
            except:
                print("đã click vào tọa độ 200, {} Không có dữ liệu.".format(n))
                pass




    def select_vehicle7(self, select_vehicle, select_vehicle_iconsearch, check_text):
        var_app.driver.implicitly_wait(0.5)
        n = 380
        while (n < 700):
            n += 80
            try:
                var_app.driver.find_element(By.XPATH, select_vehicle).click()
                print("đã click vào icon chọn xe")
                time.sleep(2)
                module_other_app.tap_scaled(var_app.driver, [(60, n)])
                time.sleep(2)
                print("đã click vào xe")
                var_app.driver.find_element(By.XPATH, var_app.report_7day).click()
                time.sleep(2)
                var_app.driver.find_element(By.XPATH, select_vehicle_iconsearch).click()

                try:
                    wait = WebDriverWait(var_app.driver, 4)
                    element = wait.until(EC.element_to_be_clickable((By.XPATH, check_text)))
                    break
                except:
                    pass
            except:
                print("đã click vào tọa độ 200, {} Không có dữ liệu.".format(n))
                pass


    def select_vehicle1(self, select_vehicle, select_vehicle_iconsearch, check_text, desire, vehicle):
        var_app.driver.implicitly_wait(0.5)
        n = 210
        while (n < 1000):
            n += 150
            try:
                var_app.driver.find_element(By.XPATH, select_vehicle).click()
                time.sleep(2)
                var_app.driver.find_element(By.XPATH, var_app.select_vehicle_input).clear()
                var_app.driver.find_element(By.XPATH, var_app.select_vehicle_input).send_keys(vehicle)
                time.sleep(2)
                module_other_app.tap_scaled(var_app.driver, [(200, n)])
                time.sleep(2)
                var_app.driver.find_element(By.XPATH, var_app.report_7day).click()
                time.sleep(2)
                var_app.driver.find_element(By.XPATH, select_vehicle_iconsearch).click()

                wait = WebDriverWait(var_app.driver, 10)
                element = wait.until(EC.element_to_be_clickable((By.XPATH, check_text)))
                time.sleep(1)

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
        var_app.driver.implicitly_wait(2)
        var_app.driver.find_element(By.XPATH, path_day).click()

        wait = WebDriverWait(var_app.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, path_check)))
        time.sleep(1.5)

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
                module_other_app.swipe_scaled(var_app.driver, startX, startY, endX, endY, duration)
            time.sleep(0.5)
        try:
            var_app.driver.find_element(By.XPATH, "//*[@text='"+path_check+"']")
            var_app.logging.info("True")
            var_app.logging.info(path_check)
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Pass")
        except:
            var_app.logging.info("False")
            var_app.logging.info(path_check)
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Fail")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, "Báo cáo bị mất trường: "+path_check+"")
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
                module_other_app.swipe_scaled(var_app.driver, endX, startY, startX, endY, duration)
            time.sleep(0.5)
            print("//*[@text='"+path_check+"']")

        try:
            var_app.driver.find_element(By.XPATH, "//*[@text='"+path_check+"']")
            var_app.logging.info("True")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Pass")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, "")
        except:
            var_app.logging.info("False")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Fail")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, "Báo cáo bị mất trường: "+path_check+"")
        time.sleep(2.5)


    def back_excel(self, number, desire):
        var_app.driver.implicitly_wait(0.2)
        try:
            var_app.driver.find_element(By.XPATH, var_app.ALLOW).click()
            time.sleep(1)
        except:
            pass
        try:
            var_app.driver.find_element(By.XPATH, var_app.DENY).click()
            time.sleep(1)
        except:
            pass

        i = 0
        while (i < number):
            i += 1
            try:
                var_app.driver.press_keycode(4)
                time.sleep(3)
                var_app.driver.find_element(By.XPATH, desire)
                break
            except:
                pass



class report:



    def report_stop_search(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(1.5)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_report_stop)
        except:
            # general.report_back(self)
            homepage_app.move_module(self, "", "", "", var_app.report_stop, 0.8, 0.65, 0.2, 0.65, 1000,  "", "", "", "_")


        general.select_vehicle(self, var_app.report_select_vehicle, var_app.report_icon_search,
                               var_app.check_report_search, "STT")

        module_other_app.write_result_text_try_if_other(code, eventname, result, "Trang chủ - báo cáo dừng đỗ",
                                              var_app.check_report_search1, "", "_BaoCao_BaoCaoDungDo_ChonPhuongTien.png")


    def report_stop_search_type(self, code, eventname, result, button, path_check, path_module, path_image):
        var_app.driver.implicitly_wait(0.3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
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
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_report_stop)
        except:
            general.report_back(self)
            homepage_app.move_module(self, "", "", "", var_app.report_stop, 0.8, 0.65, 0.2, 0.65, 1000,  "", "", "", "_")


        var_app.driver.find_element(By.XPATH, var_app.report_stop_setting).click()
        time.sleep(2.5)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - báo cáo dừng đỗ",
                                              var_app.check_report_stop_setting, "Cài đặt ẩn hiện thông tin", "_BaoCao_BaoCaoDungDo_CaiDat.png")

        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.report_stop_setting_iconx).click()
            time.sleep(1)
        except:
            pass


    def report_stop_filter(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_report_stop)
        except:
            general.report_back(self)
            homepage_app.move_module(self, "", "", "", var_app.report_stop, 0.8, 0.65, 0.2, 0.65, 1000,  "", "", "", "_")


        var_app.driver.find_element(By.XPATH, var_app.report_stop_filter).click()
        time.sleep(2.5)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - báo cáo dừng đỗ",
                                              var_app.check_report_stop_filter, "BỘ LỌC TÌM KIẾM", "_BaoCao_BaoCaoDungDo_BoLoc.png")

        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.report_stop_setting_iconx).click()
            time.sleep(1)
        except:
            pass


    def report_stop_export_excel(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_report_stop)
        except:
            general.report_back(self)
            homepage_app.move_module(self, "", "", "", var_app.report_stop, 0.8, 0.65, 0.2, 0.65, 1000,  "", "", "", "_")


        var_app.driver.find_element(By.XPATH, var_app.report_stop_export_excel).click()
        time.sleep(2.5)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.ALLOW).click()
            time.sleep(2)
        except:
            pass

        module_other_app.write_result_not_displayed_try(code, eventname, result, "Trang chủ - báo cáo dừng đỗ",
                                              var_app.check_report_stop_export_excel, "_BaoCao_BaoCaoDungDo_XuatExcel.png")

        general.back_excel(self, 4, var_app.check_report_stop)


    def report_stop_detail(self, code, eventname, result, path_check, path_check1, number_from, number_to, desire, path_image):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.find_element(By.XPATH, var_app.STT)
        except:
            report.report_stop_search(self, "", "", "")

        try:
            var_app.driver.find_element(By.XPATH, path_check)
            module_other_app.write_result_text_try_if_cut(code, eventname, result, "Trang chủ - Báo cáo dừng đỗ",
                                                  path_check, number_from, number_to, desire, path_image)
        except:
            module_other_app.write_result_text_try_if_cut(code, eventname, result, "Trang chủ - Báo cáo dừng đỗ",
                                                  path_check1, number_from, number_to, desire, path_image)


    def report_stop_check_column(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
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


    def report_stop_see_detail(self, code, eventname, result):
        var_app.driver.implicitly_wait(0.3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.find_element(By.XPATH, var_app.STT)

        except:
            report.report_stop_search(self, "", "", "")

        try:
            var_app.driver.find_element(By.XPATH, var_app.data2_column2).click()
        except:
            module_other_app.tap_scaled(var_app.driver, [(245, 688)])
            time.sleep(0.5)
            module_other_app.tap_scaled(var_app.driver, [(245, 771)])

        time.sleep(3)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - báo cáo dừng đỗ",
                                              var_app.info_detail, "THÔNG TIN CHI TIẾT", "_BaoCao_BaoCaoDungDo_XemChiTiet.png")
        var_app.driver.save_screenshot(var_app.imagepath + code + "_BaoCaoDungDo_XemChiTiet2.png")


    def report_stop_check_detail(self, code, eventname, result, type_check, path_name, path_name1, path_detail, path_detail1, desire, name_image):
        var_app.driver.implicitly_wait(0.3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        try:
            var_app.driver.implicitly_wait(2)
            var_app.driver.find_element(By.XPATH, var_app.info_detail)
        except:
            report.report_stop_see_detail(self, "", "", "")

        var_app.logging.info("--------------")
        var_app.logging.info("Trang chủ - báo cáo dừng đỗ")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)

        try:
            var_app.driver.find_element(By.XPATH, path_name)
            if type_check == "0":
                try:
                    name = var_app.driver.find_element(By.XPATH, path_name).text
                    detail = var_app.driver.find_element(By.XPATH, path_detail).text
                    module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, "{}: {}".format(name, detail))
                    var_app.logging.info(name)
                    var_app.logging.info(detail)

                    if (name == desire) and (detail != ""):
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

            if type_check == "1":
                try:
                    name = var_app.driver.find_element(By.XPATH, path_name).text
                    detail = var_app.driver.find_element(By.XPATH, path_detail).text
                    module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, "{}: {}".format(name, detail))
                    var_app.logging.info(name)
                    var_app.logging.info(detail)
                    if (name == desire) and (detail != ""):
                        var_app.logging.info("True")
                        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Pass")
                except:
                    pass

        except:
            if type_check == "0":
                try:
                    name = var_app.driver.find_element(By.XPATH, path_name1).text
                    detail = var_app.driver.find_element(By.XPATH, path_detail1).text
                    module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6,
                                               "{}: {}".format(name, detail))
                    var_app.logging.info(name)
                    var_app.logging.info(detail)

                    if (name == desire) and (detail != ""):
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

            if type_check == "1":
                try:
                    name = var_app.driver.find_element(By.XPATH, path_name1).text
                    detail = var_app.driver.find_element(By.XPATH, path_detail1).text
                    module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6,
                                               "{}: {}".format(name, detail))
                    var_app.logging.info(name)
                    var_app.logging.info(detail)
                    if (name == desire) and (detail != ""):
                        var_app.logging.info("True")
                        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Pass")
                except:
                    pass


















    def detailed_activity_reports_search(self, code, eventname, result):
        var_app.driver.implicitly_wait(0.3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_detailed_activity_reports)
        except:
            general.report_back(self)
            homepage_app.move_module(self, "", "", "", var_app.detailed_activity_reports, 0.8, 0.65, 0.2, 0.65, 1000,  "", "", "", "_")


        general.select_vehicle(self, var_app.report_select_vehicle, var_app.report_icon_search,
                               var_app.check_report_search, "STT")

        module_other_app.write_result_text_try_if_other(code, eventname, result, "Trang chủ - Báo cáo chi tiết hoạt động",
                                              var_app.check_report_search1, "", "_TrangChu_BaoCaoChiTietHoatDong_ChonPhuongTien.png")

    def detailed_activity_reports_type(self, code, eventname, result, button, path_check, path_module, path_image):
        var_app.driver.implicitly_wait(0.3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.find_element(By.XPATH, var_app.STT)
        except:
            report.detailed_activity_reports_search(self, "", "", "")


        var_app.driver.find_element(By.XPATH, button).click()
        time.sleep(1)
        var_app.driver.find_element(By.XPATH, var_app.report_icon_search).click()
        time.sleep(2.5)
        module_other_app.write_result_displayed_try(code, eventname, result, path_module,
                                                path_check, path_image)

    def detailed_activity_reports_setting(self, code, eventname, result):
        var_app.driver.implicitly_wait(0.3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_detailed_activity_reports)
        except:
            general.report_back(self)
            homepage_app.move_module(self, "", "", "", var_app.detailed_activity_reports, 0.8, 0.65, 0.2, 0.65, 1000,  "", "", "", "_")


        var_app.driver.find_element(By.XPATH, var_app.report_stop_setting).click()
        time.sleep(2.5)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Báo cáo chi tiết hoạt động",
                                              var_app.check_report_stop_setting, "Cài đặt ẩn hiện thông tin", "_TrangChu_BaoCaoChiTietHoatDong_CaiDat.png")

        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.report_stop_setting_iconx).click()
            time.sleep(1)
        except:
            pass

    def detailed_activity_reports_excel(self, code, eventname, result):
        var_app.driver.implicitly_wait(0.3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.find_element(By.XPATH, var_app.STT)
        except:
            report.detailed_activity_reports_search(self, "", "", "")

        var_app.driver.find_element(By.XPATH, var_app.detailed_activity_reports_excel).click()
        time.sleep(2.5)
        module_other_app.write_result_not_displayed_try(code, eventname, result, "Trang chủ - Báo cáo chi tiết hoạt động",
                                              var_app.check_report_stop_export_excel, "_TrangChu_BaoCaoChiTietHoatDong_XuatExcel.png")
        general.back_excel(self, 4, var_app.check_detailed_activity_reports)

    def detailed_activity_reports_detail(self, code, eventname, result, path_check, path_check1, number_from, number_to, desire, path_image):
        var_app.driver.implicitly_wait(0.3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.find_element(By.XPATH, var_app.STT)
        except:
            report.detailed_activity_reports_search(self, "", "", "")

        try:
            var_app.driver.find_element(By.XPATH, path_check)
            module_other_app.write_result_text_try_if_cut(code, eventname, result, "Trang chủ - Báo cáo chi tiết hoạt động",
                                                  path_check, number_from, number_to, desire, path_image)
        except:
            module_other_app.write_result_text_try_if_cut(code, eventname, result, "Trang chủ - Báo cáo chi tiết hoạt động",
                                                  path_check1, number_from, number_to, desire, path_image)

    def detailed_activity_reports_column(self, code, eventname, result):
        var_app.driver.implicitly_wait(0.3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
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

    def detailed_activity_reports_see_detail(self, code, eventname, result):
        var_app.driver.implicitly_wait(0.3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.find_element(By.XPATH, var_app.STT)
            var_app.driver.find_element(By.XPATH, var_app.check_detailed_activity_reports)
        except:
            report.detailed_activity_reports_search(self, "", "", "")
        try:
            var_app.driver.find_element(By.XPATH, var_app.data2_column3).click()
        except:
            module_other_app.tap_scaled(var_app.driver, [(621, 737)])
            time.sleep(2.5)
            module_other_app.tap_scaled(var_app.driver, [(606, 817)])
        time.sleep(2.5)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Báo cáo chi tiết hoạt động",
                                              var_app.info_detail, "THÔNG TIN CHI TIẾT", "_BaoCaoChiTietHoatDong_XemChiTiet.png")

    def detailed_activity_reports_check_detail(self, code, eventname, result, type_check, path_name, path_name1, path_detail, path_detail1, desire, name_image):
        var_app.driver.implicitly_wait(0.3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.info_detail)
        except:
            report.detailed_activity_reports_see_detail(self, "", "", "")

        var_app.logging.info("--------------")
        var_app.logging.info("Trang chủ - Báo cáo chi tiết hoạt động")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)

        try:
            var_app.driver.find_element(By.XPATH, path_name)
            if type_check == "0":
                try:
                    name = var_app.driver.find_element(By.XPATH, path_name).text
                    detail = var_app.driver.find_element(By.XPATH, path_detail).text
                    module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, "{}: {}".format(name, detail))
                    var_app.logging.info(name)
                    var_app.logging.info(detail)

                    if (name == desire) and (detail != ""):
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

            if type_check == "1":
                try:
                    name = var_app.driver.find_element(By.XPATH, path_name).text
                    detail = var_app.driver.find_element(By.XPATH, path_detail).text
                    module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, "{}: {}".format(name, detail))
                    var_app.logging.info(name)
                    var_app.logging.info(detail)
                    if (name == desire) and (detail != ""):
                        var_app.logging.info("True")
                        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Pass")
                except:
                    pass

        except:
            if type_check == "0":
                try:
                    name = var_app.driver.find_element(By.XPATH, path_name1).text
                    detail = var_app.driver.find_element(By.XPATH, path_detail1).text
                    module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6,
                                               "{}: {}".format(name, detail))
                    var_app.logging.info(name)
                    var_app.logging.info(detail)

                    if (name == desire) and (detail != ""):
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

            if type_check == "1":
                try:
                    name = var_app.driver.find_element(By.XPATH, path_name1).text
                    detail = var_app.driver.find_element(By.XPATH, path_detail1).text
                    module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6,
                                               "{}: {}".format(name, detail))
                    var_app.logging.info(name)
                    var_app.logging.info(detail)
                    if (name == desire) and (detail != ""):
                        var_app.logging.info("True")
                        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Pass")
                except:
                    pass















    def summary_report_of_activities_search(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.check_summary_report_of_activities)
        except:
            general.report_back(self)
            homepage_app.move_module(self, "", "", "", var_app.summary_report_of_activities, 0.8, 0.65, 0.2, 0.65, 1000,  "", "", "", "_")


        general.select_vehicle(self, var_app.report_select_vehicle, var_app.report_icon_search,
                               var_app.check_report_search, "STT")
        try:
            wait = WebDriverWait(var_app.driver, 20)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_app.check_report_search)))
        except:
            pass

        module_other_app.write_result_text_try_if_other(code, eventname, result, "Trang chủ - Báo cáo tổng hợp hoạt động",
                                              var_app.check_report_search1, "", "_TrangChu_BaoCaoTongHopHoatDong_ChonPhuongTien.png")


    def summary_report_of_activities_type(self, code, eventname, result, button, path_check, path_module, path_image):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.STT)
        except:
            report.summary_report_of_activities_search(self, "", "", "")


        var_app.driver.find_element(By.XPATH, button).click()
        time.sleep(1)
        var_app.driver.find_element(By.XPATH, var_app.report_icon_search).click()
        time.sleep(2.5)
        module_other_app.write_result_displayed_try(code, eventname, result, path_module,
                                                path_check, path_image)


    def summary_report_of_activities_setting(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.check_summary_report_of_activities)
        except:
            general.report_back(self)
            homepage_app.move_module(self, "", "", "", var_app.summary_report_of_activities, 0.8, 0.65, 0.2, 0.65, 1000,  "", "", "", "_")


        var_app.driver.find_element(By.XPATH, var_app.report_setting1).click()
        time.sleep(2.5)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Báo cáo tổng hợp hoạt động",
                                              var_app.check_report_setting, "Cài đặt ẩn hiện thông tin", "_TrangChu_BaoCaoTongHopHoatDong_CaiDat.png")

        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.cancel1).click()
            time.sleep(1)
        except:
            pass


    def summary_report_of_activities_filter(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.check_summary_report_of_activities)
        except:
            general.report_back(self)
            homepage_app.move_module(self, "", "", "", var_app.summary_report_of_activities, 0.8, 0.65, 0.2, 0.65, 1000,  "", "", "", "_")


        var_app.driver.find_element(By.XPATH, var_app.report_filter1).click()
        time.sleep(2.5)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Báo cáo tổng hợp hoạt động",
                                              var_app.check_report_filter, "BỘ LỌC TÌM KIẾM", "_TrangChu_BaoCaoTongHopHoatDong_BoLoc.png")

        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.report_filter_x).click()
            time.sleep(1)
        except:
            pass


    def summary_report_of_activities_excel(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.STT)
        except:
            report.summary_report_of_activities_search(self, "", "", "")


        var_app.driver.find_element(By.XPATH, var_app.summary_report_of_activities_excel).click()
        time.sleep(2.5)
        module_other_app.write_result_not_displayed_try(code, eventname, result, "Trang chủ - Báo cáo tổng hợp hoạt động",
                                              var_app.check_export_excel, "_TrangChu_BaoCaoTongHopHoatDong_XuatExcel.png")

        general.back_excel(self, 4, var_app.check_summary_report_of_activities)


    def summary_report_of_activities_detail(self, code, eventname, result, path_check, path_check1, number_from, number_to, desire, path_image):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.STT)
        except:
            general.report_back(self)
            report.summary_report_of_activities_search(self, "", "", "")

        try:
            var_app.driver.find_element(By.XPATH, path_check)
            module_other_app.write_result_text_try_if_cut(code, eventname, result, "Trang chủ - Báo cáo tổng hợp hoạt động",
                                                  path_check, number_from, number_to, desire, path_image)
        except:
            module_other_app.write_result_text_try_if_cut(code, eventname, result, "Trang chủ - Báo cáo tổng hợp hoạt động",
                                                  path_check1, number_from, number_to, desire, path_image)


    def summary_report_of_activities_column(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
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


    def summary_report_of_activities_see_detail(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.check_summary_report_of_activities)
            var_app.driver.find_element(By.XPATH, var_app.STT)
        except:
            report.summary_report_of_activities_search(self, "", "", "")

        try:
            var_app.driver.find_element(By.XPATH, var_app.data2_column3).click()
        except:
            module_other_app.tap_scaled(var_app.driver, [(621, 832)])
            time.sleep(2.5)
            module_other_app.tap_scaled(var_app.driver, [(621, 912)])
        time.sleep(2.5)



        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Trang chủ - Báo cáo tổng hợp hoạt động",
                                              var_app.info_detail, "THÔNG TIN CHI TIẾT", "_BaoCaoTongHopHoatDong_XemChiTiet.png")


    def summary_report_of_activities_check_detail(self, code, eventname, result, type_check, path_name, path_name1, path_detail, path_detail1, desire, name_image):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.info_detail)
        except:
            report.summary_report_of_activities_see_detail(self, "", "", "")

        var_app.logging.info("--------------")
        var_app.logging.info("Trang chủ - Báo cáo tổng hợp hoạt động")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)

        try:
            var_app.driver.find_element(By.XPATH, path_name)
            if type_check == "0":
                try:
                    name = var_app.driver.find_element(By.XPATH, path_name).text
                    detail = var_app.driver.find_element(By.XPATH, path_detail).text
                    module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, "{}: {}".format(name, detail))
                    var_app.logging.info(name)
                    var_app.logging.info(detail)

                    if (name == desire) and (detail != ""):
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

            if type_check == "1":
                try:
                    name = var_app.driver.find_element(By.XPATH, path_name).text
                    detail = var_app.driver.find_element(By.XPATH, path_detail).text
                    module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, "{}: {}".format(name, detail))
                    var_app.logging.info(name)
                    var_app.logging.info(detail)
                    if (name == desire) and (detail != ""):
                        var_app.logging.info("True")
                        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Pass")
                except:
                    pass
        except:
            if type_check == "0":
                try:
                    name = var_app.driver.find_element(By.XPATH, path_name1).text
                    detail = var_app.driver.find_element(By.XPATH, path_detail1).text
                    module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, "{}: {}".format(name, detail))
                    var_app.logging.info(name)
                    var_app.logging.info(detail)
                    if (name == desire) and (detail != ""):
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

            if type_check == "1":
                try:
                    name = var_app.driver.find_element(By.XPATH, path_name1).text
                    detail = var_app.driver.find_element(By.XPATH, path_detail1).text
                    module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, "{}: {}".format(name, detail))
                    var_app.logging.info(name)
                    var_app.logging.info(detail)
                    if (name == desire) and (detail != ""):
                        var_app.logging.info("True")
                        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Pass")
                except:
                    pass




















    def report_entering_and_exiting_the_station_search(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.check_report_entering_and_exiting_the_station)
        except:
            homepage_app.move_module(self, "", "", "", var_app.report_entering_and_exiting_the_station, 0.8, 0.65, 0.2, 0.65, 1000,  "", "", "", "_")

        general.select_vehicle(self, var_app.report_select_vehicle, var_app.report_icon_search,
                               var_app.check_report_search, "STT")

        module_other_app.write_result_text_try_if_other(code, eventname, result, "Trang chủ - Báo cáo ra vào trạm",
                                              var_app.check_report_search1, "", "_TrangChu_BaoCaoRaVaotram_ChonPhuongTien.png")


    def report_entering_and_exiting_the_station_type(self, code, eventname, result, button, path_check, path_module, path_image):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.STT)
        except:
            report.report_entering_and_exiting_the_station_search(self, "", "", "")

        var_app.driver.find_element(By.XPATH, button).click()
        time.sleep(1)
        var_app.driver.find_element(By.XPATH, var_app.report_icon_search).click()
        time.sleep(2.5)
        module_other_app.write_result_displayed_try(code, eventname, result, path_module,
                                                path_check, path_image)


    def report_entering_and_exiting_the_station_setting(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_report_entering_and_exiting_the_station)
        except:
            homepage_app.move_module(self, "", "", "", var_app.report_entering_and_exiting_the_station, 0.8, 0.65, 0.2, 0.65, 1000,  "", "", "", "_")


        var_app.driver.find_element(By.XPATH, var_app.report_setting1).click()
        time.sleep(2.5)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Báo cáo ra vào trạm",
                                              var_app.check_report_setting, "Cài đặt ẩn hiện thông tin", "_TrangChu_BaoCaoRaVaotram_CaiDat.png")

        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.cancel1).click()
            time.sleep(1)
        except:
            pass


    def report_entering_and_exiting_the_station_filter(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.check_report_entering_and_exiting_the_station)
        except:
            homepage_app.move_module(self, "", "", "", var_app.report_entering_and_exiting_the_station, 0.8, 0.65, 0.2, 0.65, 1000,  "", "", "", "_")


        var_app.driver.find_element(By.XPATH, var_app.report_filter1).click()
        time.sleep(2.5)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Báo cáo tổng hợp hoạt động",
                                              var_app.check_report_filter, "BỘ LỌC TÌM KIẾM", "_TrangChu_BaoCaoRaVaotram_BoLoc.png")

        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.report_filter_x).click()
            time.sleep(1)
        except:
            pass


    def report_entering_and_exiting_the_station_excel(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.check_report_search)
        except:
            report.summary_report_of_activities_search(self, "", "", "")


        var_app.driver.find_element(By.XPATH, var_app.summary_report_of_activities_excel).click()
        time.sleep(2.5)
        module_other_app.write_result_not_displayed_try(code, eventname, result, "Trang chủ - Báo cáo ra vào trạm",
                                              var_app.check_export_excel, "_TrangChu_BaoCaoRaVaotram_XuatExcel.png")
        general.back_excel(self, 4, var_app.check_report_entering_and_exiting_the_station)


    def report_entering_and_exiting_the_station_column(self, code, eventname, result):
        var_app.driver.implicitly_wait(0.3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
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
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.check_report_speeding)
        except:
            homepage_app.move_module(self, "", "", "", var_app.report_speeding, 0.8, 0.65, 0.2, 0.65, 1000, "", "", "", "_")

        var_app.driver.find_element(By.XPATH, var_app.report_select_vehicle).click()
        time.sleep(2)
        module_other_app.tap_scaled(var_app.driver, [(200, 360)])
        time.sleep(2)
        var_app.driver.find_element(By.XPATH, var_app.report_icon_search).click()
        time.sleep(2)
        try:
            wait = WebDriverWait(var_app.driver, 30)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_app.check_report_search1)))
        except:
            pass

        module_other_app.write_result_text_try_if_other(code, eventname, result, "Trang chủ - Báo cáo quá tốc độ",
                                              var_app.check_report_search1, "", "_TrangChu_BaoCaoQuaTocDo_ChonPhuongTien.png")


    def report_speeding_type(self, code, eventname, result, button):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
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
        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Pass")

        try:
            var_app.driver.implicitly_wait(0.3)
            checkdata = var_app.driver.find_element(By.XPATH, var_app.no_data).text
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, checkdata)
        except:
            pass


    def report_speeding_setting(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.check_report_speeding)
        except:
            homepage_app.move_module(self, "", "", "", var_app.report_speeding, 0.8, 0.65, 0.2, 0.65, 1000,  "", "", "", "_")


        var_app.driver.find_element(By.XPATH, var_app.report_setting1).click()
        time.sleep(2.5)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Báo cáo quá tốc độ",
                                              var_app.check_report_setting, "Cài đặt ẩn hiện thông tin", "_TrangChu_BaoCaoQuaTocDo_CaiDat.png")

        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.cancel1).click()
            time.sleep(1)
        except:
            pass


    def report_speeding_filter(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_report_speeding)
        except:
            homepage_app.move_module(self, "", "", "", var_app.report_speeding, 0.8, 0.65, 0.2, 0.65, 1000,  "", "", "", "_")


        var_app.driver.find_element(By.XPATH, var_app.report_filter1).click()
        time.sleep(2.5)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Báo cáo quá tốc độ",
                                              var_app.check_report_filter, "BỘ LỌC TÌM KIẾM", "_TrangChu_BaoCaoQuaTocDo_BoLoc.png")

        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.report_filter_x).click()
            time.sleep(1)
        except:
            pass


    def report_speeding_excel(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
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
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, check_text)
            var_app.driver.find_element(By.XPATH, var_app.report_speeding_excel).click()
            check_text2 = var_app.driver.find_element(By.XPATH, var_app.check_report_speeding_excel).text
            var_app.logging.info(check_text)
            var_app.logging.info(check_text2)
            if check_text == check_text2:
                var_app.logging.info("True")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Pass")
            else:
                var_app.logging.info("False")
                var_app.driver.save_screenshot(var_app.imagepath + code + "_TrangChu_BaoCaoQuaTocDo_XuatExcel")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Fail")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 13, code + "_TrangChu_BaoCaoQuaTocDo_XuatExcel")
        except:
            pass








    def business_trip_report_search(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.check_business_trip_report)
        except:
            homepage_app.move_module(self, "", "", "", var_app.business_trip_report, 0.8, 0.65, 0.2, 0.65, 1000,  "", "", "", "_")

        general.select_vehicle(self, var_app.report_select_vehicle, var_app.report_icon_search,
                               var_app.check_report_search, "STT")

        try:
            wait = WebDriverWait(var_app.driver, 30)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_app.check_report_search)))
        except:
            pass

        module_other_app.write_result_text_try_if_other(code, eventname, result, "Trang chủ - Báo cáo chuyến kinh doanh",
                                              var_app.check_report_search1, "", "_TrangChu_BaoCaoChuyenKinhDoanh_ChonPhuongTien.png")

    def business_trip_report_type(self, code, eventname, result, button, path_check, path_module, path_image):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
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
        try:
            var_app.driver.implicitly_wait(0.3)
            checkdata = var_app.driver.find_element(By.XPATH, var_app.no_data).text
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, checkdata)
            if path_image == "_TrangChu_BaoCaoChuyenKinhDoanh_HomNay.png":
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "")
        except:
            pass

    def business_trip_report_setting(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.check_business_trip_report)
        except:
            homepage_app.move_module(self, "", "", "", var_app.business_trip_report, 0.8, 0.65, 0.2, 0.65, 1000,  "", "", "", "_")


        var_app.driver.find_element(By.XPATH, var_app.report_setting1).click()
        time.sleep(2.5)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Báo cáo chuyến kinh doanh",
                                              var_app.check_report_setting, "Cài đặt ẩn hiện thông tin", "_TrangChu_BaoCaoChuyenKinhDoanh_CaiDat.png")

        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.cancel1).click()
            time.sleep(1)
        except:
            pass

    def business_trip_report_filter(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_business_trip_report)
        except:
            homepage_app.move_module(self, "", "", "", var_app.business_trip_report, 0.8, 0.65, 0.2, 0.65, 1000,  "", "", "", "_")

        var_app.driver.find_element(By.XPATH, var_app.report_filter1).click()
        time.sleep(2.5)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Báo cáo chuyến kinh doanh",
                                              var_app.check_report_filter, "BỘ LỌC TÌM KIẾM", "_TrangChu_BaoCaoChuyenKinhDoanh_BoLoc.png")

        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.report_filter_x).click()
            time.sleep(1)
        except:
            pass

    def business_trip_report_excel(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.check_report_search)
        except:
            report.business_trip_report_search(self, "", "", "")

        var_app.driver.find_element(By.XPATH, var_app.business_trip_report_excel).click()
        time.sleep(2.5)
        module_other_app.write_result_not_displayed_try(code, eventname, result, "Trang chủ - Báo cáo chuyến kinh doanh",
                                              var_app.check_export_excel, "_TrangChu_BaoCaoChuyenKinhDoanh_XuatExcel.png")
        general.back_excel(self, 4, var_app.check_business_trip_report)

    def business_trip_report_detail(self, code, eventname, result, path_check, path_check1, number_from, number_to, desire, path_image):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.STT)
        except:
            report.business_trip_report_search(self, "", "", "")

        try:
            var_app.driver.find_element(By.XPATH, path_check)
            module_other_app.write_result_text_try_if_cut(code, eventname, result, "Trang chủ - Báo cáo chuyến kinh doanh",
                                                  path_check, number_from, number_to, desire, path_image)
        except:
            module_other_app.write_result_text_try_if_cut(code, eventname, result, "Trang chủ - Báo cáo chuyến kinh doanh",
                                                  path_check1, number_from, number_to, desire, path_image)

    def business_trip_report_column(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
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
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.check_report_loss_of_signal)
        except:
            homepage_app.move_module(self, "", "", "", var_app.report_loss_of_signal, 0.8, 0.65, 0.2, 0.65, 1000,  "", "", "", "_")

        general.select_vehicle(self, var_app.report_select_vehicle, var_app.report_icon_search,
                               var_app.check_report_search, "STT")

        try:
            wait = WebDriverWait(var_app.driver, 30)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_app.check_report_search)))
        except:
            pass

        module_other_app.write_result_text_try_if_other(code, eventname, result, "Trang chủ - Báo cáo mất tín hiệu",
                                              var_app.check_report_search1, "", "_TrangChu_BaoCaoMatTinHieu_ChonPhuongTien.png")

    def report_loss_of_signal_type(self, code, eventname, result, button, path_check, path_module, path_image):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.STT)
        except:
            report.report_loss_of_signal_search(self, "", "", "")

        var_app.driver.find_element(By.XPATH, button).click()
        time.sleep(1)
        var_app.driver.find_element(By.XPATH, var_app.report_icon_search).click()
        time.sleep(2.5)
        module_other_app.write_result_displayed_try(code, eventname, result, path_module,
                                                path_check, path_image)

    def report_loss_of_signal_setting(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.check_report_loss_of_signal)
        except:
            homepage_app.move_module(self, "", "", "", var_app.report_loss_of_signal, 0.8, 0.65, 0.2, 0.65, 1000,  "", "", "", "_")


        var_app.driver.find_element(By.XPATH, var_app.report_setting1).click()
        time.sleep(2.5)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Báo cáo mất tín hiệu",
                                              var_app.check_report_setting, "Cài đặt ẩn hiện thông tin", "_TrangChu_BaoCaoMatTinHieu_CaiDat.png")

        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.cancel1).click()
            time.sleep(1)
        except:
            pass

    def report_loss_of_signal_filter(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.check_report_loss_of_signal)
        except:
            homepage_app.move_module(self, "", "", "", var_app.report_loss_of_signal, 0.8, 0.65, 0.2, 0.65, 1000,  "", "", "", "_")

        var_app.driver.find_element(By.XPATH, var_app.report_filter1).click()
        time.sleep(2.5)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Báo cáo mất tín hiệu",
                                              var_app.check_report_filter, "BỘ LỌC TÌM KIẾM", "_TrangChu_BaoCaoMatTinHieu_BoLoc.png")

        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.report_filter_x).click()
            time.sleep(1)
        except:
            pass

    def report_loss_of_signal_excel(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.check_report_search)
        except:
            report.report_loss_of_signal_search(self, "", "", "")


        var_app.driver.find_element(By.XPATH, var_app.report_loss_of_signal_excel).click()
        time.sleep(2.5)

        module_other_app.write_result_not_displayed_try(code, eventname, result, "Trang chủ - Báo cáo mất tín hiệu",
                                              var_app.check_export_excel, "_TrangChu_BaoCaoMatTinHieu_XuatExcel.png")
        general.back_excel(self, 4, var_app.check_report_loss_of_signal)

    def report_loss_of_signal_detail(self, code, eventname, result, path_check, path_check1, number_from, number_to, desire, path_image):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.find_element(By.XPATH, var_app.STT)
        except:
            report.report_loss_of_signal_search(self, "", "", "")

        try:
            var_app.driver.find_element(By.XPATH, path_check)
            module_other_app.write_result_text_try_if_cut(code, eventname, result, "Trang chủ - Báo cáo mất tín hiệu",
                                                  path_check, number_from, number_to, desire, path_image)
        except:
            module_other_app.write_result_text_try_if_cut(code, eventname, result, "Trang chủ - Báo cáo mất tín hiệu",
                                                  path_check1, number_from, number_to, desire, path_image)

    def report_loss_of_signal_column(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
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

    def report_loss_of_signal_see_detail(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.report_7day).click()
            time.sleep(2.5)
            var_app.driver.find_element(By.XPATH, var_app.report_icon_search).click()
            time.sleep(3)
        except:
            pass


        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.check_report_loss_of_signal)
            var_app.driver.find_element(By.XPATH, var_app.report_filed1)
        except:
            general.report_back(self)
            report.report_loss_of_signal_search(self, "", "", "")

        try:
            var_app.driver.find_element(By.XPATH, var_app.data2_column2).click()
        except:
            module_other_app.tap_scaled(var_app.driver, [(294, 545)])
            time.sleep(2.5)
            module_other_app.tap_scaled(var_app.driver, [(294, 621)])
        time.sleep(2.5)

        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Báo cáo mất tín hiệu",
                                              var_app.info_detail, "THÔNG TIN CHI TIẾT", "_BaoCaoMatTinHieu_XemChiTiet.png")

    def report_loss_of_signal_check_detail(self, code, eventname, result, type_check, path_name, path_name1, path_detail, path_detail1, desire, name_image):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.info_detail)
        except:
            report.report_loss_of_signal_see_detail(self, "", "", "")

        var_app.logging.info("--------------")
        var_app.logging.info("Trang chủ - Báo cáo mất tín hiệu")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)

        try:
            var_app.driver.find_element(By.XPATH, path_name)
            if type_check == "0":
                try:
                    name = var_app.driver.find_element(By.XPATH, path_name).text
                    detail = var_app.driver.find_element(By.XPATH, path_detail).text
                    module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, "{}: {}".format(name, detail))
                    var_app.logging.info(name)
                    var_app.logging.info(detail)

                    if (name == desire) and (detail != ""):
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

            if type_check == "1":
                try:
                    name = var_app.driver.find_element(By.XPATH, path_name).text
                    detail = var_app.driver.find_element(By.XPATH, path_detail).text
                    module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, "{}: {}".format(name, detail))
                    var_app.logging.info(name)
                    var_app.logging.info(detail)
                    if (name == desire) and (detail != ""):
                        var_app.logging.info("True")
                        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Pass")
                except:
                    pass
        except:
            if type_check == "0":
                try:
                    name = var_app.driver.find_element(By.XPATH, path_name1).text
                    detail = var_app.driver.find_element(By.XPATH, path_detail1).text
                    module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6,
                                               "{}: {}".format(name, detail))
                    var_app.logging.info(name)
                    var_app.logging.info(detail)

                    if (name == desire) and (detail != ""):
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

            if type_check == "1":
                try:
                    name = var_app.driver.find_element(By.XPATH, path_name1).text
                    detail = var_app.driver.find_element(By.XPATH, path_detail1).text
                    module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6,
                                               "{}: {}".format(name, detail))
                    var_app.logging.info(name)
                    var_app.logging.info(detail)
                    if (name == desire) and (detail != ""):
                        var_app.logging.info("True")
                        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Pass")
                except:
                    pass














    def fuel_dump_report_search(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.check_fuel_dump_report)
        except:
            homepage_app.move_module(self, "", "", "", var_app.fuel_dump_report, 0.8, 0.65, 0.2, 0.65, 1000,  "", "", "", "")

        general.select_vehicle(self, var_app.report_select_vehicle, var_app.report_icon_search,
                               var_app.check_report_search, "STT")

        try:
            wait = WebDriverWait(var_app.driver, 30)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_app.check_report_search)))
        except:
            pass

        module_other_app.write_result_text_try_if_other(code, eventname, result, "Trang chủ - Báo cáo đổ hút nhiên liệu",
                                              var_app.check_report_search1, "", "_TrangChu_BaoCaoDoHutNhienLieu_ChonPhuongTien.png")


    def fuel_dump_report_type(self, code, eventname, result, button, path_check, path_module, path_image):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.STT)
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
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Pass")

        else:
            module_other_app.write_result_displayed_try(code, eventname, result, path_module,
                                                    path_check, path_image)


    def fuel_dump_report_type1(self, code, eventname, result, button, path_check, path_module, path_image):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.STT)
        except:
            report.fuel_dump_report_search(self, "", "", "")

        var_app.driver.find_element(By.XPATH, button).click()
        time.sleep(2.5)
        # var_app.driver.find_element(By.XPATH, var_app.report_icon_search).click()
        # time.sleep(2.5)

        if path_image == "_TrangChu_BaoCaoDoHutNhienLieu_HomNay.png":
            var_app.logging.info("--------------")
            var_app.logging.info("Trang chủ - Báo cáo đổ hút nhiên liệu")
            var_app.logging.info("Mã - " + code)
            var_app.logging.info("Tên sự kiện - " + eventname)
            var_app.logging.info("Kết quả - " + result)
            var_app.logging.info("True")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Pass")

        else:
            module_other_app.write_result_displayed_try(code, eventname, result, path_module,
                                                    path_check, path_image)


    def fuel_dump_report_setting(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.check_fuel_dump_report)
        except:
            homepage_app.move_module(self, "", "", "", var_app.fuel_dump_report, 0.8, 0.65, 0.2, 0.65, 1000,  "", "", "", "_")

        var_app.driver.find_element(By.XPATH, var_app.report_setting1).click()
        time.sleep(2.5)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Báo cáo đổ hút nhiên liệu",
                                              var_app.check_report_setting, "Cài đặt ẩn hiện thông tin", "_TrangChu_BaoCaoDoHutNhienLieu_CaiDat.png")

        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.cancel1).click()
            time.sleep(1)
        except:
            pass


    def fuel_dump_report_filter(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.check_fuel_dump_report)
        except:
            homepage_app.move_module(self, "", "", "", var_app.fuel_dump_report, 0.8, 0.65, 0.2, 0.65, 1000,  "", "", "", "_")


        var_app.driver.find_element(By.XPATH, var_app.report_filter1).click()
        time.sleep(2.5)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Báo cáo đổ hút nhiên liệu",
                                              var_app.check_report_filter, "BỘ LỌC TÌM KIẾM", "_TrangChu_BaoCaoDoHutNhienLieu_BoLoc.png")

        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.report_filter_x).click()
            time.sleep(1)
        except:
            pass


    def fuel_dump_report_excel(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.check_report_search)
        except:
            report.fuel_dump_report_search(self, "", "", "")

        var_app.driver.find_element(By.XPATH, var_app.fuel_dump_report_excel).click()
        time.sleep(2.5)

        module_other_app.write_result_not_displayed_try(code, eventname, result, "Trang chủ - Báo cáo đổ hút nhiên liệu",
                                              var_app.check_export_excel, "_TrangChu_BaoCaoDoHutNhienLieu_XuatExcel.png")
        general.back_excel(self, 4, var_app.check_fuel_dump_report)


    def fuel_dump_report_detail(self, code, eventname, result, path_check, path_check1, number_from, number_to, desire, path_image):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        try:
            var_app.driver.find_element(By.XPATH, var_app.report_7day).click()
            time.sleep(2.5)
            var_app.driver.find_element(By.XPATH, var_app.report_icon_search).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.STT)
        except:
            report.fuel_dump_report_search(self, "", "", "")

        try:
            var_app.driver.find_element(By.XPATH, path_check)
            module_other_app.write_result_text_try_if_cut(code, eventname, result, "Trang chủ - Báo cáo đổ hút nhiên liệu",
                                                  path_check, number_from, number_to, desire, path_image)
        except:
            module_other_app.write_result_text_try_if_cut(code, eventname, result, "Trang chủ - Báo cáo đổ hút nhiên liệu",
                                                  path_check1, number_from, number_to, desire, path_image)


    def fuel_dump_report_column(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
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
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Km tích lũy từ đầu ngày")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Số lít")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Trạng thái")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Địa chỉ")

        general.report_back(self)


    def fuel_dump_report_see_detail(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.check_fuel_dump_report)
            var_app.driver.find_element(By.XPATH, var_app.report_filed1)
        except:
            general.report_back(self)
            report.fuel_dump_report_search(self, "", "", "")

        try:
            var_app.driver.find_element(By.XPATH, var_app.data2_column2).click()
        except:
            module_other_app.tap_scaled(var_app.driver, [(250, 560)])
            time.sleep(2.5)
            module_other_app.tap_scaled(var_app.driver, [(260, 650)])
        time.sleep(2.5)

        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Báo cáo đổ hút nhiên liệu",
                                              var_app.info_detail, "THÔNG TIN CHI TIẾT", "_BaoCaoDoHutNhienLieu_XemChiTiet.png")


    def fuel_dump_report_check_detail(self, code, eventname, result, type_check, path_name, path_name1, path_detail, path_detail1, desire, name_image):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)

        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.info_detail)
        except:
            report.fuel_dump_report_see_detail(self, "", "", "")

        var_app.logging.info("--------------")
        var_app.logging.info("Trang chủ - Báo cáo đổ hút nhiên liệu")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)

        try:
            var_app.driver.find_element(By.XPATH, path_name)
            if type_check == "0":
                try:
                    name = var_app.driver.find_element(By.XPATH, path_name).text
                    detail = var_app.driver.find_element(By.XPATH, path_detail).text
                    module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, "{}: {}".format(name, detail))
                    var_app.logging.info(name)
                    var_app.logging.info(detail)

                    if (name == desire) and (detail != ""):
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

            if type_check == "1":
                try:
                    name = var_app.driver.find_element(By.XPATH, path_name).text
                    detail = var_app.driver.find_element(By.XPATH, path_detail).text
                    module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, "{}: {}".format(name, detail))
                    var_app.logging.info(name)
                    var_app.logging.info(detail)
                    if (name == desire) and (detail != ""):
                        var_app.logging.info("True")
                        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Pass")
                except:
                    pass
        except:
            if type_check == "0":
                try:
                    name = var_app.driver.find_element(By.XPATH, path_name1).text
                    detail = var_app.driver.find_element(By.XPATH, path_detail1).text
                    module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6,
                                               "{}: {}".format(name, detail))
                    var_app.logging.info(name)
                    var_app.logging.info(detail)

                    if (name == desire) and (detail != ""):
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

            if type_check == "1":
                try:
                    name = var_app.driver.find_element(By.XPATH, path_name1).text
                    detail = var_app.driver.find_element(By.XPATH, path_detail1).text
                    module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6,
                                               "{}: {}".format(name, detail))
                    var_app.logging.info(name)
                    var_app.logging.info(detail)
                    if (name == desire) and (detail != ""):
                        var_app.logging.info("True")
                        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Pass")
                except:
                    pass







    def engine_report_search(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(1.5)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.check_engine_report)
        except:
            homepage_app.move_module2(self, "", "", "", var_app.engine_report, 0.8, 0.65, 0.2, 0.65, 1000,  "", "", "", "")

        general.select_vehicle1(self, var_app.report_select_vehicle, var_app.report_icon_search,
                               var_app.check_report_search, "STT", "50H07444 ")

        try:
            wait = WebDriverWait(var_app.driver, 30)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_app.check_report_search)))
        except:
            pass

        try:
            var_app.driver.find_element(By.XPATH, var_app.check_report_search1)
            module_other_app.write_result_text_try_if_other(code, eventname, result, "Trang chủ - Báo cáo động cơ",
                                                  var_app.check_report_search1, "", "_TrangChu_BaoCaoDongCo_ChonPhuongTien.png")
        except:
            var_app.logging.info("--------------")
            var_app.logging.info("Trang chủ - Báo cáo động cơ")
            var_app.logging.info("Mã - " + code)
            var_app.logging.info("Tên sự kiện - " + eventname)
            var_app.logging.info("Kết quả - " + result)
            var_app.driver.implicitly_wait(0.5)
            try:
                checkdata = var_app.driver.find_element(By.XPATH, var_app.no_data).text
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, checkdata)
            except:
                pass


    def engine_report_type(self, code, eventname, result, button, path_check, path_module, path_image):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.STT)
        except:
            report.engine_report_search(self, "", "", "")


        var_app.driver.find_element(By.XPATH, button).click()
        time.sleep(1)
        var_app.driver.find_element(By.XPATH, var_app.report_icon_search).click()
        time.sleep(2.5)

        # if path_image == "_TrangChu_BaoCaoDongCo_HomNay.png":
        #     var_app.logging.info("--------------")
        #     var_app.logging.info("Trang chủ - Báo cáo động cơ")
        #     var_app.logging.info("Mã - " + code)
        #     var_app.logging.info("Tên sự kiện - " + eventname)
        #     var_app.logging.info("Kết quả - " + result)
        #     var_app.logging.info("True")
        #     module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Pass")
        #
        # else:
        #     module_other_app.write_result_displayed_try(code, eventname, result, path_module,
        #                                             path_check, path_image)
        var_app.driver.implicitly_wait(0.5)
        try:
            var_app.driver.find_element(By.XPATH, var_app.STT)
            module_other_app.write_result_displayed_try(code, eventname, result, path_module,
                                                    path_check, path_image)
        except:
            nodata = var_app.driver.find_element(By.XPATH, var_app.no_data).text
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, nodata)


    def engine_report_setting(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.check_engine_report)
        except:
            homepage_app.move_module2(self, "", "", "", var_app.engine_report, 0.8, 0.65, 0.2, 0.65, 1000,  "", "", "", "_")


        var_app.driver.find_element(By.XPATH, var_app.report_setting1).click()
        time.sleep(2.5)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Báo cáo động cơ",
                                              var_app.check_report_setting, "Cài đặt ẩn hiện thông tin", "_TrangChu_BaoCaoDongCo_CaiDat.png")

        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.cancel1).click()
            time.sleep(1)
        except:
            pass


    def engine_report_filter(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.check_engine_report)
        except:
            homepage_app.move_module2(self, "", "", "", var_app.engine_report, 0.8, 0.65, 0.2, 0.65, 1000,  "", "", "", "_")


        var_app.driver.find_element(By.XPATH, var_app.report_filter1).click()
        time.sleep(2.5)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Báo cáo động cơ",
                                              var_app.check_report_filter, "BỘ LỌC TÌM KIẾM", "_TrangChu_BaoCaoDongCo_BoLoc.png")

        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.report_filter_x).click()
            time.sleep(1)
        except:
            pass


    def engine_report_excel(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.check_engine_report)
        except:
            report.engine_report_search(self, "", "", "")

        var_app.driver.find_element(By.XPATH, var_app.engine_report_excel).click()
        time.sleep(2.5)
        module_other_app.write_result_not_displayed_try(code, eventname, result, "Trang chủ - Báo cáo động cơ",
                                              var_app.check_export_excel, "_TrangChu_BaoCaoDongCo_XuatExcel.png")
        general.back_excel(self, 4, var_app.check_engine_report)


    def engine_report_detail(self, code, eventname, result, path_check, path_check1, number_from, number_to, desire, path_image):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.STT)
        except:
            report.engine_report_search(self, "", "", "")

        var_app.driver.implicitly_wait(0.5)
        try:
            var_app.driver.find_element(By.XPATH, path_check)
            module_other_app.write_result_text_try_if_cut(code, eventname, result, "Trang chủ - Báo cáo động cơ",
                                                  path_check, number_from, number_to, desire, path_image)
        except:
            try:
                module_other_app.write_result_text_try_if_cut(code, eventname, result, "Trang chủ - Báo cáo động cơ",
                                                      path_check1, number_from, number_to, desire, path_image)
            except:
                pass

        try:
            nodata = var_app.driver.find_element(By.XPATH, var_app.no_data).text
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, nodata)
        except:
            pass


    def engine_report_column(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
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
        try:
            var_app.driver.find_element(By.XPATH, var_app.STT)
            general.check_column1(self, code, 825, 1200, 650, 1200, 150, "STT")
            general.check_column(self, code, 825, 1200, 650, 1200, 150, "Giờ bắt đầu")
            general.check_column(self, code, 825, 1200, 650, 1200, 150, "Giờ đến")
            general.check_column(self, code, 825, 1200, 650, 1200, 150, "Số phút ")
            general.check_column(self, code, 825, 1200, 650, 1200, 150, "Nhiên liệu")
            general.check_column(self, code, 825, 1200, 650, 1200, 150, "Địa chỉ đi")
            general.check_column(self, code, 825, 1200, 650, 1200, 150, "Địa chỉ đến")
        except:
            nodata = var_app.driver.find_element(By.XPATH, var_app.no_data).text
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, nodata)
        general.report_back(self)










    def detail_vehicle_fuel_chart_search(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.check_detail_vehicle_fuel_chart)
        except:
            homepage_app.move_module(self, "", "", "", var_app.detail_vehicle_fuel_chart, 0.8, 0.65, 0.2, 0.65, 1000, "", "", "", "_")

        var_app.driver.find_element(By.XPATH, var_app.detail_vehicle_fuel_chart_select_vehicle).click()
        time.sleep(2)
        module_other_app.tap_scaled(var_app.driver, [(200, 360)])
        time.sleep(2)
        var_app.driver.find_element(By.XPATH, var_app.detail_vehicle_fuel_chart_icon_search).click()
        time.sleep(5)

        try:
            wait = WebDriverWait(var_app.driver, 10)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_app.check_detail_vehicle_fuel_chart_search1)))
            module_other_app.write_result_displayed_try(code, eventname, result, "Trang chủ - Báo cáo quá tốc độ",
                                                    var_app.check_detail_vehicle_fuel_chart_search1, "_TrangChu_BieuDoNhienLieu_TimKiem.png")
        except:
            wait = WebDriverWait(var_app.driver, 10)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_app.check_detail_vehicle_fuel_chart_search)))
            module_other_app.write_result_displayed_try(code, eventname, result, "Trang chủ - Báo cáo quá tốc độ",
                                                    var_app.check_detail_vehicle_fuel_chart_search, "_TrangChu_BieuDoNhienLieu_TimKiem.png")


        try:
            var_app.driver.implicitly_wait(0.3)
            vehicle = var_app.driver.find_element(By.XPATH, var_app.check_report_search2).text
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, vehicle)
        except:
            pass

    def detail_vehicle_fuel_chart_filter(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.check_detail_vehicle_fuel_chart)
        except:
            homepage_app.move_module(self, "", "", "", var_app.detail_vehicle_fuel_chart, 0.8, 0.65, 0.2, 0.65, 1000,  "", "", "", "_")

        var_app.driver.find_element(By.XPATH, var_app.detail_vehicle_fuel_chart_filter).click()
        time.sleep(2.5)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Báo cáo quá tốc độ",
                                              var_app.check_report_filter, "BỘ LỌC TÌM KIẾM", "_TrangChu_BieuDoNhienLieu_BoLoc.png")

        var_app.driver.implicitly_wait(0.3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.report_filter_x).click()
            time.sleep(1)
        except:
            pass
        general.report_back(self)


    def fuel_chart_check_info(self, code, eventname, result, path_check, name_image):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.fuel_chart_chart).click()
            time.sleep(2)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.fuel_chart_km1)
        except:
            report.detail_vehicle_fuel_chart_search(self, "", "", "")
            var_app.driver.find_element(By.XPATH, var_app.fuel_chart_chart).click()
            time.sleep(2)

        module_other_app.write_result_text_try_if_other(code, eventname, result, "Trang chủ - Biểu đồ nhiên liệu",
                                                    path_check, "", name_image)











    def fuel_consumption_report_search(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.check_fuel_consumption_report)
        except:
            homepage_app.move_module(self, "", "", "", var_app.fuel_consumption_report, 0.8, 0.65, 0.2, 0.65, 1000,  "", "", "", "_")

        general.select_vehicle(self, var_app.report_select_vehicle, var_app.report_icon_search,
                               var_app.check_report_search, "STT")

        try:
            wait = WebDriverWait(var_app.driver, 30)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_app.check_report_search)))
        except:
            pass

        module_other_app.write_result_text_try_if_other(code, eventname, result, "Trang chủ - Báo cáo tiêu hao nhiên liệu",
                                              var_app.check_report_search1, "", "_TrangChu_BaoCaoTieuHaoNhienLieu_ChonPhuongTien.png")

    def fuel_consumption_report_type(self, code, eventname, result, button, path_check, path_module, path_image):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.STT)
        except:
            report.fuel_consumption_report_search(self, "", "", "")

        var_app.driver.find_element(By.XPATH, button).click()
        time.sleep(1)
        var_app.driver.find_element(By.XPATH, var_app.report_icon_search).click()
        time.sleep(2.5)
        module_other_app.write_result_displayed_try(code, eventname, result, path_module,
                                                path_check, path_image)

    def fuel_consumption_report_bapgs(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.check_fuel_consumption_report)
        except:
            homepage_app.move_module(self, "", "", "", var_app.fuel_consumption_report, 0.8, 0.65, 0.2, 0.65, 1000,  "", "", "", "_")

        var_app.driver.find_element(By.XPATH, var_app.report_icon_gps).click()
        time.sleep(2.5)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Báo cáo tiêu hao nhiên liệu",
                                              var_app.check_report_icon_gps, "BA GPS", "_TrangChu_BaoCaoTieuHaoNhienLieu_BaGps.png")

        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.IGREE).click()
            time.sleep(1)
        except:
            pass

    def fuel_consumption_report_setting(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.check_fuel_consumption_report)
        except:
            homepage_app.move_module(self, "", "", "", var_app.fuel_consumption_report, 0.8, 0.65, 0.2, 0.65, 1000,  "", "", "", "_")

        var_app.driver.find_element(By.XPATH, var_app.report_setting2).click()
        time.sleep(2.5)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Báo cáo tiêu hao nhiên liệu",
                                              var_app.check_report_setting, "Cài đặt ẩn hiện thông tin", "_TrangChu_BaoCaoTieuHaoNhienLieu_CaiDat.png")

        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.cancel1).click()
            time.sleep(1)
        except:
            pass

    def fuel_consumption_report_excel(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.check_report_search)
        except:
            report.fuel_consumption_report_search(self, "", "", "")

        var_app.driver.find_element(By.XPATH, var_app.fuel_consumption_report_excel).click()
        time.sleep(2.5)

        module_other_app.write_result_not_displayed_try(code, eventname, result, "Trang chủ - Báo cáo tiêu hao nhiên liệu",
                                              var_app.check_export_excel, "_TrangChu_BaoCaoTieuHaoNhienLieu_XuatExcel.png")
        general.back_excel(self, 4, var_app.check_fuel_consumption_report)

    def fuel_consumption_report_detail(self, code, eventname, result, path_check, path_check1, number_from, number_to, desire, path_image):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.STT)
        except:
            report.fuel_consumption_report_search(self, "", "", "")

        try:
            var_app.driver.find_element(By.XPATH, path_check)
            module_other_app.write_result_text_try_if_cut(code, eventname, result, "Trang chủ - Báo cáo tiêu hao nhiên liệu",
                                                  path_check, number_from, number_to, desire, path_image)
        except:
            module_other_app.write_result_text_try_if_cut(code, eventname, result, "Trang chủ - Báo cáo tiêu hao nhiên liệu",
                                                  path_check1, number_from, number_to, desire, path_image)

    def fuel_consumption_report_column(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
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
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Tổng Km GPS")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Thời gian bật máy (phút)")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Thời gian lăn bánh (phút)")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Thời gian dừng đỗ nổ máy (phút)")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Số lần đổ")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Số lần hút")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Số lít đổ")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Số lít hút")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Số lít đầu ngày")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Số lít tồn")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Số lít tiêu hao")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Định mức quy định")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Định mức thực tế theo km")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Định mức thực tế theo bật máy")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Xem biểu đồ")

        general.report_back(self)

    def fuel_consumption_report_see_detail(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.check_fuel_consumption_report)
            var_app.driver.find_element(By.XPATH, var_app.STT)
        except:
            report.fuel_consumption_report_search(self, "", "", "")

        try:
            var_app.driver.find_element(By.XPATH, var_app.data2_column3).click()
        except:
            module_other_app.tap_scaled(var_app.driver, [(630, 1071)])
            time.sleep(2.5)
            module_other_app.tap_scaled(var_app.driver, [(627, 1156)])
        time.sleep(2.5)

        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Báo cáo tiêu hao nhiên liệu",
                                              var_app.info_detail, "THÔNG TIN CHI TIẾT", "_BaoCaoTieuHaoNhienLieu_XemChiTiet.png")

    def fuel_consumption_report_check_detail(self, code, eventname, result, type_check, path_name, path_name1, path_detail, path_detail1, desire, name_image):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.info_detail)
        except:
            report.fuel_consumption_report_see_detail(self, "", "", "")

        var_app.logging.info("--------------")
        var_app.logging.info("Trang chủ - Báo cáo tiêu hao nhiên liệu")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)

        try:
            var_app.driver.find_element(By.XPATH, path_name)
            if type_check == "0":
                try:
                    name = var_app.driver.find_element(By.XPATH, path_name).text
                    detail = var_app.driver.find_element(By.XPATH, path_detail).text
                    module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, "{}: {}".format(name, detail))
                    var_app.logging.info(name)
                    var_app.logging.info(detail)

                    if (name == desire) and (detail != ""):
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

            if type_check == "1":
                try:
                    name = var_app.driver.find_element(By.XPATH, path_name).text
                    detail = var_app.driver.find_element(By.XPATH, path_detail).text
                    module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, "{}: {}".format(name, detail))
                    var_app.logging.info(name)
                    var_app.logging.info(detail)
                    if (name == desire) and (detail != ""):
                        var_app.logging.info("True")
                        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Pass")
                except:
                    pass
        except:
            if type_check == "0":
                try:
                    name = var_app.driver.find_element(By.XPATH, path_name1).text
                    detail = var_app.driver.find_element(By.XPATH, path_detail1).text
                    module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6,
                                               "{}: {}".format(name, detail))
                    var_app.logging.info(name)
                    var_app.logging.info(detail)

                    if (name == desire) and (detail != ""):
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

            if type_check == "1":
                try:
                    name = var_app.driver.find_element(By.XPATH, path_name1).text
                    detail = var_app.driver.find_element(By.XPATH, path_detail1).text
                    module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6,
                                               "{}: {}".format(name, detail))
                    var_app.logging.info(name)
                    var_app.logging.info(detail)
                    if (name == desire) and (detail != ""):
                        var_app.logging.info("True")
                        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Pass")
                except:
                    pass



















    def Comprehensive_fuel_consumption_report_search(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.check_Comprehensive_fuel_consumption_report)
        except:
            homepage_app.move_module(self, "", "", "", var_app.Comprehensive_fuel_consumption_report, 0.8, 0.65, 0.2, 0.65, 1000,  "", "", "", "_")

        general.select_vehicle(self, var_app.report_select_vehicle, var_app.report_icon_search,
                               var_app.check_report_search, "STT")

        try:
            wait = WebDriverWait(var_app.driver, 30)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_app.check_report_search)))
        except:
            pass

        module_other_app.write_result_text_try_if_other(code, eventname, result, "Trang chủ - Báo cáo tổng hợp tiêu hao nhiên liệu",
                                              var_app.check_report_search1, "", "_TrangChu_BaoCaoTongHopTieuHaoNhienLieu_ChonPhuongTien.png")

    def Comprehensive_fuel_consumption_report_type(self, code, eventname, result, button, path_check, path_module, path_image):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.STT)
        except:
            report.Comprehensive_fuel_consumption_report_search(self, "", "", "")

        var_app.driver.find_element(By.XPATH, button).click()
        time.sleep(1)
        var_app.driver.find_element(By.XPATH, var_app.report_icon_search).click()
        time.sleep(2.5)
        module_other_app.write_result_displayed_try(code, eventname, result, path_module,
                                                path_check, path_image)

    def Comprehensive_fuel_consumption_report_bapgs(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.check_Comprehensive_fuel_consumption_report)
        except:
            homepage_app.move_module(self, "", "", "", var_app.Comprehensive_fuel_consumption_report, 0.8, 0.65, 0.2, 0.65, 1000,  "", "", "", "_")

        var_app.driver.find_element(By.XPATH, var_app.report_icon_gps).click()
        time.sleep(2.5)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Báo cáo tổng hợp tiêu hao nhiên liệu",
                                              var_app.check_report_icon_gps, "BA GPS", "_TrangChu_BaoCaoTongHopTieuHaoNhienLieu_BaGps.png")

        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.IGREE).click()
            time.sleep(1)
        except:
            pass

    def Comprehensive_fuel_consumption_report_setting(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.check_Comprehensive_fuel_consumption_report)
        except:
            homepage_app.move_module(self, "", "", "", var_app.Comprehensive_fuel_consumption_report, 0.8, 0.65, 0.2, 0.65, 1000,  "", "", "", "_")

        var_app.driver.find_element(By.XPATH, var_app.report_setting2).click()
        time.sleep(2.5)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Báo cáo tồng hợp tiêu hao nhiên liệu",
                                              var_app.check_report_setting, "Cài đặt ẩn hiện thông tin", "_TrangChu_BaoCaoTongHopTieuHaoNhienLieu_CaiDat.png")

        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.cancel1).click()
            time.sleep(1)
        except:
            pass

    def Comprehensive_fuel_consumption_report_excel(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.check_report_search)
        except:
            report.Comprehensive_fuel_consumption_report_search(self, "", "", "")

        var_app.driver.find_element(By.XPATH, var_app.Comprehensive_fuel_consumption_report_excel).click()
        time.sleep(2.5)
        module_other_app.write_result_not_displayed_try(code, eventname, result, "Trang chủ - Báo cáo tồng hợp tiêu hao nhiên liệu",
                                              var_app.check_export_excel, "_TrangChu_BaoCaoTongHopTieuHaoNhienLieu_XuatExcel.png")
        general.back_excel(self, 4, var_app.check_Comprehensive_fuel_consumption_report)

    def Comprehensive_fuel_consumption_report_detail(self, code, eventname, result, path_check, path_check1, number_from, number_to, desire, path_image):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.STT)
        except:
            report.Comprehensive_fuel_consumption_report_search(self, "", "", "")

        try:
            var_app.driver.find_element(By.XPATH, path_check)
            module_other_app.write_result_text_try_if_cut(code, eventname, result, "Trang chủ - Báo cáo tồng hợp tiêu hao nhiên liệu",
                                                  path_check, number_from, number_to, desire, path_image)
        except:
            module_other_app.write_result_text_try_if_cut(code, eventname, result, "Trang chủ - Báo cáo tồng hợp tiêu hao nhiên liệu",
                                                  path_check1, number_from, number_to, desire, path_image)

    def Comprehensive_fuel_consumption_report_column(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
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
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Số lít đầu ngày")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Số lít đổ")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Số lít hút")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Số lít tồn")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Số lần đổ")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Số lần hút")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Số lít tiêu hao")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Tổng Km GPS")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Thời gian bật máy (phút)")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Thời gian lăn bánh (phút)")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Thời gian dừng đỗ nổ máy (phút)")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Định mức quy định")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Định mức thực tế theo km")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Định mức thực tế theo bật máy")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Chi tiết")

        general.report_back(self)

    def Comprehensive_fuel_consumption_report_see_detail(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.check_Comprehensive_fuel_consumption_report)
            var_app.driver.find_element(By.XPATH, var_app.STT)
        except:
            report.Comprehensive_fuel_consumption_report_search(self, "", "", "")

        try:
            var_app.driver.find_element(By.XPATH, var_app.data2_column2).click()
        except:
            module_other_app.tap_scaled(var_app.driver, [(300, 1074)])
            time.sleep(2.5)
            module_other_app.tap_scaled(var_app.driver, [(300, 1150)])
        time.sleep(2.5)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Báo cáo tồng hợp tiêu hao nhiên liệu",
                                              var_app.info_detail, "THÔNG TIN CHI TIẾT", "_BaoCaoTongHopTieuHaoNhienLieu_XemChiTiet.png")

    def Comprehensive_fuel_consumption_report_check_detail(self, code, eventname, result, type_check, path_name, path_name1, path_detail, path_detail1, desire, name_image):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(0.3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.info_detail)
        except:
            report.Comprehensive_fuel_consumption_report_see_detail(self, "", "", "")

        var_app.logging.info("--------------")
        var_app.logging.info("Trang chủ - Báo cáo tồng hợp tiêu hao nhiên liệu")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)

        try:
            var_app.driver.find_element(By.XPATH, path_name)
            if type_check == "0":
                try:
                    name = var_app.driver.find_element(By.XPATH, path_name).text
                    detail = var_app.driver.find_element(By.XPATH, path_detail).text
                    module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, "{}: {}".format(name, detail))
                    var_app.logging.info(name)
                    var_app.logging.info(detail)

                    if (name == desire) and (detail != ""):
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

            if type_check == "1":
                try:
                    name = var_app.driver.find_element(By.XPATH, path_name).text
                    detail = var_app.driver.find_element(By.XPATH, path_detail).text
                    module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, "{}: {}".format(name, detail))
                    var_app.logging.info(name)
                    var_app.logging.info(detail)
                    if (name == desire) and (detail != ""):
                        var_app.logging.info("True")
                        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Pass")
                except:
                    pass
        except:
            if type_check == "0":
                try:
                    name = var_app.driver.find_element(By.XPATH, path_name1).text
                    detail = var_app.driver.find_element(By.XPATH, path_detail1).text
                    module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6,
                                               "{}: {}".format(name, detail))
                    var_app.logging.info(name)
                    var_app.logging.info(detail)

                    if (name == desire) and (detail != ""):
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

            if type_check == "1":
                try:
                    name = var_app.driver.find_element(By.XPATH, path_name1).text
                    detail = var_app.driver.find_element(By.XPATH, path_detail1).text
                    module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6,
                                               "{}: {}".format(name, detail))
                    var_app.logging.info(name)
                    var_app.logging.info(detail)
                    if (name == desire) and (detail != ""):
                        var_app.logging.info("True")
                        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Pass")
                except:
                    pass












    def vehicle_speed_search(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.check_vehicle_speed)
        except:
            homepage_app.move_module(self, "", "", "", var_app.vehicle_speed, 0.8, 0.65, 0.2, 0.65, 1000,  "", "", "", "")

        general.select_vehicle2(self, var_app.report_select_vehicle, var_app.report_icon_search,
                               var_app.check_report_search, "STT")

        try:
            wait = WebDriverWait(var_app.driver, 30)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_app.check_report_search)))
        except:
            pass

        module_other_app.write_result_text_try_if_other(code, eventname, result, "Trang chủ - Tốc độ của xe",
                                              var_app.check_report_search1, "", "_TrangChu_TocDoCuaXe_ChonPhuongTien.png")


    def vehicle_speed_type(self, code, eventname, result, button, path_check, path_module, path_image):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.check_vehicle_speed)
        except:
            report.vehicle_speed_search(self, "", "", "")


        var_app.driver.find_element(By.XPATH, button).click()
        time.sleep(1)
        var_app.driver.find_element(By.XPATH, var_app.report_icon_search).click()
        time.sleep(3)
        try:
            checkdata = var_app.driver.find_element(By.XPATH, var_app.check_vehicle_speed_type).text
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, checkdata)
        except:
            pass
        module_other_app.write_result_displayed_try(code, eventname, result, path_module,
                                                path_check, path_image)


    def vehicle_speed_setting(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.check_vehicle_speed)
        except:
            homepage_app.move_module(self, "", "", "", var_app.vehicle_speed, 0.8, 0.65, 0.2, 0.65, 1000,  "", "", "", "_")

        var_app.driver.find_element(By.XPATH, var_app.report_setting1).click()
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
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.cancel1).click()
            time.sleep(1)
        except:
            pass


    def vehicle_speed_filter(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.check_vehicle_speed)
        except:
            homepage_app.move_module(self, "", "", "", var_app.vehicle_speed, 0.8, 0.65, 0.2, 0.65, 1000,  "", "", "", "_")

        var_app.driver.find_element(By.XPATH, var_app.report_filter1).click()
        time.sleep(2.5)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Tốc độ của xe",
                                              var_app.check_report_filter, "BỘ LỌC TÌM KIẾM", "_TrangChu_TocDoCuaXe_BoLoc.png")

        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.report_filter_x).click()
            time.sleep(1)
        except:
            pass


    def vehicle_speed_excel(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.check_vehicle_speed)
            var_app.driver.find_element(By.XPATH, var_app.STT)
        except:
            report.vehicle_speed_search(self, "", "", "")

        var_app.driver.find_element(By.XPATH, var_app.vehicle_speed_excel).click()
        time.sleep(2.5)
        module_other_app.write_result_not_displayed_try(code, eventname, result, "Trang chủ - Tốc độ của xe",
                                              var_app.check_export_excel, "_TrangChu_TocDoCuaXe_XuatExcel.png")
        general.back_excel(self, 4, var_app.check_vehicle_speed)


    def vehicle_speed_column(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
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






    def temperature_report(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        homepage_app.move_module1(self, code, eventname, result, var_app.temperature_report, 0.8, 0.65, 0.2, 0.65, 1000,
                                 "Trang chủ - Báo cáo Nhiệt độ", var_app.check_temperature_report,
                                 "BÁO CÁO NHIỆT ĐỘ", "_TrangChu_BaoCaoNhietDo.png", "TRẦN QUANG TRƯỜNG PQA", var_app.data['login']['binhanh_tk'], var_app.data['login']['binhanh_mk'])



    def temperature_chart(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)

        homepage_app.move_module1(self, code, eventname, result, var_app.temperature_chart, 0.8, 0.65, 0.2, 0.65, 1000,
                                 "Trang chủ - Biểu đồ Nhiệt độ", var_app.check_temperature_chart,
                                 "BIỂU ĐỒ NHIỆT ĐỘ", "_TrangChu_BieuDoNhietDo.png", "TRẦN QUANG TRƯỜNG PQA", var_app.data['login']['binhanh_tk'], var_app.data['login']['binhanh_mk'])












    def continuous_driving_detailed_reports_filter(self, code, eventname, result, type_report, desire, path_image):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.check_continuous_driving_detailed_reports)
        except:
            homepage_app.move_module(self, "", "", "", var_app.continuous_driving_detailed_reports, 0.8, 0.65, 0.2, 0.65, 1000, "", "", "", "")


        var_app.driver.find_element(By.XPATH, var_app.report_filter).click()
        time.sleep(2)
        var_app.driver.find_element(By.XPATH, var_app.filter_type_report).click()
        time.sleep(2)
        var_app.driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup//*[@text='"+type_report+"']").click()
        time.sleep(2)
        var_app.driver.find_element(By.XPATH, var_app.APPLY).click()
        time.sleep(3)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Báo cáo chi tiết cuốc lái xe liên tục",
                                                var_app.check_continuous_driving_detailed_reports_filter, desire, path_image)


    def continuous_driving_detailed_reports_filter1(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.check_continuous_driving_detailed_reports)
        except:
            homepage_app.move_module(self, "", "", "", var_app.continuous_driving_detailed_reports, 0.8, 0.65, 0.2, 0.65, 1000, "", "", "", "")

        var_app.driver.find_element(By.XPATH, var_app.report_filter1).click()
        time.sleep(2.5)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Báo cáo chi tiết cuốc lái xe liên tục",
                                              var_app.check_report_filter, "BỘ LỌC TÌM KIẾM", "_BaoCaoChiTietCacCuocLaiXeLienTuc_BoLoc.png")

        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.report_filter_x).click()
            time.sleep(1)
        except:
            pass


    def continuous_driving_detailed_reports_drive_search(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.check_continuous_driving_detailed_reports)
        except:
            # report.continuous_driving_detailed_reports_filter(self, "", "", "", "Lái xe", "", "")
            homepage_app.move_module(self, "", "", "", var_app.continuous_driving_detailed_reports, 0.8, 0.65, 0.2, 0.65, 1000, "", "", "", "")




        general.select_vehicle7(self, var_app.report_select_vehicle6, var_app.report_icon_search6,
                               var_app.check_report_search)

        try:
            wait = WebDriverWait(var_app.driver, 10)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_app.STT)))
        except:
            pass

        module_other_app.write_result_text_try_if_other(code, eventname, result, "Trang chủ - Báo cáo chi tiết cuốc lái xe liên tục(lái xe)",
                                              var_app.check_report_search6, "", "_BaoCaoChiTietCacCuocLaiXeLienTuc_ChonLaiXe.png")


    def continuous_driving_detailed_reports_type(self, code, eventname, result, button, type_check, path_image):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.STT)
        except:
            report.continuous_driving_detailed_reports_drive_search(self, "", "", "")


        var_app.driver.find_element(By.XPATH, button).click()
        time.sleep(1)
        var_app.driver.find_element(By.XPATH, var_app.report_icon_search).click()
        time.sleep(3)
        if type_check == "0":
            module_other_app.write_result_displayed_try(code, eventname, result, "Trang chủ - Báo cáo chi tiết cuốc lái xe liên tục(lái xe)",
                                                    var_app.check_report_other, path_image)

        if type_check == "1":
            module_other_app.write_result_text_try_if_other(code, eventname, result, "Trang chủ - Báo cáo chi tiết cuốc lái xe liên tục(lái xe)",
                                                    var_app.report_filed1, "", path_image)


    def continuous_driving_detailed_reports_setting(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.check_continuous_driving_detailed_reports)
        except:
            homepage_app.move_module(self, "", "", "", var_app.continuous_driving_detailed_reports, 0.8, 0.65, 0.2, 0.65, 1000, "", "", "", "")



        var_app.driver.find_element(By.XPATH, var_app.report_setting1).click()
        time.sleep(2.5)

        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Báo cáo chi tiết cuốc lái xe liên tục",
                                              var_app.check_report_setting, "Cài đặt ẩn hiện thông tin", "_BaoCaoChiTietCacCuocLaiXeLienTuc_CaiDat.png")

        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.cancel1).click()
            time.sleep(1)
        except:
            pass


    def continuous_driving_detailed_reports_excel(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.STT)
        except:
            report.continuous_driving_detailed_reports_drive_search(self, "", "", "")



        var_app.driver.find_element(By.XPATH, var_app.continuous_driving_detailed_reports_excel).click()
        time.sleep(2.5)
        module_other_app.write_result_not_displayed_try(code, eventname, result, "Trang chủ - Báo cáo chi tiết cuốc lái xe liên tục(lái xe)",
                                              var_app.check_export_excel, "_BaoCaoChiTietCacCuocLaiXeLienTuc_XuatExcel.png")

        general.back_excel(self, 4, var_app.check_continuous_driving_detailed_reports)


    def continuous_driving_detailed_reports_report_detail(self, code, eventname, result, path_check, path_check1, number_from, number_to, desire, path_image):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.STT)
        except:
            report.continuous_driving_detailed_reports_drive_search(self, "", "", "")

        try:
            var_app.driver.find_element(By.XPATH, path_check)
            module_other_app.write_result_text_try_if_cut(code, eventname, result, "Trang chủ - Báo cáo chi tiết cuốc lái xe liên tục(lái xe)",
                                                  path_check, number_from, number_to, desire, path_image)
        except:
            module_other_app.write_result_text_try_if_cut(code, eventname, result, "Trang chủ - Báo cáo chi tiết cuốc lái xe liên tục(lái xe)",
                                                  path_check1, number_from, number_to, desire, path_image)


    def continuous_driving_detailed_reports_column(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)

        general.report_back(self)
        report.continuous_driving_detailed_reports_drive_search(self, "", "", "")
        var_app.logging.info("--------------")
        var_app.logging.info("Trang chủ - Báo cáo chi tiết cuốc lái xe liên tục")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)

        general.check_column1(self, code, 825, 1200, 550, 1200, 150, "STT")
        general.check_column(self, code, 825, 1200, 550, 1200, 150, "Biển kiểm soát")
        general.check_column(self, code, 825, 1200, 550, 1200, 150, "Ngày")
        general.check_column(self, code, 825, 1200, 550, 1200, 150, "Thời gian bắt đầu")
        general.check_column(self, code, 825, 1200, 550, 1200, 150, "Thời gian kết thúc")
        general.check_column(self, code, 825, 1200, 550, 1200, 150, "Tổng thời gian")
        general.check_column(self, code, 825, 1200, 550, 1200, 150, "Tọa độ bắt đầu")
        general.check_column(self, code, 825, 1200, 550, 1200, 150, "Tọa độ kết thúc")
        general.check_column(self, code, 825, 1200, 550, 1200, 150, "Địa điểm bắt đầu")
        general.check_column(self, code, 825, 1200, 550, 1200, 150, "Địa điểm kết thúc")
        general.check_column(self, code, 825, 1200, 550, 1200, 150, "Quãng đường")
        general.report_back(self)












    def driving_details_for_the_day_filter(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.check_driving_details_for_the_day)
        except:
            homepage_app.move_module(self, "", "", "", var_app.driving_details_for_the_day, 0.8, 0.65, 0.2, 0.65, 1000, "", "", "", "")

        var_app.driver.find_element(By.XPATH, var_app.report_filter2).click()
        time.sleep(2.5)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Chi tiết cuốc lái xe trong ngày",
                                              var_app.check_report_filter, "BỘ LỌC TÌM KIẾM", "_ChiTietCuocLaiXeTrongNgay_BoLoc.png")

        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.report_filter_x).click()
            time.sleep(1)
        except:
            pass


    def driving_details_for_the_day_search(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.check_driving_details_for_the_day)
        except:
            homepage_app.move_module(self, "", "", "", var_app.driving_details_for_the_day, 0.8, 0.65, 0.2, 0.65, 1000, "", "", "", "")


        general.select_vehicle5(self, var_app.report_select_vehicle1, var_app.report_select_vehicle2, var_app.report_icon_search2, var_app.report_icon_search3,
                               var_app.check_report_search, "STT")

        try:
            wait = WebDriverWait(var_app.driver, 30)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_app.check_report_search)))
        except:
            pass


        module_other_app.write_result_text_try_if_other(code, eventname, result, "Trang chủ - Chi tiết cuốc lái xe trong ngày",
                                              var_app.check_report_search2, "", "_ChiTietCuocLaiXeTrongNgay_ChonLaiXe.png")


    def driving_details_for_the_day_type(self, code, eventname, result, button, type_check, path_image):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.STT)
        except:
            report.driving_details_for_the_day_search(self, "", "", "")


        var_app.driver.find_element(By.XPATH, button).click()
        time.sleep(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.report_icon_search2).click()
        except:
            var_app.driver.find_element(By.XPATH, var_app.report_icon_search3).click()
        time.sleep(3)

        try:
            wait = WebDriverWait(var_app.driver, 30)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_app.check_driving_details_for_the_day1)))
        except:
            pass


        if type_check == "0":
            module_other_app.write_result_displayed_try(code, eventname, result, "Trang chủ - Chi tiết cuốc lái xe trong ngày",
                                                    var_app.check_report_other1, path_image)

        if type_check == "1":
            module_other_app.write_result_text_try_if_other(code, eventname, result, "Trang chủ - Chi tiết cuốc lái xe trong ngày",
                                                    var_app.report_filed1, "", path_image)

        if type_check == "2":
            try:
                var_app.driver.find_element(By.XPATH, var_app.no_data)
                module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Chi tiết cuốc lái xe trong ngày",
                                                            var_app.no_data, "Không có dữ liệu", path_image)
            except:
                module_other_app.write_result_text_try_if_other(code, eventname, result, "Trang chủ - Chi tiết cuốc lái xe trong ngày",
                                                                var_app.report_filed1, "", path_image)




    def driving_details_for_the_day_setting(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.check_driving_details_for_the_day)
        except:
            homepage_app.move_module(self, "", "", "", var_app.driving_details_for_the_day, 0.8, 0.65, 0.2, 0.65, 1000, "", "", "", "")


        var_app.driver.find_element(By.XPATH, var_app.report_setting1).click()
        time.sleep(2.5)

        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Chi tiết cuốc lái xe trong ngày",
                                              var_app.check_report_setting, "Cài đặt ẩn hiện thông tin", "_ChiTietCuocLaiXeTrongNgay_CaiDat.png")

        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.cancel1).click()
            time.sleep(1)
        except:
            pass


    def driving_details_for_the_day_excel(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.STT)
        except:
            report.driving_details_for_the_day_search(self, "", "", "")



        var_app.driver.find_element(By.XPATH, var_app.driving_details_for_the_day_excel).click()
        time.sleep(2.5)
        module_other_app.write_result_not_displayed_try(code, eventname, result, "Trang chủ - Chi tiết cuốc lái xe trong ngày",
                                              var_app.check_export_excel, "_ChiTietCuocLaiXeTrongNgay_XuatExcel.png")

        general.back_excel(self, 4, var_app.check_driving_details_for_the_day)


    def driving_details_for_the_day_detail(self, code, eventname, result, path_check, path_check1, number_from, number_to, desire, path_image):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.STT)
        except:
            report.driving_details_for_the_day_search(self, "", "", "")

        try:
            var_app.driver.find_element(By.XPATH, path_check)
            module_other_app.write_result_text_try_if_cut(code, eventname, result, "Trang chủ - Chi tiết cuốc lái xe trong ngày",
                                                  path_check, number_from, number_to, desire, path_image)
        except:
            module_other_app.write_result_text_try_if_cut(code, eventname, result, "Trang chủ - Chi tiết cuốc lái xe trong ngày",
                                                  path_check1, number_from, number_to, desire, path_image)


    def driving_details_for_the_day_column(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)

        general.report_back(self)
        report.driving_details_for_the_day_search(self, "", "", "")
        var_app.logging.info("--------------")
        var_app.logging.info("Trang chủ - Chi tiết cuốc lái xe trong ngày")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)

        print("STT")
        general.check_column1(self, code, 825, 1200, 650, 1200, 150, "STT")
        print("Ngày")

        try:
            var_app.driver.find_element(By.XPATH, "//*[@text='Ngày']")
        except:
            general.report_back(self)
            report.driving_details_for_the_day_search(self, "", "", "")
        general.check_column1(self, code, 825, 1200, 650, 1200, 150, "Ngày")
        # general.check_column1(self, code, 825, 1200, 650, 1200, 150, "Biển kiểm soát")    #filer phương tiện mới hiện trường này
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Thời gian bắt đầu")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Thời gian kết thúc")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Tổng thời gian")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Thời gian còn lại")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Tọa độ bắt đầu")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Tọa độ kết thúc")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Địa điểm bắt đầu")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Địa điểm kết thúc")
        general.report_back(self)












    def continuous_driving_detailed_reports_vehicle_search(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.check_continuous_driving_detailed_reports)
        except:
            report.continuous_driving_detailed_reports_filter(self, "", "", "", "Phương tiện", "", "")



        general.select_vehicle3(self, var_app.report_select_vehicle, var_app.report_icon_search,
                               var_app.check_report_search, "STT")

        wait = WebDriverWait(var_app.driver, 20)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, var_app.report_detail_1)))

        module_other_app.write_result_text_try_if_other(code, eventname, result, "Trang chủ - Báo cáo chi tiết cuốc lái xe liên tục",
                                              var_app.report_detail_1, "", "_BaoCaoChiTietCacCuocLaiXeLienTuc_ChonPhuongTien.png")


    def continuous_driving_detailed_reports_vehicle_type(self, code, eventname, result, button, type_check, path_image):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.STT)
        except:
            report.continuous_driving_detailed_reports_vehicle_search(self, "", "", "")


        var_app.driver.find_element(By.XPATH, button).click()
        time.sleep(1)
        var_app.driver.find_element(By.XPATH, var_app.report_icon_search).click()
        time.sleep(3)
        if type_check == "0":
            module_other_app.write_result_displayed_try(code, eventname, result, "Trang chủ - Báo cáo chi tiết cuốc lái xe liên tục",
                                                    var_app.report_detail_1, path_image)

        if type_check == "1":
            module_other_app.write_result_text_try_if_other(code, eventname, result, "Trang chủ - Báo cáo chi tiết cuốc lái xe liên tục",
                                                    var_app.report_detail_1, "", path_image)


    def continuous_driving_detailed_reports_vehicle_excel(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.report_detail_1)
        except:
            report.continuous_driving_detailed_reports_vehicle_search(self, "", "", "")



        var_app.driver.find_element(By.XPATH, var_app.continuous_driving_detailed_reports_excel).click()
        time.sleep(2.5)
        module_other_app.write_result_not_displayed_try(code, eventname, result, "Trang chủ - Báo cáo chi tiết cuốc lái xe liên tục",
                                              var_app.check_export_excel, "_BaoCaoChiTietCacCuocLaiXeLienTuc_XuatExcel.png")

        general.back_excel(self, 4, var_app.check_continuous_driving_detailed_reports)


    def continuous_driving_detailed_reports_vehicle_detail(self, code, eventname, result, path_check, number_from, number_to, desire, path_image):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.report_filed1)
        except:
            report.continuous_driving_detailed_reports_vehicle_search(self, "", "", "")

        module_other_app.write_result_text_try_if_cut(code, eventname, result, "Trang chủ - Báo cáo chi tiết cuốc lái xe liên tục",
                                              path_check, number_from, number_to, desire, path_image)


    def continuous_driving_detailed_reports_vehicle_column(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)

        general.report_back(self)
        report.continuous_driving_detailed_reports_vehicle_search(self, "", "", "")
        var_app.logging.info("--------------")
        var_app.logging.info("Trang chủ - Báo cáo chi tiết cuốc lái xe liên tục")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)

        general.check_column1(self, code, 825, 1200, 650, 1200, 150, "STT")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Lái xe")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Giấy phép lái xe")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Ngày")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Thời gian bắt đầu")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Thời gian kết thúc")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Tổng thời gian")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Tọa độ bắt đầu")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Tọa độ kết thúc")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Địa điểm bắt đầu")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Địa điểm kết thúc")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Quãng đường")
        general.report_back(self)












    def driving_report_for_the_week_search(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.check_driving_report_for_the_week)
        except:
            homepage_app.move_module(self, "Report201", eventname, result, var_app.driving_report_for_the_week, 0.8, 0.65, 0.2, 0.65, 1000, "", "", "", "")


        general.select_vehicle4(self, var_app.report_select_vehicle, var_app.report_icon_search,
                               var_app.STT)

        try:
            wait = WebDriverWait(var_app.driver, 30)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_app.STT)))
        except:
            pass


        module_other_app.write_result_text_try_if_other(code, eventname, result, "Trang chủ - Báo cáo cuốc lái xe trong tuần",
                                              var_app.check_report_search1, "", "_BaoCaoCacCuocLaiXeTrongTuan_ChonLaiXe.png")


    def driving_report_for_the_week_setting(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.check_driving_report_for_the_week)
        except:
            homepage_app.move_module(self, "Report201", eventname, result, var_app.driving_report_for_the_week, 0.8, 0.65, 0.2, 0.65, 1000, "", "", "", "")


        var_app.driver.find_element(By.XPATH, var_app.report_setting1).click()
        time.sleep(2.5)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Báo cáo cuốc lái xe trong tuần",
                                              var_app.check_report_setting, "Cài đặt ẩn hiện thông tin", "_BaoCaoCacCuocLaiXeTrongTuan_CaiDat.png")

        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.cancel1).click()
            time.sleep(1)
        except:
            pass


    def driving_report_for_the_week_filter(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.check_driving_report_for_the_week)
        except:
            homepage_app.move_module(self, "Report201", eventname, result, var_app.driving_report_for_the_week, 0.8, 0.65, 0.2, 0.65, 1000, "", "", "", "")

        var_app.driver.find_element(By.XPATH, var_app.report_filter1).click()
        time.sleep(2.5)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - Báo cáo cuốc lái xe trong tuần",
                                              var_app.check_report_filter, "BỘ LỌC TÌM KIẾM", "_BaoCaoCacCuocLaiXeTrongTuan_BoLoc.png")

        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.report_filter_x).click()
            time.sleep(1)
        except:
            pass


    def driving_report_for_the_week_excel(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.STT)
        except:
            report.driving_report_for_the_week_search(self, "", "", "")



        var_app.driver.find_element(By.XPATH, var_app.driving_report_for_the_week_excel).click()
        time.sleep(2.5)
        module_other_app.write_result_not_displayed_try(code, eventname, result, "Trang chủ - Báo cáo cuốc lái xe trong tuần",
                                              var_app.check_export_excel, "_BaoCaoCacCuocLaiXeTrongTuan_XuatExcel.png")

        general.back_excel(self, 4, var_app.check_driving_report_for_the_week)


    def driving_report_for_the_week_detail(self, code, eventname, result, path_check, path_check1, number_from, number_to, desire, path_image):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.STT)
        except:
            report.driving_report_for_the_week_search(self, "", "", "")

        try:
            var_app.driver.find_element(By.XPATH, path_check)
            module_other_app.write_result_text_try_if_cut(code, eventname, result, "Trang chủ - Báo cáo cuốc lái xe trong tuần",
                                                  path_check, number_from, number_to, desire, path_image)
        except:
            module_other_app.write_result_text_try_if_cut(code, eventname, result, "Trang chủ - Báo cáo cuốc lái xe trong tuần",
                                                  path_check1, number_from, number_to, desire, path_image)


    def driving_report_for_the_week_column(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)

        general.report_back(self)
        report.driving_report_for_the_week_search(self, "", "", "")
        var_app.logging.info("--------------")
        var_app.logging.info("Trang chủ - Báo cáo cuốc lái xe trong tuần")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)

        general.check_column1(self, code, 825, 1200, 650, 1200, 150, "STT")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Ngày")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Thời gian bắt đầu")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Thời gian kết thúc")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Tổng thời gian")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Tọa độ bắt đầu")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Tọa độ kết thúc")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Địa điểm bắt đầu")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Địa điểm kết thúc")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Quãng đường")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Số ngày hoạt động")
        general.report_back(self)













    def summary_report_of_violations(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        homepage_app.move_module1(self, code, eventname, result, var_app.summary_report_of_violations, 0.8, 0.65, 0.2, 0.65, 1000,
                                 "Trang chủ - B/c Tổng hợp vi phạm", var_app.check_summary_report_of_violations,
                                 "TỔNG HỢP TÌNH HÌNH VI PHẠM THEO ĐƠN VỊ VẬN TẢI", "_TrangChu_BaoCaoTongHopViPham.png",
                                  "PHÙNG VĂN ĐỒNG", var_app.data['login']['vandongqna_tk'], var_app.data['login']['vandongqna_mk'])


    def summary_report_of_violations_search(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.check_summary_report_of_violations)
        except:
            report.summary_report_of_violations(self, "", "", "")

        general.select_vehicle_violet(self, var_app.report_select_vehicle2, var_app.report_icon_search2,
                               var_app.report_detail1e)

        try:
            wait = WebDriverWait(var_app.driver, 30)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_app.check_report_search2)))
        except:
            pass

        module_other_app.write_result_text_try_if_other(code, eventname, result, "Trang chủ - B/c Tổng hợp vi phạm",
                                              var_app.check_report_search2, "", "_TrangChu_BaoCaoTongHopViPham_ChonLaiXe.png")


    def summary_report_of_violations_type(self, code, eventname, result, button, type_check, path_image):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.STT)
        except:
            report.summary_report_of_violations_search(self, "", "", "")

        var_app.driver.find_element(By.XPATH, button).click()
        time.sleep(1.5)
        var_app.driver.find_element(By.XPATH, var_app.report_icon_search2).click()
        time.sleep(3)
        if type_check == "0":
            module_other_app.write_result_displayed_try(code, eventname, result, "Trang chủ - B/c Tổng hợp vi phạm",
                                                    var_app.check_report_other1, path_image)

        if type_check == "1":
            module_other_app.write_result_text_try_if_other(code, eventname, result, "Trang chủ - B/c Tổng hợp vi phạm",
                                                    var_app.report_detail1e, "", path_image)


    def summary_report_of_violations_setting(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.check_summary_report_of_violations)
        except:
            homepage_app.move_module1(self, code, eventname, result, var_app.summary_report_of_violations, 0.8, 0.65, 0.2, 0.65, 1000,
                                      "", "", "", "", "", var_app.data['login']['vandongqna_tk'], var_app.data['login']['vandongqna_mk'])

        var_app.driver.find_element(By.XPATH, var_app.report_setting1).click()
        time.sleep(2.5)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - B/c Tổng hợp vi phạm",
                                              var_app.check_report_setting, "Cài đặt ẩn hiện thông tin", "_TrangChu_BaoCaoTongHopViPham_CaiDat.png")

        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.cancel1).click()
            time.sleep(1)
        except:
            pass


    def summary_report_of_violations_filter(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.check_summary_report_of_violations)
        except:
            homepage_app.move_module1(self, code, eventname, result, var_app.summary_report_of_violations, 0.8, 0.65, 0.2, 0.65, 1000,
                                      "", "", "", "", "", var_app.data['login']['vandongqna_tk'], var_app.data['login']['vandongqna_mk'])


        var_app.driver.find_element(By.XPATH, var_app.report_filter2).click()
        time.sleep(2.5)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - B/c Tổng hợp vi phạm",
                                              var_app.check_report_filter, "BỘ LỌC TÌM KIẾM", "_TrangChu_BaoCaoTongHopViPham_BoLoc.png")

        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.report_filter_x).click()
            time.sleep(1)
        except:
            pass


    def summary_report_of_violations_excel(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.check_report_search)
        except:
            report.summary_report_of_violations_search(self, "", "", "")

        var_app.driver.find_element(By.XPATH, var_app.summary_report_of_violations_excel).click()
        time.sleep(2.5)

        module_other_app.write_result_not_displayed_try(code, eventname, result, "Trang chủ - B/c Tổng hợp vi phạm",
                                              var_app.check_export_excel, "_TrangChu_BaoCaoTongHopViPham_XuatExcel.png")
        general.back_excel(self, 4, var_app.check_summary_report_of_violations)


    def summary_report_of_violations_detail(self, code, eventname, result, path_check, path_check1, number_from, number_to, desire, path_image):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        try:
            var_app.driver.find_element(By.XPATH, var_app.report_7day).click()
            time.sleep(2.5)
            var_app.driver.find_element(By.XPATH, var_app.report_icon_search).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.STT)
        except:
            report.summary_report_of_violations_search(self, "", "", "")

        try:
            var_app.driver.find_element(By.XPATH, path_check)
            module_other_app.write_result_text_try_if_cut_not_fail(code, eventname, result, "Trang chủ - Báo cáo đổ hút nhiên liệu",
                                                  path_check, number_from, number_to, desire, path_image)
        except:
            module_other_app.write_result_text_try_if_cut_not_fail(code, eventname, result, "Trang chủ - Báo cáo đổ hút nhiên liệu",
                                                  path_check1, number_from, number_to, desire, path_image)







    def summary_report_of_violations_column(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        general.report_back(self)
        report.summary_report_of_violations_search(self, "", "", "")
        var_app.logging.info("--------------")
        var_app.logging.info("Trang chủ - B/c Tổng hợp vi phạm")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        try:
            no_data = var_app.driver.find_element(By.XPATH, var_app.no_data).text
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, no_data)
            var_app.logging.info("True")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Pass")
        except:
            general.check_column1(self, code, 825, 1200, 650, 1200, 150, "STT")
            general.check_column(self, code, 825, 1200, 650, 1200, 150, "Tổng km")
            general.check_column(self, code, 825, 1200, 650, 1200, 150, "Tỷ lệ quá tốc độ 5 km/h - 10 km/h")
            general.check_column(self, code, 825, 1200, 650, 1200, 150, "Tỷ lệ quá tốc độ 10 km/h - 20 km/h")
            general.check_column(self, code, 825, 1200, 650, 1200, 150, "Tỷ lệ quá tốc độ 20 km/h - 35 km/h")
            general.check_column(self, code, 825, 1200, 650, 1200, 150, "Tỷ lệ quá tốc độ trên 35 km/h")
            general.check_column(self, code, 825, 1200, 650, 1200, 150, "Số lần quá tốc độ 5 km/h - 10 km/h")
            general.check_column(self, code, 825, 1200, 650, 1200, 150, "Số lần quá tốc độ 10 km/h - 20 km/h")
            general.check_column(self, code, 825, 1200, 650, 1200, 150, "Số lần quá tốc độ 20 km/h - 35 km/h")
            general.check_column(self, code, 825, 1200, 650, 1200, 150, "Số lần quá tốc độ trên 35 km/h")
            general.check_column(self, code, 825, 1200, 650, 1200, 150, "Số lần lái xe liên tục quá 4 h/ngày")
            general.check_column(self, code, 825, 1200, 650, 1200, 150, "Số lần lái xe quá 10 h/ngày")
            general.check_column(self, code, 825, 1200, 650, 1200, 150, "Số lần lái xe quá 48 h/tuần")
            general.report_back(self)


    def summary_report_of_violations_see_detail(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.check_summary_report_of_violations)
            var_app.driver.find_element(By.XPATH, var_app.report_filed1)
        except:
            general.report_back(self)
            report.summary_report_of_violations_search(self, "", "", "")

        module_other_app.tap_scaled(var_app.driver, [(242, 670)])
        time.sleep(2.5)
        module_other_app.tap_scaled(var_app.driver, [(236, 750)])
        time.sleep(2.5)
        module_other_app.write_result_text_try_if(code, eventname, result, "Trang chủ - B/c Tổng hợp vi phạm",
                                              var_app.info_detail, "THÔNG TIN CHI TIẾT", "_TrangChu_BaoCaoTongHopViPham_XemChiTiet.png")


    def summary_report_of_violations_check_detail(self, code, eventname, result, type_check, path_name, path_name1, path_detail, path_detail1, desire, name_image):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)

        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.info_detail)
        except:
            report.summary_report_of_violations_see_detail(self, "", "", "")

        var_app.logging.info("--------------")
        var_app.logging.info("Trang chủ - B/c Tổng hợp vi phạm")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)

        try:
            var_app.driver.find_element(By.XPATH, path_name)
            if type_check == "0":
                try:
                    name = var_app.driver.find_element(By.XPATH, path_name).text
                    detail = var_app.driver.find_element(By.XPATH, path_detail).text
                    module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, "{}: {}".format(name, detail))
                    var_app.logging.info(name)
                    var_app.logging.info(detail)

                    if (name == desire) and (detail != ""):
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

            if type_check == "1":
                try:
                    name = var_app.driver.find_element(By.XPATH, path_name).text
                    detail = var_app.driver.find_element(By.XPATH, path_detail).text
                    module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, "{}: {}".format(name, detail))
                    var_app.logging.info(name)
                    var_app.logging.info(detail)
                    if (name == desire) and (detail != ""):
                        var_app.logging.info("True")
                        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Pass")
                except:
                    pass
        except:
            if type_check == "0":
                try:
                    name = var_app.driver.find_element(By.XPATH, path_name1).text
                    detail = var_app.driver.find_element(By.XPATH, path_detail1).text
                    module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6,
                                               "{}: {}".format(name, detail))
                    var_app.logging.info(name)
                    var_app.logging.info(detail)

                    if (name == desire) and (detail != ""):
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

            if type_check == "1":
                try:
                    name = var_app.driver.find_element(By.XPATH, path_name1).text
                    detail = var_app.driver.find_element(By.XPATH, path_detail1).text
                    module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6,
                                               "{}: {}".format(name, detail))
                    var_app.logging.info(name)
                    var_app.logging.info(detail)
                    if (name == desire) and (detail != ""):
                        var_app.logging.info("True")
                        module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Pass")
                except:
                    pass












    def report_over_speeding_on_the_route(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        homepage_app.move_module1(self, code, eventname, result, var_app.report_over_speeding_on_the_route, 0.8, 0.65, 0.2, 0.65, 1000,
                                 "Trang chủ - B/C quá tốc độ theo cung đường", var_app.check_report_over_speeding_on_the_route,
                                 "BÁO CÁO QUÁ TỐC ĐỘ THEO CUNG ĐƯỜNG", "_TrangChu_BaoCaoQuaTocDoTheoCungDuong.png",
                                  "PHÙNG VĂN ĐỒNG", var_app.data['login']['conhom_quantri_tk'], var_app.data['login']['conhom_quantri_mk'])#var_app.data['login']['vandongqna_tk'], var_app.data['login']['vandongqna_mk']


    def report_over_speeding_on_the_route_search(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.check_report_over_speeding_on_the_route)
        except:
            report.report_over_speeding_on_the_route(self, "", "", "")

        # general.select_vehicle_violet(self, var_app.report_select_vehicle, var_app.report_icon_search,
        #                        var_app.STT)

        general.select_vehicle(self, var_app.report_select_vehicle, var_app.report_icon_search,
                               var_app.STT, "STT")



        try:
            wait = WebDriverWait(var_app.driver, 10)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_app.STT)))
        except:
            pass

        module_other_app.write_result_text_try_if_other(code, eventname, result, "Trang chủ - B/C quá tốc độ theo cung đường",
                                              var_app.check_report_search1, "", "_TrangChu_BaoCaoQuaTocDoTheoCungDuong_ChonPhuongTien.png")


    def report_over_speeding_on_the_route_type(self, code, eventname, result, button, type_check, path_image):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.STT)
            var_app.driver.find_element(By.XPATH, var_app.check_report_over_speeding_on_the_route)
        except:
            report.report_over_speeding_on_the_route_search(self, "", "", "")

        var_app.driver.find_element(By.XPATH, button).click()
        time.sleep(1.5)
        var_app.driver.find_element(By.XPATH, var_app.report_icon_search).click()
        time.sleep(3)
        if type_check == "0":
            module_other_app.write_result_displayed_try(code, eventname, result, "Trang chủ - B/C quá tốc độ theo cung đường",
                                                    var_app.check_report_stop_other, path_image)

        if type_check == "1":
            module_other_app.write_result_text_try_if_other(code, eventname, result, "Trang chủ - B/C quá tốc độ theo cung đường",
                                                    var_app.report_detail1, "", path_image)


    def report_over_speeding_on_the_route_setting(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.check_report_over_speeding_on_the_route)
        except:
            homepage_app.move_module1(self, code, eventname, result, var_app.report_over_speeding_on_the_route, 0.8, 0.65, 0.2, 0.65, 1000,
                                      "", "", "", "", "PHÙNG VĂN ĐỒNG", var_app.data['login']['vandongqna_tk'],  var_app.data['login']['vandongqna_mk'])

        var_app.driver.find_element(By.XPATH, var_app.report_setting1).click()
        time.sleep(2.5)
        module_other_app.write_result_text_try_if(code, eventname, result, "BÁO CÁO QUÁ TỐC ĐỘ THEO CUNG ĐƯỜNG",
                                              var_app.check_report_setting, "Cài đặt ẩn hiện thông tin", "_TrangChu_BaoCaoQuaTocDoTheoCungDuong_CaiDat.png")

        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.cancel1).click()
            time.sleep(1)
        except:
            pass


    def report_over_speeding_on_the_route_excel(self, code, eventname, result):
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
                var_app.driver.find_element(By.XPATH, var_app.check_report_over_speeding_on_the_route)
                var_app.driver.find_element(By.XPATH, var_app.check_report_search1)
            except:
                var_app.driver.find_element(By.XPATH, var_app.report_detail_1)

        except:
            report.report_over_speeding_on_the_route_search(self, "", "", "")

        var_app.driver.find_element(By.XPATH, var_app.report_over_speeding_on_the_route_excel).click()
        time.sleep(2.5)

        module_other_app.write_result_not_displayed_try(code, eventname, result, "Trang chủ - B/C quá tốc độ theo cung đường",
                                              var_app.check_export_excel, "_TrangChu_BaoCaoQuaTocDoTheoCungDuong_XuatExcel.png")
        general.back_excel(self, 4, var_app.check_summary_report_of_violations)


    def report_over_speeding_on_the_route_detail(self, code, eventname, result, path_check, path_check1, number_from, number_to, desire, path_image):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        try:
            var_app.driver.find_element(By.XPATH, var_app.report_7day).click()
            time.sleep(2.5)
            var_app.driver.find_element(By.XPATH, var_app.report_icon_search).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.check_report_over_speeding_on_the_route)
            var_app.driver.find_element(By.XPATH, var_app.check_report_search1)
        except:
            report.report_over_speeding_on_the_route_search(self, "", "", "")

        try:
            var_app.driver.find_element(By.XPATH, path_check)
            module_other_app.write_result_text_try_if_cut(code, eventname, result, "Trang chủ - Báo cáo quá tốc độ theo cung đường",
                                                  path_check, number_from, number_to, desire, path_image)
        except:
            module_other_app.write_result_text_try_if_cut(code, eventname, result, "Trang chủ - Báo cáo quá tốc độ theo cung đường",
                                                  path_check1, number_from, number_to, desire, path_image)


    def report_over_speeding_on_the_route_column(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.implicitly_wait(2)
        general.report_back(self)
        report.report_over_speeding_on_the_route_search(self, "", "", "")
        var_app.logging.info("--------------")
        var_app.logging.info("Trang chủ - B/C quá tốc độ theo cung đường")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)

        general.check_column1(self, code, 825, 1200, 650, 1200, 150, "STT")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Phương tiện")
        general.check_column1(self, code, 825, 1200, 650, 1200, 150, "Biển số xe")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Lái xe")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Thời gian bắt đầu")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Thời gian kết thúc")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Thời gian")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Tốc độ cực đại (km/h)")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Tốc độ cho phép (km/h)")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Số lần")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Quãng đường (km)")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Địa điểm bắt đầu")
        general.check_column(self, code, 825, 1200, 650, 1200, 150, "Địa điểm kết thúc")
        general.report_back(self)



