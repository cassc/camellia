# Edit this for new company 
company = [dict(val='北京xxx有限公司',    ky='title.full', desc='公司全名'),
           dict(val='xxx',                ky='title.simple', desc='公司简称'),
           dict(val='xxx',                ky='title.en', desc='公司英文简称'),
           
           dict(val='x先生',              ky='contact.name', desc='公司联系人姓名'),
           dict(val='xxx',                ky='contact.phone', desc='联系人手机号'),
           dict(val='xxx',                ky='contact.email', desc='联系人邮箱'),
           dict(val='北京xxx区xxx路xxxo', ky='contact.address', desc='公司地址'),

           # 经纬度用于在地图上标记公司位置
           dict(val='39.9042',            ky='location.lat', desc='地址纬度'),
           dict(val='116.4074',           ky='location.lon', desc='地址经度'),

           # 英文网站链接，没有就不修改
           dict(val='javascript:;',       ky='ensite', desc='公司全名'),

           # 备案号
           dict(val='粤ICP备88888888号',  ky='beianhao', desc='公司全名'),

           # 电商n链接
           dict(val='',  ky='shop.title', desc='电商名'),
           dict(val='',  ky='shop.link', desc='电商链接'),
           ]

import argparse
import os
from distutils.dir_util import copy_tree

ap = argparse.ArgumentParser()
ap.add_argument("-c", "--create-database", help="Use sample database", action='store_true')

args = vars(ap.parse_args())
copy_db = args['create_database']


def run_cmd(cmd):
    print(f'Run: {cmd}')
    os.system(cmd)

def replace_string(frm, to):
    frm = frm.replace(r'/', r'\/')
    to = to.replace(r'/', r'\/')
    run_cmd(f"grep -rl '{frm}' ./output | xargs sed -i 's/{frm}/{to}/g'")

def replace_keys(pairs):
    for d in pairs:
        k = d['ky']
        v = d['val']
        replace_string(f'__{k}__', v or '')

def build_be():
    run_cmd('cd output/be ; make build')

def build_fe():
    run_cmd('cd output/fe ; make sass')


def copy_to_target():
    run_cmd('cp output/be/main target/be/')
    run_cmd('cp docker-compose.yml target/')
    
    if copy_db:
        run_cmd('cp output/be/news.db target/be/')
        run_cmd('cp output/be/feedback.db target/be/')
        run_cmd('cp output/be/product.db target/be/')
        run_cmd('cp output/be/solution.db target/be/')
    
    copy_tree("output/be/templates/", 'target/be/templates/', preserve_symlinks=1)
    copy_tree("output/be/news/", 'target/be/news/', preserve_symlinks=1)
    copy_tree("output/fe/assets/", 'target/fe/assets/', preserve_symlinks=1)
    copy_tree("output/fe/js/", 'target/fe/js/', preserve_symlinks=1)
    copy_tree("output/fe/img/", 'target/fe/img/', preserve_symlinks=1)
    copy_tree("output/fe/css/", 'target/fe/css/', preserve_symlinks=1)
    
    
if __name__=='__main__':
    copy_tree("be", "output/be", preserve_symlinks=1)
    copy_tree("fe", "output/fe", preserve_symlinks=1)

    os.makedirs('target/be', exist_ok=True)
    os.makedirs('target/fe', exist_ok=True)

    replace_keys(company)
    build_be()
    build_fe()
    copy_to_target()
