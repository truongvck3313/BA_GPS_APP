import minitor_app
import var_app
import unittest
import caseid_app
import module_other_app
import module_gps_appv3






#adb devices
#adb shell dumpsys window | find "mCurrentFocus"
#pip install selenium==4.21.0

# module_other_app.timerun()




class Test(unittest.TestCase):
    def test_run(self):
        module_other_app.clearData(var_app.checklistpath, "Checklist", "", "")
        module_other_app.clear_log()
        module_other_app.delete_image()
        # module_gps_appv3.ModuleTest()
        # module_other_app.notification_telegram()


        # #Đăng nhập
        # caseid_app.caseid_login01(self="")
        # caseid_app.caseid_login02(self="")
        # caseid_app.caseid_login03(self="")
        # caseid_app.caseid_login04(self="")
        # caseid_app.caseid_login05(self="")
        # caseid_app.caseid_login06(self="")
        # caseid_app.caseid_login07(self="")
        # caseid_app.caseid_login08(self="")
        # caseid_app.caseid_login09(self="")
        #
        # caseid_app.caseid_login10(self="")
        # caseid_app.caseid_login11(self="")
        # caseid_app.caseid_login12(self="")
        # caseid_app.caseid_login13(self="")
        # caseid_app.caseid_login14(self="")
        # caseid_app.caseid_login15(self="")
        # caseid_app.caseid_login16(self="")
        # caseid_app.caseid_login17(self="")
        # caseid_app.caseid_login18(self="")
        # caseid_app.caseid_login19(self="")
        # caseid_app.caseid_login20(self="")
        #
        #
        #Giám sát
        caseid_app.caseid_minitor01(self="")
        caseid_app.caseid_minitor02(self="")
        caseid_app.caseid_minitor03(self="")

        caseid_app.caseid_minitor04(self="")
        caseid_app.caseid_minitor05(self="")
        caseid_app.caseid_minitor06(self="")
        caseid_app.caseid_minitor07(self="")
        caseid_app.caseid_minitor08(self="")
        caseid_app.caseid_minitor09(self="")
        caseid_app.caseid_minitor10(self="")
        caseid_app.caseid_minitor11(self="")
        caseid_app.caseid_minitor12(self="")
        caseid_app.caseid_minitor13(self="")

        caseid_app.caseid_minitor14(self="")
        caseid_app.caseid_minitor15(self="")
        caseid_app.caseid_minitor16(self="")
        caseid_app.caseid_minitor17(self="")
        caseid_app.caseid_minitor18(self="")
        caseid_app.caseid_minitor19(self="")
        caseid_app.caseid_minitor20(self="")
        caseid_app.caseid_minitor21(self="")
        caseid_app.caseid_minitor22(self="")
        caseid_app.caseid_minitor23(self="")
        caseid_app.caseid_minitor24(self="")
        caseid_app.caseid_minitor25(self="")
        caseid_app.caseid_minitor26(self="")
        caseid_app.caseid_minitor27(self="")
        caseid_app.caseid_minitor28(self="")
        caseid_app.caseid_minitor29(self="")
        caseid_app.caseid_minitor30(self="")
        caseid_app.caseid_minitor31(self="")
        caseid_app.caseid_minitor32(self="")
        caseid_app.caseid_minitor33(self="")
        caseid_app.caseid_minitor34(self="")
        caseid_app.caseid_minitor35(self="")
        caseid_app.caseid_minitor36(self="")
        caseid_app.caseid_minitor37(self="")
        caseid_app.caseid_minitor38(self="")
        caseid_app.caseid_minitor39(self="")
        caseid_app.caseid_minitor40(self="")
        caseid_app.caseid_minitor41(self="")
        caseid_app.caseid_minitor42(self="")
        caseid_app.caseid_minitor43(self="")
        caseid_app.caseid_minitor44(self="")
        caseid_app.caseid_minitor45(self="")
        caseid_app.caseid_minitor46(self="")
        caseid_app.caseid_minitor47(self="")
        caseid_app.caseid_minitor48(self="")
        caseid_app.caseid_minitor49(self="")
        caseid_app.caseid_minitor50(self="")
        caseid_app.caseid_minitor51(self="")
        caseid_app.caseid_minitor52(self="")
        caseid_app.caseid_minitor53(self="")



if __name__ == "__main__":
    unittest.main()








