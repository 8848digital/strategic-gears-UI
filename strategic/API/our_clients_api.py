import frappe
@frappe.whitelist()
def get_client():
    anout_us = frappe.get_list("Our Clients", fields=["name", "attach"])
    print(anout_us)
    return frappe.get_list("Our Clients", fields=["name", "attach"])