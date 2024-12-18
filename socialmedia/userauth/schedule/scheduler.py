from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from django.core.management import call_command
scheduler = None
def start():
    global scheduler
    if scheduler is None:
        scheduler = BackgroundScheduler()
        scheduler.add_job(
            lambda: call_command('generate_talent_of_the_month'),
            trigger=CronTrigger(day='last', hour=23, minute=59),
            #trigger=CronTrigger(minute='*/1'),
            id='generate_talent_of_the_month',
            max_instances=1,
            replace_existing=True,
        )
        scheduler.start()
        print("Scheduler started...")
    else:
        print("Scheduler already running...")