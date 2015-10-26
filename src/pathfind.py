import subprocess

# look at the comments for the function runPathfinding(mazeName,testcases). This is what you want to call.

# Because some platforms (i.e. windows) don't accept command lengths above 32768 characters. Can set higher if you want it to run faster.
maxQuerySize = 2500

# Call this function for shortest path computation.
# (calling with a batch of testcases is faster than calling multiple time separately)
# WARNING: Be sure to compile the java files in the pathfinding/ folder first!
# javac *.java   <-- may require java 8. not sure.
#
# Input arguments:
# - mazeName: either 'floor2map' or 'floor18map'
# - testcases: a list of test cases. Each test case is a 4-tuple
#              consisting of the maze coordinates of the start/end
#              points (sx,sy,ex,ey)
# Returns:
# - a list of floats representing the shortest path distances
#              for each of the test cases.
def runPathfinding(mazeName, testcases):
    testcasesList = [testcases[i:i+maxQuerySize] for i in xrange(0,len(testcases),maxQuerySize)]
    results = []
    for chunk in testcasesList:
        results += runPathfindingChunk(mazeName, chunk)
    #print len(results)
    #print results[:10]
    #print results[-10:]
    return results


def parseTestCase(testcase):
    return '-'.join(map(str,map(int,testcase)))

def runPathfindingChunk(mazeName, testcases):
    args = [mazeName] + list(map(parseTestCase,testcases))
    args = ' '.join(args)

    output = subprocess.check_output('java Compute '+args, cwd='pathfinding', shell=False)
    return list(map(float,output.split()))
    
# Sample / test
if __name__ == '__main__':
    mazeName = 'floor18map'
    testcases = [
    (18,20,21,53),
    (18,20,21,54),
    (18,20,21,55),
    (18,20,21,56),
    ]*5000
    runPathfinding(mazeName, testcases)
    