# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class TeamConfig(models.Model):
    """
    Model for managing team configurations within a project or department.

    Features:
    - Associates a team with a department, team manager, and members.
    - Auto-generates a unique system code using a sequence.
    - Supports chatter (tracking) and portal access.
    """
    _name = 'team.config'
    _description = 'Project Team Configuration'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(
        string='Team Name',
        required=True,
        help='Name of the team configuration'
    )
    department_id = fields.Many2one(
        'hr.department',
        string='Department',
        required=True,
        help='Department to which the team belongs'
    )
    team_manager_id = fields.Many2one(
        'res.users',
        string='Team Manager',
        required=True,
        tracking=True,
        help='Employee assigned as the team manager'
    )
    system_code = fields.Char(
        string='System Code',
        required=False,
        copy=False,
        readonly=True,
        help='Unique system code generated for internal tracking'
    )
    company_id = fields.Many2one(
        'res.company',
        string='Company',
        default=lambda self: self.env.company,
        tracking=True,
        help='Company associated with this team'
    )
    team_member_ids = fields.Many2many(
        'res.users',
        string='Team Members',
        help='Employees assigned as members of the team'
    )

    @api.model
    def create(self, vals):
        """
        Overrides the default create method to auto-generate a system code.
        """
        if not vals.get('system_code'):
            vals['system_code'] = self.env['ir.sequence'].next_by_code('team.config.sequence') or _('New')
        return super().create(vals)
