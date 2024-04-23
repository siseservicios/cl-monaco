#!/bin/bash
# Regenerar rama de staging
BASE_AR="/odoo_ar/odoo-16.0/reves16"
BASE_ST="/odoo_st/odoo-16.0/reves16"

set -e

# --------------------------------------------------------------------------------------
# Regenerar la rama staging en github
# --------------------------------------------------------------------------------------
echo "Regenerando rama de staging"
echo
cd $BASE_ST/sources
sudo rm -r reves
git clone git@github.com:siseservicios/reves
cd reves
git checkout staging
git checkout main
git branch -D staging
git push origin --delete staging
git checkout -b staging
git push --set-upstream origin staging
# --------------------------------------------------------------------------------------
# Hacer un backup de la base de produccion
# agregando --zipfile falla el script
# --------------------------------------------------------------------------------------
# sudo docker run --rm -i \
#     --network compose_default \
#     --link postgres:db \
#     --volume $BASE_AR/lopez:/base \
#     jobiols/dbtools:1.4.0 \
#         --db_name lopez_prod \
#         --no-neutralize \
#         --zipfile staging.zip \
#         --backup

# --------------------------------------------------------------------------------------
# restaurar la base de produccion en staging (el restore todavia falla)
# --------------------------------------------------------------------------------------
# mv /odoo_ar/odoo-16.0e/lopez/backup_dir/staging.zip /odoo_st/odoo-16.0e/lopez/backup_dir
# sudo docker run -rm -i \
#     --network compose_default \
#     --link postgres:db \
#     --volume /odoo_st/odoo-16.0e/lopez:/base \
#     jobiols/dbtools:1.4.0 \
#         --db_name lopez_test \
#         --zipfile staging.zip
#         --restore

# --------------------------------------------------------------------------------------
# Garantizar que todo esta igual en el arbol staging menos el repositorio de los modulos
# desarrollados el que vendrá de la rama staging
# Por alguna 'afortunada' razon el exclude excluye solo el ultimo lopez no el primero
# --------------------------------------------------------------------------------------

# Sincronizar todos los fuentes de produccion hacia staging
rsync -av --exclude 'reves' --exclude '.git' $BASE_AR/sources/ $BASE_ST/sources/

# Sincronizar el archivo odoo.conf
rsync -av $BASE_AR/config/ $BASE_ST/config/

# Activar el database manager en test
sed -i 's/list_db = True/list_db = False/' $BASE_ST/config/odoo.conf
