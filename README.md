# covid_registration
A simple project that helps to search and book vaccination slots by means of Public APIs.

# Technology Python 

The flow of the project is follwoing:- 
  - 👍 Update the values of config parameters in ConfigKeys.py files.
      - **mobile_number** :- It's a string parameter, enter your mobile number, registered with conwin portal
      - **secret** :- It's a string parameter. This specific key you need to get from cowin portal, it gets generated as a response of user authentication.
      - **beneficiaries** :- It's a list. Login to cowin portal and view your list of beneficiaries copy the reference id for eahc of the beneficiaries. 
      - **capcha_file** :- This can be any empty existing file.
      - **pincode** :- A list of strings
      - **min_age_limit** :- minimum age limit for which slots are required.
 
 Once values of these params are updated you may start the execution of the code from Executor.py file.
 
 - The code first check for available slots for the dates and pincode.
 - If any slots matches, it sends OTP on the mobile number
 - Enter the OTP on IDE's console
 - When asked for captcha open the file **capcha_file** either in IDE or in browser and provide the captcha.
 - 👍 you are good.

# Sample console logs
```2021-05-23 22:06:25: INFO: The request URL to schedule appointment  is https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin
2021-05-23 22:06:25: INFO: Preparing headers for get availability request.
2021-05-23 22:06:25: INFO: Checking availability for pincode 325202 on date 23-05-2021
2021-05-23 22:06:26: INFO: The Send OTP request URL is https://cdn-api.co-vin.in/api/v2/auth/generateMobileOTP
2021-05-23 22:06:26: INFO: Preparing body for SendOTP request.
2021-05-23 22:06:26: INFO: Preparing headers for SendOTP request.
2021-05-23 22:06:26: INFO: Sending OTP

**Enter OTP**:-> 
2021-05-23 22:06:27: INFO: OTP sent successfully on number 95****7009
284984
2021-05-23 22:06:39: INFO: Converting OTP to sha256
2021-05-23 22:06:39: INFO: The validate OTP request URL is https://cdn-api.co-vin.in/api/v2/auth/validateMobileOtp
2021-05-23 22:06:39: INFO: Preparing headers for validate OTP request.
2021-05-23 22:06:39: INFO: Validating OTP.
2021-05-23 22:06:40: INFO: OTP has successfully been verified.
2021-05-23 22:06:40: INFO: Extracting token for further requests.
2021-05-23 22:06:40: INFO: The request URL to get captcha is https://cdn-api.co-vin.in/api/v2/auth/getRecaptcha
2021-05-23 22:06:40: INFO: Preparing headers for get captcha request.
2021-05-23 22:06:40: INFO: Getting captcha
2021-05-23 22:06:42: INFO: Captcha received successfully.
2021-05-23 22:06:42: INFO: Extracting string response of captcha file and saving it in 
2021-05-23 22:06:42: INFO: Open /Users/nv733055/Box/pycharm/Cowin/Config/captcha.svg file (IN A BROWSER OR IN IDE) to read captcha text.

**Enter Captcha**:-> 
fWe3D
2021-05-23 22:06:56: INFO: The request URL to schedule appointment  is https://cdn-api.co-vin.in/api/v2/appointment/schedule
2021-05-23 22:06:56: INFO: Preparing headers for schedule appointment request.
2021-05-23 22:06:56: INFO: Preparing body for schedule appointment request.
2021-05-23 22:06:56: INFO: Scheduling appointment
	 Center Name: Anta Chc Covaxin		 Center Address: Anta Chc		 Date of Appointment: 23-05-2021	
2021-05-23 22:06:59: INFO: CONGRATULATIONS!!! your appointment has successfully been booked.
 Following are the details:-

Process finished with exit code 0
```
