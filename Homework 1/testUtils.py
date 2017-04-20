def test_lists_equals(list1, list2):
    if not list1 or not list2 or len(list1) != len(list2):
        return False
    
    for i, k in enumerate(list1):
        if list2[i] != list1[i]:
            return False
    return True
