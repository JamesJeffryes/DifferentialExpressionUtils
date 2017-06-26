# -*- coding: utf-8 -*-
############################################################
#
# Autogenerated by the KBase type compiler -
# any changes made here will be overwritten
#
############################################################

from __future__ import print_function
# the following is a hack to get the baseclient to import whether we're in a
# package or not. This makes pep8 unhappy hence the annotations.
try:
    # baseclient and this client are in a package
    from .baseclient import BaseClient as _BaseClient  # @UnusedImport
except:
    # no they aren't
    from baseclient import BaseClient as _BaseClient  # @Reimport


class DifferentialExpressionUtils(object):

    def __init__(
            self, url=None, timeout=30 * 60, user_id=None,
            password=None, token=None, ignore_authrc=False,
            trust_all_ssl_certificates=False,
            auth_svc='https://kbase.us/services/authorization/Sessions/Login'):
        if url is None:
            raise ValueError('A url is required')
        self._service_ver = None
        self._client = _BaseClient(
            url, timeout=timeout, user_id=user_id, password=password,
            token=token, ignore_authrc=ignore_authrc,
            trust_all_ssl_certificates=trust_all_ssl_certificates,
            auth_svc=auth_svc)

    def upload_differentialExpression(self, params, context=None):
        """
        Uploads the differential expression  *
        :param params: instance of type "UploadDifferentialExpressionParams"
           (*    Required input parameters for uploading Differential
           expression data string   destination_ref        -   object
           reference of Differential expression data. The object ref is
           'ws_name_or_id/obj_name_or_id' where ws_name_or_id is the
           workspace name or id and obj_name_or_id is the object name or id
           string   source_dir             -   directory with the files to be
           uploaded string   expressionSet_ref      -   expressionSet object
           reference string   tool_used              -   cufflinks, ballgown
           or deseq string   tool_version           -   version of the tool
           used *) -> structure: parameter "destination_ref" of String,
           parameter "source_dir" of String, parameter "expressionSet_ref" of
           String, parameter "tool_used" of String, parameter "tool_version"
           of String
        :returns: instance of type "UploadDifferentialExpressionOutput" (*   
           Output from upload differential expression    *) -> structure:
           parameter "obj_ref" of String
        """
        return self._client.call_method(
            'DifferentialExpressionUtils.upload_differentialExpression',
            [params], self._service_ver, context)

    def download_differentialExpression(self, params, context=None):
        """
        Downloads expression *
        :param params: instance of type
           "DownloadDifferentialExpressionParams" (* Required input
           parameters for downloading Differential expression string
           source_ref         -       object reference of expression source.
           The object ref is 'ws_name_or_id/obj_name_or_id' where
           ws_name_or_id is the workspace name or id and obj_name_or_id is
           the object name or id *) -> structure: parameter "source_ref" of
           String
        :returns: instance of type "DownloadDifferentialExpressionOutput" (* 
           The output of the download method.  *) -> structure: parameter
           "ws_id" of String, parameter "destination_dir" of String
        """
        return self._client.call_method(
            'DifferentialExpressionUtils.download_differentialExpression',
            [params], self._service_ver, context)

    def export_differentialExpression(self, params, context=None):
        """
        Wrapper function for use by in-narrative downloaders to download expressions from shock *
        :param params: instance of type "ExportParams" (* Required input
           parameters for exporting expression string   source_ref         - 
           object reference of Differential expression. The object ref is
           'ws_name_or_id/obj_name_or_id' where ws_name_or_id is the
           workspace name or id and obj_name_or_id is the object name or id
           *) -> structure: parameter "source_ref" of String
        :returns: instance of type "ExportOutput" -> structure: parameter
           "shock_id" of String
        """
        return self._client.call_method(
            'DifferentialExpressionUtils.export_differentialExpression',
            [params], self._service_ver, context)

    def status(self, context=None):
        return self._client.call_method('DifferentialExpressionUtils.status',
                                        [], self._service_ver, context)