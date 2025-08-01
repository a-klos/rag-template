# coding: utf-8

"""
STACKIT RAG

The perfect rag solution.

The version of the OpenAPI document: 1.0.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501


import unittest

from rag_backend_client.openapi_client.models.chat_history import ChatHistory


class TestChatHistory(unittest.TestCase):
    """ChatHistory unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ChatHistory:
        """Test ChatHistory
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `ChatHistory`
        """
        model = ChatHistory()
        if include_optional:
            return ChatHistory(
                messages = [
                    rag_backend_client.openapi_client.models.chat_history_message.chat_history_message(
                        role = 'user',
                        message = '', )
                    ]
            )
        else:
            return ChatHistory(
                messages = [
                    rag_backend_client.openapi_client.models.chat_history_message.chat_history_message(
                        role = 'user',
                        message = '', )
                    ],
        )
        """

    def testChatHistory(self):
        """Test ChatHistory"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
