import frappe
from frappe import _
from frappe.utils.response import build_response

@frappe.whitelist(allow_guest=True)
def get_services():
    try:
        our_services = frappe.get_all("Our Service", fields=["name","attach", "heading", "limit", "description"])

        for service in our_services:
            service["values"] = frappe.get_all("Service Table", filters={"parent": service.name}, fields=["name1", "description"])

        return build_response("success", data=our_services)
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
