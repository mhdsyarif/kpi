# -*- coding: utf-8 -*-

from openerp import api, models, fields

class kpi_target(models.Model):
    _name = 'kpi.target'
    _inherit = ['mail.thread']

    number = fields.Char(string='Number',required=True,
        track_visibility='onchange')
    name = fields.Char(string="Name", required=True, 
        track_visibility='onchange')
    start_date = fields.Date(string="Start Date",
        default = fields.Date.to_string, required=True, 
        track_visibility='onchange')
    end_date = fields.Date(string="End Date",
        default = fields.Date.to_string, required=True, 
        track_visibility='onchange')
    department = fields.Many2one('hr.department',
        string='Department', required=True, 
        track_visibility='onchange')
    employee_id = fields.Many2one('hr.employee',string="Personal", 
        track_visibility='onchange')
    description = fields.Text(string="Description", 
        track_visibility='onchange')

