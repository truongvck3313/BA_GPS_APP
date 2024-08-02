import time
from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import AppiumBy
import var_app
import module_other_app
from retry import retry






class login:

    @retry(tries=3, delay=2, backoff=1, jitter=5, )
    def login(self, user, password, code, eventname, result, pathcheck, desire, pathimage):
        other_function.delete_nofitication(self)
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.login_user)
        except:
            login.check_logout(self)

        var_app.driver.implicitly_wait(4)
        var_app.driver.find_element(By.XPATH, var_app.login_user).clear()
        var_app.driver.find_element(By.XPATH, var_app.login_user).send_keys(user)

        time.sleep(0.5)
        var_app.driver.find_element(By.XPATH, var_app.login_password).clear()
        var_app.driver.find_element(By.XPATH, var_app.login_password).send_keys(password)

        var_app.driver.implicitly_wait(1)
        var_app.driver.find_element(by=AppiumBy.XPATH, value=var_app.login_buttonlogin).click()
        time.sleep(2)
        other_function.delete_nofitication(self)

        # var_app.driver.press_keycode(4)
        # time.sleep(6)
        var_app.logging.info("--------------")
        var_app.logging.info("Login với tài khoản: " + user)
        var_app.logging.info("Login với mật khẩu: " + password)
        if code == "Login01" or code == "Login02" or code == "Login03":
            module_other_app.write_result_text_try_if(code, eventname, result, "Màn hình đăng nhập - Login",
                                                  pathcheck, desire, pathimage)


        if code == "Login04":
            module_other_app.write_result_not_displayed_try(code, eventname, result, "Màn hình đăng nhập - Login",
                                        var_app.check_customer_account1, "_DangNhap_TKKhachHangKhongCoQuyenGiamSat.png")



    # @retry(tries=3, delay=2, backoff=1, jitter=5, )
    def login_wrong(self, user, password, code, eventname, result):
        var_app.driver.implicitly_wait(5)
        login.check_logout(self)
        var_app.driver.find_element(By.XPATH, var_app.login_user).clear()
        var_app.driver.find_element(By.XPATH, var_app.login_user).send_keys(user)

        time.sleep(0.5)
        var_app.driver.find_element(By.XPATH, var_app.login_password).clear()
        var_app.driver.find_element(By.XPATH, var_app.login_password).send_keys(password)

        var_app.driver.find_element(by=AppiumBy.XPATH, value=var_app.login_buttonlogin).click()
        time.sleep(2.5)
        var_app.logging.info("--------------")
        var_app.logging.info("Login với tài khoản: " + user)
        var_app.logging.info("Login với mật khẩu: " + password)
        module_other_app.write_result_text_try_if(code, eventname, result, "Màn hình đăng nhập - Login",
                                              var_app.check_wronglogin, "Tài khoản hoặc mật khẩu không chính xác. Vui lòng kiểm tra lại", "_DangNhap_TKDungMatKhauSai.png")

        try:
            var_app.driver.find_element(By.XPATH, var_app.login_iconx).click()
            time.sleep(1)
        except:
            pass



    def forger_user(self, code, eventname, result):
        var_app.driver.implicitly_wait(5)
        try:
            var_app.driver.find_element(By.XPATH, var_app.login_user)
        except:
            login.check_logout(self)

        var_app.driver.find_element(By.XPATH, var_app.login_user).clear()
        var_app.driver.find_element(By.XPATH, var_app.login_user).send_keys(var_app.data['login']['taikhoansai_user'])

        time.sleep(0.5)
        var_app.driver.find_element(By.XPATH, var_app.login_password).clear()
        var_app.driver.find_element(By.XPATH, var_app.login_password).send_keys(var_app.data['login']['taikhoansai_password'])

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
            var_app.driver.find_element(by=AppiumBy.XPATH, value=var_app.forger_user_skip).click()
            time.sleep(1)
        except:
            pass



    def forger_password(self, code, eventname, result):
        var_app.driver.implicitly_wait(5)
        try:
            var_app.driver.find_element(By.XPATH, var_app.forger_password).click()
        except:
            login.check_logout(self)
            var_app.driver.find_element(By.XPATH, var_app.forger_password).click()

        time.sleep(1.5)
        # module_other_app.write_result_text_try_if(code, eventname, result, "Màn hình đăng nhập - Login",
        #                                           var_app.check_forger_password1, "Quên mật khẩu", "_DangNhap_QuenMatKhau.png")



        var_app.driver.find_element(By.XPATH, var_app.forger_password_inputuser).send_keys(var_app.data['login']['quenmatkhau_user'])
        var_app.driver.find_element(By.XPATH, var_app.forger_password_inputpassword).send_keys(var_app.data['login']['quenmatkhau_sdt'])
        time.sleep(0.5)
        var_app.driver.find_element(By.XPATH, var_app.forger_password_sendcode).click()
        time.sleep(2.5)

        module_other_app.write_result_text_try_if(code, eventname, result, "Màn hình đăng nhập - Login",
                                                  var_app.check_forger_password, "Nhập mã xác thực OTP", "_DangNhap_QuenMatKhau.png")

        try:
            var_app.driver.find_element(By.XPATH, var_app.forger_password_iconback).click()
            time.sleep(1)
            var_app.driver.find_element(By.XPATH, var_app.forger_password_iconx).click()
            time.sleep(1)
        except:
            var_app.driver.press_keycode(4)
            time.sleep(1)


    # @retry(tries=3, delay=2, backoff=1, jitter=5, )
    def remember_login_mark(self, code, eventname, result):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        try:
            var_app.driver.find_element(By.XPATH, var_app.checkbox_remember)
        except:
            other_function.delete_nofitication(self)
            login.check_logout(self)

        try:
            var_app.driver.find_element(By.XPATH, var_app.checkbox_remember2)
        except:
            var_app.driver.find_element(By.XPATH, var_app.checkbox_remember1).click()

        time.sleep(0.5)
        var_app.driver.find_element(By.XPATH, var_app.login_user).clear()
        var_app.driver.find_element(By.XPATH, var_app.login_user).send_keys(var_app.data['login']['taikhoandung_user'])
        time.sleep(0.5)
        var_app.driver.find_element(By.XPATH, var_app.login_password).clear()
        var_app.driver.find_element(By.XPATH, var_app.login_password).send_keys(var_app.data['login']['taikhoandung_password'])
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
            other_function.delete_nofitication(self)
        except:
            pass

        module_other_app.write_result_displayed_try(code, eventname, result, "Màn hình đăng nhập - Ghi nhớ đăng nhập",
                                                var_app.remember_login_mark, "_DangNhap_BoGhiNhoDangNhap.png")
        time.sleep(1)


    def remember_login_not_mark(self, code, eventname, result):
        var_app.driver.implicitly_wait(2)
        other_function.delete_nofitication(self)

        try:
            var_app.driver.find_element(By.XPATH, var_app.checkbox_remember)
        except:
            login.check_logout(self)



        try:
            var_app.driver.find_element(By.XPATH, var_app.checkbox_remember2)
            var_app.driver.find_element(By.XPATH, var_app.checkbox_remember1).click()
        except:
            pass


        time.sleep(0.5)
        var_app.driver.find_element(By.XPATH, var_app.login_user).clear()
        var_app.driver.find_element(By.XPATH, var_app.login_user).send_keys(var_app.data['login']['taikhoandung_user'])
        time.sleep(0.5)
        var_app.driver.find_element(By.XPATH, var_app.login_password).clear()
        var_app.driver.find_element(By.XPATH, var_app.login_password).send_keys(var_app.data['login']['taikhoandung_password'])
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
            other_function.delete_nofitication(self)
        except:
            pass


        module_other_app.write_result_not_displayed_try(code, eventname, result, "Màn hình đăng nhập - Ghi nhớ đăng nhập",
                                                var_app.remember_login_mark, "_DangNhap_BoGhiNhoDangNhap.png")
        time.sleep(1)
        var_app.driver.press_keycode(4)
        time.sleep(0.5)


    def logout(self):
        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.account).click()
            time.sleep(1)
            var_app.driver.swipe(400, 1200, 465, 480, 500)
            time.sleep(1)
            var_app.driver.tap([(200, 1300)])
            time.sleep(1.5)
            var_app.driver.find_element(By.XPATH, var_app.logout_all_devices).click()
        except:
            pass
        time.sleep(2)



    def check_logout(self):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        try:
            var_app.driver.find_element(By.XPATH, var_app.account).click()
            time.sleep(1)
            var_app.driver.swipe(400, 1200, 465, 480, 500)
            time.sleep(1)
            var_app.driver.tap([(200, 1300)])
            time.sleep(1.5)
            var_app.driver.find_element(By.XPATH, var_app.logout_all_devices).click()
            time.sleep(2)
        except:
            pass




    def check_logout1(self, name_account, user, password):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(7)
        except:
            pass
        var_app.driver.implicitly_wait(5)
        try:
            var_app.driver.find_element(By.XPATH, var_app.account).click()
            time.sleep(1)
            check_account = var_app.driver.find_element(By.XPATH, var_app.path_check_account).text
            if check_account == name_account:
                pass
            else:
                time.sleep(1)
                var_app.driver.swipe(400, 1200, 465, 480, 500)
                time.sleep(1)
                var_app.driver.tap([(200, 1300)])
                time.sleep(1.5)
                var_app.driver.find_element(By.XPATH, var_app.logout_all_devices).click()
                time.sleep(2)
                login.login_v3(self, user, password)
        except:
            pass
        time.sleep(0.5)




    @retry(tries=3, delay=2, backoff=1, jitter=5, )
    def login_v3(self, user, password):
        other_function.delete_nofitication(self)
        var_app.driver.implicitly_wait(5)
        login.check_logout(self)
        try:
            var_app.driver.find_element(By.XPATH, var_app.login_user).clear()
        except:
            # var_app.driver.press_keycode(4)
            # time.sleep(1)
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(5)
            var_app.driver.find_element(By.XPATH, var_app.login_user).clear()

        var_app.driver.find_element(By.XPATH, var_app.login_user).send_keys(user)


        time.sleep(0.5)
        var_app.driver.find_element(By.XPATH, var_app.login_password).clear()
        var_app.driver.find_element(By.XPATH, var_app.login_password).send_keys(password)

        var_app.driver.implicitly_wait(1)
        var_app.driver.find_element(by=AppiumBy.XPATH, value=var_app.login_buttonlogin).click()
        time.sleep(3)
        other_function.delete_nofitication(self)
        # try:
        #     var_app.driver.find_element(By.XPATH, var_app.info_fee_iconx).click()
        #     time.sleep(1)
        # except:
        #     pass

class other_function:

    def change_language(self, code, eventname, result, coordinates_x, coordinates_y, pathcheck, desire, pathimage):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.change_language_button)
        except:
            login.check_logout(self)

        var_app.driver.implicitly_wait(3)
        var_app.driver.find_element(By.XPATH, var_app.change_language_button).click()
        time.sleep(2)
        var_app.driver.tap([(coordinates_x, coordinates_y)])
        time.sleep(3)
        module_other_app.write_result_text_try_if(code, eventname, result, "Màn hình đăng nhập - Đổi ngôn ngữ",
                                                  pathcheck, desire, pathimage)



    def affiliate_link_outsite(self, code, eventname, result, affiliate_link, pathcheck, pathimage):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_change_language_vietnamese)
        except:
            login.check_logout(self)

        var_app.driver.implicitly_wait(3)
        var_app.driver.find_element(By.XPATH, affiliate_link).click()
        time.sleep(3.5)

        module_other_app.write_result_displayed_try(code, eventname, result, "Màn hình đăng nhập - Link liên kết",
                                                pathcheck, pathimage)

        var_app.driver.press_keycode(4)
        time.sleep(1.5)
        if pathimage == "_DangNhap_LinkLienKet_DangKyTuVan.png":
            var_app.driver.find_element(By.XPATH, var_app.Register_for_consultation_iconx).click()
            time.sleep(1)




    def affiliate_link_insite(self, code, eventname, result, affiliate_link, pathcheck, desire, pathimage):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_change_language_vietnamese)
        except:
            login.check_logout(self)

        var_app.driver.implicitly_wait(3)
        var_app.driver.find_element(By.XPATH, var_app.login_iconseemore).click()
        time.sleep(1)
        try:
            var_app.driver.find_element(By.XPATH, affiliate_link).click()
        except:
            try:
                var_app.driver.find_element(By.XPATH, var_app.login_iconseemore).click()
                time.sleep(1)
                var_app.driver.find_element(By.XPATH, affiliate_link).click()
            except:
                pass


        if code == "Login15" or code == "Login16" or code == "Login20":
            time.sleep(3)
            module_other_app.write_result_text_try_if_other(code, eventname, result, "Màn hình đăng nhập - Link liên kết",
                                                  pathcheck, desire, pathimage)



        if code == "Login17" or code == "Login18" or code == "Login19":
            time.sleep(4)
            module_other_app.write_result_text_try_if(code, eventname, result, "Màn hình đăng nhập - Link liên kết",
                                                  pathcheck, desire, pathimage)

        var_app.driver.press_keycode(4)
        time.sleep(1.5)



    def delete_nofitication(self):
        var_app.driver.implicitly_wait(0.2)
        try:
            var_app.driver.find_element(By.XPATH, var_app.nofitication1).click()
            time.sleep(1)
        except:
            pass

        try:
            var_app.driver.find_element(By.XPATH, var_app.transmission_iconx).click()
            time.sleep(1)
        except:
            pass

        try:
            var_app.driver.find_element(By.XPATH, var_app.info_fee_iconx).click()
            time.sleep(1)
        except:
            pass


        try:
            var_app.driver.find_element(By.XPATH, var_app.see_notification_iconx2).click()
        except:
            pass

        try:
            var_app.driver.find_element(By.XPATH, var_app.see_notification_iconx3).click()
        except:
            pass


        try:
            var_app.driver.find_element(by=AppiumBy.XPATH, value=var_app.fee_infomation_iconx).click()
            time.sleep(1)
            var_app.driver.find_element(by=AppiumBy.XPATH, value=var_app.close).click()
            time.sleep(1)
        except:
            pass

        try:
            var_app.driver.find_element(By.XPATH, var_app.see_notification_iconx4).click()
        except:
            pass

        try:
            var_app.driver.find_element(By.XPATH, var_app.see_notification_iconx5).click()
        except:
            pass