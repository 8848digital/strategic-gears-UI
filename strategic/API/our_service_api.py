import frappe
from frappe import _
from frappe.utils.response import build_response

@frappe.whitelist(allow_guest=True)
def get_service():
    try:
        # Fetch data from the parent table "Our Service"
        our_services = frappe.get_list("Our Service", fields=["attach", "heading", "limit", "description", "service_table"])

        # Fetch data from the child table "Service Table" and add it to the result
        for service in our_services:
            service["service_table_data"] = frappe.get_all("Service Table", filters={"parent": service.name}, fields=["name1", "description"])

        return build_response("success", data=our_services)
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
