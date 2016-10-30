## Use py-esdoc to create & publish a ResponsibleParty
These tests require an ES-DOC shell environment. See the [wordpress site](http://wordpress.es-doc.org) for [shell installation instructions](http://wordpress.es-doc.org/how-to-install-shell/) and [additional installation instructions and usage notes](http://wordpress.es-doc.org/stack-installation-faq/). Scripts that start with `./` are in this git repo.

### Setup
Temporarily modify the shell configuration files to only use CIM documents created during these tests.

1. In `$ESDOC_HOME/ops/config/pyesdoc.conf`,
    + Add document source called beta-test
      ```
      {
          "name": "beta-test",
          "feeds": [
              {
                  "encoding": "json",
                  "is_active": true,
                  "source": "pyesdoc",
                  "url": "none"
              }
          ]
     },
     ```
    + Turn other sources off by setting their `is_active` to `false`.
2. In `$ESDOC_HOME/ops/config/api.conf`, change `"projects": "cmip6-draft",` to `"projects": "beta-test"`,

### Tests
1. Create and publish a valid person and an organization
    1. Create valid person and organization CIM documents in py-esdoc.
    
      ```
      rm ~/esdoc-testing/pyesdoc/responsible_party/*
      ./create_responsible_party.py
      ```
    
    2. Validate
    
      ```
      esdoc-pyesdoc-validate ~/esdoc-testing/pyesdoc/responsible_party/<file>
      ```
    
    3. Archive
    
      ```
    source $ESDOC_HOME/bash/init.sh
    activate_venv pyesdoc
    rm $ESDOC_HOME/repos/esdoc-archive/esdoc/beta-test/pyesdoc/*
    python $ESDOC_HOME/bash/cmip6/archive_documents.py --source-dir=$HOME/esdoc-testing/pyesdoc/responsible_party --target-dir=$ESDOC_HOME/repos/esdoc-archive/esdoc/beta-test/pyesdoc
    deactivate
      ```
      
    4. Publish
    
      ```
    esdoc-api-daemons-kill
    esdoc-api-db-reset
    esdoc-api-daemons-init
    esdoc-api-db-ingest
      ```
      
    5. See records in the database
    
      ```
    psql -U esdoc_db_user esdoc_api
    select * from docs.tbl_document;
       ```
       
    6. See records through the web API service
    
       Get the document UID from the database, and project must be in all capital letters.
       
         ```
http://<server>:5000/2/document/search-id?client=ESDOC-SEARCH&encoding=json&project=BETA-TEST&id=<ID>&version=latest
         ```
         
2. Verify CIM validator
    1. Create an invalid organization in py-esdoc; in this case, using a string for a URL rather than a proper CIM OnlineResource property.
    
      ```
       rm ~/esdoc-testing/pyesdoc/responsible_party/*
       ./create_invalid_responsible_party.py
       ```
       
    2. See validator fail
    
       *Note: from the validator error it's not clear which attribute is the problem*

    
      ```
      esdoc-pyesdoc-validate ~/esdoc-testing/pyesdoc/responsible_party/<file>

      ```
      
    3. Archive documents
       As in Step 1-iii
     
    4. Verify publish command won’t work with invalid CIM document
       As in Step 1-iv

4. Verify CIM versioning ability
    1. Do step #1
    2. Update person and organization details, and publish updated record. This script retrieves the ResponsibleParty document with the given UID, appends ", updated" to the party's name, increases the document version by 1, and then republishes.
    
      ```
       ./update_responsible_party.py <UID>
      ```
      
    3. Verify updated record is in database, as in step 1-v
    4. Verify both sets of records can be retrieved from API as in step 1-vi using version=1, version=2, and that the version 2 document is retrieved when version=latest

3. Verify unpublishing
**Not currently possible with esdoc shell but does appear possible through the web API**
    1. Do step #1
    2. Unpublish using esdoc shell
    3. Verify records no longer available in web API
