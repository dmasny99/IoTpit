import time
import requests
import json
import sqlite3
token_RIC = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiI2MDdkMzIwYWYwM2U0NjAwMTFiMmRhNWUiLCJzdWIiOiI2MDQ5MGVjOTUzMDcyZWZjNGJmZDIyNjgiLCJncnAiOiI2MDQ5MGVjOTUzMDcyZWZjNGJmZDIyNjciLCJsaWMiOmZhbHNlLCJ1c2ciOiJhcGkiLCJmdWxsIjpmYWxzZSwicmlnaHRzIjoxLjUsImlhdCI6MTYxODgxNzU0NiwiZXhwIjoxNjIxMzcxNjAwfQ.MN77XEwaN7wrzkE0ZrYL-0LbsBqaQjMHpzYhxHVdUaY"
object_id = "607de42bf03e460011b2ee2c"
conn = sqlite3.connect('health_data.db')
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS health_monitor(
   id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
   pulse INTEGER,
   blood_pressure INTEGER,
   saturation INTEGER,
   time INTEGER);""")
conn.commit()
def make_url(id,begin,end):
    url = "https://sandbox.rightech.io/api/v1/objects/{}/packets?begin={}&end={}".format(id,begin,end)
    return url

def requester(id,begin,end):
    headers = {'Content-type': 'application/json', 'Authorization': 'Bearer {}'.format(token_RIC)}
    response = requests.get(make_url(id,begin,end),headers = headers)
    return response.json()

test = [{'_id': '607de6d833a13710001228b0', '_mid': '607ddb5ef03e460011b2edac', '_oid': '607de42bf03e460011b2ee2c', 'id': 'mqtt-iprofi_254187039-z6m7gb', '_ts': 1618863832684149, 'pulse': 62.242076486536,'blood_pressure': 130.3409483135, '_bot': True, 'online': True, 'time': 1618863832684, 'payload': '99.85637799691858', 'topic': 'health/saturation', '_gid': '60490ec953072efc4bfd2267', 'saturation': 99.856377996919}, {'_id': '607de6de33a13710001229df', '_mid': '607ddb5ef03e460011b2edac', '_oid': '607de42bf03e460011b2ee2c', 'id': 'mqtt-iprofi_254187039-z6m7gb', '_ts': 1618863838192791, 'pulse': 93.758714958794, 'blood_pressure': 130.3409483135, 'saturation': 99.856377996919, 'online': True, 'time': 1618863838192, '_bot': True, 'topic': 'health/pulse', '_gid': '60490ec953072efc4bfd2267', 'payload': '93.75871495879426'}]  
def json_parser_and_db_commiter(data):
    try:
        for i in range(len(data)):
            parsed_string = data[i]
            pulse = round(parsed_string["pulse"])
            blood_pressure = round(parsed_string["blood_pressure"])
            saturation = round(parsed_string["saturation"])
            time = round(parsed_string["time"]/1000)
            cur.execute("INSERT INTO health_monitor(pulse, blood_pressure,saturation,time) VALUES({},{},{},{});".format(pulse,blood_pressure,saturation,time))
            conn.commit()
    except KeyError:
        print("Can't find a key. Data won't be commited to the db.")
begin = round(time.time()*1000)-5000
json_parser_and_db_commiter(test)

while True:
    end = begin + 10000
    json_parser_and_db_commiter(requester(object_id,begin,end))
    begin = end
    time.sleep(20)
