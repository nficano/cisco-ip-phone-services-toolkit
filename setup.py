"""setup instructions for Cisco IP Phone Service Factory."""
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('LICENSE') as readme_file:
    license = readme_file.read()

requires = [
    'Jinja2>=2.10.1',
]

setup(
    name='cisco_ip_phone_services',
    version='2.0.22',
    author='Nick Ficano',
    author_email='nficano@gmail.com',
    packages=['cisco_ip_phone_services'],
    url='https://github.com/nficano/phone-services',
    license=license,
    entry_points={},
    package_data={
        'cisco_ip_phone_services': ['templates/*'],
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: MacOS',
        'Operating System :: Microsoft',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    description=('Cisco IP Phone Service Factory'),
    long_description=readme,
    install_requires=requires,
    zip_safe=True,
)
