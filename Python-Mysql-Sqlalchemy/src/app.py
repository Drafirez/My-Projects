# Importamos los módulos necesarios
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

# Configuracion la aplicación Flask
app = Flask(__name__)

# Configura la aplicación con MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:12345678@localhost:3307/flask_sqlalchemy'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Definiendo el modelo para la tabla en la base de datos
class Task(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(70), unique=True)
  description = db.Column(db.String(100))

  def __init__(self, title, description):
    self.title = title
    self.description = description

# Creaando las rutas de la API y las operaciones CRUD
# @app.route('/', methods=['GET'])
# def index():
#     return jsonify({'message': 'Welcome to my API'})
  
# Obteniendo todas las tareas
@app.route('/tasks', methods=['GET'])
def get_tasks():
  tasks = Task.query.all()
  result = []
  for task in tasks:
    result.append({
      'id' : task.id,
      'title' : task.title,
      'description' : task.description
    })
  return jsonify(result)

# Crear una nueva tarea
@app.route('/tasks', methods=['POST'])
def create_task():
  new_task = Task(title = request.json['title'], description = request.json['description'])
  db.session.add(new_task)
  db.session.commit()
  return jsonify({'message': 'Task Created Successfully'})

# Obtener una tarea por ID
@app.route('/tasks/<id>', methods=['GET'])
def get_task(id):
  task = Task.query.get(id)
  if task :
    return jsonify({
      'id': task.id,
      'title': task.title,
      'description': task.description
    })
  else:
    return jsonify({'message': task})

# Actualizar una tarea por ID
@app.route('/tasks/<id>', methods=['PUT'])
def update_task(id):
  task = Task.query.get(id)
  if task:
        task.title = request.json['title']
        task.description = request.json['description']
        db.session.commit()
        return jsonify({'mensaje': 'Task Updated Successfully'})
  else:
        return jsonify({'mensaje': 'Task Not Found'})

# Eliminar una tarea por ID
@app.route('/tasks/<id>', methods=['DELETE'])
def delete_task(id):
  task = Task.query.get(id)
  if task:
    db.session.delete(task)
    db.session.commit()
    return jsonify({'mensaje': 'Task Deleted Successfully'})
  else:
    return jsonify({'mensaje': 'Task Not Found'})

if __name__ == "__main__":
# Define tu modelo de Usuario aquí
    with app.app_context():
        db.create_all()
    app.run(debug=True)