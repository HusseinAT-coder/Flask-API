
from seeds.tasks.task_seeder import seed_task_category,seed_task_status

from . import db

def seed():

    seed_task_status(db)
    print('Seeding Task Status')

    seed_task_category(db)
    print('Seeding Task Category')