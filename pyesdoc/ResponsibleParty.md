## Use py-esdoc to create & publish a ResponsibleParty
1. Create and publish a valid person and an organization
    1. Create valid person and organization CIM documents in py-esdoc
    
    `rm ~/esdoc-testing/pyesdoc/responsible_party/valid/*`
    ./create_valid_responsible_party.py
    2. Validate documents using esdoc shell
    `esdoc-pyesdoc-validate <file>`
    3. Archive documents
    `source $ESDOC_HOME/bash/init.sh; activate_venv pyesdoc`
    `rm $ESDOC_HOME/repos/esdoc-archive/esdoc/beta-test/pyesdoc/*`
    `python $ESDOC_HOME/bash/cmip6/archive_documents.py --source-dir=/esdoc/testing/valid --target-dir=$ESDOC_HOME/repos/esdoc-archive/esdoc/beta-test/pyesdoc/`
    4. Publish using esdoc shell
    esdoc-api-db-reset
    esdoc-api-db-ingest
    5. See both records in the database
    psql -U esdoc_db_user esdoc_api
       select * from docs.tbl_document;
    6. See both records through the web API service
       Grab the document UID from the database
       Project must be in all capital letters
http://<server>:5000/2/document/search-id?client=ESDOC-SEARCH&encoding=json&project=BETA-TEST&id=<ID>&version=latest
2. Verify CIM validator
    1. Create an invalid person and organization in py-esdoc
       ./create_invalid_reponsible_party.py
    2. See validator fail
       esdoc-pyesdoc-validate <file>
       Comment: from the validator error it's not clear which attribute is the problem or what's the problem
    3. Archive documents
       As in Step 1c
    4. Verify publish command won’t work with invalid CIM document
       As in Step 1c
3. Verify unpublishing
    1. Do step #1
    2. Unpublish using esdoc shell
    3. Verify records no longer appear in Viewer
    4. Republish (step #1 again)
4. Verify basic CIM versioning ability
    1. Do step #1 -- OK
    2. Update person and organization details -- OK
       ./create_valid_responsible_party_version2.py
    3. Publish updated records -- OK
    4. Observe both sets of records appear in Viewer, and that the more recent one looks to be default
