"""Count words."""
from collections import Counter
def count_words(s, n):
    """Return the n most frequently occuring words in s."""
    corpus=dict()
    wordarr=s.split()
    top_n=list()
    for word in wordarr:
        corpus[word] = corpus.get(word,0)+1
    # TODO: Count the number of occurences of each word in s
    top_n=list()
    top_n=[(k,v) for k,v in corpus.iteritems()]
    top_n=sorted(top_n, key=lambda x: x[0])
    top_n=sorted(top_n, key=lambda x: x[1], reverse=True)
    
    # TODO: Sort the occurences in descending order (alphabetically in case of ties)
    # TODO: Return the top n words as a list of tuples (<word>, <count>)
    return top_n[:n]


def test_run():
    """Test count_words() with some inputs."""
    print count_words("cat bat mat cat bat cat", 3)
    print count_words("betty bought a bit of butter but the butter was bitter", 3)


if __name__ == '__main__':
    test_run()
