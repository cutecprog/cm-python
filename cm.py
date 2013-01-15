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
        >>> match('wat*, ['fire','earth','air','water'])
        3
        
        """
        pass

if __name__=="__main__":
        import doctest
        if doctest.testmod().failed == 0:
                main() 
