# CS 1440 Assignment 3: Big Data Processing - Testing Data

These directories will contain the "big data" that your program will consume.  The annual single CSV files are not included in this repository because they are just too big.  You can build each CSV file from the complete data set with your command-line Text Tools; instructions are included in each directory.

Each directory also contains an `output.txt` file which shows *exactly* what your program should output for each data set.  Use this information as a guide when you test and debug your program.  Start with small data sets, and work your way up to the largest ones, in this order:

Region   | FIPS Areas
---------|-----------
DC       | 1
HI       | 5
ME       | 16
UT       | 29
WV       | 55
OH       | 88
USA_full | 3,463


Each region is broken down into four data sets of varying size.  In order from smallest to largest:

*   `software_industry` - contains *only* data about privately-held software publishing companies; the top half of the report will have zeros
*   `all_industries` - entries that summarize *all* economic activity in the region; the bottom half of the report will have zeros
*   `complete` - includes the same data as above, plus entries for *every* economic sector in the region; your program *ignores* most of this data
*   `reversed` - like the `complete` file, but *upside-down* (this file is made with `tac`); your program should produce the same output as it does with the `complete` data set
