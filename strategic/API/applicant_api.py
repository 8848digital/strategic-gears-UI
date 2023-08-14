import frappe

@frappe.whitelist(allow_guest=True)
def applicant(**kwargs):
    try:
        if not kwargs.get('resumecv'):
            return error_response("Please define resumecv")
        if not kwargs.get('full_name'):
            return error_response("Please define full_name")
        if not kwargs.get('email'):
            return error_response("Please define email")
        if not kwargs.get('phone'):
            return error_response("Please define phone.")
        if not kwargs.get('current_company'):
            return error_response("Please define current_company.")
        if not kwargs.get('linkedin_url'):
            return error_response("Please define linkedin_url.")
        if not kwargs.get('what_is_your_nationality'):
            return error_response("Please define what_is_your_nationality.")
        if not kwargs.get('please_attach_your_iqama_application'):
            return error_response("Please define please_attach_your_iqama_application.")
        if not kwargs.get('what_is_your_major_in_the_university'):
            return error_response("Please define what_is_your_major_in_the_university.")
        if not kwargs.get('arabic_proficiency'):
            return error_response("Please define arabic_proficiency.")
        if not kwargs.get('english_proficiency'):
            return error_response("Please define english_proficiency.")
        if not kwargs.get('do_you_have_any_relatives_in_strategic_gears'):
            return error_response("Please define do_you_have_any_relatives_in_strategic_gears.")
        if not kwargs.get('additional_information'):
            return error_response("Please define additional_information.")
         
        
        applicant = frappe.new_doc("Applicant")
        applicant.resumecv = kwargs.get('resumecv')
        applicant.full_name = kwargs.get('full_name')
        applicant.email = kwargs.get('email')
        applicant.phone = kwargs.get('phone')
        applicant.current_company = kwargs.get('current_company')
        applicant.linkedin_url = kwargs.get('linkedin_url')
        applicant.what_is_your_nationality = kwargs.get('what_is_your_nationality')
        applicant.please_attach_your_iqama_application = kwargs.get('please_attach_your_iqama_application')
        applicant.what_is_your_major_in_the_university = kwargs.get('what_is_your_major_in_the_university')
        applicant.arabic_proficiency = kwargs.get('arabic_proficiency')
        applicant.english_proficiency = kwargs.get('english_proficiency')
        applicant.do_you_have_any_relatives_in_strategic_gears = kwargs.get('do_you_have_any_relatives_in_strategic_gears')
        applicant.additional_information = kwargs.get('additional_information')


        applicant.save(ignore_permissions=True)
        return {
            "status": "success",
            "message": "subscribed successfully.",
            "subscribe_id": applicant.name
        }
    except Exception as e:
        frappe.logger('leave').exception(e)
        return error_response(str(e))
    

def error_response(err_msg):
    return {
        'msg': 'error',
        'error': err_msg
    }    