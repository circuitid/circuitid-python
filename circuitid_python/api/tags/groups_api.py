# coding: utf-8

"""
    Circuit ID REST API

    # Introduction Circuit ID&reg; is an innovative cloud communications platform that redefines your connectivity experience. Our cutting-edge AI-powered solution seamlessly integrates calling, meetings, messaging, voicemail, fax, SIP Trunking, mobile broadband, and mobile phone services, accessible wherever you and your devices go.                  Whether you are a beginner getting started with our API or an experienced developer looking for advanced features, this documentation site will serve as your comprehensive guide.   We are excited to have you on board and are confident that this documentation site will empower you to leverage the full potential of our REST API.  If you have any questions or require further assistance, please don't hesitate to reach out to our support team.                  Happy coding!  # noqa: E501

    The version of the OpenAPI document: 0.47.22
    Contact: support@circuitid.com
    Generated by: https://openapi-generator.tech
"""

from circuitid_python.paths.groups.post import CreateGroup
from circuitid_python.paths.groups.get import FindGroups
from circuitid_python.paths.groups_id.get import GetGroup
from circuitid_python.paths.groups_id.patch import PatchGroup
from circuitid_python.paths.groups_id.delete import RemoveGroup


class GroupsApi(
    CreateGroup,
    FindGroups,
    GetGroup,
    PatchGroup,
    RemoveGroup,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
