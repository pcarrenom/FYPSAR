'use strict'
goog.provide('Blockly.Python.primitives');
goog.require('Blockly.Python');

Blockly.Python['wait'] = function(block) {
var text = block.getFieldValue('inp_1');
var code  = '{"primitive":"wait"'+","+ '"input":' + '"' + text + '"'+","+'"options":"none"}';
return [code, Blockly.Python.ORDER_NONE];
};

Blockly.Python['say'] = function(block) {
var text = block.getFieldValue('inp_1');
var options_dic = block.getFieldValue('inp_2');
options_dic = rizeBlockly.formatOptions(options_dic) 
var code  = '{"primitive":"say"'+","+ '"input":' + '"' + text + '"'+","+'"options":' + options_dic + '}';
return [code, Blockly.Python.ORDER_NONE];
};

Blockly.Python['walk'] = function(block) {
var text = block.getFieldValue('inp_1');
var options_dic = block.getFieldValue('inp_2');
options_dic = rizeBlockly.formatOptions(options_dic) 
var code  = '{"primitive":"walk"'+","+ '"input":' + '"' + text + '"'+","+'"options":' + options_dic + '}';
return [code, Blockly.Python.ORDER_NONE];
};

Blockly.Python['stretch'] = function(block) {
var text = block.getFieldValue('inp_1');
var options_dic = block.getFieldValue('inp_2');
options_dic = rizeBlockly.formatOptions(options_dic) 
var code  = '{"primitive":"stretch"'+","+ '"input":' + '"' + text + '"'+","+'"options":' + options_dic + '}';
return [code, Blockly.Python.ORDER_NONE];
};

Blockly.Python['leg'] = function(block) {
var text = block.getFieldValue('inp_1');
var options_dic = block.getFieldValue('inp_2');
options_dic = rizeBlockly.formatOptions(options_dic) 
var code  = '{"primitive":"leg"'+","+ '"input":' + '"' + text + '"'+","+'"options":' + options_dic + '}';
return [code, Blockly.Python.ORDER_NONE];
};

Blockly.Python['arm'] = function(block) {
var text = block.getFieldValue('inp_1');
var options_dic = block.getFieldValue('inp_2');
options_dic = rizeBlockly.formatOptions(options_dic) 
var code  = '{"primitive":"arm"'+","+ '"input":' + '"' + text + '"'+","+'"options":' + options_dic + '}';
return [code, Blockly.Python.ORDER_NONE];
};

Blockly.Python['turn'] = function(block) {
var text = block.getFieldValue('inp_1');
var options_dic = block.getFieldValue('inp_2');
options_dic = rizeBlockly.formatOptions(options_dic) 
var code  = '{"primitive":"turn"'+","+ '"input":' + '"' + text + '"'+","+'"options":' + options_dic + '}';
return [code, Blockly.Python.ORDER_NONE];
};

Blockly.Python['mode'] = function(block) {
var text = block.getFieldValue('inp_1');
var code  = '{"primitive":"mode"'+","+ '"input":' + '"' + text + '"'+","+'"options":"none"}';
return [code, Blockly.Python.ORDER_NONE];
};

Blockly.Python['touched'] = function(block) {
var text = block.getFieldValue('inp_1');
var code  = '{"primitive":"touched"'+","+ '"input":' + '"' + text + '"'+","+'"options":"none"}';
return [code, Blockly.Python.ORDER_NONE];
};

Blockly.Python['reset'] = function(block) {
var text = block.getFieldValue('inp_1');
var code  = '{"primitive":"reset"'+","+ '"input":' + '"' + text + '"'+","+'"options":"none"}';
return [code, Blockly.Python.ORDER_NONE];
};