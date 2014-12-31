'''plugin.py

'''
import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit

class AachenThemePlugin(plugins.SingletonPlugin):
    '''Theme for daten.aachen.de

    '''
    plugins.implements(plugins.IConfigurer)

    def update_config(self, config):
         toolkit.add_template_directory(config, 'templates')
         toolkit.add_resource('fanstatic', 'aachen_theme')
