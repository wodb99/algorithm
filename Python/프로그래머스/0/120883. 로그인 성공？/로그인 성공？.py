# def solution(id_pw, db):
#     id_list = []
#     pw_list = []
    
#     for temp in db:
#         id, pw = temp
#         id_list.append(id)
#         pw_list.append(pw)
    
#     if id_pw[0] not in id_list:
#         return "fail"
    
#     idx = id_list.index(id_pw[0])
    
#     if pw_list[idx] == id_pw[1]:
#         return "login"
#     else:
#         return "wrong pw"
    
def solution(id_pw, db):
    db_dict = dict(db)
    
    if id_pw[0] not in db_dict:
        return "fail"
    
    elif db_dict[id_pw[0]] == id_pw[1]:
        return "login"
    
    else:
        return "wrong pw"
