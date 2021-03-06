# -*- coding: utf-8 -*-
#BEGIN_HEADER
import logging
import os
import escher

from installed_clients.KBaseReportClient import KBaseReport
#END_HEADER


class kb_escher:
    '''
    Module Name:
    kb_escher

    Module Description:
    A KBase module: kb_escher
    '''

    ######## WARNING FOR GEVENT USERS ####### noqa
    # Since asynchronous IO can lead to methods - even the same method -
    # interrupting each other, you must be *very* careful when using global
    # state. A method could easily clobber the state set by another while
    # the latter method is running.
    ######################################### noqa
    VERSION = "0.0.1"
    GIT_URL = "git@github.com:Fxe/kb_escher.git"
    GIT_COMMIT_HASH = "f3ba015a4892b92f36c8329b051c493b7994f1e7"

    #BEGIN_CLASS_HEADER
    #END_CLASS_HEADER

    # config contains contents of config file in a hash or None if it couldn't
    # be found
    def __init__(self, config):
        #BEGIN_CONSTRUCTOR
        self.serviceWizardURL = config['srv-wiz-url']
        self.shared_folder = config['scratch']
        print(self.serviceWizardURL, self.shared_folder)
        logging.basicConfig(format='%(created)s %(levelname)s: %(message)s',
                            level=logging.INFO)
        #END_CONSTRUCTOR
        pass


    def list_maps(self, ctx, params):
        """
        :param params: instance of mapping from String to unspecified object
        :returns: instance of mapping from String to unspecified object
        """
        # ctx is the context object
        # return variables are: output
        #BEGIN list_maps
        
        namespace_filter = None
        
        local_maps = escher.list_cached_maps()
        output = {'maps' : local_maps}
        
        #END list_maps

        # At some point might do deeper type checking...
        if not isinstance(output, dict):
            raise ValueError('Method list_maps return value ' +
                             'output is not type dict as required.')
        # return the results
        return [output]

    def list_models(self, ctx, params):
        """
        :param params: instance of mapping from String to unspecified object
        :returns: instance of mapping from String to unspecified object
        """
        # ctx is the context object
        # return variables are: output
        #BEGIN list_models
        
        namespace_filter = None
        
        local_models = escher.list_cached_models()
        output = {'models' : local_models}
        
        #END list_models

        # At some point might do deeper type checking...
        if not isinstance(output, dict):
            raise ValueError('Method list_models return value ' +
                             'output is not type dict as required.')
        # return the results
        return [output]

    def get_model(self, ctx, params):
        """
        :param params: instance of mapping from String to unspecified object
        :returns: instance of mapping from String to unspecified object
        """
        # ctx is the context object
        # return variables are: output
        #BEGIN get_model
        
        output = {}
        
        #END get_model

        # At some point might do deeper type checking...
        if not isinstance(output, dict):
            raise ValueError('Method get_model return value ' +
                             'output is not type dict as required.')
        # return the results
        return [output]

    def get_map(self, ctx, params):
        """
        :param params: instance of mapping from String to unspecified object
        :returns: instance of mapping from String to unspecified object
        """
        # ctx is the context object
        # return variables are: output
        #BEGIN get_map
        
        output = {}
        
        #END get_map

        # At some point might do deeper type checking...
        if not isinstance(output, dict):
            raise ValueError('Method get_map return value ' +
                             'output is not type dict as required.')
        # return the results
        return [output]
    def status(self, ctx):
        #BEGIN_STATUS
        returnVal = {'state': "OK",
                     'message': "",
                     'version': self.VERSION,
                     'git_url': self.GIT_URL,
                     'git_commit_hash': self.GIT_COMMIT_HASH}
        #END_STATUS
        return [returnVal]
