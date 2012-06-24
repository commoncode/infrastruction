INSTALLED_APPS = (

	'infrastruction',

	# Intrastructure apps
	'grappelli.dashboard',
    'grappelli',
    'filebrowser',

    'django.contrib.admin',
    'django.contrib.admindocs',

    # Development helpers
	'django_extensions',
	'devserver',
)

# Filebrowser
FILEBROWSER_DEBUG = True

# Test for or create a dashboard file
FILEBROWSER_DIRECTORY = 'files/'
FILEBROWSER_MAX_UPLOAD_SIZE = 2097152
FILEBROWSER_SAVE_FULL_URL = False
FILEBROWSER_VERSIONS_BASEDIR = "versions"
FILEBROWSER_ADMIN_VERSIONS = {
    'admin_thumbnail': {'verbose_name': 'Admin Thumbnail', 'width': 60, 'height': 60, 'opts': 'crop'}, }
FILEBROWSER_ADMIN_VERSIONS = []


# Grappelli
GRAPPELLI_ADMIN_TITLE = 'Common Code'
GRAPPELLI_ADMIN_URL = '/admin/'

# TODO
# Test for and create a dashboard file

GRAPPELLI_INDEX_DASHBOARD = '.dashboard.CustomIndexDashboard'