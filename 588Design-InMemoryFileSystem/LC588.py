from collections import defaultdict
# Tree Node (each node has content and child node)
class Node:
    def __init__(self):
        self.child = defaultdict(Node)
        self.content = ""
class FileSystem:

    def __init__(self):
        self.root = Node()
    
    def find(self, path:str, create:bool):
        curr = self.root
        if len(path) == 1:
            return self.root
        #print(path.split("/"))
        for word in path.split("/")[1:]:
            if not curr.child.get(word) and not create:
                return None
            curr = curr.child[word]
        return curr

    def ls(self, path: str) -> List[str]:
        curr = self.find(path, False)
        if curr.content:
            return [path.split("/")[-1]]
        return sorted(curr.child.keys());
        

    def mkdir(self, path: str) -> None:
        self.find(path, True)

    def addContentToFile(self, filePath: str, content: str) -> None:
        curr = self.find(filePath, True)
        curr.content += content

    def readContentFromFile(self, filePath: str) -> str:
        curr = self.find(filePath, False)
        return curr.content


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)

# The time complexity of executing an ls command is O\big(m+n+klog(k)\big)O(m+n+klog(k)). Here, m refers to the length of the input string. We need to scan the input string once to split it and determine the various levels. n refers to the depth of the last directory level in the given input for ls. This factor is taken because we need to enter n levels of the tree structure to reach the last level. k refers to the number of entries(files+subdirectories) in the last level directory(in the current input). We need to sort these names giving a factor of klog(k).

# other functions TC is O(M + N)