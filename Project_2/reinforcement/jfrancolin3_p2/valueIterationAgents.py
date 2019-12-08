# valueIterationAgents.py
# -----------------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


import mdp, util
# import pdb

from learningAgents import ValueEstimationAgent

class ValueIterationAgent(ValueEstimationAgent):
    """
        * Please read learningAgents.py before reading this.*

        A ValueIterationAgent takes a Markov decision process
        (see mdp.py) on initialization and runs value iteration
        for a given number of iterations using the supplied
        discount factor.
    """
    def __init__(self, mdp, discount = 0.9, iterations = 100):
        """
          Your value iteration agent should take an mdp on
          construction, run the indicated number of iterations
          and then act according to the resulting policy.

          Some useful mdp methods you will use:
              mdp.getStates()
              mdp.getPossibleActions(state)
              mdp.getTransitionStatesAndProbs(state, action)
              mdp.getReward(state)
              mdp.isTerminal(state)
        """
        self.mdp = mdp
        self.discount = discount
        self.iterations = iterations
        self.values = util.Counter()

        # Write value iteration code here
        "*** YOUR CODE HERE ***"

        # repeat process iterations number of times
        for iteration in range(iterations):

            # create a copy of the dictionary values
            # we want to ensure consistent updates through iterations
            new_values = self.values.copy()

            # iterate dictionary all states
            for state in mdp.getStates():

                # get value for best possible action
                actions = mdp.getPossibleActions(state)

                # compute q_values for a state given an action
                q_value = []
                for action in actions:
                    q_value.append(self.getQValue(state, action))

                # update state utility based on max possible q_value
                if len(q_value) >= 1:
                    new_values[state] = max(q_value)

            # update the state of the grid
            self.values = new_values


    def getValue(self, state):
        """
          Return the value of the state (computed in __init__).
        """
        return self.values[state]


    def computeQValueFromValues(self, state, action):
        """
          Compute the Q-value of action in state from the
          value function stored in self.values.
        """
        "*** YOUR CODE HERE ***"

        # initialyze q_value
        q_value = 0.0

        # get all possible transitions from a given state and action
        transitions = self.mdp.getTransitionStatesAndProbs(state, action)

        # iterate through possible transitions
        for ii in range(len(transitions)):

            # unpack a tuple
            next_state, probability = transitions[ii]

            # get action reward
            reward = self.mdp.getReward(state, action, next_state)

            # consider the discount rate
            future_value = self.discount * self.values[next_state]

            # bellman update
            q_update = probability * (reward + future_value)

            # incremment q_value
            q_value = q_value + q_update

        return q_value


    def computeActionFromValues(self, state):
        """
          The policy is the best action in the given state
          according to the values currently stored in self.values.

          You may break ties any way you see fit.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return None.
        """
        "*** YOUR CODE HERE ***"

        # initialyze relevant variables
        optimum_action = None
        optimum_q_value = float('-inf')

        # get list of possible actions
        actions = self.mdp.getPossibleActions(state)

        # iterate through all actions
        for action in actions:

            # get q_value for a given action
            q_value = self.getQValue(state, action)

            # update optimum_action according to q_value found
            if q_value > optimum_q_value:
                optimum_q_value = q_value
                optimum_action = action

        # pdb.set_trace()
        return optimum_action


    def getPolicy(self, state):
        return self.computeActionFromValues(state)

    def getAction(self, state):
        "Returns the policy at the state (no exploration)."
        return self.computeActionFromValues(state)

    def getQValue(self, state, action):
        return self.computeQValueFromValues(state, action)
