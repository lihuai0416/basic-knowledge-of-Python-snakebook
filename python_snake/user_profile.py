# 用于第九章作业
def build_profile(first, last, **user_info):  #两个星号即创建一个名为user_info的字典
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info