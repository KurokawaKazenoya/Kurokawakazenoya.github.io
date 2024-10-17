import os

# 设置要查找的根目录
directory = r"D:\Canvas\Kurokawakazenoya.github.io\OLC4O_content"

# 定义替换的映射规则
replace_map = {
    '/shared/LCS_HTML_Templates/Kanata_Academy_Template_v4.1.02/_assets/thirdpartylib/jquery/jquery-3.5.1.min.js': './jquery-3.5.1.min.js',
    '/shared/LCS_HTML_Templates/Kanata_Academy_Template_v4.1.02/_assets/thirdpartylib/popper-js/popper.min.js': './popper.min.js',
    '/shared/LCS_HTML_Templates/Kanata_Academy_Template_v4.1.02/_assets/thirdpartylib/bootstrap-4.6.1/js/bootstrap.min.js': './bootstrap.min.js',
    '/shared/LCS_HTML_Templates/Kanata_Academy_Template_v4.1.02/_assets/js/scripts.min.js': './scripts.min.js',
    '/shared/LCS_HTML_Templates/Kanata_Academy_Template_v4.1.02/_assets/thirdpartylib/bootstrap-4.6.1/css/bootstrap.min.css': './bootstrap.min.css',
    '/shared/LCS_HTML_Templates/Kanata_Academy_Template_v4.1.02/_assets/thirdpartylib/fontawesome-free-5.9.0-web/css/all.min.css': './all.min.css',
    '/shared/LCS_HTML_Templates/Kanata_Academy_Template_v4.1.02/_assets/css/theme.min.css': './theme.min.css',
    '/shared/LCS_HTML_Templates/Kanata_Academy_Template_v4.1.02/_assets/css/custom.css': './custom.css',
    '/content/enforced/7234-DemoMHF4U/EVA%20SCHOOL1.png': './EVA%20SCHOOL1.png',
    'https://s.brightspace.com/lib/fonts/0.5.0/fonts.css': './front.css'
    
    
}

# 批量替换绝对路径
def replace_in_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # 逐条替换路径
    for old_path, new_path in replace_map.items():
        content = content.replace(old_path, new_path)

    # 保存替换后的内容
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

# 遍历目录并处理所有 .html 文件
for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith(".html"):
            file_path = os.path.join(root, file)
            print(f"正在处理文件: {file_path}")
            replace_in_file(file_path)

print("替换完成！")
