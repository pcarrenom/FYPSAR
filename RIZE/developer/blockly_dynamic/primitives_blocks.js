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

Blockly.Blocks["shoulder"] = {
init: function() {
	this.appendDummyInput()
		.appendField("Move shoulder")
		.appendField(new Blockly.FieldTextInput("edit"), "inp_1")
		.appendField(" options")
		.appendField(new Blockly.FieldTextInput("edit"), "inp_2")
		.appendField(new Blockly.FieldImage(configuration_image, 16, 16, "*", edit_primitive))		;
	this.setColour("#2196f3");
	this.setOutput(true,['action']);

	this.setTooltip("move the shoulders");
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
		.appendField("Move arm")
		.appendField(new Blockly.FieldTextInput("edit"), "inp_1")
		.appendField(" options")
		.appendField(new Blockly.FieldTextInput("edit"), "inp_2")
		.appendField(new Blockly.FieldImage(configuration_image, 16, 16, "*", edit_primitive))		;
	this.setColour("#2196f3");
	this.setOutput(true,['action']);

	this.setTooltip("move the arms");
 	this.setHelpUrl("");
}};

Blockly.Blocks["elbow"] = {
init: function() {
	this.appendDummyInput()
		.appendField("Move elbow")
		.appendField(new Blockly.FieldTextInput("edit"), "inp_1")
		.appendField(" options")
		.appendField(new Blockly.FieldTextInput("edit"), "inp_2")
		.appendField(new Blockly.FieldImage(configuration_image, 16, 16, "*", edit_primitive))		;
	this.setColour("#2196f3");
	this.setOutput(true,['action']);

	this.setTooltip("move the arms");
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

Blockly.Blocks["human_detected"] = {
init: function() {
	this.appendDummyInput()
		.appendField("Human detected (camera)")
		.appendField(new Blockly.FieldTextInput("edit"), "inp_1")
		.appendField(new Blockly.FieldImage(configuration_image, 16, 16, "*", edit_primitive))		;
	this.setColour("#009688");
	this.setOutput(true,['condition']);

	this.setTooltip("Is human detected with the camera?");
		this.setHelpUrl("");
}};

Blockly.Blocks["posture_change"] = {
init: function() {
	this.appendDummyInput()
		.appendField("Posture change detected (camera)")
		.appendField(new Blockly.FieldTextInput("edit"), "inp_1")
		.appendField(new Blockly.FieldImage(configuration_image, 16, 16, "*", edit_primitive))		;
	this.setColour("#009688");
	this.setOutput(true,['condition']);

	this.setTooltip("Has the body in frame changed posture?");
		this.setHelpUrl("");
}};

Blockly.Blocks["movement_detected"] = {
init: function() {
	this.appendDummyInput()
		.appendField("Movement detected (camera)")
		.appendField(new Blockly.FieldTextInput("edit"), "inp_1")
		.appendField(new Blockly.FieldImage(configuration_image, 16, 16, "*", edit_primitive))		;
	this.setColour("#009688");
	this.setOutput(true,['condition']);

	this.setTooltip("Has the body in frame moved?");
		this.setHelpUrl("");
}};

Blockly.Blocks["posture_detected"] = {
init: function() {
	this.appendDummyInput()
		.appendField("Bad posture detected (camera)")
		.appendField(new Blockly.FieldTextInput("edit"), "inp_1")
		.appendField(new Blockly.FieldImage(configuration_image, 16, 16, "*", edit_primitive))		;
	this.setColour("#009688");
	this.setOutput(true,['condition']);

	this.setTooltip("Does the body in frame have bad posture?");
		this.setHelpUrl("");
}};

Blockly.Blocks["prolonged_sitting"] = {
init: function() {
	this.appendDummyInput()
		.appendField("Prolonged sitting detected (camera)")
		.appendField(new Blockly.FieldTextInput("edit"), "inp_1")
		.appendField(new Blockly.FieldImage(configuration_image, 16, 16, "*", edit_primitive))		;
	this.setColour("#009688");
	this.setOutput(true,['condition']);

	this.setTooltip("Has the body in frame sat for an extended period of time?");
		this.setHelpUrl("");
}};

Blockly.Blocks["sidestep"] = {
init: function() {
	this.appendDummyInput()
		.appendField("Side step")
		.appendField(new Blockly.FieldTextInput("edit"), "inp_1")
		.appendField(" options")
		.appendField(new Blockly.FieldTextInput("edit"), "inp_2")
		.appendField(new Blockly.FieldImage(configuration_image, 16, 16, "*", edit_primitive))		;
	this.setColour("#2196f3");
	this.setOutput(true,['action']);

	this.setTooltip("Make robot walk sideways");
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