
function open_image_upload_div(){
    var a = document.getElementById("all-fileds");
    var c = document.createElement('div');
    a.appendChild(c).classList.add("input-wrapper");
    var d = document.createElement('div');
    c.appendChild(d).classList.add("upload-wrapper");
    var e = document.createElement('label');
    d.appendChild(e);
    var f = document.createElement('h3');
    e.appendChild(f).innerHTML = "Drag image here or";
    var g = document.createElement('i');
    e.appendChild(g).classList.add("fa");
    g.classList.add("fa-upload");
    var h = document.createElement('input');
    h.setAttribute("type" , "file");
    h.setAttribute("name" , "image_file" );
    h.setAttribute("id" , "file-input");
    h.setAttribute("required","");
    e.appendChild(h);
    var i = document.createElement('h4');
    e.appendChild(i);
    i.innerHTML = "Upoload here";

    var a1 = document.getElementsByClassName("img-snap-conatiner")[0];
    var b1 = document.createElement('div');
    a1.appendChild(b1).classList.add("image-snappart");
    var c1 = document.createElement('div');
    b1.appendChild(c1).classList.add("image-snap");
}


function open_video_upload_div(){
    var a = document.getElementById("all-fileds");
    var c = document.createElement('div');
    a.appendChild(c).classList.add("input-wrapper");
    var d = document.createElement('div');
    c.appendChild(d).classList.add("upload-wrapper");
    var e = document.createElement('label');
    d.appendChild(e);
    var f = document.createElement('h3');
    e.appendChild(f).innerHTML = "Drag video here or";
    var g = document.createElement('i');
    e.appendChild(g).classList.add("fa");
    g.classList.add("fa-upload");
    var h = document.createElement('input');
    h.setAttribute("type" , "file");
    h.setAttribute("name", "video_file");
    h.setAttribute("id" , "file-input");
    h.setAttribute("required","");
    e.appendChild(h);
    var i = document.createElement('h4');
    e.appendChild(i);
    i.innerHTML = "Upload here";

    var a1 = document.getElementsByClassName("img-snap-conatiner")[0];
    var b1 = document.createElement('div');
    a1.appendChild(b1).classList.add("image-snappart");
    var c1 = document.createElement('div');
    b1.appendChild(c1).classList.add("image-snap");
}

function create_text_area(){
    var a = document.getElementById("all-fileds");
    var b = document.createElement('div');
    a.appendChild(b).classList.add("text-wrapper")
    var c = document.createElement("div");
    b.appendChild(c).classList.add("text-editor-anotations");
    var d =document.createElement('i');
    c.appendChild(d).classList.add("fa");
    d.classList.add("fa-bold");
    var e =document.createElement('i');
    c.appendChild(e).classList.add("fa");
    e.classList.add("fa-underline");
    var f =document.createElement('i');
    c.appendChild(f).classList.add("fa");
    f.classList.add("fa-italic");
    var g = document.createElement("div");
    b.appendChild(g).classList.add("text-editor");
    g.setAttribute("contenteditable","true");
}

function textLength1(value){
    var maxlength = 100;
    if (value.length >= maxlength) return false;
    return true;
}

function textLength2(value){
    var maxlength = 250;
    if (value.length >= maxlength) return false;
    return true;
}

 var oldValue = '';
 document.getElementsByClassName('lc_count')[0].children[0].onkeyup = function(){
    document.getElementsByClassName('lc_count')[0].children[1].innerHTML =   document.getElementsByClassName('lc_count')[0].children[0].value.length +"/100";   
    if(!textLength1(this.value))
    {
        this.value = oldValue;  
    }
    else  oldValue = this.value;
 }

 var oldValue2 = '';
 document.getElementsByClassName('lc_count')[1].children[0].onkeyup = function(){
    document.getElementsByClassName('lc_count')[1].children[1].innerHTML =   document.getElementsByClassName('lc_count')[1].children[0].value.length +"/250";   
    if(!textLength2(this.value))
    {
        this.value = oldValue2;  
    }
    else  oldValue2 = this.value;
 }