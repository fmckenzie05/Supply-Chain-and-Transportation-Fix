# Team-Based Organizational Structure for Delivering Products or Services

class Team:
    def __init__(self, name, members):
        self.name = name
        self.members = members

    def solve_problem(self, problem):
        """Solves a problem by having team members work together."""
        print(f'{self.name} team solving problem: {problem}')
        for member in self.members:
            member.contribute_to_solution()

    def make_decision(self, decision):
        """Makes a decision by having team members discuss and come to a consensus."""
        print(f'{self.name} team making decision: {decision}')
        for member in self.members:
            member.provide_input()

class TeamMember:
    def __init__(self, name):
        self.name = name

    def contribute_to_solution(self):
        """Contributes to the team's solution to a problem."""
        print(f'{self.name} contributing to solution')

    def provide_input(self):
        """Provides input to the team during decision-making."""
        print(f'{self.name} providing input')

# Test the Team and TeamMember classes
team = Team('Product Development', [
    TeamMember('Alice'),
    TeamMember('Bob'),
    TeamMember('Charlie'),
])

# Have the team solve a problem
team.solve_problem('how to improve product performance')

# Have the team make a decision
team.make_decision('should we add a new feature to the product?')

