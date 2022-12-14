# Lightcast/EMSI Reports
This is the template for building Lightcast/EMSI reports. These reports are requested on a semi-regular basis and it can be useful to have a template to follow. Feel free to make modifications as needed or desired, but this should be a useful first-step. It is important to recognize that these reports are extremely high-level and often lack in nuance. 

Download this repository and then follow these 7 broad steps that must be taken:
## Step 1: Identify CIP codes
The first step is to identify the CIP codes associated with the program you are analyzing. Sometimes units will have feedback on this point, but typically they will not. There are generally two good resources to use: a) the list of programs from the University Factbook (https://itableau.du.edu/#/views/AcademicPrograms/AcademicPrograms) and b) The NCES website (https://nces.ed.gov/ipeds/cipcode/Default.aspx?y=56). The Lightcast "Program Develop & Review" tool will also allow you search for CIP codes based on program keywords.

## Step 2: Identify SOC codes
You will also need to identify the associated SOC codes. Again, there are three typical ways of determining this: a) the O\*Net website (https://www.onetonline.org/) b) the CIP-SOC crosswalk provided by Lightcast c) keyword searches in Lightcast. The SOC codes will sometimes be useful for evaluating the labor market, but often times they will be overly broad and these caveats will need to be communicated to the end user.

## Step 3: Run Lightcast report
Login into EMSI/Lightcast (https://login.economicmodeling.com/login/login.php) and navigate to the "Program Develop & Review" module under the "program" subsection. Run the report using the selected CIP/SOC codes. When the report is completed save it, but do not export it as a pdf/word document. It will be easier to download the graphics individually.

## Step 4: Download CIP code data
Navigate to the "Program Data Download" tool under the "Data Download" section. Request the same exact data you requested in step 3 for the <b>last 2 years</b> and download this data. Save it into the data directory.

## Step 5: Process downloaded data with the python script
Start by making sure that the assets/plots directory exists. Then open the "process.py" script and update the "INPUT_DATA" variable to point to the downloaded program data. Then, simply run the script. This will result in two outcomes: a histogram of completion data and the completion quantiles. I used to include a growth-share plot in the report. However, this requires some extra work and is probably not useful enough to justify.

## Step 6: Create visuals
Return to the Lightcase report you generated earlier and download or screenshot the relevant visuals. You do not need to include all visuals, but these are the ones that are generally expected: "Program Overview", "Completions by Institution", "Completions Over Time", the "Labor Market Demand", "Demographic Breakdowns", "Hard/Soft Skills".

## Step 7: Create Report/Write Exec Summary/Proof
Copy the visuals into the report template and update the executive summary with the key information and any other observations you wish to include. Then proof the report and save as a PDF.
