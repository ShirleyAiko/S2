def wds(filename):
    
    """
    input: filename
    change the whole file into wds
    """
    
    FileHandle = open(filename, "r")
    content = FileHandle.read()
    FileHandle.close()
    wds = content.split()
    return wds

def remove_adjacent_dups(list):
    
    """
    remove all the same adjacent words
    """
    
    rslt = []
    most_recent_elem = None
    for e in list:
        if e != most_recent_elem:
            rslt.append(e)
            most_recent_elem = e
    return rslt

def search_linear(list, target):
    
    """
    find the item that did not exist in the list
    """
    
    for (i, v) in enumerate(list):
       if v == target:
           return i
    return -1

def find_unknown_wds(vocab, wds):
    
    """
    return words that do not occur in the vocabulary list
    """
    
    result = []
    for w in wds:
        if (search_linear(vocab, w) < 0):
            result.append(w)
    return result


import time
all_words = wds("alice_in_wonderland.rtf")
bigger_vocab = wds("vocabulary.rtf")
t0 = time.perf_counter()
all_words.sort()
cleaned_version = remove_adjacent_dups(all_words)
missing_words = find_unknown_wds(bigger_vocab, cleaned_version)
t1 = time.perf_counter()
print("There are {0} unknown words.".format(len(missing_words)))
print("That took {0:.4f} seconds.".format(t1-t0))