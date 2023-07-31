import frappe
@frappe.whitelist()
def get_corporate():
    anout_us = frappe.get_list("Corporate News", fields=["name", "attach","heading","description"])
    print(anout_us)
    return frappe.get_list("Corporate News", fields=["name", "attach","heading","description"])