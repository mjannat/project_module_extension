from odoo import fields, models, api, _
from odoo.exceptions import ValidationError


class InheritProject(models.Model):
    _inherit = 'project.project'
    _description = 'Team Configuration for Project'

    # Link each project to a team configuration (required field)
    team_id = fields.Many2one(
        'team.config',
        string='Team Configuration',
        ondelete='cascade',
        required=True,
        tracking=True,
        help='Select the team responsible for this project.'
    )

    # Optional link to the team manager (user)
    team_manager_id = fields.Many2one(
        'res.users',
        string='Team Manager',
        ondelete='cascade',
        tracking=True,
        related='team_id.team_manager_id',
        help='User assigned as the team manager'
    )

    # List of team members assigned to this project
    team_member_ids = fields.Many2many(
        'res.users',
        string='Team Members',
        ondelete='cascade',
        tracking=True,
        related='team_id.team_member_ids',
        help='Users assigned as members of this project team.'
    )
