# coding: utf-8

"""
    Circuit ID REST API

    # Introduction Circuit ID&reg; is an innovative cloud communications platform that redefines your connectivity experience. Our cutting-edge AI-powered solution seamlessly integrates calling, meetings, messaging, voicemail, fax, SIP Trunking, mobile broadband, and mobile phone services, accessible wherever you and your devices go.                  Whether you are a beginner getting started with our API or an experienced developer looking for advanced features, this documentation site will serve as your comprehensive guide.   We are excited to have you on board and are confident that this documentation site will empower you to leverage the full potential of our REST API.  If you have any questions or require further assistance, please don't hesitate to reach out to our support team.                  Happy coding!  # noqa: E501

    The version of the OpenAPI document: 0.47.21
    Contact: support@circuitid.com
    Generated by: https://openapi-generator.tech
"""

from circuitid_python.paths.callqueueagents.post import CreateCallQueueAgent
from circuitid_python.paths.callqueueagents.get import FindCallQueueAgents
from circuitid_python.paths.callqueueagents_id.get import GetCallQueueAgent
from circuitid_python.paths.callqueueagents_id.patch import PatchCallQueueAgent
from circuitid_python.paths.callqueueagents_id.delete import RemoveCallQueueAgent


class CallQueueAgentsApi(
    CreateCallQueueAgent,
    FindCallQueueAgents,
    GetCallQueueAgent,
    PatchCallQueueAgent,
    RemoveCallQueueAgent,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
