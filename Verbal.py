from BaseAgent import BaseAgent
from random import randint
import operator

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

        # Initialize the arrays of answers and elements. Doing this in advance because
        # we know the answers and grid elements are indexed by 1..8 and A..H, respectively
        answers = []
        elements = []
        for i in range(0, self.possible_answers): answers.append(Description(""))
        for i in range(0, self.problem_elements): elements.append(Description(""))

        problem_name = "Solving %s using verbal methods with %d possible answers" % (self.problem_name, len(answers))

        self.log_section_header(problem_name)

        for this_figure in self.problem.figures:
            # Initialize some local variables
            element = False
            index = 0
            # Get the elements and answers first and assign them
            # to the right index in each of the arrays
            if ord(this_figure) in range(ord('A'), ord('Z')):
                element = True
                index = ord(this_figure) - 65
                elements[index].name = this_figure
                self.log(["Found a grid element [ index:", index, ", name:", elements[index].name, "]"])
            else:
                index = int(this_figure) - 1
                answers[index].name = this_figure
                self.log(["Found a possible answer [ index:", index, ", name:", answers[index].name, "]"])

            # Now get all the attributes for each element and answer
            figure_objects = self.problem.figures[this_figure].objects
            object_index = -1
            for figure_detail_name in figure_objects:
                these_attributes = {}
                object_index += 1
                self.log(["  Object:", figure_detail_name, ", Index: ", object_index])
                for figure_detail in figure_objects[figure_detail_name].attributes:
                    attribute = figure_objects[figure_detail_name].attributes[figure_detail]
                    these_attributes[figure_detail] = attribute
                    self.log(["   ", figure_detail, ":", attribute])
                if element:
                    elements[index].attributes.append(these_attributes)
                else:
                    answers[index].attributes.append(these_attributes)

        return self.run_comparisons(problem_name, answers, elements)

    def run_comparisons(self, problem_name, answers, elements):

        caught_error = False # If we catch an error, confidence should drop

        # Just in case we don't ever get to an answer, let's do the normal SAT out of time
        # preferred methodology...GUESS!
        answer = randint(1, self.possible_answers)

        # Using these for grid placeholders, should make it easier to read
        grid_3x3 = { "A":0, "B":1, "C":2, "D":3, "E":4, "F":5, "G":6, "H":7 }
        grid_2x2 = { "A":0, "B":1, "C":2 }


        is_2x2 = self.possible_answers == 6
        is_3x3 = self.possible_answers == 8

        if is_2x2:
            grid = grid_2x2
        elif is_3x3:
            grid = grid_3x3
        else:
            grid = None

        if is_2x2 or is_3x3:
            # Keep track of objects that must match
            must_match = {}

            attributes = []
            if is_2x2:
                for element in range(0, len(grid_2x2)):
                    attributes.append(elements[element].attributes)

                ab_equal_objects = False
                ac_equal_objects = False
                answer_objects = 0

                # Check to see how many objects are in a, b, and c and then
                # infer how many objects should be in the answer
                a_objects = attributes[grid["A"]]
                b_objects = attributes[grid["B"]]
                c_objects = attributes[grid["C"]]

                if len(a_objects) == len(b_objects): ab_equal_objects = True
                if len(a_objects) == len(c_objects): ac_equal_objects = True

                # If we have equal objects in all 3 elements, then we should
                # have the same in the answer; otherwise, if we have the same
                # number of objects in a and b, then it would serve true
                # that we would have the same number of objects in c and the answer
                if ab_equal_objects and ac_equal_objects:
                    answer_objects = len(a_objects)
                elif ab_equal_objects:
                    answer_objects = len(c_objects)

                # If we know exactly how many answers we need to look through,
                # then remove those answers that don't fit the bill
                if answer_objects > 0:
                    for this_answer in range(0, len(answers)):
                        try:
                            if len(answers[this_answer].attributes) != answer_objects:
                                del answers[this_answer]
                        except:
                            caught_error = True
                            print("Caught an error")

                # Find all the possible object descriptions
                check_matches = []
                for this_element in elements:
                    for this_object in this_element.attributes:
                        for this_key in this_object:
                            check_matches.append(this_key)
                check_matches = list(set(check_matches))

                # Iterate through all the elements to see what matches
                exact_matches = {}
                for match in check_matches:
                    for i in range(0, len(a_objects)):
                        try:
                            if a_objects[i].get(match) == b_objects[i].get(match):
                                exact_matches[match] = c_objects[i].get(match)
                        except:
                            caught_error = True
                            print("Caught an error")

                # Now look through all the answers and see if we can get a match
                answer_matches = {}
                for this_answer in answers:
                    match_count = 0
                    for this_object in this_answer.attributes:
                        perfect_match_count = len(exact_matches)
                        for match in exact_matches:
                            if match in this_object:
                                if this_object[match] == exact_matches[match]:
                                    match_count += 1
                    answer_matches[int(this_answer.name)] = match_count
                print(answer_matches)

                best_possible_score = len(exact_matches)

                # Iterate through all the answers to see if we have any perfect matches
                perfect_matches = []
                for this_match in answer_matches:
                    if answer_matches[this_match] == best_possible_score:
                        perfect_matches.append(this_match)

                # If we only have one perfect match, we're done with this problem
                if len(perfect_matches) == 1:
                    answer = perfect_matches[0]
                    print("Looks like we found a perfect match in answer", answer, "!")


            elif is_3x3:
                self.log("I can't even get 2x2 working yet :-(")

            if caught_error: answer = -1 # No confidence in errors

        return { "problem":problem_name, "value":answer }

"""





            print("Best possible score:", best_possible_score)
"""

"""

                for attribute in elements[grid["A"]].attributes[index]:
                    best_possible_score += 1
                    if is_2x2:
                        a_attr = elements[grid["A"]].attributes[0]
                        b_attr = elements[grid["B"]].attributes
                        c_attr = elements[grid["C"]].attributes
                        if a_attr == b_attr and a_attr == c_attr: must_match[attribute] = a_attr
                    elif is_3x3:
                        self.log(["Skip 3x3 for now..."])
                    else:
                        self.log(["Not sure what kind of grid, just use the guess answer..."])

                self.log(["Must match: ", must_match])

            # Let's see how many attributes of each element match
            matches = {}

            for this_answer in range(0, self.possible_answers):
                match_score = 0
                for this_attribute in answers[this_answer].attributes:
                    if this_attribute in must_match: # Make sure we only look for keys we have
                        if answers[this_answer].attributes[this_attribute] == must_match[this_attribute]: match_score += 1
                matches[this_answer] = match_score

            # Iterate through all the answers to see if we have any perfect matches
            perfect_matches = []
            for this_match in matches:
                if matches[this_match] == best_possible_score:
                    perfect_matches.append(this_match)
            # If we only have one perfect match, we're done with this problem
            if len(perfect_matches) == 1:
                answer = perfect_matches[0] + 1 # Need to +1 because the answers array is 0 based
                self.log(["Looks like we found a perfect match in answer ", answer, "!"])
"""

