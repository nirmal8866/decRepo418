# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2016-Today Geminate Consultancy Services (<http://geminatecs.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': "Tellme Feedback with Screenshot",
    'version': '17.0.1',
    'category': 'website',
    'summary': "Tellme Feedback with Screenshot",
    'description': """Geminate comes with the feedback with screenshot tool. Nowadays while operating an application, we might face a problem somewhere in any view or flow and want to highlight and send for quick help or provide feedback for improvement. we have introduced this tool where you can highlight and blackouts to specify specific points. it sends the response by mail to the user and the specified participant. if Mail (CC) is enabled then it will send additional mail in CC. mainly it is focused on different areas of application like point of sale, website, backend ERP and report views.""",
    'license': 'Other proprietary',
    'author': "Geminate Consultancy Services",
    'website': 'http://www.geminatecs.com',
    "depends": [
        'base_setup','mail'
    ],
    "data": [
        'data/mail_template.xml',
        'security/ir.model.access.csv',
        'views/res_config_settings.xml',
        'views/main.xml',
        ],
    'assets': {
        'web.assets_common': [
            'geminate_screenshot_feedback_send_all/static/src/js/main.js',
            'geminate_screenshot_feedback_send_all/static/src/xml/main.xml',
        ]
    },
    "images": ['static/description/banner.png'],
    "test": [],
    "installable": True,
}  
