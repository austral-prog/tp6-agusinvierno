# Replace the "ANSWER HERE" with your answer

def remove_elements(list_to_remove_elements):
    if len(list_to_remove_elements) > 5:
        list_to_remove_elements.pop(5)
    if len(list_to_remove_elements) > 4:
        list_to_remove_elements.pop(4)
    if len(list_to_remove_elements) > 0:
        list_to_remove_elements.pop(0)
    return list_to_remove_elements
#remove_elements()


def add_elements(list_to_add_elements):
    list_to_add_elements.insert(0, 'Pink')
    list_to_add_elements.insert(5, 'Yellow')
    return list_to_add_elements
#add_elements()


def is_empty(list_to_check):
        if len(list_to_check) == 0:
            return True
        else:
            return False
#is_empty()


def check_lists(list_to_compare1, list_to_compare2):
        if len(list_to_compare1) < 3 or len(list_to_compare2) <3:
            return False
        if list_to_compare1[2] == list_to_compare2[2]:
             return True
        else:
             return False
#check_lists()


def list_of_lists(list_of_lists_to_modify):
    list_of_lists_to_modify[0] = list_of_lists_to_modify[0][:2]
    list_of_lists_to_modify[1] = list_of_lists_to_modify[1][1:4]
    list_of_lists_to_modify[2] = list_of_lists_to_modify[2][-2:]
    return list_of_lists_to_modify
#list_of_lists()
