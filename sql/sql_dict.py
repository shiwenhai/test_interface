__author__ = 'songqi'

def change_bp_id(bp_id=1828979637078):
    sql = "update borrows set bp_id=1828979637079 WHERE id = '" + str(bp_id) + "';"
    return sql, str(bp_id)

def delete_date(bp_id):
    delete_data_dict = {}
    delete_date_dict["des_main"] = "delete from des_main where bp_id = " + str(bp_id)
    delete_date_dict["des_main"] = "delete from des_dcin where bp_id = " + str(bp_id)
    delete_date_dict["des_main"] = "delete from des_dcin_detail where bp_id = " + str(bp_id)
    return delete_data_dict


select * from des_main where bp_id = bp_id_B
select * from des_dcin where bp_id = bp_id_B
select * from des_dcin_detail where bp_id = bp_id_B

