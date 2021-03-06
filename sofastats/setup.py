from distutils.core import setup

setup(
name         = 'sofastats',
description  = 'Statistics Open For All',
version      = '1.2.2',
author       = 'Grant Paton-Simpson',
author_email = 'grant@sofastatistics.com',
package_dir  = {'sofastats':'sofa_main'},
packages     = ['sofastats', 
                'sofastats.boomslang', 
                'sofastats.dbe_plugins', 
                'sofastats.googleapi', 
                'sofastats.googleapi.atom', 
                'sofastats.googleapi.gdata', 
                'sofastats.googleapi.gdata.spreadsheet', 
                'sofastats.googleapi.gdata.docs', 
                'sofastats.googleapi.gdata.oauth', 
                'sofastats.googleapi.gdata.tlslite', 
                'sofastats.googleapi.gdata.tlslite.integration', 
                'sofastats.googleapi.gdata.tlslite.utils'], 
package_data = {'sofastats':['css/*', 
                             'images/*', 
                             '_internal/*', 
                             'locale/br/LC_MESSAGES/sofastats.mo', 
                             'locale/es_ES/LC_MESSAGES/sofastats.mo', 
                             'locale/gl_ES/LC_MESSAGES/sofastats.mo', 
                             'locale/hr_HR/LC_MESSAGES/sofastats.mo', 
                             'locale/ru_RU/LC_MESSAGES/sofastats.mo', 
                             'projs/*', 
                             'reports/sofastats_report_extras/*', 
                             'vdts/*']}
)
