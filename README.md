# loinc2hpoAnnotation
This repo holds data generated from the loinc2hpo app! There are two default folders:

**Task**: holds lists of LOINC codes awaiting annotating;

**Data**: holds annotation data

# Set up
1. Clone this repo to your local machine.
2. Start loinc2hpo
3. The first time you run this app, you need to specify this loinc2hpoAnnotation as the default folder for auto-save, and complete other settings under **Configuration** by following https://loinc2hpo.readthedocs.io/en/latest/Configuration.html#mandatory-settings.
4. Restart loinc2hpo, you should be able to see LOINC table being populated, HPO successfully loaded (signal light chaning from red to green) and the second tab **Loinc2HpoAnnotations** being populated with thousands of annotations.

How to make sure your configurations are correct?
**check your configurations**

Click `Configuration`-`Show Settings`, you should see all mandatory settings being defined. Specifically, "Path to auto-saved file" is set to "<*path*>/loinc2hpoAnnotation". <*path*> is dependent on where you cloned loinc2hpoAnnotation on your computer. If you submit annotations to the loinc2hpoAnnotation Github repository, you should also define a biocurator id in the format of institution:user initial, such as JGM:jsmith.

# Annotation
The **Task** folder contains LOINC lists that need to be annotated. Use the `filter` button to start annotating those LOINC codes. When you are done, save your session data and check in your data. We adopt a similar model with HPO in that only one person is allowed to edit the file at one time. So remember to send out an email to loinc2hpoannotation@googlegroups.com (example, LOCKING loinc2hpo as the subject) to let people know that you are locking/unlocking the files.

1. Let people know that you are locking the files. 
2. From terminal, use $cd command to enter loinc2hpoAnnotation folder
3. Pull the most recent annotation file from Github. 
```
$ git checkout develop
$ git pull origin develop
```
   Please work on the "develop" branch only.

4. Do Step 2 and 3 before you launch loinc2hpo. Now, start working on a *task*: click **Filter**, choose **loinc2hpoAnnotation**/**Task**/**UNC-loinc1.txt**. After you are done, save your session data. 

5. Execute the following command:
```
$ git add .
$ git commit -m "YOUR MESSAGE"
$ git push origin develop
```
repace "YOUR MESSAGE" with your commit comment. 

6. Let people know that you have unlocked the files. 

# Annotating with newly created HPO terms
The HPO website releases updated hp.obo and hp.owl files about once a month. If you want to use newly added HPO terms that are not officially released, you can build them by following steps below.

1. Git clone the human-phenotype-ontology Github repository at https://github.com/obophenotype/human-phenotype-ontology. Note you only need to do this step once. 

2. Install Docker if you have not do so. Note you will need to change you Docker setting to avoid memory error: Docker -> Preferences -> Advanced -> [Increase memory to 6GB or 8GB]. Note you only need to do this step once.  

3. Go to HPO repository from your terminal, then pull the most recent HPO by running
```
git pull
```
under human-phenotype-ontology folder.

4. Make sure Docker is running, then run the following command
```
cd src/ontology
sh run.sh make IMP=false prepare_release
```
Note it will take a few minutes up to more than 10 minutes to complete the task. You will need to run step 3 and 4 every time you want to update HPO. 

5. Set the path to the new hp.obo and hp.owl files in the loinc2hpo biocuration app. The newly created hp owl and obo files are under the src/ontology folder. Click **"Configuration"** - **"Change hpo.owl"** to set the path to your hpo.owl file; use the button below to set the path to the hpo.obo file. Note this step only needs to be done once unless you have changed the settings.

6. You should now be able to create a Loinc mapping with the new HPO term.

# Reset loinc2hpo settings
If you cannot launch loinc2hpo, it is probably some configurations are set incorrectly. The easiest way is to delete the configuration file under
{HOME}/.loinc2hpo

Detele the loinc2hpo.settings file by running:
```
rm loinc2hpo.settings
```
Then try launching loinc2hpo again. It will ask you to reset all the configurations. 
