from flask import Blueprint
from ..Controllers import user_controllers

app = Blueprint('user', __name__)


app.route('/')(user_controllers.landing)

app.route('/products')(user_controllers.products)

# Client
app.route('/signup', methods=['GET', 'POST'])(user_controllers.signup)
app.route('/login', methods=['GET', 'POST'])(user_controllers.login)

# Admin
app.route('/adminlogin', methods=['GET', 'POST'])(user_controllers.admin_login)
app.route('/adminsignup', methods=['GET', 'POST'])(user_controllers.admin_signup)


