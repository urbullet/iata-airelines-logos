import urllib

url = "https://daisycon.io/images/airline/?width=300&height=150&color=ffffff&iata="
# Using readlines()
file1 = open('airlines.csv', 'r')
Lines = file1.readlines()
urllib.URLopener.version = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11'

count = 0
for line in Lines:
    print(line)
    urllib.urlretrieve(url + line.strip(), 'airlines-logos/' + line.strip() + '.png')

    # print("Line{}: {}".format(count, line.strip()))


