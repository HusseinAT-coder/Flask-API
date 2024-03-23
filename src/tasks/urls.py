
from ..app import app
from .controllers import get_task_list,create_task,get_task,update_task,delete_task,update_task_status

@app.route("/tasks")
def get_list():
    return get_task_list()

@app.route("/tasks",methods = ['POST'])
def create():
    return create_task()

@app.route("/tasks/<task_id>")
def get_by_id(task_id):
    return get_task(task_id)

@app.route("/tasks/<task_id>",methods = ['PUT'])
def update(task_id):
    return update_task(task_id)

@app.route("/tasks/<task_id>",methods = ['DELETE'])
def delete(task_id):
    return delete_task(task_id)

@app.route("/tasks/status/<task_id>",methods = ['PATCH'])
def update_status(task_id):
    return update_task_status(task_id)