# your_app_name/api.py
import frappe

@frappe.whitelist()
def get_banner():
    home_banner = frappe.get_list("Home Banner", fields=["name", "attach", "heading","sub_heading","description"])
    print(home_banner)
    return frappe.get_list("Home Banner", fields=["name", "attach", "heading","sub_heading","description"])



