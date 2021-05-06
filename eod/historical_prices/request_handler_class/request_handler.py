import requests
import json
from typing import Dict
import logging

class RequestHandler():
    def __init__(self, api_key:str, timeout:int):
        # general parameters of the api
        self.api_key = api_key
        self.timeout = timeout
        self.resp = None
        
    # -------------------------------------------
    # Methods for data processing
    # -------------------------------------------
        
    def handle_request(self, endpoint_url, query_params: Dict[str, str]={}):
        """
        central point to handle the requests of the API

        Parameters
        ----------
        query_params : Dict[str, str], optional
            query parameters of the request. The default is {}.

        Returns
        -------
        dict or list
            response from the API.

        """
        # append the api key and format to the parameters 
        query_params_ = self.__append_fmt(query_params)
        
        self.resp = requests.get(url=endpoint_url,
                                 params=query_params_,
                                 timeout=self.timeout)
        
        if self.resp.status_code == 200:
            return self.resp.json()
        else:
            self.resp.raise_for_status()
    
    def __append_fmt(self, dict_to_append):
        """
        Append the type of format and api key to the query parameters

        Parameters
        ----------
        dict_to_append : dict
            paramters of the request.

        Returns
        -------
        dict_to_append : dict
            full dict of paramters of the request.

        """
        dict_to_append['fmt'] = 'json'
        dict_to_append['api_token'] = self.api_key
        return dict_to_append