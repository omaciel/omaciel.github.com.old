def REPAGINATE(pages, current_page, max_page_count):
    if type(pages) == xrange:
        pages = [i for i in pages]

    current_pages_count = len(pages)
    if current_pages_count <= max_page_count:
        return pages

    is_odd = bool(max_page_count%2)
    page_index = pages.index(current_page)
    lower_bound = max_page_count - 1
    upper_bound = current_pages_count - lower_bound

    # Inside first max_page_count-1 elements
    if page_index <= (lower_bound - 1):
        return pages[:lower_bound] + ['...', pages[-1]]

    # Inside last max_page_count-1 elements
    if page_index >= (upper_bound):
        return [pages[0], '...'] + pages[upper_bound:]

    if not is_odd:
        lower_bound = page_index - (max_page_count/2) + 2
    else:
        lower_bound = page_index - (max_page_count/2) + 1
    upper_bound = page_index + (max_page_count/2)
    return [pages[0], '...'] + pages[lower_bound:upper_bound] + ['...', pages[-1]]
