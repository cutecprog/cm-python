#!/usr/bin/env python

def main():
        pass

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

def match(item, match_col):
        """Search for an item in a column and return index into that column.
        
        >>> match('hat', ['cat','bat','hat','wat'])
        2
        >>> match('wat*', ['fire','earth','air','water'])
        3
        
        """
        pass

def order_col(data, order):
        """Format columns to given order.
        
        >>> order_col([[["name","id"],["John","13"],["Sam","7"]],[["foo","age"],["bar","72"],["bar","47"]]], [[0,1],[1]])
        [["name","id","age"],["John","13","72],["Sam","7","47"]]
        
        """
        pass

def csv_to_list(csv_str, dem = ','):
        """Convert string in CSV format into a 2d list.
        
        >>> csv_to_list("a1,b1,c1,d1,e1,")
        [['a1', 'b1', 'c1', 'd1', 'e1', '']]
        >>> csv_to_list("a2,,c2,d2,,")
        [['a2', '', 'c2', 'd2', '', '']]
        >>> csv_to_list(",b3,,d3,,f3")
        [['', 'b3', '', 'd3', '', 'f3']]
        >>> csv_to_list(",,,,e4,")
        [['', '', '', '', 'e4', '']]
        
        """
        lines = csv_str.strip('\n').split('\n')
        csv_data = []
        for l in lines:
                csv_data.append(l.strip('\r').split(dem))
        return csv_data

def list_to_csv(data, dem = ','):
        """Convert 2d list into string in CSV format.
        
        >>> print list_to_csv([['a1', 'b1', 'c1', 'd1', 'e1', ''],['a2', '', 'c2', 'd2', '', ''],\
['', 'b3', '', 'd3', '', 'f3'],['', '', '', '', 'e4', '']])
        a1,b1,c1,d1,e1,
        a2,,c2,d2,,
        ,b3,,d3,,f3
        ,,,,e4,
        
        """
        pass

if __name__=="__main__":
        import doctest
        if doctest.testmod().failed == 0:
                main() 
