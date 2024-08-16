import login_app
import module_other_app
import route
import var_app
import minitor_app
import homepage_app
import image_video_app
from retry import retry
import report_app
import utilities

import vehicle


def caseid_login01(self):
    module_other_app.get_datachecklist("Login01")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    login_app.login.check_logout(self)
    login_app.login.login(self, "ungroup", "12341234",
                          "Login01", eventname, result,
                          var_app.check_customer_account1, "Phương tiện", "_DangNhap_TKKhachHangCoQuyenGiamSat.png")



def caseid_login02(self):
    module_other_app.get_datachecklist("Login02")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    login_app.login.check_logout(self)
    login_app.login.login(self, "truongtq@bagroup.vn", "atgmj123",
                          "Login02", eventname, result,
                          var_app.check_customer_account1, "Phương tiện", "_DangNhap_TKBinhAnh.png")



def caseid_login03(self):
    module_other_app.get_datachecklist("Login03")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    login_app.login.check_logout(self)
    login_app.login.login(self, "43E02740", "12341234",
                          "Login03", eventname, result,
                          var_app.check_customer_account1, "Phương tiện", "_DangNhap_TKDaiLy.png")



def caseid_login04(self):
    module_other_app.get_datachecklist("Login04")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    login_app.login.check_logout(self)
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
    login_app.login.remember_login_mark(self, "Login08", eventname, result)



def caseid_login09(self):
    module_other_app.get_datachecklist("Login09")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    login_app.login.remember_login_not_mark(self, "Login09", eventname, result)



def caseid_login10(self):
    module_other_app.get_datachecklist("Login10")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    login_app.other_function.change_language(self, "Login10", eventname, result, 110, 410,
                          var_app.check_change_language_english, "Forgot password?", "_DangNhap_DoiNgonNgu_English.png")


def caseid_login11(self):
    module_other_app.get_datachecklist("Login11")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    login_app.other_function.change_language(self, "Login11", eventname, result, 125, 324,
                          var_app.check_change_language_vietnamese, "Quên mật khẩu?", "_DangNhap_DoiNgonNgu_TiengViet.png")




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
                          var_app.affiliate_zalo, var_app.check_affiliate_zalo, "https://zalo.me/bagpsvn", "_DangNhap_LinkLienKet_Zalo.png")



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
                          var_app.affiliate_trainghiembagps, var_app.check_affiliate_trainghiembagps, "https://bagps.vn/", "_DangNhap_LinkLienKet_TraiNghiemBAGPS.png")




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


@retry(tries=3, delay=2, backoff=1, jitter=5, )
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
                                        "Nợ phí", 650, 315, "_GiamSat_TrangThai_NoPhi.png")


def caseid_minitor05(self):
    module_other_app.get_datachecklist("Minitor05")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor05", eventname, result,
                                        "Di chuyển", 650, 450, "_GiamSat_TrangThai_DiChuyen.png")


def caseid_minitor06(self):
    module_other_app.get_datachecklist("Minitor06")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor06", eventname, result,
                                        "Dừng Tắt", 650, 580, "_GiamSat_TrangThai_DungTat.png")


def caseid_minitor07(self):
    module_other_app.get_datachecklist("Minitor07")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor07", eventname, result,
                                        "Dừng Bật", 650, 720, "_GiamSat_TrangThai_DungBat.png")



def caseid_minitor08(self):
    module_other_app.get_datachecklist("Minitor08")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor08", eventname, result,
                                        "Bật Máy", 650, 830, "_GiamSat_TrangThai_BatMay.png")



def caseid_minitor09(self):
    module_other_app.get_datachecklist("Minitor09")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor09", eventname, result,
                                        "Tắt Máy", 650, 950, "_GiamSat_TrangThai_TatMay.png")


def caseid_minitor10(self):
    module_other_app.get_datachecklist("Minitor10")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor10", eventname, result,
                                        "Quá tốc độ", 650, 1080, "_GiamSat_TrangThai_QuaTocDo.png")


def caseid_minitor11(self):
    module_other_app.get_datachecklist("Minitor11")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor11", eventname, result,
                                        "Mất GPS", 650, 1200, "_GiamSat_TrangThai_MatGPS.png")



def caseid_minitor12(self):
    module_other_app.get_datachecklist("Minitor12")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor12", eventname, result,
                                        "Mất GMS", 650, 1330, "_GiamSat_TrangThai_MatGMS.png")



def caseid_minitor13(self):
    module_other_app.get_datachecklist("Minitor13")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor13", eventname, result,
                                        "Tất cả", 650, 210, "_GiamSat_TrangThai_Tatca.png")

def caseid_minitor14(self):
    module_other_app.get_datachecklist("Minitor14")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor14", eventname, result,
                                        "Nợ phí", 650, 315, "_GiamSat_TrangThai_NoPhi.png")


def caseid_minitor15(self):
    module_other_app.get_datachecklist("Minitor15")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor15", eventname, result,
                                        "Di chuyển", 650, 450, "_GiamSat_TrangThai_DiChuyen.png")


def caseid_minitor16(self):
    module_other_app.get_datachecklist("Minitor16")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor16", eventname, result,
                                        "Dừng Tắt", 650, 580, "_GiamSat_TrangThai_DungTat.png")

def caseid_minitor17(self):
    module_other_app.get_datachecklist("Minitor17")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor17", eventname, result,
                                        "Dừng Bật", 650, 720, "_GiamSat_TrangThai_DungBat.png")

def caseid_minitor18(self):
    module_other_app.get_datachecklist("Minitor18")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor18", eventname, result,
                                        "Bật Máy", 650, 830, "_GiamSat_TrangThai_BatMay.png")

def caseid_minitor19(self):
    module_other_app.get_datachecklist("Minitor19")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor19", eventname, result,
                                        "Tắt Máy", 650, 950, "_GiamSat_TrangThai_TatMay.png")

def caseid_minitor20(self):
    module_other_app.get_datachecklist("Minitor20")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor20", eventname, result,
                                        "Quá tốc độ", 650, 1080, "_GiamSat_TrangThai_QuaTocDo.png")

def caseid_minitor21(self):
    module_other_app.get_datachecklist("Minitor21")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor21", eventname, result,
                                        "Mất GPS", 650, 1200, "_GiamSat_TrangThai_MatGPS.png")

def caseid_minitor22(self):
    module_other_app.get_datachecklist("Minitor22")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor22", eventname, result,
                                        "Mất GMS", 650, 1330, "_GiamSat_TrangThai_MatGMS.png")

def caseid_minitor23(self):
    module_other_app.get_datachecklist("Minitor23")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor23", eventname, result,
                                        "Tất cả", 650, 210, "_GiamSat_TrangThai_Tatca.png")

def caseid_minitor24(self):
    module_other_app.get_datachecklist("Minitor24")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor24", eventname, result,
                                        "Nợ phí", 650, 315, "_GiamSat_TrangThai_NoPhi.png")


def caseid_minitor25(self):
    module_other_app.get_datachecklist("Minitor25")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor25", eventname, result,
                                        "Di chuyển", 650, 450, "_GiamSat_TrangThai_DiChuyen.png")


def caseid_minitor26(self):
    module_other_app.get_datachecklist("Minitor26")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor26", eventname, result,
                                        "Dừng Tắt", 650, 580, "_GiamSat_TrangThai_DungTat.png")

def caseid_minitor27(self):
    module_other_app.get_datachecklist("Minitor27")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor27", eventname, result,
                                        "Dừng Bật", 650, 720, "_GiamSat_TrangThai_DungBat.png")

def caseid_minitor28(self):
    module_other_app.get_datachecklist("Minitor28")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor28", eventname, result,
                                        "Bật Máy", 650, 830, "_GiamSat_TrangThai_BatMay.png")

def caseid_minitor29(self):
    module_other_app.get_datachecklist("Minitor29")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor29", eventname, result,
                                        "Tắt Máy", 650, 950, "_GiamSat_TrangThai_TatMay.png")

def caseid_minitor30(self):
    module_other_app.get_datachecklist("Minitor30")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor30", eventname, result,
                                        "Quá tốc độ", 650, 1080, "_GiamSat_TrangThai_QuaTocDo.png")

def caseid_minitor31(self):
    module_other_app.get_datachecklist("Minitor31")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor31", eventname, result,
                                        "Mất GPS", 650, 1200, "_GiamSat_TrangThai_MatGPS.png")

def caseid_minitor32(self):
    module_other_app.get_datachecklist("Minitor32")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor32", eventname, result,
                                        "Mất GMS", 650, 1330, "_GiamSat_TrangThai_MatGMS.png")

def caseid_minitor33(self):
    module_other_app.get_datachecklist("Minitor33")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor33", eventname, result,
                                        "Tất cả", 650, 210, "_GiamSat_TrangThai_Tatca.png")


def caseid_minitor34(self):
    module_other_app.get_datachecklist("Minitor34")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor34", eventname, result,
                                        "Nợ phí", 650, 315, "_GiamSat_TrangThai_NoPhi.png")


def caseid_minitor35(self):
    module_other_app.get_datachecklist("Minitor35")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor35", eventname, result,
                                        "Di chuyển", 650, 450, "_GiamSat_TrangThai_DiChuyen.png")


def caseid_minitor36(self):
    module_other_app.get_datachecklist("Minitor36")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor36", eventname, result,
                                        "Dừng Tắt", 650, 580, "_GiamSat_TrangThai_DungTat.png")

def caseid_minitor37(self):
    module_other_app.get_datachecklist("Minitor37")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor37", eventname, result,
                                        "Dừng Bật", 650, 720, "_GiamSat_TrangThai_DungBat.png")

def caseid_minitor38(self):
    module_other_app.get_datachecklist("Minitor38")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor38", eventname, result,
                                        "Bật Máy", 650, 830, "_GiamSat_TrangThai_BatMay.png")

def caseid_minitor39(self):
    module_other_app.get_datachecklist("Minitor39")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor39", eventname, result,
                                        "Tắt Máy", 650, 950, "_GiamSat_TrangThai_TatMay.png")

def caseid_minitor40(self):
    module_other_app.get_datachecklist("Minitor40")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor40", eventname, result,
                                        "Quá tốc độ", 650, 1080, "_GiamSat_TrangThai_QuaTocDo.png")

def caseid_minitor41(self):
    module_other_app.get_datachecklist("Minitor41")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor41", eventname, result,
                                        "Mất GPS", 650, 1200, "_GiamSat_TrangThai_MatGPS.png")

def caseid_minitor42(self):
    module_other_app.get_datachecklist("Minitor42")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor42", eventname, result,
                                        "Mất GMS", 650, 1330, "_GiamSat_TrangThai_MatGMS.png")

def caseid_minitor43(self):
    module_other_app.get_datachecklist("Minitor43")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor43", eventname, result,
                                        "Tất cả", 650, 210, "_GiamSat_TrangThai_Tatca.png")


def caseid_minitor44(self):
    module_other_app.get_datachecklist("Minitor44")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor44", eventname, result,
                                        "Nợ phí", 650, 315, "_GiamSat_TrangThai_NoPhi.png")


def caseid_minitor45(self):
    module_other_app.get_datachecklist("Minitor45")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor45", eventname, result,
                                        "Di chuyển", 650, 450, "_GiamSat_TrangThai_DiChuyen.png")


def caseid_minitor46(self):
    module_other_app.get_datachecklist("Minitor46")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor46", eventname, result,
                                        "Dừng Tắt", 650, 580, "_GiamSat_TrangThai_DungTat.png")

def caseid_minitor47(self):
    module_other_app.get_datachecklist("Minitor47")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor47", eventname, result,
                                        "Dừng Bật", 650, 720, "_GiamSat_TrangThai_DungBat.png")

def caseid_minitor48(self):
    module_other_app.get_datachecklist("Minitor48")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor48", eventname, result,
                                        "Bật Máy", 650, 830, "_GiamSat_TrangThai_BatMay.png")

def caseid_minitor49(self):
    module_other_app.get_datachecklist("Minitor49")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor49", eventname, result,
                                        "Tắt Máy", 650, 950, "_GiamSat_TrangThai_TatMay.png")

def caseid_minitor50(self):
    module_other_app.get_datachecklist("Minitor50")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor50", eventname, result,
                                        "Quá tốc độ", 650, 1080, "_GiamSat_TrangThai_QuaTocDo.png")

def caseid_minitor51(self):
    module_other_app.get_datachecklist("Minitor51")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor51", eventname, result,
                                        "Mất GPS", 650, 1200, "_GiamSat_TrangThai_MatGPS.png")

def caseid_minitor52(self):
    module_other_app.get_datachecklist("Minitor52")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor52", eventname, result,
                                        "Mất GMS", 650, 1330, "_GiamSat_TrangThai_MatGMS.png")

def caseid_minitor53(self):
    module_other_app.get_datachecklist("Minitor53")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor53", eventname, result,
                                        "Tất cả", 650, 210, "_GiamSat_TrangThai_Tatca.png")


def caseid_minitor54(self):
    module_other_app.get_datachecklist("Minitor54")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor54", eventname, result,
                                        "Nợ phí", 650, 315, "_GiamSat_TrangThai_NoPhi.png")


def caseid_minitor55(self):
    module_other_app.get_datachecklist("Minitor55")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor55", eventname, result,
                                        "Di chuyển", 650, 450, "_GiamSat_TrangThai_DiChuyen.png")


def caseid_minitor56(self):
    module_other_app.get_datachecklist("Minitor56")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor56", eventname, result,
                                        "Dừng Tắt", 650, 580, "_GiamSat_TrangThai_DungTat.png")

def caseid_minitor57(self):
    module_other_app.get_datachecklist("Minitor57")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor57", eventname, result,
                                        "Dừng Bật", 650, 720, "_GiamSat_TrangThai_DungBat.png")

def caseid_minitor58(self):
    module_other_app.get_datachecklist("Minitor58")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor58", eventname, result,
                                        "Bật Máy", 650, 830, "_GiamSat_TrangThai_BatMay.png")

def caseid_minitor59(self):
    module_other_app.get_datachecklist("Minitor59")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor59", eventname, result,
                                        "Tắt Máy", 650, 950, "_GiamSat_TrangThai_TatMay.png")

def caseid_minitor60(self):
    module_other_app.get_datachecklist("Minitor60")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor60", eventname, result,
                                        "Quá tốc độ", 650, 1080, "_GiamSat_TrangThai_QuaTocDo.png")

def caseid_minitor61(self):
    module_other_app.get_datachecklist("Minitor61")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor61", eventname, result,
                                        "Mất GPS", 650, 1200, "_GiamSat_TrangThai_MatGPS.png")

def caseid_minitor62(self):
    module_other_app.get_datachecklist("Minitor62")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor62", eventname, result,
                                        "Mất GMS", 650, 1330, "_GiamSat_TrangThai_MatGMS.png")

def caseid_minitor63(self):
    module_other_app.get_datachecklist("Minitor63")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor63", eventname, result,
                                        "Tất cả", 650, 210, "_GiamSat_TrangThai_Tatca.png")

def caseid_minitor64(self):
    module_other_app.get_datachecklist("Minitor64")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor64", eventname, result,
                                        "Nợ phí", 650, 315, "_GiamSat_TrangThai_NoPhi.png")


def caseid_minitor65(self):
    module_other_app.get_datachecklist("Minitor65")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor65", eventname, result,
                                        "Di chuyển", 650, 450, "_GiamSat_TrangThai_DiChuyen.png")


def caseid_minitor66(self):
    module_other_app.get_datachecklist("Minitor66")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor66", eventname, result,
                                        "Dừng Tắt", 650, 580, "_GiamSat_TrangThai_DungTat.png")

def caseid_minitor67(self):
    module_other_app.get_datachecklist("Minitor67")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor67", eventname, result,
                                        "Dừng Bật", 650, 720, "_GiamSat_TrangThai_DungBat.png")

def caseid_minitor68(self):
    module_other_app.get_datachecklist("Minitor68")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor68", eventname, result,
                                        "Bật Máy", 650, 830, "_GiamSat_TrangThai_BatMay.png")

def caseid_minitor69(self):
    module_other_app.get_datachecklist("Minitor69")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor69", eventname, result,
                                        "Tắt Máy", 650, 950, "_GiamSat_TrangThai_TatMay.png")

def caseid_minitor70(self):
    module_other_app.get_datachecklist("Minitor70")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor70", eventname, result,
                                        "Quá tốc độ", 650, 1080, "_GiamSat_TrangThai_QuaTocDo.png")

def caseid_minitor71(self):
    module_other_app.get_datachecklist("Minitor71")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor71", eventname, result,
                                        "Mất GPS", 650, 1200, "_GiamSat_TrangThai_MatGPS.png")

def caseid_minitor72(self):
    module_other_app.get_datachecklist("Minitor72")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor72", eventname, result,
                                        "Mất GMS", 650, 1330, "_GiamSat_TrangThai_MatGMS.png")

def caseid_minitor73(self):
    module_other_app.get_datachecklist("Minitor73")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor73", eventname, result,
                                        "Tất cả", 650, 210, "_GiamSat_TrangThai_Tatca.png")


def caseid_minitor74(self):
    module_other_app.get_datachecklist("Minitor74")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor74", eventname, result,
                                        "Nợ phí", 650, 315, "_GiamSat_TrangThai_NoPhi.png")


def caseid_minitor75(self):
    module_other_app.get_datachecklist("Minitor75")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor75", eventname, result,
                                        "Di chuyển", 650, 450, "_GiamSat_TrangThai_DiChuyen.png")


def caseid_minitor76(self):
    module_other_app.get_datachecklist("Minitor76")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor76", eventname, result,
                                        "Dừng Tắt", 650, 580, "_GiamSat_TrangThai_DungTat.png")

def caseid_minitor77(self):
    module_other_app.get_datachecklist("Minitor77")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor77", eventname, result,
                                        "Dừng Bật", 650, 720, "_GiamSat_TrangThai_DungBat.png")

def caseid_minitor78(self):
    module_other_app.get_datachecklist("Minitor78")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor78", eventname, result,
                                        "Bật Máy", 650, 830, "_GiamSat_TrangThai_BatMay.png")

def caseid_minitor79(self):
    module_other_app.get_datachecklist("Minitor79")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor79", eventname, result,
                                        "Tắt Máy", 650, 950, "_GiamSat_TrangThai_TatMay.png")

def caseid_minitor80(self):
    module_other_app.get_datachecklist("Minitor80")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor80", eventname, result,
                                        "Quá tốc độ", 650, 1080, "_GiamSat_TrangThai_QuaTocDo.png")

def caseid_minitor81(self):
    module_other_app.get_datachecklist("Minitor81")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor81", eventname, result,
                                        "Mất GPS", 650, 1200, "_GiamSat_TrangThai_MatGPS.png")

def caseid_minitor82(self):
    module_other_app.get_datachecklist("Minitor82")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor82", eventname, result,
                                        "Mất GMS", 650, 1330, "_GiamSat_TrangThai_MatGMS.png")

def caseid_minitor83(self):
    module_other_app.get_datachecklist("Minitor83")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor83", eventname, result,
                                        "Tất cả", 650, 210, "_GiamSat_TrangThai_Tatca.png")





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




@retry(tries=3, delay=2, backoff=1, jitter=5, )
def caseid_minitor87(self):
    module_other_app.get_datachecklist("Minitor87")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.detail.detail_vehicle(self, "Minitor87", eventname, result,)


def caseid_minitor88(self):
    module_other_app.get_datachecklist("Minitor88")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.detail.detail_vehicle_sim_number1(self, "Minitor88", eventname, result,)


def caseid_minitor89(self):
    module_other_app.get_datachecklist("Minitor89")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.detail.detail_vehicle_day_register(self, "Minitor89", eventname, result,)


def caseid_minitor90(self):
    module_other_app.get_datachecklist("Minitor90")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.detail.detail_vehicle_liscense_plate(self, "Minitor90", eventname, result,)



def caseid_minitor91(self):
    module_other_app.get_datachecklist("Minitor91")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.detail.detail_vehicle_adress(self, "Minitor91", eventname, result,)


def caseid_minitor92(self):
    module_other_app.get_datachecklist("Minitor92")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.detail.detail_vehicle_time_update(self, "Minitor92", eventname, result,)


def caseid_minitor93(self):
    module_other_app.get_datachecklist("Minitor93")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.detail.detail_vehicle_speed_gps(self, "Minitor93", eventname, result,)


def caseid_minitor94(self):
    module_other_app.get_datachecklist("Minitor94")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.detail.detail_vehicle_engine(self, "Minitor94", eventname, result,)



def caseid_minitor95(self):
    module_other_app.get_datachecklist("Minitor95")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.detail.detail_vehicle_km_in_day(self, "Minitor95", eventname, result,)


def caseid_minitor96(self):
    module_other_app.get_datachecklist("Minitor96")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.detail.detail_vehicle_cumulative_kilometers(self, "Minitor96", eventname, result,)


def caseid_minitor97(self):
    module_other_app.get_datachecklist("Minitor97")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.detail.detail_vehicle_stop(self, "Minitor97", eventname, result,)


def caseid_minitor98(self):
    module_other_app.get_datachecklist("Minitor98")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.detail.detail_vehicle_stoping(self, "Minitor98", eventname, result,)



def caseid_minitor99(self):
    module_other_app.get_datachecklist("Minitor99")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.detail.detail_vehicle_stop_and_start_the_engine(self, "Minitor99", eventname, result,)


def caseid_minitor100(self):
    module_other_app.get_datachecklist("Minitor100")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.detail.detail_vehicle_air_condition(self, "Minitor100", eventname, result,)



def caseid_minitor101(self):
    module_other_app.get_datachecklist("Minitor101")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.detail.detail_vehicle_door_vehicle(self, "Minitor101", eventname, result,)


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
    minitor_app.detail.detail_vehicle_drive(self, "Minitor106", eventname, result,)


def caseid_minitor107(self):
    module_other_app.get_datachecklist("Minitor107")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.detail.detail_vehicle_license(self, "Minitor107", eventname, result,)


def caseid_minitor108(self):
    module_other_app.get_datachecklist("Minitor108")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.detail.detail_vehicle_phone(self, "Minitor108", eventname, result,)


def caseid_minitor109(self):
    module_other_app.get_datachecklist("Minitor109")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.detail.detail_vehicle_continuous_driving_time(self, "Minitor109", eventname, result,)


def caseid_minitor110(self):
    module_other_app.get_datachecklist("Minitor110")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.detail.detail_vehicle_driving_time_during_the_day(self, "Minitor110", eventname, result,)


def caseid_minitor111(self):
    module_other_app.get_datachecklist("Minitor111")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.detail.detail_vehicle_number_too_speed(self, "Minitor111", eventname, result,)


def caseid_minitor112(self):
    module_other_app.get_datachecklist("Minitor112")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.detail.detail_vehicle_management_department(self, "Minitor112", eventname, result,)


def caseid_minitor113(self):
    module_other_app.get_datachecklist("Minitor113")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.detail.detail_vehicle_vin(self, "Minitor113", eventname, result,)


def caseid_minitor114(self):
    module_other_app.get_datachecklist("Minitor114")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.detail.detail_vehicle_the_frist_activity(self, "Minitor114", eventname, result,)


def caseid_minitor115(self):
    module_other_app.get_datachecklist("Minitor115")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.detail.detail_vehicle_news_recently(self, "Minitor115", eventname, result,)


def caseid_minitor116(self):
    module_other_app.get_datachecklist("Minitor116")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.detail.detail_vehicle_status_gps(self, "Minitor116", eventname, result,)



def caseid_minitor117(self):
    module_other_app.get_datachecklist("Minitor117")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.detail.detail_vehicle_sim_number2(self, "Minitor117", eventname, result,)


def caseid_minitor118(self):
    module_other_app.get_datachecklist("Minitor118")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.detail.detail_vehicle_subscription_type(self, "Minitor118", eventname, result,)


def caseid_minitor119(self):
    module_other_app.get_datachecklist("Minitor119")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.detail.detail_vehicle_the_remaining_amount(self, "Minitor119", eventname, result,)


def caseid_minitor120(self):
    module_other_app.get_datachecklist("Minitor120")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.detail.detail_vehicle_status_sim(self, "Minitor120", eventname, result,)


def caseid_minitor121(self):
    module_other_app.get_datachecklist("Minitor121")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.detail.detail_vehicle_time_update2(self, "Minitor121", eventname, result,)


def caseid_minitor122(self):
    module_other_app.get_datachecklist("Minitor122")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.detail.detail_vehicle_battert_level(self, "Minitor122", eventname, result,)


def caseid_minitor123(self):
    module_other_app.get_datachecklist("Minitor123")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.detail.detail_vehicle_power_status(self, "Minitor123", eventname, result,)

def caseid_minitor124(self):
    module_other_app.get_datachecklist("Minitor124")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.detail.detail_vehicle_package_name(self, "Minitor124", eventname, result,)


def caseid_minitor125(self):
    module_other_app.get_datachecklist("Minitor125")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.detail.detail_vehicle_home_network(self, "Minitor125", eventname, result,)

def caseid_minitor126(self):
    module_other_app.get_datachecklist("Minitor126")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.detail.detail_vehicle_package_capacity(self, "Minitor126", eventname, result,)

def caseid_minitor127(self):
    module_other_app.get_datachecklist("Minitor127")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.detail.detail_vehicle_number_of_days_of_storage(self, "Minitor127", eventname, result,)

def caseid_minitor128(self):
    module_other_app.get_datachecklist("Minitor128")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.detail.detail_vehicle_number_of_chanels_of_storage(self, "Minitor128", eventname, result,)

def caseid_minitor129(self):
    module_other_app.get_datachecklist("Minitor129")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.detail.detail_vehicle_location(self, "Minitor129", eventname, result,)


def caseid_minitor130(self):
    module_other_app.get_datachecklist("Minitor130")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.detail.detail_vehicle_image(self, "Minitor130", eventname, result,)

def caseid_minitor131(self):
    module_other_app.get_datachecklist("Minitor131")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.detail.detail_vehicle_video(self, "Minitor131", eventname, result,)



def caseid_minitor132(self):
    module_other_app.get_datachecklist("Minitor132")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.detail.detail_vehicle_channel_camera(self, "Minitor132", eventname, result,)


def caseid_minitor133(self):
    module_other_app.get_datachecklist("Minitor133")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.detail.detail_vehicle_channel_active(self, "Minitor133", eventname, result,)

def caseid_minitor134(self):
    module_other_app.get_datachecklist("Minitor134")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.detail.detail_vehicle_network_connection(self, "Minitor134", eventname, result,)


def caseid_minitor135(self):
    module_other_app.get_datachecklist("Minitor135")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.detail.detail_vehicle_icon_update(self, "Minitor135", eventname, result,)


def caseid_minitor136(self):
    module_other_app.get_datachecklist("Minitor136")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.detail.detail_vehicle_monitor_video(self, "Minitor136", eventname, result,)

def caseid_minitor137(self):
    module_other_app.get_datachecklist("Minitor137")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.detail.detail_vehicle_monitor_image(self, "Minitor137", eventname, result,)


def caseid_minitor138(self):
    module_other_app.get_datachecklist("Minitor138")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.detail.detail_vehicle_fuel_chart(self, "Minitor138", eventname, result,)




@retry(tries=3, delay=2, backoff=1, jitter=5, )
def caseid_minitor139(self):
    module_other_app.get_datachecklist("Minitor139")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.affiliate_link.route(self, "Minitor139", eventname, result,)



def caseid_minitor140(self):
    module_other_app.get_datachecklist("Minitor140")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.affiliate_link.affiliate_link_overview(self, "Minitor140", eventname, result,
                                                       var_app.minitor_image, var_app.minitor_imageiconx, var_app.check_minitor_image,
                                                       "GIÁM SÁT HÌNH ẢNH", "_GiamSat_ChiTietXe_HinhAnh.png")


def caseid_minitor141(self):
    module_other_app.get_datachecklist("Minitor141")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.affiliate_link.affiliate_link_overview(self, "Minitor141", eventname, result,
                                                       var_app.minitor_camera, var_app.minitor_cameraiconx, var_app.check_minitor_camera,
                                                       "GIÁM SÁT NHIỀU CAMERA", "_GiamSat_ChiTietXe_Camera.png")


def caseid_minitor142(self):
    module_other_app.get_datachecklist("Minitor142")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.affiliate_link.affiliate_link_detail(self, "Minitor142", eventname, result, 720, 330, 170, 330, 500,
                                                     var_app.minitor_more, var_app.minitor_more_iconx, var_app.check_minitor_more,
                                                     "THIẾT LẬP MỤC ƯA THÍCH", "_GiamSat_Them.png")



def caseid_minitor143(self):
    module_other_app.get_datachecklist("Minitor143")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.affiliate_link.affiliate_link_detail(self, "Minitor143", eventname, result, 725, 670, 180, 670, 500,
                                                     var_app.watch_the_overview_video_again,  var_app.watch_the_overview_video_again_iconx,
                                                     var_app.check_watch_the_overview_video_again, "XEM LẠI VIDEO - TỔNG QUAN", "_GiamSat_XemLaiVideoTongQuan.png")



def caseid_minitor144(self):
    module_other_app.get_datachecklist("Minitor144")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.affiliate_link.affiliate_link_detail(self, "Minitor144", eventname, result, 725, 670, 180, 670, 500,
                                                     var_app.watch_image_camera_nd10, var_app.watch_image_camera_nd10_iconx,
                                                     var_app.check_watch_image_camera_nd10, "CAMERA", "_GiamSat_XemAnhCameraND10.png")


def caseid_minitor145(self):
    module_other_app.get_datachecklist("Minitor145")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.affiliate_link.affiliate_link_detail(self, "Minitor145", eventname, result, 725, 670, 180, 670, 500,
                                                     var_app.extract_video, var_app.extract_video_iconx, var_app.check_extract_video,
                                                     "TRÍCH XUẤT DỮ LIỆU", "_GiamSat_TrichXuatVieo.png")

def caseid_minitor146(self):
    module_other_app.get_datachecklist("Minitor146")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.affiliate_link.affiliate_link_detail(self, "Minitor146", eventname, result, 730, 1015, 180, 1015, 500,
                                                     var_app.report_stop, var_app.report_stop_iconx, var_app.check_report_stop,
                                                     "BÁO CÁO DỪNG ĐỖ", "_GiamSat_BaoCaoDungDo.png")



def caseid_minitor147(self):
    module_other_app.get_datachecklist("Minitor147")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.affiliate_link.affiliate_link_detail(self, "Minitor147", eventname, result, 730, 1015, 180, 1015, 500,
                                                     var_app.detailed_activity_reports, var_app.detailed_activity_reports_iconx, var_app.check_detailed_activity_reports,
                                                     "BÁO CÁO CHI TIẾT HOẠT ĐỘNG", "_GiamSat_BaoCaoChiTietHoatDong.png")

def caseid_minitor148(self):
    module_other_app.get_datachecklist("Minitor148")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.affiliate_link.affiliate_link_detail(self, "Minitor148", eventname, result, 730, 1015, 180, 1015, 500,
                                                     var_app.summary_report_of_activities, var_app.summary_report_of_activities_iconx,
                                                     var_app.check_summary_report_of_activities, "BÁO CÁO TỔNG HỢP HOẠT ĐỘNG", "_GiamSat_BaoCaoTongHopHoatDong.png")

def caseid_minitor149(self):
    module_other_app.get_datachecklist("Minitor149")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.affiliate_link.affiliate_link_detail(self, "Minitor149", eventname, result, 730, 1015, 180, 1015, 500,
                                                     var_app.report_entering_and_exiting_the_station, var_app.report_entering_and_exiting_the_station_iconx,
                                                     var_app.check_report_entering_and_exiting_the_station,
                                                     "BÁO CÁO RA VÀO TRẠM", "_GiamSat_BaoCaoRaVaoTram.png")

def caseid_minitor150(self):
    module_other_app.get_datachecklist("Minitor150")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.affiliate_link.affiliate_link_detail(self, "Minitor150", eventname, result, 730, 1015, 180, 1015, 500,
                                                     var_app.report_speeding, var_app.report_speeding_iconx, var_app.check_report_speeding,
                                                     "BÁO CÁO QUÁ TỐC ĐỘ", "_GiamSat_BaoCaoQuaTocDo.png")


def caseid_minitor151(self):
    module_other_app.get_datachecklist("Minitor151")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.affiliate_link.affiliate_link_detail(self, "Minitor151", eventname, result, 730, 1015, 180, 1015, 500,
                                                     var_app.business_trip_report, var_app.business_trip_report_iconx, var_app.check_business_trip_report,
                                                     "BÁO CÁO CHUYẾN KINH DOANH", "_GiamSat_BaoCaoChuyenKinhDoanh.png")

def caseid_minitor152(self):
    module_other_app.get_datachecklist("Minitor152")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.affiliate_link.affiliate_link_detail(self, "Minitor152", eventname, result, 730, 1015, 180, 1015, 500,
                                                     var_app.report_loss_of_signal, var_app.report_loss_of_signal_iconx, var_app.check_report_loss_of_signal,
                                                     "BÁO CÁO MẤT TÍN HIỆU", "_GiamSat_BaoCaoMatTinHieu.png")
def caseid_minitor153(self):
    module_other_app.get_datachecklist("Minitor153")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.affiliate_link.affiliate_link_detail(self, "Minitor153", eventname, result, 730, 1015, 180, 1015, 500,
                                                     var_app.fuel_dump_report, var_app.fuel_dump_report_iconx, var_app.check_fuel_dump_report,
                                                     "BÁO CÁO ĐỔ HÚT NHIÊN LIỆU", "_GiamSat_BaoCaoDoHutNhienLieu.png")

def caseid_minitor154(self):
    module_other_app.get_datachecklist("Minitor154")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.affiliate_link.affiliate_link_detail(self, "Minitor154", eventname, result, 730, 1015, 180, 1015, 500,
                                                     var_app.engine_report, var_app.engine_report_iconx, var_app.check_engine_report,
                                                     "BÁO CÁO ĐỘNG CƠ", "_GiamSat_BaoCaoDongCo.png")

def caseid_minitor155(self):
    module_other_app.get_datachecklist("Minitor155")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.affiliate_link.affiliate_link_detail(self, "Minitor155", eventname, result, 730, 1015, 180, 1015, 500,
                                                     var_app.fuel_chart, var_app.fuel_chart_iconx, var_app.check_fuel_chart,
                                                     "BIỂU ĐỒ NHIÊN LIỆU", "_GiamSat_BieuDoNhienLieu.png")

def caseid_minitor156(self):
    module_other_app.get_datachecklist("Minitor156")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.affiliate_link.affiliate_link_detail(self, "Minitor156", eventname, result, 730, 1015, 180, 1015, 500,
                                                     var_app.fuel_consumption_report, var_app.fuel_consumption_report_iconx, var_app.check_fuel_consumption_report,
                                                     "BÁO CÁO TIÊU HAO NHIÊN LIỆU", "_GiamSat_BaoCaoTieuHaoNhienLieu.png")


def caseid_minitor157(self):
    module_other_app.get_datachecklist("Minitor157")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.affiliate_link.affiliate_link_detail(self, "Minitor157", eventname, result, 730, 1015, 180, 1015, 500,
                                                     var_app.Comprehensive_fuel_consumption_report, var_app.Comprehensive_fuel_consumption_report_iconx,
                                                     var_app.check_Comprehensive_fuel_consumption_report,
                                                     "BÁO CÁO TỔNG HỢP TIÊU HAO NHIÊN LIỆU", "_GiamSat_BaoCaoTongHopTieuHaoNhienLieu.png")

def caseid_minitor158(self):
    module_other_app.get_datachecklist("Minitor158")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.affiliate_link.affiliate_link_detail(self, "Minitor158", eventname, result, 730, 1015, 180, 1015, 500,
                                                     var_app.vehicle_speed, var_app.vehicle_speed_iconx, var_app.check_vehicle_speed,
                                                     "TỐC ĐỘ CỦA XE", "_GiamSat_TocDoCuaXe.png")


def caseid_minitor159(self):
    module_other_app.get_datachecklist("Minitor159")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.affiliate_link.affiliate_link_detail(self, "Minitor159", eventname, result, 730, 1015, 180, 1015, 500,
                                                     var_app.report_vehicle_violations, var_app.report_vehicle_violations_iconx,
                                                     var_app.check_report_vehicle_violations,
                                                     "BÁO CÁO CHI TIẾT HÀNH VI", "_GiamSat_BaoCaoViPhamLaiXe.png")

def caseid_minitor160(self):
    module_other_app.get_datachecklist("Minitor160")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.affiliate_link.affiliate_link_detail(self, "Minitor160", eventname, result, 730, 1015, 180, 1015, 500,
                                                     var_app.summary_report_of_driving_behavior, var_app.summary_report_of_driving_behavior_iconx,
                                                     var_app.check_summary_report_of_driving_behavior,
                                                     "BÁO CÁO TỔNG HỢP HÀNH VI", "_GiamSat_BaoCaoTongHopHanhViLaiXe.png")

def caseid_minitor161(self):
    module_other_app.get_datachecklist("Minitor161")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.affiliate_link.affiliate_link_detail(self, "Minitor161", eventname, result, 725, 1370, 180, 1370, 500,
                                                     var_app.hide_and_show_the_car, var_app.hide_and_show_the_car_iconx, var_app.check_hide_and_show_the_car,
                                                     "DANH SÁCH XE ĐANG ẨN", "_GiamSat_AnHienXe.png")

def caseid_minitor162(self):
    module_other_app.get_datachecklist("Minitor162")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.affiliate_link.affiliate_link_detail(self, "Minitor162", eventname, result, 725, 1370, 180, 1370, 500,
                                                     var_app.add_driver, var_app.add_driver_iconx, var_app.check_add_driver,
                                                     "NHẬP THÔNG TIN LÁI XE", "_GiamSat_ThemLaiXe.png")

def caseid_minitor163(self):
    module_other_app.get_datachecklist("Minitor163")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.affiliate_link.affiliate_link_detail(self, "Minitor163", eventname, result, 725, 1370, 180, 1370, 500,
                                                     var_app.list_driver, var_app.list_driver_iconx, var_app.check_list_driver,
                                                     "DANH SÁCH LÁI XE", "_GiamSat_DanhSachLaiXe.png")

def caseid_minitor164(self):
    module_other_app.get_datachecklist("Minitor164")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.affiliate_link.affiliate_link_detail(self, "Minitor164", eventname, result, 725, 1370, 180, 1370, 500,
                                                     var_app.fee_information, var_app.fee_information_iconx, var_app.check_fee_information,
                                                     "THÔNG TIN PHÍ", "_GiamSat_ThongTinPhi.png")

def caseid_minitor165(self):
    module_other_app.get_datachecklist("Minitor165")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.affiliate_link.affiliate_link_detail(self, "Minitor165", eventname, result, 725, 1370, 180, 1370, 500,
                                                     var_app.enter_document_information, var_app.enter_document_information_iconx,
                                                     var_app.check_enter_document_information,
                                                     "NHẬP THÔNG TIN GIẤY TỜ", "_GiamSat_NhapThongTinGiayTo.png")

def caseid_minitor166(self):
    module_other_app.get_datachecklist("Minitor166")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.affiliate_link.affiliate_link_detail(self, "Minitor166", eventname, result, 725, 1370, 180, 1370, 500,
                                                     var_app.list_of_documents, var_app.list_of_documents_iconx, var_app.check_list_of_documents,
                                                     "DANH SÁCH GIẤY TỜ", "_GiamSat_DanhSachGiayTo.png")

def caseid_minitor167(self):
    module_other_app.get_datachecklist("Minitor167")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.affiliate_link.affiliate_link_detail(self, "Minitor167", eventname, result, 725, 1370, 180, 1370, 500,
                                                     var_app.support_customer, var_app.support_customer_iconx1, var_app.check_support_customer,
                                                     "HỖ TRỢ KHÁCH HÀNG", "_GiamSat_HoTroKhachHang.png")

def caseid_minitor168(self):
    module_other_app.get_datachecklist("Minitor168")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.affiliate_link.affiliate_link_detail(self, "Minitor168", eventname, result, 725, 1370, 180, 1370, 500,
                                                     var_app.transmission_report, var_app.transmission_report_iconx1, var_app.check_transmission_report,
                                                     "CẢNH BÁO TÍCH TRUYỀN", "_GiamSat_BaoCaoTichTruyen.png")

def caseid_minitor169(self):
    module_other_app.get_datachecklist("Minitor169")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.affiliate_link.affiliate_link_detail(self, "Minitor169", eventname, result, 725, 1370, 180, 1370, 500,
                                                     var_app.record_driver_card, var_app.record_driver_card_iconx, var_app.check_record_driver_card,
                                                     "GHI THẺ LÁI XE", "_GiamSat_GhiTheLaiXe.png")

def caseid_minitor170(self):
    module_other_app.get_datachecklist("Minitor170")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.affiliate_link.affiliate_link_detail(self, "Minitor170", eventname, result, 725, 1370, 180, 1370, 500,
                                                     var_app.list_vehicle, var_app.minitor, var_app.check_list_vehicle,
                                                    "Phương tiện", "_GiamSat_DanhSachPhuongTien.png")




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
    vehicle.overview.select_group_search(self, "Vehicle03", eventname, result)


def caseid_vehicle04(self):
    module_other_app.get_datachecklist("Vehicle04")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    vehicle.overview.select_group_select(self, "Vehicle04", eventname, result)




def caseid_vehicle05(self):
    module_other_app.get_datachecklist("Vehicle05")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    vehicle.overview.arrange_vehicle(self, "Vehicle05", eventname, result, var_app.arrange_vehicle)


def caseid_vehicle06(self):
    module_other_app.get_datachecklist("Vehicle06")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    vehicle.overview.arrange_vehicle(self, "Vehicle06", eventname, result, var_app.arrange_time)

def caseid_vehicle07(self):
    module_other_app.get_datachecklist("Vehicle07")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    vehicle.overview.arrange_vehicle(self, "Vehicle07", eventname, result, var_app.arrange_default)
#
#



def caseid_vehicle08(self):
    module_other_app.get_datachecklist("Vehicle08")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    vehicle.overview.vehicle_status(self, "Vehicle08", eventname, result,
                                        "Nợ phí", 650, 315, "_PhuongTien_TrangThai_NoPhi.png")


def caseid_vehicle09(self):
    module_other_app.get_datachecklist("Vehicle09")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    vehicle.overview.vehicle_status(self, "Vehicle09", eventname, result,
                                        "Di chuyển", 650, 450, "_PhuongTien_TrangThai_DiChuyen.png")


def caseid_vehicle10(self):
    module_other_app.get_datachecklist("Vehicle10")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    vehicle.overview.vehicle_status(self, "Vehicle10", eventname, result,
                                        "Dừng Tắt", 650, 580, "_PhuongTien_TrangThai_DungTat.png")

def caseid_vehicle11(self):
    module_other_app.get_datachecklist("Vehicle11")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    vehicle.overview.vehicle_status(self, "Vehicle11", eventname, result,
                                        "Dừng Bật", 650, 720, "_PhuongTien_TrangThai_DungBat.png")

def caseid_vehicle12(self):
    module_other_app.get_datachecklist("Vehicle12")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    vehicle.overview.vehicle_status(self, "Vehicle12", eventname, result,
                                        "Bật Máy", 650, 830, "_PhuongTien_TrangThai_BatMay.png")

def caseid_vehicle13(self):
    module_other_app.get_datachecklist("Vehicle13")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    vehicle.overview.vehicle_status(self, "Vehicle13", eventname, result,
                                        "Tắt Máy", 650, 950, "_Phuongtien_TrangThai_TatMay.png")

def caseid_vehicle14(self):
    module_other_app.get_datachecklist("Vehicle14")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    vehicle.overview.vehicle_status(self, "Vehicle14", eventname, result,
                                        "Quá tốc độ", 650, 1080, "_PhuongTien_TrangThai_QuaTocDo.png")

def caseid_vehicle15(self):
    module_other_app.get_datachecklist("Vehicle15")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    vehicle.overview.vehicle_status(self, "Vehicle15", eventname, result,
                                        "Mất GPS", 650, 1200, "_PhuongTien_TrangThai_MatGPS.png")

def caseid_vehicle16(self):
    module_other_app.get_datachecklist("Vehicle16")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    vehicle.overview.vehicle_status(self, "Vehicle16", eventname, result,
                                        "Mất GMS", 650, 1330, "_PhuongTien_TrangThai_MatGMS.png")

def caseid_vehicle17(self):
    module_other_app.get_datachecklist("Vehicle17")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    vehicle.overview.vehicle_status(self, "Vehicle17", eventname, result,
                                        "Tất cả", 650, 210, "_PhuongTien_TrangThai_Tatca.png")


def caseid_vehicle18(self):
    module_other_app.get_datachecklist("Vehicle18")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    vehicle.overview.detail_vehicle(self, "Vehicle18", eventname, result)



def caseid_vehicle19(self):
    module_other_app.get_datachecklist("Vehicle19")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    vehicle.overview.check_detail_vehicle(self, "Vehicle19", eventname, result, 6, "_PhuongTien_BienSoXe.png")

def caseid_vehicle20(self):
    module_other_app.get_datachecklist("Vehicle20")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    vehicle.overview.check_detail_vehicle(self, "Vehicle20", eventname, result, 7, "_PhuongTien_ThoiGianCapNhat.png")

def caseid_vehicle21(self):
    module_other_app.get_datachecklist("Vehicle21")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    vehicle.overview.check_detail_vehicle(self, "Vehicle21", eventname, result, 12, "_PhuongTien_DongCo.png")

def caseid_vehicle22(self):
    module_other_app.get_datachecklist("Vehicle22")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    vehicle.overview.check_detail_vehicle(self, "Vehicle22", eventname, result, 10, "_PhuongTien_KmTrongNgay.png")

def caseid_vehicle23(self):
    module_other_app.get_datachecklist("Vehicle23")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    vehicle.overview.check_detail_vehicle(self, "Vehicle23", eventname, result, 8, "_PhuongTien_VanToc.png")

def caseid_vehicle24(self):
    module_other_app.get_datachecklist("Vehicle24")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    vehicle.overview.check_detail_vehicle(self, "Vehicle24", eventname, result, 11, "_PhuongTien_ThoiGianDungDo.png")

def caseid_vehicle25(self):
    module_other_app.get_datachecklist("Vehicle25")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    vehicle.overview.check_detail_vehicle(self, "Vehicle25", eventname, result, 17, "_PhuongTien_NhietDo.png")


def caseid_vehicle26(self):
    module_other_app.get_datachecklist("Vehicle26")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    vehicle.overview.check_detail_vehicle(self, "Vehicle26", eventname, result, 14, "_PhuongTien_DiaChi.png")

def caseid_vehicle27(self):
    module_other_app.get_datachecklist("Vehicle27")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    vehicle.overview.detail_custom(self, "Vehicle27", eventname, result)

def caseid_vehicle28(self):
    module_other_app.get_datachecklist("Vehicle28")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    vehicle.overview.detail_choose_min_favorites(self, "Vehicle28", eventname, result)
#
def caseid_vehicle29(self):
    module_other_app.get_datachecklist("Vehicle29")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    vehicle.overview.detail_custom_search(self, "Vehicle29", eventname, result)




def caseid_toolbar01(self):
    module_other_app.get_datachecklist("Toolbar01")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    homepage_app.toolbar.utility_list(self, "Toolbar01", eventname, result)


def caseid_toolbar02(self):
    module_other_app.get_datachecklist("Toolbar02")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    homepage_app.toolbar.utility_list_search(self, "Toolbar02", eventname, result)


def caseid_toolbar03(self):
    module_other_app.get_datachecklist("Toolbar03")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    homepage_app.toolbar.notification(self, "Toolbar03", eventname, result)

def caseid_toolbar04(self):
    module_other_app.get_datachecklist("Toolbar04")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    homepage_app.toolbar.see_notification(self, "Toolbar04", eventname, result)

def caseid_toolbar05(self):
    module_other_app.get_datachecklist("Toolbar05")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    homepage_app.toolbar.delete_notification(self, "Toolbar05", eventname, result)


def caseid_toolbar06(self):
    module_other_app.get_datachecklist("Toolbar06")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    homepage_app.toolbar.warning_list(self, "Toolbar06", eventname, result)

def caseid_toolbar07(self):
    module_other_app.get_datachecklist("Toolbar07")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    homepage_app.toolbar.warning_list_search(self, "Toolbar07", eventname, result)

def caseid_toolbar08(self):
    module_other_app.get_datachecklist("Toolbar08")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    homepage_app.toolbar.warning_list_mark_as_read(self, "Toolbar08", eventname, result)

def caseid_toolbar09(self):
    module_other_app.get_datachecklist("Toolbar09")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    homepage_app.toolbar.support_customer(self, "Toolbar09", eventname, result)

def caseid_toolbar10(self):
    module_other_app.get_datachecklist("Toolbar10")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    homepage_app.toolbar.support_customer_search(self, "Toolbar10", eventname, result)

def caseid_toolbar11(self):
    module_other_app.get_datachecklist("Toolbar11")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    homepage_app.toolbar.support_customer_link_affiliate(self, "Toolbar11", eventname, result,
                                                         var_app.link_lost_signal, var_app.link_lost_signal_iconx, var_app.check_link_lost_signal,
                                                         "Mất tín hiệu ", "_TrangChu_HoTroKhachHang_MatTinHieu.png")
def caseid_toolbar12(self):
    module_other_app.get_datachecklist("Toolbar12")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    homepage_app.toolbar.support_customer_link_affiliate(self, "Toolbar12", eventname, result,
                                                         var_app.link_change_sea, var_app.link_change_sea_iconx, var_app.check_change_sea,
                                                         "ĐỔI BIỂN", "_TrangChu_HoTroKhachHang_DoiBien.png")

def caseid_toolbar13(self):
    module_other_app.get_datachecklist("Toolbar13")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    homepage_app.toolbar.support_customer_link_affiliate(self, "Toolbar13", eventname, result,
                                                         var_app.link_camera_error, var_app.link_camera_error_iconx, var_app.check_camera_error,
                                                         "Lỗi camera", "_TrangChu_HoTroKhachHang_LoiCamera.png")


def caseid_toolbar14(self):
    module_other_app.get_datachecklist("Toolbar14")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    homepage_app.toolbar.support_customer_link_affiliate(self, "Toolbar14", eventname, result,
                                                         var_app.link_lock_vehicle, var_app.link_lock_vehicle_iconx, var_app.check_lock_vehicle,
                                                         "LÝ DO KHÓA XE", "_TrangChu_HoTroKhachHang_KhoaXe.png")

def caseid_toolbar15(self):
    module_other_app.get_datachecklist("Toolbar15")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    homepage_app.toolbar.support_customer_link_affiliate(self, "Toolbar15", eventname, result,
                                                         var_app.link_unlock_vehicle, var_app.link_unlock_vehicle_iconx, var_app.check_unlock_vehicle,
                                                         "Mở khóa xe", "_TrangChu_HoTroKhachHang_MoKhoaXe.png")

def caseid_toolbar16(self):
    module_other_app.get_datachecklist("Toolbar16")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    homepage_app.toolbar.support_customer_link_affiliate(self, "Toolbar16", eventname, result,
                                                         var_app.link_other_support,  var_app.link_other_support_iconx, var_app.check_other_support,
                                                         "Hỗ trợ khác", "_TrangChu_HoTroKhachHang_HoTroKhac.png")


def caseid_toolbar17(self):
    module_other_app.get_datachecklist("Toolbar17")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    homepage_app.toolbar.support_customer_link_affiliate(self, "Toolbar17", eventname, result,
                                                         var_app.link_pay_fee_dvmc, var_app.link_pay_fee_dvmc_iconx, var_app.check_pay_fee_dvmc,
                                                         "Đóng phí DVMC/SC", "_TrangChu_HoTroKhachHang_DongPhiDVMC.png")
def caseid_toolbar18(self):
    module_other_app.get_datachecklist("Toolbar18")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    homepage_app.toolbar.support_customer_link_affiliate(self, "Toolbar18", eventname, result,
                                                         var_app.link_upgrade, var_app.link_upgrade_iconx, var_app.check_upgrade,
                                                         "Nâng cấp Module 4G", "_TrangChu_HoTroKhachHang_NangCap.png")
def caseid_toolbar19(self):
    module_other_app.get_datachecklist("Toolbar19")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    homepage_app.toolbar.support_customer_link_affiliate(self, "Toolbar19", eventname, result,
                                                         var_app.link_assign_car, var_app.link_assign_car_iconx, var_app.check_ssign_car,
                                                         "CHỌN PHƯƠNG TIỆN", "_TrangChu_HoTroKhachHang_GanXe.png")
def caseid_toolbar20(self):
    module_other_app.get_datachecklist("Toolbar20")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    homepage_app.toolbar.support_customer_link_affiliate(self, "Toolbar20", eventname, result,
                                                         var_app.link_change_channel_camera, var_app.link_change_channel_camera_iconx, var_app.check_change_channel_camera,
                                                         "ĐỔI TÊN KÊNH CAMERA", "_TrangChu_HoTroKhachHang_DoiKenhCamera.png")

def caseid_toolbar21(self):
    module_other_app.get_datachecklist("Toolbar21")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    homepage_app.toolbar.support_customer_link_affiliate(self, "Toolbar21", eventname, result,
                                                         var_app.link_download_video, var_app.link_download_video_iconx, var_app.check_download_video,
                                                         "XEM LẠI VIDEO - TỔNG QUAN", "_TrangChu_HoTroKhachHang_TaiVideo.png")
def caseid_toolbar22(self):
    module_other_app.get_datachecklist("Toolbar22")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    homepage_app.toolbar.support_customer_track_feedback(self, "Toolbar22", eventname, result,
                                                         var_app.status_waiting_for_progressing, var_app.quantity_waiting_for_progressing,
                                                         var_app.check_waiting_for_progressing, "_TrangChu_HoTroKhachHang_ChoXuLy.png")
def caseid_toolbar23(self):
    module_other_app.get_datachecklist("Toolbar23")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    homepage_app.toolbar.support_customer_track_feedback(self, "Toolbar23", eventname, result,
                                                         var_app.status_progressing, var_app.quantity_progressing,
                                                         var_app.check_progressing, "_TrangChu_HoTroKhachHang_DangXuLy.png")

def caseid_toolbar24(self):
    module_other_app.get_datachecklist("Toolbar24")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    homepage_app.toolbar.support_customer_track_complete(self, "Toolbar24", eventname, result)

def caseid_toolbar25(self):
    module_other_app.get_datachecklist("Toolbar25")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    homepage_app.toolbar.support_customer_track_follow_search(self, "Toolbar25", eventname, result)

def caseid_toolbar26(self):
    module_other_app.get_datachecklist("Toolbar26")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    homepage_app.toolbar.support_customer_track_follow_filter(self, "Toolbar26", eventname, result)

def caseid_toolbar27(self):
    module_other_app.get_datachecklist("Toolbar27")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    homepage_app.toolbar.sos(self, "Toolbar27", eventname, result)

def caseid_toolbar28(self):
    module_other_app.get_datachecklist("Toolbar28")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    homepage_app.toolbar.sos_send_sos(self, "Toolbar28", eventname, result)


def caseid_favorite01(self):
    module_other_app.get_datachecklist("Favorite01")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    homepage_app.favorite.more(self, "Favorite01", eventname, result)


def caseid_favorite02(self):
    module_other_app.get_datachecklist("Favorite02")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    homepage_app.favorite.mor_choose_min_favorite(self, "Favorite02", eventname, result)


def caseid_favorite03(self):
    module_other_app.get_datachecklist("Favorite03")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    homepage_app.favorite.more_search(self, "Favorite03", eventname, result)





def caseid_favorite04(self):
    module_other_app.get_datachecklist("Favorite04")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    homepage_app.favorite.favorite_toward(self, "Favorite04", eventname, result, var_app.homepage_minitor,
                                          var_app.check_homepage_minitor, "Phương tiện", "_TrangChu_YeuThich_GiamSat.png")

def caseid_favorite05(self):
    module_other_app.get_datachecklist("Favorite05")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    homepage_app.favorite.favorite_toward(self, "Favorite05", eventname, result, var_app.homepage_route,
                                          var_app.check_homepage_route, "Lộ trình", "_TrangChu_YeuThich_LoTrinh.png")



def caseid_media01(self):
    module_other_app.get_datachecklist("Media01")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    homepage_app.move_module(self, "Media01", eventname, result, var_app.image_monitoring, 725, 765, 175, 765, 500,
                                                    "Trang chủ - Hình ảnh camera - Giám sát hình ảnh", var_app.check_image_monitoring,
                                                     "GIÁM SÁT HÌNH ẢNH", "_TrangChu_GiamSatHinhAnh.png")

def caseid_media02(self):
    module_other_app.get_datachecklist("Media02")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    image_video_app.image_video.image_monitoring_select_group(self, "Media02", eventname, result)

def caseid_media03(self):
    module_other_app.get_datachecklist("Media03")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    image_video_app.image_video.image_monitoring_select_group1(self, "Media03", eventname, result)

def caseid_media04(self):
    module_other_app.get_datachecklist("Media04")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    image_video_app.image_video.image_monitoring_arrange_image(self, "Media04", eventname, result)

def caseid_media05(self):
    module_other_app.get_datachecklist("Media05")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    image_video_app.image_video.image_monitoring_refresh(self, "Media05", eventname, result)
#
def caseid_media06(self):
    module_other_app.get_datachecklist("Media06")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    image_video_app.image_video.image_monitoring_favorite(self, "Media06", eventname, result)

def caseid_media07(self):
    module_other_app.get_datachecklist("Media07")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    image_video_app.image_video.image_monitoring_see_all_image(self, "Media07", eventname, result)

def caseid_media08(self):
    module_other_app.get_datachecklist("Media08")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    image_video_app.image_video.image_monitoring_see_all_image_search(self, "Media08", eventname, result)

def caseid_media09(self):
    module_other_app.get_datachecklist("Media09")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    image_video_app.image_video.image_monitoring_see_all_image_announce(self, "Media09", eventname, result)



def caseid_media10(self):
    module_other_app.get_datachecklist("Media10")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    image_video_app.image_video.image_monitoring_search(self, "Media10", eventname, result)


def caseid_media11(self):
    module_other_app.get_datachecklist("Media11")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    image_video_app.image_video.image_monitoring_select(self, "Media11", eventname, result)


def caseid_media12(self):
    module_other_app.get_datachecklist("Media12")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    image_video_app.image_video.check_image_monitoring_select(self, "Media12", eventname, result,
                                                              var_app.detail_image_time, "_TrangChu_GiamSatHinhAnh_ChiTietAnh_ThoiGian.png")

def caseid_media13(self):
    module_other_app.get_datachecklist("Media13")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    image_video_app.image_video.check_image_monitoring_select(self, "Media13", eventname, result,
                                                              var_app.detail_image_speed, "_TrangChu_GiamSatHinhAnh_ChiTietAnh_VanToc.png")

def caseid_media14(self):
    module_other_app.get_datachecklist("Media14")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    image_video_app.image_video.check_image_monitoring_select(self, "Media14", eventname, result,
                                                              var_app.detail_image_channel, "_TrangChu_GiamSatHinhAnh_ChiTietAnh_Kenh.png")

def caseid_media15(self):
    module_other_app.get_datachecklist("Media15")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    image_video_app.image_video.check_image_monitoring_select(self, "Media15", eventname, result,
                                                              var_app.detail_image_address, "_TrangChu_GiamSatHinhAnh_ChiTietAnh_DiaChi.png")

def caseid_media16(self):
    module_other_app.get_datachecklist("Media16")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    image_video_app.image_video.check_image_monitoring_select1(self, "Media16", eventname, result,
                                                              var_app.detail_image_vehicle, "_TrangChu_GiamSatHinhAnh_ChiTietAnh_BienSo.png")




def caseid_media17(self):
    module_other_app.get_datachecklist("Media17")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    try:
        homepage_app.move_module(self, "Media17", eventname, result, var_app.camera_monitoring, 725, 765, 175, 765, 500,
                                                        "Trang chủ - Hình ảnh video - Giám sát hình ảnh", var_app.check_camera_monitoring,
                                                         "GIÁM SÁT NHIỀU CAMERA", "_TrangChu_GiamSatCamera.png")
    except:
        image_video_app.image_video.camera_monitoring_back(self)
        homepage_app.move_module(self, "Media17", eventname, result, var_app.camera_monitoring, 725, 765, 175, 765, 500,
                                                        "Trang chủ - Hình ảnh video - Giám sát hình ảnh", var_app.check_camera_monitoring,
                                                         "GIÁM SÁT NHIỀU CAMERA", "_TrangChu_GiamSatCamera.png")

def caseid_media18(self):
    module_other_app.get_datachecklist("Media18")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    image_video_app.image_video.camera_monitoring_search(self, "Media18", eventname, result)

def caseid_media19(self):
    module_other_app.get_datachecklist("Media19")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    image_video_app.image_video.camera_monitoring_check_info(self, "Media19", eventname, result,
                                                          var_app.checkcamera_vehicle, "_TrangChu_GiamSatCamera_BienSoXe.png")

def caseid_media20(self):
    module_other_app.get_datachecklist("Media20")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    image_video_app.image_video.camera_monitoring_check_info(self, "Media20", eventname, result,
                                                          var_app.checkcamera_channel, "_TrangChu_GiamSatCamera_Kenh.png")

def caseid_media21(self):
    module_other_app.get_datachecklist("Media21")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    image_video_app.image_video.camera_monitoring_check_info(self, "Media21", eventname, result,
                                                          var_app.checkcamera_timeupdate, "_TrangChu_GiamSatCamera_ThoiGianCapNhat.png")

def caseid_media22(self):
    module_other_app.get_datachecklist("Media22")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    image_video_app.image_video.camera_monitoring_check_info(self, "Media22", eventname, result,
                                                          var_app.checkcamera_address, "_TrangChu_GiamSatCamera_DiaChi.png")

def caseid_media23(self):
    module_other_app.get_datachecklist("Media23")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    image_video_app.image_video.camera_monitoring_check_icon(self, "Media23", eventname, result,
                                                          var_app.camera_icon_pause, "False", "_TrangChu_GiamSatCamera_IconTamDung.png")

def caseid_media24(self):
    module_other_app.get_datachecklist("Media24")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    image_video_app.image_video.camera_monitoring_check_icon(self, "Media24", eventname, result,
                                                          var_app.camera_icon_volumn, "True", "_TrangChu_GiamSatCamera_IconAmThanh.png")

def caseid_media25(self):
    module_other_app.get_datachecklist("Media25")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    image_video_app.image_video.camera_monitoring_check_icon(self, "Media25", eventname, result,
                                                          var_app.camera_icon_take_of_photo, "True", "_TrangChu_GiamSatCamera_IconChupAnh.png")

def caseid_media26(self):
    module_other_app.get_datachecklist("Media26")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    image_video_app.image_video.camera_monitoring_check_icon(self, "Media26", eventname, result,
                                                          "", "True", "_TrangChu_GiamSatCamera_IconToanManHinh.png")
def caseid_media27(self):
    module_other_app.get_datachecklist("Media27")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    image_video_app.image_video.camera_monitoring_check_icon(self, "Media27", eventname, result,
                                                          "", "True", "_TrangChu_GiamSatCamera_IconXoayManHinh.png")

def caseid_media28(self):
    module_other_app.get_datachecklist("Media28")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    image_video_app.image_video.camera_monitoring_check_icon_close(self, "Media28", eventname, result)



def caseid_media29(self):
    module_other_app.get_datachecklist("Media29")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    image_video_app.image_video.camera_monitoring_add_camera(self, "Media29", eventname, result)

def caseid_media30(self):
    module_other_app.get_datachecklist("Media30")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    image_video_app.image_video.camera_monitoring_add_camera_search(self, "Media30", eventname, result)

def caseid_media31(self):
    module_other_app.get_datachecklist("Media31")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    image_video_app.image_video.camera_monitoring_on_the_camera(self, "Media31", eventname, result)


def caseid_media32(self):
    module_other_app.get_datachecklist("Media32")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    image_video_app.image_video.camera_monitoring_reset(self, "Media32", eventname, result)



def caseid_media33(self):
    module_other_app.get_datachecklist("Media33")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    try:
        homepage_app.move_module(self, "Media33", eventname, result, var_app.see_again_video, 725, 765, 175, 765, 500,
                                                        "Trang chủ - Xem lại video - Tổng quan", var_app.check_see_again_video,
                                                         "XEM LẠI VIDEO - TỔNG QUAN", "_TrangChu_XemLaiVideoTongQuan.png")
    except:
        image_video_app.image_video.see_again_video_back(self)
        homepage_app.move_module(self, "Media33", eventname, result, var_app.see_again_video, 725, 765, 175, 765, 500,
                                                        "Trang chủ - Xem lại video - Tổng quan", var_app.check_see_again_video,
                                                         "XEM LẠI VIDEO - TỔNG QUAN", "_TrangChu_XemLaiVideoTongQuan.png")



def caseid_media34(self):
    module_other_app.get_datachecklist("Media34")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    image_video_app.image_video.see_again_video_search(self, "Media34", eventname, result)

def caseid_media35(self):
    module_other_app.get_datachecklist("Media35")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    image_video_app.image_video.see_again_video_search_see_video(self, "Media35", eventname, result)


def caseid_media36(self):
    module_other_app.get_datachecklist("Media36")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    image_video_app.image_video.see_again_video_see_device_search(self, "Media36", eventname, result)

def caseid_media37(self):
    module_other_app.get_datachecklist("Media37")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    image_video_app.image_video.see_again_video_see_device_see_many_channel(self, "Media37", eventname, result)

def caseid_media38(self):
    module_other_app.get_datachecklist("Media38")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    image_video_app.image_video.see_again_manny_video_iconselect_channel(self, "Media38", eventname, result)

def caseid_media39(self):
    module_other_app.get_datachecklist("Media39")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    image_video_app.image_video.see_again_video_see_device_play_automatically(self, "Media39", eventname, result)

def caseid_media40(self):
    module_other_app.get_datachecklist("Media40")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    image_video_app.image_video.see_again_video_see_device_detail(self, "Media40", eventname, result,
                                                                  var_app.check_see_again_many_video_vehicle, "",
                                                                  "_TrangChu_XemLaiVideo_XemThietBi_XemNhieuKenhCuaPhuongTien_BienSo.png")

def caseid_media41(self):
    module_other_app.get_datachecklist("Media41")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    image_video_app.image_video.see_again_video_see_device_detail(self, "Media41", eventname, result,
                                                                  var_app.check_see_again_many_video_time_update, "",
                                                                  "_TrangChu_XemLaiVideo_XemThietBi_XemNhieuKenhCuaPhuongTien_ThoiGianCapNhat.png")

def caseid_media42(self):
    module_other_app.get_datachecklist("Media42")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    image_video_app.image_video.see_again_video_see_device_detail(self, "Media42", eventname, result,
                                                                  var_app.check_see_again_many_video_address, "",
                                                                  "_TrangChu_XemLaiVideo_XemThietBi_XemNhieuKenhCuaPhuongTien_DiaChi.png")

def caseid_media43(self):
    module_other_app.get_datachecklist("Media43")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    image_video_app.image_video.see_again_video_see_device_seevideo(self, "Media43", eventname, result)

def caseid_media44(self):
    module_other_app.get_datachecklist("Media44")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    image_video_app.image_video.see_again_video_see_again_video_iconn(self, "Media44", eventname, result,
                                                                      var_app.see_again_video_icon_pause, "False",
                                                                      "_TrangChu_XemLaiVideo_XemThietBi_ClickVideo_IconTamDung.png")

def caseid_media45(self):
    module_other_app.get_datachecklist("Media45")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    image_video_app.image_video.see_again_video_see_again_video_iconn(self, "Media45", eventname, result,
                                                                      var_app.see_again_video_icon_volume, "True",
                                                                      "_TrangChu_XemLaiVideo_XemThietBi_ClickVideo_IconAmThanh.png")

def caseid_media46(self):
    module_other_app.get_datachecklist("Media46")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    image_video_app.image_video.see_again_video_see_again_video_iconn(self, "Media46", eventname, result,
                                                                      var_app.see_again_video_icon_camera, "True",
                                                                      "_TrangChu_XemLaiVideo_XemThietBi_ClickVideo_IconCamera.png")

def caseid_media47(self):
    module_other_app.get_datachecklist("Media47")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    image_video_app.image_video.see_again_video_see_again_video_iconn(self, "Media47", eventname, result,
                                                                      var_app.see_again_video_icon_fullscreen, "True",
                                                                      "_TrangChu_XemLaiVideo_XemThietBi_ClickVideo_IconToanManHinh.png")

def caseid_media48(self):
    module_other_app.get_datachecklist("Media48")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    image_video_app.image_video.see_again_video_see_again_video_iconcloud(self, "Media48", eventname, result)

def caseid_media49(self):
    module_other_app.get_datachecklist("Media49")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    image_video_app.image_video.see_again_video_see_device_detail1(self, "Media49", eventname, result,
                                                                  var_app.check_see_again_seedevice_vehicle1, "",
                                                                  "_TrangChu_XemLaiVideo_XemThietBi_ClickVideo_BienSo.png")
def caseid_media50(self):
    module_other_app.get_datachecklist("Media50")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    image_video_app.image_video.see_again_video_see_device_detail1(self, "Media50", eventname, result,
                                                                  var_app.check_see_again_seedevice_timeupdate1, "",
                                                                  "_TrangChu_XemLaiVideo_XemThietBi_ClickVideo_ThoiGianCapNhat.png")

def caseid_media51(self):
    module_other_app.get_datachecklist("Media51")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    image_video_app.image_video.see_again_video_see_device_detail1(self, "Media51", eventname, result,
                                                                  var_app.check_see_again_seedevice_address1, "",
                                                                  "_TrangChu_XemLaiVideo_XemThietBi_ClickVideo_DiaChi.png")

def caseid_media52(self):
    module_other_app.get_datachecklist("Media52")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    image_video_app.image_video.see_again_video_see_device_detail1(self, "Media52", eventname, result,
                                                                  var_app.check_see_again_seedevice_channel1, "",
                                                                  "_TrangChu_XemLaiVideo_XemThietBi_ClickVideo_Kenh.png")


def caseid_media53(self):
    module_other_app.get_datachecklist("Media53")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    image_video_app.image_video.see_again_video_see_device_icon_icloud(self, "Media53", eventname, result)

def caseid_media54(self):
    module_other_app.get_datachecklist("Media54")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    image_video_app.image_video.see_again_video_dowload_and_cloud_search(self, "Media54", eventname, result)



def caseid_media55(self):
    module_other_app.get_datachecklist("Media55")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    try:
        homepage_app.move_module(self, "Media55", eventname, result, var_app.see_nd10, 725, 765, 175, 765, 500,
                                                        "Trang chủ - Xem ảnh Camera - NĐ10", var_app.check_see_nd10,
                                                         "CAMERA", "_TrangChu_XemAnhCamera.png")
    except:
        image_video_app.image_video.see_again_video_back(self)
        image_video_app.image_video.see_image_camera_back(self)
        homepage_app.move_module(self, "Media55", eventname, result, var_app.see_nd10, 725, 765, 175, 765, 500,
                                                        "Trang chủ - Xem ảnh Camera - NĐ10", var_app.check_see_nd10,
                                                         "CAMERA", "_TrangChu_XemAnhCamera.png")



def caseid_media56(self):
    module_other_app.get_datachecklist("Media56")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    image_video_app.image_video.see_image_camera_search(self, "Media56", eventname, result)


def caseid_media57(self):
    module_other_app.get_datachecklist("Media57")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    image_video_app.image_video.see_image_camera_icon_notification(self, "Media57", eventname, result)

def caseid_media58(self):
    module_other_app.get_datachecklist("Media58")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    image_video_app.image_video.see_image_camera_select_image(self, "Media58", eventname, result)

def caseid_media59(self):
    module_other_app.get_datachecklist("Media59")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    image_video_app.image_video.see_image_camera_select_image_detail_vehicle(self, "Media59", eventname, result)

def caseid_media60(self):
    module_other_app.get_datachecklist("Media60")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    image_video_app.image_video.see_image_camera_select_image_detail(self, "Media60", eventname, result,
                                                                  var_app.check_see_image_camera_time_update, "",
                                                                  "_TrangChu_XemAnhCamera_ClickVaoAnh_ThoiGianCapNhat.png")
def caseid_media61(self):
    module_other_app.get_datachecklist("Media61")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    image_video_app.image_video.see_image_camera_select_image_detail(self, "Media61", eventname, result,
                                                                  var_app.check_see_image_camera_speed, "",
                                                                  "_TrangChu_XemAnhCamera_ClickVaoAnh_VanToc.png")
def caseid_media62(self):
    module_other_app.get_datachecklist("Media62")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    image_video_app.image_video.see_image_camera_select_image_detail(self, "Media62", eventname, result,
                                                                  var_app.check_see_image_camera_channel, "",
                                                                  "_TrangChu_XemAnhCamera_ClickVaoAnh_Kenh.png")
def caseid_media63(self):
    module_other_app.get_datachecklist("Media63")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    image_video_app.image_video.see_image_camera_select_image_detail(self, "Media63", eventname, result,
                                                                  var_app.check_see_image_camera_address, "",
                                                                  "_TrangChu_XemAnhCamera_ClickVaoAnh_DiaChi.png")
def caseid_media64(self):
    module_other_app.get_datachecklist("Media64")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    image_video_app.image_video.see_image_camera_select_image_icon_download(self, "Media64", eventname, result)

def caseid_media65(self):
    module_other_app.get_datachecklist("Media65")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    try:
        homepage_app.move_module(self, "Media65", eventname, result, var_app.export_video, 725, 765, 175, 765, 500,
                                                        "Trang chủ - Trích xuất video", var_app.check_export_video,
                                                         "TRÍCH XUẤT DỮ LIỆU", "_TrangChu_TrichXuatVideo.png")
    except:
        image_video_app.image_video.export_video_back(self)
        homepage_app.move_module(self, "Media65", eventname, result, var_app.export_video, 725, 765, 175, 765, 500,
                                                        "Trang chủ - Trích xuất video", var_app.check_export_video,
                                                         "TRÍCH XUẤT DỮ LIỆU", "_TrangChu_TrichXuatVideo.png")

def caseid_media66(self):
    module_other_app.get_datachecklist("Media66")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    image_video_app.image_video.export_video_search(self, "Media66", eventname, result)

def caseid_media67(self):
    module_other_app.get_datachecklist("Media67")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    image_video_app.image_video.export_video_Turn_on_wifi(self, "Media67", eventname, result)

def caseid_media68(self):
    module_other_app.get_datachecklist("Media68")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    image_video_app.image_video.export_video_help(self, "Media68", eventname, result)



def caseid_report01(self):
    module_other_app.get_datachecklist("Report01")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    try:
        homepage_app.move_module(self, "Report01", eventname, result, var_app.report_stop, 725, 1100, 175, 1100, 500,
                                                        "Trang chủ - Báo cáo dừng đỗ", var_app.check_report_stop,
                                                         "BÁO CÁO DỪNG ĐỖ", "_TrangChu_BaoCaoDungDo.png")
    except:
        report_app.general.report_back(self)
        homepage_app.move_module(self, "Report01", eventname, result, var_app.report_stop, 725, 1100, 175, 1100, 500,
                                                        "Trang chủ - Báo cáo dừng đỗ", var_app.check_report_stop,
                                                         "BÁO CÁO DỪNG ĐỖ", "_TrangChu_BaoCaoDungDo.png")


def caseid_report02(self):
    module_other_app.get_datachecklist("Report02")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.report_stop_search(self, "Report02", eventname, result)


def caseid_report03(self):
    module_other_app.get_datachecklist("Report03")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.report_stop_search_type(self, "Report03", eventname, result, var_app.report_today,
                                              var_app.check_report_search, "Trang chủ - báo cáo dừng đỗ", "_BaoCao_BaoCaoDungDo_HomNay.png")

def caseid_report04(self):
    module_other_app.get_datachecklist("Report04")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.report_stop_search_type(self, "Report04", eventname, result, var_app.report_7day,
                                              var_app.check_report_search, "Trang chủ - báo cáo dừng đỗ", "_BaoCao_BaoCaoDungDo_7Ngay.png")

def caseid_report05(self):
    module_other_app.get_datachecklist("Report05")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.report_stop_search_type(self, "Report05", eventname, result, var_app.report_15day,
                                              var_app.check_report_search, "Trang chủ - báo cáo dừng đỗ", "_BaoCao_BaoCaoDungDo_15Ngay.png")

def caseid_report06(self):
    module_other_app.get_datachecklist("Report06")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.report_stop_search_type(self, "Report06", eventname, result, var_app.report_other,
                                              var_app.check_report_stop_other, "Trang chủ - báo cáo dừng đỗ", "_BaoCao_BaoCaoDungDo_Khac.png")

def caseid_report07(self):
    module_other_app.get_datachecklist("Report07")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.report_stop_setting(self, "Report07", eventname, result)

def caseid_report08(self):
    module_other_app.get_datachecklist("Report08")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.report_stop_filter(self, "Report08", eventname, result)

def caseid_report09(self):
    module_other_app.get_datachecklist("Report09")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.report_stop_export_excel(self, "Report09", eventname, result)

def caseid_report10(self):
    module_other_app.get_datachecklist("Report10")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.report_stop_detail(self, "Report10", eventname, result, var_app.report_stop_time_stop1,
                                         "Tổng thời gian dừng đỗ (phút):", "_BaoCao_BaoCaoDungDo_TongThoiGianDungDo1.png")

def caseid_report11(self):
    module_other_app.get_datachecklist("Report11")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.report_stop_detail(self, "Report11", eventname, result, var_app.report_stop_time_stop2,
                                         "Tổng thời gian dừng đỗ:", "_BaoCao_BaoCaoDungDo_TongThoiGianDungDo2.png")

def caseid_report12(self):
    module_other_app.get_datachecklist("Report12")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.report_stop_detail(self, "Report12", eventname, result, var_app.report_stop_time3,
                                         "Tổng thời gian nổ máy khi dừng (phút):", "_BaoCao_BaoCaoDungDo_TongThoiGianNoMayKhiDung.png")

def caseid_report13(self):
    module_other_app.get_datachecklist("Report13")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.report_stop_detail(self, "Report13", eventname, result, var_app.report_stop_time4,
                                         "Tổng thời gian bật điều hòa khi dừng (phút):", "_BaoCao_BaoCaoDungDo_TongThoiGianBatDieuHoa.png")

def caseid_report14(self):
    module_other_app.get_datachecklist("Report14")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.report_stop_check_column(self, "Report14", eventname, result)



def caseid_report15(self):
    module_other_app.get_datachecklist("Report15")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    try:
        homepage_app.move_module(self, "Report15", eventname, result, var_app.detailed_activity_reports, 725, 1100, 175, 1100, 500,
                                                        "Trang chủ - Báo cáo chi tiết hoạt động", var_app.check_detailed_activity_reports,
                                                         "BÁO CÁO CHI TIẾT HOẠT ĐỘNG", "_TrangChu_BaoCaoChiTietHoatDong.png")
    except:
        report_app.general.report_back(self)
        homepage_app.move_module(self, "Report15", eventname, result, var_app.detailed_activity_reports, 725, 1100, 175, 1100, 500,
                                                        "Trang chủ - Báo cáo chi tiết hoạt động", var_app.check_detailed_activity_reports,
                                                         "BÁO CÁO CHI TIẾT HOẠT ĐỘNG", "_TrangChu_BaoCaoChiTietHoatDong.png")

def caseid_report16(self):
    module_other_app.get_datachecklist("Report16")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.detailed_activity_reports_search(self, "Report16", eventname, result)

def caseid_report17(self):
    module_other_app.get_datachecklist("Report17")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.report_stop_search_type(self, "Report17", eventname, result, var_app.report_today,
                                              var_app.check_report_search, "Trang chủ - Báo cáo chi tiết hoạt động", "_TrangChu_BaoCaoChiTietHoatDong_HomNay.png")

def caseid_report18(self):
    module_other_app.get_datachecklist("Report18")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.report_stop_search_type(self, "Report18", eventname, result, var_app.report_7day,
                                              var_app.check_report_search, "Trang chủ - Báo cáo chi tiết hoạt động", "_TrangChu_BaoCaoChiTietHoatDong_7Ngay.png")

def caseid_report19(self):
    module_other_app.get_datachecklist("Report19")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.report_stop_search_type(self, "Report19", eventname, result, var_app.report_15day,
                                              var_app.check_report_search, "Trang chủ - Báo cáo chi tiết hoạt động", "_TrangChu_BaoCaoChiTietHoatDong_15Ngay.png")

def caseid_report20(self):
    module_other_app.get_datachecklist("Report20")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.report_stop_search_type(self, "Report20", eventname, result, var_app.report_other,
                                              var_app.check_report_stop_other, "Trang chủ - Báo cáo chi tiết hoạt động", "_TrangChu_BaoCaoChiTietHoatDong_Khac.png")

def caseid_report21(self):
    module_other_app.get_datachecklist("Report21")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.detailed_activity_reports_setting(self, "Report21", eventname, result)


def caseid_report22(self):
    module_other_app.get_datachecklist("Report22")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.detailed_activity_reports_excel(self, "Report22", eventname, result)


def caseid_report23(self):
    module_other_app.get_datachecklist("Report23")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.detailed_activity_reports_detail(self, "Report23", eventname, result, var_app.report_detail1,
                                         "Tổng số lít nhiên liệu tiêu thụ:", "_TrangChu_BaoCaoChiTietHoatDong_TongSoLitNhienLieu.png")

def caseid_report24(self):
    module_other_app.get_datachecklist("Report24")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.detailed_activity_reports_detail(self, "Report24", eventname, result, var_app.report_detail2,
                                         "Tổng Thời gian hoạt động:", "_TrangChu_BaoCaoChiTietHoatDong_TongThoiGianHoatDong.png")

def caseid_report25(self):
    module_other_app.get_datachecklist("Report25")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.detailed_activity_reports_detail(self, "Report25", eventname, result, var_app.report_detail3,
                                         "Tổng số Km GPS:", "_TrangChu_BaoCaoChiTietHoatDong_TongSoKmGps.png")
def caseid_report26(self):
    module_other_app.get_datachecklist("Report26")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.detailed_activity_reports_detail(self, "Report26", eventname, result, var_app.report_detail4,
                                         "Tổng số Km Cơ:", "_TrangChu_BaoCaoChiTietHoatDong_TongSoKmCo.png")

def caseid_report27(self):
    module_other_app.get_datachecklist("Report27")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.detailed_activity_reports_detail(self, "Report27", eventname, result, var_app.report_detail5,
                                         "Tổng số định mức nhiên liệu:", "_TrangChu_BaoCaoChiTietHoatDong_TongSoDinhMucNhienLieu.png")

def caseid_report28(self):
    module_other_app.get_datachecklist("Report28")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.detailed_activity_reports_column(self, "Report28", eventname, result)





def caseid_report29(self):
    module_other_app.get_datachecklist("Report29")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    try:
        homepage_app.move_module(self, "Report29", eventname, result, var_app.summary_report_of_activities, 725, 1100, 175, 1100, 500,
                                                        "Trang chủ - Báo cáo tổng hợp hoạt động", var_app.check_summary_report_of_activities,
                                                         "BÁO CÁO TỔNG HỢP HOẠT ĐỘNG", "_TrangChu_BaoCaoTongHopHoatDong.png")
    except:
        report_app.general.report_back(self)
        homepage_app.move_module(self, "Report29", eventname, result, var_app.summary_report_of_activities, 725, 1100, 175, 1100, 500,
                                                        "Trang chủ - Báo cáo tổng hợp hoạt động", var_app.check_summary_report_of_activities,
                                                         "BÁO CÁO TỔNG HỢP HOẠT ĐỘNG", "_TrangChu_BaoCaoTongHopHoatDong.png")

def caseid_report30(self):
    module_other_app.get_datachecklist("Report30")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.summary_report_of_activities_search(self, "Report30", eventname, result)


def caseid_report31(self):
    module_other_app.get_datachecklist("Report31")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.summary_report_of_activities_type(self, "Report31", eventname, result, var_app.report_today,
                                              var_app.check_report_search, "Trang chủ - Báo cáo tổng hợp hoạt động", "_TrangChu_BaoCaoTongHopHoatDong_HomNay.png")

def caseid_report32(self):
    module_other_app.get_datachecklist("Report32")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.summary_report_of_activities_type(self, "Report32", eventname, result, var_app.report_7day,
                                              var_app.check_report_search, "Trang chủ - Báo cáo tổng hợp hoạt động", "_TrangChu_BaoCaoTongHopHoatDong_7Ngay.png")

def caseid_report33(self):
    module_other_app.get_datachecklist("Report33")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.summary_report_of_activities_type(self, "Report33", eventname, result, var_app.report_15day,
                                              var_app.check_report_search, "Trang chủ - Báo cáo tổng hợp hoạt động", "_TrangChu_BaoCaoTongHopHoatDong_15Ngay.png")

def caseid_report34(self):
    module_other_app.get_datachecklist("Report34")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.summary_report_of_activities_type(self, "Report34", eventname, result, var_app.report_other,
                                              var_app.check_report_stop_other, "Trang chủ - Báo cáo tổng hợp hoạt động", "_TrangChu_BaoCaoTongHopHoatDong_Khac.png")


def caseid_report35(self):
    module_other_app.get_datachecklist("Report35")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.summary_report_of_activities_setting(self, "Report35", eventname, result)

def caseid_report36(self):
    module_other_app.get_datachecklist("Report36")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.summary_report_of_activities_filter(self, "Report36", eventname, result)

def caseid_report37(self):
    module_other_app.get_datachecklist("Report37")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.summary_report_of_activities_excel(self, "Report37", eventname, result)

def caseid_report38(self):
    module_other_app.get_datachecklist("Report38")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.summary_report_of_activities_detail(self, "Report38", eventname, result, var_app.report_detail1,
                                         "Tổng thời gian lăn bánh:", "_TrangChu_BaoCaoTongHopHoatDong_TongThoiGianLanBanh.png")

def caseid_report39(self):
    module_other_app.get_datachecklist("Report39")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.summary_report_of_activities_detail(self, "Report39", eventname, result, var_app.report_detail2,
                                         "Tổng Km GPS:", "_TrangChu_BaoCaoTongHopHoatDong_TongKmGps.png")

def caseid_report40(self):
    module_other_app.get_datachecklist("Report40")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.summary_report_of_activities_detail(self, "Report40", eventname, result, var_app.report_detail3,
                                         "Tổng Km cơ:", "_TrangChu_BaoCaoTongHopHoatDong_TongKmCo.png")

def caseid_report41(self):
    module_other_app.get_datachecklist("Report41")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.summary_report_of_activities_detail(self, "Report41", eventname, result, var_app.report_detail4,
                                         "Tổng số lần dừng đỗ:", "_TrangChu_BaoCaoTongHopHoatDong_TongSoLanDungDo.png")

def caseid_report42(self):
    module_other_app.get_datachecklist("Report42")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.summary_report_of_activities_detail(self, "Report42", eventname, result, var_app.report_detail5,
                                         "Tổng số lần dừng đỗ bật điều hòa:", "_TrangChu_BaoCaoTongHopHoatDong_TongSoLanDungDoBatDieuHoa.png")

def caseid_report43(self):
    module_other_app.get_datachecklist("Report43")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.summary_report_of_activities_detail(self, "Report43", eventname, result, var_app.report_detail6,
                                         "Trung bình vận tốc cao nhất:", "_TrangChu_BaoCaoTongHopHoatDong_TrungBinhVanTocCaoNhat.png")

def caseid_report44(self):
    module_other_app.get_datachecklist("Report44")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.summary_report_of_activities_detail(self, "Report44", eventname, result, var_app.report_detail7,
                                         "Trung bình Vận tốc trung bình:", "_TrangChu_BaoCaoTongHopHoatDong_TrungBinhVanTocTrungBinh.png")


def caseid_report45(self):
    module_other_app.get_datachecklist("Report45")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.summary_report_of_activities_column(self, "Report45", eventname, result)




def caseid_report46(self):
    module_other_app.get_datachecklist("Report46")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    try:
        homepage_app.move_module(self, "Report46", eventname, result, var_app.report_entering_and_exiting_the_station, 725, 1100, 175, 1100, 500,
                                                        "Trang chủ - Báo cáo ra vào trạm", var_app.check_report_entering_and_exiting_the_station,
                                                         "BÁO CÁO RA VÀO TRẠM", "_TrangChu_BaoCaoRaVaotram.png")
    except:
        report_app.general.report_back(self)
        homepage_app.move_module(self, "Report46", eventname, result, var_app.report_entering_and_exiting_the_station, 725, 1100, 175, 1100, 500,
                                                        "Trang chủ - Báo cáo ra vào trạm", var_app.check_report_entering_and_exiting_the_station,
                                                         "BÁO CÁO RA VÀO TRẠM", "_TrangChu_BaoCaoRaVaotram.png")


def caseid_report47(self):
    module_other_app.get_datachecklist("Report47")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.report_entering_and_exiting_the_station_search(self, "Report47", eventname, result)

def caseid_report48(self):
    module_other_app.get_datachecklist("Report48")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.report_entering_and_exiting_the_station_type(self, "Report48", eventname, result, var_app.report_today,
                                              var_app.check_report_search, "Trang chủ - Báo cáo ra vào trạm", "_TrangChu_BaoCaoRaVaotram_HomNay.png")

def caseid_report49(self):
    module_other_app.get_datachecklist("Report49")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.report_entering_and_exiting_the_station_type(self, "Report49", eventname, result, var_app.report_7day,
                                              var_app.check_report_search, "Trang chủ - Báo cáo ra vào trạm", "_TrangChu_BaoCaoRaVaotram_7Ngay.png")

def caseid_report50(self):
    module_other_app.get_datachecklist("Report50")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.report_entering_and_exiting_the_station_type(self, "Report50", eventname, result, var_app.report_15day,
                                              var_app.check_report_search, "Trang chủ - Báo cáo ra vào trạm", "_TrangChu_BaoCaoRaVaotram_15Ngay.png")

def caseid_report51(self):
    module_other_app.get_datachecklist("Report51")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.report_entering_and_exiting_the_station_type(self, "Report51", eventname, result, var_app.report_other,
                                              var_app.check_report_stop_other, "Trang chủ - Báo cáo ra vào trạm", "_TrangChu_BaoCaoRaVaotram_Khac.png")

def caseid_report52(self):
    module_other_app.get_datachecklist("Report52")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.report_entering_and_exiting_the_station_setting(self, "Report52", eventname, result)

def caseid_report53(self):
    module_other_app.get_datachecklist("Report53")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.report_entering_and_exiting_the_station_filter(self, "Report53", eventname, result)

def caseid_report54(self):
    module_other_app.get_datachecklist("Report54")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.report_entering_and_exiting_the_station_excel(self, "Report54", eventname, result)


def caseid_report55(self):
    module_other_app.get_datachecklist("Report55")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.report_entering_and_exiting_the_station_column(self, "Report55", eventname, result)



def caseid_report56(self):
    module_other_app.get_datachecklist("Report56")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    try:
        homepage_app.move_module(self, "Report56", eventname, result, var_app.report_speeding, 725, 1100, 175, 1100, 500,
                                                        "Trang chủ - Báo cáo quá tốc độ", var_app.check_report_speeding,
                                                         "BÁO CÁO QUÁ TỐC ĐỘ", "_TrangChu_BaoCaoQuaTocDo.png")
    except:
        report_app.general.report_back(self)
        homepage_app.move_module(self, "Report56", eventname, result, var_app.report_speeding, 725, 1100, 175, 1100, 500,
                                                        "Trang chủ - Báo cáo quá tốc độ", var_app.check_report_speeding,
                                                         "BÁO CÁO QUÁ TỐC ĐỘ", "_TrangChu_BaoCaoQuaTocDo.png")

def caseid_report57(self):
    module_other_app.get_datachecklist("Report57")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.report_speeding_search(self, "Report57", eventname, result)


def caseid_report58(self):
    module_other_app.get_datachecklist("Report58")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.report_speeding_type(self, "Report58", eventname, result, var_app.report_today)

def caseid_report59(self):
    module_other_app.get_datachecklist("Report59")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.report_speeding_type(self, "Report59", eventname, result, var_app.report_7day)

def caseid_report60(self):
    module_other_app.get_datachecklist("Report60")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.report_speeding_type(self, "Report60", eventname, result, var_app.report_15day)

def caseid_report61(self):
    module_other_app.get_datachecklist("Report61")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.report_speeding_type(self, "Report61", eventname, result, var_app.report_other)

def caseid_report62(self):
    module_other_app.get_datachecklist("Report62")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.report_speeding_setting(self, "Report62", eventname, result,)

def caseid_report63(self):
    module_other_app.get_datachecklist("Report63")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.report_speeding_filter(self, "Report63", eventname, result,)

def caseid_report64(self):
    module_other_app.get_datachecklist("Report64")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.report_speeding_excel(self, "Report64", eventname, result,)
    report_app.general.report_back(self)


def caseid_report65(self):
    module_other_app.get_datachecklist("Report65")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    try:
        homepage_app.move_module(self, "Report65", eventname, result, var_app.business_trip_report, 725, 1100, 175, 1100, 500,
                                                        "Trang chủ - Báo cáo chuyến kinh doanh", var_app.check_business_trip_report,
                                                         "BÁO CÁO CHUYẾN KINH DOANH", "_TrangChu_BaoCaoChuyenKinhDoanh.png")
    except:
        report_app.general.report_back(self)
        homepage_app.move_module(self, "Report65", eventname, result, var_app.business_trip_report, 725, 1100, 175, 1100, 500,
                                                        "Trang chủ - Báo cáo chuyến kinh doanh", var_app.check_business_trip_report,
                                                         "BÁO CÁO CHUYẾN KINH DOANH", "_TrangChu_BaoCaoChuyenKinhDoanh.png")


def caseid_report66(self):
    module_other_app.get_datachecklist("Report66")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.business_trip_report_search(self, "Report66", eventname, result,)

def caseid_report67(self):
    module_other_app.get_datachecklist("Report67")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.business_trip_report_type(self, "Report67", eventname, result, var_app.report_today,
                                              var_app.check_report_search, "Trang chủ - Báo cáo chuyến kinh doanh", "_TrangChu_BaoCaoChuyenKinhDoanh_HomNay.png")

def caseid_report68(self):
    module_other_app.get_datachecklist("Report68")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.business_trip_report_type(self, "Report68", eventname, result, var_app.report_7day,
                                              var_app.check_report_search, "Trang chủ - Báo cáo chuyến kinh doanh", "_TrangChu_BaoCaoChuyenKinhDoanh_7Ngay.png")

def caseid_report69(self):
    module_other_app.get_datachecklist("Report69")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.business_trip_report_type(self, "Report69", eventname, result, var_app.report_15day,
                                              var_app.check_report_search, "Trang chủ - Báo cáo chuyến kinh doanh", "_TrangChu_BaoCaoChuyenKinhDoanh_15Ngay.png")

def caseid_report70(self):
    module_other_app.get_datachecklist("Report70")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.business_trip_report_type(self, "Report70", eventname, result, var_app.report_other,
                                              var_app.check_report_stop_other, "Trang chủ - Báo cáo chuyến kinh doanh", "_TrangChu_BaoCaoChuyenKinhDoanh_Khac.png")

def caseid_report71(self):
    module_other_app.get_datachecklist("Report71")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.business_trip_report_setting(self, "Report71", eventname, result,)

def caseid_report72(self):
    module_other_app.get_datachecklist("Report72")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.business_trip_report_filter(self, "Report72", eventname, result,)

def caseid_report73(self):
    module_other_app.get_datachecklist("Report73")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.business_trip_report_excel(self, "Report73", eventname, result,)

def caseid_report74(self):
    module_other_app.get_datachecklist("Report74")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.business_trip_report_detail(self, "Report74", eventname, result, var_app.report_detail1,
                                         "Tổng số phút hoạt động:", "TrangChu_BaoCaoChuyenKinhDoanh_TongSoPhutHoatDong.png")

def caseid_report75(self):
    module_other_app.get_datachecklist("Report75")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.business_trip_report_detail(self, "Report75", eventname, result, var_app.report_detail2,
                                         "Tổng km GPS:", "TrangChu_BaoCaoChuyenKinhDoanh_TongKmGps.png")

def caseid_report76(self):
    module_other_app.get_datachecklist("Report76")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.business_trip_report_detail(self, "Report76", eventname, result, var_app.report_detail3,
                                         "Tổng km cơ:", "TrangChu_BaoCaoChuyenKinhDoanh_TongKmCo.png")

def caseid_report77(self):
    module_other_app.get_datachecklist("Report77")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.business_trip_report_detail(self, "Report77", eventname, result, var_app.report_detail4,
                                         "Tổng NL tiêu thụ:", "TrangChu_BaoCaoChuyenKinhDoanh_TongNhienLieuTieuThu.png")

def caseid_report78(self):
    module_other_app.get_datachecklist("Report78")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.business_trip_report_detail(self, "Report78", eventname, result, var_app.report_detail5,
                                         "Tổng NL tiêu thụ định mức:", "TrangChu_BaoCaoChuyenKinhDoanh_TongNhienLieuTieuThuDinhMuc.png")

def caseid_report79(self):
    module_other_app.get_datachecklist("Report79")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.business_trip_report_column(self, "Report79", eventname, result,)

def caseid_report80(self):
    module_other_app.get_datachecklist("Report80")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    try:
        homepage_app.move_module(self, "Report80", eventname, result, var_app.report_loss_of_signal, 725, 1100, 175, 1100, 500,
                                                        "Trang chủ - Báo cáo mất tín hiệu", var_app.check_report_loss_of_signal,
                                                         "BÁO CÁO MẤT TÍN HIỆU", "_TrangChu_BaoCaoMatTinHieu.png")
    except:
        report_app.general.report_back(self)
        homepage_app.move_module(self, "Report80", eventname, result, var_app.report_loss_of_signal, 725, 1100, 175, 1100, 500,
                                                        "Trang chủ - Báo cáo mất tín hiệu", var_app.check_report_loss_of_signal,
                                                         "BÁO CÁO MẤT TÍN HIỆU", "_TrangChu_BaoCaoMatTinHieu.png")

def caseid_report81(self):
    module_other_app.get_datachecklist("Report81")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.report_loss_of_signal_search(self, "Report81", eventname, result, )



def caseid_report82(self):
    module_other_app.get_datachecklist("Report82")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.report_loss_of_signal_type(self, "Report82", eventname, result, var_app.report_today,
                                              var_app.check_report_search, "Trang chủ - Báo cáo mất tín hiệu", "_TrangChu_BaoCaoMatTinHieu_HomNay.png")

def caseid_report83(self):
    module_other_app.get_datachecklist("Report83")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.report_loss_of_signal_type(self, "Report83", eventname, result, var_app.report_7day,
                                              var_app.check_report_search, "Trang chủ - Báo cáo mất tín hiệu", "_TrangChu_BaoCaoMatTinHieu_7Ngay.png")

def caseid_report84(self):
    module_other_app.get_datachecklist("Report84")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.report_loss_of_signal_type(self, "Report84", eventname, result, var_app.report_15day,
                                              var_app.check_report_search, "Trang chủ - Báo cáo mất tín hiệu", "_TrangChu_BaoCaoMatTinHieu_15Ngay.png")

def caseid_report85(self):
    module_other_app.get_datachecklist("Report85")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.report_loss_of_signal_type(self, "Report85", eventname, result, var_app.report_other,
                                              var_app.check_report_stop_other, "Trang chủ - Báo cáo mất tín hiệu", "_TrangChu_BaoCaoMatTinHieu_Khac.png")

def caseid_report86(self):
    module_other_app.get_datachecklist("Report86")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.report_loss_of_signal_setting(self, "Report86", eventname, result, )

def caseid_report87(self):
    module_other_app.get_datachecklist("Report87")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.report_loss_of_signal_filter(self, "Report87", eventname, result, )



def caseid_report88(self):
    module_other_app.get_datachecklist("Report88")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.report_loss_of_signal_excel(self, "Report88", eventname, result)



def caseid_report89(self):
    module_other_app.get_datachecklist("Report89")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.report_loss_of_signal_detail(self, "Report89", eventname, result, var_app.report_detail1,
                                         "Tổng thời gian mất tín hiệu:", "_TrangChu_BaoCaoMatTinHieu_TongThoiGianMatTinHieu.png")

def caseid_report90(self):
    module_other_app.get_datachecklist("Report90")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.report_loss_of_signal_column(self, "Report90", eventname, result)


def caseid_report91(self):
    module_other_app.get_datachecklist("Report91")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    try:
        homepage_app.move_module(self, "Report91", eventname, result, var_app.fuel_dump_report, 725, 1100, 175, 1100, 500,
                                                        "Trang chủ - Báo cáo đổ hút nhiên liệu", var_app.check_fuel_dump_report,
                                                         "BÁO CÁO ĐỔ HÚT NHIÊN LIỆU", "_TrangChu_BaoCaoDoHutNhienLieu.png")
    except:
        report_app.general.report_back(self)
        homepage_app.move_module(self, "Report91", eventname, result, var_app.fuel_dump_report, 725, 1100, 175, 1100, 500,
                                                        "Trang chủ - Báo cáo đổ hút nhiên liệu", var_app.check_fuel_dump_report,
                                                         "BÁO CÁO ĐỔ HÚT NHIÊN LIỆU", "_TrangChu_BaoCaoDoHutNhienLieu.png")


def caseid_report92(self):
    module_other_app.get_datachecklist("Report92")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.fuel_dump_report_search(self, "Report92", eventname, result)


def caseid_report93(self):
    module_other_app.get_datachecklist("Report93")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.fuel_dump_report_type(self, "Report93", eventname, result, var_app.report_today,
                                              var_app.check_report_search, "Trang chủ - Báo cáo đổ hút nhiên liệu", "_TrangChu_BaoCaoDoHutNhienLieu_HomNay.png")

def caseid_report94(self):
    module_other_app.get_datachecklist("Report94")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.fuel_dump_report_type(self, "Report94", eventname, result, var_app.report_7day,
                                              var_app.check_report_search, "Trang chủ - Báo cáo đổ hút nhiên liệu", "_TrangChu_BaoCaoDoHutNhienLieu_7Ngay.png")

def caseid_report95(self):
    module_other_app.get_datachecklist("Report95")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.fuel_dump_report_type(self, "Report95", eventname, result, var_app.report_15day,
                                              var_app.check_report_search, "Trang chủ - Báo cáo đổ hút nhiên liệu", "_TrangChu_BaoCaoDoHutNhienLieu_15Ngay.png")

def caseid_report96(self):
    module_other_app.get_datachecklist("Report96")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.fuel_dump_report_type(self, "Report96", eventname, result, var_app.report_other,
                                              var_app.check_report_stop_other, "Trang chủ - Báo cáo đổ hút nhiên liệu", "_TrangChu_BaoCaoDoHutNhienLieu_Khac.png")

def caseid_report97(self):
    module_other_app.get_datachecklist("Report97")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.fuel_dump_report_setting(self, "Report97", eventname, result)

def caseid_report98(self):
    module_other_app.get_datachecklist("Report98")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.fuel_dump_report_filter(self, "Report98", eventname, result)

def caseid_report99(self):
    module_other_app.get_datachecklist("Report99")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.fuel_dump_report_excel(self, "Report99", eventname, result)


def caseid_report100(self):
    module_other_app.get_datachecklist("Report100")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.fuel_dump_report_detail(self, "Report100", eventname, result, var_app.report_detail1,
                                         "Tổng số lít thay đổi:", "_TrangChu_BaoCaoMatTinHieu_TongSoLitThayDoi.png")

def caseid_report101(self):
    module_other_app.get_datachecklist("Report101")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.fuel_dump_report_column(self, "Report101", eventname, result)


def caseid_report102(self):
    module_other_app.get_datachecklist("Report102")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    try:
        homepage_app.move_module(self, "Report102", eventname, result, var_app.engine_report, 725, 1100, 175, 1100, 500,
                                                        "Trang chủ - Báo cáo động cơ", var_app.check_engine_report,
                                                         "BÁO CÁO ĐỘNG CƠ", "_TrangChu_BaoCaoDongCo.png")
    except:
        report_app.general.report_back(self)
        homepage_app.move_module(self, "Report102", eventname, result, var_app.engine_report, 725, 1100, 175, 1100, 500,
                                                        "Trang chủ - Báo cáo động cơ", var_app.check_engine_report,
                                                         "BÁO CÁO ĐỘNG CƠ", "_TrangChu_BaoCaoDongCo.png")


def caseid_report103(self):
    module_other_app.get_datachecklist("Report103")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.engine_report_search(self, "Report103", eventname, result)



def caseid_report104(self):
    module_other_app.get_datachecklist("Report104")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.engine_report_type(self, "Report104", eventname, result, var_app.report_today,
                                              var_app.check_report_search, "Trang chủ - Báo cáo động cơ", "_TrangChu_BaoCaoDongCo_HomNay.png")

def caseid_report105(self):
    module_other_app.get_datachecklist("Report105")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.engine_report_type(self, "Report105", eventname, result, var_app.report_7day,
                                              var_app.check_report_search, "Trang chủ - Báo cáo động cơ", "_TrangChu_BaoCaoDongCo_7Ngay.png")

def caseid_report106(self):
    module_other_app.get_datachecklist("Report106")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.engine_report_type(self, "Report106", eventname, result, var_app.report_15day,
                                              var_app.check_report_search, "Trang chủ - Báo cáo động cơ", "_TrangChu_BaoCaoDongCo_15Ngay.png")

def caseid_report107(self):
    module_other_app.get_datachecklist("Report107")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.engine_report_type(self, "Report107", eventname, result, var_app.report_other,
                                              var_app.check_report_stop_other, "Trang chủ - Báo cáo động cơ", "_TrangChu_BaoCaoDongCo_Khac.png")

def caseid_report108(self):
    module_other_app.get_datachecklist("Report108")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.engine_report_setting(self, "Report108", eventname, result)

def caseid_report109(self):
    module_other_app.get_datachecklist("Report109")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.engine_report_filter(self, "Report109", eventname, result)


def caseid_report110(self):
    module_other_app.get_datachecklist("Report110")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.engine_report_excel(self, "Report110", eventname, result)

def caseid_report111(self):
    module_other_app.get_datachecklist("Report111")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.engine_report_detail(self, "Report111", eventname, result, var_app.report_detail1,
                                         "Tổng số phút:", "_TrangChu_BaoCaoDongCo_TongSoPhut.png")

def caseid_report112(self):
    module_other_app.get_datachecklist("Report112")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.engine_report_column(self, "Report112", eventname, result)



def caseid_report113(self):
    module_other_app.get_datachecklist("Report113")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    try:
        homepage_app.move_module(self, "Report113", eventname, result, var_app.detail_vehicle_fuel_chart, 725, 1100, 175, 1100, 500,
                                                        "Trang chủ - Biểu đồ nhiên liệu", var_app.check_detail_vehicle_fuel_chart,
                                                         "BIỂU ĐỒ NHIÊN LIỆU", "_TrangChu_BieuDoNhienLieu.png")
    except:
        report_app.general.report_back(self)
        homepage_app.move_module(self, "Report113", eventname, result, var_app.detail_vehicle_fuel_chart, 725, 1100, 175, 1100, 500,
                                                        "Trang chủ - Biểu đồ nhiên liệu", var_app.check_detail_vehicle_fuel_chart,
                                                         "BIỂU ĐỒ NHIÊN LIỆU", "_TrangChu_BieuDoNhienLieu.png")

def caseid_report114(self):
    module_other_app.get_datachecklist("Report114")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.detail_vehicle_fuel_chart_search(self, "Report114", eventname, result)

def caseid_report115(self):
    module_other_app.get_datachecklist("Report115")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.detail_vehicle_fuel_chart_filter(self, "Report115", eventname, result)




def caseid_report116(self):
    module_other_app.get_datachecklist("Report116")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    try:
        homepage_app.move_module(self, "Report116", eventname, result, var_app.fuel_consumption_report, 725, 1100, 175, 1100, 500,
                                                        "Trang chủ - Báo cáo tiêu hao nhiên liệu", var_app.check_fuel_consumption_report,
                                                         "BÁO CÁO TIÊU HAO NHIÊN LIỆU", "_TrangChu_BaoCaoTieuHaoNhienLieu.png")
    except:
        report_app.general.report_back(self)
        homepage_app.move_module(self, "Report116", eventname, result, var_app.fuel_consumption_report, 725, 1100, 175, 1100, 500,
                                                        "Trang chủ - Báo cáo tiêu hao nhiên liệu", var_app.check_fuel_consumption_report,
                                                         "BÁO CÁO TIÊU HAO NHIÊN LIỆU", "_TrangChu_BaoCaoTieuHaoNhienLieu.png")


def caseid_report117(self):
    module_other_app.get_datachecklist("Report117")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.fuel_consumption_report_search(self, "Report117", eventname, result)



def caseid_report118(self):
    module_other_app.get_datachecklist("Report118")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.fuel_consumption_report_type(self, "Report118", eventname, result, var_app.report_today,
                                              var_app.check_report_search, "Trang chủ - Báo cáo tiêu hao nhiên liệu", "_TrangChu_BaoCaoTieuHaoNhienLieu_HomNay.png")

def caseid_report119(self):
    module_other_app.get_datachecklist("Report119")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.fuel_consumption_report_type(self, "Report119", eventname, result, var_app.report_7day,
                                              var_app.check_report_search, "Trang chủ - Báo cáo tiêu hao nhiên liệu", "_TrangChu_BaoCaoTieuHaoNhienLieu_7Ngay.png")

def caseid_report120(self):
    module_other_app.get_datachecklist("Report120")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.fuel_consumption_report_type(self, "Report120", eventname, result, var_app.report_15day,
                                              var_app.check_report_search, "Trang chủ - Báo cáo tiêu hao nhiên liệu", "_TrangChu_BaoCaoTieuHaoNhienLieu_15Ngay.png")

def caseid_report121(self):
    module_other_app.get_datachecklist("Report121")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.fuel_consumption_report_type(self, "Report121", eventname, result, var_app.report_other,
                                              var_app.check_report_stop_other, "Trang chủ - Báo cáo tiêu hao nhiên liệu", "_TrangChu_BaoCaoTieuHaoNhienLieu_Khac.png")


def caseid_report122(self):
    module_other_app.get_datachecklist("Report122")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.fuel_consumption_report_bapgs(self, "Report122", eventname, result)

def caseid_report123(self):
    module_other_app.get_datachecklist("Report123")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.fuel_consumption_report_setting(self, "Report123", eventname, result)

def caseid_report124(self):
    module_other_app.get_datachecklist("Report124")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.fuel_consumption_report_excel(self, "Report124", eventname, result)


def caseid_report125(self):
    module_other_app.get_datachecklist("Report125")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.fuel_consumption_report_detail(self, "Report125", eventname, result, var_app.report_detail1,
                                         "Tổng số lần đổ:", "_TrangChu_BaoCaoTieuHaoNhienLieu_TongSoLanDo.png")

def caseid_report126(self):
    module_other_app.get_datachecklist("Report126")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.fuel_consumption_report_detail(self, "Report126", eventname, result, var_app.report_detail2,
                                         "Tổng số lần hút:", "_TrangChu_BaoCaoTieuHaoNhienLieu_TongSoLanHut.png")

def caseid_report127(self):
    module_other_app.get_datachecklist("Report127")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.fuel_consumption_report_detail(self, "Report127", eventname, result, var_app.report_detail3,
                                         "Tổng số lít đầu ngày:", "_TrangChu_BaoCaoTieuHaoNhienLieu_TongSoLitDauNgay.png")

def caseid_report128(self):
    module_other_app.get_datachecklist("Report128")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.fuel_consumption_report_detail(self, "Report128", eventname, result, var_app.report_detail4,
                                         "Tổng số lít đổ:", "_TrangChu_BaoCaoTieuHaoNhienLieu_TongSoLitDo.png")

def caseid_report129(self):
    module_other_app.get_datachecklist("Report129")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.fuel_consumption_report_detail(self, "Report129", eventname, result, var_app.report_detail5,
                                         "Tổng số lít hút:", "_TrangChu_BaoCaoTieuHaoNhienLieu_TongSoLitHut.png")

def caseid_report130(self):
    module_other_app.get_datachecklist("Report130")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.fuel_consumption_report_detail(self, "Report130", eventname, result, var_app.report_detail6,
                                         "Tổng số lít tồn:", "_TrangChu_BaoCaoTieuHaoNhienLieu_TongSoLitTon.png")

def caseid_report131(self):
    module_other_app.get_datachecklist("Report131")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.fuel_consumption_report_detail(self, "Report131", eventname, result, var_app.report_detail7,
                                         "Tổng số lít tiêu hao:", "_TrangChu_BaoCaoTieuHaoNhienLieu_TongSoLitTieuHao.png")



def caseid_report132(self):
    module_other_app.get_datachecklist("Report132")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.fuel_consumption_report_detail(self, "Report132", eventname, result, var_app.report_detail8,
                                         "Tổng số Km GPS:", "_TrangChu_BaoCaoTieuHaoNhienLieu_TongSoKmGps.png")

def caseid_report133(self):
    module_other_app.get_datachecklist("Report133")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.fuel_consumption_report_detail(self, "Report133", eventname, result, var_app.report_detail9,
                                         "Tổng thời gian nổ máy (phút):", "_TrangChu_BaoCaoTieuHaoNhienLieu_TongThoiGianNoMay.png")

def caseid_report134(self):
    module_other_app.get_datachecklist("Report134")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.fuel_consumption_report_detail(self, "Report134", eventname, result, var_app.report_detail10,
                                         "Tổng thời gian dừng đỗ nổ máy (phút):", "_TrangChu_BaoCaoTieuHaoNhienLieu_TongThoiGianDungDoNoMay.png")

def caseid_report135(self):
    pass
    # module_other_app.get_datachecklist("Report135")
    # eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    # result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    # report_app.report.fuel_consumption_report_detail(self, "Report135", eventname, result, var_app.report_detail11,
    #                                      "Tổng định mức quy định:", "_TrangChu_BaoCaoTieuHaoNhienLieu_TongMucQuyDinh.png")

def caseid_report136(self):
    pass
    # module_other_app.get_datachecklist("Report136")
    # eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    # result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    # report_app.report.fuel_consumption_report_detail(self, "Report136", eventname, result, var_app.report_detail12,
    #                                      "Tổng định mức thực tế:", "_TrangChu_BaoCaoTieuHaoNhienLieu_TongDinhMucThucTe.png")

def caseid_report137(self):
    module_other_app.get_datachecklist("Report137")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.fuel_consumption_report_column(self, "Report137", eventname, result,)




def caseid_report138(self):
    module_other_app.get_datachecklist("Report138")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    try:
        homepage_app.move_module(self, "Report138", eventname, result, var_app.Comprehensive_fuel_consumption_report, 725, 1100, 175, 1100, 500,
                                                        "Trang chủ - Báo cáo tổng hợp tiêu hao nhiên liệu", var_app.check_Comprehensive_fuel_consumption_report,
                                                         "BÁO CÁO TỔNG HỢP TIÊU HAO NHIÊN LIỆU", "_TrangChu_BaoCaoTongHopTieuHaoNhienLieu.png")
    except:
        report_app.general.report_back(self)
        homepage_app.move_module(self, "Report138", eventname, result, var_app.Comprehensive_fuel_consumption_report, 725, 1100, 175, 1100, 500,
                                                        "Trang chủ - Báo cáo tổng hợp tiêu hao nhiên liệu", var_app.check_Comprehensive_fuel_consumption_report,
                                                         "BÁO CÁO TỔNG HỢP TIÊU HAO NHIÊN LIỆU", "_TrangChu_BaoCaoTongHopTieuHaoNhienLieu.png")

def caseid_report139(self):
    module_other_app.get_datachecklist("Report139")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.Comprehensive_fuel_consumption_report_search(self, "Report139", eventname, result,)

def caseid_report140(self):
    module_other_app.get_datachecklist("Report140")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.Comprehensive_fuel_consumption_report_type(self, "Report140", eventname, result, var_app.report_today,
                                              var_app.check_report_search, "Trang chủ - Báo cáo tổng hợp tiêu hao nhiên liệu", "_TrangChu_BaoCaoTongHopTieuHaoNhienLieu_HomNay.png")

def caseid_report141(self):
    module_other_app.get_datachecklist("Report141")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.Comprehensive_fuel_consumption_report_type(self, "Report141", eventname, result, var_app.report_7day,
                                              var_app.check_report_search, "Trang chủ - Báo cáo tổng hợp tiêu hao nhiên liệu", "_TrangChu_BaoCaoTongHopTieuHaoNhienLieu_7Ngay.png")

def caseid_report142(self):
    module_other_app.get_datachecklist("Report142")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.Comprehensive_fuel_consumption_report_type(self, "Report142", eventname, result, var_app.report_15day,
                                              var_app.check_report_search, "Trang chủ - Báo cáo tổng hợp tiêu hao nhiên liệu", "_TrangChu_BaoCaoTongHopTieuHaoNhienLieu_15Ngay.png")

def caseid_report143(self):
    module_other_app.get_datachecklist("Report143")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.Comprehensive_fuel_consumption_report_type(self, "Report143", eventname, result, var_app.report_other,
                                              var_app.check_report_stop_other, "Trang chủ - Báo cáo tổng hợp tiêu hao nhiên liệu", "_TrangChu_BaoCaoTongHopTieuHaoNhienLieu_Khac.png")

def caseid_report144(self):
    module_other_app.get_datachecklist("Report144")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.Comprehensive_fuel_consumption_report_bapgs(self, "Report144", eventname, result,)

def caseid_report145(self):
    module_other_app.get_datachecklist("Report145")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.Comprehensive_fuel_consumption_report_setting(self, "Report145", eventname, result,)

def caseid_report146(self):
    module_other_app.get_datachecklist("Report146")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.Comprehensive_fuel_consumption_report_excel(self, "Report146", eventname, result,)

def caseid_report147(self):
    module_other_app.get_datachecklist("Report147")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.Comprehensive_fuel_consumption_report_detail(self, "Report147", eventname, result, var_app.report_detail1,
                                         "Tổng số lần đổ:", "_TrangChu_BaoCaoTongHopTieuHaoNhienLieu_TongSoLanDo.png")

def caseid_report148(self):
    module_other_app.get_datachecklist("Report148")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.Comprehensive_fuel_consumption_report_detail(self, "Report148", eventname, result, var_app.report_detail2,
                                         "Tổng số lần hút:", "_TrangChu_BaoCaoTongHopTieuHaoNhienLieu_TongSoLanHut.png")

def caseid_report149(self):
    module_other_app.get_datachecklist("Report149")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.Comprehensive_fuel_consumption_report_detail(self, "Report149", eventname, result, var_app.report_detail3,
                                         "Tổng số lít đầu ngày:", "_TrangChu_BaoCaoTongHopTieuHaoNhienLieu_TongSoLitDauNgay.png")

def caseid_report150(self):
    module_other_app.get_datachecklist("Report150")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.Comprehensive_fuel_consumption_report_detail(self, "Report150", eventname, result, var_app.report_detail4,
                                         "Tổng số lít đổ:", "_TrangChu_BaoCaoTongHopTieuHaoNhienLieu_TongSoLitDo.png")

def caseid_report151(self):
    module_other_app.get_datachecklist("Report151")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.Comprehensive_fuel_consumption_report_detail(self, "Report151", eventname, result, var_app.report_detail5,
                                         "Tổng số lít hút:", "_TrangChu_BaoCaoTongHopTieuHaoNhienLieu_TongSoLitHut.png")

def caseid_report152(self):
    module_other_app.get_datachecklist("Report152")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.Comprehensive_fuel_consumption_report_detail(self, "Report152", eventname, result, var_app.report_detail6,
                                         "Tổng số lít tồn:", "_TrangChu_BaoCaoTongHopTieuHaoNhienLieu_TongSoLitTon.png")

def caseid_report153(self):
    module_other_app.get_datachecklist("Report153")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.Comprehensive_fuel_consumption_report_detail(self, "Report153", eventname, result, var_app.report_detail7,
                                         "Tổng số lít tiêu hao:", "_TrangChu_BaoCaoTongHopTieuHaoNhienLieu_TongSoLitTieuHao.png")



def caseid_report154(self):
    module_other_app.get_datachecklist("Report154")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.Comprehensive_fuel_consumption_report_detail(self, "Report154", eventname, result, var_app.report_detail8,
                                         "Tổng số Km GPS:", "_TrangChu_BaoCaoTongHopTieuHaoNhienLieu_TongSoKmGps.png")

def caseid_report155(self):
    module_other_app.get_datachecklist("Report155")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.Comprehensive_fuel_consumption_report_detail(self, "Report155", eventname, result, var_app.report_detail9,
                                         "Tổng thời gian nổ máy (phút):", "_TrangChu_BaoCaoTongHopTieuHaoNhienLieu_TongThoiGianNoMay.png")

def caseid_report156(self):
    module_other_app.get_datachecklist("Report156")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.Comprehensive_fuel_consumption_report_detail(self, "Report156", eventname, result, var_app.report_detail10,
                                         "Tổng thời gian dừng đỗ nổ máy (phút):", "_TrangChu_BaoCaoTongHopTieuHaoNhienLieu_TongThoiGianDungDoNoMay.png")



def caseid_report157(self):
    module_other_app.get_datachecklist("Report157")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.Comprehensive_fuel_consumption_report_detail(self, "Report157", eventname, result, var_app.report_detail11,
                                         "Tổng định mức thực tế:", "_TrangChu_BaoCaoTongHopTieuHaoNhienLieu_TongDinhMucThucTe.png")

def caseid_report158(self):
    pass
    # module_other_app.get_datachecklist("Report158")
    # eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    # result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    # report_app.report.Comprehensive_fuel_consumption_report_detail(self, "Report158", eventname, result, var_app.report_detail12,
    #                                      "Tổng định mức quy định:", "_TrangChu_BaoCaoTongHopTieuHaoNhienLieu_TongMucQuyDinh.png")
#


def caseid_report159(self):
    module_other_app.get_datachecklist("Report159")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.Comprehensive_fuel_consumption_report_column(self, "Report159", eventname, result)


def caseid_report160(self):
    module_other_app.get_datachecklist("Report160")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    try:
        homepage_app.move_module(self, "Report160", eventname, result, var_app.vehicle_speed, 725, 1100, 175, 1100, 500,
                                                        "Trang chủ - Tốc độ của xe", var_app.check_vehicle_speed,
                                                         "TỐC ĐỘ CỦA XE", "_TrangChu_TocDoCuaXe.png")
    except:
        report_app.general.report_back(self)
        homepage_app.move_module(self, "Report160", eventname, result, var_app.vehicle_speed, 725, 1100, 175, 1100, 500,
                                                        "Trang chủ - Tốc độ của xe", var_app.check_vehicle_speed,
                                                         "TỐC ĐỘ CỦA XE", "_TrangChu_TocDoCuaXe.png")

def caseid_report161(self):
    module_other_app.get_datachecklist("Report161")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.vehicle_speed_search(self, "Report161", eventname, result)


def caseid_report162(self):
    module_other_app.get_datachecklist("Report162")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.vehicle_speed_type(self, "Report162", eventname, result, var_app.report_today,
                                              var_app.check_report_search, "Trang chủ - Tốc độ của xe", "_TrangChu_TocDoCuaXe_HomNay.png")

def caseid_report163(self):
    module_other_app.get_datachecklist("Report163")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.vehicle_speed_type(self, "Report163", eventname, result, var_app.report_7day,
                                              var_app.check_report_search, "Trang chủ - Tốc độ của xe", "_TrangChu_TocDoCuaXe_7Ngay.png")

def caseid_report164(self):
    module_other_app.get_datachecklist("Report164")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.vehicle_speed_type(self, "Report164", eventname, result, var_app.report_15day,
                                              var_app.check_report_search, "Trang chủ - Tốc độ của xe", "_TrangChu_TocDoCuaXe_15Ngay.png")

def caseid_report165(self):
    module_other_app.get_datachecklist("Report165")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.vehicle_speed_type(self, "Report165", eventname, result, var_app.report_other,
                                              var_app.check_report_stop_other, "Trang chủ - Tốc độ của xe", "_TrangChu_TocDoCuaXe_Khac.png")

def caseid_report166(self):
    module_other_app.get_datachecklist("Report166")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.vehicle_speed_setting(self, "Report166", eventname, result)


def caseid_report167(self):
    module_other_app.get_datachecklist("Report167")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.vehicle_speed_filter(self, "Report167", eventname, result)


def caseid_report168(self):
    module_other_app.get_datachecklist("Report168")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.vehicle_speed_excel(self, "Report168", eventname, result)


def caseid_report169(self):
    module_other_app.get_datachecklist("Report169")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.vehicle_speed_column(self, "Report169", eventname, result)


def caseid_report170(self):
    module_other_app.get_datachecklist("Report170")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    try:
        homepage_app.move_module(self, "Report170", eventname, result, var_app.report_vehicle_violations, 725, 1100, 175, 1100, 500,
                                                        "Trang chủ - Báo cáo vi phạm lái xe", var_app.check_report_vehicle_violations,
                                                         "BÁO CÁO CHI TIẾT HÀNH VI", "_TrangChu_BaoCaoViPhamLaiXe.png")
    except:
        report_app.general.report_back(self)
        homepage_app.move_module(self, "Report170", eventname, result, var_app.report_vehicle_violations, 725, 1100, 175, 1100, 500,
                                                        "Trang chủ - Báo cáo vi phạm lái xe", var_app.check_report_vehicle_violations,
                                                         "BÁO CÁO CHI TIẾT HÀNH VI", "_TrangChu_BaoCaoViPhamLaiXe.png")




def caseid_utilities01(self):
    module_other_app.get_datachecklist("Utilities01")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    try:
        login_app.login.login_v3(self, "ungroup", "12341234")
        utilities.move_module1(self, "Utilities01", eventname, result, var_app.list_vehicle, 725, 1100, 175, 1100, 500,
                                                        "Trang chủ - Danh sách phương tiện", var_app.check_list_vehicle,
                                                         "Phương tiện", "_TrangChu_DanhSachPhuongTien.png")
    except:
        utilities.general.utilities_back(self)
        utilities.move_module1(self, "Utilities01", eventname, result, var_app.list_vehicle, 725, 1100, 175, 1100, 500,
                                                        "Trang chủ - Danh sách phương tiện", var_app.check_list_vehicle,
                                                         "Phương tiện", "_TrangChu_DanhSachPhuongTien.png")


def caseid_utilities02(self):
    module_other_app.get_datachecklist("Utilities02")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    try:
        login_app.login.check_logout1(self, "KHÔNG NHÓM ĐỘI", "ungroup", "12341234")
        utilities.move_module1(self, "Utilities02", eventname, result, var_app.hide_and_show_the_car, 725, 1100, 175, 1100, 500,
                                                        "Trang chủ - Ẩn hiện xe", var_app.check_hide_and_show_the_car,
                                                         "DANH SÁCH XE ĐANG ẨN", "_TrangChu_AnHienXe.png")
    except:
        utilities.general.utilities_back(self)
        login_app.login.check_logout1(self, "KHÔNG NHÓM ĐỘI", "ungroup", "12341234")
        utilities.move_module1(self, "Utilities02", eventname, result, var_app.hide_and_show_the_car, 725, 1100, 175, 1100, 500,
                                                        "Trang chủ - Ẩn hiện xe", var_app.check_hide_and_show_the_car,
                                                         "DANH SÁCH XE ĐANG ẨN", "_TrangChu_AnHienXe.png")

def caseid_utilities03(self):
    module_other_app.get_datachecklist("Utilities03")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    utilities.utilities.hide_and_show_the_car_filter(self, "Utilities03", eventname, result)

def caseid_utilities04(self):
    module_other_app.get_datachecklist("Utilities04")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    utilities.utilities.hide_and_show_the_car_excel(self, "Utilities04", eventname, result)

def caseid_utilities05(self):
    module_other_app.get_datachecklist("Utilities05")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    utilities.utilities.hide_and_show_the_car_search(self, "Utilities05", eventname, result)

def caseid_utilities06(self):
    module_other_app.get_datachecklist("Utilities06")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    utilities.utilities.hide_and_show_the_car_checkbox(self, "Utilities06", eventname, result)

def caseid_utilities07(self):
    module_other_app.get_datachecklist("Utilities07")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    utilities.utilities.hide_and_show_the_car_icon_hide(self, "Utilities07", eventname, result)


def caseid_utilities08(self):
    module_other_app.get_datachecklist("Utilities08")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    utilities.utilities.hide_and_show_the_car_hide_vehicle(self, "Utilities08", eventname, result)

def caseid_utilities09(self):
    module_other_app.get_datachecklist("Utilities09")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    utilities.utilities.hide_and_show_the_car_un_hide_vehicle(self, "Utilities09", eventname, result)



def caseid_utilities10(self):
    module_other_app.get_datachecklist("Utilities10")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    try:
        utilities.move_module1(self, "Utilities10", eventname, result, var_app.add_driver, 725, 1100, 175, 1100, 500,
                                                        "Trang chủ - Thêm lái xe", var_app.check_add_driver,
                                                         "NHẬP THÔNG TIN LÁI XE", "_TrangChu_ThemLaiXe.png")
    except:
        utilities.general.utilities_back(self)
        utilities.move_module1(self, "Utilities10", eventname, result, var_app.add_driver, 725, 1100, 175, 1100, 500,
                                                        "Trang chủ - Thêm lái xe", var_app.check_add_driver,
                                                         "NHẬP THÔNG TIN LÁI XE", "_TrangChu_ThemLaiXe.png")


def caseid_utilities11(self):
    module_other_app.get_datachecklist("Utilities11")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    utilities.utilities.add_driver_fill_info(self, "Utilities11", eventname, result)



def caseid_utilities12(self):
    module_other_app.get_datachecklist("Utilities12")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    try:
        utilities.move_module1(self, "Utilities12", eventname, result, var_app.list_driver, 725, 1100, 175, 1100, 500,
                                                        "Trang chủ - Danh sách phương tiện", var_app.check_list_driver,
                                                         "DANH SÁCH LÁI XE", "_TrangChu_DanhSachPhuongTien.png")
    except:
        utilities.general.utilities_back(self)
        utilities.move_module1(self, "Utilities12", eventname, result, var_app.list_driver, 725, 1100, 175, 1100, 500,
                                                        "Trang chủ - Danh sách phương tiện", var_app.check_list_driver,
                                                         "DANH SÁCH LÁI XE", "_TrangChu_DanhSachPhuongTien.png")


def caseid_utilities13(self):
    module_other_app.get_datachecklist("Utilities13")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    utilities.utilities.list_driver_search(self, "Utilities13", eventname, result)



def caseid_utilities14(self):
    module_other_app.get_datachecklist("Utilities14")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    utilities.utilities.list_driver_select_vehicle(self, "Utilities14", eventname, result)



def caseid_utilities15(self):
    module_other_app.get_datachecklist("Utilities15")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    utilities.utilities.list_driver_check_info(self, "Utilities15", eventname, result, var_app.list_driver_check_info_vehicle,
                                               "_TrangChu_DanhSachPhuongTien_BienSoXe.png")

def caseid_utilities16(self):
    module_other_app.get_datachecklist("Utilities16")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    utilities.utilities.list_driver_check_info(self, "Utilities16", eventname, result, var_app.list_driver_check_info_type_liscense,
                                               "_TrangChu_DanhSachPhuongTien_LoaiBangLai.png")

def caseid_utilities17(self):
    module_other_app.get_datachecklist("Utilities17")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    utilities.utilities.list_driver_check_info(self, "Utilities17", eventname, result, var_app.list_driver_check_info_phone_number,
                                               "_TrangChu_DanhSachPhuongTien_SoDienThoai.png")

def caseid_utilities18(self):
    module_other_app.get_datachecklist("Utilities18")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    utilities.utilities.list_driver_check_info(self, "Utilities18", eventname, result, var_app.list_driver_check_info_expiration_date,
                                               "_TrangChu_DanhSachPhuongTien_NgayHetHan.png")

def caseid_utilities19(self):
    module_other_app.get_datachecklist("Utilities19")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    utilities.utilities.list_driver_icon_add(self, "Utilities19", eventname, result)



def caseid_utilities20(self):
    module_other_app.get_datachecklist("Utilities20")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    try:
        utilities.move_module1(self, "Utilities20", eventname, result, var_app.info_fee, 725, 1100, 175, 1100, 500,
                                                        "Trang chủ - Thông tin phí", var_app.check_info_fee,
                                                         "THÔNG TIN PHÍ", "_TrangChu_ThongTinPhi.png")
    except:
        utilities.general.utilities_back(self)
        utilities.move_module1(self, "Utilities20", eventname, result, var_app.info_fee, 725, 1100, 175, 1100, 500,
                                                        "Trang chủ - Thông tin phí", var_app.check_info_fee,
                                                         "THÔNG TIN PHÍ", "_TrangChu_ThongTinPhi.png")

def caseid_utilities21(self):
    module_other_app.get_datachecklist("Utilities21")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    utilities.utilities.info_fee_vehicle_owes_fees(self, "Utilities21", eventname, result)

def caseid_utilities22(self):
    module_other_app.get_datachecklist("Utilities22")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    utilities.utilities.info_fee_search_fee(self, "Utilities22", eventname, result)


def caseid_utilities23(self):
    module_other_app.get_datachecklist("Utilities23")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    utilities.utilities.info_fee_iconbagps(self, "Utilities23", eventname, result)



def caseid_utilities24(self):
    module_other_app.get_datachecklist("Utilities24")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    try:
        utilities.move_module1(self, "Utilities24", eventname, result, var_app.support_customer, 725, 1100, 175, 1100, 500,
                                                        "Trang chủ - Hỗ trợ khách hàng", var_app.check_support_customer,
                                                         "HỖ TRỢ KHÁCH HÀNG", "_TrangChu_HoTroKhachHang.png")
    except:
        utilities.general.utilities_back(self)
        utilities.move_module1(self, "Utilities24", eventname, result, var_app.support_customer, 725, 1100, 175, 1100, 500,
                                                        "Trang chủ - Hỗ trợ khách hàng", var_app.check_support_customer,
                                                         "HỖ TRỢ KHÁCH HÀNG", "_TrangChu_HoTroKhachHang.png")

def caseid_utilities25(self):
    module_other_app.get_datachecklist("Utilities25")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    utilities.utilities.support_customer_list_support(self, "Utilities25", eventname, result)

def caseid_utilities26(self):
    module_other_app.get_datachecklist("Utilities26")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    utilities.utilities.support_customer_track_feedback(self, "Utilities26", eventname, result)


def caseid_utilities27(self):
    module_other_app.get_datachecklist("Utilities27")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    try:
        utilities.move_module1(self, "Utilities27", eventname, result, var_app.transmission_report, 725, 1100, 175, 1100, 500,
                                                        "Trang chủ - Cảnh báo tích truyền", var_app.check_transmission_report,
                                                         "CẢNH BÁO TÍCH TRUYỀN", "_TrangChu_CanhBaoTichTruyen.png")
    except:
        utilities.general.utilities_back(self)
        utilities.move_module1(self, "Utilities27", eventname, result, var_app.transmission_report, 725, 1100, 175, 1100, 500,
                                                        "Trang chủ - Cảnh báo tích truyền", var_app.check_transmission_report,
                                                         "CẢNH BÁO TÍCH TRUYỀN", "_TrangChu_CanhBaoTichTruyen.png")

def caseid_utilities28(self):
    module_other_app.get_datachecklist("Utilities28")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    utilities.utilities.transmission_report_search(self, "Utilities28", eventname, result)

def caseid_utilities29(self):
    module_other_app.get_datachecklist("Utilities29")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    utilities.utilities.transmission_report_select_vehicle(self, "Utilities29", eventname, result)

def caseid_utilities30(self):
    module_other_app.get_datachecklist("Utilities30")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    utilities.utilities.transmission_report_checkbox(self, "Utilities30", eventname, result)


def caseid_utilities31(self):
    module_other_app.get_datachecklist("Utilities31")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    try:
        utilities.move_module1(self, "Utilities31", eventname, result, var_app.record_driver_card, 725, 1100, 175, 1100, 500,
                                                        "Trang chủ - Ghi thẻ lái xe", var_app.check_record_driver_card,
                                                         "GHI THẺ LÁI XE", "_TrangChu_GhiTheLaiXe.png")
    except:
        utilities.general.utilities_back(self)
        utilities.move_module1(self, "Utilities31", eventname, result, var_app.record_driver_card, 725, 1100, 175, 1100, 500,
                                                        "Trang chủ - Ghi thẻ lái xe", var_app.check_record_driver_card,
                                                         "GHI THẺ LÁI XE", "_TrangChu_GhiTheLaiXe.png")

def caseid_utilities32(self):
    module_other_app.get_datachecklist("Utilities32")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    utilities.utilities.record_driver_card_fill_info(self, "Utilities32", eventname, result)

def caseid_utilities33(self):
    module_other_app.get_datachecklist("Utilities33")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    utilities.utilities.record_driver_card_help(self, "Utilities33", eventname, result)


def caseid_utilities34(self):
    module_other_app.get_datachecklist("Utilities34")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    utilities.utilities.record_driver_card_icon(self, "Utilities34", eventname, result)


def caseid_utilities35(self):
    module_other_app.get_datachecklist("Utilities35")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    try:
        utilities.move_module1(self, "Utilities35", eventname, result, var_app.contract_list, 725, 1100, 175, 1100, 500,
                                                        "Trang chủ - Danh sách hợp đồng", var_app.check_contract_list,
                                                         "DANH SÁCH HỢP ĐỒNG", "_TrangChu_DanhSachHopDong.png")
    except:
        utilities.general.utilities_back(self)
        utilities.move_module1(self, "Utilities35", eventname, result, var_app.contract_list, 725, 1100, 175, 1100, 500,
                                                        "Trang chủ - Danh sách hợp đồng", var_app.check_contract_list,
                                                         "DANH SÁCH HỢP ĐỒNG", "_TrangChu_DanhSachHopDong.png")
    utilities.general.utilities_back(self)








