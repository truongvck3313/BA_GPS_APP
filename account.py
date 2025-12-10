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
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC










class account:

    def check_version(self, code, eventname, result):
        var_app.driver.implicitly_wait(5)
        login_app.login.login_v3(self, var_app.data['login']['khongnhom_quantri_tk'], var_app.data['login']['khongnhom_quantri_mk'])

        var_app.driver.find_element(By.XPATH, var_app.account).click()
        time.sleep(2.5)
        version = var_app.driver.find_element(By.XPATH, var_app.check_version).text
        module_other_app.writeData1(var_app.path_luutamthoi, "Sheet1", 115, 2, version)
        print(f"version: {version}")
        module_other_app.write_result_text_try_if_other(code, eventname, result, "Tài khoản - Phiên bản",
                                              var_app.check_version, "", "_TaiKhoan_PhienBan.png")













