
from tasks.models import TaskStatus,TaskCategory


task_status = [
    {
        id:1,
        name:'Planned',
    },
    {
        id:2,
        name:'In Process',
    },
    {
        id:3,
        name:'Done',
    },
]

task_categories = [
    {
        id:1,
        name:'Developed',
    },
    {
        id:2,
        name:'Business',
    }
]

def seed_task_status(self,db):

    to_be_seeded_status = []
    
    for stat in task_status:

        new_status = TaskStatus(
            id      = stat.id,
            name    = stat.name
            )
        
        to_be_seeded_status.append(new_status)

    db.session.add(to_be_seeded_status)
    db.session.commit()

def seed_task_category(self,db):

    to_be_seeded_category = []
    
    for cat in task_categories:

        new_category = TaskCategory(
            id      = cat.id,
            name    = cat.name
            )
        
        to_be_seeded_category.append(new_category)

    db.session.add(to_be_seeded_category)
    db.session.commit()