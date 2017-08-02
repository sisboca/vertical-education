# -*- coding: utf-8 -*-
# Copyright 2009-TODAY Tech-Receptives(<http://www.techreceptives.com>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html)

from odoo import models, fields


class EducationCategory(models.Model):
    _name = 'education.category'

    name = fields.Char('Name', size=256, required=True)
    code = fields.Char('Code', size=4, required=True)