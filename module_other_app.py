import time
import openpyxl
import os
from selenium.common.exceptions import NoSuchElementException
import subprocess
import var_app
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import logging
from retry import retry



def clear_log():
    logging.basicConfig(handlers=[logging.FileHandler(filename="bagps_app.log",
                                                     encoding='utf-8', mode='w')],  #w
                        format="%(asctime)s %(name)s:%(levelname)s:%(message)s",
                        datefmt="%F %A %T",
                        level=logging.INFO)







@retry(tries=3, delay=2, backoff=1, jitter=5, )
def close_app():
    var_app.driver.implicitly_wait(1)
    #pip3 install pynput
    from pynput.keyboard import Key, Controller
    keyboard = Controller()
    time.sleep(1)
    try:
        var_app.driver.find_element(By.XPATH, var_app.close_app).click()
        time.sleep(1)
    except:
        pass

    # var_app.driver.find_element(By.XPATH, var_app.check_home)
    keyboard.press(Key.f2)
    time.sleep(1.2)
    try:
        var_app.driver.swipe(420, 200, 420, 1350, 300)
    except:
        keyboard.press(Key.f2)
        time.sleep(1.2)
        try:
            var_app.driver.swipe(420, 200, 420, 1350, 300)
        except:
            pass

    time.sleep(0.5)
    try:
        var_app.driver.find_element(By.XPATH, var_app.CLEAR_ALL).click()
    except:
        var_app.driver.press_keycode(4)
    time.sleep(1.5)
    print("Đã đóng app")




def fake_ip():
    from faker import Faker
    from faker.providers import internet
    fake = Faker()
    fake.add_provider(internet)
    print(fake.ipv4_private())





def timerun():
    while True:
        time.sleep(3)
        timerun = time.strftime("%H:%M:%S", time.localtime())
        print("Thời gian hiện tại:", timerun)
        print("Thời gian chạy tool:", var_app.timerun)
        writeData1(var_app.path_luutamthoi, "Sheet1", 57, 2, timerun)
        if var_app.timerun == "":
            writeData1(var_app.path_luutamthoi, "Sheet1", 57, 2, timerun)
        else:
            writeData1(var_app.path_luutamthoi, "Sheet1", 57, 2, var_app.timerun)


        if var_app.timerun == time.strftime("%H:%M", time.localtime()):
            break
        if var_app.timerun == "":
            break





def clearData(file,sheetName,ketqua, tenanh, data):
    wordbook = openpyxl.load_workbook(file)
    sheet = wordbook.get_sheet_by_name(sheetName)
    i = 9
    while (i < 1000):
        i += 1
        i = str(i)
        sheet["H"+i] = ketqua
        sheet["I"+i] = tenanh
        sheet["K"+i] = data
        i = int(i)
    wordbook.save(file)


def clearData_luutamthoi(file,sheetName,overview, detail, api):
    wordbook = openpyxl.load_workbook(file)
    sheet = wordbook.get_sheet_by_name(sheetName)
    i = 1
    while (i < 300):
        i += 1
        i = str(i)
        sheet["B"+i] = overview
        sheet["C"+i] = detail
        sheet["D"+i] = api
        i = int(i)
    wordbook.save(file)






def readData(file,sheetName,rownum,columnno):
    wordbook = openpyxl.load_workbook(file)
    sheet = wordbook.get_sheet_by_name(sheetName)
    return sheet.cell(row=rownum,column=columnno).value




def writeData(file,sheetName,caseid,columnno,data):
    wordbook = openpyxl.load_workbook(file)
    sheet = wordbook.get_sheet_by_name(sheetName)
    i = 0
    while (i < 5000):
        i += 1
        i = str(i)
        if sheet["A"+i].value == caseid:
            i = int(i)
            sheet.cell(row=i, column=columnno).value = data
            break
        i = int(i)
    wordbook.save(file)




def writeData1(file,sheetName,rowum,columnno,data):
    wordbook = openpyxl.load_workbook(file)
    sheet = wordbook.get_sheet_by_name(sheetName)
    sheet.cell(row=rowum,column=columnno).value = data
    wordbook.save(file)




def notification_telegram():
    from DrissionPage import ChromiumPage, ChromiumOptions
    do1 = ChromiumOptions().set_paths(local_port=9201, user_data_path=r""+var_app.uploadpath+"Profile 30""")
    driver2 = ChromiumPage(addr_or_opts=do1)

    wordbook = openpyxl.load_workbook(var_app.checklistpath)
    sheet = wordbook.get_sheet_by_name("Checklist")
    case_pass = 0
    case_fail = 0
    rownum = 9
    while (rownum < 1000):
        rownum += 1
        rownum = str(rownum)
        if sheet["H"+rownum].value == "Pass":
            case_pass = case_pass+1
        if sheet["H"+rownum].value == "Fail":
            case_fail = case_fail+1
        rownum = int(rownum)
    print("số lượng case Pass", case_pass)
    print("số lượng case Fail", case_fail)
    thoigianbatdauchay = str(readData(var_app.path_luutamthoi , 'Sheet1', 47, 2))

    if case_fail >= 1:
        driver2.get("https://web.telegram.org/a/#-4248738484")
        time.sleep(2)
        case_pass = str(case_pass)
        case_fail = str(case_fail)
        driver2.ele(var_app.hopthoai).click()
        time.sleep(0.5)
        time_string1 = time.strftime("%m/%d/%Y, ", time.localtime())
        time_string1 = str(time_string1)
        time_string2 = time.strftime("%H:%M", time.localtime())
        time_string2 = str(time_string2)
        driver2.ele(var_app.hopthoai_input).input("- DateTest : "+time_string1+""+thoigianbatdauchay+" - "+time_string2+
                                                  "\n- ModeTest: " + var_app.modetest+
                                                  "\n- Số case Pass: " + case_pass+
                                                  "\n- Số case False: "+ case_fail)
        driver2.ele(var_app.hopthoai_input).input(Keys.ENTER)
        time.sleep(1)
        driver2.ele(var_app.hopthoai_iconlink).click()
        time.sleep(1)
        driver2.ele(var_app.hopthoai_iconlink_file).click()
        time.sleep(1)
        subprocess.Popen(var_app.uploadpath+"GPS_APPChecklistForAutoTest.exe")
        time.sleep(2)
        driver2.ele(var_app.hopthoai_send).click()
        time.sleep(2)
        driver2.ele(var_app.hopthoai_iconlink).click()
        time.sleep(1)
        driver2.ele(var_app.hopthoai_iconlink_file).click()
        time.sleep(2)
        subprocess.Popen(var_app.uploadpath+"bagps_app.exe")
        time.sleep(2)
        driver2.ele(var_app.hopthoai_send).click()
        time.sleep(1)




def delete_image():
    path = os.path.join(var_app.imagepath)
    l = os.listdir(path)
    print(l)
    for i in l:
        print(os.path.join(path, i))
        os.remove(os.path.join(path, i))




def get_datachecklist(ma):
    wordbook = openpyxl.load_workbook(var_app.checklistpath)
    sheet = wordbook.get_sheet_by_name("Checklist")
    rownum = 9
    while (rownum < 3000):
        rownum += 1
        rownum = str(rownum)
        if sheet["A" + rownum].value == ma:
            tensukien = sheet["B" + rownum].value
            ketqua = sheet["C" + rownum].value
            print(tensukien)
            print(ketqua)
            writeData1(var_app.path_luutamthoi, "Sheet1", 42, 2, tensukien)
            writeData1(var_app.path_luutamthoi, "Sheet1", 43, 2, ketqua)
        rownum = int(rownum)



def write_caseif():
    n = 0
    while (n < 36):
        var_app.driver.implicitly_wait(1)
        n += 1
        n = str(n)
        print("try:\n   if case == 'Utilities"+n+"':\n       caseid_app.caseid_utilities"+n+"(self)\nexcept:\n    module_other_app.close_app()")
        n = int(n)




def write_caseif1():
    n = 1
    while (n < 36):
        var_app.driver.implicitly_wait(1)
        n += 1
        n = str(n)
        print("try:\n   caseid_app.caseid_utilities"+n+"(self)\nexcept:\n     module_other_app.close_app()")
        n = int(n)
        



def write_caseif2():
    n = 84
    while (n < 155):
        var_app.driver.implicitly_wait(1)
        n += 1
        n = str(n)
        print("caseid_app.caseid_minitor"+n+"(self='""')")
        n = int(n)
#caseid_app.caseid_minitor83(self="")


def write_result_text_try_if(code, eventname, result, path_module, path_text, check_result, name_image):
    var_app.logging.info("--------------")
    var_app.logging.info(path_module)
    var_app.logging.info("Mã - " + code)
    var_app.logging.info("Tên sự kiện - " + eventname)
    var_app.logging.info("Kết quả - " + result)
    try:
        check_text = var_app.driver.find_element(By.XPATH, path_text).text
        writeData(var_app.checklistpath, "Checklist", code, 11, check_text)
        var_app.logging.info(check_text)
        if check_text == check_result:
            var_app.logging.info("True")
            writeData(var_app.checklistpath, "Checklist", code, 8, "Pass")
        else:
            var_app.logging.info("False")
            var_app.driver.save_screenshot(var_app.imagepath + code + name_image)
            writeData(var_app.checklistpath, "Checklist", code, 8, "Fail")
            writeData(var_app.checklistpath, "Checklist", code, 9, code + name_image)
    except:
        var_app.logging.info("False")
        var_app.driver.save_screenshot(var_app.imagepath + code + name_image)
        writeData(var_app.checklistpath, "Checklist", code, 8, "Fail")
        writeData(var_app.checklistpath, "Checklist", code, 9, code + name_image)
    # write_result_text_try_if(code, eventname, result, "Quản trị - Danh sách xe",
    #                                       var_app.check_open_car_quickly, "Mở xe thành công", "_QuanTri_DsXe_MoXeNhanh.png")



def write_result_text_try_if_other(code, eventname, result, path_module, path_text, check_result, name_image):
    var_app.logging.info("--------------")
    var_app.logging.info(path_module)
    var_app.logging.info("Mã - " + code)
    var_app.logging.info("Tên sự kiện - " + eventname)
    var_app.logging.info("Kết quả - " + result)
    try:
        check_text = var_app.driver.find_element(By.XPATH, path_text).text
        writeData(var_app.checklistpath, "Checklist", code, 11, check_text)
        var_app.logging.info(check_text)
        if check_text != check_result:
            var_app.logging.info("True")
            writeData(var_app.checklistpath, "Checklist", code, 8, "Pass")
        else:
            var_app.logging.info("False")
            var_app.driver.save_screenshot(var_app.imagepath + code + name_image)
            writeData(var_app.checklistpath, "Checklist", code, 8, "Fail")
            writeData(var_app.checklistpath, "Checklist", code, 9, code + name_image)
    except:
        var_app.logging.info("False")
        var_app.driver.save_screenshot(var_app.imagepath + code + name_image)
        writeData(var_app.checklistpath, "Checklist", code, 8, "Fail")
        writeData(var_app.checklistpath, "Checklist", code, 9, code + name_image)
    # write_result_text_try_if_other(code, eventname, result, "Quản trị - Danh sách xe",
    #                                       var_app.check_open_car_quickly, "None", "_QuanTri_DsXe_MoXeNhanh.png")








def write_result_displayed_try(code, eventname, result, path_module, path_text, name_image):
    var_app.logging.info("--------------")
    var_app.logging.info(path_module)
    var_app.logging.info("Mã - " + code)
    var_app.logging.info("Tên sự kiện - " + eventname)
    var_app.logging.info("Kết quả - " + result)
    try:
        var_app.driver.find_element(By.XPATH, path_text).is_displayed()
        var_app.logging.info("True")
        writeData(var_app.checklistpath, "Checklist", code, 8, "Pass")
    except NoSuchElementException:
        var_app.logging.info("False")
        var_app.driver.save_screenshot(var_app.imagepath + code + name_image)
        writeData(var_app.checklistpath, "Checklist", code, 8, "Fail")
        writeData(var_app.checklistpath, "Checklist", code, 9, code + name_image)

    # logging.info("Tìm biển kiểm soát - " + data['quantri']['bienkiemsoat'])
    # chucnangkhac.write_result_displayed_try(code, eventname, result, "Quản trị - Danh sách xe",
    #                                         var_app.check_hide_car, "_QuanTri_DsXe_AnXe.png")



def write_result_not_displayed_try(code, eventname, result, path_module, path_text, name_image):
    var_app.driver.implicitly_wait(2)
    var_app.logging.info("--------------")
    var_app.logging.info(path_module)
    var_app.logging.info("Mã - " + code)
    var_app.logging.info("Tên sự kiện - " + eventname)
    var_app.logging.info("Kết quả - " + result)
    try:
        check_not_displayed = var_app.driver.find_element(By.XPATH, path_text).is_displayed()
        var_app.logging.info("False")
        var_app.driver.save_screenshot(var_app.imagepath + code + name_image)
        writeData(var_app.checklistpath, "Checklist", code, 8, "Fail")
        writeData(var_app.checklistpath, "Checklist", code, 9, code + name_image)
    except NoSuchElementException:
        var_app.logging.info("True")
        writeData(var_app.checklistpath, "Checklist", code, 8, "Pass")
    # chucnangkhac.write_result_displayed_try(code, eventname, result, "Quản trị - Danh sách xe",
    #                                         var_app.check_hide_car, "_QuanTri_DsXe_AnXe.png")

        
        
        
def write_result_excelreport(code, sheet, column, name_sheet, number_column, number_row, output):
    if str(sheet[column + number_column]) == "<Cell '"+name_sheet+"'." + number_row + ">":
        var_app.logging.info("Check vị trí "+number_row+":  "+output+"")
        if str(sheet[column + number_column].value) == output:
            var_app.logging.info("True")
            writeData(var_app.checklistpath, "Checklist", code, 8, "Pass")
        else:
            var_app.logging.info("False")
            writeData(var_app.checklistpath, "Checklist", code, 8, "Fail")
            writeData(var_app.checklistpath, "Checklist", code, 12, "File Báo cáo tổng hợp hoạt động sai ô " + number_row)
    # chucnangkhac.write_result_excelreport(code, sheet, column, 'BC Tổng hợp', "5", "C5", "STT")



def write_result_excelreport_clear_data(code, sheet, column, name_sheet, number_column, number_row, output):
    if str(sheet[column + number_column]) == "<Cell '"+name_sheet+"'." + number_row + ">":
        var_app.logging.info("Check vị trí "+number_row+": "+output+"")
        if str(sheet[column + number_column].value) == output:
            var_app.logging.info("True")
            writeData(var_app.checklistpath, "Checklist", code, 12, " ")
            writeData(var_app.checklistpath, "Checklist", code, 8, "Pass")
        else:
            var_app.logging.info("False")
            writeData(var_app.checklistpath, "Checklist", code, 8, "Fail")
            writeData(var_app.checklistpath, "Checklist", code, 12, "File Báo cáo tổng hợp hoạt động sai ô " + number_row)
    # chucnangkhac.write_result_excelreport(code, sheet, column, 'BC Tổng hợp', "5", "C5", "STT")

        


