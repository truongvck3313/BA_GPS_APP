import time
from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import homepage_app
import image_video_app
import minitor_app
import report_app
import route
import utilities
import var_app
import module_other_app
from retry import retry
import vehicle














class login:

    @retry(tries=3, delay=2, backoff=1, jitter=5, )
    def login(self, user, password, code, eventname, result, pathcheck, desire, pathimage):
        module_other_app.close_app()

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.find_element(By.XPATH, var_app.login_user1).clear()
        except:
            module_other_app.close_app()
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)

        var_app.driver.find_element(By.XPATH, var_app.login_user1).send_keys(user)

        time.sleep(0.5)
        var_app.driver.find_element(By.XPATH, var_app.login_password1).clear()
        var_app.driver.find_element(By.XPATH, var_app.login_password1).send_keys(password)

        var_app.driver.find_element(by=AppiumBy.XPATH, value=var_app.login_buttonlogin).click()
        time.sleep(2.5)
        other_function.delete_nofitication(self)

        var_app.logging.info("--------------")
        var_app.logging.info("Login với tài khoản: " + user)
        var_app.logging.info("Login với mật khẩu: " + password)
        if code == "Login01" or code == "Login03":
            module_other_app.write_result_text_try_if_conten_other(code, eventname, result, "Màn hình đăng nhập - Login",
                                                  pathcheck, desire, pathimage)

        if code == "Login02":
            module_other_app.write_result_text_try_if(code, eventname, result, "Màn hình đăng nhập - Login",
                                                  pathcheck, desire, pathimage)


        if code == "Login04":
            module_other_app.write_result_not_displayed_try(code, eventname, result, "Màn hình đăng nhập - Login",
                                        var_app.check_minitor, "_DangNhap_TKKhachHangKhongCoQuyenGiamSat.png")


    @retry(tries=2, delay=2, backoff=1, jitter=5, )
    def login_READED(self, user, password, code, eventname, result, pathcheck, desire, pathimage):
        module_other_app.close_app()

        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.find_element(By.XPATH, var_app.login_user1).clear()
        except:
            module_other_app.close_app()
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)

        var_app.driver.find_element(By.XPATH, var_app.login_user1).send_keys(user)

        time.sleep(0.5)
        var_app.driver.find_element(By.XPATH, var_app.login_password1).clear()
        var_app.driver.find_element(By.XPATH, var_app.login_password1).send_keys(password)

        var_app.driver.find_element(by=AppiumBy.XPATH, value=var_app.login_buttonlogin).click()
        time.sleep(5)
        module_other_app.tap_scaled(var_app.driver, [(448, 1235)])
        time.sleep(2)
        module_other_app.tap_scaled(var_app.driver, [(98, 1020)])
        time.sleep(2)
        module_other_app.tap_scaled(var_app.driver, [(95, 580)])
        time.sleep(2)
        module_other_app.tap_scaled(var_app.driver, [(95, 580)])
        time.sleep(2)
        module_other_app.tap_scaled(var_app.driver, [(267, 1575)])
        time.sleep(2)
        try:
            var_app.driver.find_element(By.XPATH, var_app.minitor).click()
            time.sleep(2)
        except:
            pass
        other_function.delete_nofitication(self)

        var_app.logging.info("--------------")
        var_app.logging.info("Login với tài khoản: " + user)
        var_app.logging.info("Login với mật khẩu: " + password)
        if code == "Login01" or code == "Login03":
            module_other_app.write_result_text_try_if_conten_other(code, eventname, result, "Màn hình đăng nhập - Login",
                                                  pathcheck, desire, pathimage)

        if code == "Login02":
            module_other_app.write_result_text_try_if(code, eventname, result, "Màn hình đăng nhập - Login",
                                                  pathcheck, desire, pathimage)


        if code == "Login04":
            module_other_app.write_result_not_displayed_try(code, eventname, result, "Màn hình đăng nhập - Login",
                                        var_app.check_minitor, "_DangNhap_TKKhachHangKhongCoQuyenGiamSat.png")


    def login_wrong(self, user, password, code, eventname, result):
        var_app.driver.implicitly_wait(2)
        module_other_app.close_app()


        var_app.driver.find_element(By.XPATH, var_app.login_user1).clear()
        var_app.driver.find_element(By.XPATH, var_app.login_user1).send_keys(user)

        time.sleep(0.5)
        var_app.driver.find_element(By.XPATH, var_app.login_password1).clear()
        var_app.driver.find_element(By.XPATH, var_app.login_password1).send_keys(password)

        var_app.driver.find_element(by=AppiumBy.XPATH, value=var_app.login_buttonlogin).click()
        time.sleep(2.5)
        var_app.logging.info("--------------")
        var_app.logging.info("Login với tài khoản: " + user)
        var_app.logging.info("Login với mật khẩu: " + password)
        module_other_app.write_result_text_try_if(code, eventname, result, "Màn hình đăng nhập - Login",
                                              var_app.check_wronglogin, "Tài khoản hoặc mật khẩu không chính xác. Vui lòng kiểm tra lại", "_DangNhap_TKDungMatKhauSai.png")

        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.login_iconx).click()
            time.sleep(1)
        except:
            pass



    def forger_user(self, code, eventname, result):
        try:
            var_app.driver.implicitly_wait(0.2)
            var_app.driver.find_element(By.XPATH, var_app.login_user1)
        except:
            module_other_app.close_app()

        var_app.driver.implicitly_wait(2)
        var_app.driver.find_element(By.XPATH, var_app.login_user1).clear()
        var_app.driver.find_element(By.XPATH, var_app.login_user1).send_keys(var_app.data['login']['taikhoansai_user'])

        time.sleep(0.5)
        var_app.driver.find_element(By.XPATH, var_app.login_password1).clear()
        var_app.driver.find_element(By.XPATH, var_app.login_password1).send_keys(var_app.data['login']['taikhoansai_password'])

        var_app.driver.find_element(by=AppiumBy.XPATH, value=var_app.login_buttonlogin).click()
        time.sleep(3)
        var_app.driver.find_element(by=AppiumBy.XPATH, value=var_app.forger_user).click()
        time.sleep(1)
        var_app.logging.info("--------------")
        var_app.logging.info("Login với tài khoản: " + var_app.data['login']['taikhoansai_user'])
        var_app.logging.info("Login với mật khẩu: " + var_app.data['login']['taikhoansai_password'])
        module_other_app.write_result_text_try_if(code, eventname, result, "Màn hình đăng nhập - Login",
                                                  var_app.check_forger_user, "Để đảm bảo an toàn thông tin, Quý khách vui lòng liên hệ 19006464 để được cấp lại mật khẩu", "_DangNhap_QuenTaiKhoan.png")

        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(by=AppiumBy.XPATH, value=var_app.forger_user_skip).click()
            time.sleep(1.3)
        except:
            pass



    def forger_password(self, code, eventname, result):
        var_app.driver.implicitly_wait(2)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.forger_password).click()
        except:
            # login.check_logout(self)
            module_other_app.close_app()
            var_app.driver.find_element(By.XPATH, var_app.forger_password).click()

        time.sleep(1.5)
        var_app.driver.find_element(By.XPATH, var_app.forger_password_inputuser).send_keys(var_app.data['login']['quenmatkhau_user'])
        var_app.driver.find_element(By.XPATH, var_app.forger_password_inputpassword).send_keys(var_app.data['login']['quenmatkhau_sdt'])
        time.sleep(0.5)
        var_app.driver.find_element(By.XPATH, var_app.forger_password_sendcode).click()
        time.sleep(2.5)
        try:
            var_app.driver.find_element(By.XPATH, var_app.forger_password_sendcode).click()
            time.sleep(2.5)
        except:
            pass

        module_other_app.write_result_text_try_if(code, eventname, result, "Màn hình đăng nhập - Login",
                                                  var_app.check_forger_password, "Xác thực OTP", "_DangNhap_QuenMatKhau.png")

        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.forger_password_iconback).click()
            time.sleep(1)
            var_app.driver.find_element(By.XPATH, var_app.forger_password_iconx).click()
            time.sleep(1)
        except:
            var_app.driver.press_keycode(4)
            time.sleep(1)



    def remember_login_mark(self, code, eventname, result):
        var_app.driver.implicitly_wait(0.3)
        module_other_app.close_app()


        try:
            var_app.driver.find_element(By.XPATH, var_app.last_update).click()
            time.sleep(1)
        except:
            pass

        try:
            var_app.driver.find_element(By.XPATH, var_app.checkbox_remember1)
        except:
            module_other_app.reset_driver()
            module_other_app.open_bagps()
            time.sleep(3)
            login.logout(self)


        var_app.driver.implicitly_wait(2)

        try:
            var_app.driver.find_element(By.XPATH, var_app.checkbox_remember2)
        except:
            var_app.driver.find_element(By.XPATH, var_app.checkbox_remember1).click()

        time.sleep(0.5)
        var_app.driver.find_element(By.XPATH, var_app.login_user1).clear()
        var_app.driver.find_element(By.XPATH, var_app.login_user1).send_keys(var_app.data['login']['khongnhom_quantri_tk'])
        time.sleep(0.5)
        var_app.driver.find_element(By.XPATH, var_app.login_password1).clear()
        var_app.driver.find_element(By.XPATH, var_app.login_password1).send_keys(var_app.data['login']['khongnhom_quantri_mk'])
        var_app.driver.implicitly_wait(2)
        var_app.driver.find_element(by=AppiumBy.XPATH, value=var_app.login_buttonlogin).click()
        time.sleep(3)
        other_function.delete_nofitication(self)

        time.sleep(1)
        module_other_app.reset_driver()

        try:
            module_other_app.open_bagps()
            time.sleep(4)
            other_function.delete_nofitication(self)
        except:
            pass

        module_other_app.write_result_text_try_if(code, eventname, result, "Màn hình đăng nhập - Ghi nhớ đăng nhập",
                                                var_app.remember_login_mark, "Giám sát", "_DangNhap_BoGhiNhoDangNhap.png")
        time.sleep(1)



    def remember_login_not_mark(self, code, eventname, result):
        var_app.driver.implicitly_wait(2)
        other_function.delete_nofitication(self)

        try:
            var_app.driver.implicitly_wait(0.3)
            login.logout(self)
        except:
            pass


        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.checkbox_remember1)
        except:
            module_other_app.reset_driver()
            module_other_app.open_bagps()
            time.sleep(4)
            login.logout(self)

        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.checkbox_remember2)
            var_app.driver.find_element(By.XPATH, var_app.checkbox_remember1).click()
        except:
            pass


        time.sleep(0.5)
        var_app.driver.find_element(By.XPATH, var_app.login_user1).clear()
        var_app.driver.find_element(By.XPATH, var_app.login_user1).send_keys(var_app.data['login']['khongnhom_quantri_tk'])
        time.sleep(0.5)
        var_app.driver.find_element(By.XPATH, var_app.login_password1).clear()
        var_app.driver.find_element(By.XPATH, var_app.login_password1).send_keys(var_app.data['login']['khongnhom_quantri_mk'])
        var_app.driver.implicitly_wait(2)
        var_app.driver.find_element(by=AppiumBy.XPATH, value=var_app.login_buttonlogin).click()
        time.sleep(3)

        other_function.delete_nofitication(self)
        time.sleep(1)
        var_app.driver.press_keycode(4)
        time.sleep(0.5)
        var_app.driver.press_keycode(4)
        time.sleep(0.5)
        var_app.driver.press_keycode(4)
        time.sleep(0.5)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
            try:
                var_app.driver.find_element(By.XPATH, var_app.last_update).click()
                time.sleep(1)
            except:
                pass
            other_function.delete_nofitication(self)
        except:
            pass

        var_app.driver.implicitly_wait(1)
        try:
            module_other_app.close_app()
        except:
            pass

        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        var_app.driver.find_element(By.XPATH, var_app.login_buttonlogin)

        module_other_app.write_result_text_try_if(code, eventname, result, "Màn hình đăng nhập - Ghi nhớ đăng nhập",
                                                var_app.login_buttonlogin, "ĐĂNG NHẬP", "_DangNhap_BoGhiNhoDangNhap.png")





    def logout(self):
        var_app.driver.implicitly_wait(2)
        other_function.delete_nofitication(self)

        print("đang logout")
        try:
            var_app.driver.find_element(By.XPATH, var_app.account).click()
            time.sleep(1)
            module_other_app.swipe_scaled(var_app.driver, 400, 1200, 465, 480, 500)
            time.sleep(1)
            module_other_app.tap_scaled(var_app.driver, [(200, 1300)])
            time.sleep(1.5)
            var_app.driver.find_element(By.XPATH, var_app.logout).click()
            time.sleep(1.5)
            var_app.driver.find_element(By.XPATH, var_app.logout_all_devices).click()
            time.sleep(2)
        except:
            print("logput thất bại")



    def logout_back(self):
        pass
        # var_app.driver.implicitly_wait(0.1)
        # try:
        #     var_app.driver.find_element(By.XPATH, var_app.bagps).click()
        #     time.sleep(3)
        # except:
        #     pass
        # try:
        #     var_app.driver.find_element(By.XPATH, var_app.last_update).click()
        #     time.sleep(1)
        # except:
        #     pass
        #
        # login.login_back(self)
        # minitor_app.minitor_back()
        # route.route_back()
        # vehicle.vehicle_back()
        # homepage_app.toolbar_back()
        # image_video_app.image_back()
        # report_app.general.report_back(self)
        # utilities.general.utilities_back(self)
        # var_app.driver.implicitly_wait(1)
        # try:
        #     var_app.driver.find_element(By.XPATH, var_app.account).click()
        #     time.sleep(1)
        #     module_other_app.swipe_scaled(var_app.driver, 400, 1200, 465, 480, 500)
        #     time.sleep(1)
        #     module_other_app.tap_scaled(var_app.driver, [(200, 1300)])
        #     time.sleep(1.5)
        #     var_app.driver.find_element(By.XPATH, var_app.logout_all_devices).click()
        #     time.sleep(2)
        # except:
        #     pass



    def login_back(self):
        var_app.driver.implicitly_wait(0.2)
        try:
            var_app.driver.find_element(By.XPATH, var_app.login_back1).click()
            time.sleep(1.2)
        except:
            pass
        try:
            var_app.driver.find_element(By.XPATH, var_app.login_back2).click()
            time.sleep(1.2)
        except:
            pass
        try:
            var_app.driver.find_element(By.XPATH, var_app.login_back3).click()
            time.sleep(1.2)
        except:
            pass
        try:
            var_app.driver.find_element(By.XPATH, var_app.login_back4).click()
            time.sleep(1.2)
        except:
            pass
        try:
            var_app.driver.find_element(By.XPATH, var_app.login_back5).click()
            time.sleep(1.2)
        except:
            pass
        try:
            var_app.driver.find_element(By.XPATH, var_app.close).click()
            time.sleep(1.2)
        except:
            pass
        try:
            var_app.driver.find_element(By.XPATH, var_app.CLOSE).click()
            time.sleep(1.2)
        except:
            pass
        var_app.driver.press_keycode(4)
        time.sleep(2)



    def check_logout(self):
        var_app.driver.implicitly_wait(0.3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.last_update).click()
            time.sleep(1)
        except:
            pass
        login.logout_back(self)

        try:
            var_app.driver.find_element(By.XPATH, var_app.account).click()
            time.sleep(1)
            module_other_app.swipe_scaled(var_app.driver, 400, 1200, 465, 480, 500)
            time.sleep(1)
            module_other_app.tap_scaled(var_app.driver, [(200, 1300)])
            time.sleep(1.5)
            var_app.driver.find_element(By.XPATH, var_app.logout_all_devices).click()
            time.sleep(2)
        except:
            pass



    def check_logout1(self, name_account, user, password):
        var_app.driver.implicitly_wait(0.2)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)
        except:
            pass

        try:
            var_app.driver.find_element(By.XPATH, var_app.last_update).click()
            time.sleep(1)
        except:
            pass


        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.account).click()
            time.sleep(1)
            check_account = var_app.driver.find_element(By.XPATH, var_app.path_check_account).text
            if check_account == name_account:
                pass
            else:
                time.sleep(1)
                module_other_app.swipe_scaled(var_app.driver, 400, 1200, 465, 480, 500)
                time.sleep(1)
                module_other_app.tap_scaled(var_app.driver, [(200, 1300)])
                time.sleep(1.5)
                var_app.driver.find_element(By.XPATH, var_app.logout_all_devices).click()
                time.sleep(2)
                login.login_v3(self, user, password)
        except:
            pass

        try:
            var_app.driver.find_element(By.XPATH, var_app.login_user1)
            login.login_v3(self, user, password)
        except:
            pass

        time.sleep(0.5)



    @retry(tries=3, delay=2, backoff=1, jitter=5, )
    def login_v3(self, user, password):
        module_other_app.close_app()
        time.sleep(2)

        var_app.driver.find_element(By.XPATH, var_app.login_user1).clear()
        var_app.driver.find_element(By.XPATH, var_app.login_user1).send_keys(user)
        time.sleep(0.5)
        var_app.driver.find_element(By.XPATH, var_app.login_password1).clear()
        var_app.driver.find_element(By.XPATH, var_app.login_password1).send_keys(password)

        var_app.driver.implicitly_wait(1)
        var_app.driver.find_element(by=AppiumBy.XPATH, value=var_app.login_buttonlogin).click()
        time.sleep(3)

        login.check_login(self)
        other_function.delete_nofitication(self)
        var_app.driver.implicitly_wait(0.3)
        var_app.driver.find_element(By.XPATH, var_app.account)
        time.sleep(2)





    def check_login(self):
        var_app.driver.implicitly_wait(0.3)
        print("đang check login app")
        n = 0
        while (n < 20):
            n = n + 1
            try:
                var_app.driver.find_element(By.XPATH, var_app.login_user1)
                time.sleep(1)
                print(f"đang đợi login vào app, giây thứ; {n}")
            except:
                print("đã login vào app")
                break



class other_function:

    def change_language(self, code, eventname, result, coordinates_x, coordinates_y, pathcheck, desire, pathimage):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.change_language_button)
        except:
            module_other_app.close_app()


        var_app.driver.implicitly_wait(3)
        var_app.driver.find_element(By.XPATH, var_app.change_language_button).click()
        time.sleep(2)
        module_other_app.tap_scaled(var_app.driver, [(coordinates_x, coordinates_y)])
        time.sleep(3)
        module_other_app.write_result_text_try_if(code, eventname, result, "Màn hình đăng nhập - Đổi ngôn ngữ",
                                                  pathcheck, desire, pathimage)



    def affiliate_link_outsite(self, code, eventname, result, affiliate_link, pathcheck, pathimage):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.check_change_language_vietnamese)
        except:
            module_other_app.close_app()

        var_app.driver.implicitly_wait(2)
        var_app.driver.find_element(By.XPATH, affiliate_link).click()
        time.sleep(3.5)
        # module_other_app.write_result_text_try_if(code, eventname, result, "Màn hình đăng nhập - Link liên kết",
        #                                             pathcheck, desire, pathimage)



        if pathimage == "_DangNhap_LinkLienKet_DangKyTuVan.png":
            module_other_app.write_result_text_try_if(code, eventname, result, "Màn hình đăng nhập - Link liên kết",
                                                    pathcheck, "ĐĂNG KÝ TƯ VẤN", pathimage)
        else:
            module_other_app.write_result_not_displayed_try(code, eventname, result, "Màn hình đăng nhập - Link liên kết",
                                                            pathcheck, pathimage)

        var_app.driver.press_keycode(4)
        time.sleep(1.5)
        if pathimage == "_DangNhap_LinkLienKet_DangKyTuVan.png":
            var_app.driver.find_element(By.XPATH, var_app.Register_for_consultation_iconx).click()
            time.sleep(1)




    def affiliate_link_insite(self, code, eventname, result, affiliate_link, pathcheck, desire, pathimage):
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.check_change_language_vietnamese)
        except:
            module_other_app.close_app()

        var_app.driver.implicitly_wait(3)
        var_app.driver.find_element(By.XPATH, var_app.login_iconseemore).click()
        time.sleep(1.5)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, affiliate_link).click()
        except:
            try:
                var_app.driver.find_element(By.XPATH, var_app.login_iconseemore).click()
                time.sleep(1)
                var_app.driver.find_element(By.XPATH, affiliate_link).click()
            except:
                pass

        time.sleep(3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.OK).click()
            time.sleep(1)
        except:
            pass
        if pathimage == "_DangNhap_LinkLienKet_Youtobe.png1":#giờ chỉ cần ko ở màn đăng nhập bagps
            module_other_app.write_result_text_try_if(code, eventname, result, "Màn hình đăng nhập - Link liên kết",
                                                  pathcheck, desire, pathimage)


        else:
            module_other_app.write_result_not_displayed_try(code, eventname, result, "Màn hình đăng nhập - Link liên kết",
                                                  pathcheck, pathimage)

        # module_other_app.write_result_text_try_if(code, eventname, result, "Màn hình đăng nhập - Link liên kết",
        #                                             pathcheck, desire, pathimage)

        module_other_app.open_bagps()



    def delete_nofitication(self):
        var_app.driver.implicitly_wait(0.1)
        print("đang tắt thông báo")
        try:
            var_app.driver.find_element(By.XPATH, var_app.see_notification_batery).click()
            time.sleep(1)
            print("n15")
        except:
            pass
        try:
            var_app.driver.find_element(By.XPATH, var_app.see_notification_iconx8).click()
            time.sleep(1)
            print("n14")
        except:
            pass

        try:
            var_app.driver.find_element(By.XPATH, var_app.see_notification_iconx0).click()
            print("n13")
        except:
            pass

        try: #2
            var_app.driver.find_element(By.XPATH, var_app.nofitication1).click()
            time.sleep(1)
            print("n12")
        except:
            pass

        try:
            var_app.driver.find_element(By.XPATH, var_app.transmission_iconx).click()
            time.sleep(1)
            print("n11")
        except:
            pass

        try:
            var_app.driver.find_element(By.XPATH, var_app.info_fee_iconx).click()
            time.sleep(1)
            print("n10")
        except:
            pass


        try:
            var_app.driver.find_element(By.XPATH, var_app.see_notification_iconx2).click()
            print("n9")
        except:
            pass

        try:
            var_app.driver.find_element(By.XPATH, var_app.see_notification_iconx3).click()
            print("n8")
        except:
            pass


        try:
            var_app.driver.find_element(by=AppiumBy.XPATH, value=var_app.fee_infomation_iconx).click()
            time.sleep(1)
            print("n7")
            var_app.driver.find_element(by=AppiumBy.XPATH, value=var_app.close).click()
            time.sleep(1)
            print("n6")
        except:
            pass

        try:
            var_app.driver.find_element(By.XPATH, var_app.see_notification_iconx4).click()
            print("n4")
        except:
            pass

        try:
            var_app.driver.find_element(By.XPATH, var_app.see_notification_iconx5).click()
            print("n4")
        except:
            pass

        try:
            var_app.driver.find_element(By.XPATH, var_app.see_notification_iconx6).click()
            print("n3")
        except:
            pass
        try:
            var_app.driver.find_element(By.XPATH, var_app.CLOSE).click()
            print("n2")
        except:
            pass
        try:
            var_app.driver.find_element(By.XPATH, var_app.see_notification_iconx7).click()
            print("n1")
        except:
            pass
        try:
            var_app.driver.find_element(By.XPATH, var_app.see_notification_iconx10).click()
            time.sleep(1)
            print("n0")
        except:
            pass
        try:
            var_app.driver.find_element(By.XPATH, var_app.never).click()
            time.sleep(1)
            print("n15")
        except:
            pass
        try:
            var_app.driver.find_element(By.XPATH, var_app.READED).click()
            time.sleep(1)
            print("n16")
        except:
            pass
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.in_use_app).click()
            time.sleep(1)
            print("n17")
        except:
            pass
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.later).click()
            time.sleep(1)
            print("n18")
        except:
            pass
        print("đã tắt thông báo")



class drive:

    def for_drive(self, code, eventname, result):
        var_app.driver.implicitly_wait(0.3)
        module_other_app.close_app()

        var_app.driver.find_element(By.XPATH, var_app.FOR_DRIVE).click()
        time.sleep(2)
        module_other_app.write_result_text_try_if(code, eventname, result, "Màn hình đăng nhập - DÀNH CHO LÁI XE",
                                              var_app.check_for_drive, "TRA CỨU PHƯƠNG TIỆN", "_DANHCHOLAIXE.png")

    def for_drive_search(self, code, eventname, result):
        var_app.driver.implicitly_wait(2)

        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.for_drive_search_input)
        except:
            drive.for_drive(self, "", "", "")

        var_app.driver.find_element(By.XPATH, var_app.for_drive_search_input).clear()
        time.sleep(0.5)
        var_app.driver.find_element(By.XPATH, var_app.for_drive_search_input).send_keys("99A12468")
        time.sleep(0.5)
        var_app.driver.find_element(By.XPATH, var_app.see_info).click()
        time.sleep(5)
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.ALLOW).click()
            time.sleep(2)
        except:
            pass
        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.in_use_app).click()
            time.sleep(2)
        except:
            pass
        try:
            wait = WebDriverWait(var_app.driver, 15)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_app.check_for_drive_search)))
        except Exception as e:
            print(e)


        module_other_app.write_result_text_try_if(code, eventname, result, "Màn hình đăng nhập - DÀNH CHO LÁI XE",
                                              var_app.check_for_drive_search, "Thông tin chung", "_DANHCHOLAIXE_XemThongTin.png")



    def for_drive_icon(self, code, eventname, result, path_icon1, path_icon2, path_check, name_image):
        var_app.driver.implicitly_wait(2)

        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.Summary)
        except:
            drive.for_drive_search(self, "", "", "")

        var_app.driver.find_element(By.XPATH, path_icon1).click()
        time.sleep(1)

        module_other_app.write_result_displayed_try(code, eventname, result, "Màn hình đăng nhập - DÀNH CHO LÁI XE",
                                              path_check, name_image)

        var_app.driver.find_element(By.XPATH, path_icon2).click()
        time.sleep(1)


    def check_info_sumnary(self, code, eventname, result, type_check, path_check, name_image):
        var_app.driver.implicitly_wait(2)

        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.Summary)
        except:
            drive.for_drive_search(self, "", "", "")

        if type_check == "0":
            module_other_app.write_result_displayed_try(code, eventname, result, "Màn hình đăng nhập - DÀNH CHO LÁI XE - Tổng quan",
                                                        path_check, name_image)

        if type_check == "1":
            module_other_app.write_result_text_try_if_other(code, eventname, result, "Màn hình đăng nhập - DÀNH CHO LÁI XE - Tổng quan",
                                                      path_check, "", name_image)






    def for_drive_overview(self, code, eventname, result):
        var_app.driver.implicitly_wait(2)

        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.OVERVIEW)
        except:
            drive.for_drive_search(self, "", "", "")


        var_app.driver.find_element(By.XPATH, var_app.for_drive_overview).click()
        time.sleep(2)
        var_app.logging.info("--------------")
        var_app.logging.info("Màn hình đăng nhập - DÀNH CHO LÁI XE - Hướng dẫn")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        try:
            help1 = var_app.driver.find_element(By.XPATH, var_app.help1).text
            help2 = var_app.driver.find_element(By.XPATH, var_app.help2).text
            help3 = var_app.driver.find_element(By.XPATH, var_app.help3).text
            help4 = var_app.driver.find_element(By.XPATH, var_app.help4).text

            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 6, "1.{}\n2.{}\n3.{}\n4.{}".format(help1, help2, help3, help4))
            var_app.logging.info("1.{}\n2.{}\n3.{}\n4.{}".format(help1, help2, help3, help4))
            if help1 == "CẬP NHẬT THÔNG TIN" and help2 == "THỜI GIAN LÁI XE VÀ QUÁ TỐC ĐỘ" and help3 == "THỜI GIAN DỪNG ĐỖ" and help4 == "VIDEO HƯỚNG DẪN CÁCH TÍNH THỜI GIAN LÁI XE":
                var_app.logging.info("True")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Pass")
            else:
                var_app.logging.info("False")
                var_app.driver.save_screenshot(var_app.imagepath + code + "_DANHCHOLAIXE_HuongDan.png")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Fail")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 13, code + "_DANHCHOLAIXE_HuongDan.png")
        except:
            var_app.logging.info("False")
            var_app.driver.save_screenshot(var_app.imagepath + code + "_DANHCHOLAIXE_HuongDan.png")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 7, "Fail")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 13, code + "_DANHCHOLAIXE_HuongDan.png")


    def for_drive_punish(self, code, eventname, result):
        var_app.driver.implicitly_wait(2)

        try:
            var_app.driver.implicitly_wait(0.3)
            var_app.driver.find_element(By.XPATH, var_app.OVERVIEW)
        except:
            drive.for_drive_search(self, "", "", "")

        var_app.driver.find_element(By.XPATH, var_app.for_drive_punish).click()
        time.sleep(2)

        module_other_app.write_result_text_try_if(code, eventname, result, "Màn hình đăng nhập - DÀNH CHO LÁI XE - Tổng quan",
                                                  var_app.check_for_drive_punish, "Dữ liệu Phạt nguội được chúng tôi trích dẫn từ nguồn: Cổng thông tin điện tử Cục Cảnh Sát Giao Thông",
                                                        "_DANHCHOLAIXE_PhatNguoi.png")


    def check_info_punish(self, code, eventname, result, path_check, name_image):
        var_app.driver.implicitly_wait(2)

        try:
            print("n0-1")
            var_app.driver.implicitly_wait(0.3)
            dong1 = var_app.driver.find_element(By.XPATH, var_app.punish1).text
            print("n0")
            print(dong1)
        except:
            try:
                print("n0.5")
                var_app.driver.find_element(By.XPATH, var_app.for_drive_back).click()
                time.sleep(2)
                var_app.driver.find_element(By.XPATH, var_app.see_info).click()
                time.sleep(5)
                var_app.driver.find_element(By.XPATH, var_app.for_drive_punish).click()
                time.sleep(2)
            except:
                print("n1")
                module_other_app.close_app()
                drive.for_drive_punish(self, "", "", "")
                print("n2")


        module_other_app.write_result_text_try_if_other(code, eventname, result, "Màn hình đăng nhập - DÀNH CHO LÁI XE - Tổng quan",
                                                  path_check, "", name_image)
















