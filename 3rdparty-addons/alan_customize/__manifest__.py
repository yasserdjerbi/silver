# -*- coding: utf-8 -*-

{
    'name': 'Alan custom',
    'category': 'Website',
    'sequence': 5,
    'summary': 'Theme Alan models',
    'version': '1.6',
    'author': 'Atharva System',
    'support': 'support@atharvasystem.com',
    'website' : 'http://www.atharvasystem.com',
    'license' : 'OPL-1',
    'description': """
        """,
    'depends': ['website_mass_mailing','website_blog','website_sale_wishlist','website_sale_comparison','website_sale_stock','website_crm','website_event'],
    'data': [
        'views/assets.xml',  
        'views/website_setting.xml',
        'views/product_brand_view.xml',
        'views/product_category_view.xml',
        'views/templates.xml',
        # 'views/header_footer_template.xml',
        'views/snippets.xml',
        'views/options.xml',
        'views/website_menu_view.xml',
        'views/mega_menu_template.xml', 
        'views/product_slider_templates.xml',
        'security/ir.model.access.csv',
        'views/product_brand_template.xml',
        'views/breadcum_template.xml',
        'views/multi_tab_configure_view.xml',
        'views/snippet_multitab_slider.xml',
        'views/product_slider_snippet.xml',
        'views/website_blog_config.xml',
        'views/snippet_blog_template.xml',
        'views/product_brand_page.xml',
        'views/snippet_embeded.xml',
        'views/custom_shop_view.xml',
        'views/custom_shop_template.xml',
        'views/product_tabs_view.xml'
    ],
    'live_test_url': 'http://theme-alan.atharvasystem.com',
    'demo': [
        'data/demo.xml',
    ],
    'currency': 'EUR',
    'installable': True,
    'application': True,
}
