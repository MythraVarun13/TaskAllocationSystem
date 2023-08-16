import random
import csv
import os
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from collections import defaultdict


class Utility:
    def __init__(self):
        pass

    def display_members(self, members):
        for member in members:
            print(member.name, member.role)
    
    def team_creation(self, teams, team_members):
        weights = [0.4, 0.2, 0.3, 0.1]  # These are the weights corresponding to each option
        members_to_include = [member for member in team_members if member.role != 'Team Lead' and member.role !='Manager']
        members_team_lead = [member for member in team_members if member.role == 'Team Lead']
        # self.display_members(members_to_include)

        for team in teams:
            if members_team_lead:
                lead = random.choice(members_team_lead)
                team.add_member(lead)
                members_team_lead.remove(lead)

        for member in members_to_include:
            team = random.choices(teams, weights=weights, k=1)[0]
            team.add_member(member)

        return teams

    def delete_old_csv(self):
        file_name = 'allocated_tasks.csv'
        if os.path.exists(file_name):
            os.remove(file_name)
            print(f'Old CSV file "{file_name}" has been deleted')

    def write_to_csv(self, data):
        file_name = 'allocated_tasks.csv'
        # Open the file in write mode and create a CSV writer
        file_exists = os.path.exists(file_name)
        with open(file_name, mode='a', newline='') as file:
            writer = csv.writer(file)

            if not file_exists:
                writer.writerow(['Task Name', 'Chosen Member Name', 'Chosen Member Role', 'Team Name', 'Hours Allocated'])

            # Write the data to the CSV file
            writer.writerows(data)

    def csv_to_excel(self):
        # Read the CSV file into a pandas DataFrame
        csv_file = 'allocated_tasks.csv'
        data = pd.read_csv(csv_file)

        # Specify the Excel file name
        excel_file = 'allocated_tasks.xlsx'

        # Convert and save the DataFrame to an Excel file
        data.to_excel(excel_file, index=False)

        print(f'CSV file "{csv_file}" has been converted to Excel file "{excel_file}"')

    def plot_graph(self):
        
        file_name = 'allocated_tasks.csv'
        # Read CSV data and extract relevant information
        team_hours = defaultdict(int)

        with open(file_name, mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            for row in reader:
                team_name = row[3]
                hours_allocated = int(row[4])
                team_hours[team_name] += hours_allocated

        # Create a bar graph showing total hours allocated to each team
        teams = list(team_hours.keys())
        hours = list(team_hours.values())

        plt.bar(teams, hours)
        plt.xlabel('Team Name')
        plt.ylabel('Total Hours Allocated')
        plt.title('Total Hours Allocated to Each Team')
        plt.tight_layout()
        plt.savefig("work_allocated_bar_graph.png")
        # plt.show()
