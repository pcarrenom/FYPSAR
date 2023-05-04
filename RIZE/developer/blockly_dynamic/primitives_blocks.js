goog.provide('Blockly.Blocks.primitives');
goog.require('Blockly.Blocks');


Blockly.Blocks["wait"] = {
init: function() {
	this.appendDummyInput()
		.appendField("Wait (seconds)")
		.appendField(new Blockly.FieldTextInput("edit"), "inp_1")
		.appendField(new Blockly.FieldImage(configuration_image, 16, 16, "*", edit_primitive))		;
	this.setColour("#2196f3");
	this.setOutput(true,['action']);

	this.setTooltip("Wait some seconds");
 	this.setHelpUrl("");
}};

Blockly.Blocks["say"] = {
init: function() {
	this.appendDummyInput()
		.appendField("Say")
		.appendField(new Blockly.FieldTextInput("edit"), "inp_1")
		.appendField(" options")
		.appendField(new Blockly.FieldTextInput("edit"), "inp_2")
		.appendField(new Blockly.FieldImage(configuration_image, 16, 16, "*", edit_primitive))		;
	this.setColour("#2196f3");
	this.setOutput(true,['action']);

	this.setTooltip("Say something with the robot");
 	this.setHelpUrl("");
}};

Blockly.Blocks["walk"] = {
init: function() {
	this.appendDummyInput()
		.appendField("Walk")
		.appendField(new Blockly.FieldTextInput("edit"), "inp_1")
		.appendField(" options")
		.appendField(new Blockly.FieldTextInput("edit"), "inp_2")
		.appendField(new Blockly.FieldImage(configuration_image, 16, 16, "*", edit_primitive))		;
	this.setColour("#2196f3");
	this.setOutput(true,['action']);

	this.setTooltip("Make robot walk");
 	this.setHelpUrl("");
}};

Blockly.Blocks["stretch"] = {
init: function() {
	this.appendDummyInput()
		.appendField("Stretch")
		.appendField(new Blockly.FieldTextInput("edit"), "inp_1")
		.appendField(" options")
		.appendField(new Blockly.FieldTextInput("edit"), "inp_2")
		.appendField(new Blockly.FieldImage(configuration_image, 16, 16, "*", edit_primitive))		;
	this.setColour("#2196f3");
	this.setOutput(true,['action']);

	this.setTooltip("Perform an stretch");
 	this.setHelpUrl("");
}};

Blockly.Blocks["leg"] = {
init: function() {
	this.appendDummyInput()
		.appendField("Raise leg")
		.appendField(new Blockly.FieldTextInput("edit"), "inp_1")
		.appendField(" options")
		.appendField(new Blockly.FieldTextInput("edit"), "inp_2")
		.appendField(new Blockly.FieldImage(configuration_image, 16, 16, "*", edit_primitive))		;
	this.setColour("#2196f3");
	this.setOutput(true,['action']);

	this.setTooltip("Raise Leg");
 	this.setHelpUrl("");
}};

Blockly.Blocks["arm"] = {
init: function() {
	this.appendDummyInput()
		.appendField("Raise arm")
		.appendField(new Blockly.FieldTextInput("edit"), "inp_1")
		.appendField(" options")
		.appendField(new Blockly.FieldTextInput("edit"), "inp_2")
		.appendField(new Blockly.FieldImage(configuration_image, 16, 16, "*", edit_primitive))		;
	this.setColour("#2196f3");
	this.setOutput(true,['action']);

	this.setTooltip("Perform an stretch");
 	this.setHelpUrl("");
}};

Blockly.Blocks["turn"] = {
init: function() {
	this.appendDummyInput()
		.appendField("Turn")
		.appendField(new Blockly.FieldTextInput("edit"), "inp_1")
		.appendField(" options")
		.appendField(new Blockly.FieldTextInput("edit"), "inp_2")
		.appendField(new Blockly.FieldImage(configuration_image, 16, 16, "*", edit_primitive))		;
	this.setColour("#2196f3");
	this.setOutput(true,['action']);

	this.setTooltip("Turn robot body/head");
 	this.setHelpUrl("");
}};

Blockly.Blocks["mode"] = {
init: function() {
	this.appendDummyInput()
		.appendField("Mode (Wake up/Rest)")
		.appendField(new Blockly.FieldTextInput("edit"), "inp_1")
		.appendField(new Blockly.FieldImage(configuration_image, 16, 16, "*", edit_primitive))		;
	this.setColour("#2196f3");
	this.setOutput(true,['action']);

	this.setTooltip("Wake or rest the robot");
 	this.setHelpUrl("");
}};

Blockly.Blocks["touched"] = {
init: function() {
	this.appendDummyInput()
		.appendField("Touched")
		.appendField(new Blockly.FieldTextInput("edit"), "inp_1")
		.appendField(new Blockly.FieldImage(configuration_image, 16, 16, "*", edit_primitive))		;
	this.setColour("#009688");
	this.setOutput(true,['condition']);

	this.setTooltip("Is robot touched");
 	this.setHelpUrl("");
}};

Blockly.Blocks["reset"] = {
init: function() {
	this.appendDummyInput()
		.appendField("Reset")
		.appendField(new Blockly.FieldTextInput("edit"), "inp_1")
		.appendField(new Blockly.FieldImage(configuration_image, 16, 16, "*", edit_primitive))		;
	this.setColour("#2196f3");
	this.setOutput(true,['action']);

	this.setTooltip("Reset Robot");
 	this.setHelpUrl("");
}};