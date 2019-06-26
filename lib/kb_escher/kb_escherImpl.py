# -*- coding: utf-8 -*-
#BEGIN_HEADER
import logging
import os

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
    GIT_URL = ""
    GIT_COMMIT_HASH = ""

    #BEGIN_CLASS_HEADER
    #END_CLASS_HEADER

    # config contains contents of config file in a hash or None if it couldn't
    # be found
    def __init__(self, config):
        #BEGIN_CONSTRUCTOR
        self.callback_url = os.environ['SDK_CALLBACK_URL']
        self.shared_folder = config['scratch']
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
        
        output = {}
        
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
        
        output = {}
        
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
