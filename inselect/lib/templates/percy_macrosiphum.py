# -*- coding: UTF-8 -*-
"""Template for Diana Percy's Macrosiphum microscope slides
"""

import re
from functools import partial

from inselect.lib.metadata import MetadataTemplate
from inselect.lib.parse import parse_matches_re


template = MetadataTemplate(
{
    'Name': 'Percy Macrosiphum slides',
    'Object label': u'{catalogNumber}_{Location-value}_{Taxonomy-value}',
    'Cropped file suffix': u'.jpg',
    'Fields': [
        {
            "Name": "catalogNumber",
            "Label": "Catalog number",
            "URI": "http://rs.tdwg.org/dwc/terms/catalogNumber",
            "Mandatory": True,
            "Parser": partial(parse_matches_re, re.compile('^[0-9]{9}$'),
                        'Invalid value [{0}]: should contain nine digits'),
        },
        {
            "Name": "Location",
            "Mandatory": True,
            "ChoicesWithData" : [
                (u'Drawer 178', 112602),
                (u'Drawer 241', 112666),
                (u'Drawer 242', 112667),
                (u'Drawer 243', 112668),
                (u'Drawer 244', 112669),
                (u'Drawer 252', 112677),
                (u'Drawer 253', 112678),
                (u'Drawer 254', 112679),
                (u'Drawer 255', 112680),
                (u'Drawer 256', 112681),
                (u'Drawer 257', 112682),
                (u'Drawer 261', 112686),
                (u'Drawer 262', 112687),
                (u'Drawer 263', 112688),
                (u'Drawer 588', 113013),
                (u'Drawer 589', 113014),
            ],
        },
        {
            "Name": "Taxonomy",
            "Mandatory": True,
            "ChoicesWithData": [
                (u'[Macrosiphum]', 1094793),
                (u'aetheocornum - Smith & Knowlton', 1094794),
                (u'agrimoniellum - Cockerell', 1094795),
                (u'albertinae - Hille Ris Lambers', 1094796),
                (u'albifrons - Essig', 1094797),
                (u'alpinum - Meier', 1094798),
                (u'amygdaloides - Theobald', 1094799),
                (u'asperulophagum - Holman', 1094886),
                (u'atragenae - Holman', 1094800),
                (u'audeni - MacDougall', 1094801),
                (u'badium - Jensen', 401914),
                (u'bisensioriatum - MacDougall', 1094802),
                (u'californicum - Clarke', 1094803),
                (u'carpinicolens - Patch', 1094891),
                (u'centranthi - Theobald', 1094804),
                (u'cerinthiacum - Borner', 1094805),
                (u'cholodkovskyi - Mordvilko', 1094806),
                (u'claytonae - Jensen', 1094807),
                (u'clematifoliae - Shinji', 1094808),
                (u'clematophagum - Zhang', 1094809),
                (u'cockerelli - Hottes', 1094810),
                (u'corallorhizae - Cockerell', 1094811),
                (u'cornifoliae - Shinji', 1094812),
                (u'coryli - Davis', 1094892),
                (u'corylicola - Shinji', 1094893),
                (u'creelii - Davis', 1094813),
                (u'cyatheae - Holman', 1094814),
                (u'daphnidis - Borner', 1094815),
                (u'dicentrae - Jensen & Chan', 54323),
                (u'diervillae - Patch', 1094816),
                (u'doronicicola - Leclant', 1094817),
                (u'echinocysti - Bartholomew', 1094818),
                (u'edrossi - Essig', 1094819),
                (u'epilobiellum - Theobald & Walton', 1094820),
                (u'euphorbiae - Thomas', 1094821),
                (u'euphorbiellum - Theobald', 1094822),
                (u'fagopyri - Ghosh & Raychaudhuri', 1094823),
                (u'flavum - Tao', 1094824),
                (u'fulvae - Oestlund', 1094882),
                (u'funestum - Macchiati', 1094825),
                (u'galii - Mamontova', 1094887),
                (u'galiophagum - Wimshurst', 1094888),
                (u'gaurea - Williams', 1094826),
                (u'gei - Koch', 1094827),
                (u'geranii - Oestlund', 1094828),
                (u'hamiltoni - Robinson', 1094829),
                (u'hartigi - Hille Ris Lambers', 1094830),
                (u'hellebori - Theobald & Walton', 1094831),
                (u'holmani - Leclant', 1094832),
                (u'holodisci - Jensen', 1094833),
                (u'impatientis - Williams', 1094834),
                (u'inexpectatum - Leclant', 1094835),
                (u'jeanae - Robinson', 1094836),
                (u'kickapoo - Hottes & Frison', 1094883),
                (u'kiowanepus - Hottes', 1094837),
                (u'knautiae - Holman', 1094838),
                (u'laseri - Holman', 1094839),
                (u'lilii - Monell', 1094840),
                (u'lisae - Heie', 1094841),
                (u'martini - Cockerell', 1094842),
                (u'meixneri - Borner', 1094843),
                (u'melanpyri - Mordvilko', 1094844),
                (u'mentzeliae - Wilson', 1094845),
                (u'mertensiae - Gillette & Palmer', 1094846),
                (u'mordvilkoi - Miyazaki', 1094847),
                (u'nasonovi - Mordvilko', 1094848),
                (u'olmsteadi - Robinson', 1094849),
                (u'opportunisticum - Jensen', 402104),
                (u'oredonensis - Remaudiere', 1094850),
                (u'oregonense - Jensen', 1094851),
                (u'pachysiphon - Hille Ris Lambers', 1094852),
                (u'pallens - Hottes & Frison', 1094853),
                (u'pechumani - MacGillivray', 1094854),
                (u'perillae - Zhang', 1094896),
                (u'potentillae - Oestlund', 1094855),
                (u'potentillicaulis - Miller', 1094856),
                (u'prenanthidis - Borner', 1094857),
                (u'pseudocoryli - Patch', 1094894),
                (u'pseudogeranii - Chakrabarti & Raychau', 1094858),
                (u'pyrifoliae - MacDougall', 1094859),
                (u'raysmithi - Hille Ris Lambers', 1094860),
                (u'rosae - Linnaeus', 1094861),
                (u'rubiarctici - Heikinheimo', 1094862),
                (u'rudbeckiarum - Cockerell', 1094863),
                (u'sanguinarium - Hottes & Frison', 1094889),
                (u'selenium - Theobald', 1094864),
                (u'silenium_penfroense - Stroyan', 1094865),
                (u'silvaticum - Meier', 1094866),
                (u'sorbi - Matsumura', 1094897),
                (u'stanleyi - Wilson', 1094867),
                (u'stellariae - Theobald', 1094868),
                (u'subarcticum - Robinson', 1094869),
                (u'symphytae - Barjadze & Chakvetadze', 35530),
                (u'symphyti - Barjadze & Chakvetadze', 35272),
                (u'tenuicauda - Bartholomew', 1094870),
                (u'tiliae - Monell', 1094871),
                (u'tinctum - Walker', 1094872),
                (u'trolli - Borner', 1094873),
                (u'tuberculaceps - Essig', 1094874),
                (u'valerianae - Clarke', 1094875),
                (u'vancouveriae - Jensen', 401997),
                (u'vandenboschi - Hille Ris Lambers', 1094884),
                (u'venaefuscae - Davis', 1094876),
                (u'violae - Jensen', 401996),
                (u'weberi - Borner', 1094877),
                (u'willamettense - Jensen', 1094878),
                (u'wilsoni - Jensen', 1094879),
                (u'zionensis - Knowlton', 1094880),
            ],
        },
    ]
})
