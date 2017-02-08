from distutils.core import setup

setup(
    name='cfn_get_export_value',
    packages=['cfn_get_export_value'],  # this must be the same as the name above
    version='0.0.2',
    description='Get an exported value in AWS CloudFormation',
    author='Simon-Pierre Gingras',
    author_email='spgingras@poka.io',
    url='https://github.com/PokaInc/cfn-get-export-value',  # use the URL to the github repo
    download_url='https://github.com/PokaInc/cfn-get-export-value/tarball/0.0.1',
    keywords=['aws', 'cloudformation', 'exports'],  # arbitrary keywords
    install_requires=[
        'boto3',
    ],
    classifiers=[],
)
