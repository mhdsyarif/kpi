# -*- coding: utf-8 -*-

from openerp import api, models, fields

class kpi_activity(models.Model):
    _name = 'kpi.activity'
    _inherit = ['mail.thread']

    name = fields.Char(string="Title", required=True, 
        track_visibility='onchange')
    target_id = fields.Many2one('kpi.action',
        string="Target", required=True, 
        track_visibility='onchange')
    pic = fields.Many2one('res.users', string="PIC", required=True, 
        track_visibility='onchange')
    due_date = fields.Date(string="Due Date", 
        default = fields.Date.to_string, required=True,
        track_visibility='onchange')
    budget = fields.Float(string="Budget", 
        track_visibility='onchange')
    status = fields.Selection(
        string="Status", 
        selection=[('1','To do'),('2','On going'),('3','Finish')], 
        required=True, 
        track_visibility='onchange'
    )