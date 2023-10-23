#!/usr/bin/python3
"""
A Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""


class EmployeeData:
    __name = ""
    __no_of_completed_tasks = 0
    __no_of_total_tasks = 0
    __completed_tasks = []
    __uncompleted_tasks = []
    __userId = 0

    def __init__(self, userID):
        self.userID = userID

    @property
    def completed_tasks(self):
        return self.__completed_tasks

    @completed_tasks.setter
    def completed_tasks(self, values):
        self.__completed_tasks = values

    @property
    def no_of_completed_tasks(self):
        return self.__no_of_completed_tasks

    @no_of_completed_tasks.setter
    def no_of_completed_tasks(self, value):
        self.__no_of_completed_tasks = value

    @property
    def no_of_total_tasks(self):
        return self.__no_of_total_tasks

    @no_of_total_tasks.setter
    def no_of_total_tasks(self, value):
        self.__no_of_total_tasks = value

    @property
    def userID(self):
        return self.__userId

    @userID.setter
    def userID(self, value):
        self.__userId = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    def getemployee(self):
        reqst = requests.get(
            "https://jsonplaceholder.typicode.com/users?id={}".format(
                self.__userId))
        json_d = reqst.json()
        self.name = json_d[0]['name']

    def getdata(self):
        reqst = requests.get(
            "https://jsonplaceholder.typicode.com/todos?userId={}".format(
                self.__userId))
        json_d = reqst.json()
        for item in json_d:
            if item['completed'] is True:
                self.completed_tasks.append(item['title'])
            else:
                self.__uncompleted_tasks.append(item['title'])

    def get_figures(self):
        self.no_of_completed_tasks = len(self.__completed_tasks)
        self.no_of_total_tasks = len(self.__completed_tasks
                                     ) + len(self.__uncompleted_tasks)

    def get_employee_details(self):
        self.getemployee()
        self.getdata()
        self.get_figures()


if __name__ == "__main__":
    import requests
    from sys import argv

    employee = EmployeeData(argv[1])
    employee.get_employee_details()
    print("Employee {} is done with tasks({}/{}):".format(
        employee.name,
        employee.no_of_completed_tasks,
        employee.no_of_total_tasks)
          )
    for completed_tasks in employee.completed_tasks:
        print("\t {}".format(completed_tasks))
