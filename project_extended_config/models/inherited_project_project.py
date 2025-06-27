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

    #
    # @api.model
    # def get_user_accessible_projects(self):
    #     """
    #     Get projects accessible to the current user based on team membership.
    #     Returns a recordset of projects the user can access.
    #     """
    #     user = self.env.user
    #     if user.has_group('project.group_project_manager'):
    #         # Project managers can see all projects
    #         return self.search([])
    #     else:
    #         # Regular users can only see projects where they are team members
    #         return self.search([('team_member_ids', 'in', user.id)])
    #
    # @api.model
    # def get_user_team_projects(self):
    #     """
    #     Get projects where the current user is a team member or manager.
    #     Returns a recordset of projects.
    #     """
    #     user = self.env.user
    #     if user.has_group('project.group_project_manager'):
    #         # Project managers can see all projects
    #         return self.search([])
    #     else:
    #         # Regular users can see projects where they are team members or managers
    #         return self.search([
    #             '|',
    #             ('team_member_ids', 'in', user.id),
    #             ('team_manager_id', '=', user.id)
    #         ])
    #
    # def check_user_access(self, user=None):
    #     """
    #     Check if a user has access to this project.
    #     Returns True if user has access, False otherwise.
    #     """
    #     if not user:
    #         user = self.env.user
    #
    #     if user.has_group('project.group_project_manager'):
    #         return True
    #
    #     return user.id in self.team_member_ids.ids or user.id == self.team_manager_id.id
