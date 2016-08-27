def check_string(myword):

    #open the file using `with` context manager, it'll automatically close the file for you
    with open(/usr/share/dict/words) as f:
        found = False
        for line in f:  #iterate over the file one line at a time(memory efficient)
            if re.search("\b{0}\b".format(myword),line):    #if string found is in current line then print it
                print myword
                found = True
