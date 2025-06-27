from odoo import http
from odoo.http import request

class ProjectTaskDashboardController(http.Controller):
    @http.route('/project_task_dashboard/task_count_by_period', auth='user', type='json')
    def task_count_by_period(self, period):
        result = request.env['project.task.dashboard'].get_task_count_by_period(period)
        return result

    @http.route('/project_task_dashboard/dashboard', auth='user', type='http')
    def dashboard_action(self, **kw):
        return request.render('project_task_dashboard.task_dashboard_template', {}) 