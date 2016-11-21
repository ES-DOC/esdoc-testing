##List of tests by month
* tasks w/o links do not have testing document created yet
* tasks should be completed by the end of the month listed
* tests for other documents will be added once they are finalized in the CIM (each TBD)
* only the schedule through NOV is firm

###September 2016
 * None
  
###October 2016
  - [x] [Questionnaire Responsible Party] (https://github.com/ES-DOC/esdoc-testing/blob/master/questionnaire/ResponsibleParty.md)
  
    **10/31 testing results: Pass, but can't observe the ES-DOC archive picking up the XML feed yet**
  - [x] [Questionnaire Basics ... create account etc] (https://github.com/ES-DOC/esdoc-testing/blob/master/questionnaire/Basics.md)
  
    **10/31 testing results: [No forgot password feature yet](https://github.com/ES-DOC/esdoc-questionnaire/issues/500) and a [misleading banner on failed password changes](https://github.com/ES-DOC/esdoc-questionnaire/issues/501)**
  - [x] [IPython Notebook Specialized Model Component](https://github.com/ES-DOC/esdoc-testing/blob/master/notebook/ModelWithoutCMIP5.md)
  
    **10/31 testing results: Notebook validation and CIM output not implemented yet**
 
  - [x] [pyesdoc Responsible Party] (https://github.com/ES-DOC/esdoc-testing/blob/master/pyesdoc/ResponsibleParty.md)
  
    **10/31 testing results: Unable to retrieve explicit versions of documents or delete documents using web API**
 
###November 2016
 - [ ] [cim2cdf Simulation dump data only] (https://github.com/ES-DOC/esdoc-testing/blob/master/cdf2cim/basics)
 - [ ] IPython Notebook Specialized Model Component initialized from a CMIP5 document (Mark)
 - [ ] pyesdoc Performance initial creation (David)
 - [ ] pyesdoc Machine initial creation (David)
 - [ ] Questionnaire Performance
 - [ ] Questionnaire Machine
  
###December 2016
  - [ ] Questionnaire Model Component with one child
  - [ ] Questionnaire Model Component with nested children 
  - [ ] Questionnaire Model Component with one child initialized from a CMIP5 document
  - [ ] IPython notebook validation of CIM output
  - [ ] cim2cdf integrated into ESGF stack
  - [ ] pyesdoc Ability to validate produced documents against the master specialization
  - [ ] Viewer render Model Component document
  
  
###January 2016
  - [ ] pyesdoc Simulation ... from previously harvested netCDF info
  - [ ] pyesdoc Ensemble ... from previously harvested netCDF info
  - [ ] pyesdoc Ensemble Member ... from previously harvested netCDF info
  - [ ] pyesdoc Ensemble Axis ... from previously harvested netCDF info
  - [ ] pyesdoc Ensemble Axis Member ... from previously harvested netCDF info
  - [ ] Questionnaire Model Component with two children intialized from a CMIP5 document
  - [ ] cim2cdf data dump of CMIP5 data and convert it to a CIM2 document
  
###Unscheduled
  - [ ] pyesdoc Citation
  - [ ] Questionnaire Citation
  - [ ] Questionnaire link small document (e.g. Citation) to Model Component
  - [ ] Questionnaire import CIM2 document
  - [ ] Quesitonnaire copy exisiting document for editing
  - [ ] cim2cdf data dump of CMIP6 data and convert to a CIM2 document (depends on when any CMIP6 data is available)
  - [ ] Viewer render Citation
  - [ ] Viewer render Performance
  - [ ] Viewer render Machine
  - [ ] Viewer render Simulation
  - [ ] Viewer render Ensemble
  - [ ] Viewer render Ensemble Member
  - [ ] Viewer render Ensemble Axis
  - [ ] pyesdoc Document referencing works
  - [ ] Questionnaire allow users to choose a Document reference
  - [ ] pyesdoc convert CMIP5 Model Component document to CIM2 (requires realm mapping from CMIP5 to CMIP6)
  - [ ] test that users can change Conformance table
  - [ ] test that users can generate (and publish) Conformance documents from Conformance table
  - [ ] test that institute_controlled_info_url ("further_further_info_url") can be added to an Ensembles document and edited
  

