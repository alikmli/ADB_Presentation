



def query_style_select(query):
    lists=query.split("where")
    select_items=lists[0].split('from')[0]

    select_items=select_items.split()
    select_items.remove("give")
    return select_items

def query_style_where(query):
    lists=query.split("where")
    where_items=dict()
    where_part=lists[1]

    wh_list=list()
    if 'and' in where_part:
        wh_list=where_part.split("and")
        for item in wh_list:
            tmp=item.split("=")
            where_items[tmp[0].strip()]=tmp[1].strip()
    elif "or" in where_part:
        wh_list=where_part.split("or")
        for item in wh_list:
            tmp=item.split("=")
            where_items[tmp[0].strip()]=tmp[1].strip()

    if wh_list == list():
        tmp=where_part.split("=")
        where_items[tmp[0].strip()]=tmp[1].strip()

    return  where_items


def query_table_name(query):
    lists=query.split("from")
    second_part=lists[1]
    tbl_name=second_part.split("where")[0]
    return tbl_name.strip()

