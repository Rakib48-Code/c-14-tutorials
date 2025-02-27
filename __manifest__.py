{
    'name' : 'Hospital Management',
    'version' : '14.1.1.1.1',
    'summary' : 'Hospital Management System',
    'category' : 'Hospital',
    'author' : 'Rakib Hasan',
    'depends' : ['mail'],
    'data' : [
        'security/ir.model.access.csv',

        'data/patient_sequence.xml',
        'data/patient_reference.xml',

        'views/menu.xml',
        'views/patient_view.xml',
        'views/appointment_view.xml',

        'reports/report_action.xml',
        'reports/report_template.xml',
    ],
    'sequence' : 2,
    'application' : True,
    'installable' : True,
}