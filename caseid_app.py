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
import time
from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import AppiumBy
import vehicle
import account
















def caseid_login01(self):
    module_other_app.get_datachecklist("Login01")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    login_app.login.login(self, var_app.data['login']['khongnhom_quantri_tk'], var_app.data['login']['khongnhom_quantri_mk'], "Login01", eventname, result,
                          var_app.check_minitor_vehicle, None, "_DangNhap_TKKhachHangCoQuyenGiamSat.png")


def caseid_login02(self):
    module_other_app.get_datachecklist("Login02")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    login_app.login.login(self, var_app.data['login']['binhanh_tk'], var_app.data['login']['binhanh_mk'], "Login02", eventname, result,
                          var_app.check_minitor, "Giám sát", "_DangNhap_TKBinhAnh.png")



def caseid_login03(self):
    module_other_app.get_datachecklist("Login03")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    login_app.login.login(self, var_app.data['login']['conhom_quantri_tk'], var_app.data['login']['conhom_quantri_mk'], "Login03", eventname, result,
                          var_app.check_minitor_vehicle, None, "_DangNhap_TKDaiLy.png")



def caseid_login04(self):
    module_other_app.get_datachecklist("Login04")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    login_app.login.login(self, var_app.data['login']['khongnhom_thuong_tk1'], var_app.data['login']['khongnhom_thuong_mk1'],
                          "Login04", eventname, result, var_app.check_customer_account1, "", "")




def caseid_login05(self):
    module_other_app.get_datachecklist("Login05")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    login_app.login.login_wrong(self, "truongvck22", "11111", "Login05", eventname, result)




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


@retry(tries=3, delay=2, backoff=1, jitter=5, )
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
                          var_app.affiliate_mail, var_app.login_buttonlogin, "_DangNhap_LinkLienKet_Email.png")



def caseid_login13(self):
    module_other_app.get_datachecklist("Login13")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    login_app.other_function.affiliate_link_outsite(self, "Login13", eventname, result,
                          var_app.affiliate_bagps, var_app.login_buttonlogin, "_DangNhap_LinkLienKet_BAGPS.png")



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
                          var_app.affiliate_facebook, var_app.login_buttonlogin, "ĐĂNG NHẬP", "_DangNhap_LinkLienKet_FaceBook.png")




def caseid_login16(self):
    module_other_app.get_datachecklist("Login16")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    login_app.other_function.affiliate_link_insite(self, "Login16", eventname, result,
                          var_app.affiliate_zalo, var_app.login_buttonlogin, "ĐĂNG NHẬP", "_DangNhap_LinkLienKet_Zalo.png")



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
                          var_app.affiliate_tiktok, var_app.login_buttonlogin, "ĐĂNG NHẬP", "_DangNhap_LinkLienKet_Tiktok.png")



def caseid_login19(self):
    module_other_app.get_datachecklist("Login19")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    login_app.other_function.affiliate_link_insite(self, "Login19", eventname, result,
                          var_app.affiliate_mangluoi, var_app.login_buttonlogin, "ĐĂNG NHẬP", "_DangNhap_LinkLienKet_MangLuoi.png")




def caseid_login20(self):
    module_other_app.get_datachecklist("Login20")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    login_app.other_function.affiliate_link_insite(self, "Login20", eventname, result,
                          var_app.affiliate_trainghiembagps, var_app.login_buttonlogin, "ĐĂNG NHẬP", "_DangNhap_LinkLienKet_TraiNghiemBAGPS.png")


def caseid_login21(self):
    module_other_app.get_datachecklist("Login21")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    login_app.drive.for_drive(self, "Login21", eventname, result)


def caseid_login22(self):
    module_other_app.get_datachecklist("Login22")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    login_app.drive.for_drive_search(self, "Login22", eventname, result)

def caseid_login23(self):
    module_other_app.get_datachecklist("Login23")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    login_app.drive.for_drive_icon(self, "Login23", eventname, result, var_app.notification1, var_app.notification1, var_app.notification1, "_DANHCHOLAIXE_IconThongBao.png")

def caseid_login24(self):
    module_other_app.get_datachecklist("Login24")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    login_app.drive.for_drive_icon(self, "Login24", eventname, result, var_app.theme1, var_app.theme2, var_app.theme1,  "_DANHCHOLAIXE_IconChonNen.png")


def caseid_login25(self):
    module_other_app.get_datachecklist("Login25")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    login_app.drive.check_info_sumnary(self, "Login25", eventname, result, "1", var_app.liscense_plate, "_DANHCHOLAIXE_BienSo.png")


def caseid_login25_1(self):
    module_other_app.get_datachecklist("Login25_1")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    login_app.drive.check_info_sumnary(self, "Login25_1", eventname, result, "1", var_app.type_vehicle1, "_DANHCHOLAIXE_LoaiHinhVanTai.png")

def caseid_login26(self):
    module_other_app.get_datachecklist("Login26")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    login_app.drive.check_info_sumnary(self, "Login26", eventname, result, "1", var_app.name_drive_driving_license1, "_DANHCHOLAIXE_TenLaiXeGiayPhepLaiXe.png")


def caseid_login27(self):
    module_other_app.get_datachecklist("Login27")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    login_app.drive.check_info_sumnary(self, "Login27", eventname, result, "0", var_app.status_vehicle1, "_DANHCHOLAIXE_TrangThaiXe.png")


def caseid_login28(self):
    module_other_app.get_datachecklist("Login28")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    login_app.drive.check_info_sumnary(self, "Login28", eventname, result, "0", var_app.camera_GSHT1, "_DANHCHOLAIXE_CameraGSHT.png")


def caseid_login29(self):
    module_other_app.get_datachecklist("Login29")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    login_app.drive.check_info_sumnary(self, "Login29", eventname, result, "0", var_app.time_update1, "_DANHCHOLAIXE_CapNhatLuc.png")

def caseid_login30(self):
    pass


def caseid_login31(self):
    pass


def caseid_login32(self):
    pass

def caseid_login33(self):
    pass


def caseid_login34(self):
    pass


def caseid_login35(self):
    module_other_app.get_datachecklist("Login35")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    login_app.drive.check_info_sumnary(self, "Login35", eventname, result, "0", var_app.trip1, "_DANHCHOLAIXE_HanhTrinh.png")


def caseid_login36(self):
    module_other_app.get_datachecklist("Login36")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    login_app.drive.check_info_sumnary(self, "Login36", eventname, result, "0", var_app.image2, "_DANHCHOLAIXE_HinhAnh.png")


def caseid_login37(self):
    pass


def caseid_login38(self):
    module_other_app.get_datachecklist("Login38")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    login_app.drive.for_drive_overview(self, "Login38", eventname, result)


def caseid_login39(self):
    module_other_app.get_datachecklist("Login39")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    login_app.drive.for_drive_punish(self, "Login39", eventname, result)



def caseid_login40(self):
    module_other_app.get_datachecklist("Login40")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    login_app.drive.check_info_punish(self, "Login40", eventname, result, var_app.punish1, "_DANHCHOLAIXE_LoiViPham.png")

def caseid_login41(self):
    module_other_app.get_datachecklist("Login41")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    login_app.drive.check_info_punish(self, "Login41", eventname, result, var_app.punish2, "_DANHCHOLAIXE_ThoiGianViPham.png")


def caseid_login42(self):
    module_other_app.get_datachecklist("Login42")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    login_app.drive.check_info_punish(self, "Login42", eventname, result, var_app.punish3, "_DANHCHOLAIXE_DiaDiemViPham.png")


def caseid_login43(self):
    module_other_app.get_datachecklist("Login43")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    login_app.drive.check_info_punish(self, "Login43", eventname, result, var_app.punish4, "_DANHCHOLAIXE_TrangThai.png")

def caseid_login44(self):
    module_other_app.get_datachecklist("Login44")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    login_app.drive.check_info_punish(self, "Login44", eventname, result, var_app.punish5, "_DANHCHOLAIXE_DonViPhatHien.png")


def caseid_login45(self):
    module_other_app.get_datachecklist("Login45")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    login_app.drive.check_info_punish(self, "Login45", eventname, result, var_app.punish6, "_DANHCHOLAIXE_DonViXuLy.png")



def caseid_minitor01_1(self):
    module_other_app.get_datachecklist("Minitor01_1")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.select_many_vehicle(self, "Minitor01_1", eventname, result)



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
    minitor_app.overview.vehicle_status(self, "Minitor04", eventname, result, " Nợ phí", "_GiamSat_TrangThai_NoPhi.png")


def caseid_minitor05(self):
    module_other_app.get_datachecklist("Minitor05")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor05", eventname, result, " Di chuyển", "_GiamSat_TrangThai_DiChuyen.png")


def caseid_minitor06(self):
    module_other_app.get_datachecklist("Minitor06")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor06", eventname, result, " Dừng - Tắt", "_GiamSat_TrangThai_DungTat.png")


def caseid_minitor07(self):
    module_other_app.get_datachecklist("Minitor07")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor07", eventname, result, " Dừng - Bật", "_GiamSat_TrangThai_DungBat.png")



def caseid_minitor08(self):
    module_other_app.get_datachecklist("Minitor08")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor08", eventname, result, " Bật máy", "_GiamSat_TrangThai_BatMay.png")



def caseid_minitor09(self):
    module_other_app.get_datachecklist("Minitor09")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor09", eventname, result, " Tắt máy", "_GiamSat_TrangThai_TatMay.png")


def caseid_minitor10(self):
    module_other_app.get_datachecklist("Minitor10")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor10", eventname, result, " Quá tốc độ", "_GiamSat_TrangThai_QuaTocDo.png")


def caseid_minitor11(self):
    module_other_app.get_datachecklist("Minitor11")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor11", eventname, result, " Mất GPS", "_GiamSat_TrangThai_MatGPS.png")



def caseid_minitor12(self):
    module_other_app.get_datachecklist("Minitor12")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor12", eventname, result, " Mất GSM", "_GiamSat_TrangThai_MatGMS.png")



def caseid_minitor13(self):
    module_other_app.get_datachecklist("Minitor13")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor13", eventname, result, "Tất cả", "_GiamSat_TrangThai_Tatca.png")



def caseid_minitor14(self):
    module_other_app.get_datachecklist("Minitor14")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor14", eventname, result, " Nợ phí", "_GiamSat_TrangThai_NoPhi.png")


def caseid_minitor15(self):
    module_other_app.get_datachecklist("Minitor15")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor15", eventname, result, " Di chuyển", "_GiamSat_TrangThai_DiChuyen.png")


def caseid_minitor16(self):
    module_other_app.get_datachecklist("Minitor16")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor16", eventname, result, " Dừng - Tắt", "_GiamSat_TrangThai_DungTat.png")


def caseid_minitor17(self):
    module_other_app.get_datachecklist("Minitor17")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor17", eventname, result, " Dừng - Bật", "_GiamSat_TrangThai_DungBat.png")



def caseid_minitor18(self):
    module_other_app.get_datachecklist("Minitor18")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor18", eventname, result, " Bật máy", "_GiamSat_TrangThai_BatMay.png")



def caseid_minitor19(self):
    module_other_app.get_datachecklist("Minitor19")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor19", eventname, result, " Tắt máy", "_GiamSat_TrangThai_TatMay.png")


def caseid_minitor20(self):
    module_other_app.get_datachecklist("Minitor20")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor20", eventname, result, " Quá tốc độ", "_GiamSat_TrangThai_QuaTocDo.png")


def caseid_minitor21(self):
    module_other_app.get_datachecklist("Minitor21")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor21", eventname, result, " Mất GPS", "_GiamSat_TrangThai_MatGPS.png")



def caseid_minitor22(self):
    module_other_app.get_datachecklist("Minitor22")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor22", eventname, result, " Mất GSM", "_GiamSat_TrangThai_MatGMS.png")



def caseid_minitor23(self):
    module_other_app.get_datachecklist("Minitor23")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor23", eventname, result, "Tất cả", "_GiamSat_TrangThai_Tatca.png")



def caseid_minitor24(self):
    module_other_app.get_datachecklist("Minitor24")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor24", eventname, result, " Nợ phí", "_GiamSat_TrangThai_NoPhi.png")


def caseid_minitor25(self):
    module_other_app.get_datachecklist("Minitor25")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor25", eventname, result, " Di chuyển", "_GiamSat_TrangThai_DiChuyen.png")


def caseid_minitor26(self):
    module_other_app.get_datachecklist("Minitor26")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor26", eventname, result, " Dừng - Tắt", "_GiamSat_TrangThai_DungTat.png")


def caseid_minitor27(self):
    module_other_app.get_datachecklist("Minitor27")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor27", eventname, result, " Dừng - Bật", "_GiamSat_TrangThai_DungBat.png")



def caseid_minitor28(self):
    module_other_app.get_datachecklist("Minitor28")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor28", eventname, result, " Bật máy", "_GiamSat_TrangThai_BatMay.png")



def caseid_minitor29(self):
    module_other_app.get_datachecklist("Minitor29")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor29", eventname, result, " Tắt máy", "_GiamSat_TrangThai_TatMay.png")


def caseid_minitor30(self):
    module_other_app.get_datachecklist("Minitor30")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor30", eventname, result, " Quá tốc độ", "_GiamSat_TrangThai_QuaTocDo.png")


def caseid_minitor31(self):
    module_other_app.get_datachecklist("Minitor31")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor31", eventname, result, " Mất GPS", "_GiamSat_TrangThai_MatGPS.png")



def caseid_minitor32(self):
    module_other_app.get_datachecklist("Minitor32")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor32", eventname, result, " Mất GSM", "_GiamSat_TrangThai_MatGMS.png")



def caseid_minitor33(self):
    module_other_app.get_datachecklist("Minitor33")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor33", eventname, result, "Tất cả", "_GiamSat_TrangThai_Tatca.png")


def caseid_minitor34(self):
    module_other_app.get_datachecklist("Minitor34")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor34", eventname, result, " Nợ phí", "_GiamSat_TrangThai_NoPhi.png")


def caseid_minitor35(self):
    module_other_app.get_datachecklist("Minitor35")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor35", eventname, result, " Di chuyển", "_GiamSat_TrangThai_DiChuyen.png")


def caseid_minitor36(self):
    module_other_app.get_datachecklist("Minitor36")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor36", eventname, result, " Dừng - Tắt", "_GiamSat_TrangThai_DungTat.png")


def caseid_minitor37(self):
    module_other_app.get_datachecklist("Minitor37")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor37", eventname, result, " Dừng - Bật", "_GiamSat_TrangThai_DungBat.png")



def caseid_minitor38(self):
    module_other_app.get_datachecklist("Minitor38")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor38", eventname, result, " Bật máy", "_GiamSat_TrangThai_BatMay.png")



def caseid_minitor39(self):
    module_other_app.get_datachecklist("Minitor39")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor39", eventname, result, " Tắt máy", "_GiamSat_TrangThai_TatMay.png")


def caseid_minitor40(self):
    module_other_app.get_datachecklist("Minitor40")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor40", eventname, result, " Quá tốc độ", "_GiamSat_TrangThai_QuaTocDo.png")


def caseid_minitor41(self):
    module_other_app.get_datachecklist("Minitor41")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor41", eventname, result, " Mất GPS", "_GiamSat_TrangThai_MatGPS.png")



def caseid_minitor42(self):
    module_other_app.get_datachecklist("Minitor42")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor42", eventname, result, " Mất GSM", "_GiamSat_TrangThai_MatGMS.png")



def caseid_minitor43(self):
    module_other_app.get_datachecklist("Minitor43")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor43", eventname, result, "Tất cả", "_GiamSat_TrangThai_Tatca.png")


def caseid_minitor44(self):
    module_other_app.get_datachecklist("Minitor44")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor44", eventname, result, " Nợ phí", "_GiamSat_TrangThai_NoPhi.png")


def caseid_minitor45(self):
    module_other_app.get_datachecklist("Minitor45")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor45", eventname, result, " Di chuyển", "_GiamSat_TrangThai_DiChuyen.png")


def caseid_minitor46(self):
    module_other_app.get_datachecklist("Minitor46")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor46", eventname, result, " Dừng - Tắt", "_GiamSat_TrangThai_DungTat.png")


def caseid_minitor47(self):
    module_other_app.get_datachecklist("Minitor47")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor47", eventname, result, " Dừng - Bật", "_GiamSat_TrangThai_DungBat.png")



def caseid_minitor48(self):
    module_other_app.get_datachecklist("Minitor48")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor48", eventname, result, " Bật máy", "_GiamSat_TrangThai_BatMay.png")



def caseid_minitor49(self):
    module_other_app.get_datachecklist("Minitor49")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor49", eventname, result, " Tắt máy", "_GiamSat_TrangThai_TatMay.png")


def caseid_minitor50(self):
    module_other_app.get_datachecklist("Minitor50")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor50", eventname, result, " Quá tốc độ", "_GiamSat_TrangThai_QuaTocDo.png")


def caseid_minitor51(self):
    module_other_app.get_datachecklist("Minitor51")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor51", eventname, result, " Mất GPS", "_GiamSat_TrangThai_MatGPS.png")



def caseid_minitor52(self):
    module_other_app.get_datachecklist("Minitor52")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor52", eventname, result, " Mất GSM", "_GiamSat_TrangThai_MatGMS.png")



def caseid_minitor53(self):
    module_other_app.get_datachecklist("Minitor53")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor53", eventname, result, "Tất cả", "_GiamSat_TrangThai_Tatca.png")


def caseid_minitor54(self):
    module_other_app.get_datachecklist("Minitor54")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor54", eventname, result, " Nợ phí", "_GiamSat_TrangThai_NoPhi.png")


def caseid_minitor55(self):
    module_other_app.get_datachecklist("Minitor55")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor55", eventname, result, " Di chuyển", "_GiamSat_TrangThai_DiChuyen.png")


def caseid_minitor56(self):
    module_other_app.get_datachecklist("Minitor56")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor56", eventname, result, " Dừng - Tắt", "_GiamSat_TrangThai_DungTat.png")


def caseid_minitor57(self):
    module_other_app.get_datachecklist("Minitor57")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor57", eventname, result, " Dừng - Bật", "_GiamSat_TrangThai_DungBat.png")



def caseid_minitor58(self):
    module_other_app.get_datachecklist("Minitor58")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor58", eventname, result, " Bật máy", "_GiamSat_TrangThai_BatMay.png")



def caseid_minitor59(self):
    module_other_app.get_datachecklist("Minitor59")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor59", eventname, result, " Tắt máy", "_GiamSat_TrangThai_TatMay.png")


def caseid_minitor60(self):
    module_other_app.get_datachecklist("Minitor60")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor60", eventname, result, " Quá tốc độ", "_GiamSat_TrangThai_QuaTocDo.png")


def caseid_minitor61(self):
    module_other_app.get_datachecklist("Minitor61")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor61", eventname, result, " Mất GPS", "_GiamSat_TrangThai_MatGPS.png")



def caseid_minitor62(self):
    module_other_app.get_datachecklist("Minitor62")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor62", eventname, result, " Mất GSM", "_GiamSat_TrangThai_MatGMS.png")



def caseid_minitor63(self):
    module_other_app.get_datachecklist("Minitor63")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor63", eventname, result, "Tất cả", "_GiamSat_TrangThai_Tatca.png")


def caseid_minitor64(self):
    module_other_app.get_datachecklist("Minitor64")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor64", eventname, result, " Nợ phí", "_GiamSat_TrangThai_NoPhi.png")


def caseid_minitor65(self):
    module_other_app.get_datachecklist("Minitor65")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor65", eventname, result, " Di chuyển", "_GiamSat_TrangThai_DiChuyen.png")


def caseid_minitor66(self):
    module_other_app.get_datachecklist("Minitor66")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor66", eventname, result, " Dừng - Tắt", "_GiamSat_TrangThai_DungTat.png")


def caseid_minitor67(self):
    module_other_app.get_datachecklist("Minitor67")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor67", eventname, result, " Dừng - Bật", "_GiamSat_TrangThai_DungBat.png")



def caseid_minitor68(self):
    module_other_app.get_datachecklist("Minitor68")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor68", eventname, result, " Bật máy", "_GiamSat_TrangThai_BatMay.png")



def caseid_minitor69(self):
    module_other_app.get_datachecklist("Minitor69")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor69", eventname, result, " Tắt máy", "_GiamSat_TrangThai_TatMay.png")


def caseid_minitor70(self):
    module_other_app.get_datachecklist("Minitor70")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor70", eventname, result, " Quá tốc độ", "_GiamSat_TrangThai_QuaTocDo.png")


def caseid_minitor71(self):
    module_other_app.get_datachecklist("Minitor71")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor71", eventname, result, " Mất GPS", "_GiamSat_TrangThai_MatGPS.png")



def caseid_minitor72(self):
    module_other_app.get_datachecklist("Minitor72")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor72", eventname, result, " Mất GSM", "_GiamSat_TrangThai_MatGMS.png")



def caseid_minitor73(self):
    module_other_app.get_datachecklist("Minitor73")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor73", eventname, result, "Tất cả", "_GiamSat_TrangThai_Tatca.png")


def caseid_minitor74(self):
    module_other_app.get_datachecklist("Minitor74")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor74", eventname, result, " Nợ phí", "_GiamSat_TrangThai_NoPhi.png")


def caseid_minitor75(self):
    module_other_app.get_datachecklist("Minitor75")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor75", eventname, result, " Di chuyển", "_GiamSat_TrangThai_DiChuyen.png")


def caseid_minitor76(self):
    module_other_app.get_datachecklist("Minitor76")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor76", eventname, result, " Dừng - Tắt", "_GiamSat_TrangThai_DungTat.png")


def caseid_minitor77(self):
    module_other_app.get_datachecklist("Minitor77")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor77", eventname, result, " Dừng - Bật", "_GiamSat_TrangThai_DungBat.png")



def caseid_minitor78(self):
    module_other_app.get_datachecklist("Minitor78")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor78", eventname, result, " Bật máy", "_GiamSat_TrangThai_BatMay.png")



def caseid_minitor79(self):
    module_other_app.get_datachecklist("Minitor79")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor79", eventname, result, " Tắt máy", "_GiamSat_TrangThai_TatMay.png")


def caseid_minitor80(self):
    module_other_app.get_datachecklist("Minitor80")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor80", eventname, result, " Quá tốc độ", "_GiamSat_TrangThai_QuaTocDo.png")


def caseid_minitor81(self):
    module_other_app.get_datachecklist("Minitor81")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor81", eventname, result, " Mất GPS", "_GiamSat_TrangThai_MatGPS.png")



def caseid_minitor82(self):
    module_other_app.get_datachecklist("Minitor82")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor82", eventname, result, " Mất GSM", "_GiamSat_TrangThai_MatGMS.png")



def caseid_minitor83(self):
    module_other_app.get_datachecklist("Minitor83")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.vehicle_status(self, "Minitor83", eventname, result, "Tất cả", "_GiamSat_TrangThai_Tatca.png")



def caseid_minitor83_1(self):
    module_other_app.get_datachecklist("Minitor83_1")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.warm_passengers(self, "Minitor83_1", eventname, result,)


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




@retry(tries=2, delay=2, backoff=1, jitter=5, )
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


def caseid_minitor110_1(self):
    module_other_app.get_datachecklist("Minitor110_1")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.detail.detail_vehicle_driving_time_during_the_week(self, "Minitor110_1", eventname, result,)



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


def caseid_minitor138_1(self):
    module_other_app.get_datachecklist("Minitor138_1")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.detail.icon_support_customer(self, "Minitor138_1", eventname, result,)


def caseid_minitor138_2(self):
    module_other_app.get_datachecklist("Minitor138_2")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.detail.setting_favorite(self, "Minitor138_2", eventname, result,)


def caseid_minitor138_3(self):
    module_other_app.get_datachecklist("Minitor138_3")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.detail.setting_favorite_choose(self, "Minitor138_3", eventname, result,)


def caseid_minitor138_4(self):
    module_other_app.get_datachecklist("Minitor138_4")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.detail.setting_favorite_search(self, "Minitor138_4", eventname, result,)








# @retry(tries=3, delay=2, backoff=1, jitter=5, )
def caseid_minitor139(self):
    module_other_app.get_datachecklist("Minitor139")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.affiliate_link.affiliate_link_detail(self, "Minitor139", eventname, result, 0.85, 0.93, 0.2, 0.93, 1000,
                                                     var_app.route1, var_app.minitor, var_app.check_route2,
                                                     "Lộ trình", "_GiamSat_ChiTietXe_LoTrinh.png", 1)




def caseid_minitor140(self):
    module_other_app.get_datachecklist("Minitor140")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.affiliate_link.affiliate_link_detail(self, "Minitor140", eventname, result, 0.85, 0.5, 0.2, 0.5, 1000,
                                                     var_app.minitor_image,  var_app.minitor_imageiconx, var_app.check_image_monitoring,
                                                     "GIÁM SÁT HÌNH ẢNH", "_GiamSat_ChiTietXe_HinhAnh.png", 1)



def caseid_minitor141(self):
    module_other_app.get_datachecklist("Minitor141")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.affiliate_link.affiliate_link_detail(self, "Minitor141", eventname, result, 0.85, 0.5, 0.2, 0.5, 1000,
                                                     var_app.minitor_camera,  var_app.minitor_cameraiconx, var_app.check_camera_monitoring,
                                                     "GIÁM SÁT NHIỀU CAMERA", "_GiamSat_ChiTietXe_Camera.png", 1)




def caseid_minitor142(self):
    module_other_app.get_datachecklist("Minitor142")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.affiliate_link.affiliate_link_detail(self, "Minitor142", eventname, result, 0.85, 0.25, 0.2, 0.25, 1000,
                                                     var_app.minitor_more, var_app.minitor_more_iconx, var_app.check_minitor_more,
                                                     "THIẾT LẬP MỤC ƯA THÍCH", "_GiamSat_Them.png", 1)



def caseid_minitor143(self):
    module_other_app.get_datachecklist("Minitor143")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.affiliate_link.affiliate_link_detail(self, "Minitor143", eventname, result, 0.85, 0.5, 0.2, 0.5, 1000,
                                                     var_app.watch_the_overview_video_again,  var_app.watch_the_overview_video_again_iconx,
                                                     var_app.see_again_video1, "XEM LẠI VIDEO", "_GiamSat_XemLaiVideoTongQuan.png", 1)



def caseid_minitor144(self):
    module_other_app.get_datachecklist("Minitor144")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.affiliate_link.affiliate_link_detail(self, "Minitor144", eventname, result, 0.85, 0.5, 0.2, 0.5, 1000,
                                                     var_app.watch_image_camera_nd10, var_app.watch_image_camera_nd10_iconx,
                                                     var_app.check_watch_image_camera_nd10, "CAMERA", "_GiamSat_XemAnhCameraND10.png", 1)


def caseid_minitor145(self):
    module_other_app.get_datachecklist("Minitor145")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.affiliate_link.affiliate_link_detail(self, "Minitor145", eventname, result, 0.85, 0.5, 0.2, 0.5, 1000,
                                                     var_app.extract_video, var_app.extract_video_iconx, var_app.check_extract_video,
                                                     "TRÍCH XUẤT DỮ LIỆU", "_GiamSat_TrichXuatVieo.png", 1)


def caseid_minitor146(self):
    module_other_app.get_datachecklist("Minitor146")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.affiliate_link.affiliate_link_detail(self, "Minitor146", eventname, result, 0.85, 0.7, 0.2, 0.7, 1000,
                                                     var_app.report_stop, var_app.report_stop_iconx, var_app.check_report_stop,
                                                     "BÁO CÁO DỪNG ĐỖ", "_GiamSat_BaoCaoDungDo.png", 1)



def caseid_minitor147(self):
    module_other_app.get_datachecklist("Minitor147")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.affiliate_link.affiliate_link_detail(self, "Minitor147", eventname, result, 0.85, 0.7, 0.2, 0.7, 1000,
                                                     var_app.detailed_activity_reports, var_app.detailed_activity_reports_iconx, var_app.check_detailed_activity_reports,
                                                     "BÁO CÁO CHI TIẾT HOẠT ĐỘNG", "_GiamSat_BaoCaoChiTietHoatDong.png", 1)

def caseid_minitor148(self):
    module_other_app.get_datachecklist("Minitor148")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.affiliate_link.affiliate_link_detail(self, "Minitor148", eventname, result, 0.85, 0.7, 0.2, 0.7, 1000,
                                                     var_app.summary_report_of_activities, var_app.summary_report_of_activities_iconx,
                                                     var_app.check_summary_report_of_activities, "BÁO CÁO TỔNG HỢP HOẠT ĐỘNG", "_GiamSat_BaoCaoTongHopHoatDong.png", 1)

def caseid_minitor149(self):
    module_other_app.get_datachecklist("Minitor149")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.affiliate_link.affiliate_link_detail(self, "Minitor149", eventname, result, 0.85, 0.7, 0.2, 0.7, 1000,
                                                     var_app.report_entering_and_exiting_the_station, var_app.report_entering_and_exiting_the_station_iconx,
                                                     var_app.check_report_entering_and_exiting_the_station,
                                                     "BÁO CÁO RA VÀO TRẠM", "_GiamSat_BaoCaoRaVaoTram.png", 1)

def caseid_minitor150(self):
    module_other_app.get_datachecklist("Minitor150")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.affiliate_link.affiliate_link_detail(self, "Minitor150", eventname, result, 0.85, 0.7, 0.2, 0.7, 1000,
                                                     var_app.report_speeding, var_app.report_iconx, var_app.check_report_speeding,
                                                     "BÁO CÁO QUÁ TỐC ĐỘ", "_GiamSat_BaoCaoQuaTocDo.png", 1)


def caseid_minitor151(self):
    module_other_app.get_datachecklist("Minitor151")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.affiliate_link.affiliate_link_detail(self, "Minitor151", eventname, result, 0.85, 0.7, 0.2, 0.7, 1000,
                                                     var_app.business_trip_report, var_app.report_iconx, var_app.check_business_trip_report,
                                                     "BÁO CÁO CHUYẾN KINH DOANH", "_GiamSat_BaoCaoChuyenKinhDoanh.png", 1)

def caseid_minitor152(self):
    module_other_app.get_datachecklist("Minitor152")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.affiliate_link.affiliate_link_detail(self, "Minitor152", eventname, result, 0.85, 0.7, 0.2, 0.7, 1000,
                                                     var_app.report_loss_of_signal, var_app.report_iconx, var_app.check_report_loss_of_signal,
                                                     "BÁO CÁO MẤT TÍN HIỆU", "_GiamSat_BaoCaoMatTinHieu.png", 1)
def caseid_minitor153(self):
    module_other_app.get_datachecklist("Minitor153")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.affiliate_link.affiliate_link_detail(self, "Minitor153", eventname, result, 0.85, 0.7, 0.2, 0.7, 1000,
                                                     var_app.fuel_dump_report, var_app.report_iconx, var_app.check_fuel_dump_report,
                                                     "BÁO CÁO ĐỔ HÚT NHIÊN LIỆU", "_GiamSat_BaoCaoDoHutNhienLieu.png", 1)

def caseid_minitor154(self):
    module_other_app.get_datachecklist("Minitor154")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.affiliate_link.affiliate_link_detail(self, "Minitor154", eventname, result, 0.85, 0.7, 0.2, 0.7, 1000,
                                                     var_app.engine_report, var_app.report_iconx, var_app.check_engine_report,
                                                     "BÁO CÁO ĐỘNG CƠ", "_GiamSat_BaoCaoDongCo.png", 1)

def caseid_minitor155(self):
    module_other_app.get_datachecklist("Minitor155")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.affiliate_link.affiliate_link_detail(self, "Minitor155", eventname, result, 0.85, 0.7, 0.2, 0.7, 1000,
                                                     var_app.fuel_chart, var_app.report_iconx, var_app.check_fuel_chart,
                                                     "BIỂU ĐỒ NHIÊN LIỆU", "_GiamSat_BieuDoNhienLieu.png", 1)


def caseid_minitor155_1(self):
    module_other_app.get_datachecklist("Minitor155_1")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.affiliate_link.affiliate_link_detail(self, "Minitor155_1", eventname, result, 0.85, 0.7, 0.2, 0.7, 1000,
                                                     var_app.BC_Accumulated_Km, var_app.report_iconx, var_app.check_BC_Accumulated_Km,
                                                     "BÁO CÁO TỔNG HỢP KM TÍCH LŨY", "_GiamSat_BaoCaoTongHopKmTichLuy.png", 1)


def caseid_minitor156(self):
    module_other_app.get_datachecklist("Minitor156")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.affiliate_link.affiliate_link_detail(self, "Minitor156", eventname, result, 0.85, 0.7, 0.2, 0.7, 1000,
                                                     var_app.fuel_consumption_report, var_app.report_iconx, var_app.check_fuel_consumption_report,
                                                     "BÁO CÁO TIÊU HAO NHIÊN LIỆU", "_GiamSat_BaoCaoTieuHaoNhienLieu.png", 1)


def caseid_minitor157(self):
    module_other_app.get_datachecklist("Minitor157")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.affiliate_link.affiliate_link_detail(self, "Minitor157", eventname, result, 0.85, 0.7, 0.2, 0.7, 1000,
                                                     var_app.Comprehensive_fuel_consumption_report, var_app.report_iconx,
                                                     var_app.check_Comprehensive_fuel_consumption_report,
                                                     "BÁO CÁO TỔNG HỢP TIÊU HAO NHIÊN LIỆU", "_GiamSat_BaoCaoTongHopTieuHaoNhienLieu.png", 1)

def caseid_minitor158(self):
    module_other_app.get_datachecklist("Minitor158")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.affiliate_link.affiliate_link_detail(self, "Minitor158", eventname, result, 0.85, 0.7, 0.2, 0.7, 1000,
                                                     var_app.vehicle_speed, var_app.report_iconx, var_app.check_vehicle_speed,
                                                     "TỐC ĐỘ CỦA XE", "_GiamSat_TocDoCuaXe.png", 1)

def caseid_minitor158_1(self):
    module_other_app.get_datachecklist("Minitor158_1")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.affiliate_link.affiliate_link_detail(self, "Minitor158_1", eventname, result, 0.85, 0.7, 0.2, 0.7, 1000,
                                                     var_app.continuous_driving_detailed_reports, var_app.report_iconx, var_app.check_continuous_driving_detailed_reports,
                                                     "BÁO CÁO CHI TIẾT CÁC CUỐC LÁI XE LIÊN TỤC", "_GiamSat_BaoCaoChiTietCacCuocLaiXeLienTuc.png", 1)

def caseid_minitor158_2(self):
    module_other_app.get_datachecklist("Minitor158_2")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.affiliate_link.affiliate_link_detail(self, "Minitor158_2", eventname, result, 0.85, 0.7, 0.2, 0.7, 1000,
                                                     var_app.driving_details_for_the_day, var_app.report_iconx, var_app.check_driving_details_for_the_day,
                                                     "BÁO CÁO CHI TIẾT CÁC CUỐC LÁI XE THEO NGÀY", "_GiamSat_BaoCaoChiTietCacCuocLaiXeTheoNgay.png", 1)

def caseid_minitor158_3(self):
    module_other_app.get_datachecklist("Minitor158_3")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.affiliate_link.affiliate_link_detail(self, "Minitor158_3", eventname, result, 0.85, 0.7, 0.2, 0.7, 1000,
                                                     var_app.driving_report_for_the_week, var_app.report_iconx, var_app.check_driving_report_for_the_week,
                                                     "BÁO CÁO CÁC CUỐC LÁI XE TRONG TUẦN", "_GiamSat_BaoCaoCacCuocLaiXeTrongTuan.png", 1)

def caseid_minitor158_4(self):
    module_other_app.get_datachecklist("Minitor158_4")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.affiliate_link.affiliate_link_detail(self, "Minitor158_4", eventname, result, 0.85, 0.7, 0.2, 0.7, 1000,
                                                     var_app.BC_Speeding_violation, var_app.report_iconx, var_app.check_BC_Speeding_violation,
                                                     "BÁO CÁO CHI TIẾT VI PHẠM TỐC ĐỘ CHẠY", "_GiamSat_BaoCaoChiTietViPhamTocDoChay.png", 1)


def caseid_minitor159(self):
    module_other_app.get_datachecklist("Minitor159")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.affiliate_link.affiliate_link_detail(self, "Minitor159", eventname, result, 0.85, 0.7, 0.2, 0.7, 1000,
                                                     var_app.report_vehicle_violations, var_app.report_iconx,
                                                     var_app.check_report_vehicle_violations,
                                                     "BÁO CÁO CHI TIẾT HÀNH VI", "_GiamSat_BaoCaoViPhamLaiXe.png", 1)

def caseid_minitor160(self):
    module_other_app.get_datachecklist("Minitor160")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.affiliate_link.affiliate_link_detail(self, "Minitor160", eventname, result, 0.85, 0.7, 0.2, 0.7, 1000,
                                                     var_app.summary_report_of_driving_behavior, var_app.report_iconx,
                                                     var_app.check_summary_report_of_driving_behavior,
                                                     "BÁO CÁO TỔNG HỢP HÀNH VI", "_GiamSat_BaoCaoTongHopHanhViLaiXe.png", 1)
    module_other_app.close_app()


def caseid_minitor161(self):
    module_other_app.get_datachecklist("Minitor161")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.affiliate_link.affiliate_link_detail(self, "Minitor161", eventname, result, 0.85, 0.9, 0.2, 0.9, 1000,
                                                     var_app.hide_and_show_the_car, var_app.hide_and_show_the_car_iconx, var_app.check_hide_and_show_the_car,
                                                     "DANH SÁCH XE ĐANG ẨN", "_GiamSat_AnHienXe.png", 1)

def caseid_minitor162(self):
    module_other_app.get_datachecklist("Minitor162")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.affiliate_link.affiliate_link_detail(self, "Minitor162", eventname, result,  0.85, 0.9, 0.2, 0.9, 1000,
                                                     var_app.add_driver, var_app.add_driver_iconx, var_app.check_add_driver,
                                                     "THÔNG TIN LÁI XE", "_GiamSat_ThemLaiXe.png", 1)

def caseid_minitor163(self):
    module_other_app.get_datachecklist("Minitor163")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.affiliate_link.affiliate_link_detail(self, "Minitor163", eventname, result,  0.85, 0.9, 0.2, 0.9, 1000,
                                                     var_app.list_driver, var_app.list_driver_iconx, var_app.check_list_driver,
                                                     "DANH SÁCH LÁI XE", "_GiamSat_DanhSachLaiXe.png", 1)


def caseid_minitor163_1(self):
    module_other_app.get_datachecklist("Minitor163_1")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.affiliate_link.affiliate_link_detail(self, "Minitor163_1", eventname, result,  0.85, 0.9, 0.2, 0.9, 1000,
                                                     var_app.transmission_bca, var_app.transmission_bca_iconx, var_app.check_transmission_bca,
                                                     "TRUYỀN DỮ LIỆU BCA", "_GiamSat_TruyenDuLieuBca.png", 1)

def caseid_minitor164(self):
    module_other_app.get_datachecklist("Minitor164")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.affiliate_link.affiliate_link_detail(self, "Minitor164", eventname, result,  0.85, 0.9, 0.2, 0.9, 1000,
                                                     var_app.fee_information, var_app.fee_information_iconx, var_app.check_fee_information,
                                                     "THÔNG TIN PHÍ", "_GiamSat_ThongTinPhi.png", 1)


def caseid_minitor164_1(self):
    module_other_app.get_datachecklist("Minitor164_1")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.affiliate_link.affiliate_link_detail(self, "Minitor164_1", eventname, result,  0.85, 0.9, 0.2, 0.9, 1000,
                                                     var_app.Maintenance, var_app.Maintenance_icon_x, var_app.check_Maintenance,
                                                     "DANH SÁCH BẢO DƯỠNG", "_GiamSat_DanhSachBaoDuong.png", 1)


def caseid_minitor165(self):
    module_other_app.get_datachecklist("Minitor165")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.affiliate_link.affiliate_link_detail(self, "Minitor165", eventname, result,  0.85, 0.9, 0.2, 0.9, 1000,
                                                     var_app.enter_document_information, var_app.enter_document_information_iconx,
                                                     var_app.check_enter_document_information,
                                                     "NHẬP THÔNG TIN GIẤY TỜ", "_GiamSat_NhapThongTinGiayTo.png", 1)

def caseid_minitor166(self):
    module_other_app.get_datachecklist("Minitor166")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.affiliate_link.affiliate_link_detail(self, "Minitor166", eventname, result,  0.85, 0.9, 0.2, 0.9, 1000,
                                                     var_app.list_of_documents, var_app.list_of_documents_iconx, var_app.check_list_of_documents,
                                                     "DANH SÁCH GIẤY TỜ", "_GiamSat_DanhSachGiayTo.png", 1)

def caseid_minitor167(self):
    module_other_app.get_datachecklist("Minitor167")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.affiliate_link.affiliate_link_detail(self, "Minitor167", eventname, result,  0.85, 0.9, 0.2, 0.9, 1000,
                                                     var_app.support_customer, var_app.support_customer_iconx1, var_app.check_support_customer,
                                                     "HỖ TRỢ KHÁCH HÀNG", "_GiamSat_HoTroKhachHang.png", 1)

def caseid_minitor168(self):
    module_other_app.get_datachecklist("Minitor168")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.affiliate_link.affiliate_link_detail(self, "Minitor168", eventname, result,  0.85, 0.9, 0.2, 0.9, 1000,
                                                     var_app.warning_bca, var_app.warning_bca_iconx, var_app.check_warning_bca,
                                                     "CẢNH BÁO THIẾU THÔNG TIN", "_GiamSat_CanhBaoTichTruyemBca.png", 1)

def caseid_minitor169(self):
    module_other_app.get_datachecklist("Minitor169")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.affiliate_link.affiliate_link_detail(self, "Minitor169", eventname, result,  0.85, 0.9, 0.2, 0.9, 1000,
                                                     var_app.record_driver_card, var_app.record_driver_card_iconx, var_app.check_record_driver_card,
                                                     "GHI THẺ LÁI XE", "_GiamSat_GhiTheLaiXe.png", 1)

def caseid_minitor169_0(self):
    module_other_app.get_datachecklist("Minitor169_0")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.affiliate_link.affiliate_link_detail(self, "Minitor169_0", eventname, result,  0.85, 0.9, 0.2, 0.9, 1000,
                                                     var_app.for_drive_punish, var_app.for_drive_punish_iconx, var_app.check_for_drive_punish1,
                                                     "THÔNG TIN PHẠT NGUỘI", "_GiamSat_PhatNguoi.png", 1)

def caseid_minitor169_1(self):
    module_other_app.get_datachecklist("Minitor169_1")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.affiliate_link.affiliate_link_detail(self, "Minitor169_1", eventname, result,  0.85, 0.9, 0.2, 0.9, 1000,
                                                     var_app.overview_table, var_app.overview_table_iconx, var_app.check_overview_table,
                                                     "BẢNG TỔNG QUAN", "_GiamSat_BangTongQuan.png", 1)


def caseid_minitor169_2(self):
    module_other_app.get_datachecklist("Minitor169_2")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.affiliate_link.affiliate_link_detail(self, "Minitor169_2", eventname, result,  0.85, 0.9, 0.2, 0.9, 1000,
                                                     var_app.record_driver_card_nfc, var_app.record_driver_card_nfc_iconx, var_app.check_record_driver_card,
                                                     "GHI THẺ LÁI XE", "_GiamSat_GhiTheLaiXe_NFC.png", 1)
    try:
        var_app.driver.find_element(By.XPATH, var_app.igree).click()
        time.sleep(2.5)
    except:
        pass



def caseid_minitor170(self):
    module_other_app.get_datachecklist("Minitor170")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.affiliate_link.affiliate_link_detail(self, "Minitor170", eventname, result,  0.85, 0.9, 0.2, 0.9, 1000,
                                                     var_app.list_vehicle, var_app.minitor, var_app.check_list_vehicle,
                                                    "Phương tiện", "_GiamSat_DanhSachPhuongTien.png", 1)

def caseid_minitor171(self):
    module_other_app.get_datachecklist("Minitor171")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.penalty_noticep(self, "Minitor171", eventname, result,)


def caseid_minitor171_1(self):
    module_other_app.get_datachecklist("Minitor171_1")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.penalty_noticep_check_count(self, "Minitor171_1", eventname, result,)


def caseid_minitor172(self):
    module_other_app.get_datachecklist("Minitor172")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.penalty_noticep_search(self, "Minitor172", eventname, result,)

def caseid_minitor173(self):
    module_other_app.get_datachecklist("Minitor173")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.penalty_noticep_filter(self, "Minitor173", eventname, result,)

def caseid_minitor174(self):
    module_other_app.get_datachecklist("Minitor174")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.penalty_noticep_export_excel(self, "Minitor174", eventname, result,)

def caseid_minitor175(self):
    module_other_app.get_datachecklist("Minitor175")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.penalty_noticep_check_info(self, "Minitor175", eventname, result, var_app.blu_name, var_app.blu_data,
                                                    "PHƯƠNG TIỆN VI PHẠM", "_ThongTinPhatNguoi_PhuongTienViPham.png")

def caseid_minitor176(self):
    module_other_app.get_datachecklist("Minitor176")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.penalty_noticep_check_info(self, "Minitor176", eventname, result, var_app.green_name, var_app.green_data,
                                                    "ĐÃ XỬ LÝ", "_ThongTinPhatNguoi_DaXuLy.png")
def caseid_minitor177(self):
    module_other_app.get_datachecklist("Minitor177")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.penalty_noticep_check_info(self, "Minitor177", eventname, result, var_app.red_name, var_app.red_data,
                                                    "CHƯA XỬ LÝ", "_ThongTinPhatNguoi_ChuaXuLy.png")

def caseid_minitor178(self):
    module_other_app.get_datachecklist("Minitor178")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.penalty_noticep_check_inf_orange(self, "Minitor178", eventname, result,)

def caseid_minitor179(self):
    module_other_app.get_datachecklist("Minitor179")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.penalty_noticep_link(self, "Minitor179", eventname, result,)

def caseid_minitor180(self):
    module_other_app.get_datachecklist("Minitor180")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.penalty_noticep_check_info(self, "Minitor180", eventname, result, var_app.penalty_noticep_vehicle_name, var_app.penalty_noticep_vehicle_data,
                                                    "Xe mất tín hiệu > 30 ngày sẽ không được cập nhật thông tin phạt nguội mới nhất!", "_ThongTinPhatNguoi_PhuongTien.png")

def caseid_minitor181(self):
    module_other_app.get_datachecklist("Minitor181")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.penalty_noticep_check_info(self, "Minitor181", eventname, result, var_app.penalty_noticep_eror_name, var_app.penalty_noticep_eror_data,
                                                    "Lỗi vi phạm", "_ThongTinPhatNguoi_LoiViPham.png")

def caseid_minitor182(self):
    module_other_app.get_datachecklist("Minitor182")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.penalty_noticep_check_info(self, "Minitor182", eventname, result, var_app.penalty_noticep_time_name, var_app.penalty_noticep_time_data,
                                                    "Thời gian vi phạm", "_ThongTinPhatNguoi_ThoiGianViPham.png")

def caseid_minitor183(self):
    module_other_app.get_datachecklist("Minitor183")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.penalty_noticep_check_info(self, "Minitor183", eventname, result, var_app.penalty_noticep_address_name, var_app.penalty_noticep_address_data,
                                                    "Địa điểm vi phạm", "_ThongTinPhatNguoi_DiaDiemViPham.png")

def caseid_minitor184(self):
    module_other_app.get_datachecklist("Minitor184")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.penalty_noticep_check_info(self, "Minitor184", eventname, result, var_app.penalty_noticep_status_name, var_app.penalty_noticep_status_data,
                                                    "Trạng thái", "_ThongTinPhatNguoi_TrangThai.png")

def caseid_minitor185(self):
    module_other_app.get_datachecklist("Minitor185")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.penalty_noticep_check_info(self, "Minitor185", eventname, result, var_app.penalty_noticep_unit_name, var_app.penalty_noticep_unit_data,
                                                    "Đơn vị xử lý", "_ThongTinPhatNguoi_DonViXuLy.png")

def caseid_minitor186(self):
    module_other_app.get_datachecklist("Minitor186")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.penalty_noticep_check_info(self, "Minitor186", eventname, result, var_app.penalty_noticep_contact_name, var_app.penalty_noticep_contact_data,
                                                    "Thông tin liên hệ", "_ThongTinPhatNguoi_ThongTinLienHe.png")

def caseid_minitor186_1(self):
    module_other_app.get_datachecklist("Minitor186_1")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.penalty_noticep_route(self, "Minitor186_1", eventname, result,)


def caseid_minitor187(self):
    module_other_app.get_datachecklist("Minitor187")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.share_vehicle(self, "Minitor187", eventname, result,)

def caseid_minitor188(self):
    module_other_app.get_datachecklist("Minitor188")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.share_vehicle_create(self, "Minitor188", eventname, result, "Giám sát", var_app.Share_quickly,
                                              "Chia sẻ nhanh", "__ChiaSePhuongTien_GiamSat.png")

def caseid_minitor189(self):
    module_other_app.get_datachecklist("Minitor189")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.share_vehicle_create(self, "Minitor189", eventname, result, "Lộ trình", var_app.Share_quickly,
                                              "Chia sẻ nhanh", "__ChiaSePhuongTien_LoTrinh.png")

def caseid_minitor190(self):
    module_other_app.get_datachecklist("Minitor190")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.share_vehicle_link(self, "Minitor190", eventname, result,)


def caseid_minitor191(self):
    module_other_app.get_datachecklist("Minitor191")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.enter_temperature(self, "Minitor191", eventname, result,)

def caseid_minitor192(self):
    module_other_app.get_datachecklist("Minitor192")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.enter_temperature_save(self, "Minitor192", eventname, result, 50)

def caseid_minitor193(self):
    module_other_app.get_datachecklist("Minitor193")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.enter_temperature_check(self, "Minitor193", eventname, result,)


def caseid_minitor194(self):
    module_other_app.get_datachecklist("Minitor194")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.find_a_branch(self, "Minitor194", eventname, result,)


def caseid_minitor195(self):
    module_other_app.get_datachecklist("Minitor195")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.find_a_branch_search(self, "Minitor195", eventname, result,)

def caseid_minitor196(self):
    module_other_app.get_datachecklist("Minitor196")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.find_a_branch_setting(self, "Minitor196", eventname, result,)


def caseid_minitor197(self):
    module_other_app.get_datachecklist("Minitor197")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.find_a_branch_filter(self, "Minitor197", eventname, result,)


def caseid_minitor198(self):
    module_other_app.get_datachecklist("Minitor198")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.find_a_branch_other(self, "Minitor198", eventname, result, var_app.branch_time, "_TimDiemChiNhanh_ThoiGianCapNhat.png")


def caseid_minitor199(self):
    module_other_app.get_datachecklist("Minitor199")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.find_a_branch_other(self, "Minitor199", eventname, result, var_app.branch_current_location, "_TimDiemChiNhanh_ViTriHienTai.png")


def caseid_minitor200(self):
    module_other_app.get_datachecklist("Minitor200")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.find_a_branch_other(self, "Minitor200", eventname, result, var_app.branch_field1, "_TimDiemChiNhanh_TenChiNhanh.png")

def caseid_minitor201(self):
    module_other_app.get_datachecklist("Minitor201")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.find_a_branch_other(self, "Minitor201", eventname, result, var_app.branch_field2, "_TimDiemChiNhanh_KhoangCach.png")

def caseid_minitor202(self):
    module_other_app.get_datachecklist("Minitor202")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.find_a_branch_other(self, "Minitor202", eventname, result, var_app.branch_field3, "_TimDiemChiNhanh_DiaChi.png")

def caseid_minitor203(self):
    module_other_app.get_datachecklist("Minitor203")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.find_a_branch_button(self, "Minitor203", eventname, result, var_app.branch_ggmap, "_TimDiemChiNhanh_IconGGMap.png")


def caseid_minitor204(self):
    module_other_app.get_datachecklist("Minitor204")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    minitor_app.overview.find_a_branch_button(self, "Minitor204", eventname, result, var_app.branch_field4, "_TimDiemChiNhanh_XemTrenGiamSat.png")





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
    route.overview.route_choosetime(self, "Route03", eventname, result, var_app.route_4h, "_GiamSat_Lotrinh4h.png")

def caseid_route04(self):
    module_other_app.get_datachecklist("Route04")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    route.overview.route_choosetime(self, "Route04", eventname, result, var_app.route_8h, "_GiamSat_Lotrinh8h.png")


def caseid_route05(self):
    module_other_app.get_datachecklist("Route05")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    route.overview.route_choosetime(self, "Route05", eventname, result, var_app.route_24h, "_GiamSat_Lotrinh24h.png")


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
    route.overview.route_icon_map(self, "Route11", eventname, result)


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
    vehicle.overview.arrange_time(self, "Vehicle06", eventname, result)


def caseid_vehicle07(self):
    module_other_app.get_datachecklist("Vehicle07")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    vehicle.overview.arrange_default(self, "Vehicle07", eventname, result)



def caseid_vehicle08(self):
    module_other_app.get_datachecklist("Vehicle08")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    vehicle.overview.vehicle_status(self, "Vehicle08", eventname, result, " Nợ phí", "_Phuongtien_TrangThai_NoPhi.png")


def caseid_vehicle09(self):
    module_other_app.get_datachecklist("Vehicle09")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    vehicle.overview.vehicle_status(self, "Vehicle09", eventname, result, " Di chuyển", "_PhuongTien_TrangThai_DiChuyen.png")


def caseid_vehicle10(self):
    module_other_app.get_datachecklist("Vehicle10")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    vehicle.overview.vehicle_status(self, "Vehicle10", eventname, result, " Dừng - Tắt", "_PhuongTien_TrangThai_DungTat.png")

def caseid_vehicle11(self):
    module_other_app.get_datachecklist("Vehicle11")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    vehicle.overview.vehicle_status(self, "Vehicle11", eventname, result, " Dừng - Bật", "_PhuongTien_TrangThai_DungBat.png")

def caseid_vehicle12(self):
    module_other_app.get_datachecklist("Vehicle12")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    vehicle.overview.vehicle_status(self, "Vehicle12", eventname, result, " Bật máy", "_PhuongTien_TrangThai_BatMay.png")

def caseid_vehicle13(self):
    module_other_app.get_datachecklist("Vehicle13")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    vehicle.overview.vehicle_status(self, "Vehicle13", eventname, result, " Tắt máy", "_PhuongTien_TrangThai_TatMay.png")

def caseid_vehicle14(self):
    module_other_app.get_datachecklist("Vehicle14")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    vehicle.overview.vehicle_status(self, "Vehicle14", eventname, result, " Quá tốc độ", "_PhuongTien_TrangThai_QuaTocDo.png")

def caseid_vehicle15(self):
    module_other_app.get_datachecklist("Vehicle15")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    vehicle.overview.vehicle_status(self, "Vehicle15", eventname, result, " Mất GPS", "_PhuongTien_TrangThai_MatGPS.png")

def caseid_vehicle16(self):
    module_other_app.get_datachecklist("Vehicle16")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    vehicle.overview.vehicle_status(self, "Vehicle16", eventname, result, " Mất GSM", "_PhuongTien_TrangThai_MatGMS.png")

def caseid_vehicle17(self):
    module_other_app.get_datachecklist("Vehicle17")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    vehicle.overview.vehicle_status(self, "Vehicle17", eventname, result, "Tất cả", "_PhuongTien_TrangThai_Tatca.png")


def caseid_vehicle18(self):
    module_other_app.get_datachecklist("Vehicle18")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    vehicle.overview.detail_vehicle(self, "Vehicle18", eventname, result)



def caseid_vehicle19(self):
    module_other_app.get_datachecklist("Vehicle19")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    vehicle.overview.check_detail_vehicle(self, "Vehicle19", eventname, result, 6, "_PhuongTien_BienSoXe.png", "0")

def caseid_vehicle20(self):
    module_other_app.get_datachecklist("Vehicle20")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    vehicle.overview.check_detail_vehicle(self, "Vehicle20", eventname, result, 7, "_PhuongTien_ThoiGianCapNhat.png", "3")

def caseid_vehicle21(self):
    module_other_app.get_datachecklist("Vehicle21")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    vehicle.overview.check_detail_vehicle(self, "Vehicle21", eventname, result, 12, "_PhuongTien_DongCo.png", "0")

def caseid_vehicle22(self):
    module_other_app.get_datachecklist("Vehicle22")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    vehicle.overview.check_detail_vehicle(self, "Vehicle22", eventname, result, 10, "_PhuongTien_KmTrongNgay.png", "0")

def caseid_vehicle23(self):
    module_other_app.get_datachecklist("Vehicle23")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    vehicle.overview.check_detail_vehicle(self, "Vehicle23", eventname, result, 8, "_PhuongTien_VanToc.png", "0")

def caseid_vehicle24(self):
    module_other_app.get_datachecklist("Vehicle24")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    vehicle.overview.check_detail_vehicle(self, "Vehicle24", eventname, result, 11, "_PhuongTien_ThoiGianDungDo.png", "1")

def caseid_vehicle25(self):
    module_other_app.get_datachecklist("Vehicle25")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    vehicle.overview.check_detail_vehicle(self, "Vehicle25", eventname, result, 17, "_PhuongTien_NhietDo.png", "2")


def caseid_vehicle26(self):
    module_other_app.get_datachecklist("Vehicle26")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    vehicle.overview.check_detail_vehicle(self, "Vehicle26", eventname, result, 14, "_PhuongTien_DiaChi.png", "0")

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
    homepage_app.toolbar.support_support(self, "Toolbar10", eventname, result, var_app.support)



def caseid_toolbar11(self):
    module_other_app.get_datachecklist("Toolbar11")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    homepage_app.toolbar.support_support_button_defaut(self, "Toolbar11", eventname, result, var_app.support_other, "_HoTroKhachHang_HoTroKhac.png")


def caseid_toolbar12(self):
    module_other_app.get_datachecklist("Toolbar12")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    homepage_app.toolbar.support_support_button_lost_signal(self, "Toolbar12", eventname, result)


def caseid_toolbar13(self):
    module_other_app.get_datachecklist("Toolbar13")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    homepage_app.toolbar.support_support_button_change_license_plate(self, "Toolbar13", eventname, result)


def caseid_toolbar14(self):
    module_other_app.get_datachecklist("Toolbar14")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    homepage_app.toolbar.support_support_button_error_camera(self, "Toolbar14", eventname, result)



def caseid_toolbar15(self):
    module_other_app.get_datachecklist("Toolbar15")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    homepage_app.toolbar.support_support_button_defaut(self, "Toolbar15", eventname, result, var_app.unlock_vehicle, "_HoTroKhachHang_MoKhoaXe.png")



def caseid_toolbar16(self):
    module_other_app.get_datachecklist("Toolbar16")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    homepage_app.toolbar.support_support_button_defaut(self, "Toolbar16", eventname, result, var_app.dong_feee, "_HoTroKhachHang_DongPhiDVMC_SC.png")



def caseid_toolbar17(self):
    module_other_app.get_datachecklist("Toolbar17")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    homepage_app.toolbar.support_send_info(self, "Toolbar17", eventname, result)


def caseid_toolbar18(self):
    module_other_app.get_datachecklist("Toolbar18")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    homepage_app.toolbar.support_utilities(self, "Toolbar18", eventname, result)


def caseid_toolbar19(self):
    module_other_app.get_datachecklist("Toolbar19")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    homepage_app.toolbar.support_utilities_link(self, "Toolbar19", eventname, result, "1", var_app.clock_vehicle,
                                                var_app.support_utility_x, var_app.check_hide_and_show_the_car,
                                                         "DANH SÁCH XE ĐANG ẨN", "_HoTroKhachHang_TienIch_KhoaXe.png")

def caseid_toolbar20(self):
    module_other_app.get_datachecklist("Toolbar20")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    homepage_app.toolbar.support_utilities_link(self, "Toolbar20", eventname, result, "1", var_app.assign_car,
                                                var_app.assign_car_x, var_app.SELECT_VEHICLE,
                                                         "CHỌN PHƯƠNG TIỆN", "_HoTroKhachHang_TienIch_GanXe.png")

def caseid_toolbar21(self):
    module_other_app.get_datachecklist("Toolbar21")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    homepage_app.toolbar.support_utilities_link(self, "Toolbar21", eventname, result, "1", var_app.change_channel,
                                                var_app.change_channel_x, var_app.check_change_channel,
                                                         "ĐỔI TÊN KÊNH CAMERA", "_HoTroKhachHang_TienIch_DoiKenh.png")

def caseid_toolbar22(self):
    module_other_app.get_datachecklist("Toolbar22")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    homepage_app.toolbar.support_utilities_link(self, "Toolbar22", eventname, result, "1", var_app.dowload_video,
                                                var_app.dowload_video_x, var_app.check_dowload_video,
                                                         "XEM LẠI VIDEO", "_HoTroKhachHang_TienIch_TaiVideo.png")

def caseid_toolbar23(self):
    module_other_app.get_datachecklist("Toolbar23")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    homepage_app.toolbar.support_utilities_link(self, "Toolbar23", eventname, result, "0", "", "",
                                                var_app.call_cskh, "Gọi CSKH", "_HoTroKhachHang_TienIch_GoiCSKH.png")


def caseid_toolbar24(self):
    module_other_app.get_datachecklist("Toolbar24")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    homepage_app.toolbar.support_utilities_link(self, "Toolbar24", eventname, result, "0", "", "",
                                                var_app.call_zalo, "Gọi Zalo", "_HoTroKhachHang_TienIch_GoiZalo.png")


def caseid_toolbar25(self):
    module_other_app.get_datachecklist("Toolbar25")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    homepage_app.toolbar.support_follow(self, "Toolbar25", eventname, result)

def caseid_toolbar26(self):
    module_other_app.get_datachecklist("Toolbar26")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    homepage_app.toolbar.support_customer_track_feedback(self, "Toolbar26", eventname, result, var_app.pending_processing, var_app.pending_processing_number)



def caseid_toolbar27(self):
    module_other_app.get_datachecklist("Toolbar27")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    homepage_app.toolbar.support_customer_track_feedback(self, "Toolbar27", eventname, result, var_app.processing, var_app.processing_number)


def caseid_toolbar28(self):
    module_other_app.get_datachecklist("Toolbar28")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    homepage_app.toolbar.support_customer_track_complete(self, "Toolbar28", eventname, result)


def caseid_toolbar29(self):
    module_other_app.get_datachecklist("Toolbar29")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    homepage_app.toolbar.support_customer_track_follow_search(self, "Toolbar29", eventname, result)


def caseid_toolbar30(self):
    module_other_app.get_datachecklist("Toolbar30")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    homepage_app.toolbar.support_customer_track_follow_filter(self, "Toolbar30", eventname, result)

def caseid_toolbar30_1(self):
    module_other_app.get_datachecklist("Toolbar30_1")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    homepage_app.toolbar.support_customer_cancel(self, "Toolbar30_1", eventname, result)



def caseid_toolbar31(self):
    module_other_app.get_datachecklist("Toolbar31")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    homepage_app.toolbar.shopping(self, "Toolbar31", eventname, result)

def caseid_toolbar32(self):
    module_other_app.get_datachecklist("Toolbar32")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    homepage_app.toolbar.support_module4g(self, "Toolbar32", eventname, result)


def caseid_toolbar33(self):
    module_other_app.get_datachecklist("Toolbar33")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    homepage_app.toolbar.support_buy_a_driver_card(self, "Toolbar33", eventname, result)


def caseid_toolbar34(self):
    module_other_app.get_datachecklist("Toolbar34")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    homepage_app.toolbar.support_new_products(self, "Toolbar34", eventname, result)


def caseid_toolbar35(self):
    module_other_app.get_datachecklist("Toolbar35")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    homepage_app.toolbar.shopping_send_info(self, "Toolbar35", eventname, result)


def caseid_toolbar36(self):
    module_other_app.get_datachecklist("Toolbar36")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    homepage_app.toolbar.shopping_follow(self, "Toolbar36", eventname, result)


def caseid_toolbar37(self):
    module_other_app.get_datachecklist("Toolbar37")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    homepage_app.toolbar.shopping_follow_status(self, "Toolbar37", eventname, result, var_app.pending_processing, var_app.pending_processing_number)



def caseid_toolbar38(self):
    module_other_app.get_datachecklist("Toolbar38")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    homepage_app.toolbar.shopping_follow_status(self, "Toolbar38", eventname, result, var_app.processing, var_app.processing_number)


def caseid_toolbar39(self):
    module_other_app.get_datachecklist("Toolbar39")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    homepage_app.toolbar.shopping_follow_complete(self, "Toolbar39", eventname, result)


def caseid_toolbar40(self):
    module_other_app.get_datachecklist("Toolbar40")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    homepage_app.toolbar.shopping_follow_search(self, "Toolbar40", eventname, result)


def caseid_toolbar41(self):
    module_other_app.get_datachecklist("Toolbar41")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    homepage_app.toolbar.shopping_follow_filter(self, "Toolbar41", eventname, result)



def caseid_toolbar42(self):
    module_other_app.get_datachecklist("Toolbar42")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    homepage_app.toolbar.sos(self, "Toolbar42", eventname, result)



def caseid_toolbar43(self):
    module_other_app.get_datachecklist("Toolbar43")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    homepage_app.toolbar.sos_send_sos(self, "Toolbar43", eventname, result)


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
    homepage_app.favorite.mor_drag_and_drop(self, "Favorite04", eventname, result)

def caseid_favorite05(self):
    pass
    # module_other_app.get_datachecklist("Favorite05")
    # eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    # result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    # homepage_app.favorite.favorite_toward(self, "Favorite05", eventname, result, var_app.homepage_route,
    #                                       var_app.check_homepage_route, "Lộ trình", "_TrangChu_YeuThich_LoTrinh.png")


def caseid_favorite06(self):
    module_other_app.get_datachecklist("Favorite06")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    homepage_app.move_module(self, "Favorite06", eventname, result, var_app.overview_table, 0.8, 0.85, 0.2, 0.85, 1000,
                                                    "Trang chủ - Bảng tổng quan", var_app.check_overview_table,
                                                     "BẢNG TỔNG QUAN", "_TrangChu_BangTongQuan.png")


def caseid_favorite07(self):
    module_other_app.get_datachecklist("Favorite07")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    homepage_app.favorite.overview_table_select_group(self, "Favorite07", eventname, result)

def caseid_favorite08(self):
    module_other_app.get_datachecklist("Favorite08")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    homepage_app.favorite.overview_table_status(self, "Favorite08", eventname, result, var_app.over_table1, 0, 10,
                                                "Hoạt động:", "_TrangChu_BangTongQuan_HoatDong.png")

def caseid_favorite09(self):
    module_other_app.get_datachecklist("Favorite09")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    homepage_app.favorite.overview_table_status(self, "Favorite09", eventname, result, var_app.over_table2, 0, 8,
                                                "Tắt máy:", "_TrangChu_BangTongQuan_TatMay.png")

def caseid_favorite10(self):
    module_other_app.get_datachecklist("Favorite10")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    homepage_app.favorite.overview_table_status(self, "Favorite10", eventname, result, var_app.over_table3, 0, 11,
                                                "Quá tốc độ:", "_TrangChu_BangTongQuan_QuaTocDo.png")

def caseid_favorite11(self):
    module_other_app.get_datachecklist("Favorite11")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    homepage_app.favorite.overview_table_status(self, "Favorite11", eventname, result, var_app.over_table4, 0, 9,
                                                "Tăng tốc:", "_TrangChu_BangTongQuan_TangToc.png")

def caseid_favorite12(self):
    module_other_app.get_datachecklist("Favorite12")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    homepage_app.favorite.overview_table_status(self, "Favorite12", eventname, result, var_app.over_table5, 0, 10,
                                                "Phanh gấp:", "_TrangChu_BangTongQuan_PhanhGap.png")

def caseid_favorite13(self):
    module_other_app.get_datachecklist("Favorite13")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    homepage_app.favorite.overview_table_status(self, "Favorite13", eventname, result, var_app.over_table6, 0, 8,
                                                "Cua gấp:", "_TrangChu_BangTongQuan_CuaGap.png")

def caseid_favorite14(self):
    module_other_app.get_datachecklist("Favorite14")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    homepage_app.favorite.overview_table_status(self, "Favorite14", eventname, result, var_app.over_table7, 0, 8,
                                                "LXLT 4H:", "_TrangChu_BangTongQuan_LXLT4H.png")

def caseid_favorite15(self):
    module_other_app.get_datachecklist("Favorite15")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    homepage_app.favorite.overview_table_status(self, "Favorite15", eventname, result, var_app.over_table8, 0, 7,
                                                "LX 10H:", "_TrangChu_BangTongQuan_LX10H.png")

def caseid_favorite16(self):
    module_other_app.get_datachecklist("Favorite16")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    homepage_app.favorite.overview_table_state(self, "Favorite16", eventname, result, "0")

def caseid_favorite17(self):
    module_other_app.get_datachecklist("Favorite17")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    homepage_app.favorite.overview_table_state(self, "Favorite17", eventname, result, "1")

def caseid_favorite18(self):
    module_other_app.get_datachecklist("Favorite18")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    homepage_app.favorite.overview_table_select_vehicle(self, "Favorite18", eventname, result)

def caseid_favorite19(self):
    module_other_app.get_datachecklist("Favorite19")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    homepage_app.favorite.overview_table_info(self, "Favorite19", eventname, result, var_app.over_view_vehicle1,
                                              var_app.over_view_vehicle2, "_TrangChu_BangTongQuan_Phuongtien.png")

def caseid_favorite20(self):
    module_other_app.get_datachecklist("Favorite20")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    homepage_app.favorite.overview_table_info(self, "Favorite20", eventname, result, var_app.over_view_s1,
                                              var_app.over_view_s2, "_TrangChu_BangTongQuan_QuangDuong.png")

def caseid_favorite21(self):
    module_other_app.get_datachecklist("Favorite21")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    homepage_app.favorite.overview_table_info(self, "Favorite21", eventname, result, var_app.over_view_time1,
                                              var_app.over_view_time2, "_TrangChu_BangTongQuan_ThoiGian.png")


def caseid_favorite22(self):
    module_other_app.get_datachecklist("Favorite22")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    homepage_app.favorite.overview_table_violate(self, "Favorite22", eventname, result)






def caseid_media01(self):
    module_other_app.get_datachecklist("Media01")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    homepage_app.move_module(self, "Media01", eventname, result, var_app.image_monitoring, 0.8, 0.5, 0.2, 0.5, 1000,
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
        homepage_app.move_module(self, "Media17", eventname, result, var_app.camera_monitoring, 0.8, 0.5, 0.2, 0.5, 1000,
                                                        "Trang chủ - Hình ảnh video - Giám sát hình ảnh", var_app.check_camera_monitoring,
                                                         "GIÁM SÁT NHIỀU CAMERA", "_TrangChu_GiamSatCamera.png")
    except:
        image_video_app.image_video.camera_monitoring_back(self)
        homepage_app.move_module(self, "Media17", eventname, result, var_app.camera_monitoring, 0.8, 0.5, 0.2, 0.5, 1000,
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
                                                          var_app.camera_icon_pause, 1, "False", "_TrangChu_GiamSatCamera_IconTamDung.png")

def caseid_media24(self):
    module_other_app.get_datachecklist("Media24")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    image_video_app.image_video.camera_monitoring_check_icon(self, "Media24", eventname, result,
                                                          var_app.camera_icon_volumn, 1, "True", "_TrangChu_GiamSatCamera_IconAmThanh.png")

def caseid_media25(self):
    module_other_app.get_datachecklist("Media25")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    image_video_app.image_video.camera_monitoring_check_icon(self, "Media25", eventname, result,
                                                          var_app.camera_icon_take_of_photo, 1, "True", "_TrangChu_GiamSatCamera_IconChupAnh.png")

def caseid_media26(self):
    module_other_app.get_datachecklist("Media26")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    image_video_app.image_video.camera_monitoring_check_icon(self, "Media26", eventname, result,
                                                          var_app.camera_icon_full_creen, 0, "True", "_TrangChu_GiamSatCamera_IconToanManHinh.png")
def caseid_media27(self):
    module_other_app.get_datachecklist("Media27")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    image_video_app.image_video.camera_monitoring_check_icon(self, "Media27", eventname, result,
                                                          var_app.camera_icon_turn_creen, 0, "True", "_TrangChu_GiamSatCamera_IconXoayManHinh.png")


def caseid_media27_1(self):
    module_other_app.get_datachecklist("Media27_1")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    image_video_app.image_video.camera_monitoring_click_double(self, "Media27_1", eventname, result)



def caseid_media27_2(self):
    module_other_app.get_datachecklist("Media27_2")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    image_video_app.image_video.camera_monitoring_swipe(self, "Media27_2", eventname, result)





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

def caseid_media32_1(self):
    module_other_app.get_datachecklist("Media32_1")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    image_video_app.image_video.icon_volumn_off(self, "Media32_1", eventname, result)

def caseid_media32_2(self):
    module_other_app.get_datachecklist("Media32_2")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    image_video_app.image_video.icon_volumn_off_off(self, "Media32_2", eventname, result)

def caseid_media32_3(self):
    module_other_app.get_datachecklist("Media32_3")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    image_video_app.image_video.icon_volumn_off_on(self, "Media32_3", eventname, result)







def caseid_media33(self):
    module_other_app.get_datachecklist("Media33")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    try:
        homepage_app.move_module(self, "Media33", eventname, result, var_app.see_again_video, 0.8, 0.5, 0.2, 0.5, 1000,
                                                        "Trang chủ - Xem lại video - Tổng quan", var_app.see_again_video1,
                                                         "XEM LẠI VIDEO", "_TrangChu_XemLaiVideoTongQuan.png")
    except:
        image_video_app.image_video.see_again_video_back(self)
        homepage_app.move_module(self, "Media33", eventname, result, var_app.see_again_video, 0.8, 0.5, 0.2, 0.5, 1000,
                                                        "Trang chủ - Xem lại video - Tổng quan", var_app.see_again_video1,
                                                         "XEM LẠI VIDEO", "_TrangChu_XemLaiVideoTongQuan.png")



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
    pass
    # module_other_app.get_datachecklist("Media44")
    # eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    # result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    # image_video_app.image_video.see_again_video_see_again_video_iconn(self, "Media44", eventname, result,
    #                                                                   var_app.see_again_video_icon_pause, "False",
    #                                                                   "_TrangChu_XemLaiVideo_XemThietBi_ClickVideo_IconTamDung.png")

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
        homepage_app.move_module(self, "Media55", eventname, result, var_app.see_nd10, 0.8, 0.5, 0.2, 0.5, 1000,
                                                        "Trang chủ - Xem ảnh Camera - NĐ10", var_app.check_see_nd10,
                                                         "CAMERA", "_TrangChu_XemAnhCamera.png")
    except:
        image_video_app.image_video.see_again_video_back(self)
        image_video_app.image_video.see_image_camera_back(self)
        homepage_app.move_module(self, "Media55", eventname, result, var_app.see_nd10, 0.8, 0.5, 0.2, 0.5, 1000,
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
        homepage_app.move_module(self, "Media65", eventname, result, var_app.export_video, 0.8, 0.5, 0.2, 0.5, 1000,
                                                        "Trang chủ - Trích xuất video", var_app.check_export_video,
                                                         "TRÍCH XUẤT DỮ LIỆU", "_TrangChu_TrichXuatVideo.png")
    except:
        image_video_app.image_video.export_video_back(self)
        homepage_app.move_module(self, "Media65", eventname, result, var_app.export_video, 0.8, 0.5, 0.2, 0.5, 1000,
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
        homepage_app.move_module(self, "Report01", eventname, result, var_app.report_stop, 0.8, 0.65, 0.2, 0.65, 1000,
                                                        "Trang chủ - Báo cáo dừng đỗ", var_app.check_report_stop,
                                                         "BÁO CÁO DỪNG ĐỖ", "_TrangChu_BaoCaoDungDo.png")
    except:
        report_app.general.report_back(self)
        homepage_app.move_module(self, "Report01", eventname, result, var_app.report_stop, 0.8, 0.65, 0.2, 0.65, 1000,
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
                                              var_app.STT, "Trang chủ - báo cáo dừng đỗ", "_BaoCao_BaoCaoDungDo_HomNay.png")

def caseid_report04(self):
    module_other_app.get_datachecklist("Report04")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.report_stop_search_type(self, "Report04", eventname, result, var_app.report_7day,
                                              var_app.STT, "Trang chủ - báo cáo dừng đỗ", "_BaoCao_BaoCaoDungDo_7Ngay.png")

def caseid_report05(self):
    module_other_app.get_datachecklist("Report05")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.report_stop_search_type(self, "Report05", eventname, result, var_app.report_15day,
                                              var_app.STT, "Trang chủ - báo cáo dừng đỗ", "_BaoCao_BaoCaoDungDo_15Ngay.png")

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
    report_app.report.report_stop_detail(self, "Report10", eventname, result, var_app.report_detail1, var_app.report_detail_1, 0, 30,
                                         "Tổng thời gian dừng đỗ (phút):", "_BaoCao_BaoCaoDungDo_TongThoiGianDungDo1.png")

def caseid_report11(self):
    module_other_app.get_datachecklist("Report11")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.report_stop_detail(self, "Report11", eventname, result, var_app.report_detail2, var_app.report_detail_2, 0, 23,
                                         "Tổng thời gian dừng đỗ:", "_BaoCao_BaoCaoDungDo_TongThoiGianDungDo2.png")

def caseid_report12(self):
    module_other_app.get_datachecklist("Report12")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.report_stop_detail(self, "Report12", eventname, result, var_app.report_detail3, var_app.report_detail_3, 0, 39,
                                         "Tổng thời gian bật máy khi dừng (phút):", "_BaoCao_BaoCaoDungDo_TongThoiGianBatMayKhiDung.png")

def caseid_report13(self):
    module_other_app.get_datachecklist("Report13")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.report_stop_detail(self, "Report13", eventname, result, var_app.report_detail4, var_app.report_detail_4, 0, 44,
                                         "Tổng thời gian bật điều hòa khi dừng (phút):", "_BaoCao_BaoCaoDungDo_TongThoiGianBatDieuHoa.png")

def caseid_report13_1(self):
    module_other_app.get_datachecklist("Report13_1")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.report_stop_see_detail(self, "Report13_1", eventname, result)

def caseid_report13_2(self):
    module_other_app.get_datachecklist("Report13_2")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.report_stop_check_detail(self, "Report13_2", eventname, result, "0", var_app.info_vehicle_name1, var_app.info_vehicle_name_1,
                                               var_app.info_vehicle_detail1, var_app.info_vehicle_detail_1, "Biển số xe", "_BaoCaoDungDo_XemChiTiet_BienSoXe.png")

def caseid_report13_3(self):
    module_other_app.get_datachecklist("Report13_3")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.report_stop_check_detail(self, "Report13_3", eventname, result, "0", var_app.info_vehicle_name2, var_app.info_vehicle_name_2,
                                               var_app.info_vehicle_detail2, var_app.info_vehicle_detail_2,
                                               "Tên lái xe", "_BaoCaoDungDo_XemChiTiet_TenLaiXe.png")

def caseid_report13_3a(self):
    module_other_app.get_datachecklist("Report13_3a")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.report_stop_check_detail(self, "Report13_3a", eventname, result, "0", var_app.info_vehicle_name3, var_app.info_vehicle_name_3,
                                               var_app.info_vehicle_detail3, var_app.info_vehicle_detail_3,
                                               "Giấy phép lái xe", "_BaoCaoDungDo_XemChiTiet_GiayPhepLaiXe.png")

def caseid_report13_4(self):
    module_other_app.get_datachecklist("Report13_4")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.report_stop_check_detail(self, "Report13_4", eventname, result, "1", var_app.info_vehicle_name4, var_app.info_vehicle_name_4,
                                               var_app.info_vehicle_detail4, var_app.info_vehicle_detail_4,
                                               "Mã nhân viên", "_BaoCaoDungDo_XemChiTiet_MaNhanVien.png")

def caseid_report13_5(self):
    module_other_app.get_datachecklist("Report13_5")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.report_stop_check_detail(self, "Report13_5", eventname, result, "1", var_app.info_vehicle_name5, var_app.info_vehicle_name_5,
                                               var_app.info_vehicle_detail5, var_app.info_vehicle_detail_5,
                                               "Số điện thoại", "_BaoCaoDungDo_XemChiTiet_SoDienThoai.png")

def caseid_report13_6(self):
    module_other_app.get_datachecklist("Report13_6")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.report_stop_check_detail(self, "Report13_6", eventname, result, "0", var_app.info_vehicle_name6, var_app.info_vehicle_name_6,
                                               var_app.info_vehicle_detail6, var_app.info_vehicle_detail_6,
                                               "Thời gian", "_BaoCaoDungDo_XemChiTiet_ThoiGian.png")

def caseid_report13_7(self):
    module_other_app.get_datachecklist("Report13_7")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.report_stop_check_detail(self, "Report13_7", eventname, result, "0", var_app.info_vehicle_name7, var_app.info_vehicle_name_7,
                                               var_app.info_vehicle_detail7, var_app.info_vehicle_detail_7,
                                               "Thời gian (phút)", "_BaoCaoDungDo_XemChiTiet_ThoiGianPhut.png")

def caseid_report13_8(self):
    module_other_app.get_datachecklist("Report13_8")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.report_stop_check_detail(self, "Report13_8", eventname, result, "0", var_app.info_vehicle_name8, var_app.info_vehicle_name_8,
                                               var_app.info_vehicle_detail8, var_app.info_vehicle_detail_8,
                                               "Thời gian dừng đỗ", "_BaoCaoDungDo_XemChiTiet_ThoiGianDungDo.png")

def caseid_report13_9(self):
    module_other_app.get_datachecklist("Report13_9")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.report_stop_check_detail(self, "Report13_9", eventname, result, "0", var_app.info_vehicle_name9, var_app.info_vehicle_name_9,
                                               var_app.info_vehicle_detail9, var_app.info_vehicle_detail_9,
                                               "Nổ máy khi dừng (phút)", "_BaoCaoDungDo_XemChiTiet_NoMayKhiDungPhut.png")

def caseid_report13_10(self):
    module_other_app.get_datachecklist("Report13_10")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.report_stop_check_detail(self, "Report13_10", eventname, result, "0", var_app.info_vehicle_name10, var_app.info_vehicle_name_10,
                                               var_app.info_vehicle_detail10, var_app.info_vehicle_detail_10,
                                               "Bật ĐH khi dừng (phút)", "_BaoCaoDungDo_XemChiTiet_BatDieuHoaKhiDungPhut.png")

def caseid_report13_11(self):
    module_other_app.get_datachecklist("Report13_11")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.report_stop_check_detail(self, "Report13_11", eventname, result, "0", var_app.info_vehicle_name11, var_app.info_vehicle_name_11,
                                               var_app.info_vehicle_detail11, var_app.info_vehicle_detail_11,
                                               "Nhiệt độ", "_BaoCaoDungDo_XemChiTiet_NhietDo.png")

def caseid_report13_12(self):
    module_other_app.get_datachecklist("Report13_12")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.report_stop_check_detail(self, "Report13_12", eventname, result, "0", var_app.info_vehicle_name12, var_app.info_vehicle_name_12,
                                               var_app.info_vehicle_detail12, var_app.info_vehicle_detail_12,
                                               "Địa điểm", "_BaoCaoDungDo_XemChiTiet_DiaDiem.png")



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
        homepage_app.move_module(self, "Report15", eventname, result, var_app.detailed_activity_reports, 0.8, 0.65, 0.2, 0.65, 1000,
                                                        "Trang chủ - Báo cáo chi tiết hoạt động", var_app.check_detailed_activity_reports,
                                                         "BÁO CÁO CHI TIẾT HOẠT ĐỘNG", "_TrangChu_BaoCaoChiTietHoatDong.png")
    except:
        report_app.general.report_back(self)
        homepage_app.move_module(self, "Report15", eventname, result, var_app.detailed_activity_reports, 0.8, 0.65, 0.2, 0.65, 1000,
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
    report_app.report.detailed_activity_reports_type(self, "Report17", eventname, result, var_app.report_today,
                                              var_app.STT, "Trang chủ - Báo cáo chi tiết hoạt động", "_TrangChu_BaoCaoChiTietHoatDong_HomNay.png")

def caseid_report18(self):
    module_other_app.get_datachecklist("Report18")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.detailed_activity_reports_type(self, "Report18", eventname, result, var_app.report_7day,
                                              var_app.STT, "Trang chủ - Báo cáo chi tiết hoạt động", "_TrangChu_BaoCaoChiTietHoatDong_7Ngay.png")

def caseid_report19(self):
    module_other_app.get_datachecklist("Report19")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.detailed_activity_reports_type(self, "Report19", eventname, result, var_app.report_15day,
                                              var_app.STT, "Trang chủ - Báo cáo chi tiết hoạt động", "_TrangChu_BaoCaoChiTietHoatDong_15Ngay.png")

def caseid_report20(self):
    module_other_app.get_datachecklist("Report20")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.detailed_activity_reports_type(self, "Report20", eventname, result, var_app.report_other,
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
    report_app.report.detailed_activity_reports_detail(self, "Report23", eventname, result, var_app.report_detail_1, var_app.report_detail1, 0, 28,
                                         "Tổng tiêu hao khi di chuyển:", "_TrangChu_BaoCaoChiTietHoatDong_TongTieuHaoKhiDiChuyen.png")

def caseid_report24(self):
    module_other_app.get_datachecklist("Report24")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.detailed_activity_reports_detail(self, "Report24", eventname, result, var_app.report_detail_2, var_app.report_detail2, 0, 25,
                                         "Tổng Thời gian hoạt động:", "_TrangChu_BaoCaoChiTietHoatDong_TongThoiGianHoatDong.png")

def caseid_report25(self):
    module_other_app.get_datachecklist("Report25")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.detailed_activity_reports_detail(self, "Report25", eventname, result, var_app.report_detail_3, var_app.report_detail3, 0, 15,
                                         "Tổng số Km GPS:", "_TrangChu_BaoCaoChiTietHoatDong_TongSoKmGps.png")
def caseid_report26(self):
    module_other_app.get_datachecklist("Report26")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.detailed_activity_reports_detail(self, "Report26", eventname, result, var_app.report_detail_4, var_app.report_detail4, 0, 14,
                                         "Tổng số Km Cơ:", "_TrangChu_BaoCaoChiTietHoatDong_TongSoKmCo.png")

def caseid_report27(self):
    module_other_app.get_datachecklist("Report27")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.detailed_activity_reports_detail(self, "Report27", eventname, result, var_app.report_detail_5, var_app.report_detail5, 0, 28,
                                         "Tổng số định mức nhiên liệu:", "_TrangChu_BaoCaoChiTietHoatDong_TongSoDinhMucNhienLieu.png")

def caseid_report27_1(self):
    module_other_app.get_datachecklist("Report27_1")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.detailed_activity_reports_see_detail(self, "Report27_1", eventname, result)

def caseid_report27_2(self):
    module_other_app.get_datachecklist("Report27_2")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.detailed_activity_reports_check_detail(self, "Report27_2", eventname, result, "1", var_app.info_vehicle_name1, var_app.info_vehicle_name_1,
                                                             var_app.info_vehicle_detail1, var_app.info_vehicle_detail_1, "Loại xe", "_BaoCaoChiTietHoatDong_XemChiTiet_LoaiXe.png")

def caseid_report27_3(self):
    module_other_app.get_datachecklist("Report27_3")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.detailed_activity_reports_check_detail(self, "Report27_3", eventname, result, "0", var_app.info_vehicle_name2, var_app.info_vehicle_name_2,
                                                             var_app.info_vehicle_detail2, var_app.info_vehicle_detail_2, "Biển số xe", "_BaoCaoChiTietHoatDong_XemChiTiet_BienSoXe.png")

def caseid_report27_4(self):
    module_other_app.get_datachecklist("Report27_4")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.detailed_activity_reports_check_detail(self, "Report27_4", eventname, result, "0", var_app.info_vehicle_name3, var_app.info_vehicle_name_3,
                                                             var_app.info_vehicle_detail3, var_app.info_vehicle_detail_3, "Ngày tháng", "_BaoCaoChiTietHoatDong_XemChiTiet_NgayThang.png")

def caseid_report27_5(self):
    module_other_app.get_datachecklist("Report27_5")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.detailed_activity_reports_check_detail(self, "Report27_5", eventname, result, "0", var_app.info_vehicle_name4, var_app.info_vehicle_name_4,
                                                             var_app.info_vehicle_detail4, var_app.info_vehicle_detail_4, "Giờ đi", "_BaoCaoChiTietHoatDong_XemChiTiet_GioDi.png")

def caseid_report27_6(self):
    module_other_app.get_datachecklist("Report27_6")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.detailed_activity_reports_check_detail(self, "Report27_6", eventname, result, "0", var_app.info_vehicle_name5, var_app.info_vehicle_name_5,
                                                             var_app.info_vehicle_detail5, var_app.info_vehicle_detail_5, "Giờ đến", "_BaoCaoChiTietHoatDong_XemChiTiet_GioDen.png")

def caseid_report27_7(self):
    module_other_app.get_datachecklist("Report27_7")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.detailed_activity_reports_check_detail(self, "Report27_7", eventname, result, "0", var_app.info_vehicle_name6, var_app.info_vehicle_name_6,
                                                             var_app.info_vehicle_detail6, var_app.info_vehicle_detail_6,
                                               "Thời gian hoạt động", "_BaoCaoChiTietHoatDong_XemChiTiet_ThoiGianHoatDong.png")

def caseid_report27_8(self):
    module_other_app.get_datachecklist("Report27_8")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.detailed_activity_reports_check_detail(self, "Report27_8", eventname, result, "0", var_app.info_vehicle_name7, var_app.info_vehicle_name_7,
                                                             var_app.info_vehicle_detail7, var_app.info_vehicle_detail_7,
                                               "Km (GPS)", "_BaoCaoChiTietHoatDong_XemChiTiet_KmGps.png")

def caseid_report27_9(self):
    module_other_app.get_datachecklist("Report27_9")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.detailed_activity_reports_check_detail(self, "Report27_9", eventname, result, "0", var_app.info_vehicle_name8, var_app.info_vehicle_name_8,
                                                             var_app.info_vehicle_detail8, var_app.info_vehicle_detail_8,
                                               "Km cơ", "_BaoCaoChiTietHoatDong_XemChiTiet_KmCo.png")

def caseid_report27_10(self):
    module_other_app.get_datachecklist("Report27_10")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.detailed_activity_reports_check_detail(self, "Report27_10", eventname, result, "0", var_app.info_vehicle_name9, var_app.info_vehicle_name_9,
                                                             var_app.info_vehicle_detail9, var_app.info_vehicle_detail_9,
                                               "Định mức nhiên liệu", "_BaoCaoChiTietHoatDong_XemChiTiet_DinhMucNhienLieu.png")

def caseid_report27_11(self):
    module_other_app.get_datachecklist("Report27_11")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.detailed_activity_reports_check_detail(self, "Report27_11", eventname, result, "0", var_app.info_vehicle_name10, var_app.info_vehicle_name_10,
                                                             var_app.info_vehicle_detail10, var_app.info_vehicle_detail_10,
                                               "Nhiên liệu tiêu thụ", "_BaoCaoChiTietHoatDong_XemChiTiet_DinhMucTieuThu.png")

def caseid_report27_12(self):
    module_other_app.get_datachecklist("Report27_12")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.detailed_activity_reports_check_detail(self, "Report27_12", eventname, result, "1", var_app.info_vehicle_name11, var_app.info_vehicle_name_11,
                                                             var_app.info_vehicle_detail11, var_app.info_vehicle_detail_11,
                                               "Địa chỉ đi", "_BaoCaoChiTietHoatDong_XemChiTiet_DiaChiDi.png")

def caseid_report27_13(self):
    module_other_app.get_datachecklist("Report27_13")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.detailed_activity_reports_check_detail(self, "Report27_13", eventname, result, "1", var_app.info_vehicle_name12, var_app.info_vehicle_name_12,
                                                             var_app.info_vehicle_detail12, var_app.info_vehicle_detail_12,
                                               "Địa chỉ đến", "_BaoCaoChiTietHoatDong_XemChiTiet_DiaChiDen.png")

def caseid_report27_14(self):
    module_other_app.get_datachecklist("Report27_14")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.detailed_activity_reports_check_detail(self, "Report27_14", eventname, result, "1", var_app.info_vehicle_name13, var_app.info_vehicle_name_13,
                                                             var_app.info_vehicle_detail13, var_app.info_vehicle_detail_13,
                                               "Cuốc bù", "_BaoCaoChiTietHoatDong_XemChiTiet_CuocBu.png")

def caseid_report27_15(self):
    module_other_app.get_datachecklist("Report27_15")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.detailed_activity_reports_check_detail(self, "Report27_15", eventname, result, "0", var_app.info_vehicle_name14, var_app.info_vehicle_name_14,
                                                             var_app.info_vehicle_detail14, var_app.info_vehicle_detail_14,
                                               "Số lít bắt đầu", "_BaoCaoChiTietHoatDong_XemChiTiet_SoLitBatDau.png")

def caseid_report27_16(self):
    module_other_app.get_datachecklist("Report27_16")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.detailed_activity_reports_check_detail(self, "Report27_16", eventname, result, "0", var_app.info_vehicle_name15, var_app.info_vehicle_name_15,
                                                             var_app.info_vehicle_detail15, var_app.info_vehicle_detail_15,
                                               "Số lít kết thúc", "_BaoCaoChiTietHoatDong_XemChiTiet_SoLitKetThuc.png")




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
        homepage_app.move_module(self, "Report29", eventname, result, var_app.summary_report_of_activities, 0.8, 0.65, 0.2, 0.65, 1000,
                                                        "Trang chủ - Báo cáo tổng hợp hoạt động", var_app.check_summary_report_of_activities,
                                                         "BÁO CÁO TỔNG HỢP HOẠT ĐỘNG", "_TrangChu_BaoCaoTongHopHoatDong.png")
    except:
        report_app.general.report_back(self)
        homepage_app.move_module(self, "Report29", eventname, result, var_app.summary_report_of_activities, 0.8, 0.65, 0.2, 0.65, 1000,
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
                                              var_app.STT, "Trang chủ - Báo cáo tổng hợp hoạt động", "_TrangChu_BaoCaoTongHopHoatDong_HomNay.png")

def caseid_report32(self):
    module_other_app.get_datachecklist("Report32")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.summary_report_of_activities_type(self, "Report32", eventname, result, var_app.report_7day,
                                              var_app.STT, "Trang chủ - Báo cáo tổng hợp hoạt động", "_TrangChu_BaoCaoTongHopHoatDong_7Ngay.png")

def caseid_report33(self):
    module_other_app.get_datachecklist("Report33")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.summary_report_of_activities_type(self, "Report33", eventname, result, var_app.report_15day,
                                              var_app.STT, "Trang chủ - Báo cáo tổng hợp hoạt động", "_TrangChu_BaoCaoTongHopHoatDong_15Ngay.png")

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
    report_app.report.summary_report_of_activities_detail(self, "Report38", eventname, result, var_app.report_detail1, var_app.report_detail_1, 0, 24,
                                         "Tổng thời gian lăn bánh:", "_TrangChu_BaoCaoTongHopHoatDong_TongThoiGianLanBanh.png")

def caseid_report39(self):
    module_other_app.get_datachecklist("Report39")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.summary_report_of_activities_detail(self, "Report39", eventname, result, var_app.report_detail2, var_app.report_detail_2, 0, 12,
                                         "Tổng Km GPS:", "_TrangChu_BaoCaoTongHopHoatDong_TongKmGps.png")

def caseid_report40(self):
    module_other_app.get_datachecklist("Report40")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.summary_report_of_activities_detail(self, "Report40", eventname, result, var_app.report_detail3, var_app.report_detail_3, 0, 11,
                                         "Tổng Km cơ:", "_TrangChu_BaoCaoTongHopHoatDong_TongKmCo.png")

def caseid_report41(self):
    module_other_app.get_datachecklist("Report41")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.summary_report_of_activities_detail(self, "Report41", eventname, result, var_app.report_detail4, var_app.report_detail_4, 0, 20,
                                         "Tổng số lần dừng đỗ:", "_TrangChu_BaoCaoTongHopHoatDong_TongSoLanDungDo.png")

def caseid_report42(self):
    module_other_app.get_datachecklist("Report42")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.summary_report_of_activities_detail(self, "Report42", eventname, result, var_app.report_detail5, var_app.report_detail_5, 0, 33,
                                         "Tổng số lần dừng đỗ bật điều hòa:", "_TrangChu_BaoCaoTongHopHoatDong_TongSoLanDungDoBatDieuHoa.png")

def caseid_report43(self):
    module_other_app.get_datachecklist("Report43")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.summary_report_of_activities_detail(self, "Report43", eventname, result, var_app.report_detail6, var_app.report_detail_6, 0, 28,
                                         "Trung bình vận tốc cao nhất:", "_TrangChu_BaoCaoTongHopHoatDong_TrungBinhVanTocCaoNhat.png")

def caseid_report44(self):
    module_other_app.get_datachecklist("Report44")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.summary_report_of_activities_detail(self, "Report44", eventname, result, var_app.report_detail7, var_app.report_detail_7, 0, 30,
                                         "Trung bình Vận tốc trung bình:", "_TrangChu_BaoCaoTongHopHoatDong_TrungBinhVanTocTrungBinh.png")

def caseid_report44_1(self):
    module_other_app.get_datachecklist("Report44_1")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.summary_report_of_activities_see_detail(self, "Report44_1", eventname, result)

def caseid_report44_2(self):
    module_other_app.get_datachecklist("Report44_2")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.summary_report_of_activities_check_detail(self, "Report44_2", eventname, result, "1", var_app.info_vehicle_name1, var_app.info_vehicle_name_1,
                                                                var_app.info_vehicle_detail1, var_app.info_vehicle_detail_1, "Loại xe", "_BaoCaoTongHopHoatDong_XemChiTiet_LoaiXe.png")

def caseid_report44_3(self):
    module_other_app.get_datachecklist("Report44_3")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.summary_report_of_activities_check_detail(self, "Report44_3", eventname, result, "0", var_app.info_vehicle_name2, var_app.info_vehicle_name_2,
                                                                var_app.info_vehicle_detail2, var_app.info_vehicle_detail_2,
                                               "Biển số xe", "_BaoCaoTongHopHoatDong_XemChiTiet_BienSoXe.png")

def caseid_report44_4(self):
    module_other_app.get_datachecklist("Report44_4")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.summary_report_of_activities_check_detail(self, "Report44_4", eventname, result, "0", var_app.info_vehicle_name3, var_app.info_vehicle_name_3,
                                                                var_app.info_vehicle_detail3, var_app.info_vehicle_detail_3,
                                               "Ngày tháng", "_BaoCaoTongHopHoatDong_XemChiTiet_NgayThang.png")

def caseid_report44_5(self):
    module_other_app.get_datachecklist("Report44_5")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.summary_report_of_activities_check_detail(self, "Report44_5", eventname, result, "0", var_app.info_vehicle_name4, var_app.info_vehicle_name_4,
                                                                var_app.info_vehicle_detail4, var_app.info_vehicle_detail_4,
                                               "Giờ đi", "_BaoCaoTongHopHoatDong_XemChiTiet_GioDi.png")

def caseid_report44_6(self):
    module_other_app.get_datachecklist("Report44_6")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.summary_report_of_activities_check_detail(self, "Report44_6", eventname, result, "0", var_app.info_vehicle_name5, var_app.info_vehicle_name_5,
                                                                var_app.info_vehicle_detail5, var_app.info_vehicle_detail_5,
                                               "Giờ đến", "_BaoCaoTongHopHoatDong_XemChiTiet_GioDen.png")

def caseid_report44_7(self):
    module_other_app.get_datachecklist("Report44_7")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.summary_report_of_activities_check_detail(self, "Report44_7", eventname, result, "0", var_app.info_vehicle_name6, var_app.info_vehicle_name_6,
                                                                var_app.info_vehicle_detail6, var_app.info_vehicle_detail_6,
                                               "Thời gian lăn bánh", "_BaoCaoTongHopHoatDong_XemChiTiet_ThoiGianLanBanh.png")


def caseid_report44_8(self):
    module_other_app.get_datachecklist("Report44_8")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.summary_report_of_activities_check_detail(self, "Report44_8", eventname, result, "0", var_app.info_vehicle_name7, var_app.info_vehicle_name_7,
                                                                var_app.info_vehicle_detail7, var_app.info_vehicle_detail_7,
                                               "Thời gian dừng đỗ", "_BaoCaoTongHopHoatDong_XemChiTiet_ThoiGianDungDo.png")

def caseid_report44_9(self):
    module_other_app.get_datachecklist("Report44_9")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.summary_report_of_activities_check_detail(self, "Report44_9", eventname, result, "0", var_app.info_vehicle_name8, var_app.info_vehicle_name_8,
                                                                var_app.info_vehicle_detail8, var_app.info_vehicle_detail_8,
                                               "Km (GPS)", "_BaoCaoTongHopHoatDong_XemChiTiet_KmGps.png")

def caseid_report44_10(self):
    module_other_app.get_datachecklist("Report44_10")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.summary_report_of_activities_check_detail(self, "Report44_10", eventname, result, "0", var_app.info_vehicle_name9, var_app.info_vehicle_name_9,
                                                                var_app.info_vehicle_detail9, var_app.info_vehicle_detail_9,
                                               "Km cơ", "_BaoCaoTongHopHoatDong_XemChiTiet_KmCo.png")

def caseid_report44_11(self):
    module_other_app.get_datachecklist("Report44_11")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.summary_report_of_activities_check_detail(self, "Report44_11", eventname, result, "0", var_app.info_vehicle_name10, var_app.info_vehicle_name_10,
                                                                var_app.info_vehicle_detail10, var_app.info_vehicle_detail_10,
                                               "Số lần dừng đỗ", "_BaoCaoTongHopHoatDong_XemChiTiet_SoLanDungDo.png")

def caseid_report44_12(self):
    module_other_app.get_datachecklist("Report44_12")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.summary_report_of_activities_check_detail(self, "Report44_12", eventname, result, "0", var_app.info_vehicle_name11, var_app.info_vehicle_name_11,
                                                                var_app.info_vehicle_detail11, var_app.info_vehicle_detail_11,
                                               "Bật điều hòa (phút)", "_BaoCaoTongHopHoatDong_XemChiTiet_BatDieuHoaPhut.png")

def caseid_report44_13(self):
    module_other_app.get_datachecklist("Report44_13")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.summary_report_of_activities_check_detail(self, "Report44_13", eventname, result, "0", var_app.info_vehicle_name12, var_app.info_vehicle_name_12,
                                                                var_app.info_vehicle_detail12, var_app.info_vehicle_detail_12,
                                               "Vận tốc cực đại", "_BaoCaoTongHopHoatDong_XemChiTiet_VanTocCucDai.png")

def caseid_report44_14(self):
    module_other_app.get_datachecklist("Report44_14")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.summary_report_of_activities_check_detail(self, "Report44_14", eventname, result, "0", var_app.info_vehicle_name13, var_app.info_vehicle_name_13,
                                                                var_app.info_vehicle_detail13, var_app.info_vehicle_detail_13,
                                               "Vận tốc trung bình", "_BaoCaoTongHopHoatDong_XemChiTiet_VanTocTrungbinh.png")


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
        homepage_app.move_module(self, "Report46", eventname, result, var_app.report_entering_and_exiting_the_station, 0.8, 0.65, 0.2, 0.65, 1000,
                                                        "Trang chủ - Báo cáo ra vào trạm", var_app.check_report_entering_and_exiting_the_station,
                                                         "BÁO CÁO RA VÀO TRẠM", "_TrangChu_BaoCaoRaVaotram.png")
    except:
        report_app.general.report_back(self)
        homepage_app.move_module(self, "Report46", eventname, result, var_app.report_entering_and_exiting_the_station, 0.8, 0.65, 0.2, 0.65, 1000,
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
                                              var_app.STT, "Trang chủ - Báo cáo ra vào trạm", "_TrangChu_BaoCaoRaVaotram_HomNay.png")

def caseid_report49(self):
    module_other_app.get_datachecklist("Report49")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.report_entering_and_exiting_the_station_type(self, "Report49", eventname, result, var_app.report_7day,
                                              var_app.STT, "Trang chủ - Báo cáo ra vào trạm", "_TrangChu_BaoCaoRaVaotram_7Ngay.png")

def caseid_report50(self):
    module_other_app.get_datachecklist("Report50")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.report_entering_and_exiting_the_station_type(self, "Report50", eventname, result, var_app.report_15day,
                                              var_app.STT, "Trang chủ - Báo cáo ra vào trạm", "_TrangChu_BaoCaoRaVaotram_15Ngay.png")

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
        homepage_app.move_module(self, "Report56", eventname, result, var_app.report_speeding, 0.8, 0.65, 0.2, 0.65, 1000,
                                                        "Trang chủ - Báo cáo quá tốc độ", var_app.check_report_speeding,
                                                         "BÁO CÁO QUÁ TỐC ĐỘ", "_TrangChu_BaoCaoQuaTocDo.png")
    except:
        report_app.general.report_back(self)
        homepage_app.move_module(self, "Report56", eventname, result, var_app.report_speeding, 0.8, 0.65, 0.2, 0.65, 1000,
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
        homepage_app.move_module(self, "Report65", eventname, result, var_app.business_trip_report, 0.8, 0.65, 0.2, 0.65, 1000,
                                                        "Trang chủ - Báo cáo chuyến kinh doanh", var_app.check_business_trip_report,
                                                         "BÁO CÁO CHUYẾN KINH DOANH", "_TrangChu_BaoCaoChuyenKinhDoanh.png")
    except:
        report_app.general.report_back(self)
        homepage_app.move_module(self, "Report65", eventname, result, var_app.business_trip_report, 0.8, 0.65, 0.2, 0.65, 1000,
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
                                              var_app.STT, "Trang chủ - Báo cáo chuyến kinh doanh", "_TrangChu_BaoCaoChuyenKinhDoanh_HomNay.png")

def caseid_report68(self):
    module_other_app.get_datachecklist("Report68")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.business_trip_report_type(self, "Report68", eventname, result, var_app.report_7day,
                                              var_app.STT, "Trang chủ - Báo cáo chuyến kinh doanh", "_TrangChu_BaoCaoChuyenKinhDoanh_7Ngay.png")

def caseid_report69(self):
    module_other_app.get_datachecklist("Report69")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.business_trip_report_type(self, "Report69", eventname, result, var_app.report_15day,
                                              var_app.STT, "Trang chủ - Báo cáo chuyến kinh doanh", "_TrangChu_BaoCaoChuyenKinhDoanh_15Ngay.png")

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
    report_app.report.business_trip_report_detail(self, "Report74", eventname, result, var_app.report_detail1, var_app.report_detail_1, 0, 23,
                                         "Tổng số phút hoạt động:", "TrangChu_BaoCaoChuyenKinhDoanh_TongSoPhutHoatDong.png")

def caseid_report75(self):
    module_other_app.get_datachecklist("Report75")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.business_trip_report_detail(self, "Report75", eventname, result, var_app.report_detail2, var_app.report_detail_2, 0, 12,
                                         "Tổng km GPS:", "TrangChu_BaoCaoChuyenKinhDoanh_TongKmGps.png")

def caseid_report76(self):
    module_other_app.get_datachecklist("Report76")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.business_trip_report_detail(self, "Report76", eventname, result, var_app.report_detail3, var_app.report_detail_3, 0, 11,
                                         "Tổng km cơ:", "TrangChu_BaoCaoChuyenKinhDoanh_TongKmCo.png")

def caseid_report77(self):
    module_other_app.get_datachecklist("Report77")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.business_trip_report_detail(self, "Report77", eventname, result, var_app.report_detail4, var_app.report_detail_4, 0, 17,
                                         "Tổng NL tiêu thụ:", "TrangChu_BaoCaoChuyenKinhDoanh_TongNhienLieuTieuThu.png")

def caseid_report78(self):
    module_other_app.get_datachecklist("Report78")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.business_trip_report_detail(self, "Report78", eventname, result, var_app.report_detail5, var_app.report_detail_5, 0, 26,
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
        homepage_app.move_module(self, "Report80", eventname, result, var_app.report_loss_of_signal, 0.8, 0.65, 0.2, 0.65, 1000,
                                                        "Trang chủ - Báo cáo mất tín hiệu", var_app.check_report_loss_of_signal,
                                                         "BÁO CÁO MẤT TÍN HIỆU", "_TrangChu_BaoCaoMatTinHieu.png")
    except:
        report_app.general.report_back(self)
        homepage_app.move_module(self, "Report80", eventname, result, var_app.report_loss_of_signal, 0.8, 0.65, 0.2, 0.65, 1000,
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
                                              var_app.STT, "Trang chủ - Báo cáo mất tín hiệu", "_TrangChu_BaoCaoMatTinHieu_HomNay.png")

def caseid_report83(self):
    module_other_app.get_datachecklist("Report83")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.report_loss_of_signal_type(self, "Report83", eventname, result, var_app.report_7day,
                                              var_app.STT, "Trang chủ - Báo cáo mất tín hiệu", "_TrangChu_BaoCaoMatTinHieu_7Ngay.png")

def caseid_report84(self):
    module_other_app.get_datachecklist("Report84")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.report_loss_of_signal_type(self, "Report84", eventname, result, var_app.report_15day,
                                              var_app.STT, "Trang chủ - Báo cáo mất tín hiệu", "_TrangChu_BaoCaoMatTinHieu_15Ngay.png")

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
    report_app.report.report_loss_of_signal_detail(self, "Report89", eventname, result, var_app.report_detail1, var_app.report_detail_1, 0, 28,
                                         "Tổng thời gian mất tín hiệu:", "_TrangChu_BaoCaoMatTinHieu_TongThoiGianMatTinHieu.png")

def caseid_report89_1(self):
    module_other_app.get_datachecklist("Report89_1")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.report_loss_of_signal_see_detail(self, "Report89_1", eventname, result)

def caseid_report89_2(self):
    module_other_app.get_datachecklist("Report89_2")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.report_loss_of_signal_check_detail(self, "Report89_2", eventname, result, "0", var_app.info_vehicle_name1, var_app.info_vehicle_name_1,
                                                         var_app.info_vehicle_detail1, var_app.info_vehicle_detail_1, "Biển số xe", "_BaoCaoMatTinHieu_XemChiTiet_BienSoXe.png")

def caseid_report89_3(self):
    module_other_app.get_datachecklist("Report89_3")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.report_loss_of_signal_check_detail(self, "Report89_3", eventname, result, "0", var_app.info_vehicle_name2, var_app.info_vehicle_name_2,
                                                         var_app.info_vehicle_detail2, var_app.info_vehicle_detail_2,
                                               "Thời gian bắt đầu", "_BaoCaoMatTinHieu_XemChiTiet_ThoiGianBatDau.png")

def caseid_report89_4(self):
    module_other_app.get_datachecklist("Report89_4")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.report_loss_of_signal_check_detail(self, "Report89_4", eventname, result, "0", var_app.info_vehicle_name3, var_app.info_vehicle_name_3,
                                                         var_app.info_vehicle_detail3, var_app.info_vehicle_detail_3,
                                               "Thời gian kết thúc", "_BaoCaoMatTinHieu_XemChiTiet_ThoiGianKetThuc.png")

def caseid_report89_5(self):
    module_other_app.get_datachecklist("Report89_5")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.report_loss_of_signal_check_detail(self, "Report89_5", eventname, result, "0", var_app.info_vehicle_name4, var_app.info_vehicle_name_4,
                                                         var_app.info_vehicle_detail4, var_app.info_vehicle_detail_4,
                                               "Thời gian mất tín hiệu", "_BaoCaoMatTinHieu_XemChiTiet_ThoiGianMatTinHieu.png")

def caseid_report89_6(self):
    module_other_app.get_datachecklist("Report89_6")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.report_loss_of_signal_check_detail(self, "Report89_6", eventname, result, "1", var_app.info_vehicle_name5, var_app.info_vehicle_name_5,
                                                         var_app.info_vehicle_detail5, var_app.info_vehicle_detail_5,
                                               "Địa điểm bắt đầu", "_BaoCaoMatTinHieu_XemChiTiet_DiaDiemBatDau.png")

def caseid_report89_7(self):
    module_other_app.get_datachecklist("Report89_7")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.report_loss_of_signal_check_detail(self, "Report89_7", eventname, result, "1", var_app.info_vehicle_name6, var_app.info_vehicle_name_6,
                                                         var_app.info_vehicle_detail6, var_app.info_vehicle_detail_6,
                                               "Địa điểm kết thúc", "_BaoCaoMatTinHieu_XemChiTiet_DiaDiemKetThuc.png")

def caseid_report89_8(self):
    module_other_app.get_datachecklist("Report89_8")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.report_loss_of_signal_check_detail(self, "Report89_8", eventname, result, "0", var_app.info_vehicle_name7, var_app.info_vehicle_name_7,
                                                         var_app.info_vehicle_detail7, var_app.info_vehicle_detail_7,
                                               "Trạng thái", "_BaoCaoMatTinHieu_XemChiTiet_TrangThai.png")



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
        homepage_app.move_module(self, "Report91", eventname, result, var_app.fuel_dump_report, 0.8, 0.65, 0.2, 0.65, 1000,
                                                        "Trang chủ - Báo cáo đổ hút nhiên liệu", var_app.check_fuel_dump_report,
                                                         "BÁO CÁO ĐỔ HÚT NHIÊN LIỆU", "_TrangChu_BaoCaoDoHutNhienLieu.png")
    except:
        report_app.general.report_back(self)
        homepage_app.move_module(self, "Report91", eventname, result, var_app.fuel_dump_report, 0.8, 0.65, 0.2, 0.65, 1000,
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
                                              var_app.STT, "Trang chủ - Báo cáo đổ hút nhiên liệu", "_TrangChu_BaoCaoDoHutNhienLieu_HomNay.png")

def caseid_report94(self):
    module_other_app.get_datachecklist("Report94")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.fuel_dump_report_type(self, "Report94", eventname, result, var_app.report_7day,
                                              var_app.STT, "Trang chủ - Báo cáo đổ hút nhiên liệu", "_TrangChu_BaoCaoDoHutNhienLieu_7Ngay.png")

def caseid_report95(self):
    module_other_app.get_datachecklist("Report95")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.fuel_dump_report_type(self, "Report95", eventname, result, var_app.report_15day,
                                              var_app.STT, "Trang chủ - Báo cáo đổ hút nhiên liệu", "_TrangChu_BaoCaoDoHutNhienLieu_15Ngay.png")

def caseid_report96(self):
    module_other_app.get_datachecklist("Report96")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.fuel_dump_report_type1(self, "Report96", eventname, result, var_app.report_other,
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
    report_app.report.fuel_dump_report_detail(self, "Report100", eventname, result, var_app.report_detail1, var_app.report_detail_1, 0, 21,
                                         "Tổng số lít thay đổi:", "_TrangChu_BaoCaoDoHutNhienLieu_TongSoLitThayDoi.png")

def caseid_report100_1(self):
    module_other_app.get_datachecklist("Report100_1")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.fuel_dump_report_see_detail(self, "Report100_1", eventname, result)

def caseid_report100_2(self):
    module_other_app.get_datachecklist("Report100_2")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.fuel_dump_report_check_detail(self, "Report100_2", eventname, result, "0", var_app.info_vehicle_name1, var_app.info_vehicle_name_1,
                                                    var_app.info_vehicle_detail1, var_app.info_vehicle_detail_1,
                                               "Biển số xe", "_BaoCaoDoHutNhienLieu_XemChiTiet_BienSoXe.png")

def caseid_report100_3(self):
    module_other_app.get_datachecklist("Report100_3")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.fuel_dump_report_check_detail(self, "Report100_3", eventname, result, "0", var_app.info_vehicle_name2, var_app.info_vehicle_name_2,
                                                    var_app.info_vehicle_detail2, var_app.info_vehicle_detail_2,
                                               "Thời gian", "_BaoCaoDoHutNhienLieu_XemChiTiet_Thoigian.png")

def caseid_report100_4(self):
    module_other_app.get_datachecklist("Report100_4")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.fuel_dump_report_check_detail(self, "Report100_4", eventname, result, "0", var_app.info_vehicle_name3, var_app.info_vehicle_name_3,
                                                    var_app.info_vehicle_detail3, var_app.info_vehicle_detail_3,
                                               "Km tích lũy từ đầu ngày", "_BaoCaoDoHutNhienLieu_XemChiTiet_KmTichLuyTuDauNgay.png")

def caseid_report100_5(self):
    module_other_app.get_datachecklist("Report100_5")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.fuel_dump_report_check_detail(self, "Report100_5", eventname, result, "0", var_app.info_vehicle_name4, var_app.info_vehicle_name_4,
                                                    var_app.info_vehicle_detail4, var_app.info_vehicle_detail_4,
                                               "Trạng thái", "_BaoCaoDoHutNhienLieu_XemChiTiet_TrangThai.png")

def caseid_report100_6(self):
    module_other_app.get_datachecklist("Report100_6")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.fuel_dump_report_check_detail(self, "Report100_6", eventname, result, "0", var_app.info_vehicle_name5, var_app.info_vehicle_name_5,
                                                    var_app.info_vehicle_detail5, var_app.info_vehicle_detail_5,
                                               "Số lít", "_BaoCaoDoHutNhienLieu_XemChiTiet_SoLit.png")

def caseid_report100_7(self):
    module_other_app.get_datachecklist("Report100_7")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.fuel_dump_report_check_detail(self, "Report100_7", eventname, result, "0", var_app.info_vehicle_name6, var_app.info_vehicle_name_6,
                                                    var_app.info_vehicle_detail6, var_app.info_vehicle_detail_6,
                                               "Địa chỉ", "_BaoCaoDoHutNhienLieu_XemChiTiet_DiaChi.png")


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
        homepage_app.move_module2(self, "Report102", eventname, result, var_app.engine_report, 0.8, 0.65, 0.2, 0.65, 1000,
                                                        "Trang chủ - Báo cáo động cơ", var_app.check_engine_report,
                                                         "BÁO CÁO ĐỘNG CƠ", "_TrangChu_BaoCaoDongCo.png")
    except:
        report_app.general.report_back(self)
        homepage_app.move_module2(self, "Report102", eventname, result, var_app.engine_report, 0.8, 0.65, 0.2, 0.65, 1000,
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
                                              var_app.STT, "Trang chủ - Báo cáo động cơ", "_TrangChu_BaoCaoDongCo_HomNay.png")

def caseid_report105(self):
    module_other_app.get_datachecklist("Report105")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.engine_report_type(self, "Report105", eventname, result, var_app.report_7day,
                                              var_app.STT, "Trang chủ - Báo cáo động cơ", "_TrangChu_BaoCaoDongCo_7Ngay.png")

def caseid_report106(self):
    module_other_app.get_datachecklist("Report106")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.engine_report_type(self, "Report106", eventname, result, var_app.report_15day,
                                              var_app.STT, "Trang chủ - Báo cáo động cơ", "_TrangChu_BaoCaoDongCo_15Ngay.png")

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
    report_app.report.engine_report_detail(self, "Report111", eventname, result, var_app.report_detail1, var_app.report_detail_1, 0, 13,
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
        homepage_app.move_module(self, "Report113", eventname, result, var_app.detail_vehicle_fuel_chart, 0.8, 0.65, 0.2, 0.65, 1000,
                                                        "Trang chủ - Biểu đồ nhiên liệu", var_app.check_detail_vehicle_fuel_chart,
                                                         "BIỂU ĐỒ NHIÊN LIỆU", "_TrangChu_BieuDoNhienLieu.png")
    except:
        report_app.general.report_back(self)
        homepage_app.move_module(self, "Report113", eventname, result, var_app.detail_vehicle_fuel_chart, 0.8, 0.65, 0.2, 0.65, 1000,
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

def caseid_report115_1(self):
    module_other_app.get_datachecklist("Report115_1")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.fuel_chart_check_info(self, "Report115_1", eventname, result, var_app.fuel_chart_km1, "_BieuDoNhienLieu_KmTichLuyTuDauNgay.png")

def caseid_report115_2(self):
    module_other_app.get_datachecklist("Report115_2")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.fuel_chart_check_info(self, "Report115_2", eventname, result, var_app.fuel_chart_binh, "_BieuDoNhienLieu_Binh1.png")

def caseid_report115_3(self):
    module_other_app.get_datachecklist("Report115_3")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.fuel_chart_check_info(self, "Report115_3", eventname, result, var_app.fuel_chart_summary, "_BieuDoNhienLieu_Tong.png")

def caseid_report115_4(self):
    module_other_app.get_datachecklist("Report115_4")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.fuel_chart_check_info(self, "Report115_4", eventname, result, var_app.fuel_chart_time, "_BieuDoNhienLieu_ThoiGian.png")

def caseid_report115_5(self):
    module_other_app.get_datachecklist("Report115_5")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.fuel_chart_check_info(self, "Report115_5", eventname, result, var_app.fuel_chart_speed, "_BieuDoNhienLieu_VanToc.png")

def caseid_report115_6(self):
    module_other_app.get_datachecklist("Report115_6")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.fuel_chart_check_info(self, "Report115_6", eventname, result, var_app.fuel_chart_km2, "_BieuDoNhienLieu_Km2.png")

def caseid_report115_7(self):
    module_other_app.get_datachecklist("Report115_7")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.fuel_chart_check_info(self, "Report115_7", eventname, result, var_app.fuel_chart_engine, "_BieuDoNhienLieu_DongCo.png")

def caseid_report115_8(self):
    module_other_app.get_datachecklist("Report115_8")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.fuel_chart_check_info(self, "Report115_8", eventname, result, var_app.fuel_chart_address, "_BieuDoNhienLieu_DiaChi.png")

















def caseid_report116(self):
    module_other_app.get_datachecklist("Report116")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    try:
        homepage_app.move_module(self, "Report116", eventname, result, var_app.fuel_consumption_report, 0.8, 0.65, 0.2, 0.65, 1000,
                                                        "Trang chủ - Báo cáo tiêu hao nhiên liệu", var_app.check_fuel_consumption_report,
                                                         "BÁO CÁO TIÊU HAO NHIÊN LIỆU", "_TrangChu_BaoCaoTieuHaoNhienLieu.png")
    except:
        report_app.general.report_back(self)
        homepage_app.move_module(self, "Report116", eventname, result, var_app.fuel_consumption_report, 0.8, 0.65, 0.2, 0.65, 1000,
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
                                              var_app.STT, "Trang chủ - Báo cáo tiêu hao nhiên liệu", "_TrangChu_BaoCaoTieuHaoNhienLieu_HomNay.png")

def caseid_report119(self):
    module_other_app.get_datachecklist("Report119")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.fuel_consumption_report_type(self, "Report119", eventname, result, var_app.report_7day,
                                              var_app.STT, "Trang chủ - Báo cáo tiêu hao nhiên liệu", "_TrangChu_BaoCaoTieuHaoNhienLieu_7Ngay.png")

def caseid_report120(self):
    module_other_app.get_datachecklist("Report120")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.fuel_consumption_report_type(self, "Report120", eventname, result, var_app.report_15day,
                                              var_app.STT, "Trang chủ - Báo cáo tiêu hao nhiên liệu", "_TrangChu_BaoCaoTieuHaoNhienLieu_15Ngay.png")

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
    report_app.report.fuel_consumption_report_detail(self, "Report125", eventname, result, var_app.report_detail1, var_app.report_detail_1, 0, 15,
                                         "Tổng số Km GPS:", "_TrangChu_BaoCaoTieuHaoNhienLieu_TongSoKmGps.png")

def caseid_report126(self):
    module_other_app.get_datachecklist("Report126")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.fuel_consumption_report_detail(self, "Report126", eventname, result, var_app.report_detail2, var_app.report_detail_2, 0, 30,
                                         "Tổng thời gian bật máy (phút):", "_TrangChu_BaoCaoTieuHaoNhienLieu_TongThoiGianBatMay.png")

def caseid_report127(self):
    module_other_app.get_datachecklist("Report127")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.fuel_consumption_report_detail(self, "Report127", eventname, result, var_app.report_detail3, var_app.report_detail_3, 0, 37,
                                         "Tổng thời gian dừng đỗ nổ máy (phút):", "_TrangChu_BaoCaoTieuHaoNhienLieu_TongThoiGianDungDoNoMay.png")

def caseid_report128(self):
    module_other_app.get_datachecklist("Report128")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.fuel_consumption_report_detail(self, "Report128", eventname, result, var_app.report_detail4, var_app.report_detail_4, 0, 21,
                                         "Tổng số lít tiêu hao:", "_TrangChu_BaoCaoTieuHaoNhienLieu_TongSoLitTieuHao.png")


def caseid_report129(self):
    module_other_app.get_datachecklist("Report129")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.fuel_consumption_report_detail(self, "Report129", eventname, result, var_app.report_detail5, var_app.report_detail_5, 0, 21,
                                         "Tổng số lít đầu ngày:", "_TrangChu_BaoCaoTieuHaoNhienLieu_TongSoLitDauNgay.png")

def caseid_report130(self):
    module_other_app.get_datachecklist("Report130")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.fuel_consumption_report_detail(self, "Report130", eventname, result, var_app.report_detail6, var_app.report_detail_6, 0, 16,
                                         "Tổng số lít tồn:", "_TrangChu_BaoCaoTieuHaoNhienLieu_TongSoLitTont.png")

def caseid_report131(self):
    module_other_app.get_datachecklist("Report131")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.fuel_consumption_report_detail(self, "Report131", eventname, result, var_app.report_detail7, var_app.report_detail_7, 0, 16,
                                         "Tổng số lít hút:", "_TrangChu_BaoCaoTieuHaoNhienLieu_TongSoLitHut.png")

def caseid_report132(self):
    module_other_app.get_datachecklist("Report132")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.fuel_consumption_report_detail(self, "Report132", eventname, result, var_app.report_detail8, var_app.report_detail_8, 0, 15,
                                         "Tổng số lít đổ:", "_TrangChu_BaoCaoTieuHaoNhienLieu_TongSoLitDo.png")



def caseid_report133(self):
    module_other_app.get_datachecklist("Report133")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.fuel_consumption_report_detail(self, "Report133", eventname, result, var_app.report_detail9, var_app.report_detail_9, 0, 16,
                                         "Tổng số lần hút:", "_TrangChu_BaoCaoTieuHaoNhienLieu_TongSoLitHut.png")

def caseid_report134(self):
    module_other_app.get_datachecklist("Report134")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.fuel_consumption_report_detail(self, "Report134", eventname, result, var_app.report_detail10, var_app.report_detail_10, 0, 15,
                                         "Tổng số lần đổ:", "_TrangChu_BaoCaoTieuHaoNhienLieu_TongSoLanDo.png")

def caseid_report135(self):
    module_other_app.get_datachecklist("Report135")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.fuel_consumption_report_detail(self, "Report135", eventname, result, var_app.report_detail11, var_app.report_detail_11, 0, 25,
                                         "Định mức thực tế theo km:", "_TrangChu_BaoCaoTieuHaoNhienLieu_DinhMucThucTeTheoKm.png")

def caseid_report136(self):
    module_other_app.get_datachecklist("Report136")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.fuel_consumption_report_detail(self, "Report136", eventname, result, var_app.report_detail12, var_app.report_detail_12, 0, 30,
                                         "Định mức thực tế theo bật máy:", "_TrangChu_BaoCaoTieuHaoNhienLieu_DinhMucThucTeTheoBatMay.png")


def caseid_report136_1(self):
    module_other_app.get_datachecklist("Report136_1")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.fuel_consumption_report_see_detail(self, "Report136_1", eventname, result)

def caseid_report136_2(self):
    module_other_app.get_datachecklist("Report136_2")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.fuel_consumption_report_check_detail(self, "Report136_2", eventname, result, "0", var_app.info_vehicle_name1a, var_app.info_vehicle_name1b,
                                                           var_app.info_vehicle_detail1a,  var_app.info_vehicle_detail1b,
                                               "Biển số xe", "_BaoCaoTieuHaoNhienLieu_XemChiTiet_BienSoXe.png")

def caseid_report136_3(self):
    module_other_app.get_datachecklist("Report136_3")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.fuel_consumption_report_check_detail(self, "Report136_3", eventname, result, "0", var_app.info_vehicle_name2a, var_app.info_vehicle_name2b,
                                                           var_app.info_vehicle_detail2a,  var_app.info_vehicle_detail2b,
                                               "Ngày tháng", "_BaoCaoTieuHaoNhienLieu_XemChiTiet_NgayThang.png")

def caseid_report136_4(self):
    module_other_app.get_datachecklist("Report136_4")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.fuel_consumption_report_check_detail(self, "Report136_4", eventname, result, "0", var_app.info_vehicle_name3a, var_app.info_vehicle_name3b,
                                                           var_app.info_vehicle_detail3a,  var_app.info_vehicle_detail3b,
                                               "Giờ bắt đầu di chuyển", "_BaoCaoTieuHaoNhienLieu_XemChiTiet_GioBatDauDiChuyen.png")

def caseid_report136_5(self):
    module_other_app.get_datachecklist("Report136_5")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.fuel_consumption_report_check_detail(self, "Report136_5", eventname, result, "0", var_app.info_vehicle_name4a, var_app.info_vehicle_name4b,
                                                           var_app.info_vehicle_detail4a,  var_app.info_vehicle_detail4b,
                                               "Giờ kết thúc di chuyển", "_BaoCaoTieuHaoNhienLieu_XemChiTiet_GioKetThucDiChuyen.png")

def caseid_report136_6(self):
    module_other_app.get_datachecklist("Report136_6")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.fuel_consumption_report_check_detail(self, "Report136_6", eventname, result, "0", var_app.info_vehicle_name5a, var_app.info_vehicle_name5b,
                                                           var_app.info_vehicle_detail5a,  var_app.info_vehicle_detail5b,
                                               "Km (GPS)", "_BaoCaoTieuHaoNhienLieu_XemChiTiet_KmGps.png")

def caseid_report136_7(self):
    module_other_app.get_datachecklist("Report136_7")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.fuel_consumption_report_check_detail(self, "Report136_7", eventname, result, "0", var_app.info_vehicle_name6a, var_app.info_vehicle_name6b,
                                                           var_app.info_vehicle_detail6a,  var_app.info_vehicle_detail6b,
                                               "Thời gian bật máy (phút)", "_BaoCaoTieuHaoNhienLieu_XemChiTiet_ThoiGianBatMayPhut.png")

def caseid_report136_8(self):
    module_other_app.get_datachecklist("Report136_8")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.fuel_consumption_report_check_detail(self, "Report136_8", eventname, result, "0", var_app.info_vehicle_name7a, var_app.info_vehicle_name7b,
                                                           var_app.info_vehicle_detail7a,  var_app.info_vehicle_detail7b,
                                               "Thời gian lăn bánh (phút)", "_BaoCaoTieuHaoNhienLieu_XemChiTiet_ThoiGianLanBanhPhut.png")

def caseid_report136_9(self):
    module_other_app.get_datachecklist("Report136_9")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.fuel_consumption_report_check_detail(self, "Report136_9", eventname, result, "0", var_app.info_vehicle_name8a, var_app.info_vehicle_name8b,
                                                           var_app.info_vehicle_detail8a,  var_app.info_vehicle_detail8b,
                                               "Thời gian dừng đỗ nổ máy (phút)", "_BaoCaoTieuHaoNhienLieu_XemChiTiet_ThoiGianDungDoNoMayPhut.png")

def caseid_report136_10(self):
    module_other_app.get_datachecklist("Report136_10")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.fuel_consumption_report_check_detail(self, "Report136_10", eventname, result, "0", var_app.info_vehicle_name9a, var_app.info_vehicle_name9b,
                                                           var_app.info_vehicle_detail9a,  var_app.info_vehicle_detail9b,
                                               "Số lần đổ", "_BaoCaoTieuHaoNhienLieu_XemChiTiet_SoLanDo.png")

def caseid_report136_11(self):
    module_other_app.get_datachecklist("Report136_11")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.fuel_consumption_report_check_detail(self, "Report136_11", eventname, result, "0", var_app.info_vehicle_name10a, var_app.info_vehicle_name10b,
                                                           var_app.info_vehicle_detail10a,  var_app.info_vehicle_detail10b,
                                               "Số lần hút", "_BaoCaoTieuHaoNhienLieu_XemChiTiet_SoLanHut.png")

def caseid_report136_12(self):
    module_other_app.get_datachecklist("Report136_12")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.fuel_consumption_report_check_detail(self, "Report136_12", eventname, result, "0", var_app.info_vehicle_name11a, var_app.info_vehicle_name11b,
                                                           var_app.info_vehicle_detail11a,  var_app.info_vehicle_detail11b,
                                               "Số lít đổ", "_BaoCaoTieuHaoNhienLieu_XemChiTiet_SoLitDo.png")

def caseid_report136_13(self):
    module_other_app.get_datachecklist("Report136_13")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.fuel_consumption_report_check_detail(self, "Report136_13", eventname, result, "0", var_app.info_vehicle_name12a, var_app.info_vehicle_name12b,
                                                           var_app.info_vehicle_detail12a,  var_app.info_vehicle_detail12b,
                                               "Số lít hút", "_BaoCaoTieuHaoNhienLieu_XemChiTiet_SoLitHut.png")

def caseid_report136_14(self):
    module_other_app.get_datachecklist("Report136_14")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.fuel_consumption_report_check_detail(self, "Report136_14", eventname, result, "0", var_app.info_vehicle_name13a, var_app.info_vehicle_name13b,
                                                           var_app.info_vehicle_detail13a,  var_app.info_vehicle_detail13b,
                                               "Số lít đầu ngày", "_BaoCaoTieuHaoNhienLieu_XemChiTiet_SoLitDauNgay.png")

def caseid_report136_15(self):
    module_other_app.get_datachecklist("Report136_15")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.fuel_consumption_report_check_detail(self, "Report136_15", eventname, result, "0", var_app.info_vehicle_name14a, var_app.info_vehicle_name14b,
                                                           var_app.info_vehicle_detail14a,  var_app.info_vehicle_detail14b,
                                               "Số lít tồn", "_BaoCaoTieuHaoNhienLieu_XemChiTiet_SoLitTon.png")

def caseid_report136_16(self):
    module_other_app.get_datachecklist("Report136_16")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.fuel_consumption_report_check_detail(self, "Report136_16", eventname, result, "0", var_app.info_vehicle_name15a, var_app.info_vehicle_name15b,
                                                           var_app.info_vehicle_detail15a,  var_app.info_vehicle_detail15b,
                                               "Số lít tiêu hao", "_BaoCaoTieuHaoNhienLieu_XemChiTiet_SoLitTieuHao.png")

def caseid_report136_17(self):
    module_other_app.get_datachecklist("Report136_17")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.fuel_consumption_report_check_detail(self, "Report136_17", eventname, result, "0", var_app.info_vehicle_name16a, var_app.info_vehicle_name16b,
                                                           var_app.info_vehicle_detail16a,  var_app.info_vehicle_detail16b,
                                               "Định mức quy định", "_BaoCaoTieuHaoNhienLieu_XemChiTiet_DinhMucQuyDinh.png")


def caseid_report136_18(self):
    module_other_app.get_datachecklist("Report136_18")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.fuel_consumption_report_check_detail(self, "Report136_18", eventname, result, "0", var_app.info_vehicle_name17a, var_app.info_vehicle_name17b,
                                                           var_app.info_vehicle_detail17a,  var_app.info_vehicle_detail17b,
                                               "Định mức thực tế theo km", "_BaoCaoTieuHaoNhienLieu_XemChiTiet_DinhMucThucTeTheoKm.png")


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
        homepage_app.move_module(self, "Report138", eventname, result, var_app.Comprehensive_fuel_consumption_report, 0.8, 0.65, 0.2, 0.65, 1000,
                                                        "Trang chủ - Báo cáo tổng hợp tiêu hao nhiên liệu", var_app.check_Comprehensive_fuel_consumption_report,
                                                         "BÁO CÁO TỔNG HỢP TIÊU HAO NHIÊN LIỆU", "_TrangChu_BaoCaoTongHopTieuHaoNhienLieu.png")
    except:
        report_app.general.report_back(self)
        homepage_app.move_module(self, "Report138", eventname, result, var_app.Comprehensive_fuel_consumption_report, 0.8, 0.65, 0.2, 0.65, 1000,
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
                                              var_app.STT, "Trang chủ - Báo cáo tổng hợp tiêu hao nhiên liệu", "_TrangChu_BaoCaoTongHopTieuHaoNhienLieu_HomNay.png")

def caseid_report141(self):
    module_other_app.get_datachecklist("Report141")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.Comprehensive_fuel_consumption_report_type(self, "Report141", eventname, result, var_app.report_7day,
                                              var_app.STT, "Trang chủ - Báo cáo tổng hợp tiêu hao nhiên liệu", "_TrangChu_BaoCaoTongHopTieuHaoNhienLieu_7Ngay.png")

def caseid_report142(self):
    module_other_app.get_datachecklist("Report142")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.Comprehensive_fuel_consumption_report_type(self, "Report142", eventname, result, var_app.report_15day,
                                              var_app.STT, "Trang chủ - Báo cáo tổng hợp tiêu hao nhiên liệu", "_TrangChu_BaoCaoTongHopTieuHaoNhienLieu_15Ngay.png")

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
    report_app.report.Comprehensive_fuel_consumption_report_detail(self, "Report147", eventname, result, var_app.report_detail1, var_app.report_detail_1, 0, 15,
                                         "Tổng số Km GPS:", "_TrangChu_BaoCaoTongHopTieuHaoNhienLieu_TongSoKmGps.png")

def caseid_report148(self):
    module_other_app.get_datachecklist("Report148")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.Comprehensive_fuel_consumption_report_detail(self, "Report148", eventname, result, var_app.report_detail2, var_app.report_detail_2, 0, 30,
                                         "Tổng thời gian bật máy (phút):", "_TrangChu_BaoCaoTongHopTieuHaoNhienLieu_TongThoiGianBatMay.png")

def caseid_report149(self):
    module_other_app.get_datachecklist("Report149")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.Comprehensive_fuel_consumption_report_detail(self, "Report149", eventname, result, var_app.report_detail3, var_app.report_detail_3, 0, 37,
                                         "Tổng thời gian dừng đỗ nổ máy (phút):", "_TrangChu_BaoCaoTongHopTieuHaoNhienLieu_TongThoiGianDungDoNoMay.png")

def caseid_report150(self):
    module_other_app.get_datachecklist("Report150")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.Comprehensive_fuel_consumption_report_detail(self, "Report150", eventname, result, var_app.report_detail4, var_app.report_detail_4, 0, 21,
                                         "Tổng số lít tiêu hao:", "_TrangChu_BaoCaoTongHopTieuHaoNhienLieu_TongSoLitTieuHao.png")


def caseid_report151(self):
    module_other_app.get_datachecklist("Report151")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.Comprehensive_fuel_consumption_report_detail(self, "Report151", eventname, result, var_app.report_detail5, var_app.report_detail_5, 0, 21,
                                         "Tổng số lít đầu ngày:", "_TrangChu_BaoCaoTongHopTieuHaoNhienLieu_TongSoLitDauNgay.png")


def caseid_report152(self):
    module_other_app.get_datachecklist("Report152")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.Comprehensive_fuel_consumption_report_detail(self, "Report152", eventname, result, var_app.report_detail6, var_app.report_detail_6, 0, 16,
                                         "Tổng số lít tồn:", "_TrangChu_BaoCaoTongHopTieuHaoNhienLieu_TongSoLitTon.png")

def caseid_report153(self):
    module_other_app.get_datachecklist("Report153")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.Comprehensive_fuel_consumption_report_detail(self, "Report153", eventname, result, var_app.report_detail7, var_app.report_detail_7, 0, 16,
                                         "Tổng số lít hút:", "_TrangChu_BaoCaoTongHopTieuHaoNhienLieu_TongSoLitHut.png")

def caseid_report154(self):
    module_other_app.get_datachecklist("Report154")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.Comprehensive_fuel_consumption_report_detail(self, "Report154", eventname, result, var_app.report_detail8, var_app.report_detail_8, 0, 15,
                                         "Tổng số lít đổ:", "_TrangChu_BaoCaoTongHopTieuHaoNhienLieu_TongSoLitDo.png")



def caseid_report155(self):
    module_other_app.get_datachecklist("Report155")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.Comprehensive_fuel_consumption_report_detail(self, "Report155", eventname, result, var_app.report_detail9, var_app.report_detail_9, 0, 16,
                                         "Tổng số lần hút:", "_TrangChu_BaoCaoTongHopTieuHaoNhienLieu_TongSoLanHut.png")

def caseid_report156(self):
    module_other_app.get_datachecklist("Report156")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.Comprehensive_fuel_consumption_report_detail(self, "Report156", eventname, result, var_app.report_detail10, var_app.report_detail_10, 0, 15,
                                         "Tổng số lần đổ:", "_TrangChu_BaoCaoTongHopTieuHaoNhienLieu_TongSoLanDo.png")

def caseid_report157(self):
    module_other_app.get_datachecklist("Report157")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.Comprehensive_fuel_consumption_report_detail(self, "Report157", eventname, result, var_app.report_detail11, var_app.report_detail_11, 0, 25,
                                         "Định mức thực tế theo km:", "_TrangChu_BaoCaoTongHopTieuHaoNhienLieu_DinhMucThucTeTheoKm.png")



def caseid_report158(self):
    module_other_app.get_datachecklist("Report158")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.Comprehensive_fuel_consumption_report_detail(self, "Report158", eventname, result, var_app.report_detail12, var_app.report_detail_12, 0, 30,
                                         "Định mức thực tế theo bật máy:", "_TrangChu_BaoCaoTongHopTieuHaoNhienLieu_DinhMucThucTeTheoBatMay.png")


def caseid_report158_1(self):
    module_other_app.get_datachecklist("Report158_1")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.Comprehensive_fuel_consumption_report_see_detail(self, "Report158_1", eventname, result)

def caseid_report158_2(self):
    module_other_app.get_datachecklist("Report158_2")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.Comprehensive_fuel_consumption_report_check_detail(self, "Report158_2", eventname, result, "0", var_app.info_vehicle_name1a, var_app.info_vehicle_name1b,
                                                           var_app.info_vehicle_detail1a,  var_app.info_vehicle_detail1b,
                                               "Biển số xe", "_BaoCaoTongHopTieuHaoNhienLieu_XemChiTiet_BienSoXe.png")

def caseid_report158_3(self):
    module_other_app.get_datachecklist("Report158_3")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.Comprehensive_fuel_consumption_report_check_detail(self, "Report158_3", eventname, result, "0", var_app.info_vehicle_name2a, var_app.info_vehicle_name2b,
                                                           var_app.info_vehicle_detail2a,  var_app.info_vehicle_detail2b,
                                               "Giờ bắt đầu di chuyển", "_BaoCaoTongHopTieuHaoNhienLieu_XemChiTiet_GioBatDauDiChuyen.png")

def caseid_report158_4(self):
    module_other_app.get_datachecklist("Report158_4")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.Comprehensive_fuel_consumption_report_check_detail(self, "Report158_4", eventname, result, "0", var_app.info_vehicle_name3a, var_app.info_vehicle_name3b,
                                                           var_app.info_vehicle_detail3a,  var_app.info_vehicle_detail3b,
                                               "Giờ kết thúc di chuyển", "_BaoCaoTongHopTieuHaoNhienLieu_XemChiTiet_GioKetThucDiChuyen.png")

def caseid_report158_5(self):
    module_other_app.get_datachecklist("Report158_5")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.Comprehensive_fuel_consumption_report_check_detail(self, "Report158_5", eventname, result, "0", var_app.info_vehicle_name4a, var_app.info_vehicle_name4b,
                                                           var_app.info_vehicle_detail4a,  var_app.info_vehicle_detail4b,
                                               "Số lít đầu ngày", "_BaoCaoTongHopTieuHaoNhienLieu_XemChiTiet_SoLitDauNgay.png")

def caseid_report158_6(self):
    module_other_app.get_datachecklist("Report158_6")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.Comprehensive_fuel_consumption_report_check_detail(self, "Report158_6", eventname, result, "0", var_app.info_vehicle_name5a, var_app.info_vehicle_name5b,
                                                           var_app.info_vehicle_detail5a,  var_app.info_vehicle_detail5b,
                                               "Số lít đổ", "_BaoCaoTongHopTieuHaoNhienLieu_XemChiTiet_SoLitDo.png")

def caseid_report158_7(self):
    module_other_app.get_datachecklist("Report158_7")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.Comprehensive_fuel_consumption_report_check_detail(self, "Report158_7", eventname, result, "0", var_app.info_vehicle_name6a, var_app.info_vehicle_name6b,
                                                           var_app.info_vehicle_detail6a,  var_app.info_vehicle_detail6b,
                                               "Số lít hút", "_BaoCaoTongHopTieuHaoNhienLieu_XemChiTiet_SoLitHut.png")

def caseid_report158_8(self):
    module_other_app.get_datachecklist("Report158_8")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.Comprehensive_fuel_consumption_report_check_detail(self, "Report158_8", eventname, result, "0", var_app.info_vehicle_name7a, var_app.info_vehicle_name7b,
                                                           var_app.info_vehicle_detail7a,  var_app.info_vehicle_detail7b,
                                               "Số lít tồn", "_BaoCaoTongHopTieuHaoNhienLieu_XemChiTiet_SoLitTon.png")

def caseid_report158_9(self):
    module_other_app.get_datachecklist("Report158_9")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.Comprehensive_fuel_consumption_report_check_detail(self, "Report158_9", eventname, result, "0", var_app.info_vehicle_name8a, var_app.info_vehicle_name8b,
                                                           var_app.info_vehicle_detail8a,  var_app.info_vehicle_detail8b,
                                               "Số lần đổ", "_BaoCaoTongHopTieuHaoNhienLieu_XemChiTiet_SoLanDo.png")

def caseid_report158_10(self):
    module_other_app.get_datachecklist("Report158_10")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.Comprehensive_fuel_consumption_report_check_detail(self, "Report158_10", eventname, result, "0", var_app.info_vehicle_name9a, var_app.info_vehicle_name9b,
                                                           var_app.info_vehicle_detail9a,  var_app.info_vehicle_detail9b,
                                               "Số lần hút", "_BaoCaoTongHopTieuHaoNhienLieu_XemChiTiet_SoLanHut.png")

def caseid_report158_11(self):
    module_other_app.get_datachecklist("Report158_11")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.Comprehensive_fuel_consumption_report_check_detail(self, "Report158_11", eventname, result, "0", var_app.info_vehicle_name10a, var_app.info_vehicle_name10b,
                                                           var_app.info_vehicle_detail10a,  var_app.info_vehicle_detail10b,
                                               "Số lít tiêu hao", "_BaoCaoTongHopTieuHaoNhienLieu_XemChiTiet_SoLitTieuHao.png")

def caseid_report158_12(self):
    module_other_app.get_datachecklist("Report158_12")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.Comprehensive_fuel_consumption_report_check_detail(self, "Report158_12", eventname, result, "0", var_app.info_vehicle_name11a, var_app.info_vehicle_name11b,
                                                           var_app.info_vehicle_detail11a,  var_app.info_vehicle_detail11b,
                                               "Km (GPS)", "_BaoCaoTongHopTieuHaoNhienLieu_XemChiTiet_KmGps.png")

def caseid_report158_13(self):
    module_other_app.get_datachecklist("Report158_13")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.Comprehensive_fuel_consumption_report_check_detail(self, "Report158_13", eventname, result, "0", var_app.info_vehicle_name12a, var_app.info_vehicle_name12b,
                                                           var_app.info_vehicle_detail12a,  var_app.info_vehicle_detail12b,
                                               "Thời gian bật máy (phút)", "_BaoCaoTongHopTieuHaoNhienLieu_XemChiTiet_ThoiGianBatMayPhut.png")

def caseid_report158_14(self):
    module_other_app.get_datachecklist("Report158_14")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.Comprehensive_fuel_consumption_report_check_detail(self, "Report158_14", eventname, result, "0", var_app.info_vehicle_name13a, var_app.info_vehicle_name13b,
                                                           var_app.info_vehicle_detail13a,  var_app.info_vehicle_detail13b,
                                               "Thời gian lăn bánh (phút)", "_BaoCaoTongHopTieuHaoNhienLieu_XemChiTiet_ThoiGianLanBanhPhut.png")

def caseid_report158_15(self):
    module_other_app.get_datachecklist("Report158_15")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.Comprehensive_fuel_consumption_report_check_detail(self, "Report158_15", eventname, result, "0", var_app.info_vehicle_name14a, var_app.info_vehicle_name14b,
                                                           var_app.info_vehicle_detail14a,  var_app.info_vehicle_detail14b,
                                               "Thời gian dừng đỗ nổ máy (phút)", "_BaoCaoTongHopTieuHaoNhienLieu_XemChiTiet_ThoiGianDungDoNoMayPhut.png")

def caseid_report158_16(self):
    module_other_app.get_datachecklist("Report158_16")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.Comprehensive_fuel_consumption_report_check_detail(self, "Report158_16", eventname, result, "0", var_app.info_vehicle_name15a, var_app.info_vehicle_name15b,
                                                           var_app.info_vehicle_detail15a,  var_app.info_vehicle_detail15b,
                                               "Định mức quy định", "_BaoCaoTongHopTieuHaoNhienLieu_XemChiTiet_DinhMucQuyDinh.png")

def caseid_report158_17(self):
    module_other_app.get_datachecklist("Report158_17")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.Comprehensive_fuel_consumption_report_check_detail(self, "Report158_17", eventname, result, "0", var_app.info_vehicle_name16a, var_app.info_vehicle_name16b,
                                                           var_app.info_vehicle_detail16a,  var_app.info_vehicle_detail16b,
                                               "Định mức thực tế theo km", "_BaoCaoTongHopTieuHaoNhienLieu_XemChiTiet_DinhMucThucTeTheoKm.png")

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
        homepage_app.move_module(self, "Report160", eventname, result, var_app.vehicle_speed, 0.8, 0.65, 0.2, 0.65, 1000,
                                                        "Trang chủ - Tốc độ của xe", var_app.check_vehicle_speed,
                                                         "TỐC ĐỘ CỦA XE", "_TrangChu_TocDoCuaXe.png")
    except:
        report_app.general.report_back(self)
        homepage_app.move_module(self, "Report160", eventname, result, var_app.vehicle_speed, 0.8, 0.65, 0.2, 0.65, 1000,
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
                                              var_app.STT, "Trang chủ - Tốc độ của xe", "_TrangChu_TocDoCuaXe_HomNay.png")

def caseid_report163(self):
    module_other_app.get_datachecklist("Report163")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.vehicle_speed_type(self, "Report163", eventname, result, var_app.report_7day,
                                              var_app.STT, "Trang chủ - Tốc độ của xe", "_TrangChu_TocDoCuaXe_7Ngay.png")

def caseid_report164(self):
    module_other_app.get_datachecklist("Report164")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.vehicle_speed_type(self, "Report164", eventname, result, var_app.report_15day,
                                              var_app.STT, "Trang chủ - Tốc độ của xe", "_TrangChu_TocDoCuaXe_15Ngay.png")

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
    report_app.report.temperature_report(self, "Report170", eventname, result)


def caseid_report171(self):
    module_other_app.get_datachecklist("Report171")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.temperature_chart(self, "Report171", eventname, result)



def caseid_report172(self):
    module_other_app.get_datachecklist("Report172")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    try:
        homepage_app.move_module(self, "Report172", eventname, result, var_app.continuous_driving_detailed_reports, 0.8, 0.65, 0.2, 0.65, 1000,
                                                        "Trang chủ - Báo cáo chi tiết cuốc lái xe liên tục", var_app.check_continuous_driving_detailed_reports,
                                                         "BÁO CÁO CHI TIẾT CÁC CUỐC LÁI XE LIÊN TỤC", "_TrangChu_BaoCaoChiTietCacCuocLaiXeLienTuc.png")
    except:
        report_app.general.report_back(self)
        homepage_app.move_module(self, "Report172", eventname, result, var_app.continuous_driving_detailed_reports, 0.8, 0.65, 0.2, 0.65, 1000,
                                                        "Trang chủ - Báo cáo chi tiết cuốc lái xe liên tục", var_app.check_continuous_driving_detailed_reports,
                                                         "BÁO CÁO CHI TIẾT CÁC CUỐC LÁI XE LIÊN TỤC", "_TrangChu_BaoCaoChiTietCacCuocLaiXeLienTuc.png")


# def caseid_report173(self):
#     module_other_app.get_datachecklist("Report173")
#     eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
#     result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
#     report_app.report.continuous_driving_detailed_reports_filter(self, "Report173", eventname, result, "Lái xe", "Chọn lái xe", "_BaoCaoChiTietCacCuocLaiXeLienTuc_Filter_LaiXe.png")


def caseid_report173(self):
    module_other_app.get_datachecklist("Report173")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.continuous_driving_detailed_reports_filter1(self, "Report173", eventname, result)



def caseid_report174(self):
    module_other_app.get_datachecklist("Report174")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.continuous_driving_detailed_reports_drive_search(self, "Report174", eventname, result)

def caseid_report175(self):
    module_other_app.get_datachecklist("Report175")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.continuous_driving_detailed_reports_type(self, "Report175", eventname, result, var_app.report_today, "1",
                                                               "_BaoCaoChiTietCacCuocLaiXeLienTuc_LaiXe_HomNay.png")


def caseid_report176(self):
    module_other_app.get_datachecklist("Report176")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.continuous_driving_detailed_reports_type(self, "Report176", eventname, result, var_app.report_7day, "1",
                                                               "_BaoCaoChiTietCacCuocLaiXeLienTuc_LaiXe_7Ngay.png")


def caseid_report177(self):
    module_other_app.get_datachecklist("Report177")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.continuous_driving_detailed_reports_type(self, "Report177", eventname, result, var_app.report_15day, "1",
                                                               "_BaoCaoChiTietCacCuocLaiXeLienTuc_LaiXe_15Ngay.png")


def caseid_report178(self):
    module_other_app.get_datachecklist("Report178")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.continuous_driving_detailed_reports_type(self, "Report178", eventname, result, var_app.report_other, "0",
                                                               "_BaoCaoChiTietCacCuocLaiXeLienTuc_LaiXe_Khac.png")

def caseid_report179(self):
    module_other_app.get_datachecklist("Report179")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.continuous_driving_detailed_reports_setting(self, "Report179", eventname, result)


def caseid_report180(self):
    module_other_app.get_datachecklist("Report180")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.continuous_driving_detailed_reports_excel(self, "Report180", eventname, result)

def caseid_report181(self):
    module_other_app.get_datachecklist("Report181")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.continuous_driving_detailed_reports_report_detail(self, "Report181", eventname, result, var_app.report_detail1a, var_app.report_detail1b, 0, 17,
                                         "Họ và tên lái xe:", "_BaoCaoChiTietCacCuocLaiXeLienTu_HoVaTenLaiXe.png")

def caseid_report182(self):
    module_other_app.get_datachecklist("Report182")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.continuous_driving_detailed_reports_report_detail(self, "Report182", eventname, result, var_app.report_detail2a, var_app.report_detail2b, 0, 17,
                                         "Giấy phép lái xe:", "_BaoCaoChiTietCacCuocLaiXeLienTu_GiayPhepLaiXe.png")

def caseid_report183(self):
    module_other_app.get_datachecklist("Report183")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.continuous_driving_detailed_reports_report_detail(self, "Report183", eventname, result, var_app.report_detail3a, var_app.report_detail3b, 0, 25,
                                         "Tổng thời gian hoạt động:", "_BaoCaoChiTietCacCuocLaiXeLienTu_TongThoiGianHoatDong.png")

def caseid_report184(self):
    module_other_app.get_datachecklist("Report184")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.continuous_driving_detailed_reports_report_detail(self, "Report184", eventname, result, var_app.report_detail4a, var_app.report_detail4b, 0, 17,
                                         "Tổng quãng đường:", "_BaoCaoChiTietCacCuocLaiXeLienTu_TongQuangDuong.png")

def caseid_report185(self):
    module_other_app.get_datachecklist("Report185")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.continuous_driving_detailed_reports_report_detail(self, "Report185", eventname, result, var_app.report_detail5a_more, var_app.report_detail5b_more, 0, 11,
                                         "Tham chiếu:", "_BaoCaoChiTietCacCuocLaiXeLienTu_ThamChieu.png")


def caseid_report186(self):
    module_other_app.get_datachecklist("Report186")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.continuous_driving_detailed_reports_column(self, "Report186", eventname, result)





def caseid_report187(self):
    module_other_app.get_datachecklist("Report187")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    try:
        homepage_app.move_module(self, "Report187", eventname, result, var_app.driving_details_for_the_day, 0.8, 0.65, 0.2, 0.65, 1000,
                                                        "Trang chủ - Báo cáo chi tiết cuốc lái xe liên tục", var_app.check_driving_details_for_the_day,
                                                         "BÁO CÁO CHI TIẾT CÁC CUỐC LÁI XE THEO NGÀY", "_TrangChu_ChiTietCuocLaiXeTrongNgay.png")
    except:
        report_app.general.report_back(self)
        homepage_app.move_module(self, "Report187", eventname, result, var_app.driving_details_for_the_day, 0.8, 0.65, 0.2, 0.65, 1000,
                                                        "Trang chủ - Báo cáo chi tiết cuốc lái xe liên tục", var_app.check_driving_details_for_the_day,
                                                         "BÁO CÁO CHI TIẾT CÁC CUỐC LÁI XE THEO NGÀY", "_TrangChu_ChiTietCuocLaiXeTrongNgay.png")


def caseid_report188(self):
    module_other_app.get_datachecklist("Report188")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.driving_details_for_the_day_filter(self, "Report188", eventname, result)


def caseid_report189(self):
    module_other_app.get_datachecklist("Report189")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.driving_details_for_the_day_search(self, "Report189", eventname, result)


def caseid_report190(self):
    module_other_app.get_datachecklist("Report190")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.driving_details_for_the_day_type(self, "Report190", eventname, result, var_app.report_today, "2",
                                                               "_ChiTietCuocLaiXeTrongNgay_HomNay.png")


def caseid_report191(self):
    module_other_app.get_datachecklist("Report191")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.driving_details_for_the_day_type(self, "Report191", eventname, result, var_app.report_7day, "1",
                                                               "_ChiTietCuocLaiXeTrongNgay_7Ngay.png")


def caseid_report192(self):
    module_other_app.get_datachecklist("Report192")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.driving_details_for_the_day_type(self, "Report192", eventname, result, var_app.report_15day, "1",
                                                               "_ChiTietCuocLaiXeTrongNgay_15Ngay.png")


def caseid_report193(self):
    module_other_app.get_datachecklist("Report193")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.driving_details_for_the_day_type(self, "Report193", eventname, result, var_app.report_other, "0",
                                                               "_ChiTietCuocLaiXeTrongNgay_Khac.png")


def caseid_report194(self):
    module_other_app.get_datachecklist("Report194")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.driving_details_for_the_day_setting(self, "Report194", eventname, result)


def caseid_report195(self):
    module_other_app.get_datachecklist("Report195")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.driving_details_for_the_day_excel(self, "Report195", eventname, result)


def caseid_report196(self):
    module_other_app.get_datachecklist("Report196")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.driving_details_for_the_day_detail(self, "Report196", eventname, result, var_app.report_detail1c, var_app.report_detail1d, 0, 17,
                                         "Họ và tên lái xe:", "_ChiTietCuocLaiXeTrongNgay_BienKiemSoat.png")

def caseid_report197(self):
    module_other_app.get_datachecklist("Report197")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.driving_details_for_the_day_detail(self, "Report197", eventname, result, var_app.report_detail2c, var_app.report_detail2d, 0, 17,
                                         "Giấy phép lái xe:", "_ChiTietCuocLaiXeTrongNgay_TongThoiGianHoatDong.png")

def caseid_report198(self):
    module_other_app.get_datachecklist("Report198")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.driving_details_for_the_day_detail(self, "Report198", eventname, result, var_app.report_detail3c_more, var_app.report_detail3d_more, 0, 25,
                                         "Tổng thời gian hoạt động:", "_ChiTietCuocLaiXeTrongNgay_TongQuangDuong.png")


def caseid_report198_1(self):
    module_other_app.get_datachecklist("Report198_1")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.driving_details_for_the_day_detail(self, "Report198_1", eventname, result, var_app.report_detail3c, var_app.report_detail3d, 0, 18,
                                         "Thời gian còn lại:", "_ChiTietCuocLaiXeTrongNgay_TongQuangDuong.png")

def caseid_report199(self):
    module_other_app.get_datachecklist("Report199")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.driving_details_for_the_day_detail(self, "Report199", eventname, result, var_app.report_detail5c_more, var_app.report_detail5d_more, 0, 11,
                                         "Tham chiếu:", "_ChiTietCuocLaiXeTrongNgay_ThamChieu.png")

def caseid_report200(self):
    module_other_app.get_datachecklist("Report200")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.driving_details_for_the_day_column(self, "Report200", eventname, result)


def caseid_report201(self):
    module_other_app.get_datachecklist("Report201")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    try:
        homepage_app.move_module(self, "Report201", eventname, result, var_app.driving_report_for_the_week, 0.8, 0.65, 0.2, 0.65, 1000,
                                                        "Trang chủ - Báo cáo cuốc lái xe trong tuần", var_app.check_driving_report_for_the_week,
                                                         "BÁO CÁO CÁC CUỐC LÁI XE TRONG TUẦN", "_TrangChu_BaoCaoCacCuocLaiXeTrongTuan.png")

    except:
        report_app.general.report_back(self)
        homepage_app.move_module(self, "Report201", eventname, result, var_app.driving_report_for_the_week, 0.8, 0.65, 0.2, 0.65, 1000,
                                                        "Trang chủ - Báo cáo cuốc lái xe trong tuần", var_app.check_driving_report_for_the_week,
                                                         "BÁO CÁO CÁC CUỐC LÁI XE TRONG TUẦN", "_TrangChu_BaoCaoCacCuocLaiXeTrongTuan.png")

def caseid_report202(self):
    module_other_app.get_datachecklist("Report202")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.driving_report_for_the_week_search(self, "Report202", eventname, result)

def caseid_report203(self):
    module_other_app.get_datachecklist("Report203")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.driving_report_for_the_week_setting(self, "Report203", eventname, result)

def caseid_report204(self):
    module_other_app.get_datachecklist("Report204")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.driving_report_for_the_week_filter(self, "Report204", eventname, result)

def caseid_report205(self):
    module_other_app.get_datachecklist("Report205")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.driving_report_for_the_week_excel(self, "Report205", eventname, result)

def caseid_report206(self):
    module_other_app.get_datachecklist("Report206")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.driving_report_for_the_week_detail(self, "Report206", eventname, result, var_app.report_detail1a, var_app.report_detail1b, 0, 17,
                                         "Họ và tên lái xe:", "_BaoCaoCacCuocLaiXeTrongTuan_HoVaTenLaiXe.png")


def caseid_report207(self):
    module_other_app.get_datachecklist("Report207")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.driving_report_for_the_week_detail(self, "Report207", eventname, result, var_app.report_detail2a, var_app.report_detail2b, 0, 17,
                                         "Giấy phép lái xe:", "_BaoCaoCacCuocLaiXeTrongTuan_GiayPhepLaiXe.png")

def caseid_report208(self):
    module_other_app.get_datachecklist("Report208")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.driving_report_for_the_week_detail(self, "Report208", eventname, result, var_app.report_detail3a, var_app.report_detail3b, 0, 25,
                                         "Tổng thời gian hoạt động:", "_BaoCaoCacCuocLaiXeTrongTuan_TongThoiGianHoatDong.png")

def caseid_report209(self):
    module_other_app.get_datachecklist("Report209")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.driving_report_for_the_week_detail(self, "Report209", eventname, result, var_app.report_detail4a, var_app.report_detail4b, 0, 17,
                                         "Tổng quãng đường:", "_BaoCaoCacCuocLaiXeTrongTuan_TongQuangDuong.png")

def caseid_report210(self):
    module_other_app.get_datachecklist("Report210")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.driving_report_for_the_week_detail(self, "Report210", eventname, result, var_app.report_detail5a_more, var_app.report_detail5b_more, 0, 37,
                                         "Tuần được tính từ 00:00 Thứ hai - 23:", "_BaoCaoCacCuocLaiXeTrongTuan_GhiChu.png")

def caseid_report211(self):
    module_other_app.get_datachecklist("Report211")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.driving_report_for_the_week_column(self, "Report211", eventname, result)


def caseid_report212(self):
    module_other_app.get_datachecklist("Report212")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.summary_report_of_violations(self, "Report212", eventname, result)


def caseid_report213(self):
    module_other_app.get_datachecklist("Report213")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.summary_report_of_violations_search(self, "Report213", eventname, result)


def caseid_report214(self):
    module_other_app.get_datachecklist("Report214")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.summary_report_of_violations_type(self, "Report214", eventname, result, var_app.report_today, "1",
                                                               "_BaoCaoTongHopViPham_HomNay.png")


def caseid_report215(self):
    module_other_app.get_datachecklist("Report215")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.summary_report_of_violations_type(self, "Report215", eventname, result, var_app.report_7day, "1",
                                                               "_BaoCaoTongHopViPham_7Ngay.png")


def caseid_report216(self):
    module_other_app.get_datachecklist("Report216")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.summary_report_of_violations_type(self, "Report216", eventname, result, var_app.report_15day, "1",
                                                               "_BaoCaoTongHopViPham_15Ngay.png")


def caseid_report217(self):
    module_other_app.get_datachecklist("Report217")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.summary_report_of_violations_type(self, "Report217", eventname, result, var_app.report_other, "0",
                                                               "_BaoCaoTongHopViPham_Khac.png")


def caseid_report218(self):
    module_other_app.get_datachecklist("Report218")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.summary_report_of_violations_setting(self, "Report218", eventname, result)


def caseid_report219(self):
    module_other_app.get_datachecklist("Report219")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.summary_report_of_violations_filter(self, "Report219", eventname, result)


def caseid_report220(self):
    module_other_app.get_datachecklist("Report220")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.summary_report_of_violations_excel(self, "Report220", eventname, result)


def caseid_report221(self):
    module_other_app.get_datachecklist("Report221")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.summary_report_of_violations_detail(self, "Report221", eventname, result, var_app.report_detail1e, var_app.report_detail1f, 0, 17,
                                         "Họ và tên lái xe:", "_BaoCaoTongHopViPham_HoVaTenLaiXe.png")

def caseid_report222(self):
    module_other_app.get_datachecklist("Report222")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.summary_report_of_violations_detail(self, "Report222", eventname, result, var_app.report_detail2e, var_app.report_detail2f, 0, 17,
                                         "Giấy phép lái xe:", "_BaoCaoTongHopViPham_GiayPhepLaiXe.png")


def caseid_report223(self):
    module_other_app.get_datachecklist("Report223")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.summary_report_of_violations_detail(self, "Report223", eventname, result, var_app.report_detail3e_more, var_app.report_detail3f_more, 0, 36,
                                         "Tham chiếu: Phụ lục 71/2024/TT - BCA", "_BaoCaoTongHopViPham_ThamChieu.png")


def caseid_report224(self):
    module_other_app.get_datachecklist("Report224")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.summary_report_of_violations_see_detail(self, "Report224", eventname, result)


def caseid_report225(self):
    module_other_app.get_datachecklist("Report225")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.summary_report_of_violations_check_detail(self, "Report225", eventname, result, "0", var_app.info_vehicle_name1a, var_app.info_vehicle_name1b,
                                                           var_app.info_vehicle_detail1a,  var_app.info_vehicle_detail1b, "Tổng km", "_BaoCaoTongHopViPham_XemChiTiet_TongKm.png")

def caseid_report226(self):
    module_other_app.get_datachecklist("Report226")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.summary_report_of_violations_check_detail(self, "Report226", eventname, result, "0", var_app.info_vehicle_name2a, var_app.info_vehicle_name2b,
                                                           var_app.info_vehicle_detail2a,  var_app.info_vehicle_detail2b, "Tỷ lệ quá tốc độ 5 km/h - 10 km/h",
                                                                         "_BaoCaoTongHopViPham_XemChiTiet_TyLeQuaTocDo5_10.png")
def caseid_report227(self):
    module_other_app.get_datachecklist("Report227")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.summary_report_of_violations_check_detail(self, "Report227", eventname, result, "0", var_app.info_vehicle_name3a, var_app.info_vehicle_name3b,
                                                           var_app.info_vehicle_detail3a,  var_app.info_vehicle_detail3b, "Tỷ lệ quá tốc độ 10 km/h - 20 km/h",
                                                                         "_BaoCaoTongHopViPham_XemChiTiet_TyLeQuaTocDo10_20.png")

def caseid_report228(self):
    module_other_app.get_datachecklist("Report228")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.summary_report_of_violations_check_detail(self, "Report228", eventname, result, "0", var_app.info_vehicle_name4a, var_app.info_vehicle_name4b,
                                                           var_app.info_vehicle_detail4a,  var_app.info_vehicle_detail4b, "Tỷ lệ quá tốc độ 20 km/h - 35 km/h",
                                                                         "_BaoCaoTongHopViPham_XemChiTiet_TyLeQuaTocDo20_35.png")

def caseid_report229(self):
    module_other_app.get_datachecklist("Report229")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.summary_report_of_violations_check_detail(self, "Report229", eventname, result, "0", var_app.info_vehicle_name5a, var_app.info_vehicle_name5b,
                                                           var_app.info_vehicle_detail5a,  var_app.info_vehicle_detail5b, "Tỷ lệ quá tốc độ trên 35 km/h",
                                                                         "_BaoCaoTongHopViPham_XemChiTiet_TyLeQuaTocDoTren35.png")

def caseid_report230(self):
    module_other_app.get_datachecklist("Report230")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.summary_report_of_violations_check_detail(self, "Report230", eventname, result, "0", var_app.info_vehicle_name6a, var_app.info_vehicle_name6b,
                                                           var_app.info_vehicle_detail6a,  var_app.info_vehicle_detail6b, "Số lần quá tốc độ 5 km/h - 10 km/h",
                                                                         "_BaoCaoTongHopViPham_XemChiTiet_SoLanQuaTocDo5_10.png")

def caseid_report231(self):
    module_other_app.get_datachecklist("Report231")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.summary_report_of_violations_check_detail(self, "Report231", eventname, result, "0", var_app.info_vehicle_name7a, var_app.info_vehicle_name7b,
                                                           var_app.info_vehicle_detail7a,  var_app.info_vehicle_detail7b, "Số lần quá tốc độ 10 km/h - 20 km/h",
                                                                         "_BaoCaoTongHopViPham_XemChiTiet_SoLanQuaTocDo10_20.png")

def caseid_report232(self):
    module_other_app.get_datachecklist("Report232")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.summary_report_of_violations_check_detail(self, "Report232", eventname, result, "0", var_app.info_vehicle_name8a, var_app.info_vehicle_name8b,
                                                           var_app.info_vehicle_detail8a,  var_app.info_vehicle_detail8b, "Số lần quá tốc độ 20 km/h - 35 km/h",
                                                                         "_BaoCaoTongHopViPham_XemChiTiet_SoLanQuaTocDo20_35.png")

def caseid_report233(self):
    module_other_app.get_datachecklist("Report233")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.summary_report_of_violations_check_detail(self, "Report233", eventname, result, "0", var_app.info_vehicle_name9a, var_app.info_vehicle_name9b,
                                                           var_app.info_vehicle_detail9a,  var_app.info_vehicle_detail9b, "Số lần quá tốc độ trên 35 km/h",
                                                                         "_BaoCaoTongHopViPham_XemChiTiet_SoLanQuaTocDoTren35.png")

def caseid_report234(self):
    module_other_app.get_datachecklist("Report234")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.summary_report_of_violations_check_detail(self, "Report234", eventname, result, "0", var_app.info_vehicle_name10a, var_app.info_vehicle_name10b,
                                                           var_app.info_vehicle_detail10a,  var_app.info_vehicle_detail10b, "Số lần lái xe liên tục quá 4 h/ngày",
                                                                         "_BaoCaoTongHopViPham_XemChiTiet_SoLanLaiXeLienTucQua4h.png")

def caseid_report235(self):
    module_other_app.get_datachecklist("Report235")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.summary_report_of_violations_check_detail(self, "Report235", eventname, result, "0", var_app.info_vehicle_name11a, var_app.info_vehicle_name11b,
                                                           var_app.info_vehicle_detail11a,  var_app.info_vehicle_detail11b, "Số lần lái xe quá 10 h/ngày",
                                                                         "_BaoCaoTongHopViPham_XemChiTiet_SoLanLaiXeQua10h.png")

def caseid_report236(self):
    module_other_app.get_datachecklist("Report236")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.summary_report_of_violations_check_detail(self, "Report236", eventname, result, "0", var_app.info_vehicle_name12a, var_app.info_vehicle_name12b,
                                                           var_app.info_vehicle_detail12a,  var_app.info_vehicle_detail12b, "Số lần lái xe quá 48 h/tuần",
                                                                         "_BaoCaoTongHopViPham_XemChiTiet_SoLanLaiXeQua48h.png")

def caseid_report237(self):
    module_other_app.get_datachecklist("Report237")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.summary_report_of_violations_column(self, "Report237", eventname, result)



def caseid_report238(self):
    module_other_app.get_datachecklist("Report238")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.report_over_speeding_on_the_route(self, "Report238", eventname, result)


def caseid_report239(self):
    module_other_app.get_datachecklist("Report239")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.report_over_speeding_on_the_route_search(self, "Report239", eventname, result)


def caseid_report240(self):
    module_other_app.get_datachecklist("Report240")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.report_over_speeding_on_the_route_type(self, "Report240", eventname, result, var_app.report_today, "1",
                                                               "_BaoCaoQuaTocDoTheoCungDuong_HomNay.png")


def caseid_report241(self):
    module_other_app.get_datachecklist("Report241")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.report_over_speeding_on_the_route_type(self, "Report241", eventname, result, var_app.report_7day, "1",
                                                               "_BaoCaoQuaTocDoTheoCungDuong_7Ngay.png")


def caseid_report242(self):
    module_other_app.get_datachecklist("Report242")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.report_over_speeding_on_the_route_type(self, "Report242", eventname, result, var_app.report_15day, "1",
                                                               "_BaoCaoQuaTocDoTheoCungDuong_15Ngay.png")


def caseid_report243(self):
    module_other_app.get_datachecklist("Report243")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.report_over_speeding_on_the_route_type(self, "Report243", eventname, result, var_app.report_other, "0",
                                                               "_BaoCaoQuaTocDoTheoCungDuong_Khac.png")


def caseid_report244(self):
    module_other_app.get_datachecklist("Report244")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.report_over_speeding_on_the_route_setting(self, "Report244", eventname, result)


def caseid_report245(self):
    module_other_app.get_datachecklist("Report245")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.report_over_speeding_on_the_route_excel(self, "Report245", eventname, result)


def caseid_report246(self):
    module_other_app.get_datachecklist("Report246")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.report_over_speeding_on_the_route_detail(self, "Report246", eventname, result, var_app.report_detail1, var_app.report_detail_1, 0, 15,
                                         "Tổng thời gian:", "_BaoCaoQuaTocDoTheoCungDuong_TongThoiGian.png")

def caseid_report247(self):
    module_other_app.get_datachecklist("Report247")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.report_over_speeding_on_the_route_detail(self, "Report247", eventname, result, var_app.report_detail2, var_app.report_detail_2, 0, 22,
                                         "Tổng quãng đường (km):", "_BaoCaoQuaTocDoTheoCungDuong_TongQuangDuongKm.png")


def caseid_report248(self):
    module_other_app.get_datachecklist("Report248")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.report_over_speeding_on_the_route_detail(self, "Report248", eventname, result, var_app.report_detail3, var_app.report_detail_3, 0, 12,
                                         "Tổng số lần:", "_BaoCaoQuaTocDoTheoCungDuong_TongSoLan.png")


def caseid_report249(self):
    module_other_app.get_datachecklist("Report249")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.report_over_speeding_on_the_route_detail(self, "Report249", eventname, result, var_app.report_detail4, var_app.report_detail_4, 0, 31,
                                         "Tốc độ cực đại lớn nhất (km/h):", "_BaoCaoQuaTocDoTheoCungDuong_TocDoCucDaiLonNhat.png")


def caseid_report250(self):
    module_other_app.get_datachecklist("Report250")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    report_app.report.report_over_speeding_on_the_route_column(self, "Report250", eventname, result)














def caseid_utilities01(self):
    module_other_app.get_datachecklist("Utilities01")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    try:
        utilities.move_module1(self, "Utilities01", eventname, result, var_app.list_vehicle, 0.8, 0.85, 0.2, 0.85, 1000,
                                                        "Trang chủ - Danh sách phương tiện", var_app.check_list_vehicle,
                                                         "Phương tiện", "_TrangChu_DanhSachPhuongTien.png")
    except:
        utilities.move_module1(self, "Utilities01", eventname, result, var_app.list_vehicle, 0.8, 0.85, 0.2, 0.85, 1000,
                                                        "Trang chủ - Danh sách phương tiện", var_app.check_list_vehicle,
                                                         "Phương tiện", "_TrangChu_DanhSachPhuongTien.png")


def caseid_utilities02(self):
    module_other_app.get_datachecklist("Utilities02")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    try:
        utilities.move_module1(self, "Utilities02", eventname, result, var_app.hide_and_show_the_car, 0.8, 0.85, 0.2, 0.85, 1000,
                                                        "Trang chủ - Ẩn hiện xe", var_app.check_hide_and_show_the_car,
                                                         "DANH SÁCH XE ĐANG ẨN", "_TrangChu_AnHienXe.png")
    except:
        utilities.move_module1(self, "Utilities02", eventname, result, var_app.hide_and_show_the_car, 0.8, 0.85, 0.2, 0.85, 1000,
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
        utilities.move_module1(self, "Utilities10", eventname, result, var_app.add_driver, 0.8, 0.85, 0.2, 0.85, 1000,
                                                        "Trang chủ - Thêm lái xe", var_app.check_add_driver,
                                                         "THÔNG TIN LÁI XE", "_TrangChu_ThemLaiXe.png")
    except:
        utilities.move_module1(self, "Utilities10", eventname, result, var_app.add_driver, 0.8, 0.85, 0.2, 0.85, 1000,
                                                        "Trang chủ - Thêm lái xe", var_app.check_add_driver,
                                                         "THÔNG TIN LÁI XE", "_TrangChu_ThemLaiXe.png")


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
        utilities.move_module1(self, "Utilities12", eventname, result, var_app.list_driver, 0.8, 0.85, 0.2, 0.85, 1000,
                                                        "Trang chủ - Danh sách phương tiện", var_app.check_list_driver,
                                                         "DANH SÁCH LÁI XE", "_TrangChu_DanhSachPhuongTien.png")
    except:
        utilities.move_module1(self, "Utilities12", eventname, result, var_app.list_driver, 0.8, 0.85, 0.2, 0.85, 1000,
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
    utilities.utilities.list_driver_check_info(self, "Utilities15", eventname, result, var_app.list_driver_check_info_type_liscense,
                                               "Chọn loại bằng lái", "_TrangChu_DanhSachPhuongTien_LoaiBangLai.png")


def caseid_utilities16(self):
    module_other_app.get_datachecklist("Utilities16")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    utilities.utilities.list_driver_check_info(self, "Utilities16", eventname, result, var_app.list_driver_check_info_expiration_date,
                                               "Chọn ngày hết hạn", "_TrangChu_DanhSachPhuongTien_NgayHetHan.png")

def caseid_utilities17(self):
    module_other_app.get_datachecklist("Utilities17")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    utilities.utilities.list_driver_check_info(self, "Utilities17", eventname, result, var_app.list_driver_check_info_phone_number,
                                               "Nhập số điện thoại", "_TrangChu_DanhSachPhuongTien_SoDienThoai.png")

def caseid_utilities18(self):
    module_other_app.get_datachecklist("Utilities18")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    utilities.utilities.list_driver_check_info(self, "Utilities18", eventname, result, var_app.list_driver_check_info_vehicle,
                                               "Chọn phương tiện", "_TrangChu_DanhSachPhuongTien_PhuongTien.png")
    utilities.general.utilities_back(self)


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
        utilities.move_module1(self, "Utilities20", eventname, result, var_app.info_fee, 0.8, 0.85, 0.2, 0.85, 1000,
                                                        "Trang chủ - Thông tin phí", var_app.check_info_fee,
                                                         "THÔNG TIN PHÍ", "_TrangChu_ThongTinPhi.png")
    except:
        utilities.move_module1(self, "Utilities20", eventname, result, var_app.info_fee, 0.8, 0.85, 0.2, 0.85, 1000,
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
        utilities.move_module1(self, "Utilities24", eventname, result, var_app.support_customer, 0.8, 0.85, 0.2, 0.85, 1000,
                                                        "Trang chủ - Hỗ trợ khách hàng", var_app.check_support_customer,
                                                         "HỖ TRỢ KHÁCH HÀNG", "_TrangChu_HoTroKhachHang.png")
    except:
        utilities.move_module1(self, "Utilities24", eventname, result, var_app.support_customer, 0.8, 0.85, 0.2, 0.85, 1000,
                                                        "Trang chủ - Hỗ trợ khách hàng", var_app.check_support_customer,
                                                         "HỖ TRỢ KHÁCH HÀNG", "_TrangChu_HoTroKhachHang.png")

def caseid_utilities25(self):
    module_other_app.get_datachecklist("Utilities25")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    utilities.utilities.support_customer_tab(self, "Utilities25", eventname, result, var_app.support,
                                             var_app.select_customer, "Chọn hỗ trợ",  "_TienIch_HoTroKhachHang_HoTro.png")

def caseid_utilities26(self):
    module_other_app.get_datachecklist("Utilities26")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    utilities.utilities.support_customer_tab(self, "Utilities26", eventname, result, var_app.utilities,
                                             var_app.clock_vehicle, "Khóa xe",  "_TienIch_HoTroKhachHang_TienIch.png")


def caseid_utilities26_1(self):
    module_other_app.get_datachecklist("Utilities26_1")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    utilities.utilities.support_customer_tab(self, "Utilities26_1", eventname, result, var_app.follow,
                                             var_app.follow_search, "Tìm kiếm phản hồi",  "_TienIch_HoTroKhachHang_TheoDoi.png")






def caseid_utilities27(self):
    module_other_app.get_datachecklist("Utilities27")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    try:
        utilities.move_module1(self, "Utilities27", eventname, result, var_app.transmission_bca, 0.8, 0.85, 0.2, 0.85, 1000,
                                                        "Trang chủ - Truyền dữ liệu BCA", var_app.check_transmission_bca,
                                                         "TRUYỀN DỮ LIỆU BCA", "_TrangChu_TruyenDuLieuBCA.png")
    except:
        utilities.move_module1(self, "Utilities27", eventname, result, var_app.transmission_report, 0.8, 0.85, 0.2, 0.85, 1000,
                                                        "Trang chủ - Truyền dữ liệu BCA", var_app.check_transmission_report,
                                                         "TRUYỀN DỮ LIỆU BCA", "_TrangChu_TruyenDuLieuBCA.png")

def caseid_utilities28(self):
    module_other_app.get_datachecklist("Utilities28")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    utilities.utilities.transmission_business(self, "Utilities28", eventname, result)


def caseid_utilities29(self):
    module_other_app.get_datachecklist("Utilities29")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    utilities.utilities.transmission_business_search(self, "Utilities29", eventname, result)

def caseid_utilities30(self):
    module_other_app.get_datachecklist("Utilities30")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    utilities.utilities.transmission_business_add_new(self, "Utilities30", eventname, result)


def caseid_utilities31(self):
    module_other_app.get_datachecklist("Utilities31")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    utilities.utilities.transmission_business_update(self, "Utilities31", eventname, result)


def caseid_utilities32(self):
    module_other_app.get_datachecklist("Utilities32")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    utilities.utilities.transmission_business_delete(self, "Utilities32", eventname, result)

def caseid_utilities33(self):
    module_other_app.get_datachecklist("Utilities33")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    utilities.utilities.transmission_drive(self, "Utilities33", eventname, result)

def caseid_utilities34(self):
    module_other_app.get_datachecklist("Utilities34")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    utilities.utilities.transmission_drive_search(self, "Utilities34", eventname, result)


def caseid_utilities35(self):
    module_other_app.get_datachecklist("Utilities35")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    utilities.utilities.transmission_drive_combobox(self, "Utilities35", eventname, result)


def caseid_utilities36(self):
    module_other_app.get_datachecklist("Utilities36")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    utilities.utilities.transmission_drive_add_new(self, "Utilities36", eventname, result)

def caseid_utilities37(self):
    module_other_app.get_datachecklist("Utilities37")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    utilities.utilities.transmission_drive_update(self, "Utilities37", eventname, result)


def caseid_utilities38(self):
    module_other_app.get_datachecklist("Utilities38")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    utilities.utilities.transmission_drive_delete(self, "Utilities38", eventname, result)

def caseid_utilities39(self):
    module_other_app.get_datachecklist("Utilities39")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    utilities.utilities.transmission_vehicle(self, "Utilities39", eventname, result)

def caseid_utilities40(self):
    module_other_app.get_datachecklist("Utilities40")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    utilities.utilities.transmission_vehicle_search(self, "Utilities40", eventname, result)

def caseid_utilities41(self):
    module_other_app.get_datachecklist("Utilities41")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    utilities.utilities.transmission_vehicle_combobox(self, "Utilities41", eventname, result)

def caseid_utilities42(self):
    module_other_app.get_datachecklist("Utilities42")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    utilities.utilities.transmission_vehicle_group(self, "Utilities42", eventname, result)

def caseid_utilities43(self):
    module_other_app.get_datachecklist("Utilities43")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    utilities.utilities.transmission_vehicle_add_new(self, "Utilities43", eventname, result)

def caseid_utilities44(self):
    module_other_app.get_datachecklist("Utilities44")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    utilities.utilities.transmission_vehicle_update(self, "Utilities44", eventname, result)

def caseid_utilities45(self):
    module_other_app.get_datachecklist("Utilities45")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    utilities.utilities.transmission_image(self, "Utilities45", eventname, result)

def caseid_utilities46(self):
    module_other_app.get_datachecklist("Utilities46")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    utilities.utilities.transmission_image_search(self, "Utilities46", eventname, result)

def caseid_utilities47(self):
    module_other_app.get_datachecklist("Utilities47")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    utilities.utilities.transmission_image_combobox(self, "Utilities47", eventname, result)

def caseid_utilities48(self):
    module_other_app.get_datachecklist("Utilities48")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    utilities.utilities.transmission_image_update(self, "Utilities48", eventname, result)

def caseid_utilities49(self):
    module_other_app.get_datachecklist("Utilities49")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    utilities.utilities.transmission_image_add_new(self, "Utilities49", eventname, result)


def caseid_utilities49_1(self):
    module_other_app.get_datachecklist("Utilities49_1")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    utilities.utilities.transmission_help(self, "Utilities49_1", eventname, result)


def caseid_utilities50(self):
    module_other_app.get_datachecklist("Utilities50")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    try:
        utilities.move_module1(self, "Utilities50", eventname, result, var_app.record_driver_card, 0.8, 0.85, 0.2, 0.85, 1000,
                                                        "Trang chủ - Ghi thẻ lái xe", var_app.check_record_driver_card,
                                                         "GHI THẺ LÁI XE", "_TrangChu_GhiTheLaiXe.png")
    except:
        utilities.move_module1(self, "Utilities50", eventname, result, var_app.record_driver_card, 0.8, 0.85, 0.2, 0.85, 1000,
                                                        "Trang chủ - Ghi thẻ lái xe", var_app.check_record_driver_card,
                                                         "GHI THẺ LÁI XE", "_TrangChu_GhiTheLaiXe.png")

def caseid_utilities51(self):
    module_other_app.get_datachecklist("Utilities51")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    utilities.utilities.record_driver_card_fill_info(self, "Utilities51", eventname, result)

def caseid_utilities52(self):
    module_other_app.get_datachecklist("Utilities52")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    utilities.utilities.record_driver_card_help(self, "Utilities52", eventname, result)
#
#
def caseid_utilities53(self):
    module_other_app.get_datachecklist("Utilities53")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    utilities.utilities.record_driver_card_icon(self, "Utilities53", eventname, result)


def caseid_utilities54(self):
    module_other_app.get_datachecklist("Utilities54")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    try:
        utilities.move_module1(self, "Utilities54", eventname, result, var_app.record_driver_card_nfc, 0.8, 0.85, 0.2, 0.85, 1000,
                                                        "Trang chủ - Ghi thẻ lái xe NFC", var_app.check_record_driver_card,
                                                         "GHI THẺ LÁI XE", "_TrangChu_GhiTheLaiXeNFC.png")
    except:
        utilities.move_module1(self, "Utilities54", eventname, result, var_app.record_driver_card_nfc, 0.8, 0.85, 0.2, 0.85, 1000,
                                                        "Trang chủ - Ghi thẻ lái xe NDC", var_app.check_record_driver_card,
                                                         "GHI THẺ LÁI XE", "_TrangChu_GhiTheLaiXeNFC.png")

def caseid_utilities55(self):
    module_other_app.get_datachecklist("Utilities55")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    utilities.utilities.record_driver_card_write_nfc(self, "Utilities55", eventname, result)


def caseid_utilities56(self):
    module_other_app.get_datachecklist("Utilities56")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    utilities.utilities.record_driver_card_read_nfc(self, "Utilities56", eventname, result)


def caseid_utilities57(self):
    module_other_app.get_datachecklist("Utilities57")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    utilities.utilities.record_driver_card_nfc_help(self, "Utilities57", eventname, result, var_app.nfc_icon_help1_1, var_app.nfc_icon_help1_2, var_app.help_write_card,
                                                    "Hướng dẫn ghi thẻ", "_TrangChu_GhiTheLaiXeNFC_HuongDan1.png")


def caseid_utilities58(self):
    module_other_app.get_datachecklist("Utilities58")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    utilities.utilities.record_driver_card_nfc_help(self, "Utilities58", eventname, result, var_app.nfc_icon_help2_1, var_app.nfc_icon_help2_2, var_app.help_read_card,
                                                    "Hướng dẫn đọc thẻ", "_TrangChu_GhiTheLaiXeNFC_HuongDan2.png")


def caseid_utilities59(self):
    module_other_app.get_datachecklist("Utilities59")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    utilities.utilities.record_driver_card_icon_history(self, "Utilities59", eventname, result)




def caseid_utilities60(self):
    module_other_app.get_datachecklist("Utilities60")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    try:
        utilities.move_module2(self, "Utilities60", eventname, result, var_app.contract_list, 0.8, 0.85, 0.2, 0.85, 1000,
                                                        "Trang chủ - Danh sách hợp đồng", var_app.check_contract_list,
                                                         "DANH SÁCH HỢP ĐỒNG", "_TrangChu_DanhSachHopDong.png", var_app.data['login']['binhanh_tk'], var_app.data['login']['binhanh_mk'])
    except:
        utilities.move_module2(self, "Utilities60", eventname, result, var_app.contract_list, 0.8, 0.85, 0.2, 0.85, 1000,
                                                        "Trang chủ - Danh sách hợp đồng", var_app.check_contract_list,
                                                         "DANH SÁCH HỢP ĐỒNG", "_TrangChu_DanhSachHopDong.png", var_app.data['login']['binhanh_tk'], var_app.data['login']['binhanh_mk'])


def caseid_utilities61(self):
    module_other_app.get_datachecklist("Utilities61")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    utilities.utilities.remote_control(self, "Utilities61", eventname, result)

def caseid_utilities62(self):
    module_other_app.get_datachecklist("Utilities62")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    utilities.utilities.fee_management(self, "Utilities62", eventname, result)


def caseid_utilities63(self):
    module_other_app.get_datachecklist("Utilities63")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    utilities.utilities.shipping_order(self, "Utilities63", eventname, result)


def caseid_utilities64(self):
    module_other_app.get_datachecklist("Utilities64")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    utilities.utilities.take_photos_of_delivery(self, "Utilities64", eventname, result)



def caseid_utilities65(self):
    module_other_app.get_datachecklist("Utilities65")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    try:
        utilities.move_module2(self, "Utilities65", eventname, result, var_app.warn_passengers, 0.8, 0.85, 0.2, 0.85, 1000,
                                                        "Trang chủ - Cảnh báo hành khách", var_app.check_warn_passengers,
                                                         "CẢNH BÁO HÀNH KHÁCH", "_TrangChu_CanhBaoHanhKhach.png", var_app.data['login']['test_canhbao_hanhkhach_tk'], var_app.data['login']['test_canhbao_hanhkhach_mk'])
    except:
        utilities.move_module2(self, "Utilities65", eventname, result, var_app.warn_passengers, 0.8, 0.85, 0.2, 0.85, 1000,
                                                        "Trang chủ - Cảnh báo hành khách", var_app.check_warn_passengers,
                                                         "CẢNH BÁO HÀNH KHÁCH", "_TrangChu_CanhBaoHanhKhach.png", var_app.data['login']['test_canhbao_hanhkhach_tk'], var_app.data['login']['test_canhbao_hanhkhach_mk'])


def caseid_utilities66(self):
    pass


def caseid_utilities67(self):
    module_other_app.get_datachecklist("Utilities67")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    utilities.utilities.warn_passengers_see_detail(self, "Utilities67", eventname, result)


def caseid_utilities68(self):
    module_other_app.get_datachecklist("Utilities68")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    utilities.utilities.warn_passengers_detail(self, "Utilities68", eventname, result,
                                                                  var_app.warn_passengers_detail_warm, "",
                                                                  "_TrangChu_CanhBaoHanhKhach_ClickVaoCanhBao_TenCanhBao.png")

def caseid_utilities69(self):
    module_other_app.get_datachecklist("Utilities69")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    utilities.utilities.warn_passengers_detail(self, "Utilities69", eventname, result,
                                                                  var_app.warn_passengers_detail_drive, "",
                                                                  "_TrangChu_CanhBaoHanhKhach_ClickVaoCanhBao_LaiXe.png")


def caseid_utilities70(self):
    module_other_app.get_datachecklist("Utilities70")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    utilities.utilities.warn_passengers_detail(self, "Utilities70", eventname, result,
                                                                  var_app.warn_passengers_detail_time, "",
                                                                  "_TrangChu_CanhBaoHanhKhach_ClickVaoCanhBao_ThoiGian.png")


def caseid_utilities71(self):
    module_other_app.get_datachecklist("Utilities71")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    utilities.utilities.warn_passengers_handle(self, "Utilities71", eventname, result)

def caseid_utilities72(self):
    module_other_app.get_datachecklist("Utilities72")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    utilities.utilities.warn_passengers_see_all(self, "Utilities72", eventname, result)



def caseid_utilities73(self):
    module_other_app.get_datachecklist("Utilities73")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    try:
        utilities.move_module1(self, "Utilities73", eventname, result, var_app.maintenance, 0.8, 0.85, 0.2, 0.85, 1000,
                                                        "Trang chủ - Bảo dưỡng", var_app.check_maintenance,
                                                         "DANH SÁCH BẢO DƯỠNG", "_TrangChu_BaoDuong.png")
    except:
        utilities.move_module1(self, "Utilities73", eventname, result, var_app.maintenance, 0.8, 0.85, 0.2, 0.85, 1000,
                                                        "Trang chủ - Bảo dưỡng", var_app.check_maintenance,
                                                         "DANH SÁCH BẢO DƯỠNG", "_TrangChu_BaoDuong.png")

def caseid_utilities74(self):
    module_other_app.get_datachecklist("Utilities74")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    utilities.utilities.maintenance_vehicle(self, "Utilities74", eventname, result)


def caseid_utilities75(self):
    module_other_app.get_datachecklist("Utilities75")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    utilities.utilities.maintenance_category(self, "Utilities75", eventname, result)

def caseid_utilities76(self):
    module_other_app.get_datachecklist("Utilities76")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    utilities.utilities.maintenance_status(self, "Utilities76", eventname, result)

def caseid_utilities77(self):
    module_other_app.get_datachecklist("Utilities77")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    utilities.utilities.maintenance_group(self, "Utilities77", eventname, result)

def caseid_utilities78(self):
    module_other_app.get_datachecklist("Utilities78")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    utilities.utilities.maintenance_fill_maintenance(self, "Utilities78", eventname, result)

def caseid_utilities79(self):
    module_other_app.get_datachecklist("Utilities79")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    utilities.utilities.maintenance_fill_maintenance_SELECT(self, "Utilities79", eventname, result)


def caseid_utilities80(self):
    module_other_app.get_datachecklist("Utilities80")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    utilities.utilities.maintenance_history(self, "Utilities80", eventname, result)


def caseid_utilities81(self):
    module_other_app.get_datachecklist("Utilities81")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    utilities.utilities.maintenance_history_vehicle(self, "Utilities81", eventname, result)


def caseid_utilities82(self):
    module_other_app.get_datachecklist("Utilities82")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    utilities.utilities.maintenance_history_category(self, "Utilities82", eventname, result)

def caseid_utilities83(self):
    module_other_app.get_datachecklist("Utilities83")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    utilities.utilities.maintenance_history_excel(self, "Utilities83", eventname, result)


def caseid_utilities84(self):
    module_other_app.get_datachecklist("Utilities84")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    utilities.utilities.maintenance_detail(self, "Utilities84", eventname, result)


def caseid_utilities85(self):
    module_other_app.get_datachecklist("Utilities85")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    utilities.utilities.maintenance_detail_category_check_info(self, "Utilities85", eventname, result)


def caseid_utilities86(self):
    module_other_app.get_datachecklist("Utilities86")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    utilities.utilities.maintenance_detail_category(self, "Utilities86", eventname, result)


def caseid_utilities87(self):
    module_other_app.get_datachecklist("Utilities87")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    utilities.utilities.maintenance_detail_status(self, "Utilities87", eventname, result)


def caseid_utilities88(self):
    module_other_app.get_datachecklist("Utilities88")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    utilities.utilities.maintenance_detail_icon_fill(self, "Utilities88", eventname, result)


def caseid_utilities89(self):
    module_other_app.get_datachecklist("Utilities89")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    utilities.utilities.timekeeping(self, "Utilities89", eventname, result)

def caseid_utilities90(self):
    module_other_app.get_datachecklist("Utilities90")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    utilities.utilities.timekeeping_compensatory(self, "Utilities90", eventname, result)


def caseid_utilities91(self):
    module_other_app.get_datachecklist("Utilities91")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    utilities.utilities.timekeeping_compensatory_confirm(self, "Utilities91", eventname, result)


def caseid_utilities92(self):
    module_other_app.get_datachecklist("Utilities92")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    utilities.utilities.check_timekeeping(self, "Utilities92", eventname, result)



def caseid_utilities93(self):
    module_other_app.get_datachecklist("Utilities93")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    utilities.utilities.timekeeping_start(self, "Utilities93", eventname, result)


def caseid_utilities94(self):
    module_other_app.get_datachecklist("Utilities94")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    utilities.utilities.check_timekeeping_start(self, "Utilities94", eventname, result)


def caseid_utilities95(self):
    module_other_app.get_datachecklist("Utilities95")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    utilities.utilities.timekeeping_end(self, "Utilities95", eventname, result)

def caseid_utilities96(self):
    module_other_app.get_datachecklist("Utilities96")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    utilities.utilities.history(self, "Utilities96", eventname, result)

def caseid_utilities97(self):
    module_other_app.get_datachecklist("Utilities97")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    utilities.utilities.history_calendar(self, "Utilities97", eventname, result)

def caseid_utilities98(self):
    module_other_app.get_datachecklist("Utilities98")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    utilities.utilities.history_vehicle(self, "Utilities98", eventname, result)

def caseid_utilities99(self):
    module_other_app.get_datachecklist("Utilities99")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    utilities.utilities.history_vehicle_other(self, "Utilities99", eventname, result,
                                              var_app.timekeeping_dark_blue, "_ChamCong_LichSu_SoLanChamCong.png")

def caseid_utilities100(self):
    module_other_app.get_datachecklist("Utilities100")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    utilities.utilities.history_vehicle_other(self, "Utilities100", eventname, result,
                                              var_app.timekeeping_orange, "_ChamCong_LichSu_SoLanChamCongBu.png")

def caseid_utilities101(self):
    module_other_app.get_datachecklist("Utilities101")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    utilities.utilities.history_vehicle_other(self, "Utilities101", eventname, result,
                                              var_app.timekeeping_time, "_ChamCong_LichSu_ThoiGian.png")

def caseid_utilities102(self):
    module_other_app.get_datachecklist("Utilities102")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    utilities.utilities.history_vehicle_other(self, "Utilities102", eventname, result,
                                              var_app.timekeeping_number_timekeeping, "_ChamCong_LichSu_SoLanCham.png")

def caseid_utilities103(self):
    module_other_app.get_datachecklist("Utilities103")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    utilities.utilities.history_vehicle_other(self, "Utilities103", eventname, result,
                                              var_app.timekeeping_compensatory_timekeeping, "_ChamCong_LichSu_ChamCongBu.png")

def caseid_utilities104(self):
    module_other_app.get_datachecklist("Utilities104")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    utilities.utilities.history_vehicle_other(self, "Utilities104", eventname, result,
                                              var_app.timekeeping_start_time1, "_ChamCong_LichSu_ThoiGianBatDau.png")


def caseid_utilities105(self):
    module_other_app.get_datachecklist("Utilities105")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    utilities.utilities.history_vehicle_other(self, "Utilities105", eventname, result,
                                              var_app.timekeeping_start_vehicle1, "_ChamCong_LichSu_PhuongTienBatDau.png")

def caseid_utilities106(self):
    module_other_app.get_datachecklist("Utilities106")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    utilities.utilities.history_vehicle_other(self, "Utilities106", eventname, result,
                                              var_app.timekeeping_start_location1, "_ChamCong_LichSu_ViTriBatDau.png")

def caseid_utilities107(self):
    module_other_app.get_datachecklist("Utilities107")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    utilities.utilities.history_vehicle_display(self, "Utilities107", eventname, result,
                                              var_app.timekeeping_start_image1, "_ChamCong_LichSu_HinhAnhBatDau.png")



def caseid_utilities108(self):
    module_other_app.get_datachecklist("Utilities108")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    utilities.utilities.history_vehicle_other(self, "Utilities108", eventname, result,
                                              var_app.timekeeping_start_time2, "_ChamCong_LichSu_ThoiGianKetthuc.png")


def caseid_utilities109(self):
    module_other_app.get_datachecklist("Utilities109")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    utilities.utilities.history_vehicle_other(self, "Utilities109", eventname, result,
                                              var_app.timekeeping_start_vehicle2, "_ChamCong_LichSu_PhuongTienKetThuc.png")

def caseid_utilities110(self):
    module_other_app.get_datachecklist("Utilities110")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    utilities.utilities.history_vehicle_other(self, "Utilities110", eventname, result,
                                              var_app.timekeeping_start_location2, "_ChamCong_LichSu_ViTriKetThuc.png")

def caseid_utilities111(self):
    module_other_app.get_datachecklist("Utilities111")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    utilities.utilities.history_vehicle_display(self, "Utilities111", eventname, result,
                                              var_app.timekeeping_start_image2, "_ChamCong_LichSu_HinhAnhKetThuc.png")


def caseid_utilities112(self):
    module_other_app.get_datachecklist("Utilities112")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    utilities.utilities.history_delete(self, "Utilities112", eventname, result)



def caseid_utilities113(self):
    module_other_app.get_datachecklist("Utilities113")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    try:
        utilities.move_module1(self, "Utilities113", eventname, result, var_app.minitor1, 0.8, 0.85, 0.2, 0.85, 1000,
                                                        "Trang chủ - Tiện ích - Giám sát", var_app.check_homepage_minitor,
                                                         "Phương tiện", "_TrangChu_GiamSat.png")
    except:
        utilities.move_module1(self, "Utilities113", eventname, result, var_app.minitor1, 0.8, 0.85, 0.2, 0.85, 1000,
                                                        "Trang chủ - Tiện ích - Giám sát", var_app.check_homepage_minitor,
                                                         "Phương tiện", "_TrangChu_GiamSat.png")


def caseid_utilities114(self):
    module_other_app.get_datachecklist("Utilities114")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    try:
        utilities.move_module1(self, "Utilities114", eventname, result, var_app.route1, 0.8, 0.85, 0.2, 0.85, 1000,
                                                        "Trang chủ - Tiện ích - Lộ trình", var_app.check_homepage_route,
                                                         "Lộ trình", "_TrangChu_LoTrinh.png")
    except:
        utilities.move_module1(self, "Utilities114", eventname, result, var_app.route1, 0.8, 0.85, 0.2, 0.85, 1000,
                                                        "Trang chủ - Tiện ích - Lộ trình", var_app.check_homepage_route,
                                                         "Lộ trình", "_TrangChu_LoTrinh.png")



def caseid_account01(self):
    module_other_app.get_datachecklist("Account01")
    eventname = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(module_other_app.readData(var_app.path_luutamthoi, 'Sheet1', 43, 2))
    account.account.check_version(self, "Account01", eventname, result)







