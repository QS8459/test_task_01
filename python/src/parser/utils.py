

#find cat function to build the hierarchy level of product category
def find_cat(cats, id):
    cat_d:dict = {};
    for item in cats:
        if item.get('id') == id:
            cat_d = item;
    res_str = hierarchy(cats, cat_d);

    divided = res_str.split('/')[::-1];
    res = {}
    if 0 < len(divided) :
        res['lvl1'] = divided[0];
    if 2 <= len(divided):
        res['lvl1'] = divided[0]
        res['lvl2'] = divided[1];
    if 3 <= len(divided):
        res['lvl1'] = divided[0]
        res['lvl2'] = divided[1]
        res['lvl3'] = divided[2];
    if 4 <= len(divided) :
        res['lvl1'] = divided[0]
        res['lvl2'] = divided[1]
        res['lvl3'] = divided[2];
        res['lvlr']= '/'.join(divided[3::])
    return res;

#Hierarchy builder function finds category hierarchy recursievly
def hierarchy(a, cat_d:dict = {}):

    string = cat_d.get('name');
    parent = cat_d.get('parentId')
    inner:dict = {};
    if parent is not None:
        for item in a:
            if item.get('id') == parent:
                inner = item
        string += '/' + hierarchy(a,inner)
    return string if string is not None else '';
