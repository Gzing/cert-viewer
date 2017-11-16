from flask.views import View
import logging
import json
from flask import flash
from flask import request
from flask import (url_for, redirect)
from flask.views import MethodView
from flask import Response

from cert_viewer import helpers
from cert_viewer.forms import BitcoinForm, SimpleRegistrationForm
from cert_viewer.notifier import Notifier
from cert_viewer.views.__init__ import render


class IssuerView(View):
    def __init__(self, view):
        self.view = view

    def dispatch_request(self, *args, **kwargs):
        """
        Returns identifying information for a Blockchain Certificate issuer.
        ---
        tags:
          - issuer
        parameters:
          - name: username
            in: path
            type: string
            required: true
        responses:
          200:
            description: The issuer identification at the specified path
            schema:
              id: issuer_response
              properties:
                issuerKeys:
                  type: string
                  description: The username
                  default: some_username
                revocationKeys:
                  type: string
                  description: The username
                  default: some_username
                id:
                  type: string
                  description: The username
                  default: some_username
                name:
                  type: string
                  description: The username
                  default: some_username
                email:
                  type: string
                  description: The username
                  default: some_username
                url:
                  type: string
                  description: The username
                  default: some_username
                introductionURL:
                  type: string
                  description: The username
                  default: some_username
                image:
                  type: string
                  description: The username
                  default: some_username
        """

        view_model = self.view(*args, **kwargs)
        return view_model


class IntroductionView(MethodView):
    def post(self):
        from cert_viewer import intro_store

        post_data = request.get_json()
        intro_store.insert(post_data)

        data = {
  "url":"http://18.216.177.52",
  "id": "http://18.216.177.52/_themes/default/issuer/the-issuer.json",
  "email": "sample-certificate@learningmachine.com",
  "introductionURL": "http://18.216.177.52/intro/",
  "name": "Sample Issuer",
  "type": "Issuer",
  "publicKeys": [
    {
      "publicKey": "ecdsa-koblitz-pubkey:14X3Xvw6kQA8iA2GZQKo4ZquBLNNamLcpQ",
      "created": "2017-05-11T20:04:18.095+00:00"
    }
  ],
  "introductionAuthenticationMethod": "none",
  "introductionSuccessURL": "https://certificates.learningmachine.com/api/organization/58ffaf130456e116107f68e6/accept-success",
  "introductionErrorURL": "https://certificates.learningmachine.com/api/organization/58ffaf130456e116107f68e6/accept-failed",
  "analyticsURL": "https://certificates.learningmachine.com/api/event/certificate",
  "issuerKeys": [
    {
      "date": "2016-05-01",
      "key": "1HYPitzbwR83M3Smw6GWs5XeQzBWoJAEeS"
    }
  ],
  "revocationKeys": [
    {
      "date": "2015-05-01",
      "key": "1C6KaoDpUgdQE7wKM5B9HhVXXjA8ymbfU6"
    }
  ]
}    
        
        resp = Response(data, status=200, mimetype='application/json')
        return resp

