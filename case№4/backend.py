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
while True:
    end = begin + 10000
    json_parser_and_db_commiter(requester(object_id,begin,end))
    begin = end
    time.sleep(10)
