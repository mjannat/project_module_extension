# Project Extended Configuration

This module extends Odoo's project management with team-based access control and configuration options.

## Features

### Team-Based Project Visibility

- **Team Assignment**: Each project is assigned to a specific team
- **Access **: Projects are only visible to team members and managers

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

1. **Install the module** from the Apps menu (project_extended_config, project_task_dashboard)
   which exist in project category
2. **Create teams** via Project > Team > Team Configuration
3. **Assign team managers and members** to each team
4. **Create projects** and assign them to teams
5. **Users will automatically see only their team's projects** Team > Team Projects

## Menu Structure

- **Project > Team Configuration**: Manage teams and members
- **Project > Projects**: View projects (filtered by team access)
- **Project > Task Dashboard**: View task statistics (team-based)

## Security

The module implements record-level security rules:

- Users can only access projects where they are team members
- Team managers(Admin) can manage their all team's projects

## Technical Details

### Models

- `team.config`: Team configuration with managers and members
- `project.project`: Extended with team assignment fields

### Integration

- Works with existing project and task management
- Compatible with Odoo 16 project module
- Extends task dashboard with team-based filtering

### Additional Info

- Add the project path to the Odoo configuration file.
- Example : addons_path =
  /odoo_16/odoo_16-server/odoo/addons,/odoo_16/odoo_16-server/addons,/odoo_16/project_module_extension
- No new packages are required. Just create a virtual environment and install the Odoo 16 dependencies from
  requirements.txt, or pull the Odoo 16 image from Docker Hub.
- If you want to run unit test just type this command '-c /odoo_16/odoo.conf -d project_task_26_06_25_18_35
  --test-enable
  --init=project_extended_config' 

