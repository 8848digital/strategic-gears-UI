# your_app_name/api.py
import frappe
from frappe import _
from frappe.utils.response import build_response

@frappe.whitelist(allow_guest=True)
def get_actions():
    try:
        action = frappe.get_list("Call To Action", fields=["name", "attach","custom_heading","custom_description" ])

        for action in action:
            action["sector_data"] = frappe.get_all("Action Table", filters={"parent": action.name}, fields=["name1"])
        return build_response("success", data=action)
    except Exception as e:
        frappe.log_error(title=_("API Error"), message=e, traceback=True)
        return build_response("error", message=_("An error occurred while fetching data."))

def build_response(status, data=None, message=None):
    response = {
        "status": status
    }

    if data is not None:
        response["data"] = data

    if message is not None:
        response["message"] = message

    return response
