
a = ['1']

def main():
    for x in xrange(31):
        result = create_run_length(a[x])
        print 'Result #{0}: {1}'.format(x, result)
        a.append(result)
    print 'Solution: {0}'.format(len(a[30]))

def create_run_length(string):
    """ Brute force solution to run length encode an arbitrary string. """
    i = 0
    result = ''
    maxlen = len(string)
    while i <= maxlen - 1:
        current_character = string[i]
        count = 0
        while current_character == string[i]:
            i = i + 1
            count = count + 1
            if i >= len(string):
                break
        result += '{0}{1}'.format(count, current_character)

    return result


if __name__ == '__main__':
    main()
