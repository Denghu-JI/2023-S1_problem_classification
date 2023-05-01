
//record of position--------------------------------------------
const pos_nodes_node = new Map(); //record of whole node
const pos_nodes_des = new Map(); //record of descript buttons
const pos_nodes_finddoc = new Map(); //record of documentaiton buttons
const pos_nodes_findgit = new Map(); //record of gitpath buttons

const offset_node_mouse = new Map();
var to_be_centered
//----------------------------------------------------------------

function preload() {
  tree = loadJSON('data.json');
}

function basicSetup() {
  canvas_width = 1000;
  canvas_height = 500;
}

function setup() {
  // Set up the canvas
  basicSetup();
  createCanvas(canvas_width, canvas_height);
  // color table--------------------------
  main_background_color = color('#e6f2ff');
  main_sidebar_color = color('#99d6ff')
  main_waiting_color = color(0,0,0);
  node_color_1 = color('#ccffcc')
  node_color_2 = color('#ffffcc')
  node_button_color = color('#d9ffb3')
  // color table end here-----------------

  //dim table--------------------------
  node_width = 120
  node_height = 45
  //function table--------------------
  dragging = 0
  center_step = 100
  centering = 0
  //-------testing setup----
  pos_nodes_node.set('scipy.linalg.lstsq',[120,120,0,0])
  pos_nodes_node.set('pytorch.optim',[500,120,0,0])

}

function draw() {
  // Display the mermaid diagram as an SVG image
  centernode_animation()
  fill(main_background_color)
  stroke(main_background_color);
  rect(0,0,canvas_width,canvas_height)
  //-------waiting theme-------------
  draw_nodes()
  bottombar(0.9, main_sidebar_color)
  wait_theme(255,100)
}


function wait_theme(bg_color, transparent) {
  if (!document.hasFocus()) {
    fill(bg_color,bg_color,bg_color,transparent);
    stroke(255);
    rect(0,0,canvas_width,canvas_height)
  }
}

function sidebar(startdimh, color) {
  fill(color)
  stroke(color);
  rect(canvas_width * startdimh, 0, canvas_width * (1 - startdimh),canvas_height)
}

function bottombar(startdimv, color) {
  fill(color)
  stroke(color);
  rect(0, canvas_height * startdimv, canvas_width,canvas_height * (1 - startdimv))
}


//---------------------------------- node
function draw_nodes() {
  for (let [content, position] of pos_nodes_node) {
    draw_node(content, node_color_1, node_color_2)
  }
}

function draw_node(content, color1, color2) {
  let x = pos_nodes_node.get(content)[0]
  let y = pos_nodes_node.get(content)[1]
  let textsize = 25;
  let req_width = textsize * content.length * 0.6;
  fill(color1);
  stroke(color1);
  draw_soft_rect_up(x,y,req_width,node_height,10)

  fill(0);
  textSize(textsize);
  text(content, x + textsize * 0.6, y + textsize * 1.2) ;
  fill(color2);
  stroke(color2);
  draw_soft_rect_down(x,y + node_height,req_width,node_height * 2,10);
  fill(node_button_color)
  buttons(content, x, y, req_width, node_height,15)
  pos_nodes_node.set(content,[x,y,x + req_width, y + 3 * node_height])
}

function draw_soft_rect(x, y, width, height, dim) {
  rect(x + dim, y, width - 2 * dim , height)
  rect(x, y + dim, width, height - 2 * dim)
  circle(x + dim, y + dim, 2 * dim)
  circle(x + width - dim, y + dim, 2 * dim)
  circle(x + dim, y + height - dim, 2 * dim)
  circle(x + width - dim, y + height - dim, 2 * dim)
}

function draw_soft_rect_down(x, y, width, height, dim) {
  rect(x + dim, y, width - 2 * dim , height)
  rect(x, y, width, height - dim)
  circle(x + dim, y + height - dim, 2 * dim)
  circle(x + width - dim, y + height - dim, 2 * dim)
}

function draw_soft_rect_up(x, y, width, height, dim) {
  rect(x + dim, y, width - 2 * dim , height)
  rect(x, y + dim, width, height - dim)
  circle(x + dim, y + dim, 2 * dim)
  circle(x + width - dim, y + dim, 2 * dim)
  circle(x + dim, y + height - dim, 2 * dim)
  circle(x + width - dim, y + height - dim, 2 * dim)
}

function buttons(content, x,y, node_width, node_height, textsize) {
  if (node_width < 220) {node_width = 250}
  let x1 = x + node_width * 0.05
  let y1 = y + node_height * 1.2
  let n1 = node_width * 0.6
  let h1 = node_height * 0.5
  rect(x1, y1, n1, h1)
  pos_nodes_des.set(content,[x1, y1, x1 + n1, y1 + h1])
  let x2 = x + node_width * 0.05
  let y2 = y + node_height * 1.8
  let n2 = node_width * 0.6
  let h2 = node_height * 0.5
  rect(x2, y2, n2, h2)
  pos_nodes_findgit.set(content,[x2, y2, x2 + n2, y2 + h2])
  let x3 = x + node_width * 0.05
  let y3 = y + node_height * 2.4
  let n3 = node_width * 0.6
  let h3 = node_height * 0.5
  rect(x3, y3, n3, h3)
  pos_nodes_findgit.set(content,[x3, y3, x3 + n3, y3 + h3])
  fill(0)
  textSize(textsize)
  text('description', x + node_width * 0.05 + textsize * 0.6, y + node_height * 1.2 + textsize )
  text('find in github', x + node_width * 0.05 + textsize * 0.6, y + node_height * 1.8 + textsize )
  text('find in offical doc', x + node_width * 0.05 + textsize * 0.6, y + node_height * 2.4 + textsize )
}

//Table movement-------------------------
function center_node(target_content) {
  let target_x = canvas_width / 2 - 150
  let target_y = canvas_height / 2  - 150
  let node_pos = pos_nodes_node.get(target_content)
  let x_placement = target_x - node_pos[0]
  let y_placement = target_y - node_pos[1]
  for (let [content, position] of pos_nodes_node) {
    pos_nodes_node.set(content, [position[0] + (x_placement/5), position[1] + (y_placement/5), 0, 0])
  }
}

function centernode_animation() {
  if (centering === 1) {
    center_step = center_step - 1
    center_node(to_be_centered)
    if (center_step === 0) {
      centering = 0
    }
  }
}
//---------------------------------------

//Event Handler---------------------------
function mousePressed() {
  dragging = 0
  for (let [content, position] of pos_nodes_node) {
    if (mouseX > position[0] && mouseY > position[1] && mouseX < position[2] && mouseY < position[3]) {
      to_be_centered = content
      center_step = 30
    }
  }
  for (let [content, position] of pos_nodes_node) {
    let offsetX = position[0] - mouseX
    let offsetY = position[1] - mouseY
    offset_node_mouse.set(content, [offsetX, offsetY])
    }
  }

function mouseReleased() {
  if (!dragging){
    center_step = 30
    centering = 1
  }
}
 
function mouseDragged() {
  dragging = 1
  for (let [content, position] of pos_nodes_node) {
    let offsetX = offset_node_mouse.get(content)[0]
    let offsetY = offset_node_mouse.get(content)[1]
    pos_nodes_node.set(content, [offsetX + mouseX, offsetY + mouseY, 0, 0])
  }
}
