
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'progBEGIN CALL COMMA DIVIDE DLABEL END EQUALS EXIT GEQ GOTO GREATER ID IF IN INOUT LABEL LEQ LESSER LPAREN MINUS MULTIPLY NEQ NUM OUT PLUS PRINT PRINTLN PROC READ RETURN RPAREN SEMICOLON STRING VAR\n    prog    : vardecls procdecls BEGIN stmtlist END\n    empty  :\n    vardecls    : vardecl vardecls\n                | empty\n    \n    vardecl : VAR varlist SEMICOLON\n    \n    varlist : ID COMMA varlist\n            | ID\n    \n    procdecls   : procdecl procdecls\n                | empty\n    \n    procdecl    : PROC ID LPAREN paramlist RPAREN vardecls pstmtlist\n    \n    paramlist   : tparamlist\n                | empty\n    \n    tparamlist  : param COMMA tparamlist\n                | param\n    \n    param   : mode ID\n    \n    mode    : IN\n            | OUT\n            | INOUT\n    \n    pstmtlist   : pstmt pstmtlist\n                | pstmt\n    \n    stmtlist    : mstmt stmtlist\n                | mstmt\n    \n    pstmt   : DLABEL\n            | stmt SEMICOLON\n            | RETURN SEMICOLON\n    \n    mstmt   : DLABEL\n            | stmt SEMICOLON\n    \n    stmt    : assign\n            | condjump\n            | jump\n            | readstmt\n            | printstmt\n            | callstmt\n            | EXIT\n    \n    assign  : ID EQUALS opd arithop opd\n    \n    condjump    : IF ID cmpop ID GOTO LABEL\n    \n    jump    : GOTO LABEL\n    \n    readstmt    : READ ID\n    \n    printstmt   : PRINT printarg\n                | PRINTLN\n    \n    printarg    : ID\n                | STRING\n    \n    callstmt    : CALL ID LPAREN arglist RPAREN\n    \n    arglist : targlist\n            | empty\n    \n    targlist    : ID COMMA targlist\n                | ID\n    \n    cmpop   : LESSER\n            | GREATER\n            | LEQ\n            | GEQ\n            | EQUALS\n            | NEQ\n    \n    arithop : PLUS\n            | MINUS\n            | MULTIPLY\n            | DIVIDE\n    \n    opd : ID\n        | NUM\n    '
    
_lr_action_items = {'VAR':([0,3,16,68,],[5,5,-5,5,]),'PROC':([0,2,3,4,7,10,16,87,88,89,94,95,96,],[-2,9,-2,-4,9,-3,-5,-10,-20,-23,-19,-24,-25,]),'BEGIN':([0,2,3,4,6,7,8,10,14,16,87,88,89,94,95,96,],[-2,-2,-2,-4,13,-2,-9,-3,-8,-5,-10,-20,-23,-19,-24,-25,]),'$end':([1,38,],[0,-1,]),'DLABEL':([3,4,10,13,16,19,20,40,68,81,88,89,95,96,],[-2,-4,-3,20,-5,20,-26,-27,-2,89,89,-23,-24,-25,]),'RETURN':([3,4,10,16,68,81,88,89,95,96,],[-2,-4,-3,-5,-2,91,91,-23,-24,-25,]),'EXIT':([3,4,10,13,16,19,20,40,68,81,88,89,95,96,],[-2,-4,-3,28,-5,28,-26,-27,-2,28,28,-23,-24,-25,]),'ID':([3,4,5,9,10,13,16,17,19,20,30,32,33,35,40,41,53,54,55,56,60,61,62,63,64,65,66,67,68,71,72,73,74,75,81,85,88,89,95,96,],[-2,-4,12,15,-3,29,-5,12,29,-26,42,44,46,48,-27,57,70,-16,-17,-18,76,-48,-49,-50,-51,-52,-53,77,-2,57,-54,-55,-56,-57,29,77,29,-23,-24,-25,]),'IF':([3,4,10,13,16,19,20,40,68,81,88,89,95,96,],[-2,-4,-3,30,-5,30,-26,-27,-2,30,30,-23,-24,-25,]),'GOTO':([3,4,10,13,16,19,20,40,68,76,81,88,89,95,96,],[-2,-4,-3,31,-5,31,-26,-27,-2,84,31,31,-23,-24,-25,]),'READ':([3,4,10,13,16,19,20,40,68,81,88,89,95,96,],[-2,-4,-3,32,-5,32,-26,-27,-2,32,32,-23,-24,-25,]),'PRINT':([3,4,10,13,16,19,20,40,68,81,88,89,95,96,],[-2,-4,-3,33,-5,33,-26,-27,-2,33,33,-23,-24,-25,]),'PRINTLN':([3,4,10,13,16,19,20,40,68,81,88,89,95,96,],[-2,-4,-3,34,-5,34,-26,-27,-2,34,34,-23,-24,-25,]),'CALL':([3,4,10,13,16,19,20,40,68,81,88,89,95,96,],[-2,-4,-3,35,-5,35,-26,-27,-2,35,35,-23,-24,-25,]),'SEMICOLON':([11,12,21,22,23,24,25,26,27,28,34,37,43,44,45,46,47,57,59,83,86,90,91,92,],[16,-7,40,-28,-29,-30,-31,-32,-33,-34,-40,-6,-37,-38,-39,-41,-42,-58,-59,-35,-43,95,96,-36,]),'COMMA':([12,52,70,77,],[17,69,-15,85,]),'LPAREN':([15,48,],[36,67,]),'END':([18,19,20,39,40,],[38,-22,-26,-21,-27,]),'EQUALS':([29,42,],[41,65,]),'LABEL':([31,84,],[43,92,]),'STRING':([33,],[47,]),'RPAREN':([36,49,50,51,52,67,70,77,78,79,80,82,93,],[-2,68,-11,-12,-14,-2,-15,-47,86,-44,-45,-13,-46,]),'IN':([36,69,],[54,54,]),'OUT':([36,69,],[55,55,]),'INOUT':([36,69,],[56,56,]),'NUM':([41,71,72,73,74,75,],[59,59,-54,-55,-56,-57,]),'LESSER':([42,],[61,]),'GREATER':([42,],[62,]),'LEQ':([42,],[63,]),'GEQ':([42,],[64,]),'NEQ':([42,],[66,]),'PLUS':([57,58,59,],[-58,72,-59,]),'MINUS':([57,58,59,],[-58,73,-59,]),'MULTIPLY':([57,58,59,],[-58,74,-59,]),'DIVIDE':([57,58,59,],[-58,75,-59,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'prog':([0,],[1,]),'vardecls':([0,3,68,],[2,10,81,]),'vardecl':([0,3,68,],[3,3,3,]),'empty':([0,2,3,7,36,67,68,],[4,8,4,8,51,80,4,]),'procdecls':([2,7,],[6,14,]),'procdecl':([2,7,],[7,7,]),'varlist':([5,17,],[11,37,]),'stmtlist':([13,19,],[18,39,]),'mstmt':([13,19,],[19,19,]),'stmt':([13,19,81,88,],[21,21,90,90,]),'assign':([13,19,81,88,],[22,22,22,22,]),'condjump':([13,19,81,88,],[23,23,23,23,]),'jump':([13,19,81,88,],[24,24,24,24,]),'readstmt':([13,19,81,88,],[25,25,25,25,]),'printstmt':([13,19,81,88,],[26,26,26,26,]),'callstmt':([13,19,81,88,],[27,27,27,27,]),'printarg':([33,],[45,]),'paramlist':([36,],[49,]),'tparamlist':([36,69,],[50,82,]),'param':([36,69,],[52,52,]),'mode':([36,69,],[53,53,]),'opd':([41,71,],[58,83,]),'cmpop':([42,],[60,]),'arithop':([58,],[71,]),'arglist':([67,],[78,]),'targlist':([67,85,],[79,93,]),'pstmtlist':([81,88,],[87,94,]),'pstmt':([81,88,],[88,88,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> prog","S'",1,None,None,None),
  ('prog -> vardecls procdecls BEGIN stmtlist END','prog',5,'p_prog','parser.py',19),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',23),
  ('vardecls -> vardecl vardecls','vardecls',2,'p_vardecls','parser.py',28),
  ('vardecls -> empty','vardecls',1,'p_vardecls','parser.py',29),
  ('vardecl -> VAR varlist SEMICOLON','vardecl',3,'p_vardecl','parser.py',34),
  ('varlist -> ID COMMA varlist','varlist',3,'p_varlist','parser.py',39),
  ('varlist -> ID','varlist',1,'p_varlist','parser.py',40),
  ('procdecls -> procdecl procdecls','procdecls',2,'p_procdecls','parser.py',45),
  ('procdecls -> empty','procdecls',1,'p_procdecls','parser.py',46),
  ('procdecl -> PROC ID LPAREN paramlist RPAREN vardecls pstmtlist','procdecl',7,'p_procdel','parser.py',51),
  ('paramlist -> tparamlist','paramlist',1,'p_paramlist','parser.py',56),
  ('paramlist -> empty','paramlist',1,'p_paramlist','parser.py',57),
  ('tparamlist -> param COMMA tparamlist','tparamlist',3,'p_tparamlist','parser.py',62),
  ('tparamlist -> param','tparamlist',1,'p_tparamlist','parser.py',63),
  ('param -> mode ID','param',2,'p_param','parser.py',68),
  ('mode -> IN','mode',1,'p_mode','parser.py',73),
  ('mode -> OUT','mode',1,'p_mode','parser.py',74),
  ('mode -> INOUT','mode',1,'p_mode','parser.py',75),
  ('pstmtlist -> pstmt pstmtlist','pstmtlist',2,'p_pstmtlist','parser.py',80),
  ('pstmtlist -> pstmt','pstmtlist',1,'p_pstmtlist','parser.py',81),
  ('stmtlist -> mstmt stmtlist','stmtlist',2,'p_stmtlist','parser.py',86),
  ('stmtlist -> mstmt','stmtlist',1,'p_stmtlist','parser.py',87),
  ('pstmt -> DLABEL','pstmt',1,'p_pstmt','parser.py',92),
  ('pstmt -> stmt SEMICOLON','pstmt',2,'p_pstmt','parser.py',93),
  ('pstmt -> RETURN SEMICOLON','pstmt',2,'p_pstmt','parser.py',94),
  ('mstmt -> DLABEL','mstmt',1,'p_mstmt','parser.py',99),
  ('mstmt -> stmt SEMICOLON','mstmt',2,'p_mstmt','parser.py',100),
  ('stmt -> assign','stmt',1,'p_stmt','parser.py',105),
  ('stmt -> condjump','stmt',1,'p_stmt','parser.py',106),
  ('stmt -> jump','stmt',1,'p_stmt','parser.py',107),
  ('stmt -> readstmt','stmt',1,'p_stmt','parser.py',108),
  ('stmt -> printstmt','stmt',1,'p_stmt','parser.py',109),
  ('stmt -> callstmt','stmt',1,'p_stmt','parser.py',110),
  ('stmt -> EXIT','stmt',1,'p_stmt','parser.py',111),
  ('assign -> ID EQUALS opd arithop opd','assign',5,'p_assign','parser.py',116),
  ('condjump -> IF ID cmpop ID GOTO LABEL','condjump',6,'p_condjump','parser.py',121),
  ('jump -> GOTO LABEL','jump',2,'p_jump','parser.py',126),
  ('readstmt -> READ ID','readstmt',2,'p_readstmt','parser.py',131),
  ('printstmt -> PRINT printarg','printstmt',2,'p_printstmt','parser.py',136),
  ('printstmt -> PRINTLN','printstmt',1,'p_printstmt','parser.py',137),
  ('printarg -> ID','printarg',1,'p_printarg','parser.py',142),
  ('printarg -> STRING','printarg',1,'p_printarg','parser.py',143),
  ('callstmt -> CALL ID LPAREN arglist RPAREN','callstmt',5,'p_callstmt','parser.py',148),
  ('arglist -> targlist','arglist',1,'p_arglist','parser.py',153),
  ('arglist -> empty','arglist',1,'p_arglist','parser.py',154),
  ('targlist -> ID COMMA targlist','targlist',3,'p_targlist','parser.py',159),
  ('targlist -> ID','targlist',1,'p_targlist','parser.py',160),
  ('cmpop -> LESSER','cmpop',1,'p_cmpop','parser.py',165),
  ('cmpop -> GREATER','cmpop',1,'p_cmpop','parser.py',166),
  ('cmpop -> LEQ','cmpop',1,'p_cmpop','parser.py',167),
  ('cmpop -> GEQ','cmpop',1,'p_cmpop','parser.py',168),
  ('cmpop -> EQUALS','cmpop',1,'p_cmpop','parser.py',169),
  ('cmpop -> NEQ','cmpop',1,'p_cmpop','parser.py',170),
  ('arithop -> PLUS','arithop',1,'p_airthop','parser.py',175),
  ('arithop -> MINUS','arithop',1,'p_airthop','parser.py',176),
  ('arithop -> MULTIPLY','arithop',1,'p_airthop','parser.py',177),
  ('arithop -> DIVIDE','arithop',1,'p_airthop','parser.py',178),
  ('opd -> ID','opd',1,'p_opd','parser.py',183),
  ('opd -> NUM','opd',1,'p_opd','parser.py',184),
]
