from setuptools import setup

APP = ['Main.py']
DATA_FILES = ['login.yaml', 'logo.png']  # Include necessary data files
OPTIONS = {
    'packages': ['rumps', 'yaml', 'imaplib', 'smtplib', 'email'],
    'iconfile': 'logo.png',
    'plist': {
        'CFBundleDisplayName': 'MailMonitor',
        'CFBundleName': 'MailMonitor',
        'CFBundleIdentifier': 'com.yourcompany.YourAppName',
        'CFBundleVersion': "1.0.0",
        'LSBackgroundOnly': True,  # Enable background-only mode
        'NSUIElement': True,  # Hide from Dock and Command-Tab switcher
        'LSUIElement': True,  # Create a menu bar app without a dock icon
        'LSUIPresentationMode': 4,  # Ensure the application is brought to the foreground when launched
        'LSLaunchAtLogin': True,  # Enable launch at login
        'NSAppSleepDisabled': True,  # Prevent the app from being put to sleep
        'NSPrincipalClass': 'NSApplication',  # Set the principal class to NSApplication
        # Add any other necessary plist settings
    }
}


setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
