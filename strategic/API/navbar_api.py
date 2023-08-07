# your_app_name/api.py
import frappe
from frappe import _
from frappe.utils.response import build_response

@frappe.whitelist(allow_guest=True)
def get_navbar():
    try:
        navbar = frappe.get_list("Navbar", fields=["name1"])
        for navtab in navbar:
            navtab["value"] = frappe.get_all("Navbar Table", filters={"parent": navtab.name1}, fields=["name1","url"])
        return build_response("success", data=navbar)
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
