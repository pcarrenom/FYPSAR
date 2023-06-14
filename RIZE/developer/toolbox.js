var toolbox = '<xml id="toolbox" style="display: none">';

toolbox += '<category name="Set event triggers" colour="#009688">'
toolbox += '<block type="lists_and"></block>';
toolbox += '<block type="lists_or"></block>';
toolbox += '    <block type="touched"></block>';
toolbox += '    <block type="human_detected"></block>';
toolbox += '    <block type="posture_change"></block>';
toolbox += '    <block type="posture_detected"></block>';
toolbox += '    <block type="prolonged_sitting"></block>';
toolbox += '  </category>';

toolbox +='<sep></sep>';
toolbox +='<category name="Action builder" colour="#3373CC">'
toolbox +='<block type="do_action"></block>';
toolbox +='<block type="lists_create_with"></block>';
toolbox +='</category>';

toolbox += '<category name="Set robot actions" colour="#2196f3">'
toolbox +='    <block type="wait"></block>';
toolbox +='    <block type="say"></block>';
toolbox +='    <block type="walk"></block>';
toolbox +='    <block type="shoulder"></block>';
toolbox +='    <block type="stretch"></block>';
toolbox +='    <block type="leg"></block>';
toolbox +='    <block type="arm"></block>';
toolbox +='    <block type="elbow"></block>';
toolbox +='    <block type="turn"></block>';
toolbox +='    <block type="mode"></block>';
toolbox +='    <block type="sidestep"></block>';
toolbox +='    <block type="reset"></block>';
toolbox += '  </category>';

toolbox +='<sep></sep>';
toolbox += '<category name="Modules"  colour="#2E7D32">'
toolbox +='<block type="do_module"></block>';
toolbox +='</category>';

toolbox += '<sep></sep>';
toolbox += '<category name="Select behaviors"  colour="#424242">'
toolbox += '<block type="selector"></block>';
toolbox += '<block type="check_perception"></block>';
toolbox += '</category>';

toolbox +='<sep></sep>';
toolbox += '</xml>';