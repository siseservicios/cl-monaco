#!/bin/bash
# Copiar el filestore a test y borrarlo de prod

project="monaco"

set -e

if [ $# -eq 0 ]; then
    echo "Error: Tenes que pasar el nombre de la base de datos de test."
    echo "Uso: $0 <"$project"_test_xxxx>"
    exit 1
fi

sudo cp -ar /odoo_ar/odoo-16.0/$project/data_dir/filestore/$1 /odoo_st/odoo-16.0/$project/data_dir/filestore/
sudo rm -r /odoo_ar/odoo-16.0/$project/data_dir/filestore/$1
