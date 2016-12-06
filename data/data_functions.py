import datetime

# Postgresql works best when all column and table names are lower case.
#     Here is a function to convert all column names in a pandas DataFrame
#     to lower case.
def column_names_to_lower_case( df_IN ):
    
    '''
    Accepts a pandas DataFrame.  Converts all column names to lower case.
        Returns the updated DataFrame, or None if error.
    '''
    
    # return reference
    dl_OUT = None
    
    # declare variables
    column_name_list = None
    rename_map = None
    original_name = ""
    name_lower = ""
    
    # Make sure we have something passed in.
    if ( df_IN is not None ):
        
        # Create dictionary that maps original column names to that smae name in all lower case.
        rename_map = {}
        
        # get list of column names
        column_name_list = list( df_IN.columns )
        
        # loop over column names
        for original_name in column_name_list:
            
            # convert to all lower case
            name_lower = original_name.lower()
            
            # add to rename map
            rename_map[ original_name ] = name_lower
        
        #-- END loop over column names. --#
        
        # rename columns in DataFrame
        df_IN.rename( columns = rename_map, inplace = True )
        
        # place DataFrame in return reference.
        df_OUT = df_IN
        
    else:
        
        # nothing passed in.  For shame.
        print( "ERROR - no DataFrame passed in.  Nothing to do." )
        
        df_OUT = None
        
    #-- END check to see if DataFrame passed in --#
    
    return df_OUT
    
#-- END function column_names_to_lower_case() --#

print( "Function column_names_to_lower_case() declared at " + str( datetime.datetime.now() ) )