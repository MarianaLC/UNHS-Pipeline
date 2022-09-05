In the context of Universal Newborn Hearing Screening (UNHS), there is a range of information that should be recorded, namely data related to pregnancy, birth and newborn, identification of risk factors for deafness and Apgar score results. Therefore, one of the aims of this study is to develop an EHR template to be completed under the UNHS, containing information relating to birth registration (including Apgar scores), the hearing screening process and the identification of risk factors for deafness. To construct the template the openEHR specifications will be followed as the first step of a UNHS research pipeline. The next step is to simulate a real situation in which different fields would be extracted from the template, filled with real patient data. However, as the template was not actually filled by patients, data from a private dataset containing the same fields present in the developed template was used. This data was then mapped to the fields in the template and stored in a JSON file in MongoDB. With the data stored in MongoDB, it is possible to go to the next step, which is modelling the Data Warehouse (DW). This includes creating fact and dimension tables and choosing an appropriate architecture. In the next steps, the ETL process will be executed, which ends with the populating of the DW. Finally, from the data present in the DW it is possible to extract information and develop statistical indicators relating to the UNHS, which can be incorporated into a Business Intelligence (BI) interface. 

This is a file that serves as a guide to the functions that python files have.

openehr2.py - Responsible for mapping the paths

mongoimp.py - Responsible for populating the MongoDB database

ranu.mwb - Responsible for modelling the Data Warehouse

dims.sql - Responsible for populating the dimension tables of ranu.mwb

sqlimp.py - Responsible for populating the fact table (Data Warehouse)

RANU.twb - Contains the report of the RANU nominees performed in Tableau


