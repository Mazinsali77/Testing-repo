from odoo import api, models

class ResUsers(models.Model):
    _inherit = 'res.users'

    @api.model
    def update_odoobot_name(self):
        """Change OdooBot name to IgniteAI"""
        odoobot = self.env['res.users'].browse(2)
        if odoobot.exists() and odoobot.name == 'OdooBot':
            odoobot.write({'name': 'IgniteAI'})
