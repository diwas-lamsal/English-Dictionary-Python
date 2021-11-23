# import global_variables as gb

# Some references from https://favtutor.com/blogs/doubly-linked-list-python
# -------------------------------------------------------------------------------------

class Node:
    def __init__(self, data):
        self.item = data
        self.next = None
        self.prev = None


# -------------------------------------------------------------------------------------
class DoublyLinkedList:
    def __init__(self):
        self.start_node = None

    # -------------------------------------------------------------------------------------

    def Insert(self, word, type, meaning):
        if self.start_node is None:
            new_node = Node([word, [type, meaning]])
            self.start_node = new_node
            return
        n = self.start_node
        while n is not None:
            # If the word is equal to n (already exists)
            if n.item[0].casefold() == word.casefold():
                n.item.append([type, meaning])
                return
            # If the word is smaller than n
            if n.item[0].casefold() > word.casefold():
                new_node = Node([word, [type, meaning]])
                # If n was the first element of the list
                if n == self.start_node:
                    self.start_node = new_node
                else:
                    n.prev.next = new_node
                    new_node.prev = n.prev
                n.prev = new_node
                new_node.next = n
                return
            # If reached the end, insert at the end
            if (n.next == None):
                new_node = Node([word, [type, meaning]])
                n.next = new_node
                new_node.prev = n
                return
            n = n.next

    # -------------------------------------------------------------------------------------

    # Delete word
    def Delete(self, word):
        found = False
        if self.start_node is None:
            return found
        n = self.start_node
        while n.next is not None and n.item[0].casefold() < word.casefold():
            if n.item[0].casefold() == word.casefold():
                found = True
                # If the word is at the beginning
                if n == self.start_node:
                    self.start_node = n.next
                else:
                    n.prev.next = n.next
                return found
            n = n.next

        # If the word is at the end
        if n.item[0].casefold() == word.casefold():
            if n.prev is not None:
                n.prev.next = None
            else:
                self.start_node = n.next
            found = True
        return found

    # -------------------------------------------------------------------------------------

    # Search for word
    def Search(self, word):
        found = False
        if self.start_node is None:
            return [], found
        n = self.start_node
        while n is not None and n.item[0].casefold() < word.casefold():
            if n.item[0].casefold() == word.casefold():
                found = True
                break
            n = n.next
        return n.item if found else None, found

    # -------------------------------------------------------------------------------------

    # Traversing and Displaying each element of the list
    def Display(self):
        if self.start_node is None:
            print("The list is empty")
            return
        else:
            n = self.start_node
            while n is not None:
                print(n.item)
                n = n.next


# -------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------

DLDict = DoublyLinkedList()

# for i in gb.data_list[:]:
#     DLDict.Insert(i[0],i[1],i[2])
# DLDict.Insert("Pizza", "(n.)", "A nice food")
# DLDict.Insert("Pizza", "(n.)", "A nice food but second")
# DLDict.Insert("Pizza", "(n.)", "A nice food but third")
#
# DLDict.Insert("Apple", "(n.)", "A fruit")
#
# DLDict.Insert("Rat", "(n.)", "An animal")
# DLDict.Insert("Rat", "(n.)", "An animal with a long tail")
# DLDict.Insert("Rat", "(n.)", "A cute animal but annoying at times")
# DLDict.Insert("Zebra", "(n.)", "A large animal with stripes")
# DLDict.Insert("Ant", "(n.)", "An insect")
#

# DLDict.Display()
# print(DLDict.Search("Ant"))
