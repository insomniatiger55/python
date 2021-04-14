import faust
from faker import Faker
import json
import time
from dataClass import userINFO

from datetime import datetime
faker=Faker()

def get_user():
    return {
        "timestamp":time.strftime('%X'),
        "name":faker.name(),
        "address":faker.address(),
        "created_at":faker.year()
    }
topic='user_info'
app = faust.App('add_Resident', broker='kafka://localhost:9092', store='memory://')

user_topic = app.topic(topic,value_type=userINFO)

@app.agent(user_topic)
async def show_user(users):
    async for user in users:
        print(f'Order detail is : {user.name}\n Address is: {user.address}')
        
@app.timer(interval=2.0)
async def send_user(app):
    await user_topic.send(value=get_user())
    
if __name__ == '__main__':
    app.main()    