# cfn-get-export-value
Retrieve a AWS CloudFormation exported value by its name

[![Build Status](https://travis-ci.org/PokaInc/cfn-get-export-value.svg?branch=master)](https://travis-ci.org/PokaInc/cfn-get-export-value)

## Motivation
AWS exposes [an API to list CloudFormation exports](http://boto3.readthedocs.io/en/latest/reference/services/cloudformation.html#CloudFormation.Client.list_exports). However, retrieving the value of a particular export requires that you iterate over all the exports. This module aims to make this process easier.

## Installation
`pip install cfn_get_export_value`

## Usage
Suppose you have a CloudFormation stack that has an Output that exports its value (`some-value`) by the name `some-name`.
You can retrieve the value of `some-name` like this:

```python
from cfn_get_export_value import get_export_value

value = get_export_value('some-name')
# value: "some-value"
```

You can also specify a boto3 session argument:

```python
get_export_value('some-name', session=some_session)
```
