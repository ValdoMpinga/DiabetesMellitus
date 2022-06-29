from datetime import datetime,date
from apscheduler.schedulers.blocking import BlockingScheduler
from .diabetesModel import diabetesModelTrainer

def trainerScheculer():
   schedule = BlockingScheduler()
   schedule.add_job(diabetesModelTrainer, 'date', run_date=datetime(date.today().year, date.today().month, date.today().day + 1, 2, 30, 0))
   schedule.start()



