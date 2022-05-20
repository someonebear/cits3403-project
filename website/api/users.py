from app.api import api_bp

@api_bp.route("/users/<int:id>", methods=['GET'])
def get_user(id):
  pass

@api_bp.route("/users", methods=['GET'])
def get_users():
  pass

@api_bp.route("/users", methods=['POST'])
def create_user(id):
  pass

@api_bp.route("/users/<int:id>", methods=['PUT'])
def update_user(id):
  pass