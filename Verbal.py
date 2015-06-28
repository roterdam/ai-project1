from BaseAgent import BaseAgent
from RavensFigure import RavensFigure
from RavensProblem import RavensProblem

class Attribute(object):

    def __init__(self, attribute, value):
        self.attribute = attribute
        self.value = value


class Description(object):

    def __init__(self, name):
        self.name = name
        self.attributes = []

class Agent(BaseAgent):

    def solve(self):

        # It's been way too long away from coding, this is just ugly :-(

        # Initialize some of the variables. The elements are the three or
        # eight different images that provide the key to solving the problem,
        # the answers are the six or eight possible answers

        # Intialize the arrays of answers and elements. Doing this in advance because
        # we know the answers and grid elements are indexed by 1..8 and A..H, respectively
        answers = []
        elements = []
        for i in range(0, self.possible_answers): answers.append(Description(""))
        for i in range(0, self.problem_elements): elements.append(Description(""))

        # This was  agood learning moment, if you initialize thinking you're going to
        # have three different Description objects for answers, you're actually assigning
        # the same memory address!!!  WTF????
        #answers = [Description("")] * self.possible_answers
        #elements = [Description("")] * self.problem_elements

        self.print_section_header("Solving %s using verbal methods with %d possible answers" % (self.problem_name, len(answers)))

        for this_figure in self.problem.figures:
            # Get the elements and answers first and assign them
            # to the right index in each of the arrays
            if ord(this_figure) in range(ord('A'), ord('Z')):
                index = ord(this_figure) - 65
                elements[index].name = this_figure
                print("Found a grid element [index:", index, ", name:", elements[index].name, "]")
            else:
                index = int(this_figure) - 1
                answers[index].name = this_figure
                print("Found a possible answer [index:", index, ", name:", answers[index].name, "]")


            # Now get all the attributes for each element and answer
            figure_objects = self.problem.figures[this_figure].objects
            for figure_detail_name in figure_objects:
                print("  Object: ", figure_detail_name)
                for figure_detail in figure_objects[figure_detail_name].attributes:
                    print("    ", figure_detail, ":", figure_objects[figure_detail_name].attributes[figure_detail])



        return -1