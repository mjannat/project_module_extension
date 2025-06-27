# -*- coding: utf-8 -*-
from odoo.tests.common import TransactionCase

class TestProjectExtendedConfig(TransactionCase):
    def setUp(self):
        super().setUp()
        self.env = self.env(context=dict(self.env.context, tracking_disable=True))
        self.hr_department = self.env['hr.department'].create({'name': 'Test Department'})
        self.team_manager = self.env['res.users'].create({
            'name': 'Team Manager',
            'login': 'team_manager_test',
            'email': 'team_manager@test.com',
        })
        self.team_member = self.env['res.users'].create({
            'name': 'Team Member',
            'login': 'team_member_test',
            'email': 'team_member@test.com',
        })
        self.team = self.env['team.config'].create({
            'name': 'Test Team',
            'department_id': self.hr_department.id,
            'team_manager_id': self.team_manager.id,
            'team_member_ids': [(6, 0, [self.team_member.id])],
        })
        self.project = self.env['project.project'].create({
            'name': 'Test Project',
            'team_id': self.team.id,
        })

    def test_team_config_creation(self):
        self.assertEqual(self.team.name, 'Test Team')
        self.assertEqual(self.team.team_manager_id, self.team_manager)
        self.assertIn(self.team_member, self.team.team_member_ids)

    def test_project_team_assignment(self):
        self.assertEqual(self.project.team_id, self.team)
        self.assertEqual(self.project.team_manager_id, self.team_manager)
        self.assertIn(self.team_member, self.project.team_member_ids)

    def test_team_member_project_access(self):
        # Team member should see the project
        projects = self.env['project.project'].with_user(self.team_member).search([])
        self.assertIn(self.project, projects)