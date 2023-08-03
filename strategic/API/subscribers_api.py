import frappe

@frappe.whitelist(allow_guest=True)
def subscribe(**kwargs):
    try:
        if not kwargs.get('email'):
            return error_response("Please define Email.")
        if not kwargs.get('firstname'):
            return error_response("Please define Firstname.")
        if not kwargs.get('lastname'):
            return error_response("Please define Lastname.")
        subscribe = frappe.new_doc("Subscribe")
        subscribe.email_address = kwargs.get('email')
        subscribe.first_name = kwargs.get('firstname')
        subscribe.last_name = kwargs.get('lastname')
        subscribe.save(ignore_permissions=True)
        return {
            "status": "success",
            "message": "subscribed successfully.",
            "subscribe_id": subscribe.name
        }
    except Exception as e:
        frappe.logger('leave').exception(e)
        return error_response(str(e))
    

def error_response(err_msg):
    return {
        'msg': 'error',
        'error': err_msg
    }    