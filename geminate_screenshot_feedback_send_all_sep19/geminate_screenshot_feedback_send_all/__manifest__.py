#this is my custom libne got module
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
