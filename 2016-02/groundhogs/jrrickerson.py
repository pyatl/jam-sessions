# Groundhog data weather data analysis
import sys


# Constants according to NOAA data format documentation
STATE_CODE = b'110'
DIVISION_NUMBER = b'0'
ELEMENT_CODE = b'02'


SPRING_TEMP_INCREASE = 20.0
OUTPUT_FORMAT = 'Year: {} GH: {}   Feb: {}     March: {}   Change: {:.2f}%  Prediction: {}'


def filter_records(records, prefix):
    return [r for r in records if r.startswith(prefix)]


def main(data_file, groundhog_file):
    # Open the data file
    records = []
    prefix = STATE_CODE + DIVISION_NUMBER + ELEMENT_CODE
    with open(data_file, 'rb') as datafile:
        records = filter_records(datafile, prefix)

    temp_data = {}
    skip = len(prefix)
    for record in records:
        temps = record[skip:].split()
        year = temps.pop(0)
        temp_data[str(year, 'utf8')] = [str(t, 'utf8') for t in temps]

    groundhog_data = {}
    with open(groundhog_file, 'rb') as gf:
        for line in gf:
            year, saw_shadow = line.split()
            groundhog_data[str(year, 'utf8')] = str(saw_shadow, 'utf8')

    attempts = 0
    success = 0
    for year in sorted(groundhog_data.keys()):
        if year in temp_data:
            increase = 100 - float(temp_data[year][1]) / float(temp_data[year][2]) * 100
            if increase > SPRING_TEMP_INCREASE and groundhog_data[year] == 'N':
                result = 'GOOD'
            elif increase <= SPRING_TEMP_INCREASE and groundhog_data[year] == 'Y':
                result = 'GOOD'
            else:
                result = 'BAD'
            attempts += 1
            if result == 'GOOD':
                success += 1
            output = OUTPUT_FORMAT.format(
                year, groundhog_data[year], temp_data[year][1],
                temp_data[year][2], increase, result)
            print(output)
    print('Success Rate: {} / {} ({:.2f}%)'.format(success, attempts, success / attempts * 100))


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
