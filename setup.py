import setuptools

def readme():
    with open('README.rst') as f:
        return f.read()

setuptools.setup(
    name="telnetsrv",
    packages = ["telnetsrv"],
    version = "1.0.0",
    description = "Telnet server handler library",
    long_description = readme(),
    author = "Ian Epperson",
    author_email = "ian@epperson.com",
    extras_require = {
        'green': ['gevent'],
        'ssh': ['paramiko'],
    },
)
