import frappe

@frappe.whitelist()
def get_team():
    home_banner = frappe.get_list("Our Team", fields=["name", "attach", "designation","tittle","description"])
    print(home_banner)
    return frappe.get_list("Our Team", fields=["name", "attach", "designation","tittle","description"])