# cfn-get-export-value
Retrieve a AWS CloudFormation exported value by its name

## Installation
`pip install cfn-get-export-value`

## Usage
Suppose you have a CloudFormation stack that has an Output that exports its value (`some-value`) by the name `some-name`.
You can retrieve the value of `some-name` like this:

```python
from cfn_get_export_value import get_export_value

value = get_export_value('some-name')
# value: "some-value"
```
