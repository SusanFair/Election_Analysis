# Election_Analysis

## Overview of Election Audit
Based on a request from the Colorado Board of Elections this project has been tasked perform an Election Audit.  This audit will result in a report containing the total number of votes cast, the total number of votes per candidate, the percent of votes for each candidate and the official winner of the election based on the data provided. 

## Election-Audit Results
The results of the election are clear with Denver receiving the largest number of votes and a significant, even overwholming win.  The results breakdown is as follows:
* Total Votes: 369,711
* Total Votes per County:
  * Jefferson: 10.5% (38,855)
  * Denver: 82.8% (306,055)
  * Arapahoe: 6.7% (24,801)
* Largest County Turnout: Denver with 306055 votes!
* Total Votes per Candidate
  * Charles Casper Stockham: 23.0% (85,213)
  * Diana DeGette: 73.8% (272,892)
  * Raymon Anthony Doane: 3.1% (11,606)
* **Election Winner!:  Diana DeGette**
  * Winning Vote Count: 272,892
  * Winning Percentage: 73.8%

For an output of election results - see election_analysis.txt
* [election_analysis.txt](https://github.com/SusanFair/Election_Analysis/blob/main/analysis/election_analysis.txt)

For the raw data is available in the election_results.csv file found here:
* [election_results.csv](https://github.com/SusanFair/Election_Analysis/blob/main/Resources/election_results.csv)

## Election-Audit Summary
In performing this Election Audit we provided clear and detailed results of this US Congressional precinct election.  See the Election-Audit Results above.  In addition we were able to provide a proven tool for performing similar audits on a number of elections and election types.

### PyPoll Re-Use and Flexability
The code as currently written has a good amount of flexibility due to common naming conventions.  No specific references to the Colorad precint or state or candidate is referenced.  Generic names for files were used e.g.: election_results.csv, election_data, candidate_name, etc.  This code would therefore be usable in other congressional districts, senatorial districts and local elections.

### Modification to expand usability
The current code is design to read a .csv file.  Election results however often come in different formats.  Based on the research provided there are 3 typical types of input received:
* mail-in ballots
  * hand counted, entered into a csv file
* punch cards
  * Collect and fed into a machine that tabulates vote total
  * Note:  The code would have to be modified to accept not only a list of votes but factor in these already totaled votes as well.
* direct recording electronic (DRE)  counting machines
  * sent to the central office and read by a computer
  * Note:  the computer output file in this case may be a csv or a different file type.  The code would have to be modified to look for and additonal file and consider the data contained in it when performing county and candidate total.












# Background info for later


