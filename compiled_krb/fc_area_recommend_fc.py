# fc_area_recommend_fc.py

from __future__ import with_statement
from pyke import contexts, pattern, fc_rule, knowledge_base

pyke_version = '1.1.1'
compiler_version = 1

def move_01(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('coil_area', 'coil_information', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('coil_area', 'coil_area_ruler', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            if context.lookup_data('status')==1:
              engine.assert_('coil_area', 'move_area',
                             (rule.pattern(0).as_data(context),
                              rule.pattern(1).as_data(context),
                              rule.pattern(2).as_data(context),)),
              rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def move_02(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('coil_area', 'coil_information', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('coil_area', 'coil_area_ruler', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            if context.lookup_data('status')==2:
              engine.assert_('coil_area', 'move_area',
                             (rule.pattern(0).as_data(context),
                              rule.pattern(1).as_data(context),
                              rule.pattern(2).as_data(context),)),
              rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def move_03(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('coil_area', 'coil_information', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('coil_area', 'coil_area_ruler', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            if context.lookup_data('status')==3:
              engine.assert_('coil_area', 'move_area',
                             (rule.pattern(0).as_data(context),
                              rule.pattern(1).as_data(context),
                              rule.pattern(2).as_data(context),)),
              rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def move_04(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('coil_area', 'coil_information', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('coil_area', 'coil_area_ruler', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            if context.lookup_data('status')==4:
              engine.assert_('coil_area', 'move_area',
                             (rule.pattern(0).as_data(context),
                              rule.pattern(1).as_data(context),
                              rule.pattern(2).as_data(context),)),
              rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def move_05(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('coil_area', 'coil_information', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('coil_area', 'coil_area_ruler', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            if context.lookup_data('status')==5:
              engine.assert_('coil_area', 'move_area',
                             (rule.pattern(0).as_data(context),
                              rule.pattern(1).as_data(context),
                              rule.pattern(2).as_data(context),)),
              rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def move_06(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('coil_area', 'coil_information', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('coil_area', 'coil_area_ruler', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            if context.lookup_data('status')==6:
              engine.assert_('coil_area', 'move_area',
                             (rule.pattern(0).as_data(context),
                              rule.pattern(1).as_data(context),
                              rule.pattern(2).as_data(context),)),
              rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def move_07(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('coil_area', 'coil_information', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('coil_area', 'coil_area_ruler', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            if context.lookup_data('status')==7:
              engine.assert_('coil_area', 'move_area',
                             (rule.pattern(0).as_data(context),
                              rule.pattern(1).as_data(context),
                              rule.pattern(2).as_data(context),)),
              rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def populate(engine):
  This_rule_base = engine.get_create('fc_area_recommend')
  
  fc_rule.fc_rule('move_01', This_rule_base, move_01,
    (('coil_area', 'coil_information',
      (contexts.variable('steel_kind'),
       contexts.variable('coil_kind'),
       contexts.variable('size'),
       contexts.variable('next_unit'),),
      False),
     ('coil_area', 'coil_area_ruler',
      (contexts.variable('coil_kind'),
       contexts.variable('p0'),
       contexts.variable('p1'),
       contexts.variable('status'),),
      False),),
    (contexts.variable('coil_kind'),
     contexts.variable('p1'),
     contexts.variable('status'),))
  
  fc_rule.fc_rule('move_02', This_rule_base, move_02,
    (('coil_area', 'coil_information',
      (contexts.variable('steel_kind'),
       contexts.variable('coil_kind'),
       contexts.variable('size'),
       contexts.variable('next_unit'),),
      False),
     ('coil_area', 'coil_area_ruler',
      (contexts.variable('coil_kind'),
       contexts.variable('p1'),
       contexts.variable('p2'),
       contexts.variable('status'),),
      False),),
    (contexts.variable('coil_kind'),
     contexts.variable('p2'),
     contexts.variable('status'),))
  
  fc_rule.fc_rule('move_03', This_rule_base, move_03,
    (('coil_area', 'coil_information',
      (contexts.variable('steel_kind'),
       contexts.variable('coil_kind'),
       contexts.variable('size'),
       contexts.variable('next_unit'),),
      False),
     ('coil_area', 'coil_area_ruler',
      (contexts.variable('coil_kind'),
       contexts.variable('p2'),
       contexts.variable('p3'),
       contexts.variable('status'),),
      False),),
    (contexts.variable('coil_kind'),
     contexts.variable('p3'),
     contexts.variable('status'),))
  
  fc_rule.fc_rule('move_04', This_rule_base, move_04,
    (('coil_area', 'coil_information',
      (contexts.variable('steel_kind'),
       contexts.variable('coil_kind'),
       contexts.variable('size'),
       contexts.variable('next_unit'),),
      False),
     ('coil_area', 'coil_area_ruler',
      (contexts.variable('coil_kind'),
       contexts.variable('p3'),
       contexts.variable('p4'),
       contexts.variable('status'),),
      False),),
    (contexts.variable('coil_kind'),
     contexts.variable('p4'),
     contexts.variable('status'),))
  
  fc_rule.fc_rule('move_05', This_rule_base, move_05,
    (('coil_area', 'coil_information',
      (contexts.variable('steel_kind'),
       contexts.variable('coil_kind'),
       contexts.variable('size'),
       contexts.variable('next_unit'),),
      False),
     ('coil_area', 'coil_area_ruler',
      (contexts.variable('coil_kind'),
       contexts.variable('p4'),
       contexts.variable('p5'),
       contexts.variable('status'),),
      False),),
    (contexts.variable('coil_kind'),
     contexts.variable('p5'),
     contexts.variable('status'),))
  
  fc_rule.fc_rule('move_06', This_rule_base, move_06,
    (('coil_area', 'coil_information',
      (contexts.variable('steel_kind'),
       contexts.variable('coil_kind'),
       contexts.variable('size'),
       contexts.variable('next_unit'),),
      False),
     ('coil_area', 'coil_area_ruler',
      (contexts.variable('coil_kind'),
       contexts.variable('p5'),
       contexts.variable('p6'),
       contexts.variable('status'),),
      False),),
    (contexts.variable('coil_kind'),
     contexts.variable('p6'),
     contexts.variable('status'),))
  
  fc_rule.fc_rule('move_07', This_rule_base, move_07,
    (('coil_area', 'coil_information',
      (contexts.variable('steel_kind'),
       contexts.variable('coil_kind'),
       contexts.variable('size'),
       contexts.variable('next_unit'),),
      False),
     ('coil_area', 'coil_area_ruler',
      (contexts.variable('coil_kind'),
       contexts.variable('p6'),
       contexts.variable('p7'),
       contexts.variable('status'),),
      False),),
    (contexts.variable('coil_kind'),
     contexts.variable('p7'),
     contexts.variable('status'),))


Krb_filename = '..\\fc_area_recommend.krb'
Krb_lineno_map = (
    ((13, 17), (6, 6)),
    ((18, 22), (7, 7)),
    ((23, 23), (8, 8)),
    ((24, 27), (10, 10)),
    ((36, 40), (16, 16)),
    ((41, 45), (17, 17)),
    ((46, 46), (18, 18)),
    ((47, 50), (20, 20)),
    ((59, 63), (25, 25)),
    ((64, 68), (26, 26)),
    ((69, 69), (27, 27)),
    ((70, 73), (29, 29)),
    ((82, 86), (34, 34)),
    ((87, 91), (35, 35)),
    ((92, 92), (36, 36)),
    ((93, 96), (38, 38)),
    ((105, 109), (43, 43)),
    ((110, 114), (44, 44)),
    ((115, 115), (45, 45)),
    ((116, 119), (47, 47)),
    ((128, 132), (52, 52)),
    ((133, 137), (53, 53)),
    ((138, 138), (54, 54)),
    ((139, 142), (56, 56)),
    ((151, 155), (61, 61)),
    ((156, 160), (62, 62)),
    ((161, 161), (63, 63)),
    ((162, 165), (65, 65)),
)
