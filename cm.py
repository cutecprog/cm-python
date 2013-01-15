#!/usr/bin/env python

import csv

data1 = []
data2 = []
with open('../Downloads/pvs.csv', 'rb') as csvfile:
        dialect = csv.Sniffer().sniff(csvfile.read(1024))
        csvfile.seek(0)
        file1 = csv.reader(csvfile, dialect)
        for row in file1:
                data1.append(row)
with open('../Downloads/candidates-01-02-2013-andrea.csv', 'rb') as csvfile:
        dialect = csv.Sniffer().sniff(csvfile.read(10240))
        csvfile.seek(0)
        file2 = csv.reader(csvfile, dialect)
        for row in file2:
                data2.append(row)
def match(d1, data2):
        j=0
        index = []
        for d2 in data2:
                if d1[1].lower() == d2[9].lower() and d1[2].lower() == d2[7].lower():
                        print d2[0], '|', d2[4], '|', d2[21], '|', d2[22]
                        index.append(j)
                j+=1
        return index
i=0
k=0
for n in data1:
        j = match(n,data2)
        if j != []:
                print k, i, j
                k += 1
        i += 1


# A not working prototype for gen_match_key()...I know I'm bad
'''lastname1 = zip(*data1)[1]
lastname2 = zip(*data2)[9]
lastname1 = sorted(lastname1)
lastname2 = sorted(lastname2)
match_key = []
for i in range(0,len(lastname1)):
        j = 0
        while j < len(lastname2)\
                        and lastname1[i].lower() != lastname2[j].lower()\
                        and 1==1:
                j += 1
        match_key.append(j)
print match_key'''

def main():
        pass
        '''file1 = open("pvs.csv", "r")
        file2 = open("other_data.csv", "r")
        data = []
        data.append(csv_to_list(file1.read()))
        data.append(csv_to_list(file2.read()))
        #trim_data
        match_key = gen_match_key(data)'''

def col_as_int(col):
        """Convert column label to integer.
        
        >>> col_as_int('A')
        0
        >>> col_as_int('D')
        3
        >>> col_as_int('Z')
        25
        >>> col_as_int('AA')
        26
        >>> col_as_int('AZ')
        51
        >>> col_as_int('BA')
        52
        >>> col_as_int('ZZ')
        675
        >>> col_as_int('AAA')
        676
        >>> col_as_int('d')
        3
        >>> col_as_int('aAA')
        676
        
        """
        pass

def match(item, match_data, col_select):
        """Search for an item in a column and return index into that column.
        
        >>> match(['smith','john'], [['1232','smith','jane'],['2343','smith','john']], [1,2])
        1
        >>> match(['232324','foo','bar','smith','trash','john'],\
                 [['1232','smith','jane'],['2343','smith','john']], [,,,1,,2])
        1
        
        """
        pass

def gen_match_key(data):
        """Generate matching row indices in data sets.
        
        """
        pass

def order_col(data, order):
        """Format columns to given order.
        
        >>> order_col([[["name","id"],["John","13"],["Sam","7"]],[["foo","age"],["bar","72"],["bar","47"]]], [[0,1],[1]])
        [["name","id","age"],["John","13","72"],["Sam","7","47"]]
        
        """
        pass

if __name__=="__main__":
        import doctest
        #if doctest.testmod().failed == 0:
        #        main() 
