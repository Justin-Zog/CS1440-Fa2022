#!/usr/bin/python3  	    	       

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


# python -m pip install --user -r requirements.txt
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
import requests
import sys
import time


def crawl(url, current_depth, visited=set(), maximum_depth=3):
    """  	    	       
    Given an absolute URL, print each hyperlink found within the document.  	    	       
    This will run until
    0) No new, unvisited links are found  	    	       
    1) The maximum depth of recursion is reached
    2) The max_runtime is hit
    """

    spaces = "    "

    if current_depth > maximum_depth:
        return

    # Check the url to make sure it is legit
    if url in visited:
        return

    parsedURL = urlparse(url)

    if parsedURL.scheme and parsedURL.netloc and ('http' in parsed.scheme or 'https' in parsed.scheme):
        try:
            r = requests.get(url, timeout=10)
            visited.add(url)
            print(f"{spaces*current_depth}{url}")

        except Exception as e:
            print(f"Failed to get {url} because {e}")
            visited.add(url)
            return

        try:
            soup = BeautifulSoup(r.text, 'html.parser')
            links = soup.find_all('a')
        except Exception as e:
            print(f"Failed to parse the html with error: {e}")
            return

        for a in links:
            if a.get('href'):
                # a.get('href') will be a link we can visit
                defraggedURL = a.get('href').split('#')[0]
                # Determines if defraggedURL is an absolute URL
                parsedDefragged = urlparse(defraggedURL)
                if parsedDefragged.scheme and parsedURL.netloc and ('http' in parsed.scheme or 'https' in parsed.scheme):
                    crawl(defraggedURL, current_depth=current_depth+1, visited=visited, maximum_depth=maximum_depth)
                else:
                    # Create an absolute URL
                    absURL = urljoin(url, defraggedURL)
                    crawl(absURL, current_depth=current_depth+1, visited=visited, maximum_depth=maximum_depth)
    else:
        return


def usage():
    return 'USAGE: Enter arguments like so: URL [DEPTH]'


# If the crawler.py module is loaded as the main module, allow our `crawl` function to be used as a command line tool  	    	       
if __name__ == "__main__":

    url = ''
    visitedLinks = set()
    maxDepth = 3

    # If no arguments are given...
    if len(sys.argv) < 2:
        print(f"Error: No URL supplied\n")
        print(usage())
        exit(0)
    else:
        url = sys.argv[1]

    # Checks to see whether `url` is an absolute URL or not.
    parsed = urlparse(url)

    if not (parsed.scheme and parsed.netloc and ('http' in parsed.scheme or 'https' in parsed.scheme)):
        print(f"Error: {url} is not a valid URL.\nPlease only use absolute URLs with this program.")
        print(f"Note: Make sure the scheme is either `http` or `https`.")
        exit(0)

    # Checks to see if the user overrode the default recursion depth or time
    if len(sys.argv) >= 3:
        try:
            maxDepth = int(sys.argv[2])

        except ValueError as ve:
            print(f"Error: {ve}\nMake sure the argument after the URL is a positive whole number.")
            print(f"Setting max depth to the default value 3...")

        except TypeError as e:
            print(f"Error: {e}\nThe argument after the URL must be a positive whole number.")
            print(f"Setting max depth to the default value 3...")

        if maxDepth < 0:
            print(f"Error: The provided max depth, {maxDepth}, is less than 0.\nPlease enter a positive whole number.")
            print(f"Setting max depth to the default value 3...")
            maxDepth = 3

    plural = 's' if maxDepth != 1 else ''
    print(f"Crawling from {url} to a maximum depth of {maxDepth} link{plural}")

    defraggedURL = url.split('#')[0]
    startTime = time.time()

    try:
        crawl(defraggedURL, current_depth=0, visited=visitedLinks, maximum_depth=maxDepth)
    except KeyboardInterrupt as e:
        print(f"\nWeb-crawler was manually stopped with ^c. Here are the stats:\n")
    finally:
        # Report on the web-crawler.
        print(f"Visited {len(visitedLinks)} unique pages in {'{:.2f}'.format(time.time() - startTime)} seconds.")
        exit(0)
