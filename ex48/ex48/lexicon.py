lexicon = {'north' : 'direction',
            'south': 'direction',
            'east' : 'direction',
            'go' : 'verb',
            'kill' : 'verb',
            'eat' : 'verb',
            'the' : 'stop',
            'in' : 'stop',
            'of' : 'stop',
            'bear' : 'noun',
            'princess' : 'noun'
}

def scan(sentance):
    results = []
    line = sentance.lower()
    words = line.split()
    for word in words:
        word_type = lexicon.get(word)
        if word_type == None:
            try:
                int(word)
            except ValueError:
                results.append(('error', word))
            else:
                results.append(('numbers', word))
        else:
            results.append((word_type, word))
    return results
