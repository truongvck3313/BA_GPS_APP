import openpyxl
import var_app
import re
import caseid_app
import module_other_app






def ModuleTest():
    moduletest = ''.join(re.findall(r'\d+', var_app.moduletest))
    print(type(moduletest))
    print(moduletest)
    for i in moduletest:
        print("so", i)
        if i == "0":
            run_all(self='')
        if i == "1":
            login(self='')






#0
def run_all(self):      #Chạy tất cả
    try:
        caseid_app.caseid_login01(self)
    except:
        pass
    try:
        caseid_app.caseid_login02(self)
    except:
        pass
    try:
        caseid_app.caseid_login03(self)
    except:
        pass
    try:
        caseid_app.caseid_login04(self)
    except:
        pass
    try:
        caseid_app.caseid_login05(self)
    except:
        pass
    try:
        caseid_app.caseid_login06(self)
    except:
        pass
    try:
        caseid_app.caseid_login07(self)
    except:
        pass
    try:
        caseid_app.caseid_login08(self)
    except:
        pass
    try:
        caseid_app.caseid_login09(self)
    except:
        pass
    try:
        caseid_app.caseid_login10(self)
    except:
        pass
    try:
        caseid_app.caseid_login11(self)
    except:
        pass
    try:
        caseid_app.caseid_login12(self)
    except:
        pass
    try:
        caseid_app.caseid_login13(self)
    except:
        pass
    try:
        caseid_app.caseid_login14(self)
    except:
        pass
    try:
        caseid_app.caseid_login15(self)
    except:
        pass
    try:
        caseid_app.caseid_login16(self)
    except:
        pass
    try:
        caseid_app.caseid_login17(self)
    except:
        pass
    try:
        caseid_app.caseid_login18(self)
    except:
        pass
    try:
        caseid_app.caseid_login19(self)
    except:
        pass
    try:
        caseid_app.caseid_login20(self)
    except:
        pass




#1 đăng nhập
def login(self):
    list_mucdo1 = []
    list_mucdo2 = []
    list_mucdo3 = []
    list_mucdo4 = []
    wordbook = openpyxl.load_workbook(var_app.checklistpath)
    sheet = wordbook.get_sheet_by_name("Checklist")
    rownum = 10
    while (rownum < 36):
        rownum += 1
        rownum = str(rownum)
        if sheet["D"+rownum].value == "x":
            muc1 = sheet["A"+rownum].value
            list_mucdo1.append(muc1)
        if sheet["E"+rownum].value == "x":
            muc2 = sheet["A"+rownum].value
            list_mucdo2.append(muc2)
        if sheet["F"+rownum].value == "x":
            muc3 = sheet["A"+rownum].value
            list_mucdo3.append(muc3)
        if sheet["G"+rownum].value == "x":
            muc4 = sheet["A"+rownum].value
            list_mucdo4.append(muc4)
        rownum = int(rownum)
    print(list_mucdo2)

    modetest = ''.join(re.findall(r'\d+', var_app.modetest))
    for i in modetest:
        if i == "1":
            for case in list_mucdo1:
                try:
                    if case == 'Login01':
                        caseid_app.caseid_login01(self)
                except:
                    pass
                try:
                    if case == 'Login02':
                        caseid_app.caseid_login02(self)
                except:
                    pass
                try:
                    if case == 'Login03':
                        caseid_app.caseid_login03(self)
                except:
                    pass
                try:
                    if case == 'Login04':
                        caseid_app.caseid_login04(self)
                except:
                    pass
                try:
                    if case == 'Login05':
                        caseid_app.caseid_login05(self)
                except:
                    pass
                try:
                    if case == 'Login06':
                        caseid_app.caseid_login06(self)
                except:
                    pass
                try:
                    if case == 'Login07':
                        caseid_app.caseid_login07(self)
                except:
                    pass
                try:
                    if case == 'Login08':
                        caseid_app.caseid_login08(self)
                except:
                    pass
                try:
                    if case == 'Login09':
                        caseid_app.caseid_login09(self)
                except:
                    pass
                try:
                    if case == 'Login10':
                        caseid_app.caseid_login09(self)
                except:
                    pass
                try:
                    if case == 'Login11':
                        caseid_app.caseid_login09(self)
                except:
                    pass
                try:
                    if case == 'Login12':
                        caseid_app.caseid_login09(self)
                except:
                    pass
                try:
                    if case == 'Login13':
                        caseid_app.caseid_login09(self)
                except:
                    pass
                try:
                    if case == 'Login14':
                        caseid_app.caseid_login09(self)
                except:
                    pass
                try:
                    if case == 'Login15':
                        caseid_app.caseid_login09(self)
                except:
                    pass
                try:
                    if case == 'Login16':
                        caseid_app.caseid_login09(self)
                except:
                    pass
                try:
                    if case == 'Login17':
                        caseid_app.caseid_login09(self)
                except:
                    pass
                try:
                    if case == 'Login18':
                        caseid_app.caseid_login09(self)
                except:
                    pass
                try:
                    if case == 'Login19':
                        caseid_app.caseid_login09(self)
                except:
                    pass
                try:
                    if case == 'Login20':
                        caseid_app.caseid_login09(self)
                except:
                    pass


        if i == "2":
            for case in list_mucdo2:
                try:
                    if case == 'Login01':
                        caseid_app.caseid_login01(self)
                except:
                    pass
                try:
                    if case == 'Login02':
                        caseid_app.caseid_login02(self)
                except:
                    pass
                try:
                    if case == 'Login03':
                        caseid_app.caseid_login03(self)
                except:
                    pass
                try:
                    if case == 'Login04':
                        caseid_app.caseid_login04(self)
                except:
                    pass
                try:
                    if case == 'Login05':
                        caseid_app.caseid_login05(self)
                except:
                    pass
                try:
                    if case == 'Login06':
                        caseid_app.caseid_login06(self)
                except:
                    pass
                try:
                    if case == 'Login07':
                        caseid_app.caseid_login07(self)
                except:
                    pass
                try:
                    if case == 'Login08':
                        caseid_app.caseid_login08(self)
                except:
                    pass
                try:
                    if case == 'Login09':
                        caseid_app.caseid_login09(self)
                except:
                    pass
                try:
                    if case == 'Login10':
                        caseid_app.caseid_login09(self)
                except:
                    pass
                try:
                    if case == 'Login11':
                        caseid_app.caseid_login09(self)
                except:
                    pass
                try:
                    if case == 'Login12':
                        caseid_app.caseid_login09(self)
                except:
                    pass
                try:
                    if case == 'Login13':
                        caseid_app.caseid_login09(self)
                except:
                    pass
                try:
                    if case == 'Login14':
                        caseid_app.caseid_login09(self)
                except:
                    pass
                try:
                    if case == 'Login15':
                        caseid_app.caseid_login09(self)
                except:
                    pass
                try:
                    if case == 'Login16':
                        caseid_app.caseid_login09(self)
                except:
                    pass
                try:
                    if case == 'Login17':
                        caseid_app.caseid_login09(self)
                except:
                    pass
                try:
                    if case == 'Login18':
                        caseid_app.caseid_login09(self)
                except:
                    pass
                try:
                    if case == 'Login19':
                        caseid_app.caseid_login09(self)
                except:
                    pass
                try:
                    if case == 'Login20':
                        caseid_app.caseid_login09(self)
                except:
                    pass


        if i == "3":
            for case in list_mucdo3:
                try:
                    if case == 'Login01':
                        caseid_app.caseid_login01(self)
                except:
                    pass
                try:
                    if case == 'Login02':
                        caseid_app.caseid_login02(self)
                except:
                    pass
                try:
                    if case == 'Login03':
                        caseid_app.caseid_login03(self)
                except:
                    pass
                try:
                    if case == 'Login04':
                        caseid_app.caseid_login04(self)
                except:
                    pass
                try:
                    if case == 'Login05':
                        caseid_app.caseid_login05(self)
                except:
                    pass
                try:
                    if case == 'Login06':
                        caseid_app.caseid_login06(self)
                except:
                    pass
                try:
                    if case == 'Login07':
                        caseid_app.caseid_login07(self)
                except:
                    pass
                try:
                    if case == 'Login08':
                        caseid_app.caseid_login08(self)
                except:
                    pass
                try:
                    if case == 'Login09':
                        caseid_app.caseid_login09(self)
                except:
                    pass
                try:
                    if case == 'Login10':
                        caseid_app.caseid_login09(self)
                except:
                    pass
                try:
                    if case == 'Login11':
                        caseid_app.caseid_login09(self)
                except:
                    pass
                try:
                    if case == 'Login12':
                        caseid_app.caseid_login09(self)
                except:
                    pass
                try:
                    if case == 'Login13':
                        caseid_app.caseid_login09(self)
                except:
                    pass
                try:
                    if case == 'Login14':
                        caseid_app.caseid_login09(self)
                except:
                    pass
                try:
                    if case == 'Login15':
                        caseid_app.caseid_login09(self)
                except:
                    pass
                try:
                    if case == 'Login16':
                        caseid_app.caseid_login09(self)
                except:
                    pass
                try:
                    if case == 'Login17':
                        caseid_app.caseid_login09(self)
                except:
                    pass
                try:
                    if case == 'Login18':
                        caseid_app.caseid_login09(self)
                except:
                    pass
                try:
                    if case == 'Login19':
                        caseid_app.caseid_login09(self)
                except:
                    pass
                try:
                    if case == 'Login20':
                        caseid_app.caseid_login09(self)
                except:
                    pass


        if i == "4":
            for case in list_mucdo4:
                try:
                    if case == 'Login01':
                        caseid_app.caseid_login01(self)
                except:
                    pass
                try:
                    if case == 'Login02':
                        caseid_app.caseid_login02(self)
                except:
                    pass
                try:
                    if case == 'Login03':
                        caseid_app.caseid_login03(self)
                except:
                    pass
                try:
                    if case == 'Login04':
                        caseid_app.caseid_login04(self)
                except:
                    pass
                try:
                    if case == 'Login05':
                        caseid_app.caseid_login05(self)
                except:
                    pass
                try:
                    if case == 'Login06':
                        caseid_app.caseid_login06(self)
                except:
                    pass
                try:
                    if case == 'Login07':
                        caseid_app.caseid_login07(self)
                except:
                    pass
                try:
                    if case == 'Login08':
                        caseid_app.caseid_login08(self)
                except:
                    pass
                try:
                    if case == 'Login09':
                        caseid_app.caseid_login09(self)
                except:
                    pass
                try:
                    if case == 'Login10':
                        caseid_app.caseid_login09(self)
                except:
                    pass
                try:
                    if case == 'Login11':
                        caseid_app.caseid_login09(self)
                except:
                    pass
                try:
                    if case == 'Login12':
                        caseid_app.caseid_login09(self)
                except:
                    pass
                try:
                    if case == 'Login13':
                        caseid_app.caseid_login09(self)
                except:
                    pass
                try:
                    if case == 'Login14':
                        caseid_app.caseid_login09(self)
                except:
                    pass
                try:
                    if case == 'Login15':
                        caseid_app.caseid_login09(self)
                except:
                    pass
                try:
                    if case == 'Login16':
                        caseid_app.caseid_login09(self)
                except:
                    pass
                try:
                    if case == 'Login17':
                        caseid_app.caseid_login09(self)
                except:
                    pass
                try:
                    if case == 'Login18':
                        caseid_app.caseid_login09(self)
                except:
                    pass
                try:
                    if case == 'Login19':
                        caseid_app.caseid_login09(self)
                except:
                    pass
                try:
                    if case == 'Login20':
                        caseid_app.caseid_login09(self)
                except:
                    pass

