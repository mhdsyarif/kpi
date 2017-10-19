# -*- coding: utf-8 -*-

from openerp import api, models, fields

class kpi_action(models.Model):
    _name = 'kpi.action'
    _inherit = ['mail.thread']

    name = fields.Char(string="Title", required=True, 
        track_visibility='onchange')
    target_id = fields.Many2one('kpi.target',
        string="Target", required=True, 
        track_visibility='onchange')
    pic_id = fields.Many2one('res.partner', string="PIC", required=True, 
        track_visibility='onchange')
    due_date = fields.Date(string="Due Date", 
        default = fields.Date.to_string, required=True,
        track_visibility='onchange')
    budget = fields.Float(string="Budget", 
        track_visibility='onchange')
    resources = fields.Char(string="Resources", 
        track_visibility='onchange')
    monitor_ids = fields.One2many('kpi.activity','target_id','Achievement')