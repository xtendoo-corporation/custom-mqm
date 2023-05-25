{
    "name": "Document Format Fguadiamar",
    "summary": """Formatos de documentos de Ferreteria Guadiamar""",
    "version": "15.0.1.0.0",
    "description": """Formatos de documentos de Ferreteria Guadiamar""",
    "author": "Daniel Dominguez",
    "company": "Xtendoo",
    "website": "http://xtendoo.es",
    "category": "Extra Tools",
    "license": "AGPL-3",
    "depends": [
        "base",
        "web",
        "account_invoice_report_grouped_by_picking",
        "product",
    ],
    "data": [
        "views/layout/external_layout_clean.xml",
        "views/account/account_move.xml",
        'report/product_reports.xml',
    ],
    "installable": True,
    "auto_install": False,
}
