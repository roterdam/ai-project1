# Your Agent for solving Raven's Progressive Matrices. You MUST modify this file.
#
# You may also create and submit new files in addition to modifying this file.
#
# Make sure your file retains methods with the signatures:
# def __init__(self)
# def Solve(self,problem)
#
# These methods will be necessary for the project's main method to run.

# Install Pillow and uncomment this line to access image processing.

#from PIL import Image
from random import randint

import Verbal
import Visual

class Agent:
    # The default constructor for your Agent. Make sure to execute any
    # processing necessary before your Agent starts solving problems here.
    #
    # Do not add any variables to this signature; they will not be used by
    # main().
    def __init__(self):
        pass

    # The primary method for solving incoming Raven's Progressive Matrices.
    # For each problem, your Agent's Solve() method will be called. At the
    # conclusion of Solve(), your Agent should return an integer representing its
    # answer to the question: "1", "2", "3", "4", "5", or "6". These integers
    # are also the Names of the individual RavensFigures, obtained through
    # RavensFigure.getName() (as Strings).
    #
    # In addition to returning your answer at the end of the method, your Agent
    # may also call problem.checkAnswer(int givenAnswer). The parameter
    # passed to checkAnswer should be your Agent's current guess for the
    # problem; checkAnswer will return the correct answer to the problem. This
    # allows your Agent to check its answer. Note, however, that after your
    # agent has called checkAnswer, it will *not* be able to change its answer.
    # checkAnswer is used to allow your Agent to learn from its incorrect
    # answers; however, your Agent cannot change the answer to a question it
    # has already answered.
    #
    # If your Agent calls checkAnswer during execution of Solve, the answer it
    # returns will be ignored; otherwise, the answer returned at the end of
    # Solve will be taken as your Agent's answer to this problem.
    #
    # Make sure to return your answer *as an integer* at the end of Solve().
    # Returning your answer as a string may cause your program to crash.

    def Solve(self, problem):

        if __debug__:
            print("\n** DEBUG MODE **\n")

        verbal = Verbal.Agent(problem)
        #visual = Visual.Agent(problem)

        # Check to see the options for solving the problem
        if not problem.hasVerbal:
            # Can only solve the problem visually
            answer = None # visual.solve(problem)
        else:
            # Try and solve both visually and verbally and compare answers
            verbal_answer = verbal.solve()
            visual_answer = None # visual.solve(problem)
            if verbal_answer == visual_answer:
                answer = verbal_answer
            else:
                # Figure out how to compare the two and decide on the best
                answer = verbal_answer # <-- PLACEHOLDER


        # The answer that comes back is a list with two values,
        # the name of the problem and the value of the answer

        # Check to see if we got the right answer
        right_answer = problem.checkAnswer(answer["value"])

        if answer["value"] == right_answer:
            print("\nI got it right! Thanks for teaching me so good!")
        else:
            print("\nUgh...my answer is %d and the right answer is %d" % (answer["value"], right_answer))

        return int(answer["value"])