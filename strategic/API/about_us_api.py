import frappe

@frappe.whitelist(allow_guest=True)
def get_aboutus():
    try:
        about_us = frappe.get_list("About US", fields=["name", "attach", "heading", "description"])
        for about in about_us:
            child_table_data = frappe.get_all("About us Table", filters={"parent": about.name}, fields=["name1", "description"])
            about["values"] = [{"name1": item["name1"], "description_parts": item["description"].split('\n')} for item in child_table_data]

        return build_response("success", data=about_us)
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
