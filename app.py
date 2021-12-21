from flask import Flask, request
import utils

PATH_BASE_API = '/api/v1'

app = Flask(__name__)


@app.route('/')
def index():
    msg = utils.db_create_table()
    data = {
        "code": 200,
        "msg": "Online",
        "database": msg
    }
    return data




@app.route(f'{PATH_BASE_API}/task/create', methods=['POST', 'GET'])
def create_task():
    # Prioridad - tipo int: 1 para alto, 2 para media, 3 para baja
    if request.method == 'POST':
        data = request.json
        title = data['title']
        description = data['description']
        start_date = data['start_date']
        end_date = data['end_date']
        time = data['time']
        priority = data['priority']
        # Se envían los datos del json a la databse y retorna un mensaje 
        msg = utils.db_create_task(title, description, start_date, end_date, time, priority)
    elif request.method == 'GET':
        msg = 'Crea una nueva tarea'
    return {
        "code": 200,
        "msg": msg
    }











if __name__ == '__main__':
    app.run(debug = True)







