from odoo import api, models
from datetime import date, timedelta
from dateutil.relativedelta import relativedelta

class ProjectTaskDashboard(models.AbstractModel):
    _name = 'project.task.dashboard'
    _description = 'Project Task Dashboard Helper'

    @api.model
    def get_task_count_by_period(self, period):
        today = date.today()
        if period == 'this_week':
            start = today - timedelta(days=today.weekday())
            end = start + timedelta(days=6)
        elif period == 'this_month':
            start = today.replace(day=1)
            end = (start + relativedelta(months=1)) - timedelta(days=1)
        elif period == 'prev_week':
            end = today - timedelta(days=today.weekday() + 1)
            start = end - timedelta(days=6)
        elif period == 'prev_month':
            first_this_month = today.replace(day=1)
            end = first_this_month - timedelta(days=1)
            start = end.replace(day=1)
        else:
            return {'count': 0}
        
        # Get user's accessible projects based on team membership
        accessible_projects = self.env['project.project'].get_user_accessible_projects()
        
        # Count tasks from accessible projects only
        domain = [
            ('create_date', '>=', start), 
            ('create_date', '<=', end),
            ('project_id', 'in', accessible_projects.ids)
        ]
        count = self.env['project.task'].search_count(domain)
        return {'count': count} 