import login_app
import module_other_app
import route
import vehicle
import var_app
import minitor_app
import time
from appium.webdriver.common.appiumby import AppiumBy



import vehicle


def caseid_login01(self):
    module_other_app.get_datachecklist("Login01")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    login_app.login.login(self, "ungroup", "12341234",
                          "Login01", eventname, result,
                          var_app.check_customer_account1, "Tìm kiếm phương tiện", "_DangNhap_TKKhachHangCoQuyenGiamSat.png")



def caseid_login02(self):
    module_other_app.get_datachecklist("Login02")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    login_app.login.login(self, "truongtq@bagroup.vn", "atgmj123",
                          "Login02", eventname, result,
                          var_app.check_customer_account1, "Tìm kiếm phương tiện", "_DangNhap_TKBinhAnh.png")



def caseid_login03(self):
    module_other_app.get_datachecklist("Login03")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    login_app.login.login(self, "43E02740", "12341234",
                          "Login03", eventname, result,
                          var_app.check_customer_account1, "Tìm kiếm phương tiện", "_DangNhap_TKDaiLy.png")



def caseid_login04(self):
    module_other_app.get_datachecklist("Login04")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    login_app.login.login(self, "truongvck1", "12341234",
                          "Login04", eventname, result,
                          var_app.check_customer_account1, "", "")




def caseid_login05(self):
    module_other_app.get_datachecklist("Login05")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    login_app.login.login_wrong(self, "truongtq@bagroup.vn", "11111", "Login05", eventname, result)




def caseid_login06(self):
    module_other_app.get_datachecklist("Login06")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    login_app.login.forger_user(self, "Login06", eventname, result)




def caseid_login07(self):
    module_other_app.get_datachecklist("Login07")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    login_app.login.forger_password(self, "Login07", eventname, result)




def caseid_login08(self):
    module_other_app.get_datachecklist("Login08")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    login_app.login.remember_login(self, "Login08", eventname, result,
                                   "true", "false", "_DangNhap_BoGhiNhoDangNhap.png")



def caseid_login09(self):
    module_other_app.get_datachecklist("Login09")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    login_app.login.remember_login(self, "Login09", eventname, result,
                                   "false", "true", "_DangNhap_GhiNhoDangNhap.png")



def caseid_login10(self):
    module_other_app.get_datachecklist("Login10")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    login_app.other_function.change_language(self, "Login10", eventname, result,
                          var_app.change_language_english, var_app.check_change_language_english, "Username", "_DangNhap_DoiNgonNgu_English.png")


def caseid_login11(self):
    module_other_app.get_datachecklist("Login11")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    login_app.other_function.change_language(self, "Login11", eventname, result,
                          var_app.change_language_vietnamese, var_app.check_change_language_vietnamese, "Tên đăng nhập", "_DangNhap_DoiNgonNgu_TiengViet.png")




def caseid_login12(self):
    module_other_app.get_datachecklist("Login12")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    login_app.other_function.affiliate_link_outsite(self, "Login12", eventname, result,
                          var_app.affiliate_mail, var_app.check_affiliate_mail, "_DangNhap_LinkLienKet_Email.png")



def caseid_login13(self):
    module_other_app.get_datachecklist("Login13")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    login_app.other_function.affiliate_link_outsite(self, "Login13", eventname, result,
                          var_app.affiliate_bagps, var_app.check_affiliate_bagps, "_DangNhap_LinkLienKet_BAGPS.png")



def caseid_login14(self):
    module_other_app.get_datachecklist("Login14")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    login_app.other_function.affiliate_link_outsite(self, "Login14", eventname, result,
                          var_app.affiliate_register_for_consultation, var_app.check_affiliate_register_for_consultation, "_DangNhap_LinkLienKet_DangKyTuVan.png")


def caseid_login15(self):
    module_other_app.get_datachecklist("Login15")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    login_app.other_function.affiliate_link_insite(self, "Login15", eventname, result,
                          var_app.affiliate_facebook, var_app.check_affiliate_facebook, "https://www.facebook.com/bagps.vn", "_DangNhap_LinkLienKet_FaceBook.png")




def caseid_login16(self):
    module_other_app.get_datachecklist("Login16")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    login_app.other_function.affiliate_link_insite(self, "Login16", eventname, result,
                          var_app.affiliate_zalo, var_app.check_affiliate_zalo, "zalo://zaloapp.com/qr/link/bagpsvn", "_DangNhap_LinkLienKet_Zalo.png")



def caseid_login17(self):
    module_other_app.get_datachecklist("Login17")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    login_app.other_function.affiliate_link_insite(self, "Login17", eventname, result,
                          var_app.affiliate_youtobe, var_app.check_affiliate_youtobe, "@BAGPS", "_DangNhap_LinkLienKet_Youtobe.png")



def caseid_login18(self):
    module_other_app.get_datachecklist("Login18")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    login_app.other_function.affiliate_link_insite(self, "Login18", eventname, result,
                          var_app.affiliate_tiktok, var_app.check_affiliate_tiktok, "https://www.tiktok.com/@bagps", "_DangNhap_LinkLienKet_Tiktok.png")



def caseid_login19(self):
    module_other_app.get_datachecklist("Login19")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    login_app.other_function.affiliate_link_insite(self, "Login19", eventname, result,
                          var_app.affiliate_mangluoi, var_app.check_affiliate_mangluoi, "https://bagps.vn/mang-luoi", "_DangNhap_LinkLienKet_MangLuoi.png")




def caseid_login20(self):
    module_other_app.get_datachecklist("Login20")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    login_app.other_function.affiliate_link_insite(self, "Login20", eventname, result,
                          var_app.affiliate_trainghiembagps, var_app.check_affiliate_trainghiembagps, "@BAGPS", "_DangNhap_LinkLienKet_TraiNghiemBAGPS.png")




def caseid_minitor01(self):
    module_other_app.get_datachecklist("Minitor01")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.search_vehicle(self, "Minitor01", eventname, result)



def caseid_minitor02(self):
    module_other_app.get_datachecklist("Minitor02")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.select_1group(self, "Minitor02", eventname, result)



def caseid_minitor03(self):
    module_other_app.get_datachecklist("Minitor03")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.select_manygroup(self, "Minitor03", eventname, result)


def caseid_minitor04(self):
    module_other_app.get_datachecklist("Minitor04")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor04", eventname, result,
                                        var_app.status_feedebt, var_app.name_feedebt, var_app.quaility_feedebt, "_GiamSat_TrangThai_NoPhi.png")


def caseid_minitor05(self):
    module_other_app.get_datachecklist("Minitor05")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor05", eventname, result,
                                        var_app.status_move, var_app.name_move, var_app.quaility_move, "_GiamSat_TrangThai_DiChuyen.png")


def caseid_minitor06(self):
    module_other_app.get_datachecklist("Minitor06")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor06", eventname, result,
                                        var_app.status_stopparking, var_app.name_stopparking,
                                        var_app.quaility_stopparking, "_GiamSat_TrangThai_DungDo.png")


def caseid_minitor07(self):
    module_other_app.get_datachecklist("Minitor07")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor07", eventname, result,
                                        var_app.status_stop_turning_on, var_app.name_stop_turning_on,
                                        var_app.quaility_stop_turning_on, "_GiamSat_TrangThai_DungBat.png")



def caseid_minitor08(self):
    module_other_app.get_datachecklist("Minitor08")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor08", eventname, result,
                                        var_app.status_turn_on_the_machine, var_app.name_turn_on_the_machine,
                                        var_app.quaility_turn_on_the_machine, "_GiamSat_TrangThai_BatMay.png")



def caseid_minitor09(self):
    module_other_app.get_datachecklist("Minitor09")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor09", eventname, result,
                                        var_app.status_turn_off_the_machine, var_app.name_turn_off_the_machine,
                                        var_app.quaility_turn_of_the_machine, "_GiamSat_TrangThai_TatMay.png")


def caseid_minitor10(self):
    module_other_app.get_datachecklist("Minitor10")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor10", eventname, result,
                                        var_app.status_excessive_speed, var_app.name_excessive_speed,
                                        var_app.quaility_excessive_speed, "_GiamSat_TrangThai_QuaTocDo.png")


def caseid_minitor11(self):
    module_other_app.get_datachecklist("Minitor11")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor11", eventname, result,
                                        var_app.status_lost_gps, var_app.name_lost_gps,
                                        var_app.quaility_lost_gps, "_GiamSat_TrangThai_MatGPS.png")



def caseid_minitor12(self):
    module_other_app.get_datachecklist("Minitor12")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor12", eventname, result,
                                        var_app.status_lost_gms, var_app.name_lost_gms,
                                        var_app.quaility_lost_gms, "_GiamSat_TrangThai_MatGMS.png")



def caseid_minitor13(self):
    module_other_app.get_datachecklist("Minitor13")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor13", eventname, result,
                                        var_app.status_all, var_app.name_all,
                                        var_app.quaility_all, "_GiamSat_TrangThai_Tatca.png")

def caseid_minitor14(self):
    module_other_app.get_datachecklist("Minitor14")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor14", eventname, result,
                                        var_app.status_feedebt, var_app.name_feedebt, var_app.quaility_feedebt, "_GiamSat_TrangThai_NoPhi.png")


def caseid_minitor15(self):
    module_other_app.get_datachecklist("Minitor15")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor15", eventname, result,
                                        var_app.status_move, var_app.name_move, var_app.quaility_move, "_GiamSat_TrangThai_DiChuyen.png")


def caseid_minitor16(self):
    module_other_app.get_datachecklist("Minitor16")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor16", eventname, result,
                                        var_app.status_stopparking, var_app.name_stopparking,
                                        var_app.quaility_stopparking, "_GiamSat_TrangThai_DungDo.png")

def caseid_minitor17(self):
    module_other_app.get_datachecklist("Minitor17")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor17", eventname, result,
                                        var_app.status_stop_turning_on, var_app.name_stop_turning_on,
                                        var_app.quaility_stop_turning_on, "_GiamSat_TrangThai_DungBat.png")

def caseid_minitor18(self):
    module_other_app.get_datachecklist("Minitor18")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor18", eventname, result,
                                        var_app.status_turn_on_the_machine, var_app.name_turn_on_the_machine,
                                        var_app.quaility_turn_on_the_machine, "_GiamSat_TrangThai_BatMay.png")

def caseid_minitor19(self):
    module_other_app.get_datachecklist("Minitor19")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor19", eventname, result,
                                        var_app.status_turn_off_the_machine, var_app.name_turn_off_the_machine,
                                        var_app.quaility_turn_of_the_machine, "_GiamSat_TrangThai_TatMay.png")

def caseid_minitor20(self):
    module_other_app.get_datachecklist("Minitor20")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor20", eventname, result,
                                        var_app.status_excessive_speed, var_app.name_excessive_speed,
                                        var_app.quaility_excessive_speed, "_GiamSat_TrangThai_QuaTocDo.png")

def caseid_minitor21(self):
    module_other_app.get_datachecklist("Minitor21")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor21", eventname, result,
                                        var_app.status_lost_gps, var_app.name_lost_gps,
                                        var_app.quaility_lost_gps, "_GiamSat_TrangThai_MatGPS.png")

def caseid_minitor22(self):
    module_other_app.get_datachecklist("Minitor22")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor22", eventname, result,
                                        var_app.status_lost_gms, var_app.name_lost_gms,
                                        var_app.quaility_lost_gms, "_GiamSat_TrangThai_MatGMS.png")

def caseid_minitor23(self):
    module_other_app.get_datachecklist("Minitor23")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor23", eventname, result,
                                        var_app.status_all, var_app.name_all,
                                        var_app.quaility_all, "_GiamSat_TrangThai_Tatca.png")

def caseid_minitor24(self):
    module_other_app.get_datachecklist("Minitor24")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor24", eventname, result,
                                        var_app.status_feedebt, var_app.name_feedebt, var_app.quaility_feedebt, "_GiamSat_TrangThai_NoPhi.png")


def caseid_minitor25(self):
    module_other_app.get_datachecklist("Minitor25")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor25", eventname, result,
                                        var_app.status_move, var_app.name_move, var_app.quaility_move, "_GiamSat_TrangThai_DiChuyen.png")


def caseid_minitor26(self):
    module_other_app.get_datachecklist("Minitor26")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor26", eventname, result,
                                        var_app.status_stopparking, var_app.name_stopparking,
                                        var_app.quaility_stopparking, "_GiamSat_TrangThai_DungDo.png")

def caseid_minitor27(self):
    module_other_app.get_datachecklist("Minitor27")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor27", eventname, result,
                                        var_app.status_stop_turning_on, var_app.name_stop_turning_on,
                                        var_app.quaility_stop_turning_on, "_GiamSat_TrangThai_DungBat.png")

def caseid_minitor28(self):
    module_other_app.get_datachecklist("Minitor28")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor28", eventname, result,
                                        var_app.status_turn_on_the_machine, var_app.name_turn_on_the_machine,
                                        var_app.quaility_turn_on_the_machine, "_GiamSat_TrangThai_BatMay.png")

def caseid_minitor29(self):
    module_other_app.get_datachecklist("Minitor29")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor29", eventname, result,
                                        var_app.status_turn_off_the_machine, var_app.name_turn_off_the_machine,
                                        var_app.quaility_turn_of_the_machine, "_GiamSat_TrangThai_TatMay.png")

def caseid_minitor30(self):
    module_other_app.get_datachecklist("Minitor30")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor30", eventname, result,
                                        var_app.status_excessive_speed, var_app.name_excessive_speed,
                                        var_app.quaility_excessive_speed, "_GiamSat_TrangThai_QuaTocDo.png")

def caseid_minitor31(self):
    module_other_app.get_datachecklist("Minitor31")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor31", eventname, result,
                                        var_app.status_lost_gps, var_app.name_lost_gps,
                                        var_app.quaility_lost_gps, "_GiamSat_TrangThai_MatGPS.png")

def caseid_minitor32(self):
    module_other_app.get_datachecklist("Minitor32")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor32", eventname, result,
                                        var_app.status_lost_gms, var_app.name_lost_gms,
                                        var_app.quaility_lost_gms, "_GiamSat_TrangThai_MatGMS.png")

def caseid_minitor33(self):
    module_other_app.get_datachecklist("Minitor33")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor33", eventname, result,
                                        var_app.status_all, var_app.name_all,
                                        var_app.quaility_all, "_GiamSat_TrangThai_Tatca.png")


def caseid_minitor34(self):
    module_other_app.get_datachecklist("Minitor34")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor34", eventname, result,
                                        var_app.status_feedebt, var_app.name_feedebt, var_app.quaility_feedebt, "_GiamSat_TrangThai_NoPhi.png")


def caseid_minitor35(self):
    module_other_app.get_datachecklist("Minitor35")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor35", eventname, result,
                                        var_app.status_move, var_app.name_move, var_app.quaility_move, "_GiamSat_TrangThai_DiChuyen.png")


def caseid_minitor36(self):
    module_other_app.get_datachecklist("Minitor36")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor36", eventname, result,
                                        var_app.status_stopparking, var_app.name_stopparking,
                                        var_app.quaility_stopparking, "_GiamSat_TrangThai_DungDo.png")

def caseid_minitor37(self):
    module_other_app.get_datachecklist("Minitor37")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor37", eventname, result,
                                        var_app.status_stop_turning_on, var_app.name_stop_turning_on,
                                        var_app.quaility_stop_turning_on, "_GiamSat_TrangThai_DungBat.png")

def caseid_minitor38(self):
    module_other_app.get_datachecklist("Minitor38")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor38", eventname, result,
                                        var_app.status_turn_on_the_machine, var_app.name_turn_on_the_machine,
                                        var_app.quaility_turn_on_the_machine, "_GiamSat_TrangThai_BatMay.png")

def caseid_minitor39(self):
    module_other_app.get_datachecklist("Minitor39")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor39", eventname, result,
                                        var_app.status_turn_off_the_machine, var_app.name_turn_off_the_machine,
                                        var_app.quaility_turn_of_the_machine, "_GiamSat_TrangThai_TatMay.png")

def caseid_minitor40(self):
    module_other_app.get_datachecklist("Minitor40")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor40", eventname, result,
                                        var_app.status_excessive_speed, var_app.name_excessive_speed,
                                        var_app.quaility_excessive_speed, "_GiamSat_TrangThai_QuaTocDo.png")

def caseid_minitor41(self):
    module_other_app.get_datachecklist("Minitor41")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor41", eventname, result,
                                        var_app.status_lost_gps, var_app.name_lost_gps,
                                        var_app.quaility_lost_gps, "_GiamSat_TrangThai_MatGPS.png")

def caseid_minitor42(self):
    module_other_app.get_datachecklist("Minitor42")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor42", eventname, result,
                                        var_app.status_lost_gms, var_app.name_lost_gms,
                                        var_app.quaility_lost_gms, "_GiamSat_TrangThai_MatGMS.png")

def caseid_minitor43(self):
    module_other_app.get_datachecklist("Minitor43")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor33", eventname, result,
                                        var_app.status_all, var_app.name_all,
                                        var_app.quaility_all, "_GiamSat_TrangThai_Tatca.png")


def caseid_minitor44(self):
    module_other_app.get_datachecklist("Minitor44")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor44", eventname, result,
                                        var_app.status_feedebt, var_app.name_feedebt, var_app.quaility_feedebt, "_GiamSat_TrangThai_NoPhi.png")


def caseid_minitor45(self):
    module_other_app.get_datachecklist("Minitor45")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor45", eventname, result,
                                        var_app.status_move, var_app.name_move, var_app.quaility_move, "_GiamSat_TrangThai_DiChuyen.png")


def caseid_minitor46(self):
    module_other_app.get_datachecklist("Minitor46")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor46", eventname, result,
                                        var_app.status_stopparking, var_app.name_stopparking,
                                        var_app.quaility_stopparking, "_GiamSat_TrangThai_DungDo.png")

def caseid_minitor47(self):
    module_other_app.get_datachecklist("Minitor47")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor47", eventname, result,
                                        var_app.status_stop_turning_on, var_app.name_stop_turning_on,
                                        var_app.quaility_stop_turning_on, "_GiamSat_TrangThai_DungBat.png")

def caseid_minitor48(self):
    module_other_app.get_datachecklist("Minitor48")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor48", eventname, result,
                                        var_app.status_turn_on_the_machine, var_app.name_turn_on_the_machine,
                                        var_app.quaility_turn_on_the_machine, "_GiamSat_TrangThai_BatMay.png")

def caseid_minitor49(self):
    module_other_app.get_datachecklist("Minitor49")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor49", eventname, result,
                                        var_app.status_turn_off_the_machine, var_app.name_turn_off_the_machine,
                                        var_app.quaility_turn_of_the_machine, "_GiamSat_TrangThai_TatMay.png")

def caseid_minitor50(self):
    module_other_app.get_datachecklist("Minitor50")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor50", eventname, result,
                                        var_app.status_excessive_speed, var_app.name_excessive_speed,
                                        var_app.quaility_excessive_speed, "_GiamSat_TrangThai_QuaTocDo.png")

def caseid_minitor51(self):
    module_other_app.get_datachecklist("Minitor51")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor51", eventname, result,
                                        var_app.status_lost_gps, var_app.name_lost_gps,
                                        var_app.quaility_lost_gps, "_GiamSat_TrangThai_MatGPS.png")

def caseid_minitor52(self):
    module_other_app.get_datachecklist("Minitor52")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor52", eventname, result,
                                        var_app.status_lost_gms, var_app.name_lost_gms,
                                        var_app.quaility_lost_gms, "_GiamSat_TrangThai_MatGMS.png")

def caseid_minitor53(self):
    module_other_app.get_datachecklist("Minitor53")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor53", eventname, result,
                                        var_app.status_all, var_app.name_all,
                                        var_app.quaility_all, "_GiamSat_TrangThai_Tatca.png")


def caseid_minitor54(self):
    module_other_app.get_datachecklist("Minitor54")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor54", eventname, result,
                                        var_app.status_feedebt, var_app.name_feedebt, var_app.quaility_feedebt, "_GiamSat_TrangThai_NoPhi.png")


def caseid_minitor55(self):
    module_other_app.get_datachecklist("Minitor55")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor55", eventname, result,
                                        var_app.status_move, var_app.name_move, var_app.quaility_move, "_GiamSat_TrangThai_DiChuyen.png")


def caseid_minitor56(self):
    module_other_app.get_datachecklist("Minitor56")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor56", eventname, result,
                                        var_app.status_stopparking, var_app.name_stopparking,
                                        var_app.quaility_stopparking, "_GiamSat_TrangThai_DungDo.png")

def caseid_minitor57(self):
    module_other_app.get_datachecklist("Minitor57")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor57", eventname, result,
                                        var_app.status_stop_turning_on, var_app.name_stop_turning_on,
                                        var_app.quaility_stop_turning_on, "_GiamSat_TrangThai_DungBat.png")

def caseid_minitor58(self):
    module_other_app.get_datachecklist("Minitor58")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor58", eventname, result,
                                        var_app.status_turn_on_the_machine, var_app.name_turn_on_the_machine,
                                        var_app.quaility_turn_on_the_machine, "_GiamSat_TrangThai_BatMay.png")

def caseid_minitor59(self):
    module_other_app.get_datachecklist("Minitor59")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor59", eventname, result,
                                        var_app.status_turn_off_the_machine, var_app.name_turn_off_the_machine,
                                        var_app.quaility_turn_of_the_machine, "_GiamSat_TrangThai_TatMay.png")

def caseid_minitor60(self):
    module_other_app.get_datachecklist("Minitor60")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor60", eventname, result,
                                        var_app.status_excessive_speed, var_app.name_excessive_speed,
                                        var_app.quaility_excessive_speed, "_GiamSat_TrangThai_QuaTocDo.png")

def caseid_minitor61(self):
    module_other_app.get_datachecklist("Minitor61")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor61", eventname, result,
                                        var_app.status_lost_gps, var_app.name_lost_gps,
                                        var_app.quaility_lost_gps, "_GiamSat_TrangThai_MatGPS.png")

def caseid_minitor62(self):
    module_other_app.get_datachecklist("Minitor62")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor62", eventname, result,
                                        var_app.status_lost_gms, var_app.name_lost_gms,
                                        var_app.quaility_lost_gms, "_GiamSat_TrangThai_MatGMS.png")

def caseid_minitor63(self):
    module_other_app.get_datachecklist("Minitor63")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor63", eventname, result,
                                        var_app.status_all, var_app.name_all,
                                        var_app.quaility_all, "_GiamSat_TrangThai_Tatca.png")

def caseid_minitor64(self):
    module_other_app.get_datachecklist("Minitor64")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor64", eventname, result,
                                        var_app.status_feedebt, var_app.name_feedebt, var_app.quaility_feedebt, "_GiamSat_TrangThai_NoPhi.png")


def caseid_minitor65(self):
    module_other_app.get_datachecklist("Minitor65")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor65", eventname, result,
                                        var_app.status_move, var_app.name_move, var_app.quaility_move, "_GiamSat_TrangThai_DiChuyen.png")


def caseid_minitor66(self):
    module_other_app.get_datachecklist("Minitor66")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor66", eventname, result,
                                        var_app.status_stopparking, var_app.name_stopparking,
                                        var_app.quaility_stopparking, "_GiamSat_TrangThai_DungDo.png")

def caseid_minitor67(self):
    module_other_app.get_datachecklist("Minitor67")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor67", eventname, result,
                                        var_app.status_stop_turning_on, var_app.name_stop_turning_on,
                                        var_app.quaility_stop_turning_on, "_GiamSat_TrangThai_DungBat.png")

def caseid_minitor68(self):
    module_other_app.get_datachecklist("Minitor68")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor68", eventname, result,
                                        var_app.status_turn_on_the_machine, var_app.name_turn_on_the_machine,
                                        var_app.quaility_turn_on_the_machine, "_GiamSat_TrangThai_BatMay.png")

def caseid_minitor69(self):
    module_other_app.get_datachecklist("Minitor69")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor69", eventname, result,
                                        var_app.status_turn_off_the_machine, var_app.name_turn_off_the_machine,
                                        var_app.quaility_turn_of_the_machine, "_GiamSat_TrangThai_TatMay.png")

def caseid_minitor70(self):
    module_other_app.get_datachecklist("Minitor70")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor70", eventname, result,
                                        var_app.status_excessive_speed, var_app.name_excessive_speed,
                                        var_app.quaility_excessive_speed, "_GiamSat_TrangThai_QuaTocDo.png")

def caseid_minitor71(self):
    module_other_app.get_datachecklist("Minitor71")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor71", eventname, result,
                                        var_app.status_lost_gps, var_app.name_lost_gps,
                                        var_app.quaility_lost_gps, "_GiamSat_TrangThai_MatGPS.png")

def caseid_minitor72(self):
    module_other_app.get_datachecklist("Minitor72")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor72", eventname, result,
                                        var_app.status_lost_gms, var_app.name_lost_gms,
                                        var_app.quaility_lost_gms, "_GiamSat_TrangThai_MatGMS.png")

def caseid_minitor73(self):
    module_other_app.get_datachecklist("Minitor73")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor73", eventname, result,
                                        var_app.status_all, var_app.name_all,
                                        var_app.quaility_all, "_GiamSat_TrangThai_Tatca.png")


def caseid_minitor74(self):
    module_other_app.get_datachecklist("Minitor74")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor74", eventname, result,
                                        var_app.status_feedebt, var_app.name_feedebt, var_app.quaility_feedebt, "_GiamSat_TrangThai_NoPhi.png")


def caseid_minitor75(self):
    module_other_app.get_datachecklist("Minitor75")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor75", eventname, result,
                                        var_app.status_move, var_app.name_move, var_app.quaility_move, "_GiamSat_TrangThai_DiChuyen.png")


def caseid_minitor76(self):
    module_other_app.get_datachecklist("Minitor76")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor76", eventname, result,
                                        var_app.status_stopparking, var_app.name_stopparking,
                                        var_app.quaility_stopparking, "_GiamSat_TrangThai_DungDo.png")

def caseid_minitor77(self):
    module_other_app.get_datachecklist("Minitor77")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor77", eventname, result,
                                        var_app.status_stop_turning_on, var_app.name_stop_turning_on,
                                        var_app.quaility_stop_turning_on, "_GiamSat_TrangThai_DungBat.png")

def caseid_minitor78(self):
    module_other_app.get_datachecklist("Minitor78")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor78", eventname, result,
                                        var_app.status_turn_on_the_machine, var_app.name_turn_on_the_machine,
                                        var_app.quaility_turn_on_the_machine, "_GiamSat_TrangThai_BatMay.png")

def caseid_minitor79(self):
    module_other_app.get_datachecklist("Minitor79")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor79", eventname, result,
                                        var_app.status_turn_off_the_machine, var_app.name_turn_off_the_machine,
                                        var_app.quaility_turn_of_the_machine, "_GiamSat_TrangThai_TatMay.png")

def caseid_minitor80(self):
    module_other_app.get_datachecklist("Minitor80")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor80", eventname, result,
                                        var_app.status_excessive_speed, var_app.name_excessive_speed,
                                        var_app.quaility_excessive_speed, "_GiamSat_TrangThai_QuaTocDo.png")

def caseid_minitor81(self):
    module_other_app.get_datachecklist("Minitor81")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor81", eventname, result,
                                        var_app.status_lost_gps, var_app.name_lost_gps,
                                        var_app.quaility_lost_gps, "_GiamSat_TrangThai_MatGPS.png")

def caseid_minitor82(self):
    module_other_app.get_datachecklist("Minitor82")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor82", eventname, result,
                                        var_app.status_lost_gms, var_app.name_lost_gms,
                                        var_app.quaility_lost_gms, "_GiamSat_TrangThai_MatGMS.png")

def caseid_minitor83(self):
    module_other_app.get_datachecklist("Minitor83")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor83", eventname, result,
                                        var_app.status_all, var_app.name_all,
                                        var_app.quaility_all, "_GiamSat_TrangThai_Tatca.png")





def caseid_minitor84(self):
    module_other_app.get_datachecklist("Minitor84")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.goto_google(self, "Minitor84", eventname, result,)



def caseid_minitor85(self):
    module_other_app.get_datachecklist("Minitor85")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.turn_on_location(self, "Minitor85", eventname, result,)



def caseid_minitor86(self):
    module_other_app.get_datachecklist("Minitor86")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.icon_change_map(self, "Minitor86", eventname, result,)





def caseid_minitor87(self):
    module_other_app.get_datachecklist("Minitor87")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.detail.detail_vehicle(self, "Minitor87", eventname, result,)


def caseid_minitor88(self):
    module_other_app.get_datachecklist("Minitor88")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.detail.detail_vehicle_liscense_plate(self, "Minitor88", eventname, result,)


def caseid_minitor89(self):
    module_other_app.get_datachecklist("Minitor89")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.detail.detail_vehicle_time_update(self, "Minitor89", eventname, result,)


def caseid_minitor90(self):
    module_other_app.get_datachecklist("Minitor90")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.detail.detail_vehicle_adress(self, "Minitor90", eventname, result,)



def caseid_minitor91(self):
    module_other_app.get_datachecklist("Minitor91")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.detail.detail_vehicle_speed_gps(self, "Minitor91", eventname, result,)


def caseid_minitor92(self):
    module_other_app.get_datachecklist("Minitor92")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.detail.detail_vehicle_engine(self, "Minitor92", eventname, result,)


def caseid_minitor93(self):
    module_other_app.get_datachecklist("Minitor93")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.detail.detail_vehicle_air_condition(self, "Minitor93", eventname, result,)


def caseid_minitor94(self):
    module_other_app.get_datachecklist("Minitor94")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.detail.detail_vehicle_door_vehicle(self, "Minitor94", eventname, result,)



def caseid_minitor95(self):
    module_other_app.get_datachecklist("Minitor95")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.detail.detail_vehicle_sim_number(self, "Minitor95", eventname, result,)


def caseid_minitor96(self):
    module_other_app.get_datachecklist("Minitor96")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.detail.detail_vehicle_day_register(self, "Minitor96", eventname, result,)


def caseid_minitor97(self):
    module_other_app.get_datachecklist("Minitor97")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.detail.detail_vehicle_imei(self, "Minitor97", eventname, result,)


def caseid_minitor98(self):
    module_other_app.get_datachecklist("Minitor98")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.detail.detail_vehicle_km_in_day(self, "Minitor98", eventname, result,)



def caseid_minitor99(self):
    module_other_app.get_datachecklist("Minitor99")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.detail.detail_vehicle_cumulative_kilometers(self, "Minitor99", eventname, result,)


def caseid_minitor100(self):
    module_other_app.get_datachecklist("Minitor100")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.detail.detail_vehicle_stop(self, "Minitor100", eventname, result,)



def caseid_minitor101(self):
    module_other_app.get_datachecklist("Minitor101")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.detail.detail_vehicle_open_door_number(self, "Minitor101", eventname, result,)


def caseid_minitor102(self):
    module_other_app.get_datachecklist("Minitor102")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.detail.detail_vehicle_fuel(self, "Minitor102", eventname, result,)


def caseid_minitor103(self):
    module_other_app.get_datachecklist("Minitor103")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.detail.detail_vehicle_temperature(self, "Minitor103", eventname, result,)


def caseid_minitor104(self):
    module_other_app.get_datachecklist("Minitor104")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.detail.detail_vehicle_merory_card(self, "Minitor104", eventname, result,)


def caseid_minitor105(self):
    module_other_app.get_datachecklist("Minitor105")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.detail.detail_vehicle_group(self, "Minitor105", eventname, result,)


def caseid_minitor106(self):
    module_other_app.get_datachecklist("Minitor106")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.detail.detail_vehicle_vin(self, "Minitor106", eventname, result,)


def caseid_minitor107(self):
    module_other_app.get_datachecklist("Minitor107")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.detail.detail_vehicle_drive(self, "Minitor107", eventname, result,)


def caseid_minitor108(self):
    module_other_app.get_datachecklist("Minitor108")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.detail.detail_vehicle_license(self, "Minitor108", eventname, result,)


def caseid_minitor109(self):
    module_other_app.get_datachecklist("Minitor109")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.detail.detail_vehicle_phone(self, "Minitor109", eventname, result,)


def caseid_minitor110(self):
    module_other_app.get_datachecklist("Minitor110")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.detail.detail_vehicle_continuous_driving_time(self, "Minitor110", eventname, result,)


def caseid_minitor111(self):
    module_other_app.get_datachecklist("Minitor111")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.detail.detail_vehicle_driving_time_during_the_day(self, "Minitor111", eventname, result,)


def caseid_minitor112(self):
    module_other_app.get_datachecklist("Minitor112")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.detail.detail_vehicle_number_too_speed(self, "Minitor112", eventname, result,)


def caseid_minitor113(self):
    module_other_app.get_datachecklist("Minitor113")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.detail.detail_vehicle_management_department(self, "Minitor113", eventname, result,)


def caseid_minitor114(self):
    module_other_app.get_datachecklist("Minitor114")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.detail.detail_vehicle_package_name(self, "Minitor114", eventname, result,)


def caseid_minitor115(self):
    module_other_app.get_datachecklist("Minitor115")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.detail.detail_vehicle_home_network(self, "Minitor115", eventname, result,)


def caseid_minitor116(self):
    module_other_app.get_datachecklist("Minitor116")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.detail.detail_vehicle_package_capacity(self, "Minitor116", eventname, result,)



def caseid_minitor117(self):
    module_other_app.get_datachecklist("Minitor117")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.detail.detail_vehicle_number_of_days_of_storage(self, "Minitor117", eventname, result,)


def caseid_minitor118(self):
    module_other_app.get_datachecklist("Minitor118")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.detail.detail_vehicle_number_of_chanels_of_storage(self, "Minitor118", eventname, result,)


def caseid_minitor119(self):
    module_other_app.get_datachecklist("Minitor119")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.detail.detail_vehicle_location(self, "Minitor119", eventname, result,)


def caseid_minitor120(self):
    module_other_app.get_datachecklist("Minitor120")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.detail.detail_vehicle_image(self, "Minitor120", eventname, result,)


def caseid_minitor121(self):
    module_other_app.get_datachecklist("Minitor121")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.detail.detail_vehicle_video(self, "Minitor121", eventname, result,)


def caseid_minitor122(self):
    module_other_app.get_datachecklist("Minitor122")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.detail.detail_vehicle_channel_camera(self, "Minitor122", eventname, result,)


def caseid_minitor123(self):
    module_other_app.get_datachecklist("Minitor123")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.detail.detail_vehicle_channel_active(self, "Minitor123", eventname, result,)



def caseid_minitor124(self):
    module_other_app.get_datachecklist("Minitor124")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.affiliate_link.route(self, "Minitor124", eventname, result,)



def caseid_minitor125(self):
    module_other_app.get_datachecklist("Minitor125")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    login_app.login.logout(self)
    login_app.login.login_v3(self, "43E02740", "12341234")
    minitor_app.affiliate_link.affiliate_link_overview(self, "Minitor125", eventname, result,
                                                       var_app.minitor_image, var_app.minitor_imageiconx, var_app.check_minitor_image,
                                                       "Giám sát hình ảnh", "_GiamSat_HinhAnh.png")


def caseid_minitor126(self):
    module_other_app.get_datachecklist("Minitor126")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.affiliate_link.affiliate_link_overview(self, "Minitor126", eventname, result,
                                                       var_app.minitor_camera, var_app.minitor_cameraiconx, var_app.check_minitor_camera,
                                                       "Giám sát nhiều camera", "_GiamSat_Camera.png")


def caseid_minitor127(self):
    module_other_app.get_datachecklist("Minitor127")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.affiliate_link.affiliate_link_detail(self, "Minitor127", eventname, result, 753, 783, 128, 780, 1000,
                                                     var_app.watch_the_overview_video_again,  var_app.check_watch_the_overview_video_again,
                                                     "Xem lại video", "_GiamSat_XemLaiVideoTongQuan.png")



def caseid_minitor128(self):
    module_other_app.get_datachecklist("Minitor128")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.affiliate_link.affiliate_link_detail(self, "Minitor128", eventname, result, 753, 783, 128, 780, 1000,
                                                     var_app.watch_image_camera_nd10, var_app.check_watch_image_camera_nd10,
                                                     "Camera", "_GiamSat_XemAnhCameraND10.png")


def caseid_minitor129(self):
    module_other_app.get_datachecklist("Minitor129")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.affiliate_link.affiliate_link_detail(self, "Minitor129", eventname, result, 753, 783, 128, 780, 1000,
                                                     var_app.extract_video, var_app.check_extract_video,
                                                     "Trích xuất dữ liệu", "_GiamSat_TrichXuatVieo.png")


def caseid_minitor130(self):
    module_other_app.get_datachecklist("Minitor130")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.affiliate_link.affiliate_link_detail(self, "Minitor130", eventname, result, 777, 1135, 141, 1114, 1000,
                                                     var_app.summary_report_of_activities, var_app.check_summary_report_of_activities,
                                                     "Báo cáo tổng hợp hoạt động", "_GiamSat_BaoCaoTongHopHoatDong.png")



def caseid_minitor131(self):
    module_other_app.get_datachecklist("Minitor131")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.affiliate_link.affiliate_link_detail(self, "Minitor131", eventname, result, 777, 1135, 141, 1114, 1000,
                                                     var_app.summary_report_of_driving_behavior, var_app.check_summary_report_of_driving_behavior,
                                                     "Báo cáo tổng hợp hành vi", "_GiamSat_BaoCaoTongHopHanhViLaiXe.png")


def caseid_minitor132(self):
    module_other_app.get_datachecklist("Minitor132")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.affiliate_link.affiliate_link_detail(self, "Minitor132", eventname, result, 777, 1135, 141, 1114, 1000,
                                                     var_app.detailed_activity_reports, var_app.check_detailed_activity_reports,
                                                     "Báo cáo chi tiết hoạt động", "_GiamSat_BaoCaoChiTietHoatDong.png")


def caseid_minitor133(self):
    module_other_app.get_datachecklist("Minitor133")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.affiliate_link.affiliate_link_detail(self, "Minitor133", eventname, result, 777, 1135, 141, 1114, 1000,
                                                     var_app.vehicle_speed, var_app.check_vehicle_speed,
                                                     "Tốc độ của xe", "_GiamSat_TocDoCuaXe.png")


def caseid_minitor134(self):
    module_other_app.get_datachecklist("Minitor134")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.affiliate_link.affiliate_link_detail(self, "Minitor134", eventname, result, 777, 1135, 141, 1114, 1000,
                                                     var_app.report_vehicle_violations, var_app.check_report_vehicle_violations,
                                                     "Báo cáo chi tiết hành vi", "_GiamSat_BaoCaoViPhamLaiXe.png")



def caseid_minitor135(self):
    module_other_app.get_datachecklist("Minitor135")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.affiliate_link.affiliate_link_detail(self, "Minitor135", eventname, result, 777, 1135, 141, 1114, 1000,
                                                     var_app.fuel_consumption_report, var_app.check_fuel_consumption_report,
                                                     "Báo cáo tiêu hao nhiên liệu", "_GiamSat_BaoCaoTieuHaoNhienLieu.png")



def caseid_minitor136(self):
    module_other_app.get_datachecklist("Minitor136")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.affiliate_link.affiliate_link_detail(self, "Minitor136", eventname, result, 777, 1135, 141, 1114, 1000,
                                                     var_app.Comprehensive_fuel_consumption_report, var_app.check_Comprehensive_fuel_consumption_report,
                                                     "Báo cáo tổng hợp tiêu hao nhiên liệu", "_GiamSat_BaoCaoTongHopTieuHaoNhienLieu.png")



def caseid_minitor137(self):
    module_other_app.get_datachecklist("Minitor137")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.affiliate_link.affiliate_link_detail(self, "Minitor137", eventname, result, 777, 1135, 141, 1114, 1000,
                                                     var_app.report_stop, var_app.check_report_stop,
                                                     "Báo cáo dừng đỗ", "_GiamSat_BaoCaoDungDo.png")



def caseid_minitor138(self):
    module_other_app.get_datachecklist("Minitor138")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.affiliate_link.affiliate_link_detail(self, "Minitor138", eventname, result, 777, 1135, 141, 1114, 1000,
                                                     var_app.fuel_chart, var_app.check_fuel_chart,
                                                     "Biểu đồ nhiên liệu", "_GiamSat_BieuDoNhienLieu.png")
def caseid_minitor139(self):
    module_other_app.get_datachecklist("Minitor139")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.affiliate_link.affiliate_link_detail(self, "Minitor139", eventname, result, 777, 1135, 141, 1114, 1000,
                                                     var_app.fuel_dump_report, var_app.check_fuel_dump_report,
                                                     "Báo cáo đổ hút nhiên liệu", "_GiamSat_BaoCaoDoHutNhienLieu.png")
def caseid_minitor140(self):
    module_other_app.get_datachecklist("Minitor140")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.affiliate_link.affiliate_link_detail(self, "Minitor140", eventname, result, 777, 1135, 141, 1114, 1000,
                                                     var_app.report_loss_of_signal, var_app.check_report_loss_of_signal,
                                                     "Báo cáo mất tín hiệu", "_GiamSat_BaoCaoMatTinHieu.png")

def caseid_minitor141(self):
    module_other_app.get_datachecklist("Minitor141")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.affiliate_link.affiliate_link_detail(self, "Minitor141", eventname, result, 777, 1135, 141, 1114, 1000,
                                                     var_app.engine_report, var_app.check_engine_report,
                                                     "Báo cáo động cơ", "_GiamSat_BaoCaoDongCo.png")
def caseid_minitor142(self):
    module_other_app.get_datachecklist("Minitor142")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.affiliate_link.affiliate_link_detail(self, "Minitor142", eventname, result, 777, 1135, 141, 1114, 1000,
                                                     var_app.report_speeding, var_app.check_report_speeding,
                                                     "Báo cáo quá tốc độ", "_GiamSat_BaoCaoQuaTocDo.png")

def caseid_minitor143(self):
    module_other_app.get_datachecklist("Minitor143")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.affiliate_link.affiliate_link_detail(self, "Minitor143", eventname, result, 777, 1135, 141, 1114, 1000,
                                                     var_app.report_entering_and_exiting_the_station, var_app.check_report_entering_and_exiting_the_station,
                                                     "Báo cáo ra vào trạm", "_GiamSat_BaoCaoRaVaoTram.png")

def caseid_minitor144(self):
    module_other_app.get_datachecklist("Minitor144")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.affiliate_link.affiliate_link_detail(self, "Minitor144", eventname, result, 777, 1135, 141, 1114, 1000,
                                                     var_app.business_trip_report, var_app.check_business_trip_report,
                                                     "Báo cáo chuyến kinh doanh", "_GiamSat_BaoCaoChuyenKinhDoanh.png")

def caseid_minitor145(self):
    module_other_app.get_datachecklist("Minitor145")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.affiliate_link.affiliate_link_detail(self, "Minitor145", eventname, result, 771, 1438, 150, 1438, 1000,
                                                     var_app.hide_and_show_the_car, var_app.check_hide_and_show_the_car,
                                                     "Danh sách xe đã ẩn", "_GiamSat_AnHienXe.png")

def caseid_minitor146(self):
    module_other_app.get_datachecklist("Minitor146")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.affiliate_link.affiliate_link_detail(self, "Minitor146", eventname, result, 771, 1438, 150, 1438, 1000,
                                                     var_app.fee_information, var_app.check_fee_information,
                                                     "Tra cứu thông tin phí", "_GiamSat_ThongTinPhi.png")

def caseid_minitor147(self):
    module_other_app.get_datachecklist("Minitor147")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.affiliate_link.affiliate_link_detail(self, "Minitor147", eventname, result, 771, 1438, 150, 1438, 1000,
                                                     var_app.add_driver, var_app.check_add_driver,
                                                     "Nhập thông tin lái xe", "_GiamSat_ThemLaiXe.png")

def caseid_minitor148(self):
    module_other_app.get_datachecklist("Minitor148")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.affiliate_link.affiliate_link_detail(self, "Minitor148", eventname, result, 771, 1438, 150, 1438, 1000,
                                                     var_app.list_driver, var_app.check_list_driver,
                                                     "Danh sách lái xe", "_GiamSat_DanhSachLaiXe.png")

def caseid_minitor149(self):
    module_other_app.get_datachecklist("Minitor149")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.affiliate_link.affiliate_link_detail(self, "Minitor149", eventname, result, 771, 1438, 150, 1438, 1000,
                                                     var_app.enter_document_information, var_app.check_enter_document_information,
                                                     "Nhập thông tin giấy tờ", "_GiamSat_NhapThongTinGiayTo.png")

def caseid_minitor150(self):
    module_other_app.get_datachecklist("Minitor150")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.affiliate_link.affiliate_link_detail(self, "Minitor150", eventname, result, 771, 1438, 150, 1438, 1000,
                                                     var_app.support_customer, var_app.check_support_customer,
                                                     "Hỗ trợ khách hàng", "_GiamSat_HoTroKhachHang.png")

def caseid_minitor151(self):
    module_other_app.get_datachecklist("Minitor151")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.affiliate_link.affiliate_link_detail(self, "Minitor151", eventname, result, 771, 1438, 150, 1438, 1000,
                                                     var_app.transmission_report, var_app.check_transmission_report,
                                                     "Cảnh báo tích truyền", "_GiamSat_BaoCaoTichTruyen.png")

def caseid_minitor152(self):
    module_other_app.get_datachecklist("Minitor152")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.affiliate_link.affiliate_link_detail(self, "Minitor152", eventname, result, 771, 1438, 150, 1438, 1000,
                                                     var_app.record_driver_card, var_app.check_record_driver_card,
                                                     "Ghi thẻ lái xe", "_GiamSat_GhiTheLaiXe.png")
def caseid_minitor153(self):
    module_other_app.get_datachecklist("Minitor153")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.affiliate_link.affiliate_link_detail(self, "Minitor153", eventname, result, 771, 1438, 150, 1438, 1000,
                                                     var_app.list_of_documents, var_app.check_list_of_documents,
                                                     "Danh sách giấy tờ", "_GiamSat_DanhSachGiayTo.png")


def caseid_minitor154(self):
    module_other_app.get_datachecklist("Minitor154")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.affiliate_link.affiliate_link_detail(self, "Minitor154", eventname, result, 771, 1438, 150, 1438, 1000,
                                                     var_app.list_vehicle, var_app.check_list_vehicle,
                                                    "", "_GiamSat_DanhSachPhuongTien.png")
    var_app.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Giám sát").click()
    time.sleep(2)




def caseid_route01(self):
    module_other_app.get_datachecklist("Route01")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    route.overview.search_vehile(self, "Route01", eventname, result,)

def caseid_route02(self):
    module_other_app.get_datachecklist("Route02")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    route.overview.route_1h(self, "Route02", eventname, result,)

def caseid_route03(self):
    module_other_app.get_datachecklist("Route03")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    route.overview.route_choosetime(self, "Route03", eventname, result, var_app.route_4h)

def caseid_route04(self):
    module_other_app.get_datachecklist("Route04")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    route.overview.route_choosetime(self, "Route04", eventname, result, var_app.route_8h)


def caseid_route05(self):
    module_other_app.get_datachecklist("Route05")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    route.overview.route_choosetime(self, "Route05", eventname, result, var_app.route_24h)


def caseid_route06(self):
    module_other_app.get_datachecklist("Route06")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    route.overview.route_calender(self, "Route06", eventname, result)



def caseid_route07(self):
    module_other_app.get_datachecklist("Route07")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    route.overview.route_3tiles(self, "Route07", eventname, result)


def caseid_route08(self):
    module_other_app.get_datachecklist("Route08")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    route.overview.route_hide_route(self, "Route08", eventname, result)


def caseid_route09(self):
    module_other_app.get_datachecklist("Route09")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    route.overview.route_icon(self, "Route09", eventname, result, var_app.icon_local)

def caseid_route10(self):
    module_other_app.get_datachecklist("Route10")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    route.overview.route_icon(self, "Route10", eventname, result, var_app.icon_route)

def caseid_route11(self):
    module_other_app.get_datachecklist("Route11")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    route.overview.route_icon(self, "Route11", eventname, result, var_app.icon_map)


def caseid_vehicle01(self):
    module_other_app.get_datachecklist("Vehicle01")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    vehicle.overview.search_vehicle(self, "Vehicle01", eventname, result)


def caseid_vehicle02(self):
    module_other_app.get_datachecklist("Vehicle02")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    vehicle.overview.vehicle_note(self, "Vehicle02", eventname, result)


def caseid_vehicle03(self):
    module_other_app.get_datachecklist("Vehicle03")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    vehicle.overview.select_group(self, "Vehicle03", eventname, result)


def caseid_vehicle04(self):
    module_other_app.get_datachecklist("Vehicle04")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    vehicle.overview.arrange_vehicle(self, "Vehicle04", eventname, result)


def caseid_vehicle05(self):
    module_other_app.get_datachecklist("Vehicle05")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    vehicle.overview.arrange_time(self, "Vehicle05", eventname, result)

def caseid_vehicle06(self):
    module_other_app.get_datachecklist("Vehicle06")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    vehicle.overview.arrange_default(self, "Vehicle06", eventname, result)


def caseid_vehicle07(self):
    module_other_app.get_datachecklist("Vehicle07")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    vehicle.overview.status_vehicle(self, "Vehicle07", eventname, result,
                                        var_app.status_feedebt1, var_app.name_feedebt1, var_app.quaility_feedebt1, "_PhuongTien_TrangThai_NoPhi.png")


def caseid_vehicle08(self):
    module_other_app.get_datachecklist("Vehicle08")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    vehicle.overview.status_vehicle(self, "Vehicle08", eventname, result,
                                        var_app.status_move1, var_app.name_move1, var_app.quaility_move1, "_PhuongTien_TrangThai_DiChuyen.png")


def caseid_vehicle09(self):
    module_other_app.get_datachecklist("Vehicle09")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    vehicle.overview.status_vehicle(self, "Vehicle09", eventname, result,
                                        var_app.status_stopparking1, var_app.name_stopparking1, var_app.quaility_stopparking1, "_PhuongTien_TrangThai_DungDo.png")

def caseid_vehicle10(self):
    module_other_app.get_datachecklist("Vehicle10")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    vehicle.overview.status_vehicle(self, "Vehicle10", eventname, result,
                                        var_app.status_stop_turning_on1, var_app.name_stop_turning_on1, var_app.quaility_stop_turning_on1, "_PhuongTien_TrangThai_DungBat.png")

def caseid_vehicle11(self):
    module_other_app.get_datachecklist("Vehicle11")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    vehicle.overview.status_vehicle(self, "Vehicle11", eventname, result,
                                        var_app.status_turn_on_the_machine1, var_app.name_turn_on_the_machine1, var_app.quaility_turn_on_the_machine1, "_PhuongTien_TrangThai_BatMay.png")


def caseid_vehicle12(self):
    module_other_app.get_datachecklist("Vehicle12")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    vehicle.overview.status_vehicle(self, "Vehicle12", eventname, result,
                                        var_app.status_turn_off_the_machine1, var_app.name_turn_off_the_machine1, var_app.quaility_turn_off_the_machine1, "_PhuongTien_TrangThai_TatMay.png")


def caseid_vehicle13(self):
    module_other_app.get_datachecklist("Vehicle13")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    vehicle.overview.status_vehicle(self, "Vehicle13", eventname, result,
                                        var_app.status_excessive_speed1, var_app.name_excessive_speed1, var_app.quaility_excessive_speed1, "_PhuongTien_TrangThai_QuaTocDo.png")

def caseid_vehicle14(self):
    module_other_app.get_datachecklist("Vehicle14")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    vehicle.overview.status_vehicle(self, "Vehicle14", eventname, result,
                                        var_app.status_lost_gps1, var_app.name_lost_gps1, var_app.quaility_lost_gps1, "_PhuongTien_TrangThai_MatGPS.png")


def caseid_vehicle15(self):
    module_other_app.get_datachecklist("Vehicle15")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    vehicle.overview.status_vehicle(self, "Vehicle15", eventname, result,
                                        var_app.status_lost_gms1, var_app.name_lost_gms1, var_app.quaility_lost_gms1, "_PhuongTien_TrangThai_MatGMS.png")


def caseid_vehicle16(self):
    module_other_app.get_datachecklist("Vehicle16")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    vehicle.overview.status_vehicle(self, "Vehicle16", eventname, result,
                                        var_app.status_total1, var_app.name_total1, var_app.quaility_total1, "_PhuongTien_TrangThai_TatCa.png")

def caseid_vehicle17(self):
    module_other_app.get_datachecklist("Vehicle17")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    vehicle.overview.detailinfnfo_vehicle(self, "Vehicle17", eventname, result,
                                    var_app.vehicle_vehicle_plate, "_PhuongTien_BienSoXe.png")

def caseid_vehicle18(self):
    module_other_app.get_datachecklist("Vehicle18")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    vehicle.overview.detailinfnfo_vehicle(self, "Vehicle18", eventname, result,
                                    var_app.vehicle_time_update, "_PhuongTien_ThoiGianCapNhat.png")

def caseid_vehicle19(self):
    module_other_app.get_datachecklist("Vehicle19")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    vehicle.overview.detailinfnfo_vehicle(self, "Vehicle19", eventname, result,
                                    var_app.vehicle_engine, "_PhuongTien_DongCo.png")

def caseid_vehicle20(self):
    module_other_app.get_datachecklist("Vehicle20")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    vehicle.overview.detailinfnfo_vehicle(self, "Vehicle20", eventname, result,
                                    var_app.vehicle_km_in_day, "_PhuongTien_KmTrongNgay.png")

def caseid_vehicle21(self):
    module_other_app.get_datachecklist("Vehicle21")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    vehicle.overview.detailinfnfo_vehicle(self, "Vehicle21", eventname, result,
                                    var_app.vehicle_speed1, "_PhuongTien_VanToc.png")

def caseid_vehicle22(self):
    module_other_app.get_datachecklist("Vehicle22")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    vehicle.overview.detailinfnfo_vehicle(self, "Vehicle22", eventname, result,
                                    var_app.vehicle_stopping_time, "_PhuongTien_ThoiGianDungDo.png")

def caseid_vehicle23(self):
    module_other_app.get_datachecklist("Vehicle23")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    vehicle.overview.detailinfnfo_vehicle(self, "Vehicle23", eventname, result,
                                    var_app.vehicle_temperature, "_PhuongTien_NhietDo.png")


def caseid_vehicle24(self):
    module_other_app.get_datachecklist("Vehicle24")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    vehicle.overview.detailinfnfo_vehicle(self, "Vehicle24", eventname, result,
                                    var_app.vehicle_address, "_PhuongTien_DiaChi.png")

def caseid_vehicle25(self):
    module_other_app.get_datachecklist("Vehicle25")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    vehicle.overview.detail_custom(self, "Vehicle25", eventname, result)

def caseid_vehicle26(self):
    module_other_app.get_datachecklist("Vehicle26")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    vehicle.overview.detail_custom_search(self, "Vehicle26", eventname, result)

def caseid_vehicle27(self):
    module_other_app.get_datachecklist("Vehicle27")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    vehicle.overview.detail_choose_max_favorites(self, "Vehicle27", eventname, result)

def caseid_vehicle28(self):
    module_other_app.get_datachecklist("Vehicle28")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    vehicle.overview.detail_choose_min_favorites(self, "Vehicle28", eventname, result)






