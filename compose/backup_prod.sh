#!/bin/bash
# --------------------------------------------------------------------------------------
# Hacer un backup de la base de produccion
# --------------------------------------------------------------------------------------

project="monaco"

sudo docker run --rm -i \
    --network compose_default \
    --link postgres:db \
    --volume /odoo_ar/odoo-16.0/$project:/base \
    jobiols/dbtools:1.4.0 \
        --db_name $project"_prod" \
        --no-neutralize \
        --days-to-keep 4 \
        --backup
