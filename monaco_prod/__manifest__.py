##############################################################################
#
#    Copyright (C) 2023  wasf
#    All Rights Reserved.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your optiogitn) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    "name": "monaco",
    "version": "16.0.1.0.0",
    "category": "Tools",
    "summary": "Proyecto Droguería Monaco",
    "author": "jeo Software",
    "website": "http://github.com/siseservicios/cl-monaco",
    "license": "AGPL-3",
    "depends": [],
    "installable": True,
    # Aca empiezan las extensiones
    "env-ver": "2",
    "odoo-license": "CE",
    "config": [
        "limit_memory_hard = 2684354560",
        "limit_memory_soft = 2147483648",
        "limit_time_cpu = 600",
        "limit_time_real = 1200",
        "limit_time_real_cron = -1",
        "max_cron_threads = 2",
        "workers = 2",
        "admin_passwd = Monaco.2024!",
    ],
    "port": "8069",
    "git-repos": [
        'git@github.com:siseservicios/cl-monaco.git',
        #'http://github.com/siseservicios/reves.git -b main',

        # adhoc
        'https://github.com/ingadhoc/account-financial-tools.git adhoc-account-financial-tools',
        'https://github.com/ingadhoc/account-payment.git adhoc-account-payment',
        'https://github.com/ingadhoc/argentina-sale.git adhoc-argentina-sale',
        'https://github.com/ingadhoc/account-invoicing.git adhoc-account-invoicing',
        'https://github.com/ingadhoc/odoo-argentina.git adhoc-odoo-argentina',
        'https://github.com/ingadhoc/odoo-argentina-ce.git adhoc-odoo-argentina-ce',
        'https://github.com/ingadhoc/partner.git adhoc-partner',
        'https://github.com/ingadhoc/product.git adhoc-product',
        'https://github.com/ingadhoc/stock.git adhoc-stock',

        # oca
        'https://github.com/OCA/OpenUpgrade oca-openupgrade',
        'https://github.com/OCA/partner-contact.git oca-partner-contact',
        'https://github.com/OCA/product-attribute.git oca-product-attribute',
        'https://github.com/OCA/reporting-engine.git oca-reporting-engine',
        'https://github.com/OCA/sale-workflow.git oca-sale-workflow',
        'https://github.com/OCA/stock-logistics-availability oca-stock-logistics-availability',
        'https://github.com/OCA/stock-logistics-workflow.git oca-stock-logistics-workflow',
        'https://github.com/OCA/web.git oca-web',

    ],
    # list of images to use in the form 'name image-url'
    "docker-images": [
        "odoo jobiols/odoo-jeo:16.0",
        "postgres postgres:15.1",
    ],
}
