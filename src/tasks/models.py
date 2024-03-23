
from .. import db
from datetime import datetime

## sql datatype object
class Task(db.Model):

    id           = db.Column(db.String(50), primary_key=True, nullable=False, unique=True)               # primary key
    created      = db.Column(db.DateTime(timezone=True), default=datetime.now)                           # The Date of the Instance Creation
    updated      = db.Column(db.DateTime(timezone=True), default=datetime.now, onupdate=datetime.now)    # Date on every update
    ## creator_id   (add user Id that created this task)
    # modifier_id   (add user Id that updated this task)

    title        = db.Column(db.String(100), nullable=False)
    description  = db.Column(db.String(100))

    #relations
    status         = db.relationship("TaskStatus", back_populates="tasks")
    status_id      = db.Column(db.Integer, db.ForeignKey("task_status.id"),default = 1)

    category         = db.relationship("TaskCategory", back_populates="tasks")
    category_id      = db.Column(db.Integer, db.ForeignKey("task_category.id"))

    is_deleted     = db.Column(db.Boolean, default=False)  
    deleted        = db.Column(db.DateTime(timezone=True)) 
    # deleter_id (user id)


    ## we can add validations here


class TaskStatus(db.Model):

    __tablename__='task_status'

    id           = db.Column(db.Integer, primary_key=True, nullable=False, unique=True) 
    name         = db.Column(db.String(50), nullable=False, unique=True)

    # Relations:
    tasks        = db.relationship("Task", back_populates='status')


class TaskCategory(db.Model):

    __tablename__='task_category'

    id           = db.Column(db.Integer, primary_key=True, nullable=False, unique=True) 
    name         = db.Column(db.String(50), nullable=False, unique=True)

    # Relations:
    tasks        = db.relationship("Task", back_populates='category')