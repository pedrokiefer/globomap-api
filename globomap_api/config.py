"""
   Copyright 2018 Globo.com

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""
import os

ARANGO_DB = os.getenv('ARANGO_DB')
ARANGO_USERNAME = os.getenv('ARANGO_USERNAME')
ARANGO_PASSWORD = os.getenv('ARANGO_PASSWORD')
ARANGO_PROTOCOL = os.getenv('ARANGO_PROTOCOL')
ARANGO_HOST = os.getenv('ARANGO_HOST')
ARANGO_PORT = os.getenv('ARANGO_PORT')
FLASK_DEBUG = os.getenv('FLASK_DEBUG', False)
API_PLUGINS_CONFIG_FILE = 'api_plugins'
CORS = os.getenv('CORS', '').split(',')
SPECS = {
    'auth': 'globomap_api/specs/auth.json',
    'documents': 'globomap_api/specs/documents.json',
    'edges': 'globomap_api/specs/edges.json',
    'documents_partial': 'globomap_api/specs/documents_partial.json',
    'edges_partial': 'globomap_api/specs/edges_partial.json',
    'collections': 'globomap_api/specs/collections.json',
    'graphs': 'globomap_api/specs/graphs.json',
    'search': 'globomap_api/specs/search.json',
    'clear': 'globomap_api/specs/clear.json',
    'queries': 'globomap_api/specs/queries.json',
}

ZABBIX_UI_URL = os.getenv('ZABBIX_UI_URL')
ZABBIX_API_URL = os.getenv('ZABBIX_API_URL')
ZABBIX_API_USER = os.getenv('ZABBIX_API_USER')
ZABBIX_API_PASSWORD = os.getenv('ZABBIX_API_PASSWORD')

# Keystone
KEYSTONE_USERNAME = os.getenv('KEYSTONE_USERNAME')
KEYSTONE_PASSWORD = os.getenv('KEYSTONE_PASSWORD')

# Roles
ADMIN = 'globomap_admin'
READ = 'globomap_read'
WRITE = 'globomap_write'
COLLECTION = 'globomap_collection'
EDGE = 'globomap_edge'
GRAPH = 'globomap_graph'

# Meta Collections
META_COLLECTION = 'meta_collection'
META_GRAPH = 'meta_graph'
META_QUERY = 'meta_query'

# Logging
SENTRY_DSN = os.getenv('SENTRY_DSN')
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': 'level=%(levelname)s timestamp=%(asctime)s module=%(module)s line=%(lineno)d' +
            'message=%(message)s '
        }
    },
    'handlers': {
        'default': {
            'level': 'WARNING',
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stdout',
            'formatter': 'verbose',
        },
        'sentry': {
            'level': 'ERROR',
            'class': 'raven.handlers.logging.SentryHandler',
            'dsn': SENTRY_DSN,
        },
    },
    'loggers': {
        'api': {
            'handlers': ['default', 'sentry'],
            'level': 'WARNING',
            'propagate': True
        },
        'werkzeug': {'propagate': True},
    }
}
