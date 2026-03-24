from odoo import api, models
import base64
from odoo.modules import get_module_resource

class IrModuleModule(models.Model):
    _inherit = 'ir.module.module'

    @api.model
    def update_apps_icons(self):
        """Update apps icons"""
        apps = self.search([])
        for app in apps:
            if app.name == 'Sales':
                img_path = get_module_resource('ignite_backend_theme', 'static', 'src', 'img', 'icons', 'sales.png')
                app.write({'icon': base64.b64encode(open(img_path, "rb").read())})
            if app.name == 'Website':
                img_path = get_module_resource('ignite_backend_theme', 'static', 'src', 'img', 'icons', 'website.png')
                app.write({'icon': base64.b64encode(open(img_path, "rb").read())})
            # Add similar blocks for other apps
