The Task Allocation System is a Python program that allocates tasks to teams of engineers. The program takes into account the skills of the engineers, the priority of the tasks, and the availability of the engineers.

The program is divided into two parts: the task allocation algorithm and the utility functions. The task allocation algorithm is responsible for assigning tasks to teams, while the utility functions are responsible for tasks such as creating teams, writing data to a CSV file, and plotting a graph.

The task allocation algorithm works by first creating a list of all the tasks and all the engineers. The tasks are then sorted by priority, and the engineers are sorted by their productivity. The algorithm then iterates through the tasks, assigning them to teams one by one. For each task, the algorithm finds the team with the most available hours and assigns the task to that team. If there is no team with enough available hours, the task is assigned to the team with the highest priority.

The utility functions are responsible for tasks such as creating teams, writing data to a CSV file, and plotting a graph. The `team_creation` function creates a list of teams, where each team has a team lead and a number of engineers. The `delete_old_csv` function deletes an existing CSV file if it exists. The `write_to_csv` function writes data to a CSV file. The `csv_to_excel` function converts a CSV file to an Excel file. The `plot_graph` function plots a bar graph showing the total hours allocated to each team.

Clone the repository to your local machine.
To run the Task Allocation System, you will need to install Python and the following Python packages: `pandas`, `matplotlib`, and `csv`. Once you have installed the required packages, you can run the program by executing the following command:

```
python task_allocation.py
```

The program will then allocate the tasks to the teams and generate a CSV file and an Excel file. The CSV file will contain the task name, the engineer name, the engineer role, the team name, and the number of hours allocated. The Excel file will contain the same information as the CSV file, but it will also include a bar graph showing the total hours allocated to each team.

I hope this README file has been helpful. Please let me know if you have any questions