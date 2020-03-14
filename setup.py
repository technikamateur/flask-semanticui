from setuptools import setup


setup(
    name='Flask-Semantic-UI',
    version='1.0',
    url='https://github.com/technikamateur/flask-semanticui',
    author='Daniel aka technikamateur',
    author_email='daniel@technikamateur.de',
    description='An simple extension that includes Semantic UI in your project',
    packages=['flask_semanticui'],
    include_package_data=True,
    install_requires=[
        'Flask>=1.0'
    ]
)
