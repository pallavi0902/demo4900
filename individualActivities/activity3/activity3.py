def main ( ):
    print ( "ISQA 4900 GRADE CALCULATOR" )

    print ( "" )

    grade = eval ( input ( "Enter Your Grade :  " ) )

    print ( "" )

    if 970 <= grade <= 1000:
        print ( "You got A+" )

    elif 930 <= grade <= 969.99:
        print ( "Good!You got a A" )

    elif 900 <= grade <= 929.99:
        print ( 'Nice! A- Grade' )

    elif 870 <= grade <= 890.99:
        print ( 'You got B+' )

    elif 830 <= grade <= 860.99:
        print ( 'You got B' )

    elif 800 <= grade <= 829.99:
        print ( 'You got B-' )

    elif 770 <= grade <= 799.99:
        print ( 'You got C+' )

    elif 730 <= grade <= 769.99:
        print ( 'You890got C-' )

    elif 670 <= grade <= 699.99:
        print ( 'You got D+' )

    elif 630 <= grade <= 669.99:
        print ( 'You got D' )

    elif 600 <= grade <= 629.99:
        print ( 'You got D-' )

    elif 0 <= grade <= 599.99:
        print ( 'You got F' )
main ( )
