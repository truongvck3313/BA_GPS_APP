import time
from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import AppiumBy
import var_app

























class goivon:
    def khampha(self):
        driver.implicitly_wait(15)
        driver.find_element(By.XPATH, var_app.emso).click()
        time.sleep(3)
        driver.find_element(by=AppiumBy.XPATH, value=var_app.trangchu_iconmenu).click()
        driver.find_element(by=AppiumBy.XPATH, value=var_app.trangchu_iconmenu_goivon).click()
        time.sleep(1.5)

        el = driver.find_element(by=AppiumBy.XPATH, value=var_app.khamkha_quantam)
        print(el.get_attribute("content-desc"))

        driver.find_element(by=AppiumBy.XPATH, value=var_app.khamkha_quantam).click()
        time.sleep(1)
        driver.find_element(by=AppiumBy.XPATH, value=var_app.khamkha_quantam).click()
        time.sleep(1)
        driver.find_element(by=AppiumBy.XPATH, value=var_app.khamkha_chonduan1).click()
        time.sleep(1)
        check_khampha_tenduan = driver.find_element(by=AppiumBy.XPATH, value=var_app.check_khampha_tenduan).text
        print(check_khampha_tenduan)
        time.sleep(1)
        #Ủng hộ - ủng hộ
        driver.find_element(by=AppiumBy.XPATH, value=var_app.khamkha_ungho).click()
        time.sleep(1)
        driver.find_element(by=AppiumBy.XPATH, value=var_app.goivon_ungho_ungho).click()
        time.sleep(0.5)
        driver.find_element(by=AppiumBy.XPATH, value=var_app.khamkha_ungho_ungho50).click()
        driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Ủng hộ").click()
        time.sleep(1.5)
        driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Scrim").click()
        time.sleep(1)
        #Ủng hộ - đầu tư
        driver.find_element(by=AppiumBy.XPATH, value=var_app.khamkha_ungho).click()
        time.sleep(1)
        driver.find_element(by=AppiumBy.XPATH, value=var_app.goivon_ungho_dautu).click()
        time.sleep(0.5)
        driver.find_element(by=AppiumBy.XPATH, value=var_app.khamkha_ungho_ungho50).click()
        driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Đầu tư").click()
        time.sleep(1.5)
        driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Scrim").click()
        time.sleep(1)
        #Ủng hộ - nhắn tin
        driver.find_element(by=AppiumBy.XPATH, value=var_app.khamkha_ungho).click()
        time.sleep(1)
        driver.find_element(by=AppiumBy.XPATH, value=var_app.goivon_ungho_nhantin).click() #chưa chuyển tới trang nhắn tin cho người gọi vốn 1133
        time.sleep(1)

        #Quan tâm
        driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Quan tâm").click()
        time.sleep(1.5)
        driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Quan tâm").click()
        time.sleep(1)

        #Dấu 3 chấm - chia sẻ
        driver.find_element(by=AppiumBy.XPATH, value=var_app.goivon_dau3cham).click()
        time.sleep(1)
        driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Chia sẻ").click()
        time.sleep(1)
        driver.find_element(by=AppiumBy.XPATH, value=var_app.chiase_mota).send_keys(data['goivon']['khampha_chiase'])
        time.sleep(0.5)
        driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Chia sẻ ngay").click()
        time.sleep(2)
        #Dấu 3 chấm - sao chép,liên kết
        driver.find_element(by=AppiumBy.XPATH, value=var_app.goivon_dau3cham).click()
        time.sleep(1)
        driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Sao chép liên kết").click()    #ko sao chép đc 1133
        time.sleep(1)
        driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Scrim").click()
        #Dấu 3 chấm - sao chép,liên kết
        driver.find_element(by=AppiumBy.XPATH, value=var_app.goivon_dau3cham).click()
        time.sleep(1)
        driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Tìm sự hỗ trợ hoặc báo cáo dự án").click()    #ko 	Tìm sự hỗ trợ hoặc báo cáo dự án đc 1133
        time.sleep(1)
        driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Cuộc thảo luận").click()
        time.sleep(1)
        driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="FAQ").click()
        time.sleep(1)
        driver.swipe(682, 1062, 275, 1062, 200)
        driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Ảnh").click()
        time.sleep(1)
        driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Video").click()
        time.sleep(1)
        driver.swipe(682, 1062, 275, 1062, 200)
        driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Danh sách ủng hộ").click()
        time.sleep(1)
        driver.swipe(75, 1062, 682, 1062, 200)
        time.sleep(0.5)
        driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Giới thiệu").click()
        time.sleep(1)
        driver.swipe(350, 1200, 350, 100, 200)
        time.sleep(1)
        driver.swipe(350, 1200, 350, 100, 200)
        time.sleep(1)
        driver.swipe(350, 1200, 350, 100, 200)
        time.sleep(1)
        driver.find_element(by=AppiumBy.XPATH,  value=var_app.goivon_khampha_xem).click()
        time.sleep(2.5)
        el = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="nguyễn huy (ga)")
        # print("accessibility id")
        # print(el.get_attribute("accessibility id"))
        print("content-desc")
        print(el.get_attribute("content-desc"))

        print("text")
        print(el.get_attribute("text"))
        driver.back()
        time.sleep(1.5)
        driver.swipe(350, 1200, 350, 100, 200)
        driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Ủng hộ").click()
        time.sleep(1)
        driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Scrim").click()
        time.sleep(1)
        driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Đầu tư").click()
        time.sleep(1)
        driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Scrim").click()
        time.sleep(1)
        driver.back()
        time.sleep(1)
        driver.back()
        time.sleep(1)
        driver.back()
        time.sleep(1)

    def loimoi(self):
        driver.implicitly_wait(15)
        driver.find_element(By.XPATH, var_app.emso).click()
        time.sleep(3)
        driver.find_element(by=AppiumBy.XPATH, value=var_app.trangchu_iconmenu).click()
        driver.find_element(by=AppiumBy.XPATH, value=var_app.trangchu_iconmenu_goivon).click()
        time.sleep(1.5)
        #Lời mời
        driver.find_element(by=AppiumBy.XPATH, value=var_app.goivon_loimoi).click()
        print("heluuuuu")



class hoctap():
    def khampha(self):
        driver.implicitly_wait(15)
        driver.find_element(By.XPATH, var_app.emso).click()
        time.sleep(3)
        driver.find_element(by=AppiumBy.XPATH, value=var_app.trangchu_iconmenu).click()
        driver.find_element(by=AppiumBy.XPATH, value=var_app.trangchu_iconmenu_hoctap).click()
        time.sleep(1.5)
        driver.find_element(by=AppiumBy.XPATH, value=var_app.hoctap_khampha_traphi).click()
        time.sleep(2)
        driver.find_element(by=AppiumBy.XPATH, value=var_app.hoctap_khampha_mienphi).click()
        time.sleep(2)
        driver.find_element(by=AppiumBy.XPATH, value=var_app.hoctap_khampha_quantam).click()
        time.sleep(1)
        driver.find_element(by=AppiumBy.XPATH, value=var_app.hoctap_khampha_quantam).click()
        time.sleep(1)
        driver.find_element(by=AppiumBy.XPATH, value=var_app.hoctap_khampha_chiase).click()
        time.sleep(1)
        driver.find_element(by=AppiumBy.XPATH, value=var_app.chiase_mota).send_keys(data['hoctap']['khampha_chiase'])
        time.sleep(1)
        driver.find_element(by=AppiumBy.XPATH, value=var_app.chiase_chiasengay).click()
        check_messagechiase = driver.find_element(by=AppiumBy.XPATH, value=var_app.check_messagechiase).get_attribute("content-desc")
        logging.info("Học tập - Khám phá - Chia sẻ")
        logging.info("check font-end: Message chia sẻ khóa học - Chia sẻ thành công")
        logging.info(check_messagechiase == "Chia sẻ thành công")
        time.sleep(1)
        #Xem chi tiết khóa học
        driver.find_element(by=AppiumBy.XPATH, value=var_app.hoctap_khampha_xem1).click()
        time.sleep(1)














