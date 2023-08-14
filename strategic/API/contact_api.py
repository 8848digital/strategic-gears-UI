import frappe

@frappe.whitelist(allow_guest=True)
def contact(**kwargs):
    try:
        if not kwargs.get('full_name'):
            return error_response("Please define full_name.")
        if not kwargs.get('email_address'):
            return error_response("Please define email_address.")
        if not kwargs.get('mobile_number'):
            return error_response("Please define mobile_number.")
        if not kwargs.get('your_message'):
            return error_response("Please define your_message.")
        contact = frappe.new_doc("Contact US")
        contact.full_name = kwargs.get('full_name')
        contact.email_address = kwargs.get('email_address')
        contact.mobile_number = kwargs.get('mobile_number')
        contact.your_message = kwargs.get('your_message')
        contact.save(ignore_permissions=True)
        return {
            "status": "success",
            "message": "subscribed successfully.",
            "subscribe_id": contact.name
        }
    except Exception as e:
        frappe.logger('leave').exception(e)
        return error_response(str(e))
    

def error_response(err_msg):
    return {
        'msg': 'error',
        'error': err_msg
    }    