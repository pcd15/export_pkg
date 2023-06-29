# export_ease
Built upon Python modules that call JSON RESTful API to gather macroeconomic data, this package offers a streamlined interface through which you can request and subsequently analyze vast amounts of macroeconomic data from sources including UN Comtrade and the International Monetary Fund (IMF). Below is a step-by-step guide detailing effective use of this program. (This package was built to supplement a [research project](https://github.com/pcd15/Econ-Sanctions/blob/main/README.md) led by Morad Bali at Duke University's Nicholas School of the Environment. The link provided offers further resources to tidy the data that this package writes.)
## Running the Program
### Comtrade
* This part of the program utilizes the [comtradeapicall](https://pypi.org/project/comtradeapicall/) Python package to implement additional functionality.
* To query export data from Comtrade, you can use the following methods:
  * ```get_all_exports```: writes csv file containing export data for all available country pairs (i.e., exports from each reportner to all its partners)
  * ```get_total_exports```: writes csv file containing total-export (exports to world) data for all available reporters
* When you run these functions, you'll need to enter the criteria for your query. Both of these functions require two arguments, the first being the frequency ("A" for annual, "M" for monthly, or "B" for both) and the second being the year for which to gather data (e.g., 2021). Once the program's finished running, it'll output the names of the files that were just created.
### IMF
* Functions with which to query data:
  * ```get_reporter_exports```: writes csv file containing value exports from reporter provided in console input to all its partners 
  * ```get_total_exports```: same as Comtrade's get_total_exports method
* The code to get IMF data is almost identical in structure to Comtrade's. The only difference is the arguments for get_reporter_exports (get_total_exports is the same across Comtrade and IMF): the first argument is the name of the reporting country for which you'd like to gather (e.g., "France"), followed by the frequency and year (in the same format as Comtrade's).
  * If you input an incorrect country name for ```get_reporter_exports```, you can check country_codes.csv to see valid country names (this file is written by the program when you run ```get_reporter_exports```).
### Other Notes
* This program assumes that the source code is contained in a subdirectory within the project (e.g., ```src```) and that the files generated will be written to another subdirectory titled ```data``` (i.e., both your source code's and ```data```'s parent directory must be the root directory for your project). Be sure that your project adheres to this structure, as this package will throw errors if it can't find ```data```.
* Data is expressed in USD (Comtrade in ones, IMF in millions) and is available in both monthly and annual quantities. In addition, no data from either source are seasonally or inflation adjusted.
* Comtrade functions will retrieve data for the given year only, while IMF functions will retrieve data starting at the given year and ending with the most recently published data.
* The ```get_reporter_exports``` function for IMF has a quirk that occurs when the user requests a query for annual data starting at a year within 3 years of the current year. In this case, the function will "override" the user's indicated year and instead make the starting year 3 years less than the current year--I had to add this padding in order to work around the varying structures of the JSON file returned by the IMF API. This has no serious implications, as it still gets all the data you requested (and then some).
## Example Python Script
```
from export_ease.comtrade import Comtrade     # importing the Comtrade class
from export_ease.imf import IMF     # importing the IMF class

# see above documentation
Comtrade.get_all_exports("B", 2021)
Comtrade.get_total_exports("B", 2021)

Comtrade.get_all_imports("B", 2021)
Comtrade.get_total_imports("B", 2021)

IMF.get_reporter_exports("France", "B", 2021)
IMF.get_total_exports("B", 2021)
```

The above code can also be found in the ```test``` folder in the [GitHub repository](https://github.com/pcd15/export_pkg) for this package.
