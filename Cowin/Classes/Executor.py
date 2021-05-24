from Cowin.Config.ConfigKeys import ConfigKeys
from Cowin.Classes.Authentication import Auth

class Executor():
    def __init__(self):
        self.auth = Auth()

    def SearchAndBookAppointmnet(self):
        if self.auth.getAvailability(ConfigKeys.pincode, ConfigKeys.min_age_limit, 1, "COVAXIN", 2):
            self.auth.SendOtp(ConfigKeys.mobile_number, ConfigKeys.secret)
            self.auth.ValidateOTP(ConfigKeys.txnId, ConfigKeys.otpSha256)
            self.auth.getAndValidateCaptcha(ConfigKeys.token, ConfigKeys.capcha_file)
            self.auth.scheduleAppt(ConfigKeys.token, ConfigKeys.center_Id, ConfigKeys.session_Id, ConfigKeys.beneficiaries,
                              ConfigKeys.slot, ConfigKeys.captcha_txt, 1)
        else:
            self.auth.log.Error("No center available for vaccination.")

exe = Executor()
exe.SearchAndBookAppointmnet()