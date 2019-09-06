'''
receives map, src, dest. 
returns dist and path.
'''
import unittest


def dijkstraUtil(mp, src, dest, visited=[], prevs={}, dists={}):
    #sanity check
    if not mp or src not in mp or dest not in mp:
        return {"message": "something wrong from dijkstra."}

    #if initial run, initiate values
    if not visited:
        dists[src] = 0
    
    #base case  = end condition
    if src == dest:
        if dest not in dists:
                return {"message": "cannot find such path"}
        path = []
        curr_node = dest
        while curr_node:
            path.insert(0, curr_node)
            curr_node = prevs.get(curr_node, None)
        return {"distance": float(dists[dest]), "path": path}

    #iterate the neighbors,and append prevs
    for neighbor in mp[src]:
        new_dist = dists[src] + mp[src][neighbor]
        if new_dist < dists.get(neighbor, float('INF')):
            dists[neighbor] = new_dist
            prevs[neighbor] = src
    # then check this src visited
    visited.append(src)

    #pick new src, then recur.
    unvisited = {}
    for k in mp:
        if k not in visited:
            unvisited[k] = dists.get(k, float('INF'))
    nxt = min(unvisited, key=unvisited.get)

    return dijkstraUtil(mp, nxt, dest, visited, prevs, dists)


def dijkstra(mp, src, dest):
    res = dijkstraUtil(mp, src, dest, [], {}, {})
    return res

class Test(unittest.TestCase):

    def test_dijkstra(self):
        redmond = {
            "a": {"b": 2, "c": 5},
            "b": {"c": 2},
            "c": {"a": 8}
        }
        seattle = {
            "a": {"b": 1},
            "b": {"a": 2},
            "c": {"d": 3},
            "d": {"c": 4}
        }

        print(dijkstra(redmond, 'b', 'a'))
        
        


if __name__ == "__main__":
    unittest.main()
