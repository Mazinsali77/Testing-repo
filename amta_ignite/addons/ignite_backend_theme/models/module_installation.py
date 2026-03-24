from odoo import models

class IrModuleModule(models.Model):
    _inherit = 'ir.module.module'

    def button_immediate_install(self):
        res = super(IrModuleModule, self).button_immediate_install()
        if self.name == 'ignite_backend_theme':
            self.env['res.config.settings'].update_all_icons()
        return res

    def button_upgrade(self):
        res = super(IrModuleModule, self).button_upgrade()
        if self.name == 'ignite_backend_theme':
            self.env['res.config.settings'].update_all_icons()
        return res
