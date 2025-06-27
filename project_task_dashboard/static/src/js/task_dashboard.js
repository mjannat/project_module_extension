odoo.define('project_task_dashboard.TaskDashboard', function(require) {
    "use strict";
    var AbstractAction = require('web.AbstractAction');
    var core = require('web.core');
    var QWeb = core.qweb;
    var ajax = require('web.ajax');

    var TaskDashboard = AbstractAction.extend({
        template: 'ProjectTaskDashboard',
        events: {
            'click .ptd-task-filter-btn': '_onTaskFilterClick',
        },
        start: function() {
            this._super.apply(this, arguments);
            this._setDefaultTaskFilter();
        },
        _setDefaultTaskFilter: function() {
            var self = this;
            this._fetchTaskCountByPeriod('this_month');
            setTimeout(function() {
                self.$('.ptd-task-filter-btn').removeClass('active btn-success').addClass('btn-primary btn-secondary');
                self.$('.ptd-task-filter-btn[data-period="this_month"]').addClass('active btn-success').removeClass('btn-primary btn-secondary');
            }, 100);
        },
        _onTaskFilterClick: function(ev) {
            var $btn = $(ev.currentTarget);
            var period = $btn.data('period');
            this._fetchTaskCountByPeriod(period);
            this.$('.ptd-task-filter-btn').removeClass('active btn-success').addClass('btn-primary btn-secondary');
            $btn.addClass('active btn-success').removeClass('btn-primary btn-secondary');
        },
        _fetchTaskCountByPeriod: function(period) {
            ajax.jsonRpc('/project_task_dashboard/task_count_by_period', 'call', {period: period}).then(function(data) {
                document.getElementById('ptd_total_tasks').innerHTML = data.count;
            });
        },
    });
    core.action_registry.add('project_task_dashboard_action', TaskDashboard);
    return TaskDashboard;
}); 