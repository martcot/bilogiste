#!/usr/bin/python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup

def clean_html(html):
    cleaned = html
    
    # Toujours mettre en premier les changements qui peuvent alterer les autres
    replacements = [
        {'s':'<p><br/>', 'r':'<p>'},
        {'s':'<p><br />', 'r':'<p>'},
    ]
    
    ACCEPTED_ATTRS = ["name", "title", "href", "alt", "src",]
    ACCEPTED_STYLE = ["float", "width", "height", "padding"]

    for replacement in replacements:
        cleaned = cleaned.replace(replacement['s'], replacement['r'])

    soup = BeautifulSoup(cleaned)
    for tag in soup.findAll(True):
        
        # Supprime les tags p vides
        if (tag.string == None or tag.string.strip() == "") and tag.find(True) is None and tag.name == "p":
            tag.extract()
        
        # Clean les attributs
        new_attrs = {}
        
        for attr, val in tag.attrs.iteritems():
            if attr in ACCEPTED_ATTRS:
                new_attrs[attr] = val
                
            elif attr == "style":
                accepted_style = ""
                
                # traitement du style
                for style in [x.split(':') for x in val.split(';')]:
                    if len(style) == 2:
                        if style[0].strip() in ACCEPTED_STYLE:
                            accepted_style = accepted_style + style[0].strip() + ":" + style[1].strip() + ";"

                if not accepted_style == "":
                    new_attrs[attr] = accepted_style
            
        tag.attrs = new_attrs
            
    cleaned = unicode(soup)
    
    return cleaned
