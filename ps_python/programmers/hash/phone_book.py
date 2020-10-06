# 전화번호 목록
def solution(phone_book):
    if len(phone_book) == 1:
        return False
    for idx1,p in enumerate(phone_book):
        for b in phone_book[idx1+1:]:
            if len(b) <= len(p) and p[:len(b)] == b:
                return False
            if b[:len(p)] == p and len(b) >= len(p):
                return False
    return True