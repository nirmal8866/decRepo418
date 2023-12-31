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
from odoo import _, api, fields, models, modules, tools
from deep_translator import GoogleTranslator

@api.model
def _lang_get_l(self):
    return self.env['res.lang'].sudo().search([('code','=','en_US')],limit=1)

class ChannelInherit(models.Model):
    
    _inherit = 'discuss.channel'
    
    language = fields.Many2one('res.lang', string='Receiver Language', default=_lang_get_l, help="All the emails and documents sent to this contact will be translated in this language.")
    translation_color = fields.Char(string="Translation Color",help="Choose your color", default="#008000")

class MailThreadInherit(models.AbstractModel):
    _inherit = 'mail.thread'
    
    @api.returns('mail.message', lambda value: value.id)
    def message_post(self, *,
                     body='', subject=None, message_type='notification',
                     email_from=None, author_id=None, parent_id=False,
                     subtype_xmlid=None, subtype_id=False, partner_ids=None,
                     attachments=None, attachment_ids=None,
                     add_sign=True, record_name=False,
                     **kwargs):
        if self and self.env.user.lang and body:
            if message_type == 'comment':
                if self.translation_color:
                    channel_color = self.translation_color
                else:
                    channel_color = '#008000'
                user_length = len(self.channel_last_seen_partner_ids)
                if not user_length > 2:
                    user_language = False
                    receiver_language = False
                    for line in self.channel_last_seen_partner_ids:
                        if line.partner_id == self.env.user.partner_id:
                            user_language = line.partner_id.lang
                        else:
                            receiver_language = line.partner_id.lang
                    user_language = self.env['res.lang'].sudo().search([('code','=',user_language)],limit=1)
                    receiver_language = self.env['res.lang'].sudo().search([('code','=',receiver_language)],limit=1)
                    if receiver_language and user_language and not user_language == receiver_language:
                        team_result = GoogleTranslator(source=user_language.iso_code, target=receiver_language.iso_code).translate(body)
                        body = body +'<p class="translator_result" style="color:'+channel_color+'">'+ team_result +'</p>'
                else:
                    user_lang = self.env['res.lang'].sudo().search([('code','=',self.env.user.lang)],limit=1)
                    if self.language and not self.language.code == self.env.user.lang and user_lang:
                        team_result = GoogleTranslator(source=user_lang.iso_code, target=self.language.iso_code).translate(body)
                        body = body +'<p class="translator_result" style="color:'+channel_color+'">'+ team_result +'</p>'
        msg = super(MailThreadInherit, self).message_post(body=body, subject=subject, message_type=message_type,
                     email_from=email_from, author_id=author_id, parent_id=parent_id,
                     subtype_xmlid=subtype_xmlid, subtype_id=subtype_id, partner_ids=partner_ids,
                     attachments=attachments, attachment_ids=attachment_ids,
                     add_sign=add_sign, record_name=record_name,
                     **kwargs)
        return msg
    
