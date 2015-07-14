from BaseAgent import BaseAgent

class Description(object):

    def __init__(self, name):
        self.name = name
        self.attributes = []
        self.image = None

class Agent(BaseAgent):

    def solve(self):

        # Initialize some of the variables. The elements are the three or
        # eight different images that provide the key to solving the problem,
        # the answers are the six or eight possible answers

        # Initialize the arrays of answers and elements. Doing this in advance because
        # we know the answers and grid elements are indexed by 1..8 and A..H, respectively

        answers = []
        figures = []
        for i in range(0, self.possible_answers): answers.append(Description(""))
        for i in range(0, self.problem_figures): figures.append(Description(""))

        problem_name = "Solving %s using verbal methods with %d possible answers" % (self.problem_name, len(answers))

        self.log_section_header(problem_name)

        # Buffer the images
        for figure_name in self.problem.figures:
            if ord(figure_name) in range(ord('A'), ord('Z')):
                # This is a problem image
                print("Problem ", figure_name)
            else:
                # this is a potential answer
                print("Answer ", figure_name)







        return { "problem":"test", "value":-1 }