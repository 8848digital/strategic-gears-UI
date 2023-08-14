import frappe
from frappe import _
from frappe.utils.response import build_response

@frappe.whitelist(allow_guest=True)
def get_Reports():
    try:
        our_reports = frappe.get_all("Reports", fields=["heading", "sub_heading","description1","description2","attach"])

        
        return build_response("success", data=our_reports)
    except Exception as e:
        frappe.log_error(title=_("API Error"), message=str(e))
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
