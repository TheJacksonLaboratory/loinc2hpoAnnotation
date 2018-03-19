# loinc2hpoAnnotation
This repo holds data generated from the loinc2hpo app! There are two default folders:

**Task**: holds lists of LOINC codes awaiting annotating;

**Data**: holds annotation data

# Set up?
1. clone this repo to your local machine.
2. start loinc2hpo
3. specify this loinc2hpoAnnotation as the default folder for auto-save.
4. import default data by clicking `File`-`Open session`, choose loinc2hpoAnnotation/Data and click ok.

**check your configurations**

Click `Configuration`-`Show Settings`, you should see "<*path*>/loinc2hpoAnnotation" in line "Path to auto-saved file", and "<*path*>/loinc2hpoAnnotation/Data" in line "Path to last session". <*path*> is dependent on where you cloned loinc2hpoAnnotation on your computer.  

# Start annotation
The **Task** folder contains LOINC lists that need to be annotated. Use the `filter` button to start annotating those LOINC codes. When you are done, save your session data and check in your data:

1. in terminal, use $cd command to enter loinc2hpoAnnotation folder
2. execute the following command:
```
$ git add .
$ git commit -m "YOUR MESSAGE"
$ git push origin master

```
repace "YOUR MESSAGE" with your commit comment. 
