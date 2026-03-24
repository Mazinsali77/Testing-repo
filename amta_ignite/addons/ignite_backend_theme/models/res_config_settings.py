from odoo import api, models
import base64
from odoo.modules import get_module_resource

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    def update_all_icons(self):
        """Update all icons in Activities, Settings, and Apps"""
        self.env['res.config.settings'].update_menu_icons()
        self.env['ir.ui.menu'].update_settings_icons()
        self.env['mail.activity.type'].update_activity_icons()
        self.env['ir.module.module'].update_apps_icons()
        self.env['res.users'].update_odoobot_name()

    @api.model
    def update_menu_icons(self):
        """Updates menu icons dynamically"""
        menu_item = self.env['ir.ui.menu'].search([('parent_id', '=', False)])
        for menu in menu_item:
            if menu.name == 'Contacts':
                img_path = get_module_resource(
                    'ignite_backend_theme', 'static', 'src', 'img', 'icons',
                    'contacts.png')
                menu.write({'web_icon_data': base64.b64encode(
                    open(img_path, "rb").read())})
            if menu.name == 'Link Tracker':
                img_path = get_module_resource(
                    'ignite_backend_theme', 'static', 'src', 'img', 'icons',
                    'link_tracker.png')
                menu.write({'web_icon_data': base64.b64encode(
                    open(img_path, "rb").read())})
            if menu.name == 'Dashboards':
                img_path = get_module_resource(
                    'ignite_backend_theme', 'static', 'src', 'img', 'icons',
                    'dashboards.png')
                menu.write({'web_icon_data': base64.b64encode(
                    open(img_path, "rb").read())})
            if menu.name == 'Sales':
                img_path = get_module_resource(
                    'ignite_backend_theme', 'static', 'src', 'img', 'icons',
                    'sales.png')
                menu.write({'web_icon_data': base64.b64encode(
                    open(img_path, "rb").read())})
            if menu.name == 'Invoicing' or menu.name == 'Accounting':
                img_path = get_module_resource(
                    'ignite_backend_theme', 'static', 'src', 'img', 'icons',
                    'invoicing.png')
                menu.write({'web_icon_data': base64.b64encode(
                    open(img_path, "rb").read())})
            if menu.name == 'Inventory':
                img_path = get_module_resource(
                    'ignite_backend_theme', 'static', 'src', 'img', 'icons',
                    'inventory.png')
                menu.write({'web_icon_data': base64.b64encode(
                    open(img_path, "rb").read())})
            if menu.name == 'Purchase':
                img_path = get_module_resource(
                    'ignite_backend_theme', 'static', 'src', 'img', 'icons',
                    'purchase.png')
                menu.write({'web_icon_data': base64.b64encode(
                    open(img_path, "rb").read())})
            if menu.name == 'CRM':
                img_path = get_module_resource(
                    'ignite_backend_theme', 'static', 'src', 'img', 'icons',
                    'crm.png')
                menu.write({'web_icon_data': base64.b64encode(
                    open(img_path, "rb").read())})
            if menu.name == 'Website':
                img_path = get_module_resource(
                    'ignite_backend_theme', 'static', 'src', 'img', 'icons',
                    'website.png')
                menu.write({'web_icon_data': base64.b64encode(
                    open(img_path, "rb").read())})
            if menu.name == 'Point of Sale':
                img_path = get_module_resource(
                    'ignite_backend_theme', 'static', 'src', 'img', 'icons',
                    'pos.png')
                menu.write({'web_icon_data': base64.b64encode(
                    open(img_path, "rb").read())})
            if menu.name == 'Project':
                img_path = get_module_resource(
                    'ignite_backend_theme', 'static', 'src', 'img', 'icons',
                    'projects.png')
                menu.write({'web_icon_data': base64.b64encode(
                    open(img_path, "rb").read())})
            if menu.name == 'Timesheets':
                img_path = get_module_resource(
                    'ignite_backend_theme', 'static', 'src', 'img', 'icons',
                    'timesheet.png')
                menu.write({'web_icon_data': base64.b64encode(
                    open(img_path, "rb").read())})
            if menu.name == 'Employees':
                img_path = get_module_resource(
                    'ignite_backend_theme', 'static', 'src', 'img', 'icons',
                    'employees.png')
                menu.write({'web_icon_data': base64.b64encode(
                    open(img_path, "rb").read())})
            if menu.name == 'Expenses':
                img_path = get_module_resource(
                    'ignite_backend_theme', 'static', 'src', 'img', 'icons',
                    'expenses.png')
                menu.write({'web_icon_data': base64.b64encode(
                    open(img_path, "rb").read())})
            if menu.name == 'Live Chat':
                img_path = get_module_resource(
                    'ignite_backend_theme', 'static', 'src', 'img', 'icons',
                    'chat.png')
                menu.write({'web_icon_data': base64.b64encode(
                    open(img_path, "rb").read())})
            if menu.name == 'Email Marketing':
                img_path = get_module_resource(
                    'ignite_backend_theme', 'static', 'src', 'img', 'icons',
                    'email.png')
                menu.write({'web_icon_data': base64.b64encode(
                    open(img_path, "rb").read())})
            if menu.name == 'SMS Marketing':
                img_path = get_module_resource(
                    'ignite_backend_theme', 'static', 'src', 'img', 'icons',
                    'sms.png')
                menu.write({'web_icon_data': base64.b64encode(
                    open(img_path, "rb").read())})
            if menu.name == 'Note':
                img_path = get_module_resource(
                    'ignite_backend_theme', 'static', 'src', 'img', 'icons',
                    'note.png')
                menu.write({'web_icon_data': base64.b64encode(
                    open(img_path, "rb").read())})
                
            if menu.name == 'eLearning':
                img_path = get_module_resource(
                    'ignite_backend_theme', 'static', 'src', 'img', 'icons',
                    'elearning.png')
                menu.write({'web_icon_data': base64.b64encode(
                    open(img_path, "rb").read())})
            if menu.name == 'Surveys':
                img_path = get_module_resource(
                    'ignite_backend_theme', 'static', 'src', 'img', 'icons',
                    'surveys.png')
                menu.write({'web_icon_data': base64.b64encode(
                    open(img_path, "rb").read())})
                
            if menu.name == 'Recruitment':
                img_path = get_module_resource(
                    'ignite_backend_theme', 'static', 'src', 'img', 'icons',
                    'recruitment.png')
                menu.write({'web_icon_data': base64.b64encode(
                    open(img_path, "rb").read())})
            if menu.name == 'Attendances':
                img_path = get_module_resource(
                    'ignite_backend_theme', 'static', 'src', 'img', 'icons',
                    'attendances.png')
                menu.write({'web_icon_data': base64.b64encode(
                    open(img_path, "rb").read())})
            if menu.name == 'Fleet':
                img_path = get_module_resource(
                    'ignite_backend_theme', 'static', 'src', 'img', 'icons',
                    'fleet.png')
                menu.write({'web_icon_data': base64.b64encode(
                    open(img_path, "rb").read())})
            # if menu.name == 'Members':
            #     img_path = get_module_resource(
            #         'ignite_backend_theme', 'static', 'src', 'img', 'icons',
            #         'members.png')
            #     menu.write({'web_icon_data': base64.b64encode(
            #         open(img_path, "rb").read())})
            if menu.name == 'Events':
                img_path = get_module_resource(
                    'ignite_backend_theme', 'static', 'src', 'img', 'icons',
                    'events.png')
                menu.write({'web_icon_data': base64.b64encode(
                    open(img_path, "rb").read())})
            if menu.name == 'Time Off':
                img_path = get_module_resource(
                    'ignite_backend_theme', 'static', 'src', 'img', 'icons',
                    'timeoff.png')
                menu.write({'web_icon_data': base64.b64encode(
                    open(img_path, "rb").read())})

            if menu.name == 'Lunch':
                img_path = get_module_resource(
                    'ignite_backend_theme', 'static', 'src', 'img', 'icons',
                    'lunch.png')
                menu.write({'web_icon_data': base64.b64encode(
                    open(img_path, "rb").read())})
                
            if menu.name == 'Maintenance':
                img_path = get_module_resource(
                    'ignite_backend_theme', 'static', 'src', 'img', 'icons',
                    'maintenance.png')
                menu.write({'web_icon_data': base64.b64encode(
                    open(img_path, "rb").read())})

            if menu.name == 'Manufacturing':
                img_path = get_module_resource(
                    'ignite_backend_theme', 'static', 'src', 'img', 'icons',
                    'manufacturing.png')
                menu.write({'web_icon_data': base64.b64encode(
                    open(img_path, "rb").read())})
            if menu.name == 'Repairs':
                img_path = get_module_resource(
                    'ignite_backend_theme', 'static', 'src', 'img', 'icons',
                    'repairs.png')
                menu.write({'web_icon_data': base64.b64encode(
                    open(img_path, "rb").read())})
