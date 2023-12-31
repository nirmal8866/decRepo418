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

{
    'name': 'Geminate IM Multi Language',
    'version': '17.1.0',
    'description': """Geminate comes with a feature that supports Multilingual instant messaging where message will automatically translated to the language of 'Receiver' even if whatever language 'Sender' has used to type the message. It will automatically identify the language of receiver at both the ends and translate the message. it supports translation in group messaging as well where translated language can be configured on message channel formview.""",
    'author': 'Geminate Consultancy Services',
    'company': 'Geminate Consultancy Services',
    'website': 'https://www.geminatecs.com/',
    'summary': """Geminate IM Multi Language""",
    "license": "Other proprietary",
    'category': 'mail',
    'depends': ['mail'],
    'data': [
            'views/multi_language.xml'
    ],
    'qweb': [],
    "license": "Other proprietary",
    'installable': True,
    'images': ['static/description/multilang.jpg'],
    'auto_install': False,
    'application': False,
}  
