from apscheduler.schedulers.background import BackgroundScheduler
import warnings
from utils import *  
import time

warnings.filterwarnings('ignore')

def job():
    current_price, change_percentage = get_BGB().values()
    response = notion_update(str(current_price), str(change_percentage))
    
    if response.status_code == 200:
        print(f'price is set to {current_price} at {time.time()}')
    else:
        print(f'Something went wrong: {response.text}')

scheduler = BackgroundScheduler()
scheduler.add_job(job, 'interval', minutes=1)
scheduler.start()

print('BGB Tracking Started')

while True:
    time.sleep(1) 
