from celery import Celery
import pymongo
import time
app = Celery('tasks',broker="amqp://guest:guest@localhost:5672//", backend='db+postgresql://postgres:postgres@localhost/celerydemo')


client = pymongo.MongoClient("localhost",27017)
db = client.test

@app.task
def reverse(string):

    total_row = db.movie.count_documents({})
    if total_row>1:
        print('Greate then 10')
    else:
        print(f'Less then 10 {total_row}')
    time.sleep(1)
    return string[::-1]


app.conf.beat_schedule = {
    'add-every-10-seconds': {
        'task': 'tasks.reverse',
        'schedule': 10.0,
        'args':['Hii there']
    },
}


app.conf.timezone = 'UTC'
