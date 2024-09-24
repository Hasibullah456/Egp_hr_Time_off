# Part of Odoo. See LICENSE file for full copyright and licensing details
from odoo import models, api, fields



class time(models.Model):
    _inherit = "hr.leave"
    _description = "time off"

    employee_ids = fields.Many2many(
        'hr.employee', compute='_compute_from_holiday_type', store=True, string='Employees', readonly=True,
        groups="hr_holidays.group_hr_holidays_responsible,egp_hr.super_admin,egp_hr.officer",
        domain=lambda self: self._get_employee_domain())
