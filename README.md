# SSRS  project

SSRS module used for get data from FAST/TOOLS SCADA system and peresent it in special format. Generally used for integration of SSRS with FAST/TOOLS scada.
***
## Features
- Read data from FAST/TOOLS
- Print retrieved data to the stdout in the XML or JSON format 
- Save retrieved data to file in XML or JSON format
***
## Installation
1. Install python 3.7
2. Clone project from Github
   ```
   git clone git@github.com:ead3471/ssrs.git
   ```
3. Create virtual environment with python 2.7
   ```
   virtualenv -p `which python2.7` venv
   ```
4. Add location of dss.pyd(distributed with FAST/TOOLS) to PYTHONPATH

5. At this moment script tuned to work with distinct FAST/TOOLS project. You can change reported items by rewrite ItemsLists class in unit_items.py

5. Run FAST/TOOLS

6. In command line navigate to srs/ssrs folder

7. Run script
    By default script creates report for ItemsLists.unit_30_items in xml format.
    ```
    python sql_request_handler.py
    ```
8. You can get run script parameters with 
     ```
        python sql_request_handler.py
     ```

    
        



