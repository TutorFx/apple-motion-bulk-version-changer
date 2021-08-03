from setuptools import setup

APP=['Versao.py']
OPTIONS = {
    'argv_emulation': True,
    'iconfile': 'leno.icns'
}

setup(
    app=APP,
    options={'py2app': OPTIONS},
    setup_requires=['py2app']
)

#python3 setup.py py2app -A