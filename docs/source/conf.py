# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'JRLBM-tut'
copyright = '2025, JRLBM'
author = 'JRLBM'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [ 
    'myst_parser',
    "sphinxcontrib.mermaid",
    "sphinx_copybutton",
    'sphinx.ext.mathjax',  # 推荐使用 MathJax 渲染公式
]

# MyST 配置
myst_enable_extensions = [
    "amsmath",      # 启用数学编号
    'attrs_block',
    "tasklist",
    "deflist",
    "dollarmath",   # 启用 $ 和 $$ 数学
    # "colon_fence",  # 启用 ::: 代码块
]

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

templates_path = ['_templates']
exclude_patterns = []

language = 'zh_CH'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

html_theme_options = {
    "collapse_navigation": True,  # 默认折叠二级目录
    "sticky_navigation": True,   # 导航栏固定
    "navigation_depth": 4,       # 显示目录层级深度
    "includehidden": False,       # 包含隐藏的页面
    "titles_only": False,        # 只显示标题，不显示整个toctree
}

html_css_files = [
    'custom.css',
]