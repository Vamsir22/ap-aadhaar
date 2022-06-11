import requests

# cid = "584745269946"
# Captcha = "816147"

def request_fun(cid, Captcha= "816147"):
    payload = \
                          '''{
                               "uidNum":"%s",
                                "Captcha":"%s"
                             }''' % (cid,Captcha)

    response = requests.request('POST', "https://gramawardsachivalayam.ap.gov.in/GSWS/api/KYV/volunteerDetails", data=payload,
                                    headers={'content-type': 'application/json',
                                    'cache-control': 'no-cache'})
    return response