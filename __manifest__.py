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
        'views/menu.xml',
        'views/patient_view.xml',
    ],
    'sequence' : 2,
    'application' : True,
    'installable' : True,
}