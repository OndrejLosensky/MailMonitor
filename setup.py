from setuptools import setup

APP = ['Main.py']
DATA_FILES = ['login.yaml', 'logo.png']  # Include necessary data files
OPTIONS = {
    'packages': ['rumps', 'yaml', 'imaplib', 'smtplib', 'email'],  # Add necessary packages
    'iconfile': 'logo.png',  # Provide the path to the icon file in .icns format
    'plist': {
        'CFBundleDisplayName': 'MailMonitor',  # Set the display name of your application
        'CFBundleName': 'MailMonitor',  # Set the bundle name of your application
        'CFBundleIdentifier': 'com.yourcompany.YourAppName',  # Set the bundle identifier
        'CFBundleVersion': "1.0.0",  # Set the version of your application
        'LSUIElement': True,  # Set to True to create a menu bar app without a dock icon
        'NSHumanReadableCopyright': 'Copyright 2024, YourCompany',
        # Add any other necessary plist settings
    }
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
