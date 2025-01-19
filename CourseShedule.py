from collections import deque


def courseShedule(prerequisites, numCourses):

    # first create a list for source and sink if there is depedency of A to B it means B is source and A is sink
    inlets = [set() for _ in range(numCourses)]
    outlet = [set() for _ in range(numCourses)]

    for course in prerequisites:
        outlet[course[0]].add(course[1])
        inlets[course[1]].add(course[0])

    queue = deque()
    #identify nodes which have 0 depedencies meaning in they have 0 outlets
    sorted = []
    for i in range(numCourses):
        if len(outlet[i]) == 0:
            queue.append(i)

    # pull these nodes from queues one by one which have 0 outlets. visited all sublings abd remove their connections to 0 outlet nodes and check again if condition is met
    visited = [False] * numCourses
    while queue:
        size = len(queue)
        for _ in range(size):
            course = queue.popleft()
            visited[course]=True
            sorted.append(course)
            #from inlet
            inletCourses = inlets[course]
            for inlet in inletCourses:
                #remove course
                outlet[inlet].remove(course)
                if len(outlet[inlet]) == 0 and not visited[inlet]:
                    queue.append(inlet)
    if len(sorted) == numCourses:
        return True
    else:
        return False

def main():
    numCourses = 4
    prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
    possible = courseShedule(prerequisites, numCourses)
    print("if course schedule is possible" + str(possible))

    numCourses = 3
    prerequisites = [[0, 1], [1, 2], [2, 0]]
    possible = courseShedule(prerequisites, numCourses)
    print("if course schedule is possible" + str(possible))
main()