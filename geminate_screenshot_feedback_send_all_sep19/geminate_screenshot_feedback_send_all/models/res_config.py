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
from odoo import api, fields, models, _
import json

class screenshotFeedback(models.Model):
    _name = 'screenshort.feedback'
    _rec_name = 'email'

    url = fields.Char("Website URL")
    res_name = fields.Char("Website URL")
    email = fields.Char("Email",default=lambda self: self.env.user.partner_id.email)
    browser = fields.Text("Browser")
    note = fields.Text("Comment")
    img = fields.Binary("Image")
    binary_related_store = fields.Binary("Binary Related Store", related='img', store=True, readonly=False)
    created_date = fields.Datetime(string='Create Date', required=True, readonly=True, index=True, copy=False, default=fields.Datetime.now)
    user = fields.Many2one('res.users', copy=False,string='Responsible',default=lambda self: self.env.user,readonly=True)
    is_private = fields.Boolean("Enabled Mail (CC)",readonly=True)
    private_emails = fields.Char("Mail (CC)",readonly=True)

class SettingsInherit3cx(models.TransientModel):
    _inherit = 'res.config.settings'

    screenshot_enable = fields.Boolean("Enable Screenshot")

    screenshot_feedback_name = fields.Char("Feedback Title",required=True)
    screenshot_feedback_detail = fields.Char("Feedback Detail",required=True)
    screenshot_email_req_name = fields.Char("Request Email",required=True)
    screenshot_desc_req_name = fields.Char("Request Detail",required=True)
    screenshot_desc_note = fields.Char("Feedback Note",required=True)
    screenshot_desc_warn = fields.Char("Detail Warning Message",required=True)
    screenshot_email_warn = fields.Char("Email Warning Message",required=True)
    screenshot_drag_note = fields.Text("Drag Note",required=True)
    screenshot_highlight = fields.Char("Highlight Button",required=True)
    screenshot_highlight_detail = fields.Char("Highlight Button Detail",required=True)
    screenshot_black_out = fields.Char("Black Out Button",required=True)
    screenshot_black_out_detail = fields.Char("Black Out Button Detail",required=True)
    screenshot_next = fields.Char("Next Button",required=True)
    screenshot_back = fields.Char("Back Button",required=True)
    screenshot_description = fields.Char("Description Title",required=True)
    screenshot_additional_info = fields.Char("Additional Information Text",required=True)
    screenshot_browser_info = fields.Char("Browser Information Text",required=True)
    screenshot_page_info = fields.Char("Page Information Text",required=True)
    screenshot_page_structure = fields.Char("Page Structure Text",required=True)
    screenshot_screenshot = fields.Char("Screenshot Title",required=True)
    screenshot_submit = fields.Char("Submit Button",required=True)
    screenshot_error_msg = fields.Text("Error Message",required=True)
    screenshot_ok = fields.Char("Ok Button",required=True)
    screenshot_sucess_msg = fields.Text("Success Message",required=True)

    screenshot_initial_box = fields.Boolean("Enable Initial Box",help="Enable checkbox to open popup to add Mail (CC) by reporting user and disable checkbox to use only company setting's recipient mail ids instead of extra Mail (CC).In both cases, login user will receive a copy of mail anyhow.")
    screenshot_is_private = fields.Char("Mail (CC) Checkbox Label",required=True)
    screenshot_private_email_request = fields.Char("Mail (CC) Input Placeholder",required=True)
    screenshot_image_timeout = fields.Char("Screenshot Render Timeout",required=True)
    screenshot_partners = fields.Many2many(comodel_name='res.partner', readonly=False,string="Default Mail Recipient(s)")


    @api.model
    def get_values(self):
        res = super(SettingsInherit3cx, self).get_values()
        UrlConfig = self.env['ir.config_parameter'].sudo()
        res.update({
            'screenshot_enable': UrlConfig.get_param('geminate_screenshot_feedback_send_all.screenshot_enable'),
            'screenshot_feedback_name': UrlConfig.get_param('geminate_screenshot_feedback_send_all.screenshot_feedback_name','Feedback'),
            'screenshot_feedback_detail': UrlConfig.get_param('geminate_screenshot_feedback_send_all.screenshot_feedback_detail','Feedback lets you send us suggestions about this site. We welcome problem reports, feature ideas and general comments.'),
            'screenshot_email_req_name': UrlConfig.get_param('geminate_screenshot_feedback_send_all.screenshot_email_req_name','If you wish to be contacted please leave us your email:'),
            'screenshot_desc_req_name': UrlConfig.get_param('geminate_screenshot_feedback_send_all.screenshot_desc_req_name','Start by writing a brief description:'),
            'screenshot_desc_note': UrlConfig.get_param('geminate_screenshot_feedback_send_all.screenshot_desc_note',"Next we'll let you identify areas of the page related to your description."),
            'screenshot_desc_warn': UrlConfig.get_param('geminate_screenshot_feedback_send_all.screenshot_desc_warn','Please enter a description.'),
            'screenshot_email_warn': UrlConfig.get_param('geminate_screenshot_feedback_send_all.screenshot_email_warn','Please enter a email.'),
            'screenshot_drag_note': UrlConfig.get_param('geminate_screenshot_feedback_send_all.screenshot_drag_note',"Click and drag on the page to help us better understand your feedback. You can move this dialog if it's in the way."),
            'screenshot_highlight': UrlConfig.get_param('geminate_screenshot_feedback_send_all.screenshot_highlight',"Highlight"),
            'screenshot_highlight_detail': UrlConfig.get_param('geminate_screenshot_feedback_send_all.screenshot_highlight_detail',"Highlight areas relevant to your feedback."),
            'screenshot_black_out_detail': UrlConfig.get_param('geminate_screenshot_feedback_send_all.screenshot_black_out_detail',"Black out any personal information."),
            'screenshot_black_out': UrlConfig.get_param('geminate_screenshot_feedback_send_all.screenshot_black_out',"Black out"),
            'screenshot_next': UrlConfig.get_param('geminate_screenshot_feedback_send_all.screenshot_next','Next'),
            'screenshot_back': UrlConfig.get_param('geminate_screenshot_feedback_send_all.screenshot_back','Back'),
            'screenshot_description': UrlConfig.get_param('geminate_screenshot_feedback_send_all.screenshot_description','Description'),
            'screenshot_additional_info': UrlConfig.get_param('geminate_screenshot_feedback_send_all.screenshot_additional_info','Additional info'),
            'screenshot_browser_info': UrlConfig.get_param('geminate_screenshot_feedback_send_all.screenshot_browser_info','Browser Info'),
            'screenshot_page_info': UrlConfig.get_param('geminate_screenshot_feedback_send_all.screenshot_page_info','Page Info'),
            'screenshot_page_structure': UrlConfig.get_param('geminate_screenshot_feedback_send_all.screenshot_page_structure','Page Structure'),
            'screenshot_screenshot': UrlConfig.get_param('geminate_screenshot_feedback_send_all.screenshot_screenshot','Screenshot'),
            'screenshot_submit': UrlConfig.get_param('geminate_screenshot_feedback_send_all.screenshot_submit','Submit'),
            'screenshot_error_msg': UrlConfig.get_param('geminate_screenshot_feedback_send_all.screenshot_error_msg','Sadly an error occurred while sending your feedback. Please try again.'),
            'screenshot_ok': UrlConfig.get_param('geminate_screenshot_feedback_send_all.screenshot_ok','ok'),
            'screenshot_sucess_msg': UrlConfig.get_param('geminate_screenshot_feedback_send_all.screenshot_sucess_msg','<p>Thank you for your feedback. We value every piece of feedback we receive.</p><p>We cannot respond individually to every one, but we will use your comments as we strive to improve your experience.</p>'),
            'screenshot_initial_box': UrlConfig.get_param('geminate_screenshot_feedback_send_all.screenshot_initial_box'),
            'screenshot_private_email_request': UrlConfig.get_param('geminate_screenshot_feedback_send_all.screenshot_private_email_request','Enter Private Mail'),
            'screenshot_is_private': UrlConfig.get_param('geminate_screenshot_feedback_send_all.screenshot_is_private','Is Private'),
            'screenshot_image_timeout': UrlConfig.get_param('geminate_screenshot_feedback_send_all.screenshot_image_timeout','10000'),
            'screenshot_partners': [(6, 0, json.loads(UrlConfig.get_param('geminate_screenshot_feedback_send_all.screenshot_partners')) if UrlConfig.get_param('geminate_screenshot_feedback_send_all.screenshot_partners') else [])],
            })
        return res

    def set_values(self):
        super(SettingsInherit3cx, self).set_values()

        self.env['ir.config_parameter'].sudo().set_param(
            'geminate_screenshot_feedback_send_all.screenshot_enable', self.screenshot_enable)

        self.env['ir.config_parameter'].sudo().set_param(
            'geminate_screenshot_feedback_send_all.screenshot_feedback_name', self.screenshot_feedback_name)

        self.env['ir.config_parameter'].sudo().set_param(
            'geminate_screenshot_feedback_send_all.screenshot_feedback_detail', self.screenshot_feedback_detail)

        self.env['ir.config_parameter'].sudo().set_param(
            'geminate_screenshot_feedback_send_all.screenshot_email_req_name', self.screenshot_email_req_name)

        self.env['ir.config_parameter'].sudo().set_param(
            'geminate_screenshot_feedback_send_all.screenshot_desc_req_name', self.screenshot_desc_req_name)

        self.env['ir.config_parameter'].sudo().set_param(
            'geminate_screenshot_feedback_send_all.screenshot_desc_note', self.screenshot_desc_note)

        self.env['ir.config_parameter'].sudo().set_param(
            'geminate_screenshot_feedback_send_all.screenshot_desc_warn', self.screenshot_desc_warn)

        self.env['ir.config_parameter'].sudo().set_param(
            'geminate_screenshot_feedback_send_all.screenshot_email_warn', self.screenshot_email_warn)

        self.env['ir.config_parameter'].sudo().set_param(
            'geminate_screenshot_feedback_send_all.screenshot_drag_note', self.screenshot_drag_note)

        self.env['ir.config_parameter'].sudo().set_param(
            'geminate_screenshot_feedback_send_all.screenshot_highlight', self.screenshot_highlight)

        self.env['ir.config_parameter'].sudo().set_param(
            'geminate_screenshot_feedback_send_all.screenshot_highlight_detail', self.screenshot_highlight_detail)

        self.env['ir.config_parameter'].sudo().set_param(
            'geminate_screenshot_feedback_send_all.screenshot_black_out_detail', self.screenshot_black_out_detail)

        self.env['ir.config_parameter'].sudo().set_param(
            'geminate_screenshot_feedback_send_all.screenshot_black_out', self.screenshot_black_out)

        self.env['ir.config_parameter'].sudo().set_param(
            'geminate_screenshot_feedback_send_all.screenshot_next', self.screenshot_next)

        self.env['ir.config_parameter'].sudo().set_param(
            'geminate_screenshot_feedback_send_all.screenshot_back', self.screenshot_back)

        self.env['ir.config_parameter'].sudo().set_param(
            'geminate_screenshot_feedback_send_all.screenshot_description', self.screenshot_description)

        self.env['ir.config_parameter'].sudo().set_param(
            'geminate_screenshot_feedback_send_all.screenshot_additional_info', self.screenshot_additional_info)

        self.env['ir.config_parameter'].sudo().set_param(
            'geminate_screenshot_feedback_send_all.screenshot_browser_info', self.screenshot_browser_info)

        self.env['ir.config_parameter'].sudo().set_param(
            'geminate_screenshot_feedback_send_all.screenshot_page_info', self.screenshot_page_info)

        self.env['ir.config_parameter'].sudo().set_param(
            'geminate_screenshot_feedback_send_all.screenshot_page_structure', self.screenshot_page_structure)

        self.env['ir.config_parameter'].sudo().set_param(
            'geminate_screenshot_feedback_send_all.screenshot_screenshot', self.screenshot_screenshot)

        self.env['ir.config_parameter'].sudo().set_param(
            'geminate_screenshot_feedback_send_all.screenshot_submit', self.screenshot_submit)

        self.env['ir.config_parameter'].sudo().set_param(
            'geminate_screenshot_feedback_send_all.screenshot_error_msg', self.screenshot_error_msg)

        self.env['ir.config_parameter'].sudo().set_param(
            'geminate_screenshot_feedback_send_all.screenshot_ok', self.screenshot_ok)

        self.env['ir.config_parameter'].sudo().set_param(
            'geminate_screenshot_feedback_send_all.screenshot_sucess_msg', self.screenshot_sucess_msg)

        self.env['ir.config_parameter'].sudo().set_param(
            'geminate_screenshot_feedback_send_all.screenshot_initial_box', self.screenshot_initial_box)
        self.env['ir.config_parameter'].sudo().set_param(
            'geminate_screenshot_feedback_send_all.screenshot_private_email_request', self.screenshot_private_email_request)
        self.env['ir.config_parameter'].sudo().set_param(
            'geminate_screenshot_feedback_send_all.screenshot_is_private', self.screenshot_is_private)

        self.env['ir.config_parameter'].sudo().set_param(
                    'geminate_screenshot_feedback_send_all.screenshot_image_timeout', self.screenshot_image_timeout)

        self.env['ir.config_parameter'].sudo().set_param(
            'geminate_screenshot_feedback_send_all.screenshot_partners', self.screenshot_partners.ids if self.screenshot_partners else False)
