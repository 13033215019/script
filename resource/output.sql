insert into cm_rec_cost_center_item (receipt_id, cost_center_oid, cost_center_item_oid, tenant_id, created_date,
                                         last_modified_date, created_by, last_modified_by)
    select rec.id,(select cost_center_oid
                   from art_cost_center where code = 'PROJECT' and tenant_id = 1895203830157574145 limit 1),(
        select cost_center_item_oid
        from art_cost_center_item where code = 'FMD-F105' and cost_center_id = (
            select art_cost_center.id
            from art_cost_center where code = 'PROJECT' and tenant_id = 1895203830157574145 limit 1
        ) limit 1
        ),1895203830157574145,NOW(),NOW(),NULL,NULL
    from atl_receipt rec
             join cm_receipt_attribute attr on receipt_id = rec.id
    where attr.receipt_code = 'INV107956299';
insert into cm_rec_cost_center_item (receipt_id, cost_center_oid, cost_center_item_oid, tenant_id, created_date,
                                         last_modified_date, created_by, last_modified_by)
    select rec.id,(select cost_center_oid
                   from art_cost_center where code = 'PROJECT' and tenant_id = 1895203830157574145 limit 1),(
        select cost_center_item_oid
        from art_cost_center_item where code = 'SHFSP23001-PT' and cost_center_id = (
            select art_cost_center.id
            from art_cost_center where code = 'PROJECT' and tenant_id = 1895203830157574145 limit 1
        ) limit 1
        ),1895203830157574145,NOW(),NOW(),NULL,NULL
    from atl_receipt rec
             join cm_receipt_attribute attr on receipt_id = rec.id
    where attr.receipt_code = 'INV107870027';
insert into cm_rec_cost_center_item (receipt_id, cost_center_oid, cost_center_item_oid, tenant_id, created_date,
                                         last_modified_date, created_by, last_modified_by)
    select rec.id,(select cost_center_oid
                   from art_cost_center where code = 'PROJECT' and tenant_id = 1895203830157574145 limit 1),(
        select cost_center_item_oid
        from art_cost_center_item where code = 'SHFSP23001-PT' and cost_center_id = (
            select art_cost_center.id
            from art_cost_center where code = 'PROJECT' and tenant_id = 1895203830157574145 limit 1
        ) limit 1
        ),1895203830157574145,NOW(),NOW(),NULL,NULL
    from atl_receipt rec
             join cm_receipt_attribute attr on receipt_id = rec.id
    where attr.receipt_code = 'INV107869993';
insert into cm_rec_cost_center_item (receipt_id, cost_center_oid, cost_center_item_oid, tenant_id, created_date,
                                         last_modified_date, created_by, last_modified_by)
    select rec.id,(select cost_center_oid
                   from art_cost_center where code = 'PROJECT' and tenant_id = 1895203830157574145 limit 1),(
        select cost_center_item_oid
        from art_cost_center_item where code = 'SHFSP23001-PT' and cost_center_id = (
            select art_cost_center.id
            from art_cost_center where code = 'PROJECT' and tenant_id = 1895203830157574145 limit 1
        ) limit 1
        ),1895203830157574145,NOW(),NOW(),NULL,NULL
    from atl_receipt rec
             join cm_receipt_attribute attr on receipt_id = rec.id
    where attr.receipt_code = 'INV107869876';
insert into cm_rec_cost_center_item (receipt_id, cost_center_oid, cost_center_item_oid, tenant_id, created_date,
                                         last_modified_date, created_by, last_modified_by)
    select rec.id,(select cost_center_oid
                   from art_cost_center where code = 'PROJECT' and tenant_id = 1895203830157574145 limit 1),(
        select cost_center_item_oid
        from art_cost_center_item where code = 'FMD-F105' and cost_center_id = (
            select art_cost_center.id
            from art_cost_center where code = 'PROJECT' and tenant_id = 1895203830157574145 limit 1
        ) limit 1
        ),1895203830157574145,NOW(),NOW(),NULL,NULL
    from atl_receipt rec
             join cm_receipt_attribute attr on receipt_id = rec.id
    where attr.receipt_code = 'INV107631047';
