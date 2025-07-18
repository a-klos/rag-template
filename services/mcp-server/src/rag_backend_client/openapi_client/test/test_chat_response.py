# coding: utf-8

"""
STACKIT RAG

The perfect rag solution.

The version of the OpenAPI document: 1.0.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501


import unittest

from rag_backend_client.openapi_client.models.chat_response import ChatResponse


class TestChatResponse(unittest.TestCase):
    """ChatResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ChatResponse:
        """Test ChatResponse
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `ChatResponse`
        """
        model = ChatResponse()
        if include_optional:
            return ChatResponse(
                answer = '',
                finish_reason = '',
                citations = [
                    {"metadata":[{"key":"key","value":"value"},{"key":"key","value":"value"}],"page_content":"some text","type":"TEXT"}
                    ]
            )
        else:
            return ChatResponse(
                answer = '',
                finish_reason = '',
                citations = [
                    {"metadata":[{"key":"key","value":"value"},{"key":"key","value":"value"}],"page_content":"some text","type":"TEXT"}
                    ],
        )
        """

    def testChatResponse(self):
        """Test ChatResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
