import frappe
from frappe import _
from frappe.utils.response import build_response

@frappe.whitelist(allow_guest=True)
def get_point():
    try:
        our_point = frappe.get_all("Points Of Difference", fields=["name", "heading1", "sub_heading1", "heading2", "sub_heading2", "heading3", "sub_heading3", "heading4", "sub_heading4"])

        for point in our_point:
            point["values"] = frappe.get_all("Point Table", filters={"parent": point.name}, fields=["attach"])

        return build_response("success", data=our_point)
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
