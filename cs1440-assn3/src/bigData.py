#!/usr/bin/env python  	    	       

#                         _  	    	       
#                        (o)<  DuckieCorp Software License  	    	       
#                   .____//  	    	       
#                    \ <' )   Copyright (c) 2022 Erik Falor  	    	       
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  	    	       
#  	    	       
# Permission is granted, to any person who is EITHER an employee OR  	    	       
# customer of DuckieCorp, to deal in the Software without restriction,  	    	       
# including without limitation the rights to use, copy, modify, merge,  	    	       
# publish, distribute, sublicense, and/or sell copies of the Software, and to  	    	       
# permit persons to whom the Software is furnished to do so, subject to the  	    	       
# following conditions:  	    	       
#  	    	       
# The above copyright notice and this permission notice shall be included in  	    	       
# all copies or substantial portions of the Software.  	    	       
#  	    	       
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR  	    	       
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,  	    	       
# FITNESS FOR A PARTICULAR PURPOSE, EDUCATIONAL VALUE AND NONINFRINGEMENT. IN  	    	       
# NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,  	    	       
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR  	    	       
# OTHERWISE, ARISING FROM INDIGNATION, INDIGESTION, INDIFFERENCE, INDECENCY,  	    	       
# INDENTATION, INDETERMINATION, INTOXICATION, INDOCTRINATION, INTOLERANCE,  	    	       
# INDULGENCE, INDELICATENESS, INDISCRETION, INEFFECTIVENESS OR IN CONNECTION  	    	       
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.  	    	       


import time
import sys
from Report import Report


def getFIPS(filePath: str) -> dict:
    fipAreas = {}
    f = open(filePath + "/area-titles.csv")

    for line in f:
        # Get the line and split it by the comma to get the FIPS Code and FIPS Area
        lineArray = line.replace("\n", "").replace("\"", "").split(sep=",")

        # Checks to see if we want the Fips code on this line.
        if lineArray[0].isdecimal():
            if int(lineArray[0]) % 1000 != 0:
                fipAreas[lineArray[0]] = lineArray[1]

    f.close()

    return fipAreas


def createReport(filePath: str, fipAreas: dict) -> Report:

    numAllAreas = 0
    numSoftAreas = 0

    totalAllWages = 0
    totalSoftWages = 0
    totalAllEstab = 0
    totalSoftEstab = 0
    totalAllEmplvl = 0
    totalSoftEmplvl = 0

    maxWagesAll = ["", -1]
    maxWagesSoft = ["", -1]
    maxEstabAll = ["", -1]
    maxEstabSoft = ["", -1]
    maxEmplAll = ["", -1]
    maxEmplSoft = ["", -1]


    f = open(filePath + "/2021.annual.singlefile.csv")

    for line in f:
        # Turn the file line into an array of data.
        lineArray = line.replace("\n", "").replace("\"", "").split(sep=",")
        # Keep only the data we want.
        # Checks to see if this line pertains to one of our FIPS areas
        if fipAreas.__contains__(lineArray[0]) and lineArray[1].isdecimal() and lineArray[2].isdecimal():
            # Checks to see if the data belongs in all industries.
            if int(lineArray[1]) == 0 and int(lineArray[2]) == 10 \
                    and lineArray[10].isdigit() and lineArray[9].isdigit() and lineArray[8].isdigit():

                numAllAreas += 1

                # Add up the totals
                totalAllWages += int(lineArray[10])
                totalAllEmplvl += int(lineArray[9])
                totalAllEstab += int(lineArray[8])

                # Check to see if there is a new max
                if int(lineArray[10]) > maxWagesAll[1]:
                    maxWagesAll = [fipAreas[lineArray[0].replace("'", "")], int(lineArray[10])]

                if int(lineArray[9]) > maxEmplAll[1]:
                    maxEmplAll = [fipAreas[lineArray[0].replace("'", "")], int(lineArray[9])]

                if int(lineArray[8]) > maxEstabAll[1]:
                    maxEstabAll = [fipAreas[lineArray[0].replace("'", "")], int(lineArray[8])]

            # Checks to see if the data belongs in software publishing industry.
            elif int(lineArray[1]) == 5 and int(lineArray[2]) == 5112 \
                    and lineArray[10].isdigit() and lineArray[9].isdigit() and lineArray[8].isdigit():

                numSoftAreas += 1

                # Add up the totals
                totalSoftWages += int(lineArray[10])
                totalSoftEmplvl += int(lineArray[9])
                totalSoftEstab += int(lineArray[8])

                # Check to see if there is a new max
                if int(lineArray[10]) > maxWagesSoft[1]:
                    maxWagesSoft = [fipAreas[lineArray[0].replace("'", "")], int(lineArray[10])]

                if int(lineArray[9]) > maxEmplSoft[1]:
                    maxEmplSoft = [fipAreas[lineArray[0].replace("'", "")], int(lineArray[9])]

                if int(lineArray[8]) > maxEstabSoft[1]:
                    maxEstabSoft = [fipAreas[lineArray[0].replace("'", "")], int(lineArray[8])]

    f.close()


    # Now we have looped through the data and want to make a report object.
    reportToReturn = Report(year=2021)

    # Update the report object with the data for All Industries
    reportToReturn.all.num_areas = numAllAreas

    reportToReturn.all.total_annual_wages = totalAllWages
    reportToReturn.all.max_annual_wage = maxWagesAll

    reportToReturn.all.total_estab = totalAllEstab
    reportToReturn.all.max_estab = maxEstabAll

    reportToReturn.all.total_empl = totalAllEmplvl
    reportToReturn.all.max_empl = maxEmplAll

    # Update the report object with the data for Software Publishing Industry
    reportToReturn.soft.num_areas = numSoftAreas

    reportToReturn.soft.total_annual_wages = totalSoftWages
    reportToReturn.soft.max_annual_wage = maxWagesSoft

    reportToReturn.soft.total_estab = totalSoftEstab
    reportToReturn.soft.max_estab = maxEstabSoft

    reportToReturn.soft.total_empl = totalSoftEmplvl
    reportToReturn.soft.max_empl = maxEmplSoft

    return reportToReturn


if __name__ == '__main__':

    if len(sys.argv) != 2:
        print("Usage: src/bigData.py DATA_DIRECTORY\n Exactly one argument must be given.")
        exit()


    # print("Reading the databases...", file=sys.stderr)
    before = time.time()  	    	       

    fipAreas = getFIPS(filePath=sys.argv[1])

    rpt = createReport(filePath=sys.argv[1], fipAreas=fipAreas)

    after = time.time()  	    	       
    # print(f"Done in {after - before:.3f} seconds!", file=sys.stderr)

    # Print the completed report  	    	       
    print(rpt)  	    	       

