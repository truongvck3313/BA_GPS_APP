import minitor_app
import var_app
import unittest
import caseid_app
import module_other_app
import module_gps_appv3
import route





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

        #Đăng nhập
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
        # #Giám sát
        # caseid_app.caseid_minitor01(self="")
        # caseid_app.caseid_minitor02(self="")
        # caseid_app.caseid_minitor03(self="")
        #
        # caseid_app.caseid_minitor04(self="")
        # caseid_app.caseid_minitor05(self="")
        # caseid_app.caseid_minitor06(self="")
        # caseid_app.caseid_minitor07(self="")
        # caseid_app.caseid_minitor08(self="")
        # caseid_app.caseid_minitor09(self="")
        # caseid_app.caseid_minitor10(self="")
        # caseid_app.caseid_minitor11(self="")
        # caseid_app.caseid_minitor12(self="")
        # caseid_app.caseid_minitor13(self="")
        # caseid_app.caseid_minitor14(self="")
        # caseid_app.caseid_minitor15(self="")
        # caseid_app.caseid_minitor16(self="")
        # caseid_app.caseid_minitor17(self="")
        # caseid_app.caseid_minitor18(self="")
        # caseid_app.caseid_minitor19(self="")
        # caseid_app.caseid_minitor20(self="")
        # caseid_app.caseid_minitor21(self="")
        # caseid_app.caseid_minitor22(self="")
        # caseid_app.caseid_minitor23(self="")
        # caseid_app.caseid_minitor24(self="")
        # caseid_app.caseid_minitor25(self="")
        # caseid_app.caseid_minitor26(self="")
        # caseid_app.caseid_minitor27(self="")
        # caseid_app.caseid_minitor28(self="")
        # caseid_app.caseid_minitor29(self="")
        # caseid_app.caseid_minitor30(self="")
        # caseid_app.caseid_minitor31(self="")
        # caseid_app.caseid_minitor32(self="")
        # caseid_app.caseid_minitor33(self="")
        # caseid_app.caseid_minitor34(self="")
        # caseid_app.caseid_minitor35(self="")
        # caseid_app.caseid_minitor36(self="")
        # caseid_app.caseid_minitor37(self="")
        # caseid_app.caseid_minitor38(self="")
        # caseid_app.caseid_minitor39(self="")
        # caseid_app.caseid_minitor40(self="")
        # caseid_app.caseid_minitor41(self="")
        # caseid_app.caseid_minitor42(self="")
        # caseid_app.caseid_minitor43(self="")
        # caseid_app.caseid_minitor44(self="")
        # caseid_app.caseid_minitor45(self="")
        # caseid_app.caseid_minitor46(self="")
        # caseid_app.caseid_minitor47(self="")
        # caseid_app.caseid_minitor48(self="")
        # caseid_app.caseid_minitor49(self="")
        # caseid_app.caseid_minitor50(self="")
        # caseid_app.caseid_minitor51(self="")
        # caseid_app.caseid_minitor52(self="")
        # caseid_app.caseid_minitor53(self="")
        # caseid_app.caseid_minitor54(self="")
        # caseid_app.caseid_minitor55(self="")
        # caseid_app.caseid_minitor56(self="")
        # caseid_app.caseid_minitor57(self="")
        # caseid_app.caseid_minitor58(self="")
        # caseid_app.caseid_minitor59(self="")
        # caseid_app.caseid_minitor60(self="")
        # caseid_app.caseid_minitor61(self="")
        # caseid_app.caseid_minitor62(self="")
        # caseid_app.caseid_minitor63(self="")
        # caseid_app.caseid_minitor64(self="")
        # caseid_app.caseid_minitor65(self="")
        # caseid_app.caseid_minitor66(self="")
        # caseid_app.caseid_minitor67(self="")
        # caseid_app.caseid_minitor68(self="")
        # caseid_app.caseid_minitor69(self="")
        # caseid_app.caseid_minitor70(self="")
        # caseid_app.caseid_minitor71(self="")
        # caseid_app.caseid_minitor72(self="")
        # caseid_app.caseid_minitor73(self="")
        # caseid_app.caseid_minitor74(self="")
        # caseid_app.caseid_minitor75(self="")
        # caseid_app.caseid_minitor76(self="")
        # caseid_app.caseid_minitor77(self="")
        # caseid_app.caseid_minitor78(self="")
        # caseid_app.caseid_minitor79(self="")
        # caseid_app.caseid_minitor80(self="")
        # caseid_app.caseid_minitor81(self="")
        # caseid_app.caseid_minitor82(self="")
        # caseid_app.caseid_minitor83(self="")
        #
        # caseid_app.caseid_minitor84(self="")
        # caseid_app.caseid_minitor85(self='')
        # caseid_app.caseid_minitor86(self='')
        #
        # caseid_app.caseid_minitor87(self='')
        # caseid_app.caseid_minitor88(self='')
        # caseid_app.caseid_minitor89(self='')
        # caseid_app.caseid_minitor90(self='')
        # caseid_app.caseid_minitor91(self='')
        # caseid_app.caseid_minitor92(self='')
        # caseid_app.caseid_minitor93(self='')
        # caseid_app.caseid_minitor94(self='')
        # caseid_app.caseid_minitor95(self='')
        # caseid_app.caseid_minitor96(self='')
        # caseid_app.caseid_minitor97(self='')
        # caseid_app.caseid_minitor98(self='')
        # caseid_app.caseid_minitor99(self='')
        # caseid_app.caseid_minitor100(self='')
        # caseid_app.caseid_minitor101(self='')
        # caseid_app.caseid_minitor102(self='')
        # caseid_app.caseid_minitor103(self='')
        # caseid_app.caseid_minitor104(self='')
        # caseid_app.caseid_minitor105(self='')
        # caseid_app.caseid_minitor106(self='')
        # caseid_app.caseid_minitor107(self='')
        # caseid_app.caseid_minitor108(self='')
        # caseid_app.caseid_minitor109(self='')
        # caseid_app.caseid_minitor110(self='')
        # caseid_app.caseid_minitor111(self='')
        # caseid_app.caseid_minitor112(self='')
        # caseid_app.caseid_minitor113(self='')
        # caseid_app.caseid_minitor114(self='')
        # caseid_app.caseid_minitor115(self='')
        # caseid_app.caseid_minitor116(self='')
        # caseid_app.caseid_minitor117(self='')
        # caseid_app.caseid_minitor118(self='')
        # caseid_app.caseid_minitor119(self='')
        # caseid_app.caseid_minitor120(self='')
        # caseid_app.caseid_minitor121(self='')
        # caseid_app.caseid_minitor122(self='')
        # caseid_app.caseid_minitor123(self='')
        #
        # caseid_app.caseid_minitor124(self='')
        # caseid_app.caseid_minitor125(self='')
        # caseid_app.caseid_minitor126(self='')
        # caseid_app.caseid_minitor127(self='')
        # caseid_app.caseid_minitor128(self='')
        # caseid_app.caseid_minitor129(self='')
        # caseid_app.caseid_minitor130(self='')
        # caseid_app.caseid_minitor131(self='')
        # caseid_app.caseid_minitor132(self='')
        # caseid_app.caseid_minitor133(self='')
        # caseid_app.caseid_minitor134(self='')
        # caseid_app.caseid_minitor135(self='')
        # caseid_app.caseid_minitor136(self='')
        # caseid_app.caseid_minitor137(self='')
        # caseid_app.caseid_minitor138(self='')
        # caseid_app.caseid_minitor139(self='')
        # caseid_app.caseid_minitor140(self='')
        # caseid_app.caseid_minitor141(self='')
        # caseid_app.caseid_minitor142(self='')
        # caseid_app.caseid_minitor143(self='')
        # caseid_app.caseid_minitor144(self='')
        # caseid_app.caseid_minitor145(self='')
        # caseid_app.caseid_minitor146(self='')
        # caseid_app.caseid_minitor147(self='')
        # caseid_app.caseid_minitor148(self='')
        # caseid_app.caseid_minitor149(self='')
        # caseid_app.caseid_minitor150(self='')
        # caseid_app.caseid_minitor151(self='')
        # caseid_app.caseid_minitor152(self='')
        # caseid_app.caseid_minitor153(self='')
        # caseid_app.caseid_minitor154(self='')
        #
        #
        caseid_app.caseid_route01(self="")
        caseid_app.caseid_route02(self="")
        caseid_app.caseid_route03(self="")
        caseid_app.caseid_route04(self="")
        caseid_app.caseid_route05(self="")
        caseid_app.caseid_route06(self="")

        caseid_app.caseid_route07(self="")
        caseid_app.caseid_route08(self="")
        caseid_app.caseid_route09(self="")
        caseid_app.caseid_route10(self="")
        caseid_app.caseid_route11(self="")



if __name__ == "__main__":
    unittest.main()








