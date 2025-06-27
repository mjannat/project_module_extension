# Project Extended Configuration

This module extends Odoo's project management with team-based access control and configuration options.

## Features

### Team-Based Project Visibility
- **Team Assignment**: Each project is assigned to a specific team
- **Access Control**: Projects are only visible to team members and managers
- **Role-Based Access**: Different permissions for team members vs. team managers vs. project managers

### Team Configuration
- **Team Management**: Create and manage teams with managers and members
- **Department Association**: Teams are linked to HR departments
- **System Codes**: Auto-generated unique codes for team tracking

## How It Works

### Access Control Rules
1. **Team Members**: Can only see projects where they are assigned as team members
2. **Team Managers**: Can see and manage all projects in their teams
3. **Project Managers**: Have full access to all projects (system-wide)

### Project Assignment
1. When creating a project, you must assign it to a team
2. The team manager and members are automatically linked to the project
3. Only team members and managers can access the project

### Dashboard Integration
- The task dashboard respects team-based access
- Task counts only include tasks from accessible projects
- Filters work within the user's team context

## Setup Instructions

1. **Install the module** from the Apps menu
2. **Create teams** via Project > Team Configuration
3. **Assign team managers and members** to each team
4. **Create projects** and assign them to teams
5. **Users will automatically see only their team's projects**

## Menu Structure

- **Project > Team Configuration**: Manage teams and members
- **Project > Projects**: View projects (filtered by team access)
- **Project > Task Dashboard**: View task statistics (team-based)

## Security

The module implements record-level security rules:
- Users can only access projects where they are team members
- Team managers can manage their team's projects
- Project managers retain full system access

## Technical Details

### Models
- `team.config`: Team configuration with managers and members
- `project.project`: Extended with team assignment fields

### Security Rules
- Record rules filter project access based on team membership
- Access rights are enforced at the database level

### Integration
- Works with existing project and task management
- Compatible with Odoo 16 project module
- Extends task dashboard with team-based filtering 