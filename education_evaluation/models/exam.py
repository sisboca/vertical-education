# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from openerp import models, api, fields, _


class EducationExam(models.Model):
    _name = 'education.exam'

    name = fields.Char(
        string='Name',
        compute='_compute_name', readonly=True)

    state = fields.Selection(
        [('draft', 'Draft'),
         ('planned', 'Planned'),
         ('done', 'Done')],
        string='Status',
        default="draft")

    group_id = fields.Many2one(
        comodel_name='education.group',
        string='Group')

    subject_id = fields.Many2one(
        comodel_name='education.subject',
        string='Subject')

    result_ids = fields.One2many(
        comodel_name='education.result',
        inverse_name='exam_id',
        string='Results')

    date = fields.Date(
        string='Date')

    @api.multi
    def _compute_name(self):
        for record in self:
            record.name = record.group_id.code + \
                '/' + record.subject_id.name + '/' + record.date

    @api.multi
    def set_planned(self):
        self.state = 'planned'

    @api.multi
    def set_done(self):
        self.state = 'done'