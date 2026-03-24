from odoo import api, models
import base64
from odoo.modules import get_module_resource

class MailActivityType(models.Model):
    _inherit = 'mail.activity.type'

    @api.model
    def update_activity_icons(self):
        """Update activity icons"""
        activities = self.search([])
        for activity in activities:
            if activity.name == 'Call':
                img_path = get_module_resource('ignite_backend_theme', 'static', 'src', 'img', 'icons', 'call.png')
                activity.write({'icon': base64.b64encode(open(img_path, "rb").read())})
            if activity.name == 'Meeting':
                img_path = get_module_resource('ignite_backend_theme', 'static', 'src', 'img', 'icons', 'meeting.png')
                activity.write({'icon': base64.b64encode(open(img_path, "rb").read())})
            # Add similar blocks for other activities
