import frappe
from frappe import _
from frappe.utils.response import build_response

@frappe.whitelist(allow_guest=True)
def get_client():
    try:
        client = frappe.get_list("Our Clients", fields=["name", "attach"])
        return build_response("success", data=client)
    except Exception as e:
        frappe.log_error(title=_("API Error"), message=e)
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
