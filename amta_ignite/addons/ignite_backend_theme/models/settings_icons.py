from odoo import api, models
import base64
from odoo.modules import get_module_resource

class IrUiMenu(models.Model):
    _inherit = 'ir.ui.menu'

    @api.model
    def update_settings_icons(self):
        """Update settings icons"""
        settings_menu = self.search([('name', '=', 'Settings')])
        for menu in settings_menu:
            if menu.name == 'Purchase':
                img_path = get_module_resource('ignite_backend_theme', 'static', 'src', 'img', 'icons', 'purchase.png')
                menu.write({'web_icon_data': base64.b64encode(open(img_path, "rb").read())})
            if menu.name == 'Inventory':
                img_path = get_module_resource('ignite_backend_theme', 'static', 'src', 'img', 'icons', 'inventory.png')
                menu.write({'web_icon_data': base64.b64encode(open(img_path, "rb").read())})
            # Add other settings icons similarly
