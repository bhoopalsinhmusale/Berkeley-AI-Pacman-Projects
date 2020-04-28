# search.py
# ---------
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


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    startState=problem.getStartState()
    fringe=util.Stack()
    explored=set()
    fringe.push((startState,[],0))
    while not fringe.isEmpty():
        (currentNode, visitedPath, currentCost)=fringe.pop()
       
        if problem.isGoalState(currentNode):
            return visitedPath
        
        if currentNode not in explored:
            explored.add(currentNode)            
            successors=problem.getSuccessors(currentNode)        
            for state,direction,cost in successors:
                fringe.push([state,visitedPath+[direction],cost])
    
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    initialState = problem.getStartState()
    queue = util.Queue()
    #push the initial state as (x,y) coordinates and an empty list of actions.
    queue.push((initialState,[]))
    
    visitedNodes = []
    
    while not queue.isEmpty():
        
        (currentNode , visitedPath) = queue.pop()
        
        #if the current node/(x,y)coordinate is the final goal state, then return the visited path.
        if problem.isGoalState(currentNode):
            return visitedPath
        
        if currentNode not in visitedNodes:
            visitedNodes.append(currentNode)
            neighbours = problem.getSuccessors(currentNode)
            for nextPossibleState , direction , cost in neighbours:
                queue.push((nextPossibleState, visitedPath + [direction]))
    
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"    
    
    def getLeastCost(tuple):
        return tuple[-1][2]
    
    priorityQueue = util.PriorityQueueWithFunction(getLeastCost)
    
    initialState = problem.getStartState()
    priorityQueue.push([(initialState,[],0)])
    
    visitedNodes = []
    
    while not priorityQueue.isEmpty():
        
        currentList = priorityQueue.pop()
        
        #if the current node/(x,y)coordinate is the final goal state, then return the visited path.
        if problem.isGoalState(currentList[-1][0]):
            return currentList[-1][1]
        
        if currentList[-1][0] not in visitedNodes:
            visitedNodes.append(currentList[-1][0])
            neighbours = problem.getSuccessors(currentList[-1][0])
            for nextPossibleState , direction , cost in neighbours:
                priorityQueue.push([(nextPossibleState, currentList[-1][1] + [direction], currentList[-1][2] +cost )])
    
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    def getLeastCost(tuple):
        return tuple[-1][2]+heuristic(tuple[-1][0],problem)
    
    priorityQueue = util.PriorityQueueWithFunction(getLeastCost)
    
    initialState = problem.getStartState()
    priorityQueue.push([(initialState,[],0)])
    
    visitedNodes = []
    
    while not priorityQueue.isEmpty():
        
        currentList = priorityQueue.pop()
        
        #if the current node/(x,y)coordinate is the final goal state, then return the visited path.
        if problem.isGoalState(currentList[-1][0]):
            return currentList[-1][1]
        
        if currentList[-1][0] not in visitedNodes:
            visitedNodes.append(currentList[-1][0])
            neighbours = problem.getSuccessors(currentList[-1][0])
            for nextPossibleState , direction , cost in neighbours:
                priorityQueue.push([(nextPossibleState, currentList[-1][1] + [direction], currentList[-1][2] +cost )])
    
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
