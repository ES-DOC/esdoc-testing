## Create a Jupyter notebook ocean realm template, fill out notebook, and generate CIM documents
These tests require an ES-DOC shell environment. See the [wordpress site](http://wordpress.es-doc.org) for [shell installation instructions](http://wordpress.es-doc.org/how-to-install-shell/) and [additional installation instructions and usage notes](http://wordpress.es-doc.org/stack-installation-faq/).

1. Create model notebook template
    1. Edit `$ESDOC_HOME/bash/cmip6/write_model_notebooks.conf` to add modeling center, model name, and realm (*gfdl*, *cm4*, and *ocean* for this example) model/realm alongside Mark's IPSL example.
    2. Generate notebook
    
      ```
       rm $ESDOC_HOME/repos/esdoc-docs/cmip6/models/notebooks/*/*/*
       esdoc-cmip6-write-model-notebooks
      ```
      
2. Fill out notebook within JupyterHub
    1. Start Jupyter notebook service
    
      ```
      source $ESDOC_HOME/bash/init.sh
      activate_venv pyesdoc
      cd $ESDOC_HOME/repos/esdoc-docs/cmip6/models/notebooks
      jupyter notebook --ip <hostname>
      ```

    2. Point web browser to `<hostname>:8888`
    3. Within Jupyter file browser, navigate to `gfdl/cm4`, and click `ocean.ipynb`, which will launch notebook editor in new tab
    4. Fill out form

3. Test validator

    **Validator doesn't work yet**
    1. Fill out form correctly, and see validator pass
    2. Fill out form incorrectly, and see validator fail
    
3. Generate CIM documents
    1. Within Jupyter notebook, select "Kernel => Restart and Run All"
    2. Verify CIM documents are produced
    **Notebooks don't generate CIM documents yet, but they do generate preliminary JSON output**
    3. Archive, publish, and retrieve document in web API
