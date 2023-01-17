"""
   作用：邮件外发配置（邮件外发测试）
   作者：eza实施团队
   时间：2022-05-18
"""

#邮件服务器IP（域名）
mail_server_ip = "smtp.163.com"
#邮件服务器端口
mail_server_port = 465

#发送邮箱账号
send_user = "17628275234@163.com"

#发送邮箱密钥(通过自带工具加密后使用以防泄密)
send_pass = "VGs1S1ZFeFBWRk5HVDFCVlYwVkVWdz09RlphbXN5VGtk"

#邮件接收者
receive_list = ["gousl@fusionskye.com"]

#邮件附件（可添加多个，附件绝对路径）
file_path_list = []

#邮件主题
send_title = "python--qq邮箱自动邮件测试"

#邮件内容(可按照格式编写)
message = """
   袁童鞋，憨憨！
       干饭在即，请注意干饭时间！
     
"""
