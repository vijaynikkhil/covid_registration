class ConfigKeys():
    url = "https://cdn-api.co-vin.in/"
    get_opt_path = "api/v2/auth/generateMobileOTP"
    confirm_otp_path = "api/v2/auth/validateMobileOtp"
    get_captcha_path = "api/v2/auth/getRecaptcha"
    schedule_appt_path = "api/v2/appointment/schedule"
    get_availability_by_pin_path = "api/v2/appointment/sessions/public/calendarByPin"

    user_agent_header = ""

    pincode = ["325202"] # Enter pincode your choice
    min_age_limit = 45 # 18, or 45

    # Enter a 10 digit mobile number, registered on cowin portal.
    mobile_number = "****7009"

    # The secret you need to copy from web developer, when you login to cowin portal.
    secret = "U2FsdGVkX18Nla7q++hCUFJ2a7uaPKL99513HSKXUfiPcbSSnVw9jEtlJ5EaW3hWfd7pjYDID5GW0vjE598sOg=="

    # Login to cowin portal and view your list of beneficiaries copy the reference id for eahc of the beneficiaries.
    beneficiaries = ["73256337444812"]

    # These headers are used to make server to trust us that we are coming from browers.
    UserAgentHeader = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"
    ContentTypeHeader = "application/json"
    AcceptHeader = "application/json, text/plain, */*"
    Origin = "https://selfregistration.cowin.gov.in"
    Referer = "https://selfregistration.cowin.gov.in/"

    token=""
    captcha_txt=""

    # Enter the file path you want to save captcha
    capcha_file = "/Users/nv733055/Box/pycharm/Cowin/Config/captcha.svg"

    txnId = ""
    otpSha256 = ""

    center_Id = ""
    session_Id = ""
    center_Name = ""
    center_Address = ""
    date_of_Appointment = ""
    slot = "09:00AM-11:00AM"
