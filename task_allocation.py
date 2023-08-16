from utility import Utility

TEAM_COUNT = 4
MAX_HOURS_PER_WEEK = 40

class Team:
    def __init__(self, name):
        self.name = name
        self.members = []

    def add_member(self, member):
        self.members.append(member)

class TeamMember:
    def __init__(self, name, role, productivity):
        self.name = name
        self.role = role
        self.productivity = productivity
        self.available_hours = MAX_HOURS_PER_WEEK  # Default weekly availability

class Task:
    def __init__(self, name, project_type, hours_required, priority):
        self.name = name
        self.project_type = project_type
        self.hours_required = hours_required
        self.priority = priority

class TaskAllocationSystem:
    def __init__(self):
        self.team_members = []
        self.tasks = []

    def add_team_member(self, member):
        self.team_members.append(member)

    def add_task(self, task):
        self.tasks.append(task)

    def allocate_tasks_to_teams(self):
        utility = Utility()
        teams = [Team(f"Team {i}") for i in range(1, TEAM_COUNT + 1)]
        teams = utility.team_creation(teams, self.team_members)
        
        for team in teams:
            print(f"\nAllocating tasks for {team.name}:")
            team_members = team.members
            flag_no_members_available = False
            for task in self.tasks:
                while task.hours_required:
                    available_team_members = [member for member in team_members if member.available_hours > 0]
                    if not available_team_members:
                        print(f"No available team members for task: {task.name} in {team.name}")
                        flag_no_members_available = True
                        break
                    available_team_members.sort(key=lambda x: x.productivity, reverse=True)
                    chosen_member = available_team_members[0]
                    
                    hours_allocated = min(task.hours_required, chosen_member.available_hours)
                    chosen_member.available_hours -= hours_allocated
                    
                    # print(f"Task: {task.name} -> Assigned to: {chosen_member.name} ({chosen_member.role}) in {team.name}")
                    # print(f"   Hours Allocated: {hours_allocated}\n")
                    output = [[task.name, chosen_member.name, chosen_member.role, team.name, hours_allocated]]
                    utility.write_to_csv(output)
                    task.hours_required -=hours_allocated
                if flag_no_members_available:
                    break

                    
if __name__ == "__main__":
    team_allocation_system = TaskAllocationSystem()
    utility = Utility()

    manager = TeamMember("Manager", "Manager", 1.0)
    team_allocation_system.add_team_member(manager)

    # List comprehension
    team_leads = [
        TeamMember(f"Lead {i}", "Team Lead", 0.5) 
        for i in range(1, TEAM_COUNT + 1)
    ]

    for lead in team_leads:
        team_allocation_system.add_team_member(lead)

    senior_engineers = [
        TeamMember(f"Senior {i}", "Senior Engineer", 2.0)
        for i in range(1, 16)
    ]
    for senior in senior_engineers:
        team_allocation_system.add_team_member(senior)

    junior_engineers = [
        TeamMember(f"Junior {i}", "Junior Engineer", 1.0)
        for i in range(1, 26)
    ]
    for junior in junior_engineers:
        team_allocation_system.add_team_member(junior)  

    # add tasks 
    tasks = [
        Task(f"High Priority Task {i}", "High Priority", 80, 2) for i in range(1, 11)
    ] + [
        Task(f"Urgent Task {i}", "Urgent", 40, 1) for i in range(11, 31)
    ] + [
        Task(f"Long Term Task {i}", "Long Term", 160, 3) for i in range(31, 50)
    ]

    tasks.sort(key= lambda task: task.priority)
    for task in tasks:
        team_allocation_system.add_task(task)

    utility.delete_old_csv()
    team_allocation_system.allocate_tasks_to_teams()
    utility.csv_to_excel()
    utility.plot_graph()

