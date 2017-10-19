# -*- coding: utf-8 -*-

from openerp import api, models, fields


class kpi_achievement(models.Model):
    _name = 'kpi.achievement'
    _inherit = ['mail.thread']

    number = fields.Char(string='Number',required=True,
        track_visibility='onchange')
    target_id = fields.Many2one('kpi.target',
        string="Target", required=True, 
        track_visibility='onchange')
    target_number = fields.Char(string='Target Number',required=True,
        track_visibility='onchange')
    date = fields.Date(string="Date", 
        default = fields.Date.to_string, required=True, 
        track_visibility='onchange')
    note = fields.Text(string="Note", 
        track_visibility='onchange')

    def on_change_target_id(self, cr, uid, ids, target_id, context=None):
        values = {}
        if target_id:
            target = self.pool.get('kpi.target').browse(cr, uid, target_id, context=context)
            values = {
                'target_number': target.number,
            }
        return {'value': values}