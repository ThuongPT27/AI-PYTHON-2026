def khop_dl(set_da_nop, set_ds_lop):
    sv_da_nop = set_da_nop.intersection(set_ds_lop)
    sv_chua_nop = set_ds_lop.difference(set_da_nop)
    return (sv_da_nop, sv_chua_nop)
