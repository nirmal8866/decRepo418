    # -*- coding: utf-8 -*-
###############################################################################
#
#   Copyright (C) 2004-today OpenERP SA (<http://www.openerp.com>)
#   Copyright (C) 2016-today Geminate Consultancy Services (<http://geminatecs.com>).
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Affero General Public License as
#   published by the Free Software Foundation, either version 3 of the
#   License, or (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#   GNU Affero General Public License for more details.
#
#   You should have received a copy of the GNU Affero General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################
from odoo import fields, http, _
from odoo.http import request
import json
import base64

class WebsiteBarcodeScanner(http.Controller):

    @http.route('/screenshot/feedback/set', type='http', auth='public',csrf=False)
    def screenshot_feedback_set(self,feedback,**kw):
        data = json.loads(feedback)
        # data['img'] = data['img'].split(',')[1]
        data['img'] = ','.join(data['img'].split(',')[1:])
        obj = request.env['screenshort.feedback'].create(data)
        context = obj.env.context.copy()
        UrlConfig = request.env['ir.config_parameter'].sudo()
        context['base_url'] = UrlConfig.get_param('web.base.url')
        context['company_id'] = request.env.company.id
        template = obj.with_context(context).env.ref('geminate_screenshot_feedback_send_all.geminate_screenshot_feedback_mail')
        if template:
            email_to = obj.email
            partners_id = json.loads(UrlConfig.get_param('geminate_screenshot_feedback_send_all.screenshot_partners')) if UrlConfig.get_param('geminate_screenshot_feedback_send_all.screenshot_partners') else []
            if len(partners_id) > 0:
                partners = request.env['res.partner'].sudo().browse(partners_id)
                email_to = email_to +','+ ','.join([res.email for res in partners]) if email_to else ','.join([res.email for res in partners])
            attachment = request.env['ir.attachment'].sudo().search(
                [('res_field', '=', 'binary_related_store'), ('res_id', '=', obj.id),('res_model','=','screenshort.feedback')])
            if not attachment:
                attachment = request.env['ir.attachment'].sudo().search(
                    [('res_field', '=', 'img'), ('res_id', '=', obj.id),('res_model','=','screenshort.feedback')])
            if attachment:
                attachment.public = True
            if email_to:
                template_values = {
                    'email_to': email_to,
                    'email_from': request.env.user.company_id.email,
                    'attachment_ids':[(6,0,[attachment.id] if attachment else [])],
                    'email_cc': obj.private_emails if obj.is_private else False,
                }
                template.sudo().write(template_values)
                mail_id = template.sudo().send_mail(obj.id,force_send=True)

    @http.route('/screenshot/feedback/get', type='json', auth='public')
    def screenshot_feedback_get(self,**kw):
        res = {}
        UrlConfig = request.env['ir.config_parameter'].sudo()
        if UrlConfig.get_param('geminate_screenshot_feedback_send_all.screenshot_enable'):
            res.update({
                'feedback_name': UrlConfig.get_param('geminate_screenshot_feedback_send_all.screenshot_feedback_name'),
                'feedback_detail': UrlConfig.get_param('geminate_screenshot_feedback_send_all.screenshot_feedback_detail'),
                'email_req_name': UrlConfig.get_param('geminate_screenshot_feedback_send_all.screenshot_email_req_name'),
                'desc_req_name': UrlConfig.get_param('geminate_screenshot_feedback_send_all.screenshot_desc_req_name'),
                'desc_note': UrlConfig.get_param('geminate_screenshot_feedback_send_all.screenshot_desc_note'),
                'desc_warn': UrlConfig.get_param('geminate_screenshot_feedback_send_all.screenshot_desc_warn'),
                'email_warn': UrlConfig.get_param('geminate_screenshot_feedback_send_all.screenshot_email_warn'),
                'drag_note': UrlConfig.get_param('geminate_screenshot_feedback_send_all.screenshot_drag_note'),
                'highlight': UrlConfig.get_param('geminate_screenshot_feedback_send_all.screenshot_highlight'),
                'highlight_detail': UrlConfig.get_param('geminate_screenshot_feedback_send_all.screenshot_highlight_detail'),
                'black_out_detail': UrlConfig.get_param('geminate_screenshot_feedback_send_all.screenshot_black_out_detail'),
                'black_out': UrlConfig.get_param('geminate_screenshot_feedback_send_all.screenshot_black_out'),
                'next': UrlConfig.get_param('geminate_screenshot_feedback_send_all.screenshot_next'),
                'back': UrlConfig.get_param('geminate_screenshot_feedback_send_all.screenshot_back'),
                'description': UrlConfig.get_param('geminate_screenshot_feedback_send_all.screenshot_description'),
                'additional_info': UrlConfig.get_param('geminate_screenshot_feedback_send_all.screenshot_additional_info'),
                'browser_info': UrlConfig.get_param('geminate_screenshot_feedback_send_all.screenshot_browser_info'),
                'page_info': UrlConfig.get_param('geminate_screenshot_feedback_send_all.screenshot_page_info'),
                'page_structure': UrlConfig.get_param('geminate_screenshot_feedback_send_all.screenshot_page_structure'),
                'screenshot': UrlConfig.get_param('geminate_screenshot_feedback_send_all.screenshot_screenshot'),
                'submit': UrlConfig.get_param('geminate_screenshot_feedback_send_all.screenshot_submit'),
                'error_msg': UrlConfig.get_param('geminate_screenshot_feedback_send_all.screenshot_error_msg'),
                'ok': UrlConfig.get_param('geminate_screenshot_feedback_send_all.screenshot_ok'),
                'sucess_msg': UrlConfig.get_param('geminate_screenshot_feedback_send_all.screenshot_sucess_msg'),
                'enable_email': False if request.env.user and request.env.user.id not in [1, 3, 4, 5] else True,
                'private_email_request': UrlConfig.get_param('geminate_screenshot_feedback_send_all.screenshot_private_email_request'),
                'is_private': UrlConfig.get_param('geminate_screenshot_feedback_send_all.screenshot_is_private'),
                'image_timeout': UrlConfig.get_param('geminate_screenshot_feedback_send_all.screenshot_image_timeout'),
                })
            return {
                'detail':res,
                'post_html':False,
                'initial_box':UrlConfig.get_param('geminate_screenshot_feedback_send_all.screenshot_initial_box'),
                'enable':True
            }
        return {'enable':False}
