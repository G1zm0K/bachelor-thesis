def make_wordlist(input):
    accept_words_list = set()
    for w in open(input, "r").read().splitlines():
        if not w == "":
            accept_words_list.add(w)
    return accept_words_list