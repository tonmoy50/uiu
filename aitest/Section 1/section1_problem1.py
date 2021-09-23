class Node:
    def __init__(self):
        self.name = ""  #name of the container
        self.data = ""  #raw html data of the container
        self.isleaf = False     #check for whether a container is a node or leaf_node
        self.leafs = []
    
    def GetInnerHTML(self):
        if self.isleaf:
            return self.data
        else:
            return self.leafs
    
    def GetHTML(self):
        datas = [i for i in self.leafs[i].data]
        return datas


class Container:
    def __init__(self):
        self.nodes = []
    
    def AddNode(self):
        objects = Node()
        objects.data = input()
        temp_isleaf = int(input() )
        if(temp_isleaf == 1):
            objects.isleaf = True
        else:
            objects.isleaf = False
            number_of_leaves = int( input() )
            for i in range(number_of_leaves):
                new_object = Node()
                objects.leafs.append(new_object)
            
        

        self.nodes.append( objects )

    
    def RemoveNode(self, node):
        self.nodes.remove(node)
    

def main():
    obj1 = Container()
    obj1.AddNode()
    

if __name__ == "__main__":
    main()

