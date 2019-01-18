import pytest

from cfn_get_export_value import get_export_value
from cfn_get_export_value.cfn_get_export_value import ExportNotFoundError


def test__get_export_value__value_exists_in_first_page(mocker):
    def fake_list_exports(next_token=None, client=None, session=None):
        if not next_token:
            return {
                u'Exports': [
                    {
                        u'ExportingStackId': 'arn:aws:cloudformation:us-east-1:123456789123:stack/stack1/a366f690-e71d-11e5-a15b-500c524058c6',
                        u'Value': 'export-1-value',
                        u'Name': 'export-1-name'
                    },
                    {
                        u'ExportingStackId': 'arn:aws:cloudformation:us-east-1:123456789123:stack/stack1/a366f690-e71d-11e5-a15b-500c524058c6',
                        u'Value': 'export-2-value',
                        u'Name': 'export-2-name'
                    },
                    {
                        u'ExportingStackId': 'arn:aws:cloudformation:us-east-1:123456789123:stack/stack2/bae09890-e71c-11e5-ac25-50d5cafe76fe',
                        u'Value': 'export-3-value',
                        u'Name': 'export-3-key'
                    },
                    {
                        u'ExportingStackId': 'arn:aws:cloudformation:us-east-1:123456789123:stack/stack3/f3d2a120-c3d0-11e6-9ef7-500c5cc81217',
                        u'Value': 'export-4-value',
                        u'Name': 'export-4-key'
                    },
                    {
                        u'ExportingStackId': 'arn:aws:cloudformation:us-east-1:123456789123:stack/stack3/f3d2a120-c3d0-11e6-9ef7-500c5cc81217',
                        u'Value': 'export-5-value',
                        u'Name': 'export-5-key'
                    }
                ],
                'ResponseMetadata': {
                    'RetryAttempts': 0,
                    'HTTPStatusCode': 200,
                    'RequestId': '561d8003-c617-11e6-ace2-4792e10afcfc',
                    'HTTPHeaders': {
                        'x-amzn-requestid': '561d8003-c617-11e6-ace2-4792e10afcfc',
                        'date': 'Mon, 19 Dec 2016 18:17:00 GMT',
                        'content-length': '1946',
                        'content-type': 'text/xml'
                    }
                }
            }

    _mock_list_exports(fake_list_exports, mocker)

    # When
    val = get_export_value(name='export-4-key')

    # Then
    assert val == 'export-4-value'


def test__get_export_value__value_exists_in_another_page(mocker):
    def fake_list_exports(next_token=None, client=None, session=None):
        if not next_token:
            return {
                u'Exports': [
                    {
                        u'ExportingStackId': 'arn:aws:cloudformation:us-east-1:123456789123:stack/stack1/a366f690-e71d-11e5-a15b-500c524058c6',
                        u'Value': 'export-1-value',
                        u'Name': 'export-1-name'
                    },
                    {
                        u'ExportingStackId': 'arn:aws:cloudformation:us-east-1:123456789123:stack/stack1/a366f690-e71d-11e5-a15b-500c524058c6',
                        u'Value': 'export-2-value',
                        u'Name': 'export-2-name'
                    },
                    {
                        u'ExportingStackId': 'arn:aws:cloudformation:us-east-1:123456789123:stack/stack2/bae09890-e71c-11e5-ac25-50d5cafe76fe',
                        u'Value': 'export-3-value',
                        u'Name': 'export-3-value'
                    },
                ],
                u'NextToken': 'abcd'
            }
        if next_token == 'abcd':
            return {
                u'Exports': [
                    {
                        u'ExportingStackId': 'arn:aws:cloudformation:us-east-1:123456789123:stack/stack3/f3d2a120-c3d0-11e6-9ef7-500c5cc81217',
                        u'Value': 'export-4-value',
                        u'Name': 'export-4-key'
                    },
                    {
                        u'ExportingStackId': 'arn:aws:cloudformation:us-east-1:123456789123:stack/stack3/f3d2a120-c3d0-11e6-9ef7-500c5cc81217',
                        u'Value': 'export-5-value',
                        u'Name': 'export-5-key'
                    }
                ],
            }

    _mock_list_exports(fake_list_exports, mocker)

    # When
    val = get_export_value(name='export-4-key')

    # Then
    assert val == 'export-4-value'


def test__get_export_value__name_does_not_exist(mocker):
    def fake_list_exports(next_token=None, client=None, session=None):
        if not next_token:
            return {
                u'Exports': [
                    {
                        u'ExportingStackId': 'arn:aws:cloudformation:us-east-1:123456789123:stack/stack1/a366f690-e71d-11e5-a15b-500c524058c6',
                        u'Value': 'export-1-value',
                        u'Name': 'export-1-name'
                    },
                    {
                        u'ExportingStackId': 'arn:aws:cloudformation:us-east-1:123456789123:stack/stack1/a366f690-e71d-11e5-a15b-500c524058c6',
                        u'Value': 'export-2-value',
                        u'Name': 'export-2-name'
                    },
                    {
                        u'ExportingStackId': 'arn:aws:cloudformation:us-east-1:123456789123:stack/stack2/bae09890-e71c-11e5-ac25-50d5cafe76fe',
                        u'Value': 'export-3-value',
                        u'Name': 'export-3-value'
                    },
                ],
                u'NextToken': 'abcd'
            }
        if next_token == 'abcd':
            return {
                u'Exports': [
                    {
                        u'ExportingStackId': 'arn:aws:cloudformation:us-east-1:123456789123:stack/stack3/f3d2a120-c3d0-11e6-9ef7-500c5cc81217',
                        u'Value': 'export-4-value',
                        u'Name': 'export-4-key'
                    },
                    {
                        u'ExportingStackId': 'arn:aws:cloudformation:us-east-1:123456789123:stack/stack3/f3d2a120-c3d0-11e6-9ef7-500c5cc81217',
                        u'Value': 'export-5-value',
                        u'Name': 'export-5-key'
                    }
                ],
            }

    _mock_list_exports(fake_list_exports, mocker)

    # When
    with pytest.raises(ExportNotFoundError):
        get_export_value(name='export-6-key')


def _mock_list_exports(fake_list_exports, mocker):
    mocker.patch('cfn_get_export_value.cfn_get_export_value._list_exports', side_effect=fake_list_exports)
