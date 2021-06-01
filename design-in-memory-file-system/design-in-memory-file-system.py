from collections import defaultdict
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