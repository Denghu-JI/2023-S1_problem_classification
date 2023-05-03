
//record of position--------------------------------------------
const pos_nodes_node = new Map(); //record of whole node
const pos_nodes_des = new Map(); //record of descript buttons
const pos_nodes_finddoc = new Map(); //record of documentaiton buttons
const pos_nodes_findgit = new Map(); //record of gitpath buttons
const pos_func_buttons = new Map();

const offset_node_mouse = new Map();
const descriptions = new Map();

var pos_sidebar
var pending_centered
var to_be_centered
var current_des
var other_task
var tree
var current_tree
//----------------------------------------------------------------

function preload() {
  tree = loadJSON('https://jsonofthetree.s3.ap-southeast-2.amazonaws.com/data.json');

}

function basicSetup() {
  canvas_width = 850;
  canvas_height = 400;
}

function setup() {
  for (const [name, [x, y, depth, parentIndex]] of Object.entries(tree)) {
    pos_nodes_node.set((name), [x,y,0,0])
  }
  // Set up the canvas
  basicSetup();
  let myCanva = createCanvas(canvas_width, canvas_height);
  myCanva.parent('my_canva_parent');
  
  // color table--------------------------
  main_background_color = color('#e6f2ff');
  main_sidebar_color1 = color('#99d6ff')
  main_sidebar_color2 = color('#ffffcc')
  main_sidebar_color3 = color('#d9ffb3')

  main_waiting_color = color(0,0,0);
  node_color_1 = color('#ccffcc')
  node_color_2 = color('#ffffcc')
  node_button_color = color('#d9ffb3')
  buttom_buttons_color = color('#ccccff')
  // color table end here-----------------

  //dim table--------------------------
  node_width = 120
  node_height = 40
  //function table--------------------
  dragging = 0
  center_step = 100
  centering = 0
  sidebar_step = 30
  sidebar_flag = 0
  sidebar_open = 0
  sidebar_close = 1
  to_be_centered = 'scipy.linalg.lstsq'
  //-------testing setup----
  // pos_nodes_node.set('scipy.linalg.lstsq',[120,120,0,0])
  // pos_nodes_node.set('pytorch.optim',[500,120,0,0])
  // pos_nodes_node.set('test.node.test', [350,300,0,0])
  descriptions.set('scipy.linalg.lstsq', 'this is a des for scipy.linalg.lstsq')
  descriptions.set('pytorch.optim', 'this is a asdasdasd aksjdna askjdsq')
  descriptions.set('test.node.test', 'test test 123 123')
  current_des = 'scipy.linalg.lstsq'
  if (windowWidth < 945) {
    canvas_width = windowWidth
  } else {canvas_width = 945}
  pos_sidebar = [canvas_width ,canvas_height * 0.1]
  tree = loadJSON('https://jsonofthetree.s3.ap-southeast-2.amazonaws.com/data.json')
  current_tree = 'CoFI'

}

function draw() {
  // Display the mermaid diagram as an SVG image
  if (windowWidth < 945) {
    canvas_width = windowWidth
  } else {canvas_width = 945}
  resizeCanvas(canvas_width,canvas_height)
  centernode_animation()
  fill(main_background_color)
  stroke(main_background_color);
  rect(0,0,canvas_width,canvas_height)
  //-------waiting theme-------------
  draw_nodes()
  sidebar(0.3, 0.7, main_sidebar_color1, main_sidebar_color2, main_sidebar_color3)
  bottombar(0.9, main_sidebar_color2)
  wait_theme(255,100)
  fill(0)
  // text(pos_nodes_des.get('CoFI'), 50,50)
  // text(sidebar_flag,50,70)
  // text(sidebar_step,50,90)
  // text(pos_func_buttons.get('hide_sidebar'),50,110)
  text(to_be_centered,50,50)


}


function wait_theme(bg_color, transparent) {
  if (!document.hasFocus()) {
    fill(bg_color,bg_color,bg_color,transparent);
    stroke(255);
    rect(0,0,canvas_width,canvas_height)
  }
}
//---------------sidebar implementation
function sidebar(startdimh, startdimv, color1, color2, color3) {
  let front_size = 22
  fill(color1)
  stroke(color1)
  rect(pos_sidebar[0], pos_sidebar[1], canvas_width * startdimh, canvas_height * startdimv)
  fill(color2)
  stroke(color2)
  rect(pos_sidebar[0], pos_sidebar[1] + canvas_height * startdimv * 0.2, canvas_width * startdimh, canvas_height * startdimv * 0.8)
  fill(color3)
  stroke(color3)
  rect(pos_sidebar[0] + canvas_width * startdimh * 0.3, pos_sidebar[1] + canvas_height * startdimv * 0.85, canvas_width * startdimh * 0.3, canvas_height * startdimv * 0.1)
  pos_func_buttons.set('hide_sidebar', [pos_sidebar[0] + canvas_width * startdimh * 0.3, pos_sidebar[1] + canvas_height * startdimv * 0.85, pos_sidebar[0] + canvas_width * startdimh * 0.3 + canvas_width * startdimh * 0.3, canvas_height * startdimv * 0.1 + pos_sidebar[1] + canvas_height * startdimv * 0.85])
  fill(75)
  textSize(front_size)
  text('Hide', pos_sidebar[0] + canvas_width * startdimh * 0.3 + front_size * 0.6, pos_sidebar[1] + canvas_height * startdimv * 0.85 + front_size * 0.05, canvas_width * startdimh * 0.4, canvas_height * startdimv * 0.1)

  if (current_des) {
    let front_size = 22
    let body_size = 20
    fill(0)
    textSize(front_size)
    text(current_des,pos_sidebar[0] + front_size*0.6, pos_sidebar[1] + front_size * 1.2)
    textSize(body_size)
    text(descriptions.get(current_des),pos_sidebar[0] + body_size*0.6, pos_sidebar[1] + canvas_height * startdimv * 0.2 + body_size * 1.2, canvas_width * startdimh, canvas_height * startdimv * 0.8)
  }
  if (sidebar_flag === 1) {
    sidebar_sliding(startdimh)
    sidebar_step = sidebar_step - 1
    if (sidebar_step === 0) {
      sidebar_step = 30
      sidebar_flag = 0
    }
  }
}
function sidebar_sliding(startdimh) {
  if (sidebar_open === 1) {
    if (pos_sidebar[0] > canvas_width * (1 - startdimh)) {
      pos_sidebar[0] -= 10
    }
  }
  if (sidebar_open === 0) {
    if (pos_sidebar[0] < canvas_width) {
      pos_sidebar[0] += 10
    }
  }
}
//----------------------------------------------------------------------------
function bottombar(startdimv, color) {
  fill(color)
  stroke(color);
  rect(0, canvas_height * startdimv, canvas_width,canvas_height * (1 - startdimv))
  buttom_buttons(startdimv)
}

function buttom_buttons(startdimv) {
  let offsetX = canvas_width * 0.02
  let offsetY = canvas_height * (startdimv * 1.01)
  let h = canvas_height - offsetY - (offsetY - canvas_height * startdimv)
  let w = canvas_width * 0.25 - 2 * offsetX
  let textsize = 22
  //-------------button pos calculation
  let x1 = offsetX
  let x2 = offsetX+ canvas_width * 0.25
  let x3 = offsetX+ canvas_width * 0.5
  let x4 = offsetX+ canvas_width * 0.75
  let y = offsetY
  fill(buttom_buttons_color)
  stroke(buttom_buttons_color)
  rect(x1, y, w, h)
  rect(x2, y, w, h)
  rect(x3, y, w, h)
  rect(x4, y, w, h)
  //button pos reg----------
  pos_func_buttons.set('return to top',[x1, y, x1 + w, y + h])
  pos_func_buttons.set('CoFI',[x2, y, x2 + w, y + h])
  pos_func_buttons.set('Espresso',[x3, y, x3 + w, y + h])
  pos_func_buttons.set('Examples',[x4, y, x4 + w, y + h])
  //------------------------
  fill(0)
  // stroke(0)
  textSize(textsize)
  let textoffsetX = textsize * 0.6
  let textoffsetY = textsize * 0.15
  
  text('return to top',textoffsetX + x1, textoffsetY + y, w, h)
  text('CoFI',textoffsetX + x2, textoffsetY + y, w, h)
  text('Espresso', textoffsetX + x3, textoffsetY + y, w, h)
  text('Examples', textoffsetX + x4, textoffsetY + y, w, h)

  // pos_func_buttons.set('return to top',[textoffsetX + offsetX, textoffsetY + offsetY, textoffsetX + offsetX + canvas_width * 0.25 - 2 * offsetX, w + textoffsetY + offsetY])
  // pos_func_buttons.set('CoFI',[textoffsetX + offsetX+ canvas_width * 0.25, textoffsetY + offsetY, canvas_width * 0.25 - 2 * offsetX, w])
  // pos_func_buttons.set('Espresso',[textoffsetX + offsetX, textoffsetY + offsetY, textoffsetX + offsetX + canvas_width * 0.25 - 2 * offsetX, w + textoffsetY + offsetY])
  // pos_func_buttons.set('Examples',[textoffsetX + offsetX, textoffsetY + offsetY, textoffsetX + offsetX + canvas_width * 0.25 - 2 * offsetX, w + textoffsetY + offsetY])
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
  let textsize = 20;
  let req_width = textsize * content.length * 0.6;
  if (req_width < 220) {
    req_width = 220
  }
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
  text('description', x + node_width * 0.05 + textsize * 0.5, y + node_height * 1.2 + textsize*0.9 )
  text('find in github', x + node_width * 0.05 + textsize * 0.5, y + node_height * 1.8 + textsize*0.9 )
  text('find in offical doc', x + node_width * 0.05 + textsize * 0.5, y + node_height * 2.4 + textsize*0.9 )
}

//Table movement-------------------------
function center_node(target_content) {
    let target_x = canvas_width / 2 - 150
    let target_y = canvas_height / 2  - 150
    let node_pos = pos_nodes_node.get(target_content)
    let x_placement = target_x - node_pos[0]
    let y_placement = target_y - node_pos[1]
    for (let [content, position] of pos_nodes_node) {
    pos_nodes_node.set(content, [position[0] + (x_placement/3), position[1] + (y_placement/3), 0, 0])
  }
}

function centernode_animation() {
  if (centering === 1 && to_be_centered != '') {
    center_step = center_step - 1
    center_node(to_be_centered)
    if (center_step === 0) {
      centering = 0
      to_be_centered = ''
    }
  }
}
//---------------------------------------

//Event Handler---------------------------
function mousePressed() {
  dragging = 0
  for (let [content, position] of pos_func_buttons) {
    if (mouseX > position[0] && mouseY > position[1] && mouseX < position[2] && mouseY < position[3]) {
      if (content === 'hide_sidebar' && sidebar_open === 1) {
        sidebar_open = 0
        sidebar_flag = 1
        return
      } 
      if (content === 'return to top') {
        to_be_centered = current_tree
        center_step = 30
        return
      } 
    }
  }
  for (let [content, position] of pos_nodes_node) {
    if (mouseX > position[0] && mouseY > position[1] && mouseX < position[2] && mouseY < position[3]) {
      let description_pos = pos_nodes_des.get(content)
      if (mouseX > description_pos[0] && mouseY > description_pos[1] && mouseX < description_pos[2] && mouseY < description_pos[3]) {
        current_des = content
        if (sidebar_open === 0) {
          sidebar_flag = 1
          sidebar_open = 1
          return
        }
      } else{
        other_task = 0
        to_be_centered = content
        center_step = 30
      }
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
