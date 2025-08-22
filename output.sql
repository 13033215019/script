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
    where rec.bill_no = '25312000000181078405';
insert into cm_rec_cost_center_item (receipt_id, cost_center_oid, cost_center_item_oid, tenant_id, created_date,
                                         last_modified_date, created_by, last_modified_by)
    select rec.id,(select cost_center_oid
                   from art_cost_center where code = 'PROJECT' and tenant_id = 1895203830157574145 limit 1),(
        select cost_center_item_oid
        from art_cost_center_item where code = 'TJPHII2019DZZY01-PT' and cost_center_id = (
            select art_cost_center.id
            from art_cost_center where code = 'PROJECT' and tenant_id = 1895203830157574145 limit 1
        ) limit 1
        ),1895203830157574145,NOW(),NOW(),NULL,NULL
    from atl_receipt rec
             join cm_receipt_attribute attr on receipt_id = rec.id
    where rec.bill_no = '25952000000137009102';
insert into cm_rec_cost_center_item (receipt_id, cost_center_oid, cost_center_item_oid, tenant_id, created_date,
                                         last_modified_date, created_by, last_modified_by)
    select rec.id,(select cost_center_oid
                   from art_cost_center where code = 'PROJECT' and tenant_id = 1895203830157574145 limit 1),(
        select cost_center_item_oid
        from art_cost_center_item where code = 'FMD-F000 ' and cost_center_id = (
            select art_cost_center.id
            from art_cost_center where code = 'PROJECT' and tenant_id = 1895203830157574145 limit 1
        ) limit 1
        ),1895203830157574145,NOW(),NOW(),NULL,NULL
    from atl_receipt rec
             join cm_receipt_attribute attr on receipt_id = rec.id
    where rec.bill_no = '2525300242';
insert into cm_rec_cost_center_item (receipt_id, cost_center_oid, cost_center_item_oid, tenant_id, created_date,
                                         last_modified_date, created_by, last_modified_by)
    select rec.id,(select cost_center_oid
                   from art_cost_center where code = 'PROJECT' and tenant_id = 1895203830157574145 limit 1),(
        select cost_center_item_oid
        from art_cost_center_item where code = 'FMD-F000 ' and cost_center_id = (
            select art_cost_center.id
            from art_cost_center where code = 'PROJECT' and tenant_id = 1895203830157574145 limit 1
        ) limit 1
        ),1895203830157574145,NOW(),NOW(),NULL,NULL
    from atl_receipt rec
             join cm_receipt_attribute attr on receipt_id = rec.id
    where rec.bill_no = 'F000PO-001442';
insert into cm_rec_cost_center_item (receipt_id, cost_center_oid, cost_center_item_oid, tenant_id, created_date,
                                         last_modified_date, created_by, last_modified_by)
    select rec.id,(select cost_center_oid
                   from art_cost_center where code = 'PROJECT' and tenant_id = 1895203830157574145 limit 1),(
        select cost_center_item_oid
        from art_cost_center_item where code = 'FMD-F000 ' and cost_center_id = (
            select art_cost_center.id
            from art_cost_center where code = 'PROJECT' and tenant_id = 1895203830157574145 limit 1
        ) limit 1
        ),1895203830157574145,NOW(),NOW(),NULL,NULL
    from atl_receipt rec
             join cm_receipt_attribute attr on receipt_id = rec.id
    where rec.bill_no = '9000933059';
insert into cm_rec_cost_center_item (receipt_id, cost_center_oid, cost_center_item_oid, tenant_id, created_date,
                                         last_modified_date, created_by, last_modified_by)
    select rec.id,(select cost_center_oid
                   from art_cost_center where code = 'PROJECT' and tenant_id = 1895203830157574145 limit 1),(
        select cost_center_item_oid
        from art_cost_center_item where code = 'FMD-F000 ' and cost_center_id = (
            select art_cost_center.id
            from art_cost_center where code = 'PROJECT' and tenant_id = 1895203830157574145 limit 1
        ) limit 1
        ),1895203830157574145,NOW(),NOW(),NULL,NULL
    from atl_receipt rec
             join cm_receipt_attribute attr on receipt_id = rec.id
    where rec.bill_no = '9000932795';
insert into cm_rec_cost_center_item (receipt_id, cost_center_oid, cost_center_item_oid, tenant_id, created_date,
                                         last_modified_date, created_by, last_modified_by)
    select rec.id,(select cost_center_oid
                   from art_cost_center where code = 'PROJECT' and tenant_id = 1895203830157574145 limit 1),(
        select cost_center_item_oid
        from art_cost_center_item where code = 'FMD-F000 ' and cost_center_id = (
            select art_cost_center.id
            from art_cost_center where code = 'PROJECT' and tenant_id = 1895203830157574145 limit 1
        ) limit 1
        ),1895203830157574145,NOW(),NOW(),NULL,NULL
    from atl_receipt rec
             join cm_receipt_attribute attr on receipt_id = rec.id
    where rec.bill_no = '9000932794';
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
    where rec.bill_no = '25312000000199836857';
insert into cm_rec_cost_center_item (receipt_id, cost_center_oid, cost_center_item_oid, tenant_id, created_date,
                                         last_modified_date, created_by, last_modified_by)
    select rec.id,(select cost_center_oid
                   from art_cost_center where code = 'PROJECT' and tenant_id = 1895203830157574145 limit 1),(
        select cost_center_item_oid
        from art_cost_center_item where code = 'TJCDS22004-PT' and cost_center_id = (
            select art_cost_center.id
            from art_cost_center where code = 'PROJECT' and tenant_id = 1895203830157574145 limit 1
        ) limit 1
        ),1895203830157574145,NOW(),NOW(),NULL,NULL
    from atl_receipt rec
             join cm_receipt_attribute attr on receipt_id = rec.id
    where rec.bill_no = '2300829805';
insert into cm_rec_cost_center_item (receipt_id, cost_center_oid, cost_center_item_oid, tenant_id, created_date,
                                         last_modified_date, created_by, last_modified_by)
    select rec.id,(select cost_center_oid
                   from art_cost_center where code = 'PROJECT' and tenant_id = 1895203830157574145 limit 1),(
        select cost_center_item_oid
        from art_cost_center_item where code = 'TJPHIV2019SNF01-PT' and cost_center_id = (
            select art_cost_center.id
            from art_cost_center where code = 'PROJECT' and tenant_id = 1895203830157574145 limit 1
        ) limit 1
        ),1895203830157574145,NOW(),NOW(),NULL,NULL
    from atl_receipt rec
             join cm_receipt_attribute attr on receipt_id = rec.id
    where rec.bill_no = '25112000000103843017';
