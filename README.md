# loinc2hpoAnnotation
This repo holds data generated from the loinc2hpo app! There are two default folders:

**Task**: holds lists of LOINC codes awaiting annotating;

**Data**: holds annotation data

# Set up
1. clone this repo to your local machine.
2. start loinc2hpo
3. specify this loinc2hpoAnnotation as the default folder for auto-save.
4. import default data by clicking `File`-`Open session`, choose loinc2hpoAnnotation/Data and click ok.

**check your configurations**

Click `Configuration`-`Show Settings`, you should see "<*path*>/loinc2hpoAnnotation" in line "Path to auto-saved file", and "<*path*>/loinc2hpoAnnotation/Data" in line "Path to last session". <*path*> is dependent on where you cloned loinc2hpoAnnotation on your computer.  

# Annotation
The **Task** folder contains LOINC lists that need to be annotated. Use the `filter` button to start annotating those LOINC codes. When you are done, save your session data and check in your data. We adopt a similar model with HPO in that only one person is allowed to edit the file at one time. So remember to send out an email to loinc2hpoannotation@googlegroups.com (example, LOCKING loinc2hpo as the subject) to let people know that you are locking/unlocking the files.

1. Let people know that you are locking the files. 
2. From terminal, use $cd command to enter loinc2hpoAnnotation folder
3. Pull the most recent annotation file from Github. 
```
$ git checkout develop
$ git pull origin develop
```
4. Do Step 2 and 3 before you launch loinc2hpo. Now, start annotation with loinc2hpo. After you are done, save your session data. 

5. Execute the following command:
```
$ git add .
$ git commit -m "YOUR MESSAGE"
$ git push origin develop
```
repace "YOUR MESSAGE" with your commit comment. 

6. Let people know that you have unlocked the files. 
