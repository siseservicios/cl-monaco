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
    "version": "17.0.1.0.0",
    "category": "Tools",
    "summary": "Proyecto Drogueria Monaco",
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
        "limit_time_cpu = 20000",
        "limit_time_real = 20000",
        "limit_time_real_cron = -1",
        "max_cron_threads = 2",
        "workers = 2",
        "admin_passwd = Monaco.2024",
    ],
    "port": "8069",
    "git-repos": [
        "git@github.com:siseservicios/cl-monaco.git",
        #"http://github.com/siseservicios/reves.git -b main",

        "https://github.com/ingadhoc/account-financial-tools.git",
        "https://github.com/ingadhoc/account-payment.git",
        "https://github.com/ingadhoc/odoo-argentina.git",
        "https://github.com/ingadhoc/argentina-sale.git",
        "https://github.com/ingadhoc/account-invoicing.git",
        "https://github.com/ingadhoc/odoo-argentina-ce.git",
        "https://github.com/ingadhoc/stock.git",

        # oca
        'https://github.com/OCA/reporting-engine.git',
        'https://github.com/OCA/stock-logistics-workflow.git',
        'https://github.com/OCA/web.git',

    ],
    # list of images to use in the form 'name image-url'
    "docker-images": [
        "odoo jobiols/odoo-jeo:17.0",
        "postgres postgres:15.1",
    ],
}
