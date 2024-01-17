def last_element(lst):
    """Return last item in list (None if list is empty.
    
        >>> last_element([1, 2, 3])
        3
        
        >>> last_element([]) is None
        True
    """

    # return lst[len(lst) - 1] if (lst) else return None

    # 1st attempt works...
    # if lst:
    #     return lst[len(lst) - 1] 
    # else:
    #     return None

    # this is better...
    if lst:
        return lst[-1]