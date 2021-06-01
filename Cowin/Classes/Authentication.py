from Cowin.Config.ConfigKeys import ConfigKeys
from Cowin.Classes.Logger import Logger
import requests
import json
import hashlib
import datetime


class Auth():
    def __init__(self):
        self.log = Logger()

    def setHeaders(self, userAgent: str, contentType: str, accept: str,origin: str,referer: str):
        header = {"User-Agent": userAgent,
                  "Content-Type": contentType,
                  "accept": accept,
                  "origin": origin,
                 "referer": referer}
        return header

    def SendOtp(self, mobile_number: str, secret: str):
        request_url = ConfigKeys.url + ConfigKeys.get_opt_path
        send_OTP_request_body = {}

        self.log.Info("The Send OTP request URL is " + request_url)

        self.log.Info("Preparing body for SendOTP request.")
        send_OTP_request_body["mobile"] = mobile_number
        send_OTP_request_body["secret"] = secret

        self.log.Info("Preparing headers for SendOTP request.")
        header = self.setHeaders(ConfigKeys.UserAgentHeader,
                                 ConfigKeys.ContentTypeHeader,
                                 ConfigKeys.AcceptHeader,
                                 ConfigKeys.Origin,
                                 ConfigKeys.Referer)
        try:
            self.log.Info("Sending OTP")
            authentication_response = requests.post(url=request_url, json=send_OTP_request_body, headers=header)
            if authentication_response.ok:
                self.log.Info("OTP sent successfully on number " + str(mobile_number))
                authentication_response_body = json.loads(authentication_response.text)
                ConfigKeys.txnId = authentication_response_body["txnId"]
                ConfigKeys.otpSha256 = self.getOTPandConvertoSha265()
            else:
                self.log.Error("Error occurred in send OTP request." + str(authentication_response.status_code))
                exit()
        except Exception as ex:
            self.log.Error("Exception ocurred in SendOTP request." + str(ex))
            exit()

    def getOTPandConvertoSha265(self):
        otp = input("\n*****Enter OTP*****:-> \n")
        self.log.Info("Converting OTP to sha256")
        sha_signature = \
            hashlib.sha256(otp.encode()).hexdigest()
        return sha_signature

    def ValidateOTP(self, txnID: str, otpSha256: str):
        validate_otp_request_url = ConfigKeys.url + ConfigKeys.confirm_otp_path
        self.log.Info("The validate OTP request URL is " + validate_otp_request_url)

        self.log.Info("Preparing headers for validate OTP request.")
        header = self.setHeaders(ConfigKeys.UserAgentHeader,
                                 ConfigKeys.ContentTypeHeader,
                                 ConfigKeys.AcceptHeader,
                                 ConfigKeys.Origin,
                                 ConfigKeys.Referer)

        validate_otp_body = {"txnId": txnID, "otp": otpSha256}
        try:
            self.log.Info("Validating OTP.")
            otpValidationResponse = requests.post(url=validate_otp_request_url, json=validate_otp_body, headers=header)
            if otpValidationResponse.ok:
                self.log.Info("OTP has successfully been verified.")
                otpValidationResponseBody = json.loads(otpValidationResponse.text)
                self.log.Info("Extracting token for further requests.")
                ConfigKeys.token = otpValidationResponseBody["token"]
            else:
                self.log.Error("OTP validation was unsuccessful.")
                exit()
        except Exception as ex:
            self.log.Error("Exception occurred in otp validation ." + str(ex))
            exit()

    def getAndValidateCaptcha(self, token: str, captcha_file: str):

        request_url = ConfigKeys.url + ConfigKeys.get_captcha_path
        self.log.Info("The request URL to get captcha is " + request_url)

        self.log.Info("Preparing headers for get captcha request.")
        header = self.setHeaders(ConfigKeys.UserAgentHeader,
                                 ConfigKeys.ContentTypeHeader,
                                 ConfigKeys.AcceptHeader,
                                 ConfigKeys.Origin,
                                 ConfigKeys.Referer)
        header["Authorization"] = "Bearer " + token

        try:
            self.log.Info("Getting captcha")
            getCapthaResponse = requests.post(url=request_url, headers=header)
            if getCapthaResponse.ok:
                self.log.Info("Captcha received successfully.")
                getCapthaResponseBody = json.loads(getCapthaResponse.text)
                self.log.Info("Extracting string response of captcha file and saving it in ")
                ci = getCapthaResponseBody["captcha"]
                with open(captcha_file, 'w') as filetowrite:
                    filetowrite.write(ci.replace("\\", "")) #There are some escape sequences "\" that need to be removed.
                self.log.Info("Open "+ captcha_file+ " file (IN A BROWSER OR IN IDE) to read captcha text.")
                ConfigKeys.captcha_txt = input("\n*****Enter Captcha*****:-> \n")
            else:
                self.log.Error("Error occurred to get captcha.")
                exit()
        except Exception as ex:
            self.log.Error("Exception occurred to get captcha." + str(ex))
            exit()

    def scheduleAppt(self, token, center_id: str, session_id: str,
                     beneficiaries: list, slot: str, captcha: str, dose: int):
        schedule_appointment_url = ConfigKeys.url + ConfigKeys.schedule_appt_path
        self.log.Info("The request URL to schedule appointment  is " + schedule_appointment_url)

        self.log.Info("Preparing headers for schedule appointment request.")
        header = self.setHeaders(ConfigKeys.UserAgentHeader,
                                 ConfigKeys.ContentTypeHeader,
                                 ConfigKeys.AcceptHeader,
                                 ConfigKeys.Origin,
                                 ConfigKeys.Referer)
        header["Authorization"] = "Bearer " + token

        self.log.Info("Preparing body for schedule appointment request.")
        schedule_appointment_body = {"center_id": center_id, "session_id": session_id,
                "beneficiaries": beneficiaries, "slot": slot,
                "captcha": captcha, "dose": dose}
        try:
            self.log.Info("Scheduling appointment")
            schedule_appt_response = requests.post(url=schedule_appointment_url,
                                                   json=schedule_appointment_body, headers=header)
            if schedule_appt_response.ok:
                self.log.Info("CONGRATULATIONS!!! your appointment has successfully been booked.\n Following are the details:-")
                print("\t Center Name: "+ ConfigKeys.center_Name + "\t" \
                      "\t Center Address: "+ ConfigKeys.center_Address + "\t" \
                      "\t Date of Appointment: "+ ConfigKeys.date_of_Appointment + "\t")
            else:
                self.log.Error("Error occurred to schedule appointment.")
                exit()
        except Exception as ex:
            self.log.Error("Exception occurred while scheduling appointment." + str(ex))
            exit()


    def getAvailability(self, pincodes: list, min_age_limit: int, dose_type: int, vaccine: str, check_for_days: int):
        is_Available = False
        get_availability_url = ConfigKeys.url + ConfigKeys.get_availability_by_pin_path
        self.log.Info("The request URL to schedule appointment  is " + get_availability_url)

        self.log.Info("Preparing headers for get availability request.")
        header = self.setHeaders(ConfigKeys.UserAgentHeader,
                                 ConfigKeys.ContentTypeHeader,
                                 ConfigKeys.AcceptHeader,
                                 ConfigKeys.Origin,
                                 ConfigKeys.Referer)
        base = datetime.datetime.today()
        date_list = [base + datetime.timedelta(days=x) for x in range(check_for_days)]
        date_str = [x.strftime("%d-%m-%Y") for x in date_list]
        for pincode in pincodes:
            for date in date_str:
                param = {"pincode": pincode, "date": date}
                self.log.Info("Checking availability for pincode "+ str(pincode)+ " on date "+ str(date))
                try:
                    response = requests.get(url=get_availability_url, params=param, headers=header)
                    if response.ok:
                        response_json = json.loads(response.text)
                        if response_json["centers"]:
                            for center in response_json["centers"]:
                                for session in center["sessions"]:
                                    if session["min_age_limit"] <= min_age_limit:
                                        if session["vaccine"] == vaccine:
                                            if session["available_capacity_dose" + str(dose_type)] > 0:
                                                ConfigKeys.center_Id = center["center_id"]
                                                ConfigKeys.session_Id = session["session_id"]
                                                ConfigKeys.center_Name = center["name"]
                                                ConfigKeys.center_Address = center["address"]
                                                ConfigKeys.date_of_Appointment = str(format(date))
                                                is_Available = True
                                                return is_Available

                    else:
                        self.log.Error("Error occurred while checking availability for "+
                                       str(pincode)+ " on date "+ str(date))
                        return is_Available

                except Exception as ex:
                    self.log.Error("Exception occurred while checking appointment." + str(ex))
                    exit()
        return is_Available

