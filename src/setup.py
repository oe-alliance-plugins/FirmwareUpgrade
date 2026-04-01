from setuptools import setup
import setup_translate

pkg = 'SystemPlugins.FirmwareUpgrade'
setup(name='enigma2-plugin-systemplugins-firmwareupgrade',
       version='3.0',
       description='Upgrade your system Firmware',
       package_dir={pkg: 'FirmwareUpgrade'},
       packages=[pkg],
       package_data={pkg: ['images/*.png', '*.png', '*.xml', 'locale/*/LC_MESSAGES/*.mo', 'plugin.png']},
       cmdclass=setup_translate.cmdclass,  # for translation
      )
