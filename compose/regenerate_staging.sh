#!/bin/bash
# Regenerar rama de staging
BASE_AR="/odoo_ar/odoo-16.0/monaco"
BASE_ST="/odoo_st/odoo-16.0/monaco"

set -e

# --------------------------------------------------------------------------------------
# Bajar el servicio
# --------------------------------------------------------------------------------------
sudo docker compose down

# --------------------------------------------------------------------------------------
# Regenerar la rama staging en github
# --------------------------------------------------------------------------------------
echo "Regenerando rama de staging"
echo
cd $BASE_ST
sudo rm -r sources
cp -ar $BASE_AR/sources $BASE_ST

git -C $BASE_ST/sources/monaco checkout staging

# --------------------------------------------------------------------------------------
# Hacer un backup de la base de produccion
# --------------------------------------------------------------------------------------

# Activar el database manager en test
sed -i 's/list_db = False/list_db = True/' $BASE_ST/config/odoo.conf
