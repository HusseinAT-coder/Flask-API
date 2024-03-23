
from .models import Task
from flask import request, jsonify,abort
import uuid
from .. import db   
from datetime import datetime

#Get all tasks
def get_task_list():

    tasks = Task.query.filter_by(is_deleted=False).all()

    response = []
    for task in tasks: response.append(
        {
            "id":task.id,
            "title":task.title,
            "description":task.description,
            "category":task.category.name,
            "status":task.status.name,
        }
    )

    return jsonify(response)

def create_task():

    request_form = request.form.to_dict()

    id = str(uuid.uuid4()) # generate a random id
    new_task = Task(
                    id             = id,
                    title          = request_form['title'],
                    description    = request_form['description'],
                    category_id    = request_form['category_id']
                    )
    
    db.session.add(new_task)
    db.session.commit()

    ## return the created task
    created_task = Task.query.get(id)

    return jsonify({
        "id":created_task.id,
        "title":created_task.title,
        "description":created_task.description,
        "category_id":created_task.category_id,
        "status_id":created_task.status_id
    })

def get_task(task_id):

    task = Task.query.filter_by(is_deleted=False,id=task_id).first_or_404('Task not found')

    # Check if task is None
    # if task is None:
    #     # Raise a 404 Not Found error
    #     abort(404, "Task not found")

    response = {
        "id":task.id,
        "title":task.title,
        "description":task.description,
        "category_id":task.category_id,
        "status":task.status.name
    }

    return jsonify(response)

def update_task(task_id):

    ## get body data
    request_form = request.form.to_dict()

    # get db task
    task = Task.query.filter_by(is_deleted=False,id=task_id).first_or_404('Task not found')

    # Check if task is None
    # if task is None:
    #     # Raise a 404 Not Found error
    #     abort(404, "Task not found")

    # update fields
    task.title        = request_form['title']
    task.description     = request_form['description']
    task.category_id     = request_form['category_id']

    # commit changes
    db.session.commit()

    # get the new version
    updated_task = Task.query.get(task_id)

    response = {
        "id":updated_task.id,
        "title":updated_task.title,
        "description":updated_task.description,
        "category_id":updated_task.category_id,
        "status_id":updated_task.status_id
    }

    return jsonify(response)

def delete_task(task_id):

    task = Task.query.get(task_id)

    # Check if task is None
    if task is None:
        # Raise a 404 Not Found error
        abort(404, "Task not found")
    
    # if found then delete
    # Task.query.filter_by(id=task_id).delete()
        
    # using soft delete
    task.is_deleted = True
    task.deleted = datetime.now()
    
    db.session.commit()

    return jsonify(success=True)

def update_task_status(task_id):

    # get body data
    request_form = request.form.to_dict()

    task = Task.query.filter_by(is_deleted=False,id=task_id).first_or_404('Task not found')

    # Check if task is None
    # if task is None:
    #     # Raise a 404 Not Found error
    #     abort(404, "Task not found")

    # check if status found : TODO

    # then update
    task.status_id = request_form['status_id']

    # commit changes
    db.session.commit()

    return jsonify(success=True)