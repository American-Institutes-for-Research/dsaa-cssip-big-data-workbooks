Topic 2: SELECT Statement
=======

SELECT STATEMENT
-------

SELECT statements are used to filter and display the data that you might be interested in using or investigating. SELECT is a very powerful tool and allows for many different types of data filtering, aggregation, and grouping. 

SELECT statement syntax is as following: 

SELECT
	[ALL | DISTINCT | DISTINCTROW]
		[HIGH_PRIORITY]
		[STRAIGHT_JOIN]
		[SQL_SMALL_RESULT] [SQL_BIG_RESULT] [SQL_BUFFER_RESULT]
		[SQL_CACHE | SQL_NO_CACHE] [SQL_CALC_FOUND_ROWS]
	select_expr [, select_expr ...]
	[FROM table_references
	[WHERE where_condition]
	[GROUP BY {col_name | expr | position}
		[ASC | DESC], ...]
	[HAVING where_condition]
	[ORDER BY {col_name | expr | position}
		[ASC | DESC], ...]
	[LIMIT {[offset,] row_count | row_count OFFSET offset}]
	[PROCEDURE procedure_name(argument_list)]
	[INTO OUTFILE 'file_name' export_options
		| INTO DUMPFILE 'file_name'
		| INTO var_name [, var_name]]
	[FOR UPDATE | LOCK IN SHARE MODE]]

EXERCISE
------

