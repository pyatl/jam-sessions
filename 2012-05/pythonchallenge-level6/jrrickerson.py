import zipfile

filename = 'channel.zip'
start = '90052'

def solve():
    file_list = []
    comment_list = []
    keep_going = True
    current_name = start
    with zipfile.ZipFile(filename) as zfile:
        file_list = zfile.namelist()
        while keep_going:
            open_file = '{0}.txt'.format(current_name)
            info = zfile.getinfo(open_file)
            comment_list.append(info.comment)
            with zfile.open(open_file) as textfile:
                split_line = textfile.readline().split()
            if len(split_line) == 4:
                current_name = split_line[3]
                print 'Moving on to number {0}'.format(current_name)
            else:
                keep_going = False

        print ''.join(comment_list), 
                





if __name__ == '__main__':
    solve()
