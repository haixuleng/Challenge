# Donation Analytics

Determine the total dollars received, the total number of contributions received and donation amount in a given percentile of repeat donators. 
The project is implemented using Python and has been tested successfully in Ubuntu 14.04 with Python 2.7.

I used FEC data, and interestingly I found that some individual donations are negative. Because this issue is not mentioned in the description of the challenge, I didn't take any extra actions towards these data.  


## Getting Started

### Prerequisites

Python Packages

```
numpy
sys
os
```

### Running

```
./run.sh 
```

Or

```
python ${YOUR_DIRECTORY}/src/donation-analytics.py ${YOUR_ITCONT_FILE} ${YOUR_PERCENTILE_FILE} ${YOUR_OUTPUT_FILE}
```


## Example

Here is an example showing the input files (itcont.txt and percentile.txt) and corresponding output file (repeat_donors.txt). 

### itcont.txt

```
C00629618|N|TER|P|201701230300133512|15C|IND|PEREZ, JOHN A|LOS ANGELES|CA|90017|PRINCIPAL|DOUBLE NICKEL ADVISORS|01032017|40|H6CA34245|SA01251735122|1141239|||2012520171368850783
C00177436|N|M2|P|201702039042410894|15|IND|DEEHAN, WILLIAM N|ALPHARETTA|GA|300047357|UNUM|SVP, SALES, CL|01312017|384||PR2283873845050|1147350||P/R DEDUCTION ($192.00 BI-WEEKLY)|4020820171370029337
C00177436|N|M2|P|201702039042410893|15|IND|WATJEN, THOMAS R.|KEY LARGO|FL|330375267|UNUM|CHAIRMAN OF THE BOARD|01042017|5000||40373239|1147350|||4020820171370029334
C00177436|N|M2|P|201702039042410894|15|IND|DEEHAN, WILLIAM N|ALPHARETTA|GA|300047357|UNUM|SVP, SALES, CL|01312017|600||PR2283873845050|1147350||P/R DEDUCTION ($192.00 BI-WEEKLY)|4020820171370029337
C00629618|N|TER|P|201701230300133512|15C|IND|PEREZ, JOHN A|LOS ANGELES|CA|90017|PRINCIPAL|DOUBLE NICKEL ADVISORS|01032017|20|H6CA34245|SA01251735122|1141239|||2012520171368850783
C00177436|N|M2|P|201702039042410894|15|IND|DEEHAN, WILLIAM N|ALPHARETTA|GA|300047357|UNUM|SVP, SALES, CL|01312017|900||PR2283873845050|1147350||P/R DEDUCTION ($192.00 BI-WEEKLY)|4020820171370029337
```

### percentile.txt

```
50
```

### repeat_donors.txt

```
C00177436|30004|2017|600|600|1
C00177436|30004|2017|600|1500|2
```

I ignored the first and fifth lines becaue OTHER_ID field contains data, and the contributer (DEEHAN, WILLIAM N) in the second line is a repeat donor, who contributed Jan. 31 2017 in the fourth and sixth lines.


## Performance

I used **set** and **dictionary** hashable data structures in python. The average time complexity is O(N), where N is the number of lines in one data. 

I tested the program on a Dell laptop with I7 4600U CPU and 16GM memory.

| Data Name | Data Size  | Time |
| ------------- | ------------- | ------------- |
| 2017-2018 Data Files: Contribution by Individuals | 1.3 GB  | 5 minutes 40 seconds  |
| 1993-1994 Data Files: Contribution by Individuals | 101.9 MB | 10 seconds  |


## Authors

* **Haixu Leng** - *Physics Department, University of Maryland, Baltimore County* 


## Acknowledgments

* The test data are downloaded from the Federal Election Commission (FEC).
