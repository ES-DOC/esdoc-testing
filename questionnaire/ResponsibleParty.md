## Use the Questionnaire to create & publish a ResponsibleParty
These tests use [cim2.questionnaire.es-doc.org](http://cim2.questionnaire.es-doc.org) and assume there's an existing CMIP6 project that you are a member of. If there's an existing CMIP6 project but you're not a member of it, go to the project, click "Join project", and have Allyn accept the request.
1. Create and publish a valid person and an organization
    a. Create a valid person and organization
    b. Validate
    c. Publish
    d. See both records in the Viewer
2. Verify CIM validator
    a. Create an invalid person and organization
    b. See validator fail
    c. Verify Q won't publish an invalid CIM document
3. Verify unpublishing
    a. Do step #1
    b. Unpublish
    c. Verify records no longer appear in Viewer
    d. Republish (step #1 again)
4. Verify basic CIM versioning ability
    a. Do step #1
    b. Update person and organization details
    c. Publish updated records
    d. Observe both sets of records appear in Viewer, and that the more recent one looks to be default

Testing results: No testing done so far
