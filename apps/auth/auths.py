def user_loader_handler(identity=None):
    """
    用户对象加载处理对象
    :param identity:用户身份标识
    :return:
    """
    if identity is None:
        return None
    current_user = Admin.objects(user_code=identity).first()
    return current_user