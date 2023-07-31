import frappe
@frappe.whitelist()
def get_about():
    anout_us = frappe.get_list("About US", fields=["name", "attach", "heading","description"])
    print(anout_us)
    return frappe.get_list("About US", fields=["name", "attach", "heading","description"])