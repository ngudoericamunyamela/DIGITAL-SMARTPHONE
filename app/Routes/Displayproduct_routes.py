from flask import Blueprint
from ..Controllers import Displayproduct_controllers

app = Blueprint ('Service',__name__)


app.route("/Display_Servicess", methods=["POST", "GET"])(Displayproduct_controllers.delete_Display_Services)
app.route("/Edit_Services", methods=["POST"])(Displayproduct_controllers.update_service)
app.route("/Update_Services", methods=["POST"])(Displayproduct_controllers.update_service2)
app.route("/delete_Display_Services", methods=["GET", "POST"])(Displayproduct_controllers.delete_Display_Services)

