from flask import Blueprint
from ..Controllers import user_controllers

app = Blueprint('user', __name__)

app.route('/signup', methods=['GET', 'POST'])(user_controllers.signup)
app.route('/')(user_controllers.landing)
app.route('/services')(user_controllers.services)
app.route('/login', methods=['GET', 'POST'])(user_controllers.login)
app.route('/adminlogin', methods=['GET', 'POST'])(user_controllers.admin_login)
app.route('/adminsignup', methods=['GET', 'POST'])(user_controllers.admin_signup)


