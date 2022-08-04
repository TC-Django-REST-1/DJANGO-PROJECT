# Organizations tasks management

## Idea:
A system for managing the tasks of the organizations and its staff, while providing the most important features of the treatment

## Inspiration:
Facilitate the process of managing tasks and assigning them to the right people


## List of Services / Features:

- Possibility to divide employees into teams
- Possibility to view all employees
- Possibility to display employees of a particular team
- The possibility of assigning a status to the task (completed, todo, in_progress)
- View all tasks and filter by status
- View the tasks of a specific team
- Submit review requests to the team manager
- Review the requests by team manager


## Users
All types of users can have one or more of the same type in the same organization or team.<br>
**That means**
- It is **not possible** to create a team that does not have a manager
- It is **not possible** to create a team that does not contain an employees

> Note
- When you delete an organization, everything belonging to it will be erased
- When an employee is deleted, he will not be deleted from the tasks he was in, but only his account status will be changed, but he will be erased from the teams in which he was
- When a team is deleted, its members will not be erased, and the tasks it has accomplished will not be deleted, but only the team's status will be changed
- When you delete a task, it will be erased only

### Organization supervisor
- Possibility to edit, delete the organization
- Add, delete, edit employees
- Add, delete, edit teams
- Add, delete, edit tasks

### Team Manager
- Add, delete members on the team
- Assign, remove assignments task to specific people on the team
- Change the status of the task
- Review the tasks

### Team member
- Request the manager to review a task
