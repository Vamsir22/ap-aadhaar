from flask import Flask, render_template, request
from req import *
import json

# url = 'https://gramawardsachivalayam.ap.gov.in/GSWS/api/KYV/volunteerDetails'
# req_params = {'uidNum': '584745269946', 'Captcha': '816147'}

# response = requests.post(url, req_params)

app =Flask(__name__)

@app.route('/')
def aadhaar():
    return render_template("index.html")

@app.route('/final',methods = ['POST', 'GET'])
def final():
    # try:
    if request.method == 'POST':
        final = request.form
        for key, value in final.items():
            response = request_fun(str(value))
            final = response.text
            # print(final)
            final = json.loads(final)
            # print(type(final))
    return render_template("response.html",final = final)
    # except Exception as e:
    #     print("exception: ", e)

app.run(debug=True)



