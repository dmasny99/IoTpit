import sqlite3
import time
import datetime
import numpy as np
import matplotlib
#matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
import sqlite3
conn = sqlite3.connect('health_data.db')
cur = conn.cursor()
cur.execute("SELECT * FROM health_monitor;")
res = cur.fetchall()
ar =np.array(res)
print(ar)
pulse = np.asarray(ar[:,1]).reshape(-1,1)
time = np.asarray(ar[:,4]).reshape(-1,1)

pulse = np.hstack((pulse,time))
"""
fmt = dates.DateFormatter('%H:%M:%S')

fig, ax = plt.subplots()
plt.plot(pulse[:,0])
plt.show()
"""