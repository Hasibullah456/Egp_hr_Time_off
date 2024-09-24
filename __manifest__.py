{
    'name' : 'egp_hr_time_off',
    'version': '1.2',
    'category': 'time off',
    'sequence': -100,
    'description': "Egp hr management",
    'depends': ['hr','hr_holidays'],
    'data': [
        # 'data/default_allocation_data.xml',
        'security/security.xml',
        'security/ir.model.access.csv',

        'data/egp_hr_timeoff_hr_leave_type_default_data.xml',
        'report/egp_hr_time_off_report.xml',
        # 'report/egh_hr_time_off_report_days.xml',
        'data/default_user.xml',

    ],
    'installable': True,
    'auto_install': True,
    'application': True,
    'assets': {
        'web.assets_backend': [
            # 'bus/static/src/*.js',
            # 'bus/static/src/services/**/*.js',
            # 'bus/static/src/workers/websocket_worker.js',
            # 'bus/static/src/workers/websocket_worker_utils.js',
        ],
        'web.assets_frontend': [
            # 'bus/static/src/*.js',
            # 'bus/static/src/services/**/*.js',
            # ('remove', 'bus/static/src/services/assets_watchdog_service.js'),
            # ('remove', 'bus/static/src/simple_notification_service.js'),
            # 'bus/static/src/workers/websocket_worker.js',
            # 'bus/static/src/workers/websocket_worker_utils.js',
        ],
        'web.tests_assets': [
            # 'bus/static/tests/helpers/**/*',
        ],
        'web.qunit_suite_tests': [
            # 'bus/static/tests/**/*.js',
            # ('remove', 'bus/static/tests/helpers/**/*'),
        ],
        'bus.websocket_worker_assets': [
            # 'web/static/src/module_loader.js',
            # 'bus/static/src/workers/*',
        ],
    },
    'license': 'LGPL-3',
}
