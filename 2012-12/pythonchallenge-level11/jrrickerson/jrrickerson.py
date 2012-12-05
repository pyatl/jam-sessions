# Python Challenge level 11
# From URL: http://www.pythonchallenge.com/pc/return/5808.html
# User: huge Pass: file

from PIL import Image

def main():
    image = Image.open('cave.jpg')
    old_size = image.size
    print 'Old image size: ', old_size
    result_image = Image.new('RGBA', (old_size[0], old_size[1] / 2))
    print 'New image size: ', result_image.size
    data = image.getdata()
    print 'Old data length: ', len(data)
    odds_only = [data[x] for x in range(len(data)) if x % 2 == 0]
    print 'Odds only data length: ', len(odds_only)
    result_image.putdata(odds_only)

    result_image.save('result.jpg')


if __name__ == '__main__':
    main()

