import time
from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import AppiumBy
import var_app
import module_other_app
from retry import retry







class login:

    @retry(tries=3, delay=2, backoff=1, jitter=5, )
    def login(self, user, password, code, eventname, result, pathcheck, desire, pathimage):
        var_app.driver.implicitly_wait(5)
        try:
            var_app.driver.find_element(By.XPATH, var_app.login_user)
        except:
            login.check_logout(self)

        try:
            var_app.driver.find_element(By.XPATH, var_app.login_user).clear()
        except:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(2)

        try:
            var_app.driver.find_element(By.XPATH, var_app.login_user).clear()
        except:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(2)
            var_app.driver.find_element(By.XPATH, var_app.login_user).clear()

        try:
            var_app.driver.find_element(By.XPATH, var_app.login_user).send_keys(user)
        except:
            var_app.driver.find_element(By.XPATH, var_app.login_user).send_keys(user)

        time.sleep(0.5)
        var_app.driver.find_element(By.XPATH, var_app.login_password).clear()
        var_app.driver.find_element(By.XPATH, var_app.login_password).send_keys(password)

        check_remember_login1 = var_app.driver.find_element(By.XPATH, var_app.checkbox_remember).get_attribute("checked")
        print("checkbox: ", check_remember_login1)
        if check_remember_login1 == "true":
            var_app.driver.find_element(By.XPATH, var_app.checkbox_remember).click()
            time.sleep(0.5)

        var_app.driver.implicitly_wait(2)
        var_app.driver.find_element(by=AppiumBy.XPATH, value=var_app.login_buttonlogin).click()
        time.sleep(2)

        try:
            var_app.driver.find_element(by=AppiumBy.XPATH, value=var_app.fee_infomation_iconx).click()
            time.sleep(1)
            var_app.driver.find_element(by=AppiumBy.XPATH, value=var_app.close).click()
            time.sleep(1)
        except:
            pass


        try:
            pathcheck1 = var_app.driver.find_element(by=AppiumBy.XPATH, value=var_app.account)
        except:
            var_app.driver.find_element(by=AppiumBy.XPATH, value=var_app.login_buttonlogin).click()
            time.sleep(2)

        var_app.driver.press_keycode(4)

        var_app.driver.implicitly_wait(5)
        var_app.logging.info("--------------")
        var_app.logging.info("Login với tài khoản: " + user)
        var_app.logging.info("Login với mật khẩu: " + password)
        if code == "Login01" or code == "Login02" or code == "Login03":
            module_other_app.write_result_text_try_if(code, eventname, result, "Màn hình đăng nhập - Login",
                                                  pathcheck, desire, pathimage)


        if code == "Login04":
            module_other_app.write_result_not_displayed_try(code, eventname, result, "Màn hình đăng nhập - Login",
                                        var_app.check_customer_account1, "_DangNhap_TKKhachHangKhongCoQuyenGiamSat.png")
        login.logout(self)



    @retry(tries=3, delay=2, backoff=1, jitter=5, )
    def login_wrong(self, user, password, code, eventname, result):
        var_app.driver.implicitly_wait(5)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
        except:
            var_app.driver.press_keycode(3)
            time.sleep(2)
            try:
                var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            except:
                pass
            time.sleep(2)
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
                                                  var_app.check_forger_user, "Vui lòng gọi đến số 19006464 để được hỗ trợ", "_DangNhap_QuenTaiKhoan.png")

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
        module_other_app.write_result_text_try_if(code, eventname, result, "Màn hình đăng nhập - Login",
                                                  var_app.check_forger_password1, "Quên mật khẩu", "_DangNhap_QuenMatKhau.png")



        var_app.driver.find_element(By.XPATH, var_app.forger_password_inputuser).send_keys(var_app.data['login']['quenmatkhau_user'])
        var_app.driver.find_element(By.XPATH, var_app.forger_password_inputpassword).send_keys(var_app.data['login']['quenmatkhau_sdt'])
        time.sleep(0.5)
        var_app.driver.find_element(By.XPATH, var_app.forger_password_sendcode).click()
        time.sleep(2.5)

        # module_other_app.write_result_text_try_if(code, eventname, result, "Màn hình đăng nhập - Login",
        #                                           var_app.check_forger_password, "Nhập mã OTP", "_DangNhap_QuenMatKhau.png")

        try:
            var_app.driver.find_element(By.XPATH, var_app.forger_password_iconback).click()
            time.sleep(1)
            var_app.driver.find_element(By.XPATH, var_app.forger_password_iconx).click()
            time.sleep(1)
        except:
            var_app.driver.press_keycode(4)
            time.sleep(1)



    def remember_login(self, code, eventname, result, checked, desire, name_image):
        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.checkbox_remember).get_attribute("checked")
        except:
            login.check_logout(self)


        try:
            check_remember_login1 = var_app.driver.find_element(By.XPATH, var_app.checkbox_remember).get_attribute("checked")
            print("checkbox: ", check_remember_login1)
            if check_remember_login1 == checked:
                var_app.driver.find_element(By.XPATH, var_app.checkbox_remember).click()
        except:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(1)
            check_remember_login1 = var_app.driver.find_element(By.XPATH, var_app.checkbox_remember).get_attribute("checked")
            print("checkbox: ", check_remember_login1)
            if check_remember_login1 == checked:
                var_app.driver.find_element(By.XPATH, var_app.checkbox_remember).click()
        time.sleep(0.5)


        var_app.driver.find_element(By.XPATH, var_app.login_user).clear()
        var_app.driver.find_element(By.XPATH, var_app.login_user).send_keys(var_app.data['login']['taikhoandung_user'])

        check_remember_login2 = var_app.driver.find_element(By.XPATH, var_app.checkbox_remember).get_attribute("checked")
        print("checkbox: ", check_remember_login2)
        if check_remember_login2 == checked:
            var_app.driver.find_element(By.XPATH, var_app.checkbox_remember).click()

        time.sleep(0.5)
        var_app.driver.find_element(By.XPATH, var_app.login_password).clear()
        var_app.driver.find_element(By.XPATH, var_app.login_password).send_keys(var_app.data['login']['taikhoandung_password'])

        check_remember_login3 = var_app.driver.find_element(By.XPATH, var_app.checkbox_remember).get_attribute("checked")
        print("checkbox: ", check_remember_login3)
        if check_remember_login3 == checked:
            var_app.driver.find_element(By.XPATH, var_app.checkbox_remember).click()
        time.sleep(0.5)

        var_app.driver.implicitly_wait(2)
        var_app.driver.find_element(by=AppiumBy.XPATH, value=var_app.login_buttonlogin).click()
        time.sleep(2)

        try:
            pathcheck1 = var_app.driver.find_element(by=AppiumBy.XPATH, value=var_app.account)
        except:
            var_app.driver.find_element(by=AppiumBy.XPATH, value=var_app.login_buttonlogin).click()
            time.sleep(2)

        var_app.driver.press_keycode(4)

        login.check_logout(self)

        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(1)
        except:
            pass


        var_app.logging.info("Màn hình đăng nhập - Ghi nhớ đăng nhập")
        var_app.logging.info("Mã - " + code)
        var_app.logging.info("Tên sự kiện - " + eventname)
        var_app.logging.info("Kết quả - " + result)
        try:
            check_remember_login1 = var_app.driver.find_element(By.XPATH, var_app.checkbox_remember).get_attribute("checked")
            if check_remember_login1 == desire:
                var_app.logging.info("True")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Pass")
            else:
                var_app.logging.info("False")
                var_app.driver.save_screenshot(var_app.imagepath + code + name_image)
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Fail")
                module_other_app.writeData(var_app.checklistpath, "Checklist", code, 9, code + name_image)
        except:
            var_app.logging.info("False")
            var_app.driver.save_screenshot(var_app.imagepath + code + name_image)
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 8, "Fail")
            module_other_app.writeData(var_app.checklistpath, "Checklist", code, 9, code + name_image)
        # var_app.driver.press_keycode(3)
        time.sleep(2)



    def logout(self):
        var_app.driver.implicitly_wait(3)
        try:
            var_app.driver.find_element(By.XPATH, var_app.account).click()
            time.sleep(0.5)
            var_app.driver.find_element(By.XPATH, var_app.logout).click()
            time.sleep(1.5)
            var_app.driver.find_element(By.XPATH, var_app.logout_all_devices).click()
        except:
            pass
        time.sleep(2)



    def check_logout(self):
        var_app.driver.implicitly_wait(5)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(4)
        except:
            pass

        try:
            var_app.driver.press_keycode(4)
            var_app.driver.find_element(By.XPATH, var_app.account).click()
            time.sleep(0.5)
            var_app.driver.find_element(By.XPATH, var_app.logout).click()
            time.sleep(1.5)
            var_app.driver.find_element(By.XPATH, var_app.logout_all_devices).click()
            time.sleep(2)
        except:
            pass
        var_app.driver.press_keycode(4)
        time.sleep(0.5)




    def check_logout1(self, name_account, user, password):
        var_app.driver.implicitly_wait(1)
        try:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(7)
        except:
            pass
        var_app.driver.implicitly_wait(5)
        try:
            var_app.driver.press_keycode(4)
            var_app.driver.find_element(By.XPATH, var_app.account).click()
            time.sleep(1)
            check_account = var_app.driver.find_element(By.XPATH, var_app.path_check_account).text
            if check_account == name_account:
                pass
            else:
                var_app.driver.find_element(By.XPATH, var_app.logout).click()
                time.sleep(1.5)
                var_app.driver.find_element(By.XPATH, var_app.logout_all_devices).click()
                time.sleep(2)
                var_app.driver.press_keycode(4)
                login.login_v3(self, user, password)
        except:
            pass
        time.sleep(0.5)




    @retry(tries=3, delay=2, backoff=1, jitter=5, )
    def login_v3(self, user, password):
        var_app.driver.implicitly_wait(10)
        login.check_logout(self)
        try:
            var_app.driver.find_element(By.XPATH, var_app.login_user)
        except:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(3)

        try:
            var_app.driver.find_element(By.XPATH, var_app.login_user).clear()
        except:
            login.check_logout(self)
            var_app.driver.find_element(By.XPATH, var_app.login_user).clear()
        try:
            var_app.driver.find_element(By.XPATH, var_app.login_user).send_keys(user)
        except:
            var_app.driver.find_element(By.XPATH, var_app.login_user).send_keys(user)


        time.sleep(0.5)
        var_app.driver.find_element(By.XPATH, var_app.login_password).clear()
        var_app.driver.find_element(By.XPATH, var_app.login_password).send_keys(password)

        check_remember_login1 = var_app.driver.find_element(By.XPATH, var_app.checkbox_remember).get_attribute("checked")
        print("checkbox: ", check_remember_login1)
        if check_remember_login1 == "false":
            var_app.driver.find_element(By.XPATH, var_app.checkbox_remember).click()
            time.sleep(0.5)

        var_app.driver.implicitly_wait(2)
        var_app.driver.find_element(by=AppiumBy.XPATH, value=var_app.login_buttonlogin).click()
        time.sleep(2)

        try:
            var_app.driver.find_element(by=AppiumBy.XPATH, value=var_app.fee_infomation_iconx).click()
            time.sleep(1)
            var_app.driver.find_element(by=AppiumBy.XPATH, value=var_app.close).click()
            time.sleep(1)
        except:
            pass

        try:
            pathcheck1 = var_app.driver.find_element(by=AppiumBy.XPATH, value=var_app.account)
        except:
            var_app.driver.find_element(by=AppiumBy.XPATH, value=var_app.login_buttonlogin).click()
            time.sleep(2)
        var_app.driver.press_keycode(4)
        time.sleep(1)



class other_function:

    def change_language(self, code, eventname, result, language, pathcheck, desire, pathimage):
        var_app.driver.implicitly_wait(5)
        login.check_logout(self)
        try:
            var_app.driver.find_element(By.XPATH, var_app.change_language_button).click()
        except:
            var_app.driver.find_element(By.XPATH, var_app.bagps).click()
            time.sleep(1)
            var_app.driver.find_element(By.XPATH, var_app.change_language_button).click()
        time.sleep(2)
        var_app.driver.find_element(By.XPATH, language).click()
        time.sleep(3)
        module_other_app.write_result_text_try_if(code, eventname, result, "Màn hình đăng nhập - Đổi ngôn ngữ",
                                                  pathcheck, desire, pathimage)



    def affiliate_link_outsite(self, code, eventname, result, affiliate_link, pathcheck, pathimage):
        var_app.driver.implicitly_wait(5)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_change_language_vietnamese)
        except:
            login.check_logout(self)

        var_app.driver.find_element(By.XPATH, affiliate_link).click()
        time.sleep(3.5)

        module_other_app.write_result_displayed_try(code, eventname, result, "Màn hình đăng nhập - Link liên kết",
                                                pathcheck, pathimage)

        var_app.driver.press_keycode(4)
        time.sleep(1.5)




    def affiliate_link_insite(self, code, eventname, result, affiliate_link, pathcheck, desire, pathimage):
        var_app.driver.implicitly_wait(5)
        try:
            var_app.driver.find_element(By.XPATH, var_app.check_change_language_vietnamese)
        except:
            login.check_logout(self)

        var_app.driver.find_element(By.XPATH, var_app.login_iconseemore).click()
        time.sleep(1)
        var_app.driver.find_element(By.XPATH, affiliate_link).click()



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






